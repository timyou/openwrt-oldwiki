'''DDNS howto'''


[[TableOfContents]]


= About Dynamic DNS (DDNS) =

The DDNS service is for etablishing connections from computers on
the Internet to your computer. This is useful if you want to run
server software on your computer and only have a dynamic IP.

!OpenWrt uses the package {{{ez-ipupdate}}} for providing DDNS
service.


= Requirements =

A recent OpenWrt version. This howto was written for the
'White Russian RC3' and later releases.


= Installation =

{{{
ipkg install ez-ipupdate
}}}


= Configuration =

ez-ipupdate can be used with the following services:

 * http://www.ez-ip.net
 * http://www.justlinux.com
 * http://www.dhs.org
 * http://www.dyndns.org
 * http://www.ods.org
 * http://gnudip.cheapnet.net (GNUDip)
 * http://www.dyn.ca (GNUDip)
 * http://www.tzo.com
 * http://www.easydns.com
 * http://www.dyns.cx
 * http://www.hn.org
 * http://www.zoneedit.com


== Creating the configuration file ==

Easiest way to use ez-ipupdate is creating a configuration file.
We call the file {{{/etc/ez-ipupdate.conf}}}. You can choose any
other name.

{{{
cat > /etc/ez-ipupdate.conf
}}}

{{{
service-type=zoneedit
user=myname:mypassword
interface=eth0
host=mydomain.com

# Do not change the lines below
cache-file=/tmp/ez-ipup
pid-file=/var/run/ez-ipupdate.pid
}}}

/!\ '''NOTE:''' {{{interface=eth0}}}: use {{{ppp0}}} for PPP based
stuff and {{{vlan1}}} for DHCP stuff.

The list of allowed parameters in the configuration file are:

{{{
address                 usage: address=[ip address]
cache-file              usage: cache-file=[cache file]
cloak-title             usage: cloak-title=[title]
daemon                  usage: daemon=[command]
execute                 usage: execute=[shell command]
debug                   usage: debug
foreground              usage: foreground
pid-file                usage: pid-file=[file]
host                    usage: host=[host]
interface               usage: interface=[interface]
mx                      usage: mx=[mail exchanger]
max-interval            usage: max-interval=[number of seconds between updates]
notify-email            usage: notify-email=[address to email if bad things happen]
offline                 usage: offline
retrys                  usage: retrys=[number of trys]
server                  usage: server=[server name]
service-type            usage: service-type=[service type]
timeout                 usage: timeout=[sec.millisec]
resolv-period           usage: resolv-period=[time between failed resolve attempts]
period                  usage: period=[time between update attempts]
url                     usage: url=[url]
user                    usage: user=[user name][:password]
run-as-user             usage: run-as-user=[user]
run-as-euser            usage: run-as-euser=[user] (this is not secure)
wildcard                usage: wildcard
quiet                   usage: quiet
connection-type         usage: connection-type=[connection type]
request                 usage: request=[request uri]
partner                 usage: partner=[easydns partner]
}}}

The main configuration is done now.


= Starting DDNS =


== Manually via the command line ==

{{{
/usr/sbin/ez-ipupdate -c /etc/ez-ipupdate.conf
}}}


== Via hotplug (recommended) ==

This updates your DDNS every time a WAN connection gets etablished.
To get this working you need to do the following:

{{{
mkdir -p /etc/hotplug.d/iface
}}}

{{{
cat > /etc/hotplug.d/iface/15-ez-ipupdate
}}}

{{{
[ "$ACTION" = "ifup" -a "$INTERFACE" = "wan" ] && /usr/sbin/ez-ipupdate -c /etc/ez-ipupdate.conf &
}}}

You have give execution rights for {{{15-ez-ipupdate}}}:

{{{
chmod 755 /etc/hotplug.d/iface/15-ez-ipupdate
}}}

If {{{/etc/hotplug.d/iface/15-ez-ipupdate}}} does not look like the above one, you
have to edit the file manually with the {{{vi}}} editor.

To update your DDNS account do:

{{{
ifdown wan && ifup wan
}}}


== Via init script ==

{{{
cat > /etc/init.d/ez-ipupdate
}}}

{{{
#!/bin/sh

BIN=ez-ipupdate
CONF=/etc/$BIN.conf
RUN_D=/var/run
PID_F=$RUN_D/$BIN.pid
[ -f $CONF ] || exit

case $1 in
 start)
  mkdir -p $RUN_D
  $BIN -d -c $CONF
  ;;
 stop)
  [ -f $PID_F ] && kill -9 $(cat $PID_F)
  ;;
 *)
  echo "usage: $0 (start|stop)"
  exit 1
esac

exit $?
}}}

After saving the file {{{/etc/init.d/ez-ipupdate}}} set the executable bit on it.

{{{
chmod +x /etc/init.d/ez-ipupdate
}}}

To start it automatically on booting do:

{{{
ln -s /etc/init.d/ez-ipupdate /etc/init.d/S80ez-ipupdate
}}}

ez-ipupdate will now be started as a daemon when OpenWrt is started and update IP address automatically when needed.

== Via a cronjob ==

This updates your DDNS account on a specified time via {{{crond}}}. You have to
configure [:HowtoEnableCron] before you continue.

Do:

{{{
crontab -e
}}}

Insert a line like this:

{{{
0 22 * * * /usr/sbin/ez-ipupdate -c /etc/ez-ipupdate.conf &
}}}

When finished do {{{ESC}}} and {{{:wq}}} to save it. You can check it with
{{{crontab -l}}}. This will execute {{{ez-ipupdate}}} every day at 10:00 pm.

There are some cron job calculators around the Internet. They maybe helpful
for you. One of them is [http://www.csgnetwork.com/crongen.html].


== Debugging ==

To check if ez-ipupdate really updated your IP look at the contents of the
file {{{/tmp/ez-ipup}}}:

{{{
test -f /tmp/ez-ipup && cat /tmp/ez-ipup
}}}

The dump of my {{{/tmp/ez-ipup}}} file:

{{{
1127182459,aaa.bbb.ccc.ddd
}}}

The first number is a Unix timestamp. And {{{aaa.bbb.ccc.ddd}}} is your current
IP address. You can checkout your current IP address with [http://www.whatismyip.com/]
or [http://www.whatismyip.org/].

For advanced debugging enable the {{{debug}}} parameter in the configuration file.


= Useful links =

For more details please have a look at the links below.

[[BR]]- [http://en.wikipedia.org/wiki/Ddns]
[[BR]]- [http://www.ez-ipupdate.com/]
