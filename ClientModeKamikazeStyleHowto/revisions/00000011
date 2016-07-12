## Please edit system and help pages ONLY in the moinmaster wiki! For more
## information, please see MoinMaster:MoinPagesEditorGroup.
##master-page:CategoryTemplate
##master-date:Unknown-Date
#format wiki
#language en
= Client Mode Wireless =
by Tho Tran — last modified 2007-03-07 13:29

'''Kamikaze Style'''

 * The following instructions will set up client mode wireless on a Fonera device.
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
        option proto    static
        option ipaddr   172.16.0.1
        option netmask  255.255.255.0
#       option type     bridge
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
        #option channel  5
config wifi-iface
        option device   wifi0
        #option network lan
        #option mode     ap
        option mode     sta
        option ssid     yourSSIDHere
        #option hidden   0
        option encryption wep
        option key      your26CharacterHexKeyHere}}}
 . '''Reboot the device. '''
 .
== WPA2-AES ==
Assuming you have WEP working correctly you should now be connected and surfing the web. To get WPA to work you'll need to install the wpa_supplicant package.

{{{
# ipkg update
# ipkg install wpa_supplicant
}}}
/etc/config/wireless

 * The only option you'll have to set now is "option mode sta".
{{{
config wifi-device  wifi0
        option type     atheros
        #option channel  5
config wifi-iface
        option device   wifi0
        #option network lan
        #option mode     ap
        option mode     sta
        #option ssid     yourSSIDHere
        #option hidden   0
        #option encryption wep
        #option key     your26CharacterHexKeyHere}}}
 . '''Reboot the device.'''
/etc/wpa_supplicant.conf

 * Your wifi options are now set in /etc/wpa_supplicant.conf (you'll have to create this file) instead of /etc/config/wireless.
 * Set your SSID.
 * Set your key.
{{{
ctrl_interface=/var/run/wpa_supplicant
update_config=1
network={
        ssid="yourSSIDHere"
        psk="yourKeyHere"
        proto=RSN
        key_mgmt=WPA-PSK
        pairwise=CCMP
        disabled=0
}
}}}

Now start wpa_supplicant.

{{{
# wpa_supplicant -Dwext -iath0 -c/etc/wpa_supplicant.conf -B}}}
That should do it; happy hunting.

== Autostart wpa_supplicant ==
Here's how to get wpa_supplicant to start on boot/reboot.

 * Create the file /etc/init.d/wpaStart.sh
{{{
#!/bin/sh
wpa_supplicant -Dwext -iath0 -c/etc/wpa_supplicant.conf -B}}}
 * Change the permissions on wpaStart.sh to 755.
 * Create a symbolic link to it from /etc/rc.d/ directory.
{{{
# ln -s /etc/init.d/wpaStart.sh S90wpaStart}}}
== Useful Commands ==
 * ifconfig
 * iwconfig
 * wpa_cli
'''List of pages in this category:'''

[[FullSearch()]]

----
 . CategoryCategory
