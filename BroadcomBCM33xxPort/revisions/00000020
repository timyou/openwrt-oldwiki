[[TableOfContents]]

This page covers the BCM33xx SoC specificities, but the BCM63xx SoC are mostly the same chip, except that the DOCSIS/EuroDOCSIS core is replaced with a DSL one.

= Status of the Broadcom 33xx port of OpenWrt =
 * The Broadcom BCM33xx currently only begins booting with the SB4xxx cable modems
 * We have no GPL'd drivers for Ethernet or DOCSIS so this makes the board pretty useless

== What is this Broadcom 33xx stuff? ==
[http://www.broadcom.com/products/Cable/Cable-Modem-Solutions/BCM3349 Broadcom33xx SoC] integrates DOCSIS/EuroDOCSIS features and routing.

== What are 33xx variants? ==
There are many 33xx variants. Only those with a TLB will be supported:
||Chip ||CPU Mhz ||USB Device ||VoIP ||WiFi ||DOCSIS ||TLB ||Product ID ||-march ||Surfboard ||
||[http://www.datasheetcatalog.org/datasheets2/13/131978_1.pdf bcm3300] ||  n/a ||- ||- ||- ||1.0/1.1 ||- ||- ||- ||3100 ||
||bcm3302 || ? || ? || ? || ? || - || ? || ? || ? || ||
||[http://www.datasheetcatalog.org/datasheets2/15/155898_1.pdf bcm3345] ||  140 ||1.1 ||- ||- ||1.0/1.1 ||Yes? ||0x28000 ||mips32? ||4200 ||
||[http://www.datasheetcatalog.org/datasheets/166/404171_DS.pdf bcm3348] ||  200 ||1.1 ||- ||- ||1.0/1.1/2.0 ||Yes? ||      ? ||mips32? ||5100 ||
||[http://www.broadcom.com/collateral/pb/3349-PB03-R.pdf bcm3349] ||  200 ||1.1 ||- ||EBI/PCMCIA ||1.0/1.1/2.0 ||Yes? ||      ? ||mips32? ||5101 ||
||[http://www.datasheetcatalog.org/datasheets/134/404172_DS.pdf bcm3350] ||  100 ||1.1 ||- ||- ||1.0/1.1 || No  ||0x28000 ||mips32? ||4100 ||
||[http://www.broadcom.com/collateral/pb/3368-PB202-R.pdf bcm3368] ||  300 ||1.1 ||2 lines ||Expansion Bus ||2.0 ||Yes? ||      ? ||mips32? ||- ||

=== bcm3300 ===
This chip does not include a CPU itself.

Known platforms:
 * 3Com HomeConnect Cable Modem
 * Aastra PipeRider HM200
 * Ambit 60098E/U
 * Arris CM200[U]
 * Askey CME03x
 * Cisco uBR924
 * Com21 DOXport 1010
 * E-Tech ICE 200
 * E-Tech ITCM
 * GVC USB Cable Modem
 * Motorola SURFboard 3100A/B
 * Samsung InfoRanger ITCM/SCM-110R
 * Thomson RCA DCM 205/215/225
 * Zyxel Prestige 941

=== bcm3302 ===
This chip seems to be a general-purpose MIPS CPU. It is usually included with other platforms like bcm47xx and such.

=== bcm3345 ===
Known platforms:
 * [:OpenWrtDocs/Hardware/Motorola/SB4200:Motorola SURFboard 4200]
 * Hitron BRG-3520

http://www.datasheetcatalog.org/datasheets2/15/155898_1.pdf

Used in the [:OpenWrtDocs/Hardware/Motorola/SB4200:SB4200] cable modem

=== bcm3348 ===
Known platforms:
 * [:OpenWrtDocs/Hardware/Motorola/SB5100:Motorola SURFboard 5100]
 * [:OpenWrtDocs/Hardware/Motorola/SBG900E:Motorola SBG900E]
 * Scientific-Atlanta WebStar DPX-2100
 * [:OpenWrtDocs/Hardware/Thomson/TCM390:Thomson TCM390]

=== bcm3349 ===
Known platforms:
 * [:OpenWrtDocs/Hardware/Motorola/SB5101:Motorola SURFboard 5101]
 * [:OpenWrtDocs/Hardware/Scientific-Atlanta/DPC2100:Scientific-Atlanta WebStar DPC2100]

=== bcm3350 ===
Known platforms:
 * [:OpenWrtDocs/Hardware/Motorola/SB4100:Motorola SURFboard 4000/410x]
 * Ambit 60218P
 * Ambit 60194E
 * Askey CME063
 * Com21 DOXport 1110
 * Hitron BRG-3510
 * Icable ICS-110
 * Linksys BEFCMUH4/BEFCMU10
 * Thomson RCA DCM 235/305
 * [:OpenWrtDocs/Hardware/USRobotics/USR6000:USRobotics USR6000]

MIPS R3000 CPU '''without a TLB''' (random register always reads a 0)

Note: Ralf says this is just mostly R3000-*compatible*, so -march=mips32 is safer.

http://www.datasheetcatalog.org/datasheets/134/404172_DS.pdf

read_c0_prid() => 0x28000

NS16550 serial UART

i82559 Ethernet

Used in the [:OpenWrtDocs/Hardware/Motorola/SB4100:SB4100] cable modem

=== bcm3368 ===
Known platforms:
 * [:OpenWrtDocs/Hardware/Netgear/CVG834G:Netgear CVG834G]
 * Scientific-Atlanta WebStar DPX 2203

== Finished tasks ==
The support for Broadcom 33xx is at this state :

 * Linux 2.6.x booting before failing to find init on bcm3348 (SB4200)
 * Linux 2.6.x booting to BusyBox shell on bcm3349 (WebSTAR DPC2100)
== TODO ==
 * Talk with Broadcom related vendors to make them release some sources
    The Netgear CVG834G uses a bcm33xx chip and has GPL'd eCos. Netgear modified the Atlas driver in eCos to add the bcm3350.

== Firmware/Bootloader ==
Surfboard modems use a VxWorks bootloader.

----
 . CategoryOpenWrtPort
