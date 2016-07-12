'''DDNS howto'''

[[TableOfContents]]

= About Dynamic DNS (DDNS) =
The DDNS service comes in handy for establishing connections from computers on the Internet to your network at home. This is especially useful if you want to run server software or SSH on your !OpenWrt and only have a dynamic IP.

!OpenWrt uses the package {{{updatedd}}} for providing DDNS service.

/!\ '''Please note:''' ez-ipupdate has been critizied for various reasons in the !OpenWrt Forum. However, if you are using PPP or PPPoE (as often for DSL), you can use a simple script - no package needs to be installed. See at the end in the section '''ip-up Script Alternative'''.

= Requirements =
 * A recent OpenWrt version. This howto was written for the 'Kamikaze 7.07' and later releases.
 * An account with a compatible DDNS service (see Configuration)
= Installation =
Install the updatedd package and the plugin package for your DDNS service. <plugin> can be changeip, dyndns, eurodyndns, hn, noip, ods, ovh, regfish, tzo or zoneedit.

{{{
ipkg update
ipkg install updatedd updatedd-mod-<plugin>
}}}
= Configuration =
Updatedd can be used with the following services:

 * [http://www.changeip.com/ http://www.changeip.com]
 * http://www.dyndns.org
 * http://www.eurodns.com
 * http://www.hn.org (Closed according to notice on site.)
 * [http://www.dyns.cx http://www.no-ip.com]
 * http://www.ods.org
 * [http://www.dyn.ca http://www.ovh.com]
 * http://www.regfish.com
 * http://www.tzo.com
 * http://www.zoneedit.com
== The configuration file ==
Kamikaze uses UCI to configure the updatedd configuration file (/etc/config/updatedd).

=== Show the current configuration ===
Default configuration after installing the updatedd package.
{{{
uci show updatedd
}}}
{{{
updatedd.cfg1=updatedd
updatedd.cfg1.update=0
}}}

=== Add a new service ===
{{{
uci set updatedd.cfg1=updatedd
uci set updatedd.cfg1.service=dyndns
uci set updatedd.cfg1.user=<username>
uci set updatedd.cfg1.passwd=<password>
uci set updatedd.cfg1.host=<hostname>.dyndns.org
uci set updatedd.cfg1.update=1
uci set uci commit updatedd
}}}

The main configuration is done now.

=== Multiple Hostnames ===
If you have more than one hostname registered and would like to update them all to the same IP via updatedd, then simply add another section/config via UCI to /etc/config/updatedd.

{{{
uci set updatedd.cfg2=updatedd
uci set updatedd.cfg2.service=dyndns
uci set updatedd.cfg2.user=<username>
uci set updatedd.cfg2.passwd=<password>
uci set updatedd.cfg2.host=<hostname>.homelinux.org
uci set updatedd.cfg2.update=1
uci commit updatedd
}}}

=== Delete a service ===
{{{
uci del updatedd.cfg2
uci commit updatedd
}}}

= Starting DDNS =
== Via hotplug (recommended and default) ==
This updates your DDNS every time a WAN connection gets etablished.

For a test run, temporarilly remove the {{{quiet}}} option from the config and do:

{{{
ifdown wan && ifup wan
}}}
You can see updatedd's output with the {{{logread}}} command.

Dyndns requires periodic updates no longer than 30 days in order to keep your DNS names. If  you seldom reset your router, or your WAN connection is usually stable, hotplug may not be enough.  Use cronjob described below to update your Dyndns records weekly in case they are expired.

== Manually via the command line ==
{{{
...
}}}
== Via init script (obsolete) ==
To start it now, do:

{{{
/etc/init.d/updatedd start
}}}
== Via a cronjob (obsolote) ==
This updates your DDNS account on a specified time via {{{crond}}}. You have to configure HowtoEnableCron before you continue.

Do:

{{{
crontab -e
}}}
Insert a line like this:

{{{
0 22 * * * /etc/init.d/updatedd start &
}}}
When finished do {{{ESC}}} and {{{:wq}}} to save it. You can check it with {{{crontab -l}}}. This will execute {{{ez-ipupdate}}} every day at 10:00 pm.

There are some cron job calculators around the Internet. They maybe helpful for you. One of them is http://www.csgnetwork.com/crongen.html.

= ip-up Script Alternative =
If you are using PPP or PPPoE (as often for DSL), you can use a simple script, because the pppd supports to run scripts in case of interface changes.

Create the file /etc/ppp/ip-up.d/S01dyndns with the following content:

{{{
#!/bin/sh

USER="username"
PASS="password"
DOMAIN="yourhost.homeip.net"

registered=$(nslookup $DOMAIN|sed s/[^0-9.]//g|tail -n1)
current=$(wget -O - http://checkip.dyndns.org|sed s/[^0-9.]//g)
[ "$current" != "$registered" ] && {
	wget -O /dev/null http://$USER:$PASS@members.dyndns.org/nic/update?hostname=$DOMAIN &&
	registered=$current
}
sleep 3
newip=$(wget -O - http://checkip.dyndns.org|sed s/[^0-9.]//g)
newdns=$(nslookup $DOMAIN|sed s/[^0-9.]//g|tail -n1)
echo "Set ${newip} (DNS: ${newdns}), had ${current} (DNS: ${registered})" \
	| /usr/bin/logger -t ddupd
}}}
This script queries DNS to find the current registered address, compares it with the current external IP using the ''checkip'' Web Service to avoid unneeded updates.

The last two lines are for debug and can be ommitted. Often, DNS is not updated withhin the 3 seconds the script waits (at least it takes some seconds more until the clients recognise because of caching). By replacing the wget-update URL other DNS services should also be usable.

This script is heavily based on the nice pragmatic proposal of ''mbm'' here: http://forum.openwrt.org/viewtopic.php?pid=3947#p3947 Thanks you!
