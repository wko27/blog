---
layout: post
unique_id: ayce_sushi
title: AYCE Sushi
categories: []
locations: 
---

YESTERDAY:
* power yoga in the morning
* leftovers for lunch
* hike!
* correctly got two more UDIDs
* all-you-can-eat sushi at Kenzo
  * overdid it xD
*

TODAY:
* decided my hack for handling Gmail by forwarding to a web UI was bad
  * ended up figuring out how to create new email threads
  * refactored my entire new conversation thread UI layer and cleaned up a bunch of code
* finally added a conversation consistency check and sanitized my database
* bit of data analysis
  * sensor maxes out :( needs more testing

LEARNINGS:
* much easier to manipulate maps in javascript than java
* base64 encoding libraries on npm all assume it's running on server-side with nodejs
  * Buffer isn't available in the react-native runtime
  * have to use a global hack + npm install buffer to get this working <.<
* grr, just discovered Gmail API doesn't allow automatically adding labels to sent emails
  * I'll have to do some trickery to get around this ...
  * maybe use a custom header?
  * sleep first though xD
