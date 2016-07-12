I set up cron in order to publish my IP on the internet when it changes. You may know some more useful tasks for cron on your router.

The easiest way to do this is to add the following to your /etc/rcS init script. This may be bad practice, but it saves having to create a new file on the flash.

{{{
# start crond
mkdir -p /var/spool/cron/crontabs
echo "0 * * * * /usr/bin/checkmyip" > /var/spool/cron/crontabs/root
/usr/sbin/crond
}}}

If you don't know how to edit the original files (read-only) on OpenWRT read this - EditingRomFiles

Now either run the commands above manually or reboot your router to activate crond.

Replace the echo line with the cron job you want to add. If you want to add more lines to that, just add additional echo lines using ">>" instead of ">" in the command in order to append lines to the end of the cron file.

I'm not sure if this works in the default configuration of OpenWRT, since I already had a root user when I did this (installing dropbear (Mini SSH Server) adds the root user) on my router. So someone can may want to shed light on this issue.
