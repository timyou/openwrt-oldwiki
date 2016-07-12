#pragma section-numbers off
#pragma keywords JTAG, Linksys, debrick, de-brick, Hairydairymaid
#pragma description This page talks about different types of JTAG cables.
= JTAG Cables =
This page discusses two popular types of [wiki:WikiPedia:jtag JTAG] cables and provides a few tips on how to use a buffered Wiggler-type cable with Hairydairymaid's debrick utility.

== Several Types of Cables ==
There are several different types of cables that are popular for hooking up to JTAG headers inside consumer electronic equipment. Most of these rely on a regular PC's parallel port to drive the JTAG signal lines. There are vendors of commercial JTAG cables that sell them at extravagent prices. For the home user or hobbyist, however, a better choice is usually to construct a cable at home from commonly available parts.

For SOHO routers and other network devices there are two popular cables: the buffered Wiggler-type cable and the unbuffered-type cable. The single largest segment of homemade JTAG cable users is probably satellite television receiver owners. A search on ebay for JTAG will turn up many people selling JTAG cables for use with satellite TV receivers. The JTAG interface is pretty much standardized but the difference in pinouts for different equipment can vary widely. The cables for sale on ebay could probably be easily made to work with SOHO routers, and vice versa, but this page will not cover them. I've never bought or used one so I don't know exactly how they are constructed.

There are other types of JTAG cables as well. Macraigor sells the Raven cable which is even more expensive than the Wiggler. Lately there are also cables that use a USB interface on the PC side instead of the 25-pin parallel port connector. I have not had any experience with these. There are still other JTAG solutions out there that are faster and more sophisticated than the interfaces built by hobbyists, but these are generally not cost-effective for someone who just wants to re-flash a single flash chip. A complete JTAG test rig is used in industry for much more than programming flash chips. Some of these industrial-strength setups can cost thousands and thousands of dollars.

Driving a JTAG interface through the parallel port on a PC is a slow proposition. ''Really'' slow. This is due more to the nature of the parallel port connection than an inherent limit of the JTAG specification. In fact, the JTAG spec allows for up to 25 milliion bits-per-second transfers. With a parallel port cable, however, you will be lucky to achieve more than about 400,000 bits-per-second. With these speeds it is not unusual to spend 25 minutes writing a mere 256 KB of data over a JTAG cable. Programming an entire 2 MB or 4 MB flash chip can literally take hours. It's worth it, however, if you have an otherwise worthless device on your hands and JTAG is the only way to revive it. The Macraigor Raven and USB JTAG adaptors are much faster, but there are no known schematic to implement it.

There are a many varians of the LPT-to-JTAG cables. All of them are different in the LPT pins -to- JTAG pins mapping and may be in the buffered and unbuffered variant.

=== Unbuffered Cable, Xilinx DLC5 Cable III ===
This is the simplest type of JTAG cable, the easiest to construct and the cheapest to make. The original cable was introduced by Xilinx and has a full name "[http://toolbox.xilinx.com/docsan/3_1i/pdf/docs/jtg/jtg.pdf Xilinx DLC5 JTAG Parallel Cable III]". Someone removed a buffer and changed it with a four 100 Ohm resistor. Popularized by the Hairydairymaid de-brick utility software for Linksys routers, many people have successfully built their own unbuffered JTAG cable. It consists of only a few cheap resistors, a 25-pin parallel port connector and a ribbon-cable with a 12-pin connector that slides onto a header soldered onto the PCB found inside the cases of Linksys WRT54G and WRT54GS routers. The chief limitation of this type of cable is that it must be very short; the length must be 6 inches or less (15 cm) to avoid problems with electrical noise.

attachment:JTAGunbuffered.png

JTAG-to-LPT mapping

{{{
 TDI  -  DATA0   - pin 2
 TDO  -  SELECT  - pin 13
 TMS  -  DATA2   - pin 4
 TCK  -  DATA1   - pin 3}}}

The Linksys WRT54G and WRT54GS routers are based on Broadcom CPUs which are a type of MIPS32 processor. Broadcom has implemented EJTAG version 2.0 in their chips. This allows the use of DMA transfers via JTAG which, while slow, is faster than the implementation of EJTAG v2.5 and v2.6 which do not support DMA transfers.

=== Buffered Cable, Wiggler ===
This type of cable is a bit more complicated than the unbuffered one, although it is also fairly easy to construct. The cable most often used in this category is the so-called Wiggler cable. The Wiggler is a commercial cable sold by [http://www.macraigor.com/wiggler.htm Macraigor Systems]. With a list price of $150 USD they are not cheap. There is a schematic on the internet that is commonly accepted to be the equivalent of what's inside a Wiggler cable. This schematic, by [http://www.sensi.org/~alec/ Alec], was drawn up for devicves that implement a typical EJTAG header in devices based on the ADM5120 System-on-Chip, another design based on the MIPS32 architecture. The ADM5120 has support for EJTAG v2.6, which does ''not'' support DMA transfers.

attachment:wiggler.png

JTAG-to-LPT mapping

{{{
 TDI   - DATA3   - pin 5
 TDO   - BUSY    - pin 11
 TMS   - DATA1   - pin 3
 TCK   - DATA2   - pin 4
 nSRST - DATA0   - pin 2
 nTRST - DATA4   - pin 6}}}

Whereas an unbuffered cable can be constructed for maybe $5 USD or less, the parts for a Wiggler-type cable will cost a little more, perhaps in the $15 to $30 USD range. The advantage of a buffered cable is that it is not as constrained as to length and is more immune to noise and static, thus permitting a higher data transfer rate.

This cable is filly compatible with Macraigor [http://www.macraigor.com/ocd_cmd.htm OCD Commander]. The wire between DATA6 (pin 8 on the LPT DB-25) and ERROR (pin 15) is used to identify a presence of the Wiggler cable and requred by some JTAG software (i.e. Macraigor). It may be omitted for Hairydairymaid debrick utility.

Another consideration is that a buffered Wiggler-style cable '''requires''' a voltage source to operate. Usually +3.3 volts is needed and is commonly referred to as Vcc (voltage common-collector is the traditional meaning of Vcc). The buffer IC may take a Vcc from the PC LPT also. The DATA7 pin may be used for this purposes, so Wiggler software should provide aclive "1" at this pin. Do not use this pin if your JTAG header provides Vcc.

== Headers ==
There are two major JTAG header arrangements used in SOHO routers based on MIPS CPUs. One uses 12 pins and the other uses 14 pins. While not radically different, you should be familiar with both.

=== 12 Pin Header ===
Found in Linksys routers such as the WRT54G and WRT54GS, the 12-pin header has the following arrangement of JTAG signals and pins:

{{{
 nTRST  1   2 GND
 TDI    3   4 GND
 TDO    5   6 GND
 TMS    7   8 GND
 TCK    9  10 GND
 nSRST 11  12 GND}}}

Seems, this header is a truncated version of the full EJTAG header.

=== 14 Pin Header ===
This header is fully MIPS EJTAG 2.6 compatible and described in the EJTAG 2.6 standart. Found in Edimax routers (and other brands that are Edimax clones), the 14-pin header has the following arrangement of JTAG signals and pins:

{{{
 nTRST  1   2 GND
 TDI    3   4 GND
 TDO    5   6 GND
 TMS    7   8 GND
 TCK    9  10 GND
 nSRST 11  12 n/a
   n/a 13  14 Vcc}}}

A buffered cable such as the Wiggler requires an external Vcc voltage supply. The 14-pin header conveniently supplies this voltage on pin 14. The typical unbuffered cable, however, does not require an external voltage in order to function. Formally, the pin 14 is called VREF and used to indicate a JTAG signal levels: 5V, 3.3V or 2.5V. On the most devices this pin is tied to the device's Vcc and may be used to power a buffer IC chip (and to generate an appropriate levels as result). Note that the 12-pin JTAG header arrangement does not provide Vcc.

== Software ==
The most famous software for JTAG is probably the Linksys De-Brick Utility by Hairydairymaid (aka Lightbulb). As of 1 April 2006 the most recent version is v4.5. You can [http://downloads.openwrt.org/utils/HairyDairyMaid_WRT54G_Debrick_Utility_v45.zip download it from the OpenWrt site]. Virtually everyone who uses this software opts for an unbuffered cable, and the software itself, by default, expects this type of cable to be used.

The Hairydairymaid de-brick utility is mainly with Linksys WRT54G and WRT54GS routers. It will ''not'' help you de-brick other routers that are not based on Broadcom CPUs (e.g. Edimax and its clones).

'''''[Edit by hairydairymaid - the v4.5 debrick utility WILL and CAN operate on most any MIPS based cpu supporting EJTAG by using PrAcc routines (non-dma mode) - use the /nodma switch. It is not limited to WRT54G/GS units.] '''''

Another popular JTAG utility is a [http://openwince.sourceforge.net/jtag/ Openwince JTAG]. Unfortunately, the development is stalled, but you can use a CVS snapshot fork with EJTAG driver implemented by Marek Michalkiewicz : [http://www.amelek.gda.pl/rtl8181/jtag/ jtag-0.6-cvs-20051228]. One more snapshot with corrected Flash block mapping may be found there: http://star.oai.pp.ru/jtag/jtag-brecis-ok.zip. To access a Flash chip in 8-, 16- or 32-bit mode via EJTAG, use 0x1fc00000, 0x3fc00000 and 0x5fc00000 addresses respectively.

{{{
jtag> print 
No. Manufacturer Part Stepping Instruction Register
---------------------------------------------------------------------------------------------
0 Lexra LX5280 1 BYPASS BR

Active bus:
*0: EJTAG compatible bus driver via PrAcc (JTAG part No. 0)
start: 0x00000000, length: 0x20000000, data width: 8 bit
start: 0x20000000, length: 0x20000000, data width: 16 bit
start: 0x40000000, length: 0x20000000, data width%3
