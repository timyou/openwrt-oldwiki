The Buffalo WHR-HP-G54-4 seems to work fine with OpenWRT RC5.

== Flo's user report ==
After uploading the WhiteRussian RC5 file "openwrt-brcm-2.4-jffs2-4MB.trx" the router is reachable via LAN interface with IP 192.168.11.1.

mtd erase nvram (for resetting NVRAM settings) seem to be supported by this device.

For getting the WirelessLAN interface to work it's necessary to manually set the corresponding OpenWRT NVRAM wireless variables:

nvram set wifi_ifname=eth1

nvram set wlan_hardware_present=yes

nvram commit

==> reboot the device

Maybe you would also change the LAN IP-range to OpenWRT defaults:

nvram set lan_ipaddr=192.168.1.1

nvram set lan_netmask=255.255.255.0

nvram commit

==> reboot the device

Hope I did not forget anything ;-)
