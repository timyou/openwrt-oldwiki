[[TableOfContents]]

This page covers the BCM63xx SoC specificities, but the BCM33xx SoC (excluding BCM3302 which is a CPU) are the exact same chip, except that the DSL core is replaced with a DOCSIS/EuroDOCSIS one.

= Status of the Broadcom 63xx port of OpenWrt =
 * The Broadcom BCM963xx currently only works with BCM6348/BCM6358 boards. Others expected soon.
 * We have GPL drivers for USB (OHCI and EHCI), Ethernet, DSL is still binary though.
 * Belkin has released [http://www.belkin.com/uk/support/article/?lid=enu&pid=F5D7633uk4A&aid=9294&scid=314 "GPL code for the F5D7633"], but it only has binary Broadcom drivers.
 * TP-link also has some code out for the platform --> see [http://www.tp-link.com/support/gpl.asp TP-link GPL code for many of their products (many are broadcom based).]
 * D-Link GPL download center: [http://tsd.dlink.com.tw/ D-Link GPL code for all of their products (DSL-2640B, DSL-2740B).]

== What is this Broadcom 63xx stuff? ==
[http://www.broadcom.com/products/DSL/xDSL-CPE-Solutions/BCM6348 Broadcom63xx SoC]integrates ADSL/ADSL2+ features, routing, and external Wireless NIC.

The ethernet SOC is similar to that used in the BCM7318 which is also used in the Tivo. Tivo has release complete sources of their ethernet driver [http://dynamic.tivo.com/linux/linux.asp tivo source] which could be the basis of a working BCM63xx driver. See the files:

{{{
 linux-2.4/drivers/net/
   bcmemac7318.c
   bcmemac7318.h
   bcmenet.c
   bcmenet.h
   bcmenet_regs.h
}}}
== What are 63xx variants? ==
There are six 63xx variants: bcm6345,bcm6338,bcm6348,bcm6358,bcm6368,bcm6816
||<tablewidth="532px" tableheight="155px">Chip ||CPU Mhz ||USB Device ||USB Host ||WiFi ||ADSL2 ||ADSL2+ ||VDSL || Fiber ||
||bcm6345 ||  75 ||1.1 ||- ||- ||Yes ||No ||No ||
||bcm6335 ||  ??? ||?.? ||- ||- ||? ||? ||? ||No ||
||bcm6338 ||  240 ||1.1 ||- ||- ||Yes ||Yes ||No ||No ||
||bcm6348 ||  240 ||1.1 ||1.1 ||Yes ||Yes ||Yes ||No ||No ||
||bcm6358 ||  300 ||2.0 ||2.0 ||Yes ||Yes ||Yes ||Yes ||No ||
||bcm6368 ||  300 ||2.0 ||2.0 ||Yes ||Yes ||Yes ||Yes ||Yes ||
||bcm6816 ||  300 ||2.0 ||2.0 ||Yes ||Yes ||Yes ||Yes ||Yes ||


There are also some other variants like bcm6341, which is a DSP used in VoIP products.

== Known 63xx platforms ==
=== Known 6345 platforms:* ===
||[http://www.dynalink.com.au/modemsadsl_cur.htm?prod=RTA230 Dynalink RTA230] ||
||[:OpenWrtDocs/Hardware/Dynalink/RTA770W:Dynalink RTA770W] ||
||[:OpenWrtDocs/Hardware/Linksys/WAG54GS:ZTE ZXDSL 831A] ||
||[http://gigaset.siemens.com/shc/0,1935,hq_en_0_42931_rArNrNrNrN,00.html Siemens SE515] ||
||[http://www.zhone.com/products/6211/ Paradyne 6211-A1] ||
||[http://www.usr.com/images/products/product-emea.asp?prod=9105 US Robotics USR9105] ||
||[http://www.usr.com/images/products/product-emea.asp?prod=9106 US Robotics USR9106] ||
||[http://www.belkin.com/uk/support/product/?lid=enu&pid=F5D7632uk4A Belkin F5D7632 v2] ||
=== Known 6338 platforms*: ===
||[http://ru.asus.com/products.aspx?l1=13&l2=96&l3=0&l4=0&model=1105&modelmenu=1 ASUS AM602] ||
||[:OpenWrtDocs/Hardware/Huawei/EchoLife HG520:Huawei EchoLife HG510] ||
||[http://www.netgear.co.uk/adsl_ethernet_modem_dm111p.php Netgear DM111P] ||
||[:OpenWrtDocs/Hardware/Linksys/WAG54GS:ZTE ZXDSL 831CII] ||
||<style="text-align: left; vertical-align: top;">[http://www.dynalink.co.nz/modemsadsl_cur.htm?prod=RTA1320 Dynalink RTA1320] [http://www.nateks-networks.ru/content/view/44/45/ (Nateks Unispot21)] ||
||[:OpenWrtDocs/Hardware/Siemens/CL110:Siemens CL 110] ||
||[http://zhone.com/products/6211/ Zhone 6211] ||
||[http://zhone.com/products/6212/ Zhone 6212-l2/-l3] ||
||[http://www.tp-link.com/products/product_des.asp?id=44 tp-link tp-8840] ||
=== Known 6348 platforms*: ===
||[http://www.3com.com/products/en_US/detail.jsp?tab=features&pathtype=purchase&sku=3CRWDR200A-75 3Com 3CRWDR200A-75] ||
||[http://ru.asus.com/products.aspx?l1=13&l2=96&l3=0&l4=0&model=1106&modelmenu=1 ASUS AM604] ||
||[http://ru.asus.com/products.aspx?l1=13&l2=96&l3=0&l4=0&model=1107&modelmenu=1 ASUS AM604g] ||
||[:OpenWrtDocs/Hardware/Asus/WL600g:ASUS WL-600G] ||
||[:OpenWrtDocs/Hardware/Asus/AM200g:ASUS AM200G] ||
||[:OpenWrtDocs/Hardware/Belkin/f5d7633-4:Belkin f5d7633-4] ||
||[:OpenWrtDocs/Hardware/BT/Voyager2091:BT Voyager 2091] ||
||[:OpenWrtDocs/Hardware/Comtrend/CT-5621:Comtrend CT-5621]||
||[http://www.comtrend.com/index.php?module=products&op=show&sn=2 Comtrend CT-536/1+] ||
||[http://comtrend.com/index.php?module=products&op=show&sn=41 Comtrend CT-638/1] ||
||[http://www.dynalink.co.nz/cms/index.php?page=rta1046vw Dynalink RTA1046VW] ||
||[:OpenWrtDocs/Hardware/Freebox/FreeboxV4:Freebox v4] ||
||[http://www.tecomproduct.com/AH4021.htm Hitachi AH4021 (German Telekom "Speedport W500V")] ||
||[:OpenWrtDocs/Hardware/Huawei/EchoLife HG520:Huawei EchoLife HG520] ||
||[:OpenWrtDocs/Hardware/Huawei/HG550:Huawei EchoLife HG550] ||
||[:OpenWrtDocs/Hardware/Inventel/Livebox:Inventel Livebox] ||
||[:OpenWrtDocs/Hardware/Linksys/WAG54GS:Linksys WAG54GS] ||
||[:OpenWrtDocs/Hardware/Linksys/WAG54GX2:Linksys WAG54GX2] ||
||[http://www-uk.linksys.com/servlet/Satellite?c=L_Product_C2&childpagename=UK/Layout&cid=1169671146123&pagename=Linksys/Common/VisitorWrapper&lid=4612360558B01 Linksys WAG325N] ||
||[http://www-se.linksys.com/servlet/Satellite?c=L_Product_C2&childpagename=SE/Layout&cid=1147937922090&pagename=Linksys/Common/VisitorWrapper Linksys WAG300N] ||
||[http://www.netcomm.com.au/ADSL/NB8W_new.php Netcomm NB8W] (Re-branded Comtrend CT-536) ||
||[http://www.netcomm.com.au/ADSL/NB9_new.php Netcomm NB9] (Re-branded Comtrend CT-638) ||
||[http://www.netcomm.com.au/ADSL/NB9W_new.php Netcomm NB9W] (Re-branded Comtrend CT-638) ||
||[:OpenWrtDocs/Hardware/Netgear/DG834GT:Netgear DG834GT] ||
||[http://www.netgear.co.uk/wireless_modem_router_dg834pn.php Netgear DG834PN] ||
||Pirelli Alice Gate 2+ Wi-Fi (See 6358 too) ||
||[http://www.thomson-broadband.co.uk/codepages/content3.asp?c=7&ProductID=511 Thomson Speedtouch ST585v6] ||
||[http://www.thomsonbroadbandpartner.com/dsl-modems-gateways/products/previous-product-detail.php?id=84 Thomson Speedtouch ST716(g)] ||
||[http://www.thomson-broadband.co.uk/codepages/content3.asp?c=7&ProductID=528 Thomson Speedtouch ST780(i)WL] ||
||[http://www.usr-emea.com/products/p-broadband-product.asp?prod=bb-9107&loc=unkg US Robotics USR9107] ||
||[http://www.usr-emea.com/products/p-broadband-product.asp?prod=bb-9108&loc=unkg US Robotics USR9108] ||
||[http://zhone.com/products/6218/ Zhone 6218] ||
||[http://zhone.com/products/6238/ Zhone 6238] ||
|| Sagem F@ST 2504 (commonly shipped by Sky Broadband in UK) ||
=== Known 6358 platforms*: ===
||[:OpenWrtDocs/Hardware/Buffalo/WBMR-G300N:Buffalo WBMR-G300N] ||
||[http://www.dlink.com/products/?pid=567 D-Link DSL-2640B] ||
||[http://www.dlink.co.uk/cs/Satellite?c=Product_C&childpagename=DLinkEurope-GB%2FDLProductCarousel&cid=1197319446523&p=1197318962342&packedargs=ParentPageID%3D1197318962321%26TopLevelPageProduct%3DConsumer%26locale%3D1195806691854%26packedargs%3DProductParentID%253D1195808621247&pagename=DLinkEurope-GB%2FDLWrapper D-Link DSL-2740B hw C2, C3] ||
||[:OpenWrtDocs/Hardware/Freebox/FreeboxV5:Freebox v5] ||
||[:OpenWrtDocs/Hardware/Netcomm/NB9WMAXX:Netcomm NB9WMAXX] ||
||[:OpenWrtDocs/Hardware/Netgear/DG834N:Netgear DG834N] ||
||[:OpenWrtDocs/Hardware/Neuf/NeufBox4:Neuf Box 4] ||
||[:OpenWrtDocs/Hardware/PirelliBroadbandSolutions/AliceGateVoIP2Plus:ALICE GATE VoIP 2 Plus Wi-Fi Business] ||
||[http://www.usr-emea.com/products/p-broadband-product.asp?prod=bb-9113&loc=unkg US Robotics USR9113] ||
||[http://zhone.com/products/6228/ Zhone 6228] ||
* If no dedicated Openwrt page is found an external link is supplied

== Finished tasks ==
The support for Broadcom 63xx is at this state :

 * Full linux-2.6.27 support with GPL drivers for Ethernet and USB, only DSL is binary
== TODO ==
 * Talk with Broadcom related vendors to make them release some sources
  . Pirelli Broadband Solutions relesed a GPL source code of its Alice Gate 2+ Wi-Fi at this [http://www.it.pirellibroadband.com/web/products-solutions/solutions/sme-net/gpl/default.page link] ans a group of people are adapting the USR9108 source code to better work on the same router at this [http://jackthevendicator.dlinkpedia.net/files/broadcom/pirelli_alice_gate_2_plus_wifi/src/ link]
== Firmware/Bootloader ==
Some devices use RedBoot such as Inventel Liveboxes. Other run CFE with a built-in LZMA decompressor such as Siemens SE515, Free Freebox ... CFE is not using standard LZMA compression arguments, and most noticebly, changes the dictionnary size, so beware.

= How to help =
 * Port ATM/ADSL changes to kernel 2.6.27 and use the binary DSL for now
 * Test the currently merged kernel in order to see if it boots on CFE based boards.
----
 . CategoryOpenWrtPort
----
 ["CategoryBCM63xx"]
