= Repeater =
by pier11 — last modified 2007-04-12 21:28

'''Applicable''': Kamikaze, Broadcom.

'''Tested''': WRT54G v2.0, Kamikaze r6816(02 Apr).

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
 
'''References''':
 *Compiled official Kamikaze [http://www.nbd.name/openwrt.html documentation]
 *Wiki on [:OpenWrtDocs/KamikazeConfiguration:Kamikaze configuration]
