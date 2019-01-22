---
layout: post
unique_id: tech_lead_and_pm
title: Tech Lead and PM
categories: [work]
locations: 
---

There's data out there that shows the best indicator of performant engineering teams are those where the tech lead and product managers align.

So, how do we make sure tech leads and product managers get along with each other?  During my career so far, I've had the opportunity to work directly with about eight different product managers.  The ones which I respected were those that took the time to understand reasons why an engineer pushes back against a task.

** Advice to Product Managers **

Engineers are inherently lazy.  We want to put the least amount of effort to maximize results.  However, we are not against doing a bit of extra work now to save a lot of time in the future.  For example, adding tests now means less chance of the new guy breaking things when he joins in six months and waking me up for an on-fire at 3 am.  Another example is building a prototype which will be thrown away.  We can be convinced that all the features are necessary but if it's going to take three weeks to build and we have to redo it from scratch immediately afterwards; that's hard to stomach as a lazy person.  You'll need to convince me that those features are necessary and I'll need to convince myself that there's no simpler shortcuts to take (e.g. injecting css into a wordpress site via javascript, but that's another story).

** Advice to Tech Leads **

Product managers live in a precarious world.  It is somewhat easy to show that code is "correct".  It is not easy to show that a product's design is "correct".  It is impossible to say it is "correct" to every stakeholder, from every user to the CEO and the board of directors.  If the users love it but the CEO doesn't, we have a problem.  If the CEO loves it but the user doesn't, we have a different problem.  As a result, the product manager is usually under a lot of stress.  A healthy understanding of the perception of the product from internal and external stakeholders is crucial in understanding a product manager's position before he or she asks for a feature.

One of my rules when working with my product manager was to avoid useless debate.  Sometimes, it's actually faster to implement a feature, let the PM see the design flaws and discard the code rather than debate about it on a whiteboard.  This has a couple of advantages:
* instead of one engineer and one PM stuck in a room for two hours arguing, the engineer spends two hours coding and the pm can do other tasks
* if it turns out the PM was right after all, then great you now have a prototype that you can clean up
* the PM learns that when an engineer actually pushes back hard, it's because it's something that is non-trivial to build or prototype

On the plus side, a good tech lead should know the code inside and out and anticipate features that may need to be built.  Plus, they get to prototype which is something that tech leads often don't have time to do.

This also works when pushing for a feature that a PM thinks is unnecessary.  As an example, our text analysis job was quite complicated involving multiple transformations.  Our professional services team had no easy way to figure out what went wrong when topics didn't match correctly.  Engineering had built in a debugging endpoint which exposed quite a bit of information.  During a hackathon, Guille found an easy way to expose this page to the professional services team.  They found it so useful that product gave us resources to clean it up properly.
