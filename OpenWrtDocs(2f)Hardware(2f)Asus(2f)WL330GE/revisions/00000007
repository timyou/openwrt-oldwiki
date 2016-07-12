[[TableOfContents]]

== Hardware Info ==

The hardware is very similar to the [:OpenWrtDocs/Hardware/Asus/WL520GU:WL-520gU] and uses the heavily integrated BCM5354 core. '''This device is not to be confused with the WL-330g''', which is a distinctly different piece of hardware.

== Bootloader Recovery Mode ==

The device can be booted in bootloader recovery mode by powering on while holding the reset button. The power LED should flash and the router should respond to a tftp'd firmware image and pings at '''192.168.1.220'''. See [:OpenWrtDocs/Hardware/Asus/Flashing:flashing Asus routers].

== Support in 8.09 ==

Unfortunately, [http://lists.openwrt.org/pipermail/openwrt-devel/2009-February/003900.html the patch] that added support for detecting and configuring this device was added after 8.09 was released (see [https://dev.openwrt.org/changeset/14624 r14624]). Everything works fine out of the box with the standard 8.09 image, but the reset button and power LED are not supported. Minor features, yes, but without them it's impossible to get the device in to [:OpenWrtDocs/Troubleshooting:failsafe mode]. Since this device has only one ethernet port, you may find yourself locked out. With failsafe mode you could recover without reflashing.

Your options are applying the patch to the 8.09 sources or downloading a pre-compiled firmware that I'm providing as a courtesy. This firmware matches the 8.09 release exactly, with the patch added and without the kmod-switch package (this is unneeded).

 * [http://priv.kupesoft.com/openwrt/wl-330ge/openwrt-WL-330gE-8.09-brcm-2.4-squashfs.trx openwrt-WL-330gE-8.09-brcm-2.4-squashfs.trx]
 * [http://etc.kupesoft.com/openwrt/wl-330ge/WL-330gE.patch WL-330gE.patch]
