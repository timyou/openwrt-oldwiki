= Linksys WRTP54G =
The Linksys WRTP54G and Linksys RTP300 linux-powered units are Voice-over-IP enabled routers based on the TI AR7 chipsets.

|| ||'''WRTP54G''' http://www1.linksys.com/products/image180/WRTP54G.jpg ||'''RTP300''' http://www1.linksys.com/products/image180/RTP300.jpg||
||Base Hardware||1 Ethernet uplink port, 4x 10/100MBps switch ports, 2 phone jacks|| 1 Ethernet uplink port, 4x 10/100MBps switch ports, 2 phone jacks||
||Wifi Support:||54MBps 802.11b/g|| None ||
||Linksys webpage||[http://www1.linksys.com/products/product.asp?grid=33&prid=692 Product Page] [http://www.linksys.com/servlet/Satellite?childpagename=US%2FLayout&packedargs=page%3D2%26cid%3D1115416835852%26c%3DL_Content_C1&pagename=Linksys%2FCommon%2FVisitorWrapper&SubmittedElement=Linksys%2FFormSubmit%2FProductDownloadSearch&sp_prodsku=1118334626380 Downloads]|| [http://www1.linksys.com/products/product.asp?grid=33&prid=695 Product Page] [http://www.linksys.com/servlet/Satellite?childpagename=US%2FLayout&packedargs=page%3D2%26cid%3D1115416835852%26c%3DL_Content_C1&pagename=Linksys%2FCommon%2FVisitorWrapper&SubmittedElement=Linksys%2FFormSubmit%2FProductDownloadSearch&sp_prodsku=1119460383933 Downloads]||
||CyberTAN equiv model||  [http://www.cybertan.com.tw/product/wgv614.asp WGV614] http://www.cybertan.com.tw/product/productpic/wgv614.jpg|| [http://www.cybertan.com.tw/product/brv614.asp BRV614] http://www.cybertan.com.tw/product/productpic/brv614.jpg||
||__Firmware Releases__||||||
||1.00.37:||[http://httpconfig.vonage.net/wrt-11.1.0-r016-1.00.37-r050624.img Firmware Image] [http://www1.linksys.com/support/opensourcecode/WRTP54G/1.00.37/wrtp54g_cyt_1_00_37_gpl.tgz Source Code]|| [http://httpconfig.vonage.net/rt-11.1.0-r016-1.00.37-r050624.img Firmware Image] [ftp://ftp.linksys.com/opensourcecode/rtp300/1.00.37/rtp300_cyt_1_00_37_gpl.tgz Source Code]||
||1.00.43:||[http://httpconfig.vonage.net/wrt-11.1.0-r021-1.00.43-r050816.img Firmware Image] No Source|| ||
||1.00.45:|| ||[http://httpconfig.vonage.net/rt-11.1.0-r021-1.00.45-r050823.img Firmware Image] No Source||
||1.00.55:||[http://httpconfig.vonage.net/wrt-11.1.0-r021-1.00.55-r051013.img Firmware Image] No Source||[http://httpconfig.vonage.net/rt-11.1.0-r021-1.00.55-r051013.img Firmware Image] No Source||

'''Notes'''

 * CyberTAN is a subcontractor for Linksys and their name appears in the router's source code (even the archive name: _cyt_).

 * The WRTP54G and RTP300 both run dropbear SSH and some time ago root access was gained to an RTP300 box.

 * Source code is incomplete, it's missing some of the binary files (cm_*, lib_cm, webcm) which are used in changing config settings and flashing new firmware updates.  Binaries can be found in the zip file of the FS dump below.

 * The nearly complete contents of that router's file system were extracted and stored [http://www.northern.ca/projects/openwrt/RTP300-1.0.55-fs-dump.zip here]

 * All of the entries in the ''/proc'' directory were cat-ed out to a log file found [http://www.northern.ca/projects/openwrt/rtp300-1.0.55-proc-dump.txt here]

 * A number of the common montavista router linux tools are found (cm_logic, webcm, etc) on these routers... the following page describles some very interesting hacking techniques that likely also apply to the WRTP54G / RTP300: http://sub.st/index.php?page=hacking_actiontec

See also:
[:AR7Port]

= Pinouts =
== WRTP54G Serial Console ==

{{{________________________________________
|                                         |
|                                         led
|                   Pin 1: GND   ---> @   |
|                                         led
|         Pin 2: Not Connected   ---> @   |
|                                         led
|                   Pin 3: RX   ----> @   |                 Front of WRTP54G
|                                         led
|                   Pin 4: TX   ----> @   |
|                                         |
|                   Pin 5: VCC  ----> @   led
|                                         |
|                                         |
|                                         |
 \________________________________________|
}}}
The WRTP54G is *almost* a photo replica of the wag54gv2 hence the fccid of wag54gv2m.  The board layout differs slightly, although enough that the serial and jtag headers are positioned parallel to the front of the unit as opposed to the perpendicular alignment on the wag54gv2

== WRTP54G JTAG Pinout ==

{{{
__________________________________________
|                     J3                  |
|                                         led
| Pin 1: TRST  ----> @   @ <-- Pin 2:GND  |
|                                         led
| Pin 3: TDI   ----> @   @ <-- Pin 4:GND  |
|                                         led
| Pin 5: TDO   ----> @   @ <-- Pin 6:GND  |
|                                         led
| Pin 7: TMS   ----> @   @ <-- Pin 8:GND  |   Front of WRTP54G
|                                         |
| Pin 9: TCK   ----> @   @ <-- Pin 10:GND led
|                                         |
| Pin 11:RST   ----> @   @ <-- Pin 12:NC  |
|                                         |
| Pin 13:DINT  ----> @   @ <-- Pin 14:VIO*|
 \________________________________________|

    *voltage reference @ 3.3 volts
}}}

The AR7 is based on ejtag version 2.6.

This ejtag layout should support all ar7 based boards with a 14 pin jtag pinout.  The same cable as used for the standard wrt54g (based on the xilinx III/dlc-5) as demonstrated by !HairyDairyMaid can be constructed and is well documented.  Debug INT pin 13 is optional and pin 14 can be left unhooked for passive cabling.

Since DMA Routines do '''not''' exist for this ejtag version (compared to ejtag v2.0 supported on the wrt54g) interfacing requires a rewrite utilizng prAcc routines of the v2.6 standard.

[http://www.dlinkpedia.net/index.php/Jtag_su_30xT JTAG for a similar AR7 device], [http://www.dlinkpedia.net/index.php/Interfaccia_JTAG JTAGInterface] (Italian!)

----
CategoryModel ["CategoryAR7Device"]
