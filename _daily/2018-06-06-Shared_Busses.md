---
layout: post
unique_id: shared_busses
title: Shared Busses
categories: []
locations: 
---

YESTERDAY:
* cereal for breakfast
* ran into some crazy compilation issues on SAADC drivers
* in n out for lunch
* segger j-link finally arrived!
  * necessary to flash firmware onto production boards
  * first time using an Amazon locker
  * 10/10 LTR, super simple and delivery in less than 24 hours
* accelerometer and bluetooth worked on first pass
* temp/pressure did not :(
  * spent 4 hours getting my dev board to match it
* yoga
  * super tired for some reason, maybe cuz no nap?
* caught up with Ji in the parking lot
* leftover wings, a smoothie, and some greens for dinner
* continue debugging temp/pressure
  * discovered that the SDA and SCL lines were connected to pins 9 and 10
  * pins 9 and 10 are reserved for NFC operation unless you mark a special flag ...
* need to context switch to demo prep testing

TODAY:
* woke up, ran debugger, realized that my #define wasn't used in that part of the code
  * added flag to Makefile as a -D option and it works!!!
  * pressure/temp readings fully functional on sensor
* finished last of dumplings for lunch
* head to office
* back to battery power reads via SAADC

LEARNINGS:
* so, I realized that I might have been doing a keto diet by accident
  * my only regular intake on calories is 1/2 a cup of rice maybe twice a week and a banana for my smoothie every other day
  * everything else is protein, veggie, nuts and usually Asian food
    * but since Asian restaurants started charging for bowls of rice, I've been eating less rice out :P
  * this may explain why I don't gain weight despite my eating habits
  * doesn't explain the naps yet though
