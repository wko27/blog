---
layout: post
unique_id: email_comments
title: Email Comments
categories: []
locations: 
---

A while ago, I was exploring options for adding comments to this blog.  Disqus is a popular commenting tool that can be added to any website.  It provides a snippet of html/javascript that provides a list of comments, a comment form, and handles tricky things like multimedia uploads, spam moderation, and engagement metrics.  However, Disqus seems mostly geared towards bloggers who want to monetize and a lot of their features are "require ads", "require logins", "show promotions", etc.  I'm also not a huge fan of tying myself to a 3rd party service just to host comments when I'm already using GitHub to host the content itself.

**How hard can it be to set up comments stored in GitHub instead?**

Basically, we need two things:
1. Blog needs a **comment box** that sends an email to my Gmail
2. Need to periodically **read comments** from Gmail and **upload them to GitHub**
3. Blog needs to **list** those comments

To accomplish item 1, we just need an HTML form, and a button which triggers some javascript.  That javascript will open a mailto link which will have the comment all ready to be sent to my Gmail inbox.  The HTML form is in the comment div [here](https://github.com/wko27/blog/blob/master/_layouts/post.html).  The javascript code is [here](https://github.com/wko27/blog/blob/master/assets/comment.js).

For item 2, we're going to use a Python script and run it on either AWS EC2, or a raspberry pi.  We'll be using the [Gmail API](https://developers.google.com/gmail/api/) to read emails and [GitHub API](https://developer.github.com/v3/) to upload the comments.  The Python code for this is [here](https://github.com/wko27/blog/blob/master/scripts/comment.py).

There's a bit of complexity since we need to mark that we've already uploaded the comment for a particular email to avoid re-processing the same comment over and over again.  To do this, we'll use a Gmail label; so first we configure our Gmail account to label all incoming mail with a '[blog-comment]'-prefixed subject as 'needs_updating'.  Then, in our script, we read all messages with that label, upload them, and remove the label.  

Note that you'll need to generate an OAuth key and an access token for the Gmail account.  Please follow [this tutorial](https://developers.google.com/gmail/api/quickstart/python) to get those!  You'll also need a [GitHub API token](https://github.com/blog/1509-personal-api-tokens).

For item 3, we just need a bit of Jekyll/Liquid templating code to display those comments.  The code for this is in the 'article-comments' div [here](https://github.com/wko27/blog/blob/master/_layouts/post.html).  I used [livestamp.js](https://mattbradley.github.io/livestampjs/) to display timestamps a bit more nicely.  It requires jquery.js and moment.js so those are added to my [head.html](https://github.com/wko27/blog/blob/master/_includes/head.html).

Lastly, I wanted a little tooltip on the submit button to inform users that the email form is intentional.  Tiny bit of JQuery to handle that is the tooltip functionality [here](https://github.com/wko27/blog/blob/master/_includes/head.html).

Tada, simple email commenting system, plus:
* Comment feed comes straight through your inbox
* Gmail itself can filter spam
* Super easy to reply privately to public comments
* Users can send private messages via email by just clearing the subject line prefix (I may add a button for that)

Feel free to leave a comment (har har har) if you need help with this!
