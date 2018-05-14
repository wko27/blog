---
layout: post
unique_id: low_frequency_clock
title: Low Frequency Clock
categories: []
locations: 
---

YESTERDAY:
* outing with parents while Amy stays at home working
  * family haircut!
  * overdid it for lunch as usual ($36 for four gigantic plates of food)
  * Costco run with Dad
    * they are bringing boxes of Hershey's chocolate to my grandma
* afternoon yoga class
  * teacher-in-training = cheap class :D
  * endless crunches q.q
  * wayyyy too hot
    * had to lay down and rest since I knew my body overheated
    * went to parking garage afterwards, 90+ degrees outside was nice and cool
* nap
* family dinner
  * tried to go to a restaurant my sis liked, but owners are on vacation for 2 weeks
  * ended up at a place called Cafe Spot
  * sole + pork chop w/ HK curry over spaghetti
  * plus corn, veggies, and a tasty appetizer soup!
* got home, spent 5 hours figuring out how to get a timer to work on the nRF52
  * I thought Medallia had it bad with releasing new versions without proper deprecation
  * documentation shows 3 low-level APIs and 1 high-level APIs all to manipulate the timer
    * release notes on the latest SDK shows an experimental version of the high-level API (possible replacement?)
    * the examples in the SDK mix usages of the low-level and high-level API
    * the questions on the forum are all over the place from an even older deprecated API which required accessing nRF52's registers directly ...

TODAY:
* hang out with parents
* leftovers for lunch
* almost done with yeager's poem
  * over 6 months late
  * at this point, I'll just give it to him on his anniversary
* loaded up car
* head back to bay area
  * cruising up the 101 with my sis!
  * dinner at Subway in Santa Barbara
  * lovely bathroom with a view of the skies
* unpacked most things
* back to work on adxl

LEARNINGS:
* the correct way to set a gdb breakpoint is via a __asm__("BKPT")
  * I had previously discovered a way which worked using some code from [here](https://devzone.nordicsemi.com/f/nordic-q-a/12963/software-breakpoints-with-j-link-probe)
  * I usually invoke this immediately from main function to trigger gdb on main
  * turns out for some reason, after working properly for three days, it caused a hard fault on invocation
  * this took me 3 hours to figure out since any time I tried to poke with a debugger it crashed
  * I also couldn't poke it with a logger because the logging library needs a few ms to initialize and if you crash too early in main, you get nothing
* in order to use the "app_timer" library, one must first initialize the low frequency clock using a completely different "clock" API
  * this isn't obvious at all unless you happen to stare very closely at one of the examples in the SDK, e.g. spi_master_using_nrf_spi_mngr
* wherever only has three e's not four xD
