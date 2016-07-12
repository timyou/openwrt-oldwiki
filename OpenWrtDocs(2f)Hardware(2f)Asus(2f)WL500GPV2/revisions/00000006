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
||'''Flash size''' ||8MiB (Macronix 29LV640DB, 64K sector size) ||
||'''RAM''' ||32MiB ||
||'''Wireless''' ||Onboard BCM5354 802.11b/g ||
||'''Ethernet Switch''' || ? ||
||'''USB''' ||2x USB 2.0 ||
||'''Serial''' ||Yes ||
||'''JTAG''' ||No ||
=== Serial Port ===
Serial is located on pin soldering points (ready for soldering of 8-pin connector for use with detachable cable) on the center of the right upper side (viewing from front panel) above the ASUS label.
||RESET ||(unused) ||
||GND ||3.3V_OUT ||
||UART_TX1 ||UART_TX0 ||
||UART_RX1 ||UART_RX0 ||


Pin 1 (with the square solder pad) is RX0.

These serial ports use TTL levels. You need an additional voltage convertor to get a standard serial port. The parameters are 115200 baud and 8-n-1.
