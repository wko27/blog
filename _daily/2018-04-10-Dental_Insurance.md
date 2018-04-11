---
layout: post
unique_id: dental_insurance
title: Dental Insurance
categories: []
locations: 
---

YESTERDAY:
* leftover soup for lunch
* yoga
* started on a backend refactor
  * realized I was basically building a stream processing graph
  * spent 3 hours playing with Spark and Storm to see if it was easy to slot in
    * it wasn't ... to run both locally requires a fair amount of setup
    * storm requires a local zookeeper node plus a ton of output
    * spark streaming comes with parallelizable operations in the DStream object, but none of them are useful for me ...
      * I have analyses that require multiple data streams as input, but there's no unique key I need to perform a join, I just use last X seconds window (guess I could use timestamp as a key, but ... seemed wrong)
    * anyway, rethought the reasoning and I'll probably do aggregate streaming analyses (across multiple users, data sets) using one of the two, but stick to my own thing for real-time localized analyses
* climbing
* pan-fried a tasty pork chop
  * super juicy!
* laundry
* finished a book 
  * secret agent plot with a Ph.D. mathematician sidekick
  * unfortunately, the mathematician can actually multiply numbers, which completey ruined my disbelief suspension

TODAY:
* woke up at 8:30 am
* discovered my dental insurance refused one of my claims
  * spent an hour bouncing around call agents who didn't have credentials to "unlock my account"
* nap
* went to library
* finished rewrite of my streaming processing logic
* made a japanese curry with chicken breast meat
  * made way too much but showed restraint!
  * managed to cut myself again with the peeler :'(
* watched 12 angry men
  * holy crap that was a good film
  * I would not have appreciated this nearly as much even post-college

LEARNINGS:
* that peeler is sharper than any of my knives
