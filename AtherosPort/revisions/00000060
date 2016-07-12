== What is this stuff? ==

The AR531x/231x is a platform by Atheros, which is used for dual-band and single-band 108Mb/s routers and accesspoints. It is also refered as a ''WiSoC - Wireless System-on-a-Chip'', and the radio inside often refered as ''RoC - Radio-on-a-Chip''.

== Atheros WiSoC generations/evolution ==

1. AR5001 generation (802.11a only)
 * [http://www.atheros.com/pt/ar5001A.html AR5001AP] (AR5311 CPU + AR5111 5GHz RoC)

2. AR5002 generation (first dual-band designs)
 * AR5002AP-A (AR2312 CPU + AR5122 5GHz RoC)
 * [http://www.atheros.com/pt/AR5002AP-GBulletin.htm AR5002AP-G] (AR2312 CPU + AR2112 2.4GHz RoC)
 * [http://www.atheros.com/pt/AR5002AP-XBulletin.htm AR5002AP-X] (AR2312 CPU + AR5112 2.4/5GHz RoC)
 * [http://www.atheros.com/pt/AR5002AP-2XBulletin.htm AR5002AP-2X] (AR5312 CPU + AR5112 2.4/5GHz RoC + AR2112 2.4GHz RoC)

3-4. AR5003 and AR5004 generation (Super-AG technology)
''The AR5003 got merged into the AR5004. The new !WiSoCs are/were in production, but they were not announced.''
 * AR2313
 * AR5213
 * AR2314

5. AR5005 generation (MIMO technology, onboard AES engine, serial flash)
 * [http://www.atheros.com/pt/AR5005VA.htm AR5005VA] (AR5513 CPU + AR5112 RoC)
 * [http://www.atheros.com/pt/AR5005VL.htm AR5005VL] (AR5513 CPU + AR5112 RoC)

6. AR5006 generation (single-chip solutions)
 * [http://www.atheros.com/pt/AR5006AP-G.htm AR5006AP-G] (AR2315) - 54Mbps only
 * [http://www.atheros.com/pt/AR5006AP-GS.htm AR5006AP-GS] (AR2316)
 * AR5315

7. AR5007 generation (radical decrease of BOM)
 * [http://www.atheros.com/pt/AR5007AP-G.htm AR5007AP-G] (AR2317)

== Devices ==

 * Bufallo WER-AM54G54 (AR5002AP-2X)
 * D-Link [http://www.dlink.com/products/?sec=0&pid=316 DI-524], at least HW rev C1, but it only has 8MB RAM and 1MB ROM.
 * D-Link [http://support.dlink.com/products/view.asp?productid=DWL%2D2210AP DWL-2210AP] (AR2313)
 * D-Link [http://www.dlink.com/products/?pid=292 DWL-2100AP] (AR5002AP-G : core AR2312@180/240MHz, radio AR2112)
 * D-Link [http://www.dlink.com/products/?pid=304 DWL-7100AP] (AR5002AP-2X)
 * D-Link DWL-774 (AR5002AP-2X) (discontinued)
 * LevelOne WBR-3405TX : AR2313A and Marvell 88E6060 switch
 * Linksys [:OpenWrtDocs/Hardware/Linksys/WRT55AG: WRT55AG v2] [http://www1.linksys.com/products/product.asp?grid=33&scid=35&prid=664 Product Link] (AR5002AP-2X)
 * Meraki [http://www.meraki.net/mini.html Mini] (AR2315) - source available for [http://www.meraki.net/linux Meraki's own Linux port]
 * MicraDigital/Belkin F5D7230 (ver.1020ec) (AR2315A)
 * Netgear [http://www.seattlewireless.net/index.cgi/NetgearWGR614 WGR614]v3.
 * Netgear [:OpenWrtDocs/Hardware/Netgear/WGT624: WGT624] [http://www.netgear.com/products/details/WGT624.php Product link] (AR5002AP-G) (v2 AR5001AP)
 * Netgear [http://www.seattlewireless.net/index.cgi/NetgearWG102 WG102] (AR2313)
 * Senao NL-5354 AP1 Aries2 (AR5002AP-2X)
 * Senao NL-3054 AP3 Aries2 (AR2313)
 * Siemens [:OpenWrtDocs/Hardware/Siemens/SE551: SE551] (AR2316)
 * Wistron [:OpenWrtDocs/Hardware/Wistron/CA8-4_CE8-1: CA8-4/CE8-1] aka Ovislink [http://www.ovislink.com.tw/WLA5000AP.htm WLA-5000AP], !LinkPro WLT-108AAP, Diswire CAP2/5 (AR5002AP-X)
 * Wistron CR8-2 aka !LinkPro WLT-108AAR (AR5002AP-2X)
 * Smc WEBT-G aka Philips SNR6500 aka Siemens Wlan Repeater 108 (AR2316)
 
OEM dual APs, internally identical:

 * !TrendNet [http://www.trendware.com/products/TEW-510APB.htm TEW-510APB] Atheros AR5312 SoC 220MHz
 * Tonze AW-6660 
 * SparkLAN WX-7800A
 * !XtendLan WDAP-1001 

and [http://customerproducts.atheros.com/customerproducts/ResultsPageBasic.asp many more].

[http://atheros.rapla.net/ Atheros chipsets based wireless 802.11a/b/g devices]

----

== TODO ==

   * Write docs on the !VxWorks bootloader
   * Get JTAG on the go
   * Get it work, tested

== Firmware/Bootloader ==

There are at least 3 variants

 * !VxWorks' own bootloader - most Atheros devices (There is a description of the basic workings on the [:OpenWrtDocs/Hardware/Netgear/WGT624:Netgear WGT624] page.)
 * !RedBoot - the [http://sources.redhat.com/ecos/docs-latest/redboot/redboot-guide.html manual] is very good.
 * !NetBoot - the standard loader in dwl7100ap allowed boot firmware image via network from tftp server direct to ram - this method is useful for testing, but can not be used for real work...
 * ThreadX - D-Link uses OS called ThreadX on lowend 1M flash + 8M RAM models. They have custom boot loader that doesn't output anything sensible to serial port but does have recovery mode so you can upload firmware using browser.

== JTAG ==

Atheros 531x/231x use standart MIPS EJTAG v2.6 and most of devices use a 14-pin EJTAG header. See a [:JTAG_Cables] for more info on using JTAG.

The latest [http://openwince.sourceforge.net/jtag/ Openwince JTAG] fork contains support for the Atheros chips. The CVS snapshot may be found there: [http://www.amelek.gda.pl/rtl8181/jtag/ jtag-0.6-cvs-20051228]

== How to help ==

If you want to help and got some basic kernel hacking knowledge, you should start by familiarizing yourself with the OpenWrt build system. All the kernel and image stuff is in the target/ subdirectory.

AR531x/231x-specific kernel patches will go into {{{target/linux/linux-2.4/patches/ar531x}}}. The build system part that constructs the firmware images for AR531x based routers will be in {{{target/linux/image/ar531x}}}.

== Work done currently ==

Support for the AR2315 based devices is available in Kamikaze. Support for the older/newer designs will be added soon soon, with runtime board detection support.

----
CategoryOpenWrtPort
