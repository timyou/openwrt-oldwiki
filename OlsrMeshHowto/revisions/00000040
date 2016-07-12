= Introduction =

Mesh networks self-arrange and auto-configure themselves on the basis of network topology changes.  For example, the properly configured OLSR mesh will automatically arrange itself in cases where one node fails, or when a new route emerges, or when a low traffic route becomes available or disappears.  The concept of a mesh network is not new; the Internet itself is a huge mesh network.  So what's new?  Well, mesh networks with wireless technology on OpenWrt simply rocks! ;)

OLSR is one of the routing protocols available to create a [http://en.wikipedia.org/wiki/Mobile_ad-hoc_network Mobile Adhoc Networks (MANET)], or rather, in more general terms, a wireless mesh network.  [http://www.olsr.org The OLSR code developed by Andreas Tønnesen] is the best suited for our case as packages have been created for OpenWrt.

This wiki page contains information on how to create an OLSR mesh network by configuring OpenWrt and olsrd (the OLSR daemon process) yourself.  If your objective is to get an OLSR network quickly running, you may want to have a look at firmware that has been specifically created for this purpose.  An example of this sort of firmare is the [http://firmware.freifunk.net Freifunk project].  If you're determined to get OLSR running on OpenWrt without the assistance of pre-packaged firmare, keep reading!


= The Network =

There are an infinite number of ways that a mesh network can be configured; below is a simple example that allows routing over a set of subnets in the 10.0.0.0/255.0.0.0 range through the OLSR mesh.

{{{

      WAN                                                 WAN
       |                                                   |
OpenWrt + OLSR Node 1 ---- wireless link ---- OpenWrt + OLSR Node 2
       |                                                   |
      LAN                                                 LAN
       |                                                   |
  Workstation A                                      Workstation B

}}}

Both nodes (in this case the ["OpenWrtDocs/Hardware/Linksys/WRT54GL"] was used) need to have OLSR installed.  In general, OLSR will have to be installed on any node that participates in establishing routing between the OLSR-aware subnets that you configure.  OLSR needs to be configured to listen on all WIFI interfaces on these routers.  Running it on wired interfaces is usually not necessary, and according to some sources may interfere with other services on these interfaces such as dhcp.

If the "wired" interfaces on your router are on a different subnet from the wireless interfaces you can configure OLSR to distribute ''host and network association'' (HNA) messsages to other routers.  Depending on if if you are running IPv4 or IPv6 you will either have Hna4 or Hna6 directives in your olsrd.conf file.


= HOW TO =

1. Setting up wireless on your router

You will have to configure wireless networking on your router.  If you are on a Kamikaze release, your file /etc/config/wireless might look as follows:

{{{
config wifi-device  wl0
        option type     broadcom
        option channel  11
        # disable radio to prevent an open ap after reflashing:
        option disabled 0

config wifi-iface
        option device   wl0
        # option network        lan
        option mode     adhoc
        option ssid     OLSR
        option hidden   0
        option encryption none
}}}

After a fresh install of OpenWrt, you'll probably have to enable the wireless interface by modifying the "option disabled" line.  You'll also have to change the wireless interface to adhoc mode from the default of "ap".

You'll also have to separate the wifi and lan interfaces.  This is done by  in Ad Hoc mode with Lan and Wifi seperate (ie. no br0)

1. Install olsrd

Assuming that you have OpenWrt installed and correctly configured (e.g., your ipkg configuration is correct), you can see which olsrd package is available in the ipkg repositories that you have access to:

{{{
  ipkg update
  ipkg list | grep olsrd
}}}

You should see a number of olsr-related packages.  The package named "olsrd" is the primary daemon process, and the others that you see such as olsrd-mod-dyn-gw are plugins (olsrd is very extensible and has great plugin support).

Assuming that you saw an olsrd package after the command above, install it with {{{ipkg install olsrd}}}.

2. Edit the /etc/olsrd.conf file

You will see a line in your olsrd.conf file that says {{{Interface "XXX"}}}.  Change "XXX" to the wireless interface on your router.  In my case, this was wl0.

The rest of the defaults in the file should work.  Try {{{/etc/init.d/olsrd start}}} to see if it works.

Below is the full olsrd.conf that I use on my production system:

{{{
###
# olsr.org OLSR daemon config file
# /etc/olsrd.conf
#
# Modified for sample OLSR network by Justin S. Leiteb
# http://justin.phq.org/ Fri Jun  8 10:34:27 EDT 2007
# Many comments and commented line from conf file distributed
# with olsrd omitted for brevity in wiki.
###

DebugLevel	0
IpVersion	4
ClearScreen     yes

## HNA - for non-olsr networks connected to this node.
# On the second OLSR node (olsrd.conf not supplied for this node, since only one line is different), 
# which has a LAN interface on the 10.100.2.0/255.255.255.0 network, the Hna4 entry is: 
# 10.100.2.0 255.255.255.0.  These Hna4 entries are what propagates information about how to route 
# to these subnets through the mesh.
Hna4
{
	# My home LAN
	10.100.1.0  255.255.255.0
}

AllowNoInt	yes
UseHysteresis	yes

# Hysteresis parameters
HystScaling	0.50
HystThrHigh	0.80
HystThrLow	0.30


LinkQualityLevel	0
Pollrate	0.05
NicChgsPollInt  3.0

Interface "wl0"
{
    AutoDetectChanges            yes
}

# Run http server with mesh information.  Won't work unless you've already installed
# the olsrd_httpinfo plugin through ipkg.
LoadPlugin "olsrd_httpinfo.so.0.1"
{
	PlParam		"port"	"1979"
	PlParam		"Net"	"0.0.0.0 0.0.0.0"
}
}}}


3. Configuring the firewall for OLSR

You will have to make some changes to /etc/firewall.user for your OLSR mesh to function.  This will allow the router to forward packets between the interfaces, including the WIFI and LAN interfaces that you separated earlier.

The following is an example firewall.user that was supplied for what appears to be a WhiteRussian system, however it will not work on Kamikaze:

{{{
#!/bin/sh
 . /etc/functions.sh
 
 WAN=$(nvram get wan_ifname)
 LAN=$(nvram get lan_ifname)
 WIFI=$(nvram get wifi_ifname)
 
 iptables -F input_rule
 iptables -F output_rule
 iptables -F forwarding_rule
 iptables -t nat -F prerouting_rule
 iptables -t nat -F postrouting_rule

# For forwarding WAN (internet) to WIFI

 iptables -A forwarding_rule -i $WAN  -o $WIFI  -j  ACCEPT 

# READER'S NOTE: After testing the above setting setting and not getting it to work I used the following line which seems to work fine. I remember noticing a comment somewhere stating that using '-i $WAN' is ignored, which could have been the cause. Notice that they are opposite. If only one of these settings are truely correct, please verify and remove the offending line.

 iptables -A forwarding_rule -i $WIFI  -o $WAN  -j  ACCEPT 

#For forwarding  LAN & WIFI in nodes
 
iptables -A forwarding_rule -i $LAN  -o $WIFI  -j  ACCEPT

 
#For WIFI clients to connect to node
 
iptables -A forwarding_rule -i $WIFI  -o $WIFI  -j  ACCEPT

#For connecting a Wired Lan client of node 1 to wired client of node 2

iptables -A forwarding_rule -i $LAN -o $LAN  -j  ACCEPT

}}}

The above won't work on Kamikaze in particular because nvram is no longer used for system configuration in this system.  Following is a firewall.user for a kamikaze system.  It works for an OLSR mesh running Kamikaze r7509.

{{{
#!/bin/sh

# Copyright (C) 2006 OpenWrt.org

iptables -F input_rule
iptables -F output_rule
iptables -F forwarding_rule
iptables -t nat -F prerouting_rule
iptables -t nat -F postrouting_rule

# The following chains are for traffic directed at the IP of the 
# WAN interface

iptables -F input_wan
iptables -F forwarding_wan
iptables -t nat -F prerouting_wan

# Does anyone have a command to get the name of the WIFI interface on Kamikaze so 
# that it doesn't have to be hard-coded here?  This is a bit sloppy it seems.
WIFI=wl0

## -- This allows port 22 to be answered by (dropbear on) the router
iptables        -A input_wan      -p tcp --dport 22 -j ACCEPT

# Allow connections to olsr info port.
iptables        -A input_wan      -p tcp --dport 1979 -j ACCEPT

# OLSR needs port 698 to transmit state messages. 
iptables -A input_rule -p udp --dport 698 -j ACCEPT

###################################################################
### START Rules that allow forwarding from one network to another.
### Rules based on openwrt wiki page:
###   http://wiki.openwrt.org/OlsrMeshHowto
###################################################################

# Debugging... do we have WIFI, LAN and WAN appropriately defined?
# These values are passed to us from /etc/init.d/firewall, which
# calls this script.

# echo WIFI == $WIFI
# echo LAN == $LAN
# echo WAN == $WAN

iptables -A forwarding_rule -i $WAN -o $WIFI -j ACCEPT

iptables -A forwarding_rule -i $WIFI -o $WAN -j ACCEPT

# For forwarding LAN & WIFI in nodes
iptables -A forwarding_rule -i $LAN -o $WIFI -j ACCEPT

# For WIFI clients to connect to nodes.
iptables -A forwarding_rule -i $WIFI -o $WIFI -j ACCEPT

# For connecting a wired lan client of node 1 to wired lan client of node 2
iptables -A forwarding_rule -i $LAN -o $LAN -j ACCEPT

# WIFI needs to go to LAN ports, too!
iptables -A forwarding_rule -i $WIFI -o $LAN -j ACCEPT
}}}

Now reboot your router for the changes to take effect.

4. Running OLSR on startup

After you have installed and configured olsrd to your liking, make it run when the router boots.  The debug level must be set to "0" in the olsrd.conf file for it to start.  Next, make a symbolic link in /etc/rc.d to the startup script:

{{{
ln -s /etc/init.d/olsrd /etc/rc.d/S60olsrd
}}}

5. Reboot and test

Reboot your router and test everything by pinging interfaces on the different devices.  Go and have a beverage of choice to celebrate!

= Configuration Notes and Tips =

 * The configuration above seems to work on Kamikaze only when the "Internet" (WAN) port on each Linksys wrt54g is used.  There seem to be iptables issues preventing the lan ports from working properly.

 * Kamikaze (up to release 7509) doesn't calculate broadcast addresses properly.  These need to be explicitly coded in to the /etc/config/network file for each interface as "broadcast x.x.x.x" parameters.

= After basic configuration =

You may want to check out some of the plugins that are easy to configure and show you the basic status of your mesh.  On my network I run olsrd-mod-httpinfo, which provides a basic http server that shows you the status of the mesh.

= References =

 * [http://www.olsr.org www.olsr.org Master's thesis of primary developer of olsrd] - should be read before attempting to install OLSR if you aren't clear on the fundamentals of how it works 
 * [http://nbd.name/openwrt Manual for Kamikaze by one of the developers] - great reference on networking interface configuration and other parts of the OpenWrt system
 * [http://wiki.openwrt.org/OpenWrtDocs Main wiki documentation for OpenWrt] - Of course! :)
