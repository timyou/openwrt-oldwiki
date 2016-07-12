The Motorola '''SBG900E''' is cable modem based on Broadcom BCM3348 chip. The core chip has no wireless capabilities but MiniPCI card is used to provide b/g WLAN. Ethernet and USB ports are provided. The modem is compatible with DOCSIS and EuroDOCSIS standards. 

The '''E''' stands perhaps for '''Europe''' but that just a guess.

= Hardware =

 * Main Chip: [http://web.archive.org/web/20030627094926/www.broadcom.com/pbs/3348-PB02-403-RDS.pdf Broadcom QAMLink® BCM3348KPB]
 * Ram: 32 MB SDRAM ([http://web.archive.org/web/20051112090141/www.winbond.com/e-winbondhtm/partner/PDFresult.asp?Pname=1050 Winbond W982516CH-75, 4M x 4 banks x 16bit]) 
 * Flash: Intel (under a over-soldered metal cage)
 * B/G WLAN MiniPCI card (on back-side, under a soldered metal cage) with internal and external (non-removable) antennas

== Connectors ==

On back-side, in top-down order:

 * Reset button
 * RJ45
 * USB v1.1
 * Cable
 * 12 VDC

In addition, there seems to be RJ11 reservation and a place for a chip that is pin compatible with MAX232 chip.

== Leds ==

In front panel. Green, unless otherwise stated. In top-down order:

 * Power
 * Receive
 * Send
 * Online
 * PC/Activity
 * Wireless (Orange led)

= Accessing SBG900E =

== Opening the Case ==

Just one torx in the upper corner of the back (near the antenna). Two clips in the bottom under an adhesive label. In addition, the labeling of the LEDS is adhesively attached. You may either cut the adhesives or remove them (I used the latter alternative). 

== Ethernet Access ==

Standard firmware provides configuration interface using HTTP. Currently, there exists no known way to break into the device/OS through it.

== Serial Access ==

Provides serial connector J9, which is clearly marked:

||<:25%> 3.3v ||<:25%> GND ||<:25%> SIN ||<:25%> SOUT ||
||<:> O ||<:> O ||<:> O ||<:> O ||

Serial is not yet tested.

== JTAG Access ==

Provides a JTAG connector in J3, which seems to follow similar semantics as [:OpenWrtDocs/Hardware/Thomson/TCM390:TCM390] (only 10 pins like it). The mainboard connects resistors to pins 1,3,7,9 and 2,4,6,8,10 to GND as expected. Pin 5 wiring is unique and goes under metal cage under which the MiniPCI card resides. The cage is soldered in place.

http://lauterbach.com/admips3.gif

JTAG is not yet tested.

== Unknown Stuff ==

 * 1x6 connector J2 very close to the main chip. Purpose unknown...
 * Can the RJ11 + MAX232 pin-compatible chip reservation be used for some purpose...
