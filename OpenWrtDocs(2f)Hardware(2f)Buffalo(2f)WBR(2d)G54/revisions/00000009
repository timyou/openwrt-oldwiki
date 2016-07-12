= Buffalo WBR-G54 =

attachment:wbrg54-top.jpg

'''Note:''' OpenWrt (Kamikaze v7.09) doesn't work out of the box with this device (the last simple working version is White Russian). The problem is that the default Kamikaze config is to use vlans on the first ethernet adapter, but this device has different ethernet adapters for LAN and WAN, so gets all confused. You need to build your own copy of Kamikaze, and either fix the vlan stuff there, or just enable wifi and ssh in to fix.

You can download a pre-built Kamikaze 7.09 with working vlan/ethernet configuration from [http://gagravarr.org/misc/openwrt-kamikaze_7.09_WBR-G54-squashfs.trx here]. It will come up with ssh, and a default root password of "password", on the IP 192.168.1.9

See [http://forum.openwrt.org/viewtopic.php?id=11292 this forum post] for more details. Apparently, Serial or JTAG are not possible.

== Installation ==

Used the same TFTP method as for the WBR2-G54 : the only difference is that the TTL during the bootloader is 128 and not 100.

== Wireless config ==

The old Buffalo 2.20 firmware (newest available for the WBR-G54) uses the older wl*_ nvram settings convention. My wireless config took a lot of fiddling to get working for some reason, so I was keen to preserve it.

I dumped the wl*_ settings, edited them to be wl0_* istead, and scripted them back into the nvram. One "wifi" later, hey presto, working wireless.

== Restoring Buffalo firmware ==

As per the OpenWrt manual except that 34 bytes not 32 need to be trimmed from the front of the file WBR-G54_2.20_1.16 which is obtained from Buffalo's European website.
