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

The base configuration is to install the olsrd package on a OpenWrt router. 

So, assuming that you have OpenWrt installed and correctly configured (e.g., your ipkg configuration is correct), you can see which olsrd package is available in the ipkg repositories that you have access to:

{{{
  ipkg update
  ipkg list | grep olsrd
}}}

You should see a number of olsr-related packages.  The package named simply, "olsrd" is the primary daemon process, and the others that you see such as olsrd-mod-dyn-gw are plugins (olsrd is very extensible and has great plugin support).

Assuming that you saw an olsrd package, install it with {{{ipkg install olsrd}}}.

2. Edit the /etc/olsrd.conf file
  . In the lower side of the olsrd.conf file you see Interface "XXX" just change XXX to your wireless interface which was eth1 in my case

''''''

{{{
  Interface "eth1" 
{  #IPv4 broadcast address to use.The 
   #one usefull example would be 255.255.255.255

}}}

 . Then you just need to run the command olsrd and it should take the default values and run.

3. Modifying  /etc./firewall.user      for OLSR network Now as the bridge br0 is broken we have to add a few lines into firewalll scripts so as to have proper functioning.The following are basic rules required

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

4.Running OLSR on startup

Well if you need olsr to run on the startup then we have to make a startup script in /etc/init.d/S60olsrd

{{{
#!/bin/sh
/bin/olsrd
}}}

[Todo: explanation of HNA4, plugins, negative weights etc ]

= References =

* [http://www.olsr.org www.olsr.org] :Read main thesis and rfc
* [http://nbd.name/openwrt Manual for Kamikaze by one of the developers]
* [http://wiki.openwrt.org/OpenWrtDocs Main wiki documentation for OpenWrt]

----
 . CategoryHowTo 
