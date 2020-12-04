---
layout: post
unique_id: firebase_password_reset_from_gmail
title: Firebase Password Reset from Gmail
categories: [firebase, gmail]
locations: 
---

Firebase authentication has a useful email/password login option and it's default behavior includes easy ways to trigger password resets.  One annoyance though is that the invoking the password reset will be sent from *noreply@(project-id).firebaseapp.com* email address.  This can easily end up in a customer's spam folder or blocked by email filters, etc.

Firebase offers two ways to fix this; one by setting up a custom domain and one by integrating with any SMTP server.  We'll focus on the second one for today and specifically hooking it up to Gmail.

![SMTP]({{ site.baseurl }}/assets/img/2020-12-04_firebase_smtp_gmail.jpg){:class="img-responsive"}

The steps are pretty simple:

1. Toggle enable on
2. Enter each of the fields (see above for the correct values for Gmail)
3. Hit save

Some parts to pay closer attention to:
1. The username should include the full email address with the @host.com extension
2. The SMTP security mode should be set to STARTTLS and not SSL for Gmail
3. If this is a GSuite (now called Google Workplaces) account, you'll have to do a few extra steps
4. in the Google Admin console, go to Security and 'Less Secure Apps', then click the option to 'Allow users to manage their access to less secure apps' (see below)

![Less Secure Apps]({{ site.baseurl }}/assets/img/2020-12-04_google_admin_less_secure_apps.png){:class="img-responsive"}

5. in Gmail, click on your profile to 'Manage your Google Account', then head to Security and enable 2-factor authentication
6. in Gmail, in the same Security tab, there's also a section for 'App Passwords', it's a good practice to avoid sharing the account password with Firebase, so create a custom one

![Gmail Security]({{ site.baseurl }}/assets/img/2020-12-04_gmail_security.png){:class="img-responsive"}

If you test now by triggering a password reset for a user on the Firebase authentication tab, you should get a password reset email from that Gmail account!  Unfortunately if it doesn't arrive, then there's no easy way I've found to debug; so carefully check each step.

Bonus!

Ok, so notice how the email at the top is a noreply@(custom domain) but the email I use as a user is somebodyelse@(custom domain)?  Here, we're using a Google Groups email address and sending emails from our Gmail account under an alias.

To set up the Google Group:
1. Create your Google Group
2. For a no-reply group, I ensured that group members do NOT receive any inbound messages
3. Under 'Group Settings', in the 'Posting policies' section, ensure that 'Who can post as group' is enabled

![Google Group Posting Policies]({{ site.baseurl }}/assets/img/2020-12-04_google_group_posting_policies.png){:class="img-responsive"}

To enable the Gmail account to post on behalf of the group, we'll just need a few more steps:
1. Back in your Gmail account, click the settings button in the upper right, then click 'See All Settings'
2. Head to the 'Accounts' tab and see the 'Send mail as' section, then 'Add another email address'

![Gmail Accounts]({{ site.baseurl }}/assets/img/2020-12-04_gmail_account_settings.png){:class="img-responsive"}

If all goes well, that will become an option and now you should receive emails from the Google groups email address :)
