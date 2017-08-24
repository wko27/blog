---
layout: post
unique_id: engineering_management
title: Engineering Management
---

One of the common questions asked by candidates during a culture interview is "how has the culture changed over the years?".  In my opinion, the largest shifts in engineering culture occurred due to changes in team structure and management.  The first major change resulted from our decision to split into multiple teams.  The second came from our decision to switch from people managers to technical managers.

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

<hr/>

When we initially split into teams, each team had a product manager, a unique tech lead, and a single shared people manager.

**What does that manager do?**

In my opinion, an engineering manager is primarily responsible for resource allocation:
* which projects/teams are funded
* who is staffed on projects/teams
* how salaries/stock options/bonuses are distributed to individuals
* setting hiring goals for existing/new teams
* prioritizing which tasks the team should focus on

However, there are two distinct styles of enginering management:
* people managers
* technical managers

People managers tend to play a more supportive role; enabling individuals by finding opportunities for them (e.g. technical projects, mentorship opportunities, leadership initiatives).  They ensure a team has the resources to accomplish tasks; whether it's bringing in an architect from another team, an external consultant, or bringing in other roles to assist (SRE, product support).  They rely on technical leads and product leads for technical and product-related decisions.

Technical managers tend to play a more direct role; from setting a technical vision, and defining/tracking metrics towards goals, to choosing projects/libraries/frameworks to use, to actually writing and reviewing code.

As our engineering team grew, we clearly needed more managers.  Since we already had strong tech leads, we originally focused on acquiring more people managers.

**Why did we change this?**

In short, it's very rare to find a manager candidate with a solid technical foundation (necessary to work with a strong tech lead), but wants to focus on people management instead.  Managers tended to be promoted from the ranks of "good engineers" and these candidates liked to stay in touch with the latest technologies.  Managers that didn't come from pure software engineering roles still tended to be career-focused.  Progressing upwards towards higher management positions requires showing an ability to handle increased responsibilities.  Demonstrating such proficiency is done by making the "right" calls for important decisions.  It's much easier to show that a technical decision was the right call vs. a people management decision, e.g. a "20% increase in sales due to critical feature X which I drove" is a more objective resume builder than "20% increase in sales due to my tech lead's decisions which I supported".  In the end, high-performing eng mgr candidates tended to desire technical impact in their role and so we altered the role to fit the demand.

**How did this affect the culture?**

A tech lead is an individual contributor responsible for coding the best solutions for the team, product, company, and customers.  Debates about libraries/frameworks/maintainability/performance are (or should be) followed up with investigations and data points.  There tends to be a high level of transparency to these discussions; even when they become philosophical or religious (e.g. emacs vs vim), at least everybody knows who's on which side and why.  It's much easier to trust a tech lead with decisions because you can always ask why.

A people manager is a manager responsible for allocating resources towards projects.  These decisions are much more subjective and touchy involving who is better at X or who doesn't like to work with Y.  These tend to have less transparency due to the sensitive nature of pride and avoiding hurting people's feelings.  In a transparent world, people wouldn't feel bad just because somebody else is better at X, and Y and Z would resolve their differences via open feedback and compromise.  However, this isn't the state of the typical American engineering work culture.  In the absence of such transparency, we have to trust our people managers to make the right decisions for the team.

When these responsibilities are split, it's clear that if the tech lead's proposal was not taken, then there were other non-technical factors at play.  When all of these responsibilities fall on one person, it's a higher burden to explain why a particular decision was made.  When the decision maker can not be transparent about why a decision is made, it's very easy for him/her to lose the trust of the team.

I've seen managers that are able to obtain/retain that trust but it's very difficult for every manager in a growing company to hold it.  Lack of trust in a manager quickly leads to all sorts of unhealthy culture issues.

I believe that "trust" is the most correct measure of a manager's effectiveness.  A manager that does not have the trust of his/her superiors is unable to make decisions that are objectively better for the team.  A manager that does not have the trust of the team can not effectively execute on those decisions.
