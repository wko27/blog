---
layout: post
unique_id: hamstring_workout
title: Hamstring Workout
categories: []
locations: 
---

YESTERDAY:
* head to office
  * start debugging flash
* chick fil a for lunch
* found out that due to a little bug in a refactor last week, none of my status register reads were working for flash
  * by luck (and probably the slowness of the Cortex M4 processor compared to beefier CPUs), my flash reads were "mostly" working
  * also by luck, the "configuration status" register value that I updated set a few bits properly disabling more of those one-time protection pages
  * when I fixed that bug, everything broke


TODAY:
* realized that there's a permission register which is initialized to protect all blocks
  * disabled that thing completely, but things still failing
* chatted with hardware engineer for 2 hours debugging flash
* Taiwanese for lunch
* refactored tests, still failing
* took a nap
  * woke up from nap and realized that my test is incorrect; I've been doing sequential reads and writes so it's possible that I'm only verifying reads on the flash's internal buffered value instead of flushes
* rewrote a lot more code
  * found the third bug!!
  * I was using the nrfx spim library's synchronous transactions for configuration and asynchronous transactions for read/write/erase
  * when I moved my erase code to use synchronous transactions, things magically worked
  * issue was that I forgot to set a particular flag before sending the erase command
* hosted a board game night
  * ordered pizza for the first time since college
  * ~3 hour game of terraforming mars ... bit exhausting but fun!

LEARNINGS:
* learned a new hamstring workout
  * basically bridge pose with butt raised, but then slide your feet out and in (wearing socks on a slippery floor)
  * holy cow, my hamstrings were instantly sore xD

