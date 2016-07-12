[[TableOfContents]]
= Status of the Broadcom 63xx port of OpenWrt =

== What is this Broadcom 63xx stuff? ==

[http://www.broadcom.com/products/DSL/xDSL-CPE-Solutions/BCM6348 Broadcom63xx SoC] integrates ADSL/ADSL2+ features, routing, and external Wireless NIC.

Known 6345 platforms*:
||[http://www.dynalink.com.au/modemsadsl_cur.htm?prod=RTA230 Dynalink RTA230] ||
||[:OpenWrtDocs/Hardware/Dynalink/RTA770W:Dynalink RTA770W] ||
||[http://gigaset.siemens.com/shc/0,1935,hq_en_0_42931_rArNrNrNrN,00.html Siemens SE515] ||

Known 6348 platforms*:
||[http://www.comtrend.com/index.php?module=products&op=show&sn=2 Comtrend CT-536+] ||
||[:OpenWrtDocs/Hardware/Linksys/WAG54GS:Linksys WAG54GS] ||
||[:OpenWrtDocs/Hardware/Linksys/WAG54GX2:Linksys WAG54GX2] ||
||[:OpenWrtDocs/Hardware/Netgear/DG834GT:Netgear DG834GT] ||
||[http://www.usr-emea.com/products/p-broadband-product.asp?prod=bb-9108&loc=unkg US Robotics USR9108] ||
||[:OpenWrtDocs/Hardware/Huawei/EchoLife_HG520:Huawei EchoLife HG520] ||
||[:OpenWrtDocs/Hardware/Huawei/HG550:Huawei EchoLife HG550] ||

* If no dedicated Openwrt page is found an external link is supplied

== Finished tasks ==

The support for Broadcom 63xx is at this state :

   * Linux 2.6.16.7 kernel booting

== TODO ==

   * Fix MTD/Flash map driver (need special table for CFE and [http://sources.redhat.com/ecos/docs-latest/redboot/redboot-guide.html RedBoot] devices)
   * Try to run binary drivers with CONFIG_VERSIONING set on

== Firmware/Bootloader ==

Some devices use RedBoot such as Inventel Liveboxes. Other run CFE with a built-in LZMA decompressor such as Siemens SE515, Free Freebox ...

= How to help =

   * Create valid firmware images.

   * Test the currently merged kernel in order to see if it boots on CFE based boards.
   * It can now boot on RedBoot enabled devices, supply a valid MTD partition in the kernel command line, as well as boot_loader=RedBoot
----
CategoryOpenWrtPort
