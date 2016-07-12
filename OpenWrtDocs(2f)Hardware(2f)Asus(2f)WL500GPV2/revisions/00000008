#pragma section-numbers off
||<tablebgcolor="#f1f1ed" tablewidth="40%" tablestyle="margin: 0pt 0pt 1em 1em; float: right; font-size: 0.9em;"style="padding: 0.5em;">[[TableOfContents]]||
== ASUS WL-500g Premium V2 ==
The redesigned version of the ASUS WL-500g Premium router, ["OpenWrtDocs/Hardware/Asus/WL500GP"] , has the following changes:

 * Broadcom BCM5354 CPU @ 240 Mhz
 * On-board wireless LAN controller
 * WLAN port and antenna port have changed sides
Support in trunk since [https://dev.openwrt.org/changeset/10693 changeset 10693].

== Hardware ==

There is an [http://www.vr-zone.com/?i=5624 article about the wl-500gPv2] with a picture.

=== Info ===
||<tablewidth="400px" tableheight="289px">'''Architecture''' ||MIPS ||
||'''Vendor''' ||Broadcom ||
||'''Bootloader''' ||CFE ||
||'''System-On-Chip''' ||Broadcom BCM5354 ||
||'''CPU Speed''' ||240 Mhz ||
||'''Flash''' ||8MiB (Macronix 29LV640DB, 64K sector size) ||
||'''RAM''' ||32MiB ||
||'''Wireless''' ||Onboard BCM5354 802.11b/g ||
||'''Ethernet Switch''' || ? ||
||'''USB''' ||2x USB 2.0 ||
||'''Serial''' ||Yes ||
||'''JTAG''' ||No ||
=== Serial Port ===
This 500g v2 has two sets of soldering points.  The first is two rows of 6 pins (JTAG perhaps).  The second, which is the serial port, is one row of four pins.  
||Pin 4 || GND ||
||Pin 3 || UART_TX ||
||Pin 2 || UART_RX ||
||Pin 1 || 3.3V ||

When examining the board carefully, one can see that pin 4 has no trace leading to it -- it is simply part of the top layer ground plane.  Pin 1 is connected to a relatively fat power trace.

These serial ports use TTL levels. You need an additional voltage convertor to get a standard serial port. The parameters are 115200 baud and 8-n-1.
