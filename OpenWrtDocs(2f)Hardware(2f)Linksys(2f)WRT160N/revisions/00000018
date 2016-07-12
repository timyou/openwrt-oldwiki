#pragma section-numbers off
||<tablebgcolor="#f1f1ed" tablewidth="40%" tablestyle="FONT-SIZE: 0.9em; FLOAT: right; MARGIN: 0pt 0pt 1em 1em"style="PADDING-RIGHT: 0.5em; PADDING-LEFT: 0.5em; PADDING-BOTTOM: 0.5em; PADDING-TOP: 0.5em">[[TableOfContents]]||

= Linksys WRT160N =

== Notes ==

There is NO known OpenWrt firmware that supports this device. Support is possible one day though because DD-WRT supports it as of v24 rc 7 - build 9344 (25.03.08). 
Please Update this wiki page if this information is proven false or a port is created.
Link to Product info page at linksys.com -> [http://www.linksys.com/servlet/Satellite?c=L_Product_C2&childpagename=US%2FLayout&cid=1175239516849&pagename=Linksys%2FCommon%2FVisitorWrapper WRT160N Product_Page]

The Linksys WRT160N is the Ultra Range Plus Wireless-N Broadband Router.

== Hardware ==

== Info ==
||<tablestyle="FLOAT: right; margin: -15px 0 0 0; padding: 0;">attachment:wrt160N_CPU_systeminfo_.jpg||

||'''Architecture''' ||MIPS ||
||'''Vendor''' ||Broadcom ||
||'''Bootloader''' ||CFE ||
||'''CPU Speed''' ||266 Mhz ||
||'''Flash size''' ||4 MiB ||
||'''RAM''' ||16 MiB ||
||'''Wireless''' ||Broadcom BCM47xx 802.11b/g/n Wireless LAN (integrated) ||
||'''Ethernet''' ||Switch in CPU ||
||'''USB''' ||No ||

=== Chipset ===

 * BCM4703 [http://www.broadcom.com/collateral/pb/4703_4704-PB00-R.pdf Product_Brief]
 * BCM4321 [http://www.broadcom.com/collateral/pb/4321_2055-PB02-R.pdf Product_Brief]
 * BCM5325 [http://www.broadcom.com/collateral/pb/5325-PB05-R.pdf Product_Brief]

=== Flashchip ===

 * EN29LV320AB [http://www.eonsdi.com/pdf/EN29LV320.pdf Data Sheet]

=== Wireless Chip ===

 * BCM2055 (under the shield) [http://www.broadcom.com/collateral/pb/4321_2055-PB02-R.pdf Product_Brief]

=== Pads on PCB ===

There is 3 sets of pads on the PCB of the WRT160N.

JP1 and JP3 seem to be missing some surface mount components so may not actually work. 
Half of the JP1 and JP3 pads are on the reverse side of the PCB.

JP2 works if you use a 3.3v TTL to RS-232.

'''JP1'''
|| On Reverse ||'''Pad 2''' ||GND ||'''Pad 4''' ||GND ||'''Pad 6''' ||GND ||'''Pad 8''' ||GND ||'''Pad 10''' ||GND ||'''Pad 11''' || ? ||
|| On Front ||'''Pad 1''' || ? ||'''Pad 3''' || ? ||'''Pad 5''' || ? ||'''Pad 7''' || ? ||'''Pad 9''' || ? ||'''Pad 12''' || ? ||

'''JP2'''

3.3v TTL Serial
|| On Front ||'''Pad 1''' || 3.3v ||'''Pad 2''' || TX ||'''Pad 3''' || RX ||'''Pad 4''' || Not Connected ||'''Pad 5''' || GND ||

'''JP3'''
|| On Reverse ||'''Pad 2''' ||GND ||'''Pad 4''' ||GND ||'''Pad 6''' ||GND ||'''Pad 8''' ||GND ||'''Pad 10''' ||GND ||'''Pad 11''' || ? ||
|| On Front ||'''Pad 1''' || ? ||'''Pad 3''' || ? ||'''Pad 5''' || ? ||'''Pad 7''' || ? ||'''Pad 9''' || ? ||'''Pad 12''' || ? ||

=== JTAG Port ===

Not yet documented.

=== Serial Ports ===

JP2 is a 3.3v serial port.  Boot messages can be seen if you connect a 3.3v level shifter here and monitor with a serial port. 

DO NOT CONNECT DIRECTLY TO A PC SERIAL PORT. Use a 3.3v TTL level shifter. 
Details at this page:
 * http://wiki.openwrt.org/OpenWrtDocs/Customizing/Hardware/Serial_Console

=== Boot Messages ===

Boot messages are [http://wiki.openwrt.org/OpenWrtDocs/Hardware/Linksys/WRT160N/BootMessages here]

== TODO ==

 * Find the data sheets for the chips used in this device.
 * Figure out what JP1, JP3 are for and the exact pinouts.

== Other Categories this device is in ==

 . Category80211nDevice
 . CategoryNotSupported
