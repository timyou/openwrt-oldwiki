'''HowtoEnableCron'''


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

First you have to create a init script so that {{{crond}}} will start up
automatically on each bootup of your router. We call it {{{S51crond}}} and it
should go in the {{{/etc/init.d}}} directory. To create it via copy & paste
do:

{{{
cat > /etc/init.d/S51crond
}}}

{{{
#!/bin/sh
#
# crond           Starts crond
#
mkdir -p /etc/spool/cron/crontabs
mkdir -p /var/spool/cron
ln -s /etc/spool/cron/crontabs/ /var/spool/cron/crontabs

start() {
 echo -n "Starting crond: "
 /usr/sbin/crond
 touch /var/lock/crond
 echo "OK"
}

stop() {
 echo -n "Stopping crond: "
 killall crond
 rm -f /var/lock/crond
 echo "OK"
}

restart() {
 stop
 start
}

case "$1" in
 start)
  start
  ;;
 stop)
  stop
  ;;
 restart|reload)
  restart
  ;;
 *)
  echo $"Usage: $0 {start|stop|restart}"
  exit 1
esac

exit $?
}}}

After pasting it, press {{{ENTER}}} and then hit {{{CTRL+D}}} keys to save the
file.

Now make sure the init script executable and start it with

{{{
chmod a+x /etc/init.d/S51crond
/etc/init.d/S51crond start
}}}


== Creating a cron job ==

The cron jobs are saved in the {{{/etc/spool/cron/crontabs/root}}} file.
You have two ways on adding a cron job to {{{crond}}}.

The first one is just to create the {{{root}}} file with {{{echo}}} like this:

{{{
echo "0 * * * * /usr/sbin/rdate tock.usno.navy.mil" >> /var/spool/cron/crontabs/root
}}}

or use {{{crontab -e}}} (calls the {{{vi}}} editor) to edit the cron job file.
Copy & paste

{{{
0 * * * * /usr/sbin/rdate tock.usno.navy.mil
}}}

than hit {{{ESC}}} and enter {{{:wq}}} to save the file.

The example cron job will sync the routers time every hour using {{{rdate}}}.

When done you can list the cron jobs with

{{{
crontab -l
}}}

{{{
0 * * * * /usr/bin/myprogram
}}}

That's it.


= Links =

 * Cron job calculator
 - [http://www.csgnetwork.com/crongen.html]
