= Kamikaze Configuration =
THIS IS ALL UNTESTED.  PLEASE TRY TO CONFIRM IT FOR YOURSELF.
== Forward / Background ==
In the early days of OpenWRT, the only target platforms were the WRT54G and similar Broadcom based routers.  This platform had an NVRAM (much like high end, commercial routers) to store configuration information.  Up until White Russian, OpenWRT used NVRAM for configuration.  As OpenWRT expanded to new platforms without NVRAM, NVRAM was abandoned in favor of configuration files in /etc/config.  This configuration method presents related information in the same area and is much like existing *nix configuration files.


Some older Kamikaze builds are configured like NVRAM, only with key=value pairs in the config file.


== Order for Network Initialization ==

1. CFE (bootloader) may initialise switch into VLANS based on NVRAM information

2. Kamikaze may (will?) initialise switch into VLANS based on information in /etc/config/network (see below) - note this creates network devices with names like ''vlan0'' or ''eth0.0'' (what are the actual names?) note also this used to be done using the ''robocfg'' utility; how is it done now? 

3. Kamikaze may (will?) initialise the wifi card - note this can be done using ''madwifi'' and ''iwconfig'', is that what is happening during startup?

4. Kamikaze may (will?) initialise bridges to link wireless interface with (v)LAN based on information in /etc/config/network - note this can be done using the ''brctl'' utility, is this what is used during startup?

5. Kamikaze will assign ip addresses or ask for dhcp IP leases for network devices or bridges - could be using ''ifconfig''?


== Network Configuration ==
Many of the concepts from earlier versions are retained in Kamikaze.  Both lan and wan still exist on Kamikaze, while VLANs are still used to separate WAN and LAN interfaces.

  * Network Background: OpenWrtDocs/NetworkInterfaces
  * /etc/config/network documentations https://dev.openwrt.org/browser/trunk/docs/network.tex
  * Some IP, netmask, etc review site
  * Some bridging and brctl info page
=== VLANs ===
Since most routers use a single switch, you need to split up your WAN and LAN.  There are some alternate configurations, like all ports switched and DMZ.

See [:OpenWrtDocs/HardwareTables/switchPorts: Switch Ports]

{{{
# Normal routing configuration for WRT54Gv3
config switch eth0
        option vlan0    "0 1 2 3 5*"
        option vlan1    "4 5"
}}}

=== Network Layer ===
==== DHCP ====
{{{
config interface wan
	option ifname	eth0.1
	option proto	dhcp
        option hostname MyRouter This is only used if the proto is dhcp otherwise it is ignored.
}}}

==== Static ====
{{{
config interface lan
	option ifname	eth0.0
	option proto	static
	option ipaddr	192.168.1.2
	option netmask	255.255.255.0
	option gateway	192.168.1.1
	option dns	192.168.1.1
}}}
DNS option not working in build 5195.  Had to edit ''/etc/resolv.conf'' for it to work.  Needs further testing. (This is due to /etc/resolv.conf being a real file from packages/base-files, instead of a symlink to /tmp/resolv.conf)

==== Bridging Interfaces ====
{{{
config interface lan
	option type	bridge
	option ifname	"eth0.0 ath0"
	option proto	static
	option ipaddr	192.168.1.1
	option netmask	255.255.255.0
}}}

==== Bridged xDSL ====
{{{
config interface wan
	option ifname	nas0
	option proto	dhcp
}}}

=== PPPoE and PPPoA ===
Normally, these are used for DSL.

{{{
config interface wan
	option ifname	eth0
	option proto	pppoe
        option username xxxxxx
        option password xxxxxx
}}}
=== 802.11x ===
'''Note: Currently supported on Broadcom only'''
  * /etc/config/wireless documentations https://dev.openwrt.org/browser/trunk/docs/wireless.tex
  * Other types, e.g. madwifi, are not yet handled here and must use a startup script to work.
Wireless specific (Layers 1 and 2) configuration is in /etc/config/wireless.  Layer 3 (Network) is done in /etc/config/network.

Default Configuration:
{{{
config wifi-device	wl0
	option type	broadcom
	option channel	5

config wifi-iface
	option device	wl0
	option mode	ap
	option ssid	OpenWrt
	option hidden	0
	option encryption none
}}}

Full outline of the wifi config file is as follows:
{{{
config wifi-device     wifi device name
       option type     currently only broadcom
       option country  country code [not mandatory, used for setting restrictions based on country regulations]
       option channel  1-14
       option maxassoc Maximum number of associated clients
       option distance The distance between the ap and the furthest client in meters.

config wifi-iface
       option network  the interface you want wifi to bridge with 
       option device   wifi device name
       option mode     ap, sta, adhoc, or wds
       option encryption none, wep, psk, psk2, wpa, wpa2 
       option key      encryption key or radius shared secret
       option server   radius server
       option port     radius port
}}}
'''Notes:

"option network <interface>": This setting is mandatory if you want your wifi interface bridged to your lan (Normal bridging: "option network lan")

"option encryption <key>": wpa and wpa2 are for radius config, use psk for WPA-PSK
