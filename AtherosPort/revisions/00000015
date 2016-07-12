[[TableOfContents]]
= Status of the Atheros 531x/231x port of OpenWrt =

== What is this stuff? ==

The AR531x and 231x is a router platform by Atheros, which is used for dual-band and single-band 108Mb/s routers, including
 * Netgear [http://www.seattlewireless.net/index.cgi/NetgearWGR614 WGR614]v3.
 * [:OpenWrtDocs/Hardware/Netgear/WGT624:Netgear WGT624] [http://www.netgear.com/products/details/WGT624.php Product link]
 * [http://www1.linksys.com/products/product.asp?grid=33&scid=35&prid=664 Linksys WRT55AG v2] (Note: v1 '''IS Broadcom based''', so this porting effort doesn't have anything to do with it.)
 * [http://www.dlink.com/products/?sec=0&pid=316 D-Link DI-524], at least HW rev C1, but it only has 8MiB RAM and 1MiB ROM (see [http://www.kollasch.net/JonathanKollasch/WirelessEquipmentPhotos here])
 * [http://support.dlink.com/products/view.asp?productid=DWL%2D2210AP D-Link DWL-2210AP], at least according to [http://devicescape.com Devicescape]

and [http://customerproducts.atheros.com/customerproducts/ResultsPageBasic.asp many more].

The guys over at [http://www.jungo.com/openrg/download/jungo_software_specification.pdf Jungo] claim to support the AR531X/AR2313:
"The following hardware components/platforms are fully supported. Jungo provides production-ready OpenRG and OpenSM
software evaluations for all listed reference designs..."
 *  Atheros
    * AR531X
    * AR2313

Someone might ask them, if they can supply some newer kernel patches for this plattform.

----
There is an accesspoint device sold in the Czech Republic which is also based on an AR2313. It wouldn't be interesting but it seems to be one more atheros SoC device running linux. You can find a boot up log [http://cz-free.net/phpBB2/viewtopic.php?p=537& here]. A firmware for this ap is [http://www.i4shop.net/cz/iObchod/2005/Firmware/ca8-4-v1.07e01.bin here]. 

== TODO ==

   * Write docs on the VxWorx bootloader
   * Port the kernel patches to recent kernels
   * Get JTAG on the go
   * Port the ethernet driver from RedBoot to Linux
   * Get it work, tested, and later into the OpenWrt buildroot. 

== Firmware/Bootloader ==

There are at least 2 variants

 * VxWorx' own bootloader - most AR7 devices
 * RedBoot


= How to help =

If you want to help and got some basic kernel hacking knowledge, you should start by familiarizing yourself with the OpenWrt build system. It now has support for building images for non-broadcom hardware.
All the kernel and image stuff is in the target/ subdirectory.

All the sources we have for this platform is at http://downloads.openwrt.org/reference/

AR531x/231x-specific kernel patches will go into {{{target/linux/linux-2.4/patches/ar531x}}}. The build system part that constructs the firmware images for AR531x based routers will be in {{{target/linux/image/ar531x}}}.
