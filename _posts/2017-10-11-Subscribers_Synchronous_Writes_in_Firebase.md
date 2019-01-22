---
layout: post
unique_id: firebase_subscribers_synchronous_writes
title: Subscribers and Synchronous Writes in Firebase
categories: [technical]
locations: 
---

This post focuses on the [Firebase Admin Java API](https://github.com/firebase/firebase-admin-java) which we use to build services to support our app.

In my [previous post]({{ site.baseurl }}/Synchronous_Writes_in_Firebase), we covered use cases that need synchronous writes and how to implement them with the Firebase API.  There are some subtleties when using synchronous writes though!

Firebase provides the useful ability to add listeners for changes to various parts of the tree.  For example:

```
ref.addChildEventListener(new ChildEventListener() {
    @Override public void onChildAdded(DataSnapshot snapshot, String previousChildName) {
        // do stuff here
    }
    
    // methods overridden with no-ops omitted here
}
```

The `DataSnapshot` is an immutable snapshot of the entire subtree for the newly added child.  Our listener is called whenever a child changes, and we can override other methods in the `ChildEventListener` interface to watch for deletions, changes, etc.

This is useful, but which thread does that code run in?

It turns out this runs in the Firebase worker thread.  However, this is the SAME thread that is used to trigger the `CompletionListener` callback for writes/reads/updates.  This can easily lead to deadlock issues which we'll illuminate with a practical example:

Suppose every time a child changes in refA, we want a `synchronous write` to refB.

Here's the synchronousWrite method from before:
```
public void synchronousWrite(DatabaseReference ref, Object value) {
    CountDownLatch latch = new CountDownLatch(1);
    AtomicReference<DatabaseError> error = new AtomicReference<>();
    ref.write(
        value,
        (error, ref2) => {
    	    error.set(databaseError);
            latch.countDown();
        }
    );

    latch.await(TIMEOUT_DURATION, TimeUnit.SECONDS);

    if (error.get() != null) {
        throw IllegalStateException("sadness", error.get().toException());
    }
}
```

Here's how we would implement our desired logic:

```
refA.addChildEventListener(new ChildEventListener() {
    @Override public void onChildAdded(DataSnapshot snapshot, String previousChildName) {
        synchronousWrite(snapshot);
    }
}
```

What happens here?  Let's call our Firebase worker thread T.  Then, the sequence is:
* something creates a new child in refA
* T calls our `onChildAdded` method
* T calls our `synchronousWrite` method
* T calls the asynchronous `write` method
* T waits until the latch counts down

However, the latch never counts down because the `CompletionListener` can't fire since it is suppose to run in T!!

The actual problem here is that Firebase is using the same thread for firing child events and completion events.

To solve this, we need to ensure that we NEVER block in a listener.  This is a difficult constraint to enforce if you just use the default Firebase API though since your method deep in the stack may not know it was invoked from within a `ChildEventListener`.

My solution was to create a utility method which:
* creates a `BlockingQueue` and an `Executor`
* adds a listener which simply adds events to the queue
* spawns a single thread which processes events from the queue

The implementation looks like this (I use a bounded queue to ensure we fail if the service isn't able to keep up with handling updates).

```
import java.util.concurrent.ArrayBlockingQueue;
import java.util.concurrent.BlockingQueue;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import com.google.common.util.concurrent.ThreadFactoryBuilder;
import com.google.firebase.database.ChildEventListener;
import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.Query;

/**
 * Subscribes to events from a {@link DatabaseReference} and passes them
 * to a {@link BlockingQueue} consumed by a thread in a separate {@link Executor}
 * <p>
 *
 * This is used to avoid handling child events in the default Firebase worker thread
 */
class OnChangeSubscriber {
    private static final Logger LOG = LoggerFactory.getLogger(OnChangeSubscriber.class);
    
    private static final int DEFAULT_QUEUE_CAPACITY = 1024 * 1024;
    
    private volatile boolean broken = false;
    
    private final String name;
    private final Query query;
    private final ChildEventListener listener;
    private final ArrayBlockingQueue<Event> queue;
    private final ExecutorService executor;
    
    private ChildEventListener delegatedListener;
    
    public OnChangeSubscriber(String name, Query query, ChildEventListener listener) {
        this.name = name;
        this.query = query;
        this.listener = listener;
        this.queue = new ArrayBlockingQueue<>(DEFAULT_QUEUE_CAPACITY);
        this.executor = Executors.newSingleThreadExecutor(
                new ThreadFactoryBuilder()
                        .setNameFormat(name + "-%d")
                        .setDaemon(true)
                        .build()
            );
    }
    
    /** Add the listener */
    public final void start() {
        this.delegatedListener = new ChildEventListener() {
            @Override public void onChildRemoved(DataSnapshot snapshot) {
                handle(Event.of(ChangeType.REMOVED, snapshot, null));
            }
            
            @Override public void onChildMoved(DataSnapshot snapshot, String previousChildName) {
                handle(Event.of(ChangeType.MOVED, snapshot, previousChildName));
            }
            
            @Override public void onChildChanged(DataSnapshot snapshot, String previousChildName) {
                handle(Event.of(ChangeType.CHANGED, snapshot, previousChildName));
            }

            @Override public void onChildAdded(DataSnapshot snapshot, String previousChildName) {
                handle(Event.of(ChangeType.ADDED, snapshot, previousChildName));
            }
            
            @Override public void onCancelled(DatabaseError error) {
                handle(Event.cancelled(error));
            }
        };
        LOG.info("Adding child event listener to " + query);
        this.query.addChildEventListener(this.delegatedListener);
        
        this.executor.execute(() -> {
            while (true) {
                Event event;
                try {
                    event = OnChangeSubscriber.this.queue.take();
                } catch (InterruptedException e) {
                    LOG.warn("Queue " + name + " interrupted while obtaining next event, aborting!", e);
                    break;
                }

                process(event);
            }
        });
    }
    
    /** Remove the listener */
    public final void stop() {
        this.query.removeEventListener(this.delegatedListener);
        this.delegatedListener = null;
    }
    
    private void process(Event event) {
        switch (event.type()) {
        case ADDED:
            this.listener.onChildAdded(event.snapshot(), event.previousChildName());
            return;
        case CANCELLED:
            this.listener.onCancelled(event.error());
            return;
        case CHANGED:
            this.listener.onChildChanged(event.snapshot(), event.previousChildName());
            return;
        case MOVED:
            this.listener.onChildMoved(event.snapshot(), event.previousChildName());
            return;
        case REMOVED:
            this.listener.onChildRemoved(event.snapshot());
            return;
        }
        
        throw new IllegalStateException("Unknown event type: " + event.type() + " and type is " + event.getClass().getName());
    }
    
    private void handle(Event event) {
        if (broken) {
            LOG.warn("Queue " + name + " is broken, ignoring: " + event.snapshot().getKey());
        }
        
        if (!this.queue.offer(event)) {
            broken = true;
            LOG.error("Queue " + name + " is full!!!! Restart service!!!");
            return;
        }
    }
    
    private enum ChangeType {
        ADDED,
        CANCELLED,
        CHANGED,
        MOVED,
        REMOVED,
    }
    
    private interface Event {
        ChangeType type();
        DataSnapshot snapshot();
        String previousChildName();
        DatabaseError error();
        
        static Event of(ChangeType type, DataSnapshot snapshot, String previousChildName) {
            return new Event() {
                @Override public ChangeType type() {
                    return type;
                }

                @Override public DataSnapshot snapshot() {
                    return snapshot;
                }

                @Override public String previousChildName() {
                    return previousChildName;
                }

                @Override public DatabaseError error() {
                    return null;
                }
            };
        }
    
        static Event cancelled(DatabaseError error) {
            return new Event() {
    
                @Override public ChangeType type() {
                    return ChangeType.CANCELLED;
                }
    
                @Override public DataSnapshot snapshot() {
                    return null;
                }
    
                @Override public String previousChildName() {
                    return null;
                }
    
                @Override public DatabaseError error() {
                    return error;
                }           
            };
        }
    }
}
```
