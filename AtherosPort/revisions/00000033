[[TableOfContents]]
= Status of the Atheros 531x/231x port of OpenWrt =

== What is this stuff? ==

The AR531x and 231x is a router platform by Atheros, which is used for dual-band and single-band 108Mb/s routers, including
 * Netgear [http://www.seattlewireless.net/index.cgi/NetgearWGR614 WGR614]v3.
 * Netgear [:OpenWrtDocs/Hardware/Netgear/WGT624: WGT624] [http://www.netgear.com/products/details/WGT624.php Product link]
 * Linksys [:OpenWrtDocs/Hardware/Linksys/WRT55AG: WRT55AG v2] [http://www1.linksys.com/products/product.asp?grid=33&scid=35&prid=664 Product Link] (Note: v1 '''IS Broadcom based''', so this porting effort doesn't have anything to do with it.)
 * D-Link [http://www.dlink.com/products/?sec=0&pid=316 DI-524], at least HW rev C1, but it only has 8MiB RAM and 1MiB ROM (see [http://www.kollasch.net/JonathanKollasch/WirelessEquipmentPhotos here])
 * D-Link [http://support.dlink.com/products/view.asp?productid=DWL%2D2210AP DWL-2210AP]
 * Senao NL-5354 AP1 Aries2 dual band AP (AR5312+AR5112+AR2112)
 * Senao NL-3054 AP3 Aries2 (AR2313+AR2112 radio)
 * D-Link DWL-7100AP [http://www.dlink.com/products/?pid=304]

OEM dual APs, internally identical:

 * !TrendNet TEW-510APB [http://www.trendware.com/sp/products/TEW-510APB.htm]
 * Tonze AW-6660 
 * SparkLAN WX-7800A
 * !XtendLan WDAP-1001 
 * WRTA-119AG_V01

and [http://customerproducts.atheros.com/customerproducts/ResultsPageBasic.asp many more].

----

== TODO ==

   * Write docs on the !VxWorks bootloader
   * Port the kernel patches to recent kernels
   * Get JTAG on the go
   * Get it work, tested, and later into the OpenWrt buildroot. 

== Firmware/Bootloader ==

There are at least 3 variants

 * !VxWorks' own bootloader - most Atheros devices (There is a description of the basic workings on the [:OpenWrtDocs/Hardware/Netgear/WGT624:Netgear WGT624] page.)
 * !RedBoot - the [http://sources.redhat.com/ecos/docs-latest/redboot/redboot-guide.html manual] is very good.
 * !NetBoot - the standart loader in dwl7100ap allowed boot firmware image via network from tftp server direct to ram - this method is useful for testing, but can used for real work...

== JTAG ==

Atheros 531x/231x use standart MIPS EJTAG v2.6 and most of devices use a 14-pin EJTAG header. See a [:JTAG_Cables] for more info on using JTAG.

The latest [http://openwince.sourceforge.net/jtag/ Openwince JTAG] fork contains support for the Atheros chips. The CVS snapshot may be found there: [http://www.amelek.gda.pl/rtl8181/jtag/ jtag-0.6-cvs-20051228]

= How to help =

If you want to help and got some basic kernel hacking knowledge, you should start by familiarizing yourself with the OpenWrt build system. It now has support for building images for non-broadcom hardware.
All the kernel and image stuff is in the target/ subdirectory.

All the sources we have for this platform is at http://downloads.openwrt.org/reference/
Others source code could be found on ftp://ftp.gpl-devices.org/pub/platforms/Atheros_531x_and_231x/  .
Note that D-link_DWL-2210AP/v1.0.2.8/dwl2210ap-source_1.0.2.8.tar.gz seems to include more kernel code than mips-linux-2.4.25.tar.bz2 one (ethernet stuff).


AR531x/231x-specific kernel patches will go into {{{target/linux/linux-2.4/patches/ar531x}}}. The build system part that constructs the firmware images for AR531x based routers will be in {{{target/linux/image/ar531x}}}.

== Work Done currently ==

The architecture files are updated and in the openwrt buildroot. At present it is not fully integrated, it defaults to using the AP30 configuration, and the ethernet driver is not optional. Support for ar5315 series CPUs is not present.

There are patches in {{{target/linux/ar531x-2.4/patches/}}}, the config file for the kernel in {{{target/linux/ar531x-2.4/config}}}.

Patches still to be applied:

    Removal of PCI based packages as ar5312 series CPU's lack PCI.

----
CategoryOpenWrtPort
