#pragma section-numbers off
||<tablebgcolor="#f1f1ed" tablewidth="40%" tablestyle="margin: 0pt 0pt 1em 1em; float: right; font-size: 0.9em;"style="padding: 0.5em;">[[TableOfContents]]||
= Using Non-Bridged WiFi =
The default OpenWRT configuration bridges the !WiFi and LAN interfaces.  This gives any computer on your !WiFi network full access to your wired network.  The more paranoid among us prefer to separate the two interfaces.

This example assumes your !WiFi network will use 192.168.2.x, with the OpenWRT router on 192.168.2.1.  I'm using a [:OpenWrtDocs/Hardware/Linksys/WRT54GL:WRT54GL]; the details may vary on other devices.

== /etc/config/network ==

First, find the {{{config interface lan}}} section and delete the {{{option type bridge}}} line.  Note that this will change the name of your LAN interface.  On the [:OpenWrtDocs/Hardware/Linksys/WRT54GL:WRT54GL] it changes from `br-lan` to `eth0.0`.  This may require changes to your firewall configuration.

Then, add a new section to configure the !WiFi interface:
{{{
#### Wi-Fi LAN configuration
config interface wifi
	option ifname	"wl0"
	option proto	static
	option ipaddr	192.168.2.1
	option netmask	255.255.255.0}}}

== /etc/config/wireless ==

Make sure the device and network match the ones you defined in `/etc/config/network`.  It should look like this:

{{{
config wifi-iface
	option device	wl0
	option network	wifi}}}

You should also change the default SSID and [:OpenWrtDocs/KamikazeConfiguration/WiFiEncryption:enable encryption].  Once you've done that, remove the {{{option disabled 1}}} line, or the !WiFi interface won't operate.

== /etc/config/dhcp (optional) ==

If you want dnsmasq to provide DHCP services on your !WiFi network, you'll need to add a section enabling that:

{{{
config dhcp
	option interface	wifi
	option start 		100
	option limit		150
	option leasetime	4h}}}

= Shorewall =

Your !WiFi network should now be operational on 192.168.2.x after a reboot.  However, it will not be able to communicate with your LAN or the Internet until you set up the appropriate firewall rules.  It may be possible to do that with the default OpenWRT firewall, but I'm more familiar with Shorewall, so that's what I used.

I'm still using Shorewall 3.4, so I enabled the net/shorewall package from the packages repository.  The following setup is based on the [http://www.shorewall.net/3.0/three-interface.htm Shorewall three-interface configuration].

== /etc/shorewall/params ==

I recommend defining your interface names in `/etc/shorewall/params`.  This will aid both readability and portability (if you ever need to move your configuration to another device).

{{{
NET_IF=eth0.1
LOC_IF=eth0.0
WF_IF=wl0
#LAST LINE - ADD YOUR ENTRIES ABOVE THIS ONE - DO NOT REMOVE}}}

== /etc/shorewall/zones ==

{{{
#ZONE	TYPE	OPTIONS			IN			OUT
#					OPTIONS			OPTIONS
fw	firewall
net	ipv4
loc	ipv4
wifi	ipv4
#LAST LINE - ADD YOUR ENTRIES ABOVE THIS ONE - DO NOT REMOVE}}}

== /etc/shorewall/interfaces ==

{{{
#ZONE	INTERFACE	BROADCAST	OPTIONS
net	$NET_IF		detect		dhcp,tcpflags,routefilter,norfc1918,nosmurfs,logmartians
loc	$LOC_IF		detect		dhcp,tcpflags,detectnets,nosmurfs
wifi	$WF_IF		detect		dhcp,tcpflags,detectnets,nosmurfs
#LAST LINE -- ADD YOUR ENTRIES BEFORE THIS ONE -- DO NOT REMOVE}}}

== /etc/shorewall/masq ==

{{{
#INTERFACE		SOURCE		ADDRESS		PROTO	PORT(S)	IPSEC
$NET_IF			$LOC_IF
$NET_IF			$WF_IF
#LAST LINE -- ADD YOUR ENTRIES ABOVE THIS LINE -- DO NOT REMOVE}}}

== /etc/shorewall/policy ==

{{{
#SOURCE		DEST		POLICY		LOG LEVEL	LIMIT:BURST

#
# Note about policies and logging:
#	This file contains an explicit policy for every combination of
#	zones defined in this sample.  This is solely for the purpose of
#	providing more specific messages in the logs.  This is not
#	necessary for correct operation of the firewall, but greatly
#	assists in diagnosing problems.
#

#
# Policies for traffic originating from the local LAN (loc)
#
# If you want to force clients to access the Internet via a proxy server
# on your firewall, change the loc to net policy to REJECT info.
loc		net		ACCEPT
loc		wifi		ACCEPT
loc		$FW		REJECT		info
loc		all		REJECT		info

#
# Policies for traffic originating from the firewall ($FW)
#
# If you do not want open access to the Internet from your firewall, change the
# $FW to net policy to REJECT and add the 'info' LOG LEVEL.
$FW		net		ACCEPT
$FW		wifi		REJECT		info
$FW		loc		REJECT		info
$FW		all		REJECT		info

#
# Policies for traffic originating from the Internet zone (net)
#
net		$FW		DROP		info
net		loc		DROP		info
net		wifi		DROP		info
net		all		DROP		info

#
# Policies for traffic originating from the local Wi-Fi LAN (wifi)
#
wifi		net		ACCEPT
wifi		loc		REJECT		info
wifi		$FW		REJECT		info
wifi		all		REJECT		info

# THE FOLLOWING POLICY MUST BE LAST
all		all		REJECT		info

#LAST LINE -- ADD YOUR ENTRIES ABOVE THIS LINE -- DO NOT REMOVE}}}

== /etc/shorewall/rules ==

{{{
#ACTION		SOURCE		DEST		PROTO	DEST	SOURCE		ORIGINAL	RATE		USER/
#							PORT	PORT(S)		DEST		LIMIT		GROUP
#								PORT	PORT(S) DEST			LIMIT	GROUP
#
#	Accept SSH connections for administration
SSH/ACCEPT	loc		$FW
SSH/ACCEPT	net		$FW
SSH/ACCEPT	wifi		$FW

#	Allow Ping from the local network
Ping/ACCEPT	loc		$FW
Ping/ACCEPT	wifi		$FW
Ping/ACCEPT	loc		wifi
Ping/ACCEPT	wifi		loc

# Reject Ping from the "bad" net zone.. and prevent your log from being flooded..
Ping/REJECT	net		$FW

ACCEPT		$FW		loc		icmp
ACCEPT		$FW		net		icmp
ACCEPT		$FW		wifi		icmp

# Accept DNS connections from local network to the firewall
DNS/ACCEPT	loc		$FW
DNS/ACCEPT	wifi		$FW

# Forward https traffic to byte:
DNAT		net		$WWW_IP		tcp	443
ACCEPT		wifi		$WWW_IP:443 	tcp	443

#LAST LINE -- ADD YOUR ENTRIES BEFORE THIS ONE -- DO NOT REMOVE}}}

== /etc/shorewall/routestopped ==

You may want to include "{{{$WF_IF -}}}" here as well.

{{{
#INTERFACE	HOST(S)                  OPTIONS
$LOC_IF		-
#LAST LINE -- ADD YOUR ENTRIES BEFORE THIS ONE -- DO NOT REMOVE}}}

----
CategoryHowTo
