__'''Introduction'''__

Mesh networks are networks which are self arranging and auto configure themselves on the basis of topology changes.  For example, the mesh will automatically arrange itself in cases where one node fails, or when a new route emerges, or when a low traffic route becomes available or disappears.  The concept of mesh network is not new; the Internet itself is a huge mesh network.  So what's new?  Well, mesh networks with wireless simply rocks! ;)

OLSR is one of the routing protocol available to create a Mobile Adhoc Networks (MANET) or rather, in more general terms, a wireless Mesh network.  [http://www.olsr.org The OLSR code developed by Andreas Tønnesen] is the best suited for our case as packages have been created for OpenWrt.

If your objective, however, is to quickly create a mesh network you may want to have a look at firmware that has been specifically created for this purpose.  As of Friday, June 8, 2007 the [http://firmware.freifunk.net Freifunk Firmware] is maintained.  This package includes OpenWrt combined with the OLSR package mentioned above.  Below are steps that you can take to create an OLSR mesh by configuring OpenWrt and olsrd (the OLSR daemon process) yourself.

__'''The Network'''__

 . {{{
                          Wired to Lan Client (HNA4) 
                   (WAN)           |
                     |             / 
 Internet---------->Node1- - - - Node2 
                      ^           \ - - wifi to Client (Olsr/Non Olsr running client)
                      | 
                      |
               Wifi Link with olsr      
 }}}

Both Nodes(WRTs) need to have olsr installed.Same is the case for any n number of nodes participating.OLSR has to run on WIFI interface running it on wired interface is optional tho it wont be of much help.The non olsr interfaces (like WAN and wired client in the above case) are added by entering the network/ip address in the HNA4  field of the olsrd.conf file.

__'''HOW TO''' __ __ __ __ __ __ __

1.The Base Configuration:

 . The base configuration is install the olsr package on a OpenWrt router in Ad Hoc mode with Lan and Wifi seperate (ie. no br0)
  . {{{
  ipkg update
  ipkg install olsrd_0.4.10-1_mipsel.ipk  }}}
 2.Edit the /etc/olsrd.conf file
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

[Todo: explanation of HNA4  ,plugins ,negetive weights etc ]

Reference::

[http://www.olsr.org www.olsr.org] :Read main thesis and rfc

http://wiki.openwrt.org/OpenWrtDocs :Everything and anything in it

----
 . CategoryHowTo 
