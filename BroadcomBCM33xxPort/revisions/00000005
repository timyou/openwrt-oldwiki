[[TableOfContents]]

This page covers the BCM33xx SoC specificities, but the BCM63xx SoC are mostly the same chip, except that the DOCSIS/EuroDOCSIS core is replaced with a DSL one.

= Status of the Broadcom 33xx port of OpenWrt =
 * The Broadcom BCM33xx currently only begins booting with the SB4100 cable modem
 * We have no GPL'd drivers for Ethernet or DOCSIS so this makes the board pretty useless

== What is this Broadcom 33xx stuff? ==
[http://www.broadcom.com/products/Cable/Cable-Modem-Solutions/BCM3349 Broadcom33xx SoC] integrates DOCSIS/EuroDOCSIS features and routing.

== What are 33xx variants? ==
There are many 33xx variants. Only those with a TLB will be supported:
||Chip ||CPU Mhz ||USB Device ||USB Host ||WiFi ||DOCSIS ||TLB ||Surfboard ||Product ID ||-march ||
||[http://www.datasheetcatalog.org/datasheets2/15/155898_1.pdf bcm3345] ||  140 ||1.1 ||- ||- ||1.0/1.1 ||Yes? ||[:OpenWrtDocs/Hardware/Motorola/SB4200:SB4200] ||      ? ||mips32? ||
||[http://www.datasheetcatalog.org/datasheets/166/404171_DS.pdf bcm3348] ||  200 ||1.1 ||- ||- ||1.1/2.0 ||Yes? ||[:OpenWrtDocs/Hardware/Motorola/SB5100:SB5100] ||      ? ||mips32? ||
||[http://www.datasheetcatalog.org/datasheets/134/404172_DS.pdf bcm3350] ||  100 ||1.1 ||- ||- ||1.0/1.1 || No  ||[:OpenWrtDocs/Hardware/Motorola/SB4100:SB4100] ||0x28000 ||mips32? ||

=== bcm3350 ===

MIPS R3000 CPU '''without a TLB''' (random register always reads a 0)

Note: Ralf says this is just mostly R3000-*compatible*, so -march=mips32 is safer.

http://www.datasheetcatalog.org/datasheets/134/404172_DS.pdf

read_c0_prid() => 0x28000

NS16550 serial UART

i82559 Ethernet

Used in the [:OpenWrtDocs/Hardware/Motorola/SB4100:SB4100] cable modem

=== bcm3345 ===

http://www.datasheetcatalog.org/datasheets2/15/155898_1.pdf

Used in the [:OpenWrtDocs/Hardware/Motorola/SB4200:SB4200] cable modem

== Finished tasks ==
The support for Broadcom 33xx is at this state :

 * Linux 2.6.x loading
== TODO ==
 * Linux 2.6.x booting on bcm3345
 * Talk with Broadcom related vendors to make them release some sources
    The Netgear CVG834G uses a bcm33xx chip and has GPL'd eCos. Netgear modified the Atlas driver in eCos to add the bcm3350.

== Firmware/Bootloader ==
Surfboard modems use a VxWorks bootloader.

----
 . CategoryOpenWrtPort
