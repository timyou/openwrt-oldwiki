#pragma section-numbers off
||<tablebgcolor="#f1f1ed" tablewidth="40%" tablestyle="margin: 0pt 0pt 1em 1em; float: right; font-size: 0.9em;"style="padding: 0.5em;">[[TableOfContents]]||
= Client Mode Wireless =

'''Kamikaze Style'''

 * The two files you'll need to work with are /etc/config/network and /etc/config/wireless.

== AP without authentication (open) ==
== AP using WEP ==
== AP using WPA/WPA2 ==
WPA requires a program that interfaces with the driver called a supplicant.  There are two supplicants available for OpenWRT (and Linux, in general): wpa_supplicant and xsupplicant.  Xsupplicant supports both Atheros and Broadcom devices (e.g. WRT54G), while wpa_supplicant supports Atheros (among other chipsets), but not Broadcom.

=== wpa_supplicant ===
=== xsupplicant ===
== Bridged and routed client modes ==
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
== Finding networks ==
Both Broadcom and Atheros chipsets support scanning with the iwlist command.  This command will scan all interfaces for networks:
[code]
iwlist scanning
[/code]

== Automated Script for Fonera and Meraki ==
/!\ '''These scripts are third party content. They are not released or supported by the !OpenWrt developers.'''

'''For Fonera and Meraki Mini (or related) routers only.'''

Read the instructions and get the tar.gz package from here http://fon.testbox.dk/packages/NEW/LEGEND4.5/clientscript/

That's it. The package of scripts self-installs and will ask you questions to configure your wired and wireless connections. Your current configuration will be backed up and can be restored with the "aprestore" command. Type in "clientmode" after installation to configure client mode. This is currently the easiest and most complete means of having client mode on an Atheros router. These scripts are incompatible with firmwares that use NVRAM. They are included in the Legend Rev4.5 firmware, which will soon be released on the site above. ^ Meltyblood Aug 2nd 2007

== Useful Commands ==
 * ifconfig
 * iwconfig
 * wpa_cli
'''List of pages in this category:'''

[[FullSearch()]]

----
 . CategoryCategory
