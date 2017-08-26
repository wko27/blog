---
layout: post
unique_id: team_split
title: Culture Shifts - Team Split
categories: [long]
---

One of the common questions asked by candidates during a culture interview is "how has the culture changed over the years?".  In my opinion, the largest shifts in engineering culture occurred due to changes in team structure and management.  The first major change resulted from our decision to split into multiple teams.  The second came from our decision to switch from people managers to technical managers (which I'll cover in [this blog post]({{ site.baseurl }}/Technical-vs-People-Manager)).

<hr/>

When I joined Medallia, we had 12 developers that all reported to a manager who reported to a VP and that VP reported directly to the CEO.

Like many startups, we were proud of our flat culture and there were no formal titles amongst the ICs (individual contributors).  Everybody was allowed to work on anything although individuals had areas of expertise and interests.

**Why did we break into teams?**

When we reached about two dozen developers, it became ridiculous to pretend we could all be on-call for every part of the product.  People were suffering from the overhead of context-switching and we recognized that each product area needed a roadmap and clear owners.

There are in general two ways to create teams; one is by assigning teams functional areas of the codebase and the other is to assign product features (which typically require building/extending different services unless the feature is an API, extremely minimally scoped, or code/system duplication is acceptable.  We experimented with both actually before settling on the functional approach.  In the product approach, code quality quickly loses consistency as owners transition.

**Why did breaking into teams cause a culture shift?**

Dividing into teams meant each single individual contributor no longer felt full ownership over problems outside of their team's domain of responsibility.  E.g. if I discover a race condition in the ORM layer exposed while building a feature for text analytics, I had to go through platform team to complete the fix.  There's nothing inherently wrong with this in itself, but fixing something yourself will always feel more agile/empowered than going through a barrier.

Lots of initiatives were taken to solve this including:
* "common good" system to reward efforts which benefited everybody
  * this was a shared pool of bug fixes, tooling ideas, etc that anybody could work on
* map product/code components to team responsibilities
* pursuit of microservices (worth its own blog post)
* being explicit in new hire training that perspectives are welcome on any parts of the codebase
* initiatives to increase cross-team communication
* refactoring legacy components to respect team boundaries (API divisions)
* accountability metrics
* tiger teams to solve joint issues
* allow individuals to cross team boundaries

This last solution had some complexities.  Disallowing people to cross boundaries means teams must be very strict with deadlines to avoid blocking other teams.  There are endless ways to improve predictability for a team but excessive planning quickly eats up time and energy.  Allowing people to cross team boundaries can help ease the friction but can bring its own issues.  Allowing individuals to temporarily contribute code to another team's codebase causes ownership issues since the writer/reviewer of code is not permanently responsible for the maintenance of his/her changes.  Allowing individuals to permanently cross team boundaries means certain individuals have now have "superpowers" compared to normal team members.  If this is used cautiously and judiciously, then it can be ok; but it can quickly devolve into a culture that glorifies heroic saves.

To clarify, many of these issues were anticipated before we split into teams.  Also, the change in feelings of ownership was a gradual transition, not an immediate change.

Inevitably with growth, splitting into teams becomes a necessity in order to protect and focus people/teams/resources.  However, it comes with a loss of ownership and impact for individual contributors.  With one team, the customer of each developer is the product team and by extension: our customers, or sales/marketing, or product support.  Withsplit teams, one should be clear that other teams are also customers and adjust goals/metrics/priorities accordingly.

[Continue to part 2]({{ site.baseurl }}/Technical-vs-People-Manager)!
