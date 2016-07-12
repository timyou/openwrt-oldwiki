= Buffalo WBR-G54 =

'''Note:''' OpenWrt (Kamikaze v7.06) doesn't work anymore with this device. The last working version is White Russian. The problem is that Kamikaze after a flash tries to get its ip using broken DHCP requests (didn't [http://forum.openwrt.org/viewtopic.php?id=11292 yet found why], maybe because there's VLAN info in it). The Safe mode that allows you to boot with a static ip address doesn't work either because the reset button is not supported by OpenWrt with this device. And Serial or JTAG are not possible.

== Installation ==

Used the same TFTP method as for the WBR2-G54 : the only difference is that the TTL during the bootloader is 128 and not 100.

== Wireless config ==

The old Buffalo 2.20 firmware (newest available for the WBR-G54) uses the older wl*_ nvram settings convention. My wireless config took a lot of fiddling to get working for some reason, so I was keen to preserve it.

I dumped the wl*_ settings, edited them to be wl0_* istead, and scripted them back into the nvram. One "wifi" later, hey presto, working wireless.

== Restoring Buffalo firmware ==

As per the OpenWrt manual except that 34 bytes not 32 need to be trimmed from the front of the file WBR-G54_2.20_1.16 which is obtained from Buffalo's European website.
