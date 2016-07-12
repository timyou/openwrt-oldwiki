I set up cron in order to publish my IP on the internet when it changes. You may know some more useful tasks for cron on your router.  The easiest way to do this is as follows:

Create the following script as `/etc/init.d/S51crond`:

{{{
#!/bin/sh
# start crond
mkdir -p /var/spool/cron/crontabs
echo "0 * * * * /usr/bin/checkmyip" > /var/spool/cron/crontabs/root
/usr/sbin/crond
}}}

If you don't know how to edit the original files (read-only) on OpenWRT read this - EditingRomFiles

Now either run the commands above manually or reboot your router to activate crond.

Replace the echo line with the cron job you want to add. If you want to add more lines to that, just add additional echo lines using ">>" instead of ">" in the command in order to append lines to the end of the cron file.
