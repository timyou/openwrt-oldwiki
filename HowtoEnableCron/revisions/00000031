'''EnableCronHowto'''


[[TableOfContents]]


= Introduction =

Cron jobs are useful to repeat things on configurable intervals. For example
you can update your IP address on a [:DDNSHowTo:DDNS service] or you can sync
the routers time with {{{rdate}}} once a day.

You may know some more useful tasks for cron on your Wrt router.


= Requirements =

 * a standard OpenWrt White Russian installation (works with all release
 candidates)
 * {{{rdate}}} or the {{{ntpclient}}} (both optional) to sync the time on your
 router


= Installation =

{{{Crond}}} is installed by default. !OpenWrt uses the !BusyBox {{{crond}}}.


= Configuration =

== Create a init script for crond ==

First you have to modify the init script so that {{{crond}}} will start up
automatically on each bootup of your router. This because RC4 doesn't have a correct
{{{S60crond}}} script in the {{{/etc/init.d}}} directory.
Remove the link and copy paste this into it.
do:

{{{
cat > /etc/init.d/S60crond
}}}

{{{
#!/bin/sh
[ -d /etc/crontabs ] || mkdir -p /etc/crontabs
[ -e /var/spool/cron/crontabs ] || {
        mkdir -p /var/spool/cron
        ln -s /etc/crontabs /var/spool/cron/crontabs
} && crond -c /etc/crontabs
}}}

After pasting it, press {{{ENTER}}} and then hit {{{CTRL-D}}} keys to save the
file.

Now make sure the init script is executable and start it with

{{{
chmod a+x /etc/init.d/S60crond
/etc/init.d/S60crond start
}}}


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

The cron jobs are defined in the {{{/etc/crontabs/root}}} file.
{{{crond}}} reads the file. You have two ways on adding a cron job to this file.

The first one is just to create the {{{root}}} file with {{{echo}}} like this:

{{{
echo "0 * * * * /usr/sbin/rdate time.fu-berlin.de" >> /etc/crontabs/root
}}}

or use {{{crontab -e}}} (calls the {{{vi}}} editor) to edit the cron job file.
Copy & paste

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

 * Cron job calculator
 [[BR]]- [http://www.csgnetwork.com/crongen.html]
