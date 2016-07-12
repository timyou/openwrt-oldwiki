''('''Kamikaze users''': This HowTo was originally written in 2004; it applies to White Russian and Shorewall 2.09.  Shorewall 3.4 is now included in Kamikaze, and many things have changed.  Until an updated howto is written, Kamikaze users should probably run {{{ipkg install shorewall}}} and continue at the [http://www.shorewall.net/Documentation_Index.html Shorewall documentation pages].)''

== Introduction ==

=== What is it? ===

[http://www.shorewall.net/ Shorewall] is a popular set of shell scripts used to ease configuration of an iptables based firewall, and also allow a more complex set of firewall rules to be managed easily.

=== Why? ===

The default firewall for openwrt is very basic and not as robust as some would like. Shorewall also configures some advanced functionalities (not all supported by openwrt) that are harder to do by hand. Another possible advantage is that automating shorewall configuration through a web interface is not very hard.

== Quick Start (ipkg installation) ==
Instead of downloading and modifiying the original shorewall, you can build and/or install the ipkg I have made for OpenWRT. If you do you can skip the rest of the steps below, and go straight to the [http://www.shorewall.net/Documentation_Index.html Shorewall Documentation] on how to further configure your firewall from the defaults in the ipkg.

=== Installing the IPKG Package ===

Simply add the following line to {{{/etc/ipkg.conf}}}:{{{
src yani http://openwrt.wojjie.net/packages
}}}

Note: Another Shorewall package, of a more recent version, is available at http://openwrt.homelinux.net/

and run:{{{
ipkg update
ipkg install shorewall
}}}

ipkg should install the dependencies (iproute2 and iptables-saverestore) and procede to install shorewall. When completed you will be given instructions to check your configuration and when happy add the RC script so that it is loaded at boot time.

Make sure you have logging enabled as described in the Setting up Logging MiniHowtos.

=== Building the IPKG Package ===

If you want to build and install your own shorewall ipk see BuildingPackages to install an ipkg build environment and then:{{{
wget http://www.shorewall.net/pub/shorewall/2.0/shorewall-2.0.9/shorwall-2.0.9.lrp
wget http://openwrt.wojjie.net/src/iptables-saverestore.tar.gz
wget http://openwrt.wojjie.net/src/shorwall-2.0.9-ipkg.tar.gz
tar -xzvf iptables-saverestore.tar.gz
#(if you have built iptables-save/restore as shown below in howto)
#cp <buildrootpath>/build_mipsel/root/usr/sbin/iptables-* iptables-saverestore/usr/sbin/
fakeroot ipkg-build iptables-saverestore

mkdir ipkgroot
cd ipkgroot
tar -xzvf ../shorwall-2.0.9.lrp
tar -xzvf ../shorwall-2.0.9-ipkg.tar.gz
fakeroot ipkg-buildpackage -c
cd ..
}}}

And install:{{{
ipkg install iptables-saverestore_1.0_mipsel.ipk shorewall_2.0.9_all.ipk
}}}

== Requirements ==

You will require the following OpenWRT packages:

 * iproute2 (ip_2.0_mipsel.ipk)

You may require the following OpenWRT packages if you want the associated features:
 * OpenVPN
  * OpenVPN Packages
  * Add line for [http://www.shorewall.net/OPENVPN.html openvpn tunnel] in {{{/etc/shorewall/tunnels}}}
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
We can now simply extract the tarball into the root of the router. Make sure you have enough space before preceding, I have a WRT54GS so I'm a bit spoilt ;) : {{{
cd /
tar -xzvf /tmp/shorwall-2.0.9.tar.gz
}}}

This will extract the following files:{{{
-rwx------ root/root 2249 2004-04-05 17:23:28 etc/init.d/shorewall
drwx------ root/root 0 2004-09-23 18:55:35 etc/shorewall/
-rw------- root/root 691 2004-04-05 17:23:28 etc/shorewall/ecn
-rw------- root/root 1756 2004-05-14 09:40:31 etc/shorewall/nat
-rw------- root/root 1423 2004-04-05 17:23:28 etc/shorewall/tos
-rw------- root/root 7275 2004-05-18 12:47:39 etc/shorewall/interfaces
-rw------- root/root 244 2004-04-05 17:23:28 etc/shorewall/init
-rw------- root/root 4836 2004-09-23 18:48:42 etc/shorewall/masq
-rw------- root/root 291 2004-07-30 13:34:44 etc/shorewall/stop
-rw------- root/root 2282 2004-04-05 17:23:28 etc/shorewall/accounting
-rw------- root/root 4813 2004-05-14 09:40:31 etc/shorewall/hosts
-rw------- root/root 13580 2004-09-23 18:48:42 etc/shorewall/rules
-rw------- root/root 294 2004-07-30 13:34:33 etc/shorewall/start
-rw------- root/root 23254 2004-08-22 20:15:22 etc/shorewall/shorewall.conf
-rw------- root/root 589 2004-05-18 12:47:39 etc/shorewall/zones
-rw------- root/root 726 2004-04-05 17:23:28 etc/shorewall/maclist
-rw------- root/root 2645 2004-04-05 17:23:28 etc/shorewall/tcrules
drw------- root/root 0 2004-09-23 18:55:35 etc/shorewall/start.d/
-rw------- root/root 224 2004-04-05 17:23:28 etc/shorewall/stopped
-rw------- root/root 626 2004-04-05 17:23:28 etc/shorewall/modules
-rw------- root/root 3162 2004-04-05 17:23:28 etc/shorewall/tunnels
-rw------- root/root 1161 2004-09-23 18:48:42 etc/shorewall/actions
-rw------- root/root 684 2004-04-05 17:23:28 etc/shorewall/params
-rw------- root/root 3282 2004-05-18 12:47:39 etc/shorewall/policy
drw------- root/root 0 2004-09-23 18:55:35 etc/shorewall/stop.d/
-rw------- root/root 1019 2004-04-05 17:23:28 etc/shorewall/routestopped
-rw------- root/root 1696 2004-04-05 17:23:28 etc/shorewall/proxyarp
-rw------- root/root 326 2004-05-14 09:42:19 etc/shorewall/initdone
-rw------- root/root 1334 2004-04-05 17:23:28 etc/shorewall/blacklist
-rwx------ root/root 25192 2004-07-25 13:56:48 sbin/shorewall
drwx------ root/root 0 2004-09-23 18:55:35 usr/share/shorewall/
-rw------- root/root 9738 2004-06-12 12:39:54 usr/share/shorewall/help
-rw------- root/root 687 2004-04-05 17:23:28 usr/share/shorewall/action.DropSMB
-rw------- root/root 825 2004-04-05 17:23:28 usr/share/shorewall/rfc1918
-rw------- root/root 429 2004-07-16 16:38:59 usr/share/shorewall/action.Drop
-rw------- root/root 425 2004-04-05 17:23:28 usr/share/shorewall/action.AllowRdate
-rw------- root/root 493 2004-04-05 17:23:28 usr/share/shorewall/action.AllowTrcrt
-rw------- root/root 414 2004-04-05 17:23:28 usr/share/shorewall/action.DropPing
-rw------- root/root 432 2004-04-05 17:23:28 usr/share/shorewall/action.DropUPnP
-rw------- root/root 135 2004-05-18 12:58:26 usr/share/shorewall/configpath
-rw------- root/root 2464 2004-09-23 18:48:42 usr/share/shorewall/bogons
-rw------- root/root 442 2004-07-16 16:38:59 usr/share/shorewall/action.Reject
-rwx------ root/root 150419 2004-09-23 18:48:42 usr/share/shorewall/firewall
-rw------- root/root 1836 2004-07-16 16:38:59 usr/share/shorewall/actions.std
-rw------- root/root 5665 2004-05-18 10:30:22 usr/share/shorewall/action.template
-rw------- root/root 485 2004-04-05 17:23:28 usr/share/shorewall/action.AllowTelnet
-rw------- root/root 14370 2004-06-30 15:55:27 usr/share/shorewall/functions
-rw------- root/root 6 2004-09-23 18:48:42 usr/share/shorewall/version
-rw------- root/root 426 2004-04-05 17:23:28 usr/share/shorewall/action.AllowDNS
-rw------- root/root 476 2004-04-05 17:23:28 usr/share/shorewall/action.AllowFTP
-rw------- root/root 426 2004-04-05 17:23:28 usr/share/shorewall/action.AllowNTP
-rw------- root/root 412 2004-04-05 17:23:28 usr/share/shorewall/action.AllowPCA
-rw------- root/root 607 2004-04-05 17:23:28 usr/share/shorewall/action.AllowSMB
-rw------- root/root 400 2004-04-05 17:23:28 usr/share/shorewall/action.AllowSSH
-rw------- root/root 436 2004-04-05 17:23:28 usr/share/shorewall/action.AllowVNC
-rw------- root/root 429 2004-04-05 17:23:28 usr/share/shorewall/action.AllowWeb
-rw------- root/root 397 2004-04-05 17:23:28 usr/share/shorewall/action.AllowAuth
-rw------- root/root 461 2004-04-05 17:23:28 usr/share/shorewall/action.AllowIMAP
-rw------- root/root 417 2004-04-05 17:23:28 usr/share/shorewall/action.AllowNNTP
-rw------- root/root 474 2004-04-05 17:23:28 usr/share/shorewall/action.AllowPOP3
-rw------- root/root 410 2004-04-05 17:23:28 usr/share/shorewall/action.AllowPing
-rw------- root/root 626 2004-04-05 17:23:28 usr/share/shorewall/action.AllowSMTP
-rw------- root/root 433 2004-04-05 17:23:28 usr/share/shorewall/action.AllowSNMP
-rw------- root/root 452 2004-04-05 17:23:28 usr/share/shorewall/action.AllowVNCL
-rw------- root/root 426 2004-04-05 17:23:28 usr/share/shorewall/action.RejectAuth
-rw------- root/root 417 2004-04-05 17:23:28 usr/share/shorewall/action.DropDNSrep
-rw------- root/root 682 2004-04-05 17:23:28 usr/share/shorewall/action.RejectSMB
drwx------ root/root 0 2004-09-23 18:55:35 var/lib/shorewall/
-rw------- root/root 1440 2004-04-05 17:23:28 var/lib/lrpkg/shorwall.conf
-rw-r--r-- root/root 20 2004-05-24 17:33:55 var/lib/lrpkg/shorwall.exclude.list
-rw------- root/root 89 2004-06-24 11:20:08 var/lib/lrpkg/shorwall.help
-rw------- root/root 113 2004-05-14 09:40:31 var/lib/lrpkg/shorwall.list
lrwxrwxrwx root/root 0 2004-09-23 18:55:35 var/lib/lrpkg/shorwall.version -> ../../../usr/share/shorewall/version
}}}


The files under /var/lib are luckily LEAF specific, and part of the lrpkg package format. These files are not needed and will in fact be removed on the router's next reset since /var uses the router's ram disk.

=== Replacing Printf ===
The default openwrt busybox comes with printf removed, you have two choices:

 * Recompile busybox with printf support, and copy /usr/bin/printf to your router.
 * Replace printf calls in shorewall with echo/awk statements.

The second of these is actually easier and saves you quite a bit of space. The principle is that the printf that comes in the awk language is essentially the same as bash's printf, and you can replace{{{
printf '%7d %5d %s\n' $count $port $srv
}}}
with
{{{
echo $count $port $srv | awk '{printf("%7d %5d %s\n",$1,$2,$3)}'
}}}

You will need to do this a few times in /sbin/shorewall and /usr/share/firewall.

=== Configuration ===
This is the important part. Before we can use the shorewall firewall we will have to configure it so that it works on the OpenWRT set of interfaces, and also add any firewall rules that we may wish to have.

(Added by AndrewSteele: It's worth noting that you'll get strange errors like this:
{{{
Adding Common Rules
iptables: No chain/target/match by that name
   ERROR: Command "/usr/sbin/iptables -A smurfs -s 192.168.10.255  -j  LOG  --log-level info --log-prefix "Shorewall:smurfs:DROP:"" Failed
}}}
If you have not loaded in the ipt_LOG module.  I've spent months (on and off) trying to crack this!)

To do this first download the package which has the ipt_LOG module
{{{
ipkg install iptables-mod-extra
}}}
To load the module manually
{{{
insmod ipt_LOG.o
}}}
To load the module on startup create a file in /etc/modules.d/ directory (eg 90-shorewall) containing this
{{{
ipt_LOG.o
}}}
==== Configure Logging ====
The package we installed has been preconfigured for a LEAF router which uses the ULOG logging daemon. Thus the first change we need to make is to set shorewall to use syslogd. If you havn't already got syslogd running/configured on your system please see the mini-howto on "Setting up logging". The two files that contain the references to ULOG are: {{{
etc/shorewall/shorewall.conf:LOGNEWNOTSYN=ULOG
etc/shorewall/shorewall.conf:MACLIST_LOG_LEVEL=ULOG
etc/shorewall/shorewall.conf:TCP_FLAGS_LOG_LEVEL=ULOG
etc/shorewall/shorewall.conf:RFC1918_LOG_LEVEL=ULOG
etc/shorewall/shorewall.conf:SMURF_LOG_LEVEL=ULOG
etc/shorewall/shorewall.conf:BOGON_LOG_LEVEL=ULOG
etc/shorewall/policy:net all DROP ULOG
etc/shorewall/policy:all all REJECT ULOG
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
net eth0 detect dhcp,routefilter,norfc1918
loc eth1 detect
}}}

to (substitute vlan1, br0 for your WAN and LAN interfaces respectively as found above):{{{
net vlan1 detect dhcp,routefilter,norfc1918
loc br0 detect dhcp,routeback
}}}

The dhcp options allow dhcp traffic through the WAN and LAN interfaces since our router attempts to get an address from the ISP through the WAN interface and serves DHCP addresses to clients on the LAN interface. The routeback option tells shorewall that the interface is virtual so it can handle the traffic flow this causes.

===== /etc/shorewall/masq =====
We will also need to configure the Masqueradeing rules with our interfaces, change the lines in {{{/etc/shorewall/masq}}} from:{{{
eth0 eth1
}}}
to (again substitute vlan1, br0 for your WAN and LAN interfaces):{{{
vlan1 br0
}}}
==== Remove TOS Support ====
Since the OpenWRT iptables hasn't got support for TOS, we have to remove the support from Shorewall, to do this comment out (or remove) all lines from {{{/etc/shorewall/tos}}}, in my case:{{{
#all all tcp - ssh 16
#all all tcp ssh - 16
#all all tcp - ftp 16
#all all tcp ftp - 16
#all all tcp ftp-data - 8
#all all tcp - ftp-data 8
}}}

==== Configure Firewall Rules ====

===== /etc/shorewall/rules =====
Finally we will want to customize the firewall to a set of rules we define. You will probably want to start out with this basic configuration which you can set in {{{/etc/shorewall/rules}}}:{{{
#ACTION SOURCE DEST PROTO DEST SOURCE ORIGINAL RATE USER/
# PORT PORT(S) DEST LIMIT GROUP
# PORT PORT(S) DEST LIMIT

# Accept DNS connections from the firewall to the network
#
AllowDNS fw net

# Accept SSH connections from the local network for administration
#
AllowSSH loc fw

# Accept SSH connections from the internet for administration
#AllowSSH net fw

# Allow Ping To And From Firewall to local network
#
AllowPing loc fw
AllowPing fw loc
AllowPing fw net

# Allow Ping To Firewall from internet
#
#AllowPing net fw

#
# OpenWRT specific rules:
# allow loc to fw udp/53 for local/caching DNS servers to work
# allow loc to fw tcp/80 for weblet to work
# allow loc to fw udp/67 and udp/68 for dnsmasq's dhcpd to work
AllowDNS loc fw
AllowWeb loc fw

# Allow syslogd to send messages to loghost in LAN
#ACCEPT fw loc udp 514

#LAST LINE -- ADD YOUR ENTRIES BEFORE THIS ONE -- DO NOT REMOVE
}}}

===== /etc/shorewall/routestopped =====
You will also probably want to add the interface of your LAN to the {{{/etc/shorewall/routestopped}}} file which tells Shorewall what interface to accept connections from when the firewall is stopped (a good thing :) ). Without this shorewall will keep any current connections open however for `absent minded administrators'.

Add the following to {{{/etc/shorewall/routestopped}}}:{{{
br0 - routeback
}}}

===== /etc/shorewall/policy =====
By default shorewall comes configured so that the firewall hasn't got access to the internet itself for increased security, however with OpenWRT we want access to the internet if only to use the ipkg system. To allow access simply follow the instructions in {{{/etc/shorewall/policy}}} and uncomment the line as follows:{{{
# If you want open access to the Internet from your Firewall
# remove the comment from the following line.
fw net ACCEPT
}}}

=== Starting Shorewall at boot time ===

To automatically start shorewall at boot time we will want to add an RC script. Shorewall installs such a script in /etc/init.d/shorewall, however we will want to modify this and rename it so that it works with openWRT.

==== Editing RC Script ====

We can start with the shorewall rc script as a basis, first edit the script {{{/etc/init.d/shorewall}}} and change it so that it looks like this:{{{
################################################################################
# Give Usage Information #
################################################################################
usage() {
    echo "Usage: $0 start|stop|restart|status"
    exit 1
}

start() {
    echo "Starting Shorewall Firewall"
    #If saved rules exist, load them
    if [ -e /etc/shorewall/restore ]; then
        mkdir -p /var/lib/shorewall
        cp /etc/shorewall/restore /var/lib/shorewall/
        exec /sbin/shorewall restore | tee /var/log/shorewallstartup.log
    else
        #create the rules and save them in the background
        exec /sbin/shorewall start |tee /var/log/shorewallstartup.log &&\
         shorewall save && cp /var/lib/shorewall/restore /etc/shorewall/ &
    fi
}


################################################################################
# E X E C U T I O N B E G I N S H E R E #
################################################################################
command="$1"

mkdir -p /var/log
touch /var/log/shorewall.log

case "$command" in
    start)
        start
        ;;
    stop|restart|status)
        exec /sbin/shorewall $@
        ;;
    *)

        usage
        ;;

esac

}}}

==== Speeding up Shorewall startup with iptables-restore ====

This script will attempt to restore Shorewall using a Shorewall restore file (created using the command {{{shorewall save}}}) or will start Shorewall and attempt to create a restore file. Since Shorewall takes a long time to start (not restore) on the WRT54G it backgrounds this process. This process seems to take up to a few minutes(!).

The {{{shorewall restore}}} and {{{shorewall save}}} script however use the {{{iptables-save}}} and {{{iptables-restore}}} commands that are unfortunately pruned to save space when OpenWRT is built. You will likely want to install these however instead of waiting a few minutes for your firewall to startup each time your router boots. To get the files you must download the latest OpenWRT sources and in the {{{buildroot/make/openwrt.mk}}} file uncomment the following lines:{{{
        # remove other unneeded files
        #rm -f $(TARGET_DIR)/usr/sbin/iptables-save
        #rm -f $(TARGET_DIR)/usr/sbin/iptables-restore
}}}

After building OpenWRT as normal, copy the files:{{{
buildroot/build_mipsel/root/usr/sbin/iptables-save
buildroot/build_mipsel/root/usr/sbin/iptables-restore
}}}

to the {{{/usr/sbin/}}} directory on your router.

Now save the Shorewall configuration by starting our RC script:{{{
/etc/init.d/shorewall start
}}}

Before proceding make sure your script works properly (so you don't end up with a hung/inaccessible router on boot!) by starting and stopping Shorewall using the RC script:{{{
/etc/init.d/shorewall stop
/etc/init.d/shorewall start
}}}
==== Rename RC script so it is started at boot ====

Now we have our script working properly we must rename it so it is run on startup. First remove the file/symbolic link {{{/etc/init.d/S45firewall}}}, there is a backup of the original file at /rom/etc/init.d/S45firewall and rename our script to S45shorewall:{{{
rm /etc/init.d/S45firewall
mv /etc/init.d/shorewall /etc/init.d/S45shorewall
}}}

And we are finally done :) . Reboot the router and cross your fingers...

== Adding Traffic Shaping ==
Note: I am a newbie when it comes to TC and shorewall, but what I have works so here it is:

=== About Traffic Shaping ===
It is important to note that when you are running services that are very time/bandwidth sensitive that QoS or traffic shaping is very important.  The rules below are a good example to customize to your requirements; however, I will describe the design point that I used as I think it will match most people's requirements.

==== Traffic Shaping in General ====
The simple way of thinking of traffic shaping is this:  Consider all your traffic coming into a "router" of sorts.  This Router is aware of the types of traffic and will seperate it into a series of buckets.   The buckets all have a hole in the bottom to allow this sorted traffic through; however, these are special holes:
 * If bucket 1 has traffic in it, that traffic will flow, ignoring any traffic sitting in bucket 2 or 3.
 * If bucket 1 is empty, and bucket 2 has traffic.  Bucket 2's traffic will flow ignoring bucket 3 and,
 * If bucket 1 and 2 are empty, then the traffic in bucket 3 will flow.

Thus 1 will always get priority.

==== My Setup ====
 * I run a network where my main phone line is based on VoIP with an asterisk server and multiple internal and external extensions.
 * I run a webserver, mail server and other standard services
 * I run a few workstations that browse the internet
 * I have a system that is dedicated to P2P applications

Obviously I want my voice converstaions to be perfect and uninterrupted, and my P2P applications to use only unused bandwidth and not impact any of my other communications.  Thus here is how I will make 3 buckets to prioritize my traffic:
 1. VoIP traffic
 2. Default traffic
 3. P2P traffic

=== OpenWRT Configuration ===
 '''Requirements:'''
- tc
- shorewall
Note: You do not require the wondershaper.

==== Shorewall Configuration ====
Shorewall has the ability to setup all of the traffic shaping items; however, the package that is available for the openwrt doesnt seem to setup the classes or qdisc portions.  (only the tcrules file is processed), so we will use a combination of a manually setup tcstart script and the tcrules processed by shorewall.
===== /etc/shorewall/modules =====
Add the following lines to this file to add the required support{{{
 * loadmodule ipt_LOG  # Take care of logging issues noted above
}}}
===== /etc/shorewall/shorewall.conf =====
set the following:{{{
 * TC_ENABLED=Yes
 * CLEAR_TC=Yes
}}}
===== /etc/shorewall/tcrules =====
It is important to note that the '''Marks''' here are in decimal; however in the TCStart Script they are in hexdecimal: Thus 16 dec = 10 hex, 48 dec = 30 hex.
Set the following:
{{{
#MARK           SOURCE          DEST            PROTO   PORT(S) CLIENT  USER
#                                                               PORT(S)
# Allow good pings -- Doesnt work in OpenWRT ??
#1:P            0.0.0.0/0       0.0.0.0/0       icmp    echo-request
#1:P            0.0.0.0/0       0.0.0.0/0       icmp    echo-reply
# VOIP is highest priority
16              192.168.20.3    0.0.0.0/0       udp     5060,4569,10000:20000
# Primus VOIP also highest
16              192.168.20.15   0.0.0.0/0       udp
16              192.168.20.15   0.0.0.0/0       tcp
# Add the primus router here too

# P2P is lowest class traffic
##Azuerus on linux vm
48              0.0.0.0/0       0.0.0.0/0       tcp     9000:9010
48              0.0.0.0/0       0.0.0.0/0       udp     9000:9010
48              192.168.20.169  0.0.0.0/0       tcp
48              192.168.20.169  0.0.0.0/0       udp
# Everything else
# Caught in the "default"
}}}
===== /etc/shorewall/tcstart =====
This script will be called by shorewall automagically and needs to have chmod 744 set on it.
{{{
#!/bin/ash
# Wonder Shaper
# please read the README before filling out these values
#
# Set the following values to somewhat less than your actual download
# and uplink speed. In kilobits. Also set the device that is to be shaped.

DOWNLINK=5000
UPLINK=650
DEV=vlan1

if [ "$1" = "status" ]
then
        tc -s qdisc ls dev $DEV
        tc -s class ls dev $DEV
exit
fi

# clean existing down- and uplink qdiscs, hide errors
tc qdisc del dev $DEV root    2> /dev/null > /dev/null
tc qdisc del dev $DEV ingress 2> /dev/null > /dev/null

if [ "$1" = "stop" ]
then
        exit
fi
#Inserting various kernel modules -- Load better in /etc/shorwall/modules ??
insmod ipt_TOS
insmod ipt_tos
insmod ipt_length
insmod sch_prio
insmod sch_red
insmod sch_htb
insmod sch_sfq
insmod sch_ingress
insmod cls_tcindex
insmod cls_fw
insmod cls_route
insmod cls_u32

###### uplink
# install root HTB, point default traffic to 1:20:
tc qdisc add dev $DEV root handle 1: htb default 20

# shape everything at $UPLINK speed - this prevents huge queues in your
# DSL modem which destroy latency:
tc class add dev $DEV parent 1: classid 1:1 htb rate ${UPLINK}kbit burst 6k

# high prio class 1:10, med 1:20, and bulk 1:30:
tc class add dev $DEV parent 1:1 classid 1:10 htb rate ${UPLINK}kbit burst 6k prio 0

#Ash shell doesnt allow math in the string below, so I am using the let command
let RATE=9*$UPLINK/10
tc class add dev $DEV parent 1:1 classid 1:20 htb rate ${UPLINK}kbit burst 6k prio 1

let RATE2=8*$UPLINK/10
tc class add dev $DEV parent 1:1 classid 1:30 htb rate ${RATE2}kbit ceil ${RATE}kbit bu

# all get Stochastic Fairness:
tc qdisc add dev $DEV parent 1:10 handle 10: sfq perturb 10
tc qdisc add dev $DEV parent 1:20 handle 20: sfq perturb 10
tc qdisc add dev $DEV parent 1:30 handle 30: sfq perturb 10

# a different method of setting Fairness:  Dont know which is better
#tc qdisc add dev $DEV parent 1:10 handle 10: red limit 400000b min 10000b max 50000b a
#tc qdisc add dev $DEV parent 1:20 handle 20: red limit 400000b min 10000b max 50000b a
#tc qdisc add dev $DEV parent 1:30 handle 30: red limit 400000b min 10000b max 50000b a

# Setup filtering where handle 0x10 0x20 and 0x30 the hex versions of the marks defined in tcrules
tc filter add dev $DEV parent 1: protocol ip handle 0x30 fw flowid 1:30
tc filter add dev $DEV parent 1: protocol ip handle 0x20 fw flowid 1:20
tc filter add dev $DEV parent 1: protocol ip handle 0x10 fw flowid 1:10
}}}
===== Useful commands =====
  * tcstart status  -- This will give you the status of your "buckets"
  * iptables --show -t mangle  -- This will show you your "marking rules" for bucket sorting

===== Other useful points =====
Notice that we are only shaping outgoing traffic -- As it may make sense to shape incoming traffic, you need to stop and think a moment.   We need to receive the incoming traffic before we can shape it, and our LAN is not bandwidth limited like our WAN connection, so why bother shape it?  We have already received it...

Thankfully 95% of our latency issues surround two things: 1) incoming connection rate and 2) upload rate.   For 1, with proper configuration of our p2p clients we can handle this.  For 2, the above script works well.
----
CategoryHowTo
