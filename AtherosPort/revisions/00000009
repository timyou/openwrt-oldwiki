[[TableOfContents]]
= Status of the Atheros 531x/231x port of OpenWrt =

== What is this stuff? ==

The AR531x and 231x is a router platform by Atheros, which is used for dual-band and single-band 108Mb/s routers, including
 * [:OpenWrtDocs/Hardware/Netgear/WGT624:Netgear WGT624] [http://www.netgear.com/products/details/WGT624.php Product link]
 * [http://www1.linksys.com/products/product.asp?grid=33&scid=35&prid=664 Linksys WRT55AG v2] (Note: v1 '''IS Broadcom based''', so this porting effort doesn't have anything to do with it.)
 * [http://www.dlink.com/products/?sec=0&pid=316 D-Link DI-524], at least HW rev C1
 * [http://support.dlink.com/products/view.asp?productid=DWL%2D2210AP D-Link DWL-2210AP], at least according to [http://devicescape.com Devicescape]

and many more.

The guys over at [[http://www.jungo.com/openrg/download/jungo_software_specification.pdf Jungo]] claim to support the AR531X/AR2313:
The following hardware components/platforms are fully supported. Jungo provides production-ready OpenRG and OpenSM
software evaluations for all listed reference designs...
 *  Atheros
    * AR531X
    * AR2313

Someone might ask them, if they can supply some newer kernel patches for this plattform.

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
