---
layout: post
unique_id: sleep_deprivation
title: Sleep Deprivation
categories: []
locations: 
---

YESTERDAY:
* woke up at 7:30 for morning climbing
  * turns out I can do an 11a when sleep deprived!
  * note to others: please don't pee in public showers especially when the water flows from your stall through mine to the drain
* call out to an [excellent mix](https://soundcloud.com/officialsenza/bloom)
* finally debugged my ADXL 372
  * turns out there's a #define macro that prevents SPI reads of over 256 bytes
  * also finally got all my numbers right, so not running into missing bytes in my buffers
* bento for lunch
* spent the rest of the afternoon believing that my GATT notification of 256 bytes were split into 20 byte partitions
  * finally figured out that wasn't the case with a little hardcoded test
* caught up on Westworld
  * VM in a VM again?
* unhealthy wingstop dinner
* discovered max MTU
  * also discovered that Nordic error messages actually print little helper texts in the IDE!
  * wasted an hour reading forum posts before looking at it more closely
* got it all hooked up yay
  * only weird thing is I have 319 hz worth of data (for 13 seconds), but I only configured the sensor to read at 200 hz ...

TODAY:
* cleaned up some issues on the app
* reverted some changes to the website that we made for a demo video
* leftover chicken, dumplings, and leafy greens for lunch
* guitar lesson
  * told my teacher that my sis gave me a banjo :p
* headed to work and started implementing battery power reads using an ADC driver (analog to digital converter)
  * got confused between ADC and SAADC (successive approximation ADC)
* caught up with friends over Taiwanese dinner
* spent 2.5 hours learning how to [play Cripple Creek on the banjo](https://www.youtube.com/watch?v=BdYuUZ2NrpY)
  * that was my cleanest recording out of two dozen xD

LEARNINGS:
* SPI reads are limited to 256 byte transfers unless you use EasyDMA lists!
  * and apparently EasyDMA lists are disabled on nRF52840
* learned how characteristic notification reads actually work
* how to configure and negotiate max MTU
