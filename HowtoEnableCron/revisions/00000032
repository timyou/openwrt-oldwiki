'''EnableCronHowto'''

[[TableOfContents]]
= Introduction =
Cron jobs are useful to repeat things on configurable intervals. For example you can update your IP address on a [:DDNSHowTo:DDNS service] or you can sync the routers time with {{{rdate}}} once a day.

You may know some more useful tasks for cron on your Wrt router.

= Requirements =
 * a standard OpenWrt White Russian installation (works with all release candidates)
 * {{{rdate}}} or the {{{ntpclient}}} (both optional) to sync the time on your router

= Installation =
{{{Crond}}} is installed by default. !OpenWrt uses the !BusyBox {{{crond}}}.

= Configuration =
== Testing crond (optional) ==
Create a minute job in the root crontab file:

{{{
echo "*/1 * * * * /bin/date > /tmp/crontest" >> /etc/crontabs/root
}}}

Wait a minute, and see {{{/tmp/crontest}}} file:

{{{
cat /tmp/crontest
}}}

== Creating a cron job ==
The cron jobs are defined in the {{{/etc/crontabs/root}}} file. {{{crond}}} reads the file. You have two ways on adding a cron job to this file.

The first one is just to create the {{{root}}} file with {{{echo}}} like this:

{{{
echo "0 * * * * /usr/sbin/rdate time.fu-berlin.de" >> /etc/crontabs/root
}}}

or use {{{crontab -e}}} (calls the {{{vi}}} editor) to edit the cron job file. Copy & paste

{{{
0 * * * * /usr/sbin/rdate time.fu-berlin.de
}}}

than hit {{{ESC}}} and enter {{{:wq}}} to save the file.

The example cron job will sync the routers time every hour using {{{rdate}}}.

When done you can list the cron jobs with

{{{
crontab -l
}}}

{{{
0 * * * * /usr/sbin/rdate time.fu-berlin.de
}}}

That's it.

= Links =
 * Cron job calculator [[BR]]- http://www.csgnetwork.com/crongen.html
