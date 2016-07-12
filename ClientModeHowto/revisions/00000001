

= Client mode =

If you want to use your WRT to connect to another AP or computer rather than to use it as an AP, here are the steps to follow:

== Setting up client mode ==

If you have internet access from the WRT, it's a good moment to install the wl package, that we'll need later.

{{{ipkg install http://nthill.free.fr/openwrt/ipkg/stable/20041003/wl_0.1-2_mipsel.ipk}}}

First reverse the firewall. Optionally, if you just want to disable it, you can delete the file /etc/init.d/S45firewall.
To reverse it, here is the content you should put in /etc/init.d/S45firewall:

{{{
#!/bin/sh
. /etc/functions.sh

WAN=$(nvram get wan_ifname)
WIFI=$(nvram get wifi_ifname)

IPT=/usr/sbin/iptables

for T in filter nat mangle ; do
  $IPT -t $T -F
  $IPT -t $T -X
done

$IPT -t filter -A INPUT -m state --state INVALID -j DROP
$IPT -t filter -A INPUT -m state --state RELATED,ESTABLISHED -j ACCEPT
$IPT -t filter -A INPUT -i $WIFI -j DROP

$IPT -t filter -A FORWARD -m state --state INVALID -j DROP
$IPT -t filter -A FORWARD -m state --state RELATED,ESTABLISHED -j ACCEPT
$IPT -t filter -A FORWARD -i $WIFI -j DROP
$IPT -t filter -A FORWARD -o $WIFI -p tcp --tcp-flags SYN,RST SYN -j TCPMSS --clamp-mss-to-pmtu
}}}
Optionally, if you want the source IP address of the outgoing traffic to be modified to the ip of the wifi interface, you should also add the following line:

{{{ $IPT -t nat -A POSTROUTING -o $WIFI -j MASQUERADE }}}

This is also known as doing NAT (Network Address Translation), and it's likely your case if you use the WRT to connect to the internet. If you want your outgoing traffic to keep the source IP address unchanged, don't add that line.

The next step is breaking down the default bridge between the wifi interface and the LAN ports. This is done as follows:

{{{
nvram set lan_ifname=vlan0		#  "vlan2" on hardware version 1
nvram set wifi_ifname=eth1		#  "eth2" on hardware version 1
}}}

This is the main command. It changes the WRT's behavior from AP to client, or station ("sta" for short):

{{{nvram set wl0_mode=sta}}}

Then configure the interaces normally. For example, assuming the wifi interface uses DHCP and the LAN interface has the static IP address 192.168.1.1:

{{{nvram set lan_proto=static
nvram set lan_ipaddr=192.168.1.1
nvram set wifi_proto=dhcp}}}

You can configure other options if you need to, like wifi_dns or wifi_gateway. 
We are done with NVRAM, so we commit and reboot the WRT:

{{{nvram commit
reboot}}}

== Finding and joining networks ==

You can now scan for nearby access points.

{{{wl scan ; sleep 1 ; wl scanresults}}}

To join a non-encrypted access point you type:

{{{wl join ssid}}}

You can tell WRT to join the same SSID each time it boots by setting wl0_ssid:

{{{nvram set wl0_ssid=MyNetwork}}}

When you set an interface to DHCP, OpenWRT runs the DHCP client on that interface automatically at boot time. If you want to re-run the client, for example because you joined another ssid, you can reboot (assuming you also set wl0_ssid nvram variable), or you can run the udhcpc command:

{{{udhcpc -i eth1 -b}}}

This will ask the network for an IP address over the interface eth1 (wifi in v2), and fork to the background if it gets no replies.

The command wl manages the radio, and it's pretty powerful. Among many options (see them here: http://wifi-portal.elevate.nl/docs/wl.txt.). There are some  particulary interesting:

{{{wl txpwr}}}: change the transmit power. Accepts a value between 0-255, which I've heard it's in mW, but don't know for sure. It's said that setting a high value here (above 84) will shorten the live of your radio to the point that setting it to 250 will make it last some months. Use this setting at your own risk.

{{{wl txant / wl antdiv}}}: this commands will let you choose which antenna will be used to send and receive respectively. This is usually useful if you have replaced an antenna. 0 means main antenna (the one near the power plug) and 1 means the other antenna. 

{{{wl status}}}: prints the current ssid, signal quality, channel... etc.

{{{wl dissasoc}}}: dissasociates from the current ssid

{{{wl rate}}}: sets/gets the speed rate. To set it to auto, use -1.

That's all what comes to my head now. If you have questions/comments about client mode write to switch at euskalnet.net.

NOTE: A lot of info was taken from http://wifi-portal.elevate.nl/docs/clientmode.html. Thanks to whoever wrote that page (I wasn't able to find his name).
