= Kamikaze Configuration =
THIS IS ALL UNTESTED.  PLEASE TRY TO CONFIRM IT FOR YOURSELF.
== Forward / Background ==
In the early days of OpenWRT, the only target platforms were the WRT54G and similar Broadcom based routers.  This platform had an NVRAM (much like high end, commercial routers) to store configuration information.  Up until White Russian, OpenWRT used NVRAM for configuration.  As OpenWRT expanded to new platforms without NVRAM, NVRAM was abandoned in favor of configuration files in /etc/config.  This configuration method presents related information in the same area and is much like existing *nix configuration files.
There is an order to initialisation:
1. CFE (bootloader) may initialise switch into VLANS based on NVRAM information
2. Kamikaze may (will?) initialise switch into VLANS based on information in /etc/config/network (see below) - note this creates network devices with names like ''vlan0'' or ''eth0.0'' (what are they?) note also this used to be done using the ''robocfg'' utility; how is it done now? 
3. Kamikaze may (will?) initialise the wifi card - note this can be done using ''madwifi'' and ''iwconfig'', is that what is happening during startup?
4. Kamikaze may (will?) initialise bridges to link wireless with LAN based on information in /etc/config/network - note this can be done using the ''brctl'' utility, is this what is used during startup?
4. Kamikaze will assign ip addresses to network devices or bridges - could be using ''brctl'' or ''ifconfig''

Some older Kamikaze builds are configured like NVRAM, only with key=value pairs in the config file.

== Network Configuration ==
Many of the concepts from earlier versions are retained in Kamikaze.  Both lan and wan still exist on Kamikaze, while VLANs are still used to separate WAN and LAN interfaces.

  * Network Background: OpenWrtDocs/NetworkInterfaces
  * Some IP, netmask, etc review site
  * Some bridging and brctl info page
=== VLANs ===
Since most routers use a single switch, you need to split up your WAN and LAN.
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
}}}

==== Static ====
{{{
config interface lan
	option ifname	eth0.0
	option proto	static
	option ipaddr	192.168.1.1
	option netmask	255.255.255.0
}}}
=== PPPoE and PPPoA ===
Normally, these are used for DSL.

These values are from an older configuration:
{{{
wan_proto=pppoe
wan_ifname=ppp0
wan_device=nas0
atm_vpi=0
atm_vci=35
ppp_username=user@host.com
ppp_passwd=password

# For pppoe
pppoe_atm=1
ppp_mtu=1492

# For pppoa
ppp_mtu=1500
}}}
=== 802.11x ===
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
