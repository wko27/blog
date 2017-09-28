---
layout: post
unique_id: 
title: Redux Thunk
categories: []
locations: 
---

BEFORE YESTERDAY:
* started refactoring mobile app
* quick sprint to San Jose Airport to help with a baby seat issue
* lunch @ Mario's, lovely Italian restaurant in Mountain View
* baked a 1 lb salmon for dinner
* found cheap frozen strawberries at Safeway (bought 5 lbs)
* tried on clothes at Dick's
* smoothie!
* finished [blog post on hiking poles]({{ site.baseurl }}/Hiking_Poles)

YESTERDAY:
* features!
  * got login working
  * refactored the entire data model stored in redux
  * implemented ability to change contact's name (and it updates two screens automatically upon save)
  * fixed it so setting no contact name reverts back to default display of phone numbers
* went for a run!
* forgot to eat dinner
  * ate a frozen burrito and a pear
* rock climbing

TODAY:
* woke up really hungry
  * made scrambled eggs Gordon Ramsay style (coconut oil instead of butter)
* finished some leafy greens in my fridge
* made a tasty vegetable soup
* went for a run
* dancing
* more features!
  * finally fixed my data model in Firebase
  * found a potential bug in Firebase
    * if you set a child listener on a ref.startsAt query, it doesn't seem to trigger?
  * frontend fixes
    * sending replies works again!
    * marking read/unread works properly!
  * batched message reads to avoid ridiculous scrolling on load
  * fixed login so it actually persists properly when restarting the app

LEARNINGS:
* lambdas in java are ->, lambdas in javascript are =>
* how react-thunk actually works
  * basically, the idea is if you want to chain asynchronous actions:
    * we want to use promises, but redux's dispatch function typically just returns the action created
    * we need dispatch to return a promise, hence the need for redux-thunk's **middleware**
      * here middleware is just a fancy name for overriding the dispatch function
    * specifically, redux-thunk inverts control, so instead of calling ```dispatch(functionThatReturnsAction)```, you can do ```dispatch(functionThatReturnsFunctionThatDispatchesActionAndReturnsArbitraryValues)```
    * this is powerful, because arbitrary values is typically ... a promise!
  * the only other key fact you need to know is:
    * reducers are called **immediately** after an action is dispatched
* how redux-persist works
  * although apparently next version has some severe breaking changes
