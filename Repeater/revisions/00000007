= Repeater =
by pier11 — last modified 2007-04-12 21:28

'''Applicable''': Kamikaze, Broadcom.

'''Tested''': WRT54G v2.0, Kamikaze r6816(02 Apr). Linksys WRT54GL, Kamikaze 7.09 (19 may 2008).

This page describes configuration of Kamikaze as a wireless repeater. In this configuration it uses open wireless network and creates your own private wireless network on top of it.

All you have to do is edit the following two files and reboot. That's it!

''/etc/config/wireless''
{{{
config wifi-device  wl0
	option type     broadcom
	option channel  5
# disable radio to prevent an open ap after reflashing:
	option disabled 0

config wifi-iface
	option device   wl0
	option network	lan
	option mode     ap
	option ssid     YourSSIDHere
	option hidden   0
	option encryption	wep
	option key	'1'
	option key1	'XXXXXXXXXXXXXXXXXXXXXXXXXX'

config wifi-iface
	option device   wl0
	option mode	sta
	option ssid	HostSSIDHere
	option encryption none
}}}
''/etc/config/network''
{{{
#### VLAN configuration 
config switch eth0
	option vlan0	"1 2 3 4 5*"
	option vlan1	"0 5"


#### Loopback configuration
config interface loopback
	option ifname	"lo"
	option proto	static
	option ipaddr	127.0.0.1
	option netmask	255.0.0.0


#### LAN configuration
config interface lan
	option type 	bridge
	option ifname	"eth0.0"
	option proto	'static'
	option ipaddr	'10.0.0.1'
	option netmask	'255.255.255.0'
	option gateway	''
	option dns	''


#### WAN configuration
config interface	wan
	option ifname	"wl0"
	option proto	dhcp
}}}
'''Notes''':
 *You have to have your derivative network on a different address range than a host network.
 *In the end you will see two interfaces : wl0 with the IP from the other AP and wl0.1 that shows with brctl. The packets are routed by openwrt. The "magic" comes from the fact that the broadcom chip really has two wifi interfaces that can be configured separately and work independently : one as an AP and the other as a STAtion.
 *If there is Encryption key:too big on wl0 after configuring the AP with a wep key, it won't prevent the setup to work. However, one may have to manualy set the wep key using wlc wepkey =1,2021232324 (or another 64 bit wep key instead of 2021222324).
 *Download http://dachary.org/repeater-openwrt.tar.gz for an example installation working on a WRT54GL running Kamikaze 7.09 (19 may 2008).
'''References''':
 *Compiled official Kamikaze [http://www.nbd.name/openwrt.html documentation]
 *Wiki on [:OpenWrtDocs/KamikazeConfiguration:Kamikaze configuration]
