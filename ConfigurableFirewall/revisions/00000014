With a ConfigurableFirewall package OpenWRTs configuration of the firewall could be be very flexible yet easy. A nice solution seems to be the FireHOL firewall builder scripts. (available at http://firehol.sourceforge.net and in debian)

The script takes a configuration like the following:

 * /etc/firehol/FireholConf

To ease automatic configuration when installing packages it was proposed to split zone policy into separate files:

 * /etc/firehol/RedZone
 * /etc/firehol/OrangeZone
 * /etc/firehol/BlueZone
 * /etc/firehol/GreenZone

The firewall rules are then build and activated during startup:

 * /etc/init.d/S45Firewall

The boot script executes the /sbin/firehol shell script which in turn sources /lib/firehol/firehol and the configuration files.

= Shorewall HowTo =

== Introduction ==

=== What is it? ===

[http://www.shorewall.net/ Shorewall] is a popular set of shell scripts used to ease configuration of an iptables based firewall, and also allow a more complex set of firewall rules to be managed easily.

=== Why? ===

The default firewall for openwrt is very basic and not as robust as some would like. Shorewall also configures some advanced functionalities (not all supported by openwrt) that are harder to do by hand. Another possible advantage is that automating shorewall configuration through a web interface is not very hard.

== Requirements ==

You will require the following OpenWRT packages:

 * iproute2 (ip_2.0_mipsel.ipk)

You may require the following OpenWRT packages if you want the associated features:
 * IPSEC VPN
  * OpenSwan Packages (see OpenSwan HowTo)
  * Add line for [http://www.shorewall.net/IPSEC.htm ipsec tunnel] in {{{/etc/shorewall/tunnels}}}
 * IPV6 Tunnel
  * IPV6 Kernel modules (kmod-ipv6_2.4.20-1_mipsel.ipk)
  * IPT6 Kernel modules (kmod-ipt6_2.4.20-1_mipsel.ipk)
  * Add line for [http://www.shorewall.net/6to4.htm 6to4 tunnel] in {{{/etc/shorewall/tunnels}}}
 * Traffic Shaping
  * tc (tc_2.0_mipsel.ipk)
  * Set {{{TC_ENABLED=Yes}}} in {{{/etc/shorewall.conf}}}

First we need to download shorewall. I downloaded the latest stable [http://www.shorewall.net/pub/shorewall/2.0/shorewall-2.0.9/shorwall-2.0.9.lrp (2.09) LRP package]. The LRP package is made for the [http://leaf.sourceforge.net/ Linux Embedded Appliance Firewall] project, and thus is particularly suited to the needs of OpenWRT. The LRP Package is in fact just a tar.gz tarball, and you can rename it as such.

On the OpenWRT router: {{{
cd /tmp
wget http://www.shorewall.net/pub/shorewall/2.0/shorewall-2.0.9/shorwall-2.0.9.lrp
mv shorwall-2.0.9.lrp shorwall-2.0.9.tar.gz
}}}

== Installation ==
We can now simply extract the tarball into the root of the router. Make sure you have enough space before preceding, I have a WRT54GS so I'm a bit spoilt ;-): {{{
cd /
tar -xzvf /tmp/shorwall-2.0.9.tar.gz
}}}

This will extract the following files:{{{
-rwx------ root/root      2249 2004-04-05 17:23:28 etc/init.d/shorewall
drwx------ root/root         0 2004-09-23 18:55:35 etc/shorewall/
-rw------- root/root       691 2004-04-05 17:23:28 etc/shorewall/ecn
-rw------- root/root      1756 2004-05-14 09:40:31 etc/shorewall/nat
-rw------- root/root      1423 2004-04-05 17:23:28 etc/shorewall/tos
-rw------- root/root      7275 2004-05-18 12:47:39 etc/shorewall/interfaces
-rw------- root/root       244 2004-04-05 17:23:28 etc/shorewall/init
-rw------- root/root      4836 2004-09-23 18:48:42 etc/shorewall/masq
-rw------- root/root       291 2004-07-30 13:34:44 etc/shorewall/stop
-rw------- root/root      2282 2004-04-05 17:23:28 etc/shorewall/accounting
-rw------- root/root      4813 2004-05-14 09:40:31 etc/shorewall/hosts
-rw------- root/root     13580 2004-09-23 18:48:42 etc/shorewall/rules
-rw------- root/root       294 2004-07-30 13:34:33 etc/shorewall/start
-rw------- root/root     23254 2004-08-22 20:15:22 etc/shorewall/shorewall.conf
-rw------- root/root       589 2004-05-18 12:47:39 etc/shorewall/zones
-rw------- root/root       726 2004-04-05 17:23:28 etc/shorewall/maclist
-rw------- root/root      2645 2004-04-05 17:23:28 etc/shorewall/tcrules
drw------- root/root         0 2004-09-23 18:55:35 etc/shorewall/start.d/
-rw------- root/root       224 2004-04-05 17:23:28 etc/shorewall/stopped
-rw------- root/root       626 2004-04-05 17:23:28 etc/shorewall/modules
-rw------- root/root      3162 2004-04-05 17:23:28 etc/shorewall/tunnels
-rw------- root/root      1161 2004-09-23 18:48:42 etc/shorewall/actions
-rw------- root/root       684 2004-04-05 17:23:28 etc/shorewall/params
-rw------- root/root      3282 2004-05-18 12:47:39 etc/shorewall/policy
drw------- root/root         0 2004-09-23 18:55:35 etc/shorewall/stop.d/
-rw------- root/root      1019 2004-04-05 17:23:28 etc/shorewall/routestopped
-rw------- root/root      1696 2004-04-05 17:23:28 etc/shorewall/proxyarp
-rw------- root/root       326 2004-05-14 09:42:19 etc/shorewall/initdone
-rw------- root/root      1334 2004-04-05 17:23:28 etc/shorewall/blacklist
-rwx------ root/root     25192 2004-07-25 13:56:48 sbin/shorewall
drwx------ root/root         0 2004-09-23 18:55:35 usr/share/shorewall/
-rw------- root/root      9738 2004-06-12 12:39:54 usr/share/shorewall/help
-rw------- root/root       687 2004-04-05 17:23:28 usr/share/shorewall/action.DropSMB
-rw------- root/root       825 2004-04-05 17:23:28 usr/share/shorewall/rfc1918
-rw------- root/root       429 2004-07-16 16:38:59 usr/share/shorewall/action.Drop
-rw------- root/root       425 2004-04-05 17:23:28 usr/share/shorewall/action.AllowRdate
-rw------- root/root       493 2004-04-05 17:23:28 usr/share/shorewall/action.AllowTrcrt
-rw------- root/root       414 2004-04-05 17:23:28 usr/share/shorewall/action.DropPing
-rw------- root/root       432 2004-04-05 17:23:28 usr/share/shorewall/action.DropUPnP
-rw------- root/root       135 2004-05-18 12:58:26 usr/share/shorewall/configpath
-rw------- root/root      2464 2004-09-23 18:48:42 usr/share/shorewall/bogons
-rw------- root/root       442 2004-07-16 16:38:59 usr/share/shorewall/action.Reject
-rwx------ root/root    150419 2004-09-23 18:48:42 usr/share/shorewall/firewall
-rw------- root/root      1836 2004-07-16 16:38:59 usr/share/shorewall/actions.std
-rw------- root/root      5665 2004-05-18 10:30:22 usr/share/shorewall/action.template
-rw------- root/root       485 2004-04-05 17:23:28 usr/share/shorewall/action.AllowTelnet
-rw------- root/root     14370 2004-06-30 15:55:27 usr/share/shorewall/functions
-rw------- root/root         6 2004-09-23 18:48:42 usr/share/shorewall/version
-rw------- root/root       426 2004-04-05 17:23:28 usr/share/shorewall/action.AllowDNS
-rw------- root/root       476 2004-04-05 17:23:28 usr/share/shorewall/action.AllowFTP
-rw------- root/root       426 2004-04-05 17:23:28 usr/share/shorewall/action.AllowNTP
-rw------- root/root       412 2004-04-05 17:23:28 usr/share/shorewall/action.AllowPCA
-rw------- root/root       607 2004-04-05 17:23:28 usr/share/shorewall/action.AllowSMB
-rw------- root/root       400 2004-04-05 17:23:28 usr/share/shorewall/action.AllowSSH
-rw------- root/root       436 2004-04-05 17:23:28 usr/share/shorewall/action.AllowVNC
-rw------- root/root       429 2004-04-05 17:23:28 usr/share/shorewall/action.AllowWeb
-rw------- root/root       397 2004-04-05 17:23:28 usr/share/shorewall/action.AllowAuth
-rw------- root/root       461 2004-04-05 17:23:28 usr/share/shorewall/action.AllowIMAP
-rw------- root/root       417 2004-04-05 17:23:28 usr/share/shorewall/action.AllowNNTP
-rw------- root/root       474 2004-04-05 17:23:28 usr/share/shorewall/action.AllowPOP3
-rw------- root/root       410 2004-04-05 17:23:28 usr/share/shorewall/action.AllowPing
-rw------- root/root       626 2004-04-05 17:23:28 usr/share/shorewall/action.AllowSMTP
-rw------- root/root       433 2004-04-05 17:23:28 usr/share/shorewall/action.AllowSNMP
-rw------- root/root       452 2004-04-05 17:23:28 usr/share/shorewall/action.AllowVNCL
-rw------- root/root       426 2004-04-05 17:23:28 usr/share/shorewall/action.RejectAuth
-rw------- root/root       417 2004-04-05 17:23:28 usr/share/shorewall/action.DropDNSrep
-rw------- root/root       682 2004-04-05 17:23:28 usr/share/shorewall/action.RejectSMB
drwx------ root/root         0 2004-09-23 18:55:35 var/lib/shorewall/
-rw------- root/root      1440 2004-04-05 17:23:28 var/lib/lrpkg/shorwall.conf
-rw-r--r-- root/root        20 2004-05-24 17:33:55 var/lib/lrpkg/shorwall.exclude.list
-rw------- root/root        89 2004-06-24 11:20:08 var/lib/lrpkg/shorwall.help
-rw------- root/root       113 2004-05-14 09:40:31 var/lib/lrpkg/shorwall.list
lrwxrwxrwx root/root         0 2004-09-23 18:55:35 var/lib/lrpkg/shorwall.version -> ../../../usr/share/shorewall/version
}}}


The files under /var/lib are luckily LEAF specific, and part of the lrpkg package format. These files are not needed and will in fact be removed on the router's next reset since  /var uses the router's ram disk.

=== Configuration ===
This is the important part. Before we can use the shorewall firewall we will have to configure it so that it works on the OpenWRT set of interfaces, and also add any firewall rules that we may wish to have.

==== Configure Logging ====
The package we installed has been preconfigured for a LEAF router which uses the ULOG logging daemon. Thus the first change we need to make is to set shorewall to use syslogd. If you havn't already go syslogd running/configured on your system please see the mini-howto on "Setting up logging". The two files that contain the references to ULOG are: {{{
etc/shorewall/shorewall.conf:LOGNEWNOTSYN=ULOG
etc/shorewall/shorewall.conf:MACLIST_LOG_LEVEL=ULOG
etc/shorewall/shorewall.conf:TCP_FLAGS_LOG_LEVEL=ULOG
etc/shorewall/shorewall.conf:RFC1918_LOG_LEVEL=ULOG
etc/shorewall/shorewall.conf:SMURF_LOG_LEVEL=ULOG
etc/shorewall/shorewall.conf:BOGON_LOG_LEVEL=ULOG
etc/shorewall/policy:net                all             DROP            ULOG
etc/shorewall/policy:all                all             REJECT          ULOG
}}}

Replace each occourance of {{{ULOG}}} with {{{info}}} or some other valid Shorewall [http://www.shorewall.net/shorewall_logging.html logging level].

==== Configure Interfaces ====

Since the WRT54G uses a very unusual set of interfaces (bridge of switch and wireless used for internal network, etc) we will have to change the default interface configuration. On my WRT54GS my WAN (Internet) interface is {{{vlan1}}} and my LAN (internal interface) is {{{br0}}}. This may be different fro you, the easiest way to find out is to run the folling commands to find your WAN and LAN interfaces respectively:{{{
root@OpenWrt:~# nvram get wan_ifname
vlan1
root@OpenWrt:~# nvram get lan_ifname
br0
}}}

===== /etc/shorewall/interfaces =====
Now we know our WAN and LAN interfaces we can change configure Shorewall's interface configuration. Change the lines in {{{/etc/shorewall/interfaces}}} from:{{{
net     eth0            detect          dhcp,routefilter,norfc1918
loc     eth1            detect
}}}

to (substitute vlan0,br0 for your WAN and LAN interfaces respectively as found above):{{{
net     vlan1         detect          dhcp,routefilter,norfc1918
loc     br0           detect          dhcp,routeback
}}}

The dhcp options allow dhcp traffic through the WAN and LAN interfaces since our router attempts to get an address from the ISP through the WAN interface and serves DHCP addresses to clients on the LAN interface. The routeback option tells shorewall that the interface is virtual so it can handle the traffic flow this causes.

===== /etc/shorewall/masq =====
We will also need to configure the Masqueradeing rules with our interfaces, change the lines in {{{/etc/shorewall/masq}}} from:{{{
eth0                    eth1
}}}
to (again substitute vlan0,br0 for your WAN and LAN interfaces):{{{
vlan1                 br0
}}}
==== Remove TOS Support ====
Since the OpenWRT iptables hasn't got support for TOS, we have to remove the support from Shorewall, to do this comment out (or remove) all lines from {{{/etc/shorewall/tos}}}, in my case:{{{
#all  all             tcp             -               ssh             16
#all  all             tcp             ssh             -               16
#all  all             tcp             -               ftp             16
#all  all             tcp             ftp             -               16
#all  all             tcp             ftp-data        -               8
#all  all             tcp             -               ftp-data        8
}}}
