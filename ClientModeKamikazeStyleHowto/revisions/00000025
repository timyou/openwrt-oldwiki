#pragma section-numbers off
||<tablebgcolor="#f1f1ed" tablewidth="40%" tablestyle="margin: 0pt 0pt 1em 1em; float: right; font-size: 0.9em;"style="padding: 0.5em;">[[TableOfContents]]||
= Client Mode Wireless =
'''This way is recommended since it is actually automatic:'''

1. Read the instructions and get the tar.gz package from here http://fon.testbox.dk/packages/NEW/LEGEND4.5/clientscript/

That's it. The package of scripts self-installs and will ask you questions to configure your wired and wireless connections. Your current configuration will be backed up and can be restored with the "aprestore" command. Type in "clientmode" after installation to configure client mode. This is currently the easiest and most complete means of having client mode on an Atheros router. These scripts are incompatible with firmwares that use NVRAM. They are included in the Legend Rev4.5 firmware, which will soon be released on the site.  For Fonera and Meraki Mini (or related) routers only. ^ Meltyblood Aug 2nd 2007

by Tho Tran — last modified 2007-03-07 13:29

2007-12-01 — Tried routed client-mode again with Kamikaze 7.09 and Broadcom !WiFi does not work good (very high ping times and dhcp does not always works reliable, I'll test it in a few month again)

'''Kamikaze Style'''

 * The following instructions will set up routed client-mode wireless on a Fonera device.
 * The two files you'll need to work with are /etc/config/network and /etc/config/wireless.
== Requirements ==
== Configuring client mode ==
=== Bridged client mode ===
=== Routed client mode ===
/etc/config/network

 * Give the LAN interface a static IP.
 * Configure the WAN interface for DHCP.
{{{
config interface loopback
        option ifname   lo
        option proto    static
        option ipaddr   127.0.0.1
        option netmask  255.0.0.0
config interface lan
        option ifname   eth0
#       option type     bridge
        option proto    static
        option ipaddr   192.168.1.1
        option netmask  255.255.255.0
config interface wan
        option ifname   ath0
        option proto    dhcp}}}
/etc/config/wireless

 * Set the wifi-iface option to sta (client mode).
 * Set the SSID to the one you'll be connecting to.
{{{
config wifi-device  wifi0
        option type     atheros
#       option channel  5
#       option diversity 1
#       option txantenna 0
#       option rxantenna 0
#       option distance  2000
# disable radio to prevent an open ap after reflashing:
        option disabled 0
config wifi-iface
        option device   wifi0
#       option network  lan
        option mode     sta
        option ssid     yourSSIDHere
        option hidden   0
#       option txpower  15
#       option bgscan   enable
        option encryption none}}}
 . '''Reboot the device. '''
 .
== Finding and joining networks ==
== Some more configuration ==
== Useful Commands ==
 * ifconfig
 * iwconfig
 * wpa_cli
'''List of pages in this category:'''

[[FullSearch()]]

----
 . CategoryCategory
