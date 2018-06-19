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
* called dad
* read documentation and implemented flash reads and writes

TODAY:
* 

LEARNINGS:
* what '*this = 1' means in a C++ constructor?
  * actually ... I lied, I still have no idea what this does
* lol so I got my flash writes to work
  * and then I discovered that the first 12 pages are "One Time Program" (OTP) pages which explains why my subsequent write attempts failed
* EasyDMA has a max transfer size of 255 bytes per SPI transaction
  * we can get around this by using EasyDMA ArrayLists and PPI (complicated)
  * or we can just do several transactions in a row before bringing slave select pin high
    * but of course, you can only do this in SPIM_EXTENDED mode which is only supported on nrf52840, not nrf52832
