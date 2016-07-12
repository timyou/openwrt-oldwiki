I set up cron in order to publish my IP on the internet when it changes. You may know some more useful tasks for cron on your router.  An easy way to do this is as follows:

Lets say you want to run checkmyip every hour.  To do that, create the following script as `/etc/init.d/S51crond`:

{{{
#!/bin/sh
# start crond
mkdir -p /var/spool/cron/crontabs
echo "0 * * * * /usr/bin/checkmyip" > /var/spool/cron/crontabs/root
/usr/sbin/crond
}}}

Set the permissions so it can be executed directly:

{{{
chmod 755 /etc/init.d/S51crond
}}}

Now either run the command /etc/init.d/S51crond manually or reboot your router to activate crond.

Replace the echo line with the cron job you want to add. If you want to add more lines to that, just add additional echo lines using ">>" instead of ">" in the command in order to append lines to the end of the cron file.

Alternately, create /etc/spool/cron/crontabs and use the following script:

{{{
#!/bin/sh
# start crond
/usr/sbin/crond -c /etc/spool/cron/crontabs
}}}

This will leave all changes in place between reboots. All cronjobs go in the /etc/spool/cron/crontabs/root file.

You can also use the 'crontab -e' command to make your changes this way.

'''Troubleshooting:'''

If crond says "Ignoring 'root'" then create /etc/passwd and /etc/group with an entry for root.

/etc/passwd:
{{{
root:x:0:0:root:/:/bin/sh
}}}

and /etc/group:

{{{
root:x:0:
}}}

Also, make sure you have the clock set correctly on your router!  An easy way to do this is to do this:

{{{
rdate tock.usno.navy.mil
}}}
