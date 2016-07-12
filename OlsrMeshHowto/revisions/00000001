
The following are the steps to have a Mesh Network with using Openwrt firmware on Linksys WRT54GL wifi routers running the Olsr protocol :



Consider a network of 4 nodes all having openwrt installed in it.

Step 1: Change to Adhoc Mode

nvram set wl0_infra=0       (for ad hoc mode)

nvram ser wl0_mode=sta   (client mode)


Step 2: Separate the LAN and WIFI By breaking the Br0 Bridge.

And assign a separate IP to LAN and WIFI

Reference:
 
nvram set lan_ifname=vlan0

nvram set lan_proto=static

nvram set lan_ipaddr=192.168.1.25

nvram set lan_netmask=255.255.255.0


nvram set wifi_ifname=eth1

nvram set wifi_proto=static

nvram set wifi_ipaddr=192.168.2.25

nvram set wifi_netmask=255.255.255.0


nvram set wan_ifname=vlan1

nvram set wan_proto=dhcp

nvram set lan_ifnames=vlan0 eth2 eth3

 


Only gateway terminal should have WAN enabled as needed rest all should have WAN as none


Also u may want to divide the antenna as:Left is Tx and Right is Rx

nvram set wl0_antdiv=0

nvram commit

reboot


Step 3: DHCP for wifi

Since the LAN WIFI Bridge in broken dnsmasq will give only DHCP address to LAN which is wired.

So to enable DHCP on wifi since I need that more edit  


 /etc/init.d/S50dnsmasq


!/bin/sh

. /etc/functions.sh

# interface to use for DHCP

iface=lan         <---#change this to wifi as iface=wifi #



……….

REST SCRIPT FOLLOWS AS IT IS


……….

REST SCRIPT FOLLOWS AS IT IS

………………….



Step 4: Firewall (etc/firewall.user)

Now the WAN and WIFI needs forwarding and WIFI and LAN (wired needs forwarding)

#This is for LAN(wired)  WIFI forwarding 
iptables -A forwarding_rule -i $LAN -o $WIFI -j ACCEPT

#This is for WAN WIFI forwarding 

 iptables -A forwarding_rule -i $WIFI -o $WAN -j ACCEPT



Step 5: Install OLSR plug-in

ipkg  update

ipkg install olsrd

To have olsr running in startup I edited /etc/init.d/rcS
and appended ‘olsrd’  command to it 

[It said that startup script should be ised as in /etc/init.d/ S**** but mine dint work :( ]


changes to be made in 

 /etc/olsrd.conf


1.  DebugLevel	0  <---To make olsrd run in background

2. Hna4
   { 

#Add the wired network address  here example

192.168.1.0 255.255.255.0  

#Note for a gateway which connects to internet add following

0.0.0.0  0.0.0.0

     }

3. Interface "eth1"  The interfaces on which olsr should run
 {
    # All The Blah Blah upto the next line can stay if not commented

    # Emission and validity intervals.

    # If not defined, RFC proposed values will

    # in most cases be used.

    #This is whats needed :

    HelloInterval	2.00

    HelloValidityTime	36.00

    TcInterval		4.00

    TcValidityTime	36.00

    MidInterval		6.00

    MidValidityTime	36.00

    HnaInterval		6.00

    HnaValidityTime	36.00

    #LinkQualityMult	default 1.0

    # Olsrd will choose links with the lowest value.

    #Weight	 0

}

#Above values take from freifunk  they work well for me.


Now when u give the command ‘olsrd’ in the CLI it should detatch from the current process after parsing the olsrd.conf file.Else it will say configuration  is ‘fubar’  


Step 6.WEP

Check if everything works

If yes add WEP 

wl0_wep=enabled

wl0_key=1

wl0_key1=xxx   (26 hexadecimal digits)

nvram commit  

reboot


Step 7:Use olsr switch  for windows from www.olsr.org  downloads section to see if things are working fine and 

nodes are up and running olsr




Reference::
www.olsr.org  :Read main thesis and rfc 
http://wiki.openwrt.org/OpenWrtDocs :Everything and anything in it

----
CategoryHowTo
