[[TableOfContents]]

== Hardware Info ==

The hardware is very similar to the [:OpenWrtDocs/Hardware/Asus/WL520GU:WL-520gU] and uses the heavily integrated BCM5354 core. '''This device is not to be confused with the WL-330gE''', which is a distinctly different piece of hardware.

== Bootloader Recovery Mode ==

The device can be booted in bootloader recovery mode by powering on while holding the reset button. The power LED should flash and the router should respond to a tftp'd firmware image and pings at '''192.168.1.220'''. See [:OpenWrtDocs/Hardware/Asus/Flashing:flashing Asus routers].

== Support in 8.09 ==

Unfortunately, [http://lists.openwrt.org/pipermail/openwrt-devel/2009-February/003900.html this patch] that adds support for detecting and configuring this device was added after 8.09 was released in [https://dev.openwrt.org/changeset/14624 r14624]. Everything works out of the box with the standard 8.09 image, but the reset button and power LED are not supported. It therefore is impossible to get the device in to failsafe mode. Your options are applying the patch to the 8.09 sources or downloading a pre-compiled firmware that I'm providing as a courtesy. This firmware matches the 8.09 release exactly, with the added patch and without the kmod-switch package (this is unneeded).



== Patch Info ==

Works out of the box, with the exception of the reset button. For now, you can download and apply [http://lists.openwrt.org/pipermail/openwrt-devel/2009-February/003900.html this patch] against trunk or 8.09 for proper detection and support.
