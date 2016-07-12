'''EnableCronHowto'''

[[TableOfContents]]

= Introduction =
Cron jobs are useful to repeat things on configurable intervals. E. g. reconnect your WAN connection at a given time if you are using PPPoE.

You may know some more useful tasks for cron on your Wrt router.

= Requirements =
 * A standard !OpenWrt Kamikaze release
= Installation =
{{{Crond}}} is installed and running by default. Follow the testing section below and if your test fails try this:

It may be that cron is not autostarting.

{{{
  ps -elf | grep cron
}}}
If crond, the cron daemon is running, you will see:

{{{
 1760 root        380 S   crond -c /etc/crontabs -b
 2260 root        292 S   grep cron
}}}
If you do not see the crond running then ensure the cron system gets stated at boot-time.

{{{
/etc/init.d/cron start
/etc/init.d/cron enable
}}}
= Configuration =
== Testing crond (optional) ==
Create a minute job in the root crontab file:

{{{
echo "* * * * * echo \"Testing crond...\" | /usr/bin/logger -t crond" >> /etc/crontabs/root
}}}
Run {{{logread -f}}} and after a minute you should see:

{{{
Jan  1 02:50:01 OpenWrt cron.notice crond[566]: USER root pid 577 cmd echo "Testing crond..." | /usr/bin/logger -t crond
Jan  1 02:50:01 OpenWrt user.notice crond: Testing crond...
}}}
== Creating a cron job ==
The cron jobs are defined in the {{{/etc/crontabs/root}}} file. {{{crond}}} reads this file. You have two ways on adding a cron job to this file.

The first one is just to create the {{{root}}} file with {{{echo}}} like this:

{{{
echo "0 4 * * * ifdown wan && sleep 2 && ifup wan" >> /etc/crontabs/root
}}}
or use {{{crontab -e}}} (calls the {{{vi}}} editor) to edit the cron job file. Copy & paste

{{{
0 4 * * * ifdown wan && sleep 2 && ifup wan}}}
than hit {{{ESC}}} and enter {{{:wq}}} to save the file.

The example cron job reconnects your WAN connection at a 4am every day if you are using PPPoE.

When done you can list the cron jobs with

{{{
crontab -l
}}}
{{{
0 4 * * * ifdown wan && sleep 2 && ifup wan}}}
That's it.

= Links =
 * Cron job calculator [[BR]]- http://www.csgnetwork.com/crongen.html
