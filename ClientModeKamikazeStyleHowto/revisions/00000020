## Please edit system and help pages ONLY in the moinmaster wiki! For more
## information, please see MoinMaster:MoinPagesEditorGroup.
##master-page:CategoryTemplate
##master-date:Unknown-Date
#format wiki
#language en
= Client Mode Wireless =
'''This way is recommended since it is actually automatic:'''

1. Read the instructions and get the tar.gz package from here http://fon.testbox.dk/packages/NEW/LEGEND4.5/clientscript/

That's it. The package of scripts self-installs and will ask you questions to configure your wired and wireless connections. Your current configuration will be backed up and can be restored with the "aprestore" command. Type in "clientmode" after installation to configure client mode. This is currently the easiest and most complete means of having client mode on an Atheros router. These scripts are incompatible with firmwares that use NVRAM. They are included in the Legend Rev4.5 firmware, which will soon be released on the site.  For Fonera and Meraki Mini (or related) routers only.
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


by Tho Tran — last modified 2007-03-07 13:29

'''Kamikaze Style'''

 * The following instructions will set up routed client-mode wireless on a Fonera device.
 * The two files you'll need to work with are /etc/config/network and /etc/config/wireless.
== WEP ==
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
 * Set the encryption type to WEP.
 * Set the encryption key.
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
        option encryption wep
        option key      your26CharacterHexKeyHere}}}
 . '''Reboot the device. '''
 .
== WPA2-AES ==
Assuming you have WEP working correctly you should now be connected and surfing the web. To get WPA to work you'll need to install the wpa-supplicant package.

{{{
# ipkg update
# ipkg install wpa-supplicant}}}
/etc/config/wireless

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
        option encryption psk2
        option key      yourtopsecretpassword}}}
 . '''Reboot the device.'''
That should do it; happy hunting.

== Useful Commands ==
 * ifconfig
 * iwconfig
 * wpa_cli
'''List of pages in this category:'''

[[FullSearch()]]

----
 . CategoryCategory
