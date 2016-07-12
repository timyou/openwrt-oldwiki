[[TableOfContents]]

= Status of the Broadcom 63xx port of OpenWrt =

 * The Broadcom BCM963xx currently only works with BCM96348 boards, but will soon with others as well
 * We have no GPL'd drivers for Ethernet, DSL so this makes the board pretty useless

== What is this Broadcom 63xx stuff? ==

[http://www.broadcom.com/products/DSL/xDSL-CPE-Solutions/BCM6348 Broadcom63xx SoC]integrates ADSL/ADSL2+ features, routing, and external Wireless NIC.
== What are 63xx variants? ==
There are four 63xx variants: bcm6345,bcm6338,bcm6348,bcm6358
||<tablewidth="532px" tableheight="155px" tablealign="">Chip||CPU Mhz||USB Device||USB Host||WiFi||ADSL2||ADSL2+||VDSL||
||bcm6345||  75  ||1.1||-||-||Yes||No||No||
||bcm6338||  240  ||1.1||-||-||Yes||Yes||No||
||bcm6348||  240  ||1.1||1.1||Yes||Yes||Yes||No||
||bcm6358||  300  ||2.0||2.0||Yes||Yes||Yes||Yes||

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
||[http://ru.asus.com/products.aspx?l1=13&l2=96&l3=0&l4=0&model=1105&modelmenu=1 ASUS AM602] ||
||[:OpenWrtDocs/Hardware/Huawei/EchoLife HG520:Huawei EchoLife HG510] ||
||[http://www.netgear.co.uk/adsl_ethernet_modem_dm111p.php Netgear DM111P] ||
||[:OpenWrtDocs/Hardware/Linksys/WAG54GS:ZTE ZXDSL 831CII] ||

Known 6348 platforms*:
||[http://ru.asus.com/products.aspx?l1=13&l2=96&l3=0&l4=0&model=1106&modelmenu=1 ASUS AM604] ||
||[http://ru.asus.com/products.aspx?l1=13&l2=96&l3=0&l4=0&model=1107&modelmenu=1 ASUS AM604g] ||
||[:OpenWrtDocs/Hardware/Asus/WL600g:ASUS WL-600G] ||
||[:OpenWrtDocs/Hardware/Belkin/f5d7633-4:Belkin f5d7633-4] ||
||[http://www.dlink.com/products/?pid=567 D-Link DSL-2640B] ||
||[http://www.comtrend.com/index.php?module=products&op=show&sn=2 Comtrend CT-536/1+] ||
||[http://comtrend.com/index.php?module=products&op=show&sn=41 Comtrend CT-638/1] ||
||[:OpenWrtDocs/Hardware/Freebox/FreeboxV4: Freebox v4] ||
||[http://www.tecomproduct.com/AH4021.htm Hitachi AH4021 (German Telekom "Speedport W500V")] ||
||[:OpenWrtDocs/Hardware/Huawei/EchoLife HG520:Huawei EchoLife HG520] ||
||[:OpenWrtDocs/Hardware/Huawei/HG550:Huawei EchoLife HG550] ||
||[:OpenWrtDocs/Hardware/Inventel/Livebox: Inventel Livebox] ||
||[:OpenWrtDocs/Hardware/Linksys/WAG54GS:Linksys WAG54GS] ||
||[:OpenWrtDocs/Hardware/Linksys/WAG54GX2:Linksys WAG54GX2] ||
||[http://www-uk.linksys.com/servlet/Satellite?c=L_Product_C2&childpagename=UK%2FLayout&cid=1169671146123&pagename=Linksys%2FCommon%2FVisitorWrapper&lid=4612360558B01  Linksys WAG325N] ||
||[http://www-se.linksys.com/servlet/Satellite?c=L_Product_C2&childpagename=SE%2FLayout&cid=1147937922090&pagename=Linksys%2FCommon%2FVisitorWrapper Linksys WAG300N] ||
||[http://www.netcomm.com.au/ADSL/NB8W_new.php Netcomm NB8W] (Re-branded Comtrend CT-536) ||
||[http://www.netcomm.com.au/ADSL/NB9_new.php Netcomm NB9] (Re-branded Comtrend CT-638) ||
||[http://www.netcomm.com.au/ADSL/NB9W_new.php Netcomm NB9W] (Re-branded Comtrend CT-638) ||
||[:OpenWrtDocs/Hardware/Netgear/DG834GT:Netgear DG834GT] ||
||[http://www.netgear.co.uk/rangemaxnext_wirelessbroadbandrouter_dg834n.php Netgear DG834N] ||
||[http://www.netgear.co.uk/wireless_modem_router_dg834pn.php Netgear DG834PN] ||
||[http://www.thomson-broadband.co.uk/codepages/content3.asp?c=7&ProductID=511 Thomson Speedtouch ST585v6] ||
||[http://www.usr-emea.com/products/p-broadband-product.asp?prod=bb-9107&loc=unkg US Robotics USR9107] ||
||[http://www.usr-emea.com/products/p-broadband-product.asp?prod=bb-9108&loc=unkg US Robotics USR9108] ||

Known 6358 platforms*:
||[:OpenWrtDocs/Hardware/Freebox/FreeboxV5: Freebox v5] ||
||[:OpenWrtDocs/Hardware/Neuf/NeufBoxV4: NeufBox v4] ||
||[http://www.usr-emea.com/products/p-broadband-product.asp?prod=bb-9113&loc=unkg US Robotics USR9113] ||

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
