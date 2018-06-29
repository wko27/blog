---
layout: post
unique_id: frayed_knot
title: Frayed Knot
categories: []
locations: 
---

YESTERDAY:
* woke up and tried out my new ideas
  * turns out fixing a bug in the SDK + adding a 250 usec delay into my code gets 2048 byte writes to flash working, hooray!
  * manually controlling slave select pin to do sequential (programmatically controlled) SPI transfers did not work though
* simple lunch at home
* put everything together to test and ... things kind of broke?
  * oddly enough, a validation check on the read-only parameter page caused my accelerometer interrupt handler to stop triggering
  * ended up in a red herring suspecting that the 250 usec delay was causing my accelerometer writes
    * suspecting that I'm not waiting for a STOPPED event after triggering a STOP task
  * eventually changed interrupt priorities to give accelerometer higher and it may have fixed it?
* went climbing with Knut to take a break
  * found a climb with a slightly damaged rope
  * staff was very thankful we reported it
  * saw Jenn Luu!!
* brought along Knut to meet up with hardware contractor before he goes on PTO
  * weirdly enough my code magically started working before their eyes
  * literally both the PPI and non-PPI code worked when I showed it to them
  * suspecting the interrupt priority fix made things work properly
* late night in n out for dinner

TODAY:
* woke up pretty late
* 
* figured out a bug in the example code (using a task address offset instead of a task itself)
* added a fix using a SWI (software interrupt) and an EGU (event generator unit) to wait for SPI stopped event
* debugged memory corruption issue
  * pretty sure the issue is that my accelerometer interrupt is causing extra SPI transfers during long flash reads/writes
  * should probably time the function to see exactly how long I have
  * would be nice if there was a short to send SPI stop task
* ok yoga
* dropped by Target (haven't done that in ages)
* baked chicken for dinner
  * too much salt, didn't sleep well
* researching for Detroit
  * so they have four yoga places nearby
  * one offers Christian guidance during your practice
  * one is specifically for getting high before/during/after practice
  * one only offers at most three classes a day
  * the last one thankfully looks more legit and has a new student discount ...

LEARNINGS:
* SWI (software interrupts) are how you trigger interrupt handlers from events!
* really shouldn't rely on fixed message termination indicators when transferring arbitrary binary data :P
* still enjoy connecting people with shared interests
