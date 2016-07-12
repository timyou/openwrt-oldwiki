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
Note : you can safely replace 100 Ohm resistors with couples of 220 Ohm connected in parallel. 220 Ohm (Red-Red-Brown) is a much more frequent     value found on electronic boards of recovery.

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

This cable is fully compatible with Macraigor [http://www.macraigor.com/ocd_cmd.htm OCD Commander]. The wire between DATA6 (pin 8 on the LPT DB-25) and ERROR (pin 15) is used to identify a presence of the Wiggler cable and requred by some JTAG software (i.e. Macraigor). It may be omitted for Hairydairymaid debrick utility.

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
This header is fully MIPS EJTAG 2.6 compatible and described in the EJTAG 2.6 standard. Found in Edimax routers (and other brands that are Edimax clones), the 14-pin header has the following arrangement of JTAG signals and pins:

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
The most famous software for JTAG is probably the Linksys De-Brick Utility by Hairydairymaid (aka Lightbulb). As of 1 April 2006 the most recent version is v4.5. You can [http://downloads.openwrt.org/utils/HairyDairyMaid_WRT54G_Debrick_Utility_v48.zip download it from the OpenWrt site]. Virtually everyone who uses this software opts for an unbuffered cable, and the software itself, by default, expects this type of cable to be used.

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
start: 0x40000000, length: 0x20000000, data width: 32 bit}}}

=== Using a Buffered Cable with the De-Brick Utility ===
Inside the zip file download for the [http://downloads.openwrt.org/utils/HairyDairyMaid_WRT54G_Debrick_Utility_v45.zip Hairydairymaid WRT54G Debrick Utility] there is a PDF file that describes the software and how to use it. He specifically talks about using an unbuffered cable and pointedly notes that the cable he uses does '''not''' tie pin 1 of the JTAG header to anything.

That's all well and good for an unbuffered cable, but if you ''do'' happen to have a buffered Wiggler-style cable then you ''will'' have to deal with the nTRST signal. The Hairydairymaid software doesn't account for that signal line since the recommended cable doesn't carry it, but your Wiggler-style cable ''does'' use that signal and the debrick utility will ''not'' work out-of-the-box with a Wiggler-style cable as a result. The reason for this is because the software leaves the output for the nTRST line at logic-level 0, which means the signal coming out of your cable to the JTAG header will always be asserted, and as a result the JTAG circuitry inside your router will forever be resetting itself.

Hairydairymaid notes in one of his files (wrt54g.h) that there are a few changes to make if you're using a Wiggler-style buffered cable, but those changes alone are not enough. In order to use a Wiggler-style cable with the debrick utility there are a couple of other changes you will need to make.

First and foremost is an external voltage supply. Vcc from the Linksys board must be brought to the Wiggler interface. Usually this means an extra jumper wire in addition to the 14-connector ribbon cable. Note that if your Wiggler cable has a 14-pin connector that pins 13 and 14 in it will not be connected to anything on the Linksys board. Pins 1 through 12 correspond properly to the signals on the 12-pin Linksys JTAG header, but positions 13 and 14 will not be connected to anything at all. On most Linksys routers there is another connector near the JTAG header that can be used to connect two serial ports to the router. This is typically a 10-pin header and, fortunately for us, pins 1 and 2 of this serial port header carry Vcc at 3.3 volts. This is perfect, and all that needs to be done is to run a jumper wire from one of those pins into your homemade Wiggler circuit at any appropriate spot where Vcc is called for. If you build your own cable from Alec's schematic then you should know where those spots are. Alternatively, you could also run a short jumper from pin 1 or 2 of the serial port header to the open hole of the ribbon cable connector at position 14. That might actually be the best choice.

Second is the software. File 'wrt54g.c' must be modified so that logic-level 1 is always output to pin 1 of the JTAG header. Alternatively you could just not connect pin 1 to anything, but then your cable wouldn't be a true Wiggler clone anymore. Ensuring that nTRST is always a '1' will prevent the JTAG circuitry on your device from being in a constant state of 'reset'.

Another change to the software is not directly related to the cable per-se. Some have observed that certain Intel flash chips are not successfully erased by the debrick utility. I believe that is because there is a time delay that must be observed after commanding a block of flash memory to be erased that is not observed by the program. I had this problem, specifically, on a WRT54GS v2.1 router with an Intel StrataFlash 28F640J3 chip. The datasheet for this chip states that it may take up to 5 seconds for an "erase block" command to complete. The software should account for this delay.

The following patch file addresses the issues outlined above. It should be applied to version 4.5 of Hairydairymaid's de-brick utility. It modified both 'wrt54g.h' and 'wrt54g.c'. The changes are not that extreme and less than 35 lines altogether are modified (or added; no lines are deleted).

'''''[NOTE by hairydairymaid - while this patch will not harm anything - it is not needed. Intel flash chips (and most others) have a built in "pin toggle" mechanism that fires when the specific write or erase has finished. Various flash chip erases/writes can and do take different times but waiting for that "pin toggle" is the proper way to account for things (not by just waiting x seconds) and it is exactly how the debrick utility operates and virtually all proper flashing routines are written. Use what works for you.]'''''

--------
attachment:debrick-wiggler.patch.gz

--------
Please note that the above gzipped patch file uses Unix-style line endings. The de-brick utility source code files use DOS-style line endings. This shouldn't be a problem but if you gunzip the patch file and open it in a DOS or Windows editor it may look strange.

== Summary ==
I was trying to revive a bricked Linksys WRT54GS one day and couldn't get Hairydairymaid's utility to work. I was on a Linux system and had other software called "jtag tools" which I obtained from the [http://openwince.sourceforge.net/jtag/ openwince JTAG site]. That program was able to detect the BCM4712 processor inside my router. The de-brick utility, however, kept telling me that my cable was bad. I knew the cable was not the problem since jtag tools was working flawlessly and a couple of days worth of investigation led me to the solution I have presented here. After I tweaked the de-brick utility source code I was able to successfully re-flash my WRT54GS router.

Personally, as an engineer, I prefer the buffered cable and would not use an unbuffered cable even though hundreds of other people have used them without any problems. A Wiggler-style cable can also be used for other devices that adhere to the JTAG specification. I'm not sure about the unbuffered type of cable. I hope this writeup will help anyone who has had trouble using a buffered JTAG cable and the Hairydairymaid software together, or who might want a cable that will almost certainly work with devices besides just Linksys routers.

== Links ==
 * [:OpenWrtDocs/Troubleshooting#head-2905e5d0dd7320ac475dd4aa53c0c4ea93ffbadd:Troubleshooting OpenWrt (JTAG Section)]
 * [http://www.linux-mips.org/wiki/JTAG EJTAG] at the Linux-MIPS wiki
 * [http://www.mips.com/content/Documentation/MIPSDocumentation/EJTAG/doclibrary EJTAG Specification] from MIPS Technologies, Inc. (free registration required)
 * [http://forum.amilda.org/viewtopic.php?id=43 Two examples] of successful Wiggler-style cable projects
 * [http://midge.vlad.org.ua/forum/viewtopic.php?t=121 Debrick example] using OpenwinCE with EJTAG driver.
 * [http://openwince.sourceforge.net/jtag/ Openwince JTAG], "Supported hardware" section for other types of the JTAG cables.
 * [http://www.k9spud.com/jtag/ K9SPUD JTAG] another Wiggler schematic
 * [http://www.ixo.de/info/usb_jtag/ USB JTAG] a budget USB JTAG adapter
 * a discussion at ["zt8qmwz"] homepage about implementing EJTAG PRAcc in the Hairydairymaid De-brick utility
 * [http://downloads.openwrt.org/utils/ HairyDairyMaid_WRT54G_Debrick_Utility]
 * [http://ar7.wikispaces.com/JTAG AR7 JTAG]
