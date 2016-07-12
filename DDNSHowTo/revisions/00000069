'''DDNS howto'''

[[TableOfContents]]
= About Dynamic DNS (DDNS) =
The DDNS service comes in handy for establishing connections from computers on the Internet to your network at home. This is especially useful if you want to run server software or ssh on your OpenWRT and only have a dynamic IP.

!OpenWrt uses the package {{{ez-ipupdate}}} for providing DDNS service.

= Requirements =
 * A recent OpenWrt version. This howto was written for the 'White Russian RC5' and later releases.
 * An account with a compatible DDNS service (see Configuration)

= Installation =
Since December 2006, ez-ipupdate is part of the standard package repository of White Russian RC6. For installation, just use the commands
{{{
ipkg update
ipkg install ez-ipupdate
}}}

= Configuration =
ez-ipupdate can be used with the following services:

 * http://www.justlinux.com
 * http://www.dhs.org
 * http://www.dyndns.org
 * http://www.ods.org
 * http://gnudip.cheapnet.net (GNUDip)
 * http://www.dyn.ca (GNUDip)
 * http://www.tzo.com
 * http://www.easydns.com
 * http://www.dyns.cx
 * http://www.zoneedit.com
 * http://www.ez-ip.net (Looks dead - domain squatter...)
 * http://www.hn.org (Closed according to notice on site.)

ez-ipupdate cannot be used with No-IP.com's service. For that use the [:No-IP.comHowTo:noip client]

== Creating the configuration file ==
As of White Russian RC5, the ez-ipupdate package comes with a template configuration file in {{{/etc/ez-ipupdate.conf}}}. You must edit it to reflect your service-type, user, password and host (domain) name:

{{{
service-type=zoneedit
user=myname:mypassword
host=mydomain.com
quiet

# Do not change the lines below
cache-file=/tmp/ez-ipupdate.cache
pid-file=/var/run/ez-ipupdate.pid
}}}

/!\ '''NOTE:''' With White Russian RC5 or newer, there is no more need for an {{{interface}}} line if you use the hotplug mechanism (which is default now). You only have to set it when using cron or daemon mode as decribed at the end of this howto.

/!\ '''NOTE:''' You should point the cache-file to a permanent location in the jffs tree if your router is rebooted more often than your ip actually changes. Otherwise your previous ip is forgotten over reboots and your DDNS provider might lock you out for unneccessary updates.

/!\ '''NOTE:''' There's a modified version of ez-ipupdate (http://ouaye.net/files/ez-ipupdate_3.0.11b8-2_mipsel.ipk announced in 
http://forum.openwrt.org/viewtopic.php?pid=39855) which adds the feature of announcing the WAN IP retrieved from an external web (e.g. checkip). This is usefull if your OpenWRT is behind a modem-router. Anyway, you first need to install the whiterussian one (ipkg install ez-ipupdate) and then install the modified one (ipkg install http://ouaye.net/files/ez-ipupdate_3.0.11b8-2_mipsel.ipk). Then, a few files need to be manually modified:

''/etc/hotplug.d/iface/10-ez-update'':
{{{
. /etc/functions.sh
NAME=ez-ipupdate
CONFIG=/etc/$NAME/$NAME.conf
COMMAND=/usr/sbin/$NAME
[ "$ACTION" = "ifup" -a "$INTERFACE" = "wan" ] && {
        [ -x $COMMAND ] && [ -r $CONFIG ] && {
                if [ -n "$(grep web-detect $CONFIG)" ]; then
                        $COMMAND -c $CONFIG 2>&1 | logger -t $NAME
                else
                        IFNAME=$(nvram get ${INTERFACE}_ifname)
                        $COMMAND -c $CONFIG -i $IFNAME 2>&1 | logger -t $NAME
                fi
        } &
}
}}}

''/etc/init.d/S52ez-ipupdate'':
{{{
...
                   echo -n "Starting ez-ipupdate:..."
                   if [ -n "$(grep web-detect $ddns_conf)" ]; then
                     /usr/sbin/ez-ipupdate -d -F $PID_F -c $ddns_conf -b $ddns_cache -e $ddns_exec_ok
                   else
                     /usr/sbin/ez-ipupdate -d -F $PID_F -c $ddns_conf -b $ddns_cache -i $wan_interface -e $ddns_exec_ok
                   fi
...
}}}

''/etc/ez-ipupdate/ez-ipupdate.conf'' (after configuring with webif, if applicable):
{{{
service-type=dyndns
user=user:password
host=dynamiciphost
interface=web-detect

# Do not change the lines below
cache-file=/etc/ez-ipupdate/ez-ipupdate.cache
pid-file=/var/run/ez-ipupdate.pid
max-interval=86400
}}}

''Open issues'':
 * /etc/ez-ipupdate.conf is no longer usefull
 * Both start scripts (hotplug.d and init.d) are not assuming the same information if unmodified

'''END NOTE'''

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
== Via hotplug (recommended and default) ==
This updates your DDNS every time a WAN connection gets etablished. Since White Russian RC5 the hotplug script is included in the ez-ipupdate package.

Unfortunately, as of version 3.0.11b8-2 in White Russian RC6, the hotplug script {{{/etc/hotplug.d/iface/10-ez-ipupdate}}} is broken, since it uses the obsolete {{{"include /lib/network"}}} mechanism. To make it work, you must edit it to invoke {{{nvram}}} directly, which is just the way the other scripts were adapted:
{{{
NAME=ez-ipupdate
CONFIG=/etc/$NAME.conf
COMMAND=/usr/sbin/$NAME

[ "$ACTION" = "ifup" -a "$INTERFACE" = "wan" ] && {
        [ -x $COMMAND ] && [ -r $CONFIG ] && {
                        ifname=$(nvram get ${INTERFACE}_ifname)
                        [ -n "$ifname" ] && \
                          $COMMAND -c $CONFIG -i $ifname 2>&1 | logger -t $NAME
        } &
}
}}}

For a test run, temporarilly remove the {{{quiet}}} option from the config and do:

{{{
ifdown wan && ifup wan
}}}

You can see ez-ipupdate's output with the {{{logread}}} command.

Dyndns requires periodic updates no longer than 30 days in order to keep your DNS names. If 
you seldom reset your router, or your WAN connection is usually stable, hotplug may not be enough. 
Use cronjob described below to update your Dyndns records weekly in case they are expired.

== Manually via the command line ==
{{{
/usr/sbin/ez-ipupdate -c /etc/ez-ipupdate.conf -i replacethiswithyourinterface}}}

== Via init script (obsolete) ==
{{{
cat > /etc/init.d/ez-ipupdate
}}}

{{{
#!/bin/sh

#ip-ezupdate requires the interface on the command line in daemon mode
INT=eth0
BIN=ez-ipupdate
CONF=/etc/$BIN.conf
RUN_D=/var/run
PID_F=$RUN_D/$BIN.pid
[ -f $CONF ] || exit

case $1 in
 start)
  mkdir -p $RUN_D
  $BIN -d -i $INT -c $CONF
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

ez-ipupdate will now be run as a daemon when OpenWrt is started and update IP address automatically when needed.

To start it now, do:

{{{
/etc/init.d/ez-ipupdate start
}}}

== Via a cronjob (obsolote) ==
This updates your DDNS account on a specified time via {{{crond}}}. You have to configure HowtoEnableCron before you continue.

Do:

{{{
crontab -e
}}}

Insert a line like this:

{{{
0 22 * * * /usr/sbin/ez-ipupdate -c /etc/ez-ipupdate.conf &
}}}

When finished do {{{ESC}}} and {{{:wq}}} to save it. You can check it with {{{crontab -l}}}. This will execute {{{ez-ipupdate}}} every day at 10:00 pm.

There are some cron job calculators around the Internet. They maybe helpful for you. One of them is http://www.csgnetwork.com/crongen.html.

== Debugging ==
To check if ez-ipupdate really updated your IP look at the contents of the file {{{/tmp/ez-ipupdate.cache}}}:

{{{
test -f /tmp/ez-ipupdate.cache && cat /tmp/ez-ipupdate.cache
}}}

The dump of my {{{/tmp/ez-ipupdate.cache}}} file:

{{{
1127182459,aaa.bbb.ccc.ddd
}}}

The first number is a Unix timestamp. And {{{aaa.bbb.ccc.ddd}}} is your current IP address. You can checkout your current IP address with http://www.whatismyip.com/ or http://www.whatismyip.org/.

For advanced debugging enable the {{{debug}}} parameter in the configuration file.

== Multiple Hostnames ==
If you have more than one hostname registered and would like to update them all to the same IP via ez-ipupdate, then simply specify a comma-separated list of hostnames in ez-ipupdate.conf

{{{
service-type=dyndns
user=myname:mypassword
host=first.com,second.com,third.com
quiet

# Do not change the lines below
cache-file=/tmp/ez-ipupdate.cache
pid-file=/var/run/ez-ipupdate.pid
}}}

= Useful links =
For more details please have a look at the links below.

http://en.wikipedia.org/wiki/Ddns http://www.ez-ipupdate.com/
