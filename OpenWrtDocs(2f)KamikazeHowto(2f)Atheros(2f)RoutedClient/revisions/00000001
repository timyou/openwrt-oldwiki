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

config interface wan
	option ifname ath0
	option proto dhcp

config interface lan
	option ifname eth0
	option proto static
	option ipaddr 10.0.0.1
	option netmask 255.255.255.0
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
	option network wan
	option mode sta
	option ssid OpenWrt
	option encryption none
}}}
{{{
reboot
}}}

'''List of pages in this category:'''

[[FullSearch()]]

----
CategoryCategory
