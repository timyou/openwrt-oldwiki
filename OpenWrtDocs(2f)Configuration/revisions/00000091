#acl Known:read,write All:read
##
## Note: these pages document the firmware itself, not packages
##       questions/comments should be posted to the forum
##
## THIS PAGE DOCUMENTS THE FIRMWARE, NOT PACKAGES
## DO NOT ADD PACKAGE DOCUMENTATION/CONFIGURATION TO THIS PAGE
##
[:OpenWrtDocs]
[[TableOfContents]]

= NVRAM =
NVRAM stands for Non-Volatile RAM, in this case the last 64K of the flash chip used to store various configuration information in a ''name=value'' format.

{{{#!CSV
Command; Description
nvram show | sort | less; Display everything in nvram
nvram get boot_wait; Get a specific variable
nvram set boot_wait=on; Set a value
nvram set lan_ifnames="vlan0 vlan1 vlan2"; set multiple values to one param
nvram unset foo; Delete a variable
nvram commit; Write changes to the flash chip (otherwise only stored in RAM)
}}}

A complete list of nvram options can be found at [:OpenWrtNVRAM].

= Network configuration =

'''Quick overview of the router architecture:'''

The WRT54G is made up of an Ethernet switch, a wireless access point and a router chip that connects them together.

[http://upload.wikimedia.org/wikipedia/commons/0/0f/WRT54G_internal_architecture.png]

The names of the network interfaces will depend largely on what hardware OpenWrt is run on.
||'''Manufacturer'''||'''Model'''||'''Hardware version'''||'''LAN'''||'''WAN'''||'''WIFI'''||'''Comments'''||
||Linksys||WRT54G||v1.x||vlan2||vlan1||eth2|| ||
||Linksys||WRT54G||v2.x/v3.0||vlan0||vlan1||eth1|| ||
||Linksys||WRT54GS||v1.x/v2.0||vlan0||vlan1||eth1|| ||
||Asus||WL-300g|| ||eth0||None||eth2|| ||
||Asus||WL-500g|| ||eth0||eth1||eth2|| ||
||Asus||WL-500g Deluxe|| ||vlan0||vlan1||eth1||eth0 is the whole switch, with lan and wan ports||
||Buffalo||WBR-G54|| ||eth0||eth1||eth2|| ||
||Buffalo||WBR2-G54S|| ||vlan0||vlan1||eth1||eth0 is the whole switch, with lan and wan ports||
||Buffalo||WLA-G54|| ||eth0||N/A||eth2||No WAN port on this device||
||Motorola||WR850G||v3||vlan0||vlan1||eth1||eth0 is the whole switch, with lan and wan ports||
||Microsoft||MN700||v.x||eth0||eth1||eth2|| ||
||Siemens||SE505||v2||vlan0||vlan1||eth1||eth0 is the whole switch, with lan and wan ports||
Please update to include other models.

NOTE: LAN and WIFI are bridged together in br0 by default, on some devices WAN can be eth1 and LAN eth0.

In general, the switch works the following way: It recieves data (physical) on either
lan port or on the wan port. Then the switch tags the packages (with VLAN), so Linux
is able to see the difference and that way we have the vlan devices, which describe wan
or lan port.

[[BR]]
The basic (802.3) network configuration is handled by a series of NVRAM variables:
{{{#!CSV
NVRAM; Description
<name>_ifname; The name of the linux interface the settings apply to
<name>_ifnames; Devices to be added to the bridge (only if the above is a bridge)
<name>_proto; The protocol which will be used to configure an IP
            ; static: Manual configuration (see below)
            ; dhcp: Perform a DHCP request
            ; pppoe: Create a ppp tunnel (requires pppoecd package)
<name>_ipaddr; ip address (x.x.x.x)
<name>_netmask; netmask (x.x.x.x)
<name>_gateway; Default Gateway (x.x.x.x)
<name>_dns; DNS server (x.x.x.x)
}}}
The command ''ifup <name>'' will configure the interface defined by <name>_ifname according to the above variables. As an example, the /etc/init.d/S40network script will automatically run the following commands at boot:
{{{
ifup lan
ifup wan
ifup wifi
}}}
The ''ifup lan'' command will bring up the interface specified by lan_ifname. Normally the lan_ifname is set to br0 which will cause it to create the bridge br0 and add the the interfaces from lan_ifnames to the bridge; lan_proto is usually static which means that br0 will have the ip address from lan_ipaddr, and so on for the rest of the variables listed above.

It's important to remember that it's the <name>_ifname that specifies the interfaces, the <name> compontent itself has almost no value. This means that if you changed lan_ifname to be the internet port, vlan1, then ''ifup lan'' would bring up the internet port, not the lan ports (despite using the command ''ifup lan'' and using the lan_ variables). Also, it means that you can create any <name> variables you want, foo_ifname, foo_proto .... and they would be used by ''ifup foo''.

The only <name> with any significance is '''wan''', used by the /etc/S45firewall script. The firewall script will NAT traffic through the wan_ifname, blocking connections to wan_ifname.

Further information about the variables used can be found at [:OpenWrtNVRAM]

Don't forget to check the [:OpenWrtFaq] for information about howto setup PPPOE etc.

== Sample network configurations ==

For client mode configuration (rather than AP mode), see this page: [:ClientModeHowto]

(note these examples use wrt54g v2.x/wrt54gs v1.x interface names)

The default network configuration:
(lan+wireless bridged as 192.168.1.1/24, wan as dhcp)
{{{
lan_ifname=br0
lan_ifnames="vlan0 eth1"
lan_proto=static
lan_ipaddr=192.168.1.1
lan_netmask=255.255.255.0

wan_ifname=vlan1
wan_proto=dhcp
}}}


If you just want to use OpenWrt as an access point you can avoid the WAN interface completely:
(lan+wireless bridged as 192.168.1.25/24, routed through 192.168.1.1, wan ignored)
{{{
lan_ifname=br0
lan_ifnames="vlan0 eth1"
lan_proto=static
lan_ipaddr=192.168.1.25
lan_netmask=255.255.255.0
lan_gateway=192.168.1.1
lan_dns=192.168.1.1

wan_proto=none
}}}

To separate the LAN from the WIFI:
(lan as 192.168.1.25/24, wireless as 192.168.2.25/24, wan as dhcp, remove your wifi interface (eth1 on v2/3 linksys routers) from the lan_ifnames variable)
{{{
lan_ifname=vlan0
lan_proto=static
lan_ipaddr=192.168.1.25
lan_netmask=255.255.255.0

wifi_ifname=eth1
wifi_proto=static
wifi_ipaddr=192.168.2.25
wifi_netmask=255.255.255.0

wan_ifname=vlan1
wan_proto=dhcp

lan_ifnames=vlan0 eth2 eth3
}}}

Note that the default behaviour is to [http://forum.openwrt.org/viewtopic.php?pid=8410#p8410 use WPA] if your WRT54G is running in AP mode.  If you don't want to use WPA, unset wl0_crypto with:

{{{
nvram unset wl0_crypto && nvram commit
}}}

== The ethernet switch ==

The WRT54G is essentially a WAP54G (wireless access point) with a 6 port switch. There's only one physical ethernet connection and that's wired internally into port 5 of the switch; the WAN is port 0 and the LAN is ports 1-4. The separation of the WAN and LAN interfaces is done by the switch itself. The switch has a vlan map which tells it which vlans can be accessed through which ports.

The vlan configuration is based on two variables (per vlan) in nvram.

{{{
vlan0ports="1 2 3 4 5*" (use ports 1-4 on the back, 5 is the wrt54g itself)
vlan0hwname=et0
}}}

=== Normal Behavior ===

This is only the case if the nvram variable boardflags is set. On the WRT54G V1.1 and earlier, it's not set.

When the et module (ethernet driver) loads it will read from vlan0ports to vlan15ports, behind the scenes the ethernet driver is using these variables to generate a more complex configuration which will be sent to the switch. When packets are recieved from external devices they need to be assigned a vlan id, and when packets are sent to those external devices the vlan tags need to be removed.

PVID represents the primary vlan id, in other words if a packet doesn't have a vlan tag, which vlan does it belong to? The ethernet driver handles this rather trivially, in the case of vlan0ports="1 2 3 4 5*", ports 1-4 are set to PVID 0 (vlan0). Since the wrt needs to recieve packets from both the LAN (vlan0) and the WAN (vlan1), port 5 is a special case appearing in both vlan0ports and vlan1ports. This is where the '*' is used -- it determines the PVID of port 5, which is also the only port not to untag packets (for hopefully obvious reasons).

The second variable, vlan0hwname is used by the network configuration program (or script in the case of openwrt) to determine the parent interface. This should be set to "et0" meaning the interface matching et0macaddr.

'''Sample configurations'''
(unless otherwise specified, vlan variables not shown are assumed to be unset)

Default:
{{{
vlan0ports="1 2 3 4 5*"
vlan0hwname=et0
vlan1ports="0 5"
vlan1hwname=et0
}}}

All ports lan (vlan0):
{{{
vlan0ports="0 1 2 3 4 5*"
vlan0hwname=et0
}}}

LAN (vlan0), WAN (vlan1), DMZ (vlan2):
{{{
vlan0ports="3 4 5*"
vlan0hwname=et0
vlan1ports="0 5"
vlan1hwname=et0
vlan2ports="1 2 5"
vlan2hwname=et0
}}}

= Wireless configuration =

== Basic settings ==

|| '''NVRAM variable''' || '''Description''' ||
|| wl0_mode  || '''ap''' = Access Point (master mode), '''sta''' Client mode ||
|| wl0_ssid  || ESSID ||
|| wl0_infra || '''0''' = Ad Hoc mode, '''1''' = normal AP/Client mode ||
|| wl0_closed || '''0''' = Broadcast ESSID, '''1''' Hide ESSID ||

See OpenWrtNVRAM for more NVRAM settings.

== WEP encryption ==

|| '''NVRAM variable''' || '''Description''' ||
|| wl0_wep || '''disabled''' = disabled WEP, '''enabled''' = enable WEP ||
|| wl0_key || '''1''' .. '''4''' = Select WEP key to use ||
|| wl0_key[1..4] || WEP key in hexadecimal format (allowed hex chars are 0-9a-f) ||

Avoid using WEP keys with 00 at the end, otherwise the driver won't be able to detect the key length correctly.

A 128-Bit WEP key must be 26 hex digits long.

Setting up WPA will override any WEP settings.

== WPA encryption ==

For enabling WPA, you need to install the nas package. 
When you enable or disable WPA settings, you should make sure that the NVRAM variable '''wl0_auth_mode''' is unset, because it is obsolete.

More information is on ["OpenWrtDocs/nas"]. (solve problem with WhiteRussian RC2 and client mode)

|| '''NVRAM variable''' || '''Description''' ||
||<rowspan=6> wl0_akm || '''open''' = No WPA ||
||  '''psk''' = WPA Personal/PSK (Preshared Key) ||
||  '''wpa''' WPA with a RADIUS server ||
||  '''psk2''' = WPA2 PSK ||
||  '''wpa2''' WPA2 with RADIUS ||
||  '''"psk psk2"''' or '''"wpa wpa2"''' = support both WPA and WPA2 ||
||<rowspan=3> wl0_crypto || '''tkip''' = RC4 encryption ||
||  '''aes''' = AES encryption ||
||  '''aes+tkip''' = support both ||
|| wl0_wpa_psk || Password to use with WPA/WPA2 PSK (at least 8, up to 63 chars) ||
|| wl0_radius_key || Shared Secret for connection to the Radius server ||
|| wl0_radius_ipaddr || IP to connect... ||
|| wl0_radius_port || Port# to connect... ||

== Wireless Distribution System (WDS) / Repeater / Bridge ==

OpenWrt supports the WDS protocol, which allows a point to point link to be established between two access points. By default, WDS links are added to the br0 bridge, treating them as part of the lan/wifi segment; clients will be able to seamlessly connect through either access point using wireless or the wired lan ports as if they were directly connected.

Configuration of WDS is simple, and depends on one of two variables

{{{#!CSV
NVRAM; Description
wl0_lazywds; Accept WDS connections from anyone (0:disabled 1:enabled)
wl0_wds; List of WDS peer mac addresses (xx:xx:xx:xx:xx:xx, space separated)
}}}

For security reasons, it's recommended that you leave wl0_lazywds off and use wl0_wds to control WDS access to your AP.
wl0_wds functions as an access list of peers to accept connections from and peers to try to connect to; the peers will either need the mac address of your AP in their wl0_wds list, or wl0_lazywds enabled.

Easy steps for a successfull WDS:

First do it without wireless protection and then activate the protection.
If you activate both you will double the pain to find a problem.

 1. Configure the IPs of each AP - don't use the same! For easier maintenance you can use the same subnet.
 1. Add the '''other''' APs MAC address to the list of allowed peers to each AP. With OpenWRT it's the variable wl0_wds.
 1. Disable all the unneeded services like DHCP, port forwarding, firewalling etc. '''except''' on the AP the has the internet connection. Remember: The other APs only act as the extended arm of the internet connected AP.
 1. Configure the WLAN parameters on all APs identical. That is SSID, channel, etc. - keep it simple. If you want to try boosters etc. do this later.
 1. Have you commited your values? Do it. And reboot.
 1. Now connect a lan cable to each AP and try to ping the internet AP. It should answer. Else start checking the settings.
 1. You are done. Now activate security on the devices. Optionally hide the SSID (wl0_closed=1). If WPA-PSK doesn't work chances are that a peer partner doesn't support it. Try WEP.

== OpenWRT wireless bridge ==

With 

{{{
nvram set wl0_mode=wet
}}}

you can use your AP/Router as a Bridge.

This section is work in progress, please refer to the following docs:

http://woz.gs/wifi/openwrtbridge.html

http://openwrt.org/forum/viewtopic.php?t=1078&highlight=wl0mode+wet

For the "invisible wire" style, e.g. for bridging between two buildings, you might want to check out this link:

http://www.jean.nu/view.php/page/openwrt

== OpenWRT as Client ==

Starting with RC2 WhiteRussian basically the only thing you have to do is to switch the WL mode like with the bridge:

{{{
nvram set wl0_mode=sta
}}}

Breaking down the bridge is not really necessary as described in ["ClientModeHowto"]

= Software configuration =

== System ==

=== dnsmasq ===

Dnsmasq is lightweight, easy to configure DNS forwarder and DHCP server.

Documentation can be found at ["OpenWrtDocs/dnsmasq"]

=== nas ===

'''nas''' is the binary, Broadcom proprietary, tool that sets up security connection on wireless device.

Documentation with discovered feature can be found at ["OpenWrtDocs/nas"] .

=== wl ===

'''wl''' is a proprietary Linksys binary tool for setting the parameters of the wireless interface.

Documentation with discovered feature can be found at ["OpenWrtDocs/wl"] .

=== TimeZone and NTP ===

To set a Time Zone type something like the following line in /etc/profile:
{{{
export TZ="CET-1CETDST"
}}}
''note: This sets TimeZome to GMT+1''

If you want to use a TimeClient to Syncronize use rdate
for that copy the following line at the beginnig after the comment in the /etc/init.d/rcS

{{{
/usr/sbin/rdate 128.138.140.44
}}}

Putting a TimeZone entry for the Systemlogger could also be an good idea
simply put a line like something in /etc/TZ:

{{{
CET-1CEST-2,M3.5.0/02:00:00,M10.5.0/03:00:00
}}}
''note: this sets TimeZone for CET/CEST (Central European Time UTC+1 / Central European Summer Time UTC+2) and the starting (5th week of March at 02:00) and endtime (5th week of October at 03:00) of DST (Daylight Saving Time).''

More can be found here: http://leaf.sourceforge.net/doc/guide/buci-tz.html#id2594640
and: http://openwrt.org/forum/viewtopic.php?id=131

Examples:
||Australia||Melbourne||EST-10EDT-11,M10.5.0/02:00:00,M3.5.0/03:00:00||
||<rowspan=13>Europe||Amsterdam, Netherlands||||
||Barcelona, Spain||||
||Berlin, Germany||CET-1CEST-2,M3.5.0/02:00:00,M10.5.0/03:00:00||
||Brussels, Belgium||||
||Copenhagen, Denmark||CET-1CEST-2,M3.5.0/02:00:00,M10.5.0/03:00:00||
||Dublin, Ireland||GMT+0IST-1,M3.5.0/01:00:00,M10.5.0/02:00:00||
||Geneva, Switzerland||CET-1CEST-2,M3.5.0/02:00:00,M10.5.0/03:00:00||
||London, Great Britain||GMT+0BST-1,M3.5.0/01:00:00,M10.5.0/02:00:00||
||Madrid, Spain||||
||Oslo, Norway||||
||Paris, France||||
||Prague, Czech Republic||CET-1CEST-2,M3.5.0/02:00:00,M10.5.0/03:00:00||
||Roma, Italy||||
||<rowspan=7>USA & Canada||Hawaii Time||HAW10||
||Alaska Time||AKST9AKDT||
||Pacific Time||PST8PDT||
||Mountain Time||MST7MDT||
||Central Time||CST6CDT||
||Eastern Time||EST5EDT||
||Atlantic Time||AST4ADT||
Please update and include your Time Zone.[[BR]]
You can find more on timezones on [http://www.timeanddate.com/worldclock/ timeanddate.com].

=== Crontab ===
HowtoEnableCron

== Applications ==

=== httpd ===

'''httpd''' is the binary, part of BusyBox, tool that start http daemon.

Documentation can be found at ["OpenWrtDocs/httpd"] .

= Hardware =

== LED ==

Document can be found at ["wrtLEDCodes"]
