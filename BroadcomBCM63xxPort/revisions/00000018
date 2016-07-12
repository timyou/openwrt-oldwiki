[[TableOfContents]]

= Status of the Broadcom 63xx port of OpenWrt =

 * The Broadcom BCM963xx currently only works with BCM96348 boards, but will soon with others as well
 * We have no GPL'd drivers for Ethernet, DSL so this makes the board pretty useless

== What is this Broadcom 63xx stuff? ==

[http://www.broadcom.com/products/DSL/xDSL-CPE-Solutions/BCM6348 Broadcom63xx SoC]integrates ADSL/ADSL2+ features, routing, and external Wireless NIC.
== What are 63xx variants? ==
There are four 63xx variants: bcm6345,bcm6338,bcm6348,bcm6358
||<tablewidth="532px" tableheight="155px" tablealign="">Chip||CPU Mhz||USB Device||USB Host||WiFi||
||bcm6345||  75  ||1.1||-||-||
||bcm6338||  240  ||1.1||-||-||
||bcm6348||  240  ||1.1||1.1||Yes||
||bcm6358||  300  ||2.0||2.0||Yes||

== Known 63xx platforms ==

Known 6345 platforms*:
||[http://www.dynalink.com.au/modemsadsl_cur.htm?prod=RTA230 Dynalink RTA230] ||
||[:OpenWrtDocs/Hardware/Dynalink/RTA770W:Dynalink RTA770W] ||
||[:OpenWrtDocs/Hardware/Linksys/WAG54GS:ZTE ZXDSL 831A]||
||[http://gigaset.siemens.com/shc/0,1935,hq_en_0_42931_rArNrNrNrN,00.html Siemens SE515] ||
||[http://www.zhone.com/products/6211/ Paradyne 6211-A1] ||
||[http://www.usr.com/images/products/product-emea.asp?prod=9105 US Robotics USR9105] ||
||[http://www.usr.com/images/products/product-emea.asp?prod=9106 US Robotics USR9106] || ||


Known 6338 platforms*:

||[:OpenWrtDocs/Hardware/Huawei/EchoLife HG520:Huawei EchoLife HG510] ||
||[:OpenWrtDocs/Hardware/Linksys/WAG54GS:ZTE ZXDSL 831CII] ||

Known 6348 platforms*:
||[http://www.comtrend.com/index.php?module=products&op=show&sn=2 Comtrend CT-536+] ||
||[:OpenWrtDocs/Hardware/Linksys/WAG54GS:Linksys WAG54GS] ||
||[:OpenWrtDocs/Hardware/Linksys/WAG54GX2:Linksys WAG54GX2] ||
||[:OpenWrtDocs/Hardware/Netgear/DG834GT:Netgear DG834GT] ||
||[http://www.usr-emea.com/products/p-broadband-product.asp?prod=bb-9108&loc=unkg US Robotics USR9108] ||
||[:OpenWrtDocs/Hardware/Huawei/EchoLife HG520:Huawei EchoLife HG520] ||
||[:OpenWrtDocs/Hardware/Huawei/HG550:Huawei EchoLife HG550] ||
||[http://www.tecomproduct.com/AH4021.htm Hitachi AH4021 (German Telekom "Speedport W500V")] ||
||[:OpenWrtDocs/Hardware/Asus/WL600g:ASUS WL-600G] ||
||[:OpenWrtDocs/Hardware/Belkin/f5d7633-4:belkin f5d7633-4] ||
||[:OpenWrtDocs/Hardware/Freebox/FreeboxV4: Freebox v4] ||
||[:OpenWrtDocs/Hardware/Inventel/Livebox: Inventel Livebox] ||
||[http://www.dlink.com/products/?pid=567 D-Link DSL-2640B] ||

Known 6358 platforms*:
||[:OpenWrtDocs/Hardware/Freebox/FreeboxV5: Freebox v5] ||
||[:OpenWrtDocs/Hardware/Neuf/NeufBoxV4: NeufBox v4] ||

* If no dedicated Openwrt page is found an external link is supplied

== Finished tasks ==
The support for Broadcom 63xx is at this state :

 * Linux 2.6.x booting

== TODO ==

 * Talk with Broadcom related vendors to make them release some sources

== Firmware/Bootloader ==
Some devices use RedBoot such as Inventel Liveboxes. Other run CFE with a built-in LZMA decompressor such as Siemens SE515, Free Freebox ...

== Paradyne 6211-A1 JTAG & RS232 ==
Board image attachment:6211_A1_JTAG.jpg

= How to help =
 * Create valid firmware images.
 * Test the currently merged kernel in order to see if it boots on CFE based boards.
 * It can now boot on RedBoot enabled devices, supply a valid MTD partition in the kernel command line, as well as boot_loader=RedBoot
----
 CategoryOpenWrtPort
