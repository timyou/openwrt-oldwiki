## Please edit system and help pages ONLY in the moinmaster wiki! For more
## information, please see MoinMaster:MoinPagesEditorGroup.
##master-page:CategoryTemplate
##master-date:Unknown-Date
#format wiki
#language en

{{{
vi /etc/config/network
}}}
{{{
config interface loopback
	option ifname lo
	option proto static
	option ipaddr 127.0.0.1
	option netmask 255.0.0.0

config interface lan
	option ifname eth0
	option type bridge
	option proto static
	option ipaddr 10.0.0.2
	option netmask 255.255.255.0
	option gateway 10.0.0.1
	option dns 10.0.0.1
}}}
{{{
vi /etc/config/wireless
}}}
{{{
config wifi-device wifi0
	option type atheros
	option channel 11

config wifi-iface
	option device wifi0
	option network lan
	option mode ap
	option ssid OpenWrt
	option encryption none
}}}
{{{
/etc/init.d/dnsmasq disable
}}}
{{{
reboot
}}}

'''List of pages in this category:'''

[[FullSearch()]]

----
CategoryCategory
