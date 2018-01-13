---
layout: post
unique_id: super_glue
title: Super Glue
categories: []
locations: 
---

YESTERDAY:
* rock climbing + yoga
* bought two small tires to play with
  * spent 30 mins prying out the inner tube and taking out the hub
* took Dad to a ping pong gym
  * quite spry for 70 years old!!
* took parents to their first Ethiopian restaurant
  * we ordered these stuffed jalapeno peppers and they were crazy spicy

TODAY:
* parents departure
* rock climbing
* fixed testing app
  * figured out how to add new intents properly
  * also figured out the layout system for defining views in Android; pretty nifty
  * app now shows sensor battery life and number of records uploaded in current recording
* mounted sensor on tire
  * super glued a piece of laminated paper to a tire
  * taped sensor to the paper
* made loh mai fan with garlic and twice as much sausage (a delicious oops)
* dinner party @ Brian's with some fun anime!
  * made linguini from scratch :D
  * enjoyed some delicious clams in a white wine sauce
* added a db validation test to math project
  * this was ... painful (see learnings)

LEARNINGS:
* tldr; jest is a real PITA ...
* I wanted to add context to a deeply nested check (cuz Firebase)
* options for doing this:
  1. add a test per db entity that I want to verify
  2. try-catch and rethrow with context (or the poor javascript verson of this)
  3. modify error message thrown to include context
  4. pass the context down every function call (ewwwww)

1 is not possible because the *describe* mechanism one uses to show dynamic tests doesn't support async behavior (and since I need to do a db-read before figuring out all my test cases, this isn't great).  This is also prone to race conditions if e.g. somebody deletes a db entity between describe extract and the actual test run.

2 is not possible because Javascript doesn't support nested errors (<.<) AND jest hides console output on test failure.  Supposedly this is done so test output is readable for parallelized runs.  They have a --verbose which supposedly suppress the suppression but doesn't always work.  They have a -runInBandn flag to force single-threaded execution, but that didn't work.

3 is tricky because they wrote their entire matcher framework to only accept two arguments.  I'd have to re-write all of the matchers (either to take in 3 args, or to assume the first is an object where I can extract context).

So ... I ended up going with option 4 and creating my own assert library ...

