---
layout: post
unique_id: father's_day
title: Father's Day
categories: []
locations: 
---

YESTERDAY:
* woke up and re-implemented gpio pin configurations manually
  * finally got flash responding with proper values!!!
  * apparently my write protect and hold pins need to actually be configured
  * doesn't suffice to just set them high
* ended up 30 mins late to climbing
  * overdid it on the fingers with an 11b
  * scraped part of my pinky off on a v2
  * fingers aren't used to bouldering anyomre xD
  * teaching a friend's nephew some basics of climbing
* Taiwanese for lunch
* cleaned up flash code
* nap
* Shanghainese for dinner at Shanghai Bistro in Fremont
  * pan-fried pork buns were quite delicious and not oily!
  * lovely discussion on all sorts of interesting things Google does with books
* father's day call!
* read documentation and implemented flash reads and writes

TODAY:
* (super secret) accelerator program welcome call, found out about some other startups
* rewrote spi logic trying two different workarounds for EasyDMA 255 byte transfer limit
* went home to finish leftovers for lunch
* nap
* dental appointment
  * back to electric toothbrush!
* abs and core class
* pork chop and last of veggie soup for dinner
  * yeesh, took me ~10 days to finish that soup!
* late night working session

LEARNINGS:
* what '*this = 1' means in a C++ constructor?
  * actually ... I lied, I still have no idea what this does
  * update: ok figured it out, there was an operator overload for '=' in the header file
* lol so I got my flash writes to work
  * and then I discovered that the first 12 pages are "One Time Program" (OTP) pages which explains why my subsequent write attempts failed
* EasyDMA has a max transfer size of 255 bytes per SPI transaction
  * possible workarounds
    * first one was changing the constant in nrfx/mdk/nrf52832_peripherals.h, #define SPIM2_EASYDMA_MAXCNT_SIZE 8
      * got weird results with that
    * second was a red herring forum post from 2 years ago indicating that you can just do multiple transactions in a row and manually control slave select pin
      * unfortunately, this require SPIM_EXTENDED mode which is only supported on nrf52840
      * also, I'm pretty sure it wouldn't work even if I hacked it
    * third was to use PPI and an EasyDMA array list feature
    * fourth was to manipulate the pins directly ...

