---
layout: post
unique_id: san_jose_rock_n_roll
title: San Jose Rock n Roll
categories: []
locations: 
---

YESTERDAY:
* Thousand Tasty in Milpitas for lunch!
  * bought two sacks of frozen dumplings
* guitar teacher contacted me using MyStache! :D
* yoga
* helped Brian break into a house and steal a car (totally legal, no worries)
* Falafel Stop for dinner

TODAY:
* san jose rock n roll half marathon!
  * hurt my knee, so I walked the last 3 miles :p
  * R8 roll recovery + two hour nap and it's all good
* korean bowl for lunch
* dinner with the sis
* debugged why my Firebase event handler wasn't firing!
* got self-registration almost fully working :D

LEARNINGS:
* in Firebase's Java SDK, all the event handlers are handled on the same thread
  * this means specifically that you can very easily deadlock if attempting to do synchronous writes within an event handler
    * e.g. on child changed, update a different ref and wait for the completion handler for the update to fire
  * my fix to this is to update my little wrapper library to use a separate thread and a blocking queue to ensure that we don't block the event handler from completing
  * should probably open source this at some point ...
* also figured out the difference between Firebase's `on('child_changed')` and `on('value')`
  * basically, only use `on('child_changed')` if somebody is pushing new values into the ref
  * otherwise, if e.g. two children get updated, you have to handle it in two different events
  * if you use `on('value')` to wait for a specific change, you can wrap in a promise like this:

```
new Promise((resolve, reject) => {
  ref.on('value', snapshot => {
    const { status, statusReason } = snapshot.val();
    switch (status) {
      case "FAILED":
        reject(Error(statusReason));
        ref.off();
      case "SENT":
        resolve();
        ref.off();
      default:
        // Continue waiting for status to change
  };
});
```
