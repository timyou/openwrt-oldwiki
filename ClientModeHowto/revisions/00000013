= Client mode =

If you want to use your WRT to connect to another AP or computer rather than to use it as an AP, here are the steps to follow:

== Setting up client mode ==

If you have internet access from the WRT, it's a good moment to install the wl package, that we'll need later.

{{{ipkg install http://nthill.free.fr/openwrt/ipkg/stable/20041003/wl_0.1-2_mipsel.ipk}}}

The first step is breaking down the default bridge between the wifi interface and the LAN ports. Note that we're using the wan_ifname to refer to the wireless connection; this will save you from having to rewrite the firewall:

{{{
nvram set lan_ifname=vlan0		#  "vlan2" on hardware version 1.x
nvram set wan_ifname=eth1		#  "eth2" on hardware version 1.x
}}}

This is the main command. It changes the WRT's behavior from AP to client, or station ("sta" for short):

{{{
nvram set wl0_mode=sta
}}}

Then configure the interaces normally. For example, assuming the wifi interface uses DHCP and the LAN interface has the static IP address 192.168.1.1:

{{{
nvram set lan_proto=static
nvram set lan_ipaddr=192.168.1.1
nvram set wan_proto=dhcp
}}}

You can configure other options if you need to, like wifi_dns or wifi_gateway. 
We are done with NVRAM, so we commit and reboot the WRT:

{{{
nvram commit
reboot
}}}

== Finding and joining networks ==

You can now scan for nearby access points.

{{{
wl scan ; sleep 1 ; wl scanresults
}}}

if you get an eth error, try 

{{{
wl ap 0
}}}

This will put it into client mode

To join a non-encrypted access point you type:

{{{
wl join MyNetwork
}}}
or, with a network key:
{{{
wl join MyNetwork key 736576656E
}}}

You can tell WRT to join the same SSID each time it boots by setting wl0_ssid:

{{{
nvram set wl0_ssid=MyNetwork
}}}

To use WEP, set the variables wl0_wep and wl0_key1 (in hex)

{{{
nvram set wl0_wep=enabled
nvram set wl0_key1=736576656E
}}}

Don't forget!

{{{
nvram commit
}}}

When you set an interface to DHCP, OpenWRT runs the DHCP client on that interface automatically at boot time. If you want to re-run the client, for example because you joined another ssid, you can reboot (assuming you also set wl0_ssid nvram variable), or you can run the udhcpc command:

{{{
udhcpc -i eth1 -b
}}}

This will ask the network for an IP address over the interface eth1 (wifi in v2), and fork to the background if it gets no replies.

If you want to have the wired clients getting their ip-config with dhcp, you have to configure that as well.
The dhcp-server configuration is in /etc/dnsmasq.conf
Break the link to make it editable and make it survive a reboot:

{{{
cp -f /rom/etc/dnsmasq.conf /etc/
}}}

Then use vi to edit the line which starts with 'except-interface=vlan1'. Now you want the dhcp-server to listen
on vlan1, but not offer any leases on eth1 (that would be bad!). Change the line to read
{{{
except-interface=eth1
}}}

Since my router gives me ip-addresses on 192.168.1.* already, I changed my OpenWrt to use 192.168.10.*:
I changed the line that starts with dhcp-range as follows
{{{
dhcp-range=192.168.10.100,192.168.10.250,255.255.255.0,12h
}}}

and then set the interface accordingly:
{{{
nvram set lan_ipaddr=192.168.1.1
nvram commit
reboot
}}}

The command wl manages the radio, and it's pretty powerful. Among many options (see them here: http://wifi-portal.elevate.nl/docs/wl.txt.). There are some  particulary interesting:

{{{
wl txpwr
}}}
: change the transmit power. Accepts a value between 0-255, which I've heard it's in mW, but don't know for sure. It's said that setting a high value here (above 84) will shorten the live of your radio to the point that setting it to 250 will make it last some months. Use this setting at your own risk.

{{{
wl txant / wl antdiv
}}}
: this commands will let you choose which antenna will be used to send and receive respectively. This is usually useful if you have replaced an antenna. 0 means main antenna (the one near the power plug) and 1 means the other antenna. 

{{{
wl status
}}}
: prints the current ssid, signal quality, channel... etc.

{{{
wl dissasoc
}}}
: dissasociates from the current ssid

{{{
wl rate
}}}
: sets/gets the speed rate. To set it to auto, use -1.

That's all what comes to my head now. If you have questions/comments about client mode write to switch at euskalnet.net.

NOTE: A lot of info was taken from http://wifi-portal.elevate.nl/docs/clientmode.html. Thanks to whoever wrote that page (I wasn't able to find his name).


== Try these scripts to make life easy ==
###
### Old script removed; set nvram variables correctly and use ifup
### see above.

{{{
#!/bin/sh
# Scan script, "scan c" will be continuous

wl ap 0
while [ 1 ]; do
wl scan
sleep 1
if [ $# -eq 1 ]
  then
    clear
    wl scanresults | grep -B 1 Mode
  else
    wl scanresults
    break
fi
done
}}}
