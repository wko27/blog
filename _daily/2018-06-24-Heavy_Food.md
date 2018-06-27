---
layout: post
unique_id: heavy_food
title: Heavy Food
categories: []
locations: 
---

YESTERDAY:
* woke up at 10:30
* lunch with parents at Cafe Spot
* accidentally went home instead of going to haircut place
* got python code for UART upload to db
* went to aunt's surprise birthday dinner
  * which turned out to actually be my own surprise birthday dinner!
  * my cousin and I are both turning 30 within the next two months, so we had a joint celebration
  * <3
  * tons of gifts including a new office chair and a fantastic lazy susan
  * spent half the night writing thank you cards to everybody
* found out I can't stream from accelerometer or write to flash for more than X seconds
  * turns out shaking the sensor board while attached to Segger J-Link was causing the debugger to freak out
  * Segger Embedded Studio reports that the stack is stuck in address 0xDEADBEEF though ...
* found a weird bug where read from flash + send over UART results in flash erased?
  * writing some tests to debug further

TODAY:
* $8 hair cut
* dim sum with cousin-in-law's family
* saw Incredible II with the cousins
* leftovers for dinner with parents
* conversation about expectations
* 5.5 hour drive back to bay area
  * wasn't sleepy for some reason, straight shot
  * realized a bug around 3 hours in
* got home just before midnight
* unpack everything, then sleep

LEARNINGS:
* pyserial version in conda is 2.7, not latest 3.4 and doesn't include read_until function ...
  * conda uninstalled and switched to pip
* bitshifts in python use unsigned int32s ... need to do explicit subtraction to get proper sign bit
* if you update a global variable in a function in python, need to declare it global (otherwise it'll believe it's a declaration + assignment of a new local)
* how to properly debug when SoftDevice is enabled
  * issue is if you stop execution, there's a higher interrupt that will trigger and get out of whack due to unexpected timing issues
  * one trick is to force the primask register to 1 to disable those interrupts
  * this will break SoftDevice, but at least you can step through code without ending up in a SoftDevice assertion error
  * programmatic setting can be done through __ASM volatile ("MSR primask, %0" : : "r" (0x1) : "memory");
