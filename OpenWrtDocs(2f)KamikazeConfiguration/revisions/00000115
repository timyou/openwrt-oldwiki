[[TableOfContents]]

= Kamikaze Configuration =
== Foreword / Background ==
In the early days of OpenWRT, the only target platforms were the WRT54G and similar Broadcom-based routers.  This platform has an NVRAM (much like high-end, commercial routers) to store configuration information.  Up until White Russian, OpenWRT used NVRAM for configuration.  As OpenWRT expanded to new platforms without NVRAM, NVRAM was abandoned in favour of configuration files in /etc/config.  This configuration method presents related information in the same area and is much like existing *nix configuration files.

Some older Kamikaze builds have configuration files which mimic the NVRAM configuration in that there are only key=value pairs in the configuration files.

== Order for Network Initialization ==
1. CFE (bootloader) may initialise switch into VLANS based on NVRAM information

2. Kamikaze initialise switch into VLANS based on information in /etc/config/network (see below) - note this creates network devices with names like ''eth0.0''. Note also this used to be done using the ''robocfg'' utility; how is it done now?

3. Kamikaze initialise the wifi card - note this can be done using ''madwifi'' or ''iwconfig'', is that what is happening during startup? (it uses self made scripts, calling wlc, isn't it?)

4. Kamikaze initialise bridges to link wireless interface with (v)LAN based on information in /etc/config/network - note this can be done using the ''brctl'' utility, is this what is used during startup?

5. Kamikaze will assign ip addresses or ask for dhcp IP leases for network devices or bridges - could be using ''ifconfig''?

== Network Configuration ==
Many of the concepts from earlier versions are retained in Kamikaze.  Both lan and wan still exist on Kamikaze, while VLANs are still used to separate WAN and LAN interfaces.

 * Network Background: OpenWrtDocs/NetworkInterfaces
 * [http://downloads.openwrt.org/kamikaze/docs/openwrt.html#x1-80001.2.1 /etc/config/network documentations]
 * Some IP, netmask, etc review site
 * Some bridging and brctl info page
=== VLANs ===
Since most routers use a single switch, you need to split up your WAN and LAN. There are some alternate configurations, like all ports switched and DMZ. See [:OpenWrtDocs/HardwareTables/switchPorts:Switch Ports] for more details.

{{{
# Normal routing configuration for WRT54Gv3
config switch eth0
        option vlan0    "0 1 2 3 5*"
        option vlan1    "4 5"
}}}
The "*" mark is set for the default VLAN. Packets transferred between interfaces on the default VLAN are the ones that will remain unchanged, while all other will be "tagged". See more in section "VLAN Trunking" under the [:OpenWrtDocs/NetworkInterfaces:VLAN and bridging concepts] page.

If you are using a VLAN 802.11q capable external switch, you can use it simply by configuring the VLAN interfaces as instructed in the next section.  For example: VLAN 1 on the switch would correspond to eth0.1 on OpenWRT.

=== Network Layer ===
==== DHCP ====
{{{
config interface wan
        option ifname   eth0.1
        option proto    dhcp
        option hostname MyRouter  #This is only used if the proto is dhcp otherwise it is ignored.
}}}
==== Static ====
{{{
config interface lan
        option ifname   eth0.0
        option proto    static
        option ipaddr   192.168.1.2
        option netmask  255.255.255.0
        option gateway  192.168.1.1
        option dns      192.168.1.1

Note: In current versions of Kamikaze, traffic forwarding is disallowed by default. this means that in
order to route between multiple networks on your local network, you will need to allow this.
from telnet or ssh, enter this if your router can ping these networks, but hosts return "destination port unreachable"

 uci set firewall.@zone[0].forward=ACCEPT; uci commit firewall; /etc/init.d/firewall restart


}}}
==== Sub interfaces / IP Alias ====
Kamikaze 8.09:
{{{
config alias
        option interface lan
        option proto    static
        option ipaddr   192.168.1.2
        option netmask  255.255.255.0
	option gateway 192.168.1.1
}}}

Older Versions:
{{{
config interface lan1
        option ifname   eth0.0:0
        option proto    static
        option ipaddr   192.168.1.2
        option netmask  255.255.255.0
        option gateway  192.168.1.1
Note: The "option type" must be absent!
(http://forum.openwrt.org/viewtopic.php?id=10505)
}}}
You can configure multiple DNS servers by separating entries with space:

{{{
option dns "192.168.1.1 192.168.80.100"
}}}
==== Bridging Interfaces ====
{{{
config interface lan
        option type     bridge
        option ifname   "eth0.0"    #See note 1 for adding a wireless interface to the bridge.
        option proto    static
        option ipaddr   192.168.1.1
        option netmask  255.255.255.0
}}}
==== Bridged xDSL ====
{{{
config interface wan
        option ifname   nas0
        option proto    dhcp
}}}
==== MAC Address Cloning ====
Add the following option to /etc/config/network under the wan section:

{{{
option macaddr xx:xx:xx:xx:xx:xx
}}}
Restart the network using:

{{{
/etc/init.d/network restart
}}}
or reboot your router

Check dmesg or syslog for the change.  If the mac address does not change, clean your nvram variables using these instructions:

{{{
http://wiki.openwrt.org/Faq#head-71cacf8460752af3f5771d2fae54923ded5beb9c
}}}
=== Static Routes ===
Routes are automatically setup to the networks attached to interfaces.  Other static routes may be created.

 {{{ config route foo
   option interface lan
   option target 1.1.1.0
   option netmask 255.255.255.0
   option gateway 192.168.1.1
}}}
The name for the route section is optional, the interface, target and gateway options are mandatory. Leaving out the netmask option will turn the route into a host route.
 * interface -- The route is created after the designated interface is brought up.
 * target -- Network to which a route is to be established.  0.0.0.0 is the default route.
 * netmask -- netmask of target network, in dotted quad format x.x.x.x.  0.0.0.0 is the netmask for the default route.
 * gateway -- Packets destined to the target network are sent to this IP address.
=== PPPoE and PPPoA ===
PPPoE and PPPoA used for "dial-up" Cable and DSL connections, but not bridged.
[:OpenWrtDocs/Kamikaze/PPPoX:PPP over *]
=== Wireless configuration ===
==== 802.11x ====
'''Note: Currently supported on Broadcom and Atheros (MadWifi) only'''

 * /etc/config/wireless documentations https://dev.openwrt.org/browser/trunk/docs/wireless.tex

Wireless specific (Layers 1 and 2) configuration is in /etc/config/wireless.  Layer 3 (Network) is done in /etc/config/network.

Default Configuration:

{{{
config wifi-device      wl0
        option type     broadcom
        option channel  5
        option disabled 1
config wifi-iface
        option device   wl0
        option mode     ap
        option ssid     OpenWrt
        option hidden   0
        option encryption none
}}}
Full outline of the wifi config file is as follows:

{{{
config wifi-device     wifi device name
       option type     currently only broadcom and atheros
       option country  country code [not mandatory, used for setting restrictions based on country regulations]
       option channel  1-14
       option disabled 1 disables the wireless card, 0 enables the wireless card
       option maxassoc Currently only for Broadcom. Maximum number of associated clients
       option distance The distance between the ap and the furthest client in meters.
       option agmode     Currently only for Atheros.  Options are: 11b, 11g, 11a, 11bg
       option diversity Currently only for Atheros. 0 disables diversity, 1 enables diversity (default)
       option txantenna Currently only for Atheros. 0 for auto (default), 1 for antenna 1, and 2 for antenna 2
       option rxantenna Currently only for Atheros. 0 for auto (default), 1 for antenna 1, and 2 for antenna 2
config wifi-iface
       option network  the interface you want wifi to bridge with
       option device   wifi device name
       option mode     ap, sta, adhoc, or wds
       option ssid     ssid to be used
       option bssid    used for wds to set the mac address of the other wds unit
       option encryption none, wep, psk, psk2, wpa, wpa2 (note 4,5)
       option key      encryption key or radius shared secret, when used for wep if you only use one key it can be placed here otherwise set this to the key number you would like to use and use the following key1-4 options
       option key1     wep key 1
       option key2     wep key 2
       option key3     wep key 3
       option key4     wep key 4
       option server   radius server
       option port     radius port
       option txpower  Currently only for Atheros. This value is measured in dbm
       option bgscan   Currently only for Atheros. This controls client background scanning, 0 disabled, 1 enabled (default)
       option hidden   0 broadcasts the ssid; 1 disables broadcasting of the ssid
       option isolate  0 disables ap isolation (default); 1 enables ap isolation
       option wds      Atheros only. 0 disables wds (default), 1 enables wds
}}}
'''Notes: '''

'''1) "option network <interface>": This setting is mandatory if you want your wifi interface bridged to your lan (Normal bridging: "option network lan").'''  If you don't want to do that, see [:OpenWrtDocs/KamikazeConfiguration/NonBridgedWiFi:Using Non-Bridged WiFi].

'''2) "option encryption <key>": wpa and wpa2 are for radius config, use psk for WPA-PSK or psk2 for WPA-PSK2 (AES)''' You must install hostapd-mini for ap and wpa_supplicant for client.

'''3) "option key <key>": You must use a key that is at least 8 characters long if you are using psk2.''' If your key is fewer than 8 characters long, you may get the following error under Kamikaze 7.09: "wl0: ignore i/f due to error(s)".

'''4) "option mode": there is no 'wet' mode any more.''' However, if you select 'sta' mode, and also bridge the wireless to another interface (e.g. 'option network lan'), then wet mode is enabled automatically. This allows the unit to act as a wireless bridge, so that one or more PCs sitting behind the OpenWrt box can join the LAN. Some ARP and DHCP masquerading is done so that this doesn't require WDS mode on the access point. ''(Tested with Kamikaze 7.07 and a Broadcom chipset and 2.4 kernel; may not work for Atheros and/or 2.6 users)''

'''5) "option type broadcom":''' If you get an error about 'broadcom unsupported', make sure you have the '''wlc''' and '''kmod-brcm-wl''' packages installed. You will probably also need '''nas''' for WPA.

'''6) hostapd:''' For WPA you may need hostapd. The kamikaze 7.07 does not include hostapd and must be installed to support WPA (at least when using madwifi).
===== Client Mode with WPA/WPA2 =====
See ["OpenWrtDocs/Kamikaze/ClientMode"]

==== MAC Filter ====
First, you need to have installed the wl package - '''ipkg install wl'''
||'''uci variable''' ||'''Description''' ||
||'''wireless.wl0.macfilter''' ||(0/1/2) used to (disable checking/deny/allow) mac addresses listed in wl0.maclist ||
||'''wireless.wl0.maclist''' ||List of space-separated mac addresses to allow/deny according to wl0.macfilter. Addresses should be entered with colons, e.g.: "00:02:2D:08:E2:1D 00:03:3E:05:E1:1B". note that if you have more than one mac use quotes or only the first will be recognized. ||


Create the following script as '''/etc/init.d/wlmacfilter'''

{{{
#!/bin/sh /etc/rc.common
# The macfilter 2 means that the filter works in "Allow" mode.
# Other options are: 0 - disabled, or 1 - Deny.
#
# The maclist is a list of mac addresses to allow/deny, quoted, with spaces
#  separating multiple entries
# eg  "00:0D:0B:B5:2A:BF 00:0D:0C:A2:2A:BA"
START=47
MACFILTER=`uci get wireless.wl0.macfilter`
MACLIST=`uci get wireless.wl0.maclist`
start() {
        wlc ifname wl0 maclist "$MACLIST"
        wlc ifname wl0 macfilter "$MACFILTER"
}
stop() {
        wlc ifname wl0 maclist none
        wlc ifname wl0 macfilter 0
}
}}}
Finally, enable the script to run at boot time:

{{{
chmod 755 /etc/init.d/wlmacfilter
/etc/init.d/wlmacfilter enable}}}
Set the variables

{{{
uci set wireless.wl0.macfilter="2"
uci set wireless.wl0.maclist="00:0D:0B:B5:2A:BF 00:0D:0C:A2:2A:BA"
uci commit}}}
After making changes to the mac list with uci, run '''/etc/init.d/wlmacfilter start'''
=== Firewall ===
[:OpenWrtDocs/Kamikaze/FirewallConfiguration: Kamikaze firewall configuration]
== Services ==
=== DHCP ===
OpenWrt uses the lightweight [http://www.thekelleys.org.uk/dnsmasq/doc.html dnsmasq] DHCP server, which is configured in '''/etc/config/dhcp''':

{{{
config dhcp
        option interface        lan
        option start            100
        option limit            150
        option leasetime        12h
config dhcp
        option interface        wan
        option ignore   1}}}
This will make dnsmasq will offer up to 150 address leases, starting from address .100 of your network with a lease time of 12 hours. e.g. 10.0.0.100-10.0.0.249

If you think dnsmasq is not offering addresses as configured, use ''ps w'' to see what command-line arguments it was run with:

{{{
root@wrt:~# ps w | grep dnsmasq
  606 nobody      452 S   /usr/sbin/dnsmasq --dhcp-range=lan,10.0.0.10,10.0.0.60,255.255.255.0,12h -I eth0.1}}}
A common problem is to have the --dhcp-range option missing:

 . {{{/usr/sbin/dnsmasq -I eth0.1}}} (or ppp0, or whatever your WAN interface is -- -I means "don't offer addresses on this interface", more on that in ''dnsmasq --help'')
If that's the case, just append to your lan interface section:

{{{
option force 1
}}}
= Customizing Startup/Shutdown =
The user space boot process is initiated by init as configured in {{{/etc/inittab}}}.  Kamakaze uses a limited form of the System V startup process.   Scripts in {{{/etc/init.d/}}} are run with the arguments of {{{start}}} or {{{stop}}} to start services at boot or stop them at shutdown.  The order of the startup scripts is determined by the names of the links in {{{/etc/rc.d/}}}.  

{{{/etc/init.d/}}} scripts may be run by hand to manually start or stop services on a 1-time basis.

Each {{{/etc/init.d/foo}}} script (should) take the arguments {{{disable}}} and {{{enable}}} to permanently disable or enable automatic boot-time startup of the service.

The startup process may be extended with CustomStartupScripts.  This should also be read by those who want to change the order in which services are started.
= HowTo =
There are How Tos spread throughout the wiki.  An easy way to browse through them (and get ideas) is the How To category:
  * CategoryHowTo

Additionally, some of the more exotic How Tos can be found on the OpenWrt forum:
  * [http://forum.openwrt.org/viewforum.php?id=17 OpenWrt How To Forum]

###
###
###
###
### Please don't add any more howtos here.  It's not that we don't want them, it's that we don't want the main Kamikaze page growing.
###
###
###
###

= Sample Application Config Scripts =
 * Repeater http://wiki.openwrt.org/Repeater
