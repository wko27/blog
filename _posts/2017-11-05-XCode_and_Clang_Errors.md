---
layout: post
unique_id: xcode-clang
title: XCode and Clang Errors
categories: []
locations: 
---

Spent ~6 hours on this today, so figures it deserves a post ... the original start of this whole fiasco was introducing one extra dependency for react-native-version-info.  There's absolutely nothing wrong with that particular library, in fact I had that up and running perfectly within minutes on Android.  For some reason, my iOS build failed to compile with an error caused by recursive expansion of a search header path from a completely different dependency, react-native-fcm:

```
Argument list too long: recursive header expansion failed
```

After trying various quick-fixes from stack overflow and GitHub issues, I sat down to figure out exactly what's going on here ...

Before we dive in, I'll cover some brief terminology in case my readers are unfamiliar with iOS projects. In XCode, one can add native iOS dependencies via *Cocoapods** (or just Pods).  Each dependency is declared in a **Podfile** and has a corresponding sub-directory in a **Pods** folder.  Each dependency also becomes a sub-project in the XCode workspace and can have its own configurable build dependencies and targets.

In Objective-C, we have two ways to include files from other directores.  A **local include** is quoted, e.g. include "foo/bar.h", and a **global include** is surrounded by angle brackets, e.g. include <foo/bar.h>.

In XCode, we specify the directories where these headers can be found via "Header Search Paths" (for local) and "Framework Search Paths" (for global) from the "Build Settings" menu.  When creating a path, one can specify if the path is "recursive" or "not recursive".  By default, the react-native-fcm project had a recursive Header Search Path which searched the entire Pods directory, basically looking for headers from any dependency.  By adding a new dependency, we added a new sub-directory to the **Pods** folder and apparently the glob expansion of directories overcame a limit on the number of allowed arguments to Clang.

Ok, so easy fix, we just figure out which particular Pods this react-native-fcm thing relies on and add those directly, right?

Well, I did this and cleaned (force cleaned by deleting DerivedData directory which can be found in File => Workplace Settings), and rebuilt a bunch of times.  However, for some reason one of my headers was missing.  Turns out the required header was a global include and thus needed to be passed via "Framework Search Paths".

The solution in this case seems pretty trivial, but the process of figuring out was a bit fun:

I'm a big fan of taking something that doesn't work with something that does work and figuring out the difference between them.

So, first step was to find a working, building example of react-native-fcm without any other dependencies.  We then build that target successfully and compare the underlying clang paramters calls of the failing version against the working version.

In XCode, once you hit a build error, there's a lovely log of the exact command that failed to run.  In addition, you can see the log output of successful builds via Views => Navigators => Report Navigator.

The clang call itself should look something like:

```
/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang ...
```

XCode nicely includes the directory where this should run as well, so you can test in a terminal to reproduce the success/failure of the command.

Since there's ~150 parameters passed to Clang from XCode, we stuff it into a text editor and replace spaces with newlines.  Now we diff for differences and copy and paste them back together.  Note that the local header directories are passed to Clang via the -I flag and framework header directories are passed via -F flag.

Tiny one-liner to assist with joining our parameters back into a command that we can test:

```
$( cat /tmp/tmp1.txt | tr -d '\n' )
```

Then, we just copy and paste parameters back and forth between the working and non-working one until we see exactly which flags we were missing :)

For more reading:
 * [Apple's documentation on includes](https://developer.apple.com/library/content/documentation/MacOSX/Conceptual/BPFrameworks/Tasks/IncludingFrameworks.html)

