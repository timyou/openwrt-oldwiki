[[TableOfContents]]

= Linksys WAG354G v1 =
The Linksys WAG354G is an ADSL gateway with wireless  acccess point integrated.

== Specifications ==
ADSL2/2+ support up to 24Mbit/s+

4 port switch

Wireless 802.11b/g

The unit comes with an internal antenna. It's possible to add an external antenna via the R-SMA plug.

=== Hardware ===
Platform: ''TI AR7WRD''

SoC: ''TNETD7300AGDW''

Processor: ''MIPS 4KEc V4.8'' @ 150 MHz

4 port switch: ''Infineon ADM6996L''

Wireless chipset: ''TI TNETW1130''

Expansions: '''minipci slot''' for wireless card (maybe can be used for other cards?)

Internal:

[http://www.hughe.co.uk/pub/pics/tech/openwrt/WAG354G_big.jpg Big size]

attachment:WAG354G_small.jpg

----
 . '''Serial console'''
Serial console can be plugged to JP5: connector lacks, it has to be soldered on the board.

Pinout:

{{{
                  JP5_______
  |               [1]  [2]  [3]  [4]  [5]
  |
  |
  |___ _ ___|-|____|-|__leds___|-|_|-|_|-|_|-|___ _ _ _
Legend:
1  GND
2  NC
3  Rx
4  Tx
5  Vcc
}}}
[http://wiki.openwrt.org/OpenWrtDocs/Hardware/Linksys/WAG354G?action=AttachFile&do=get&target=serial-wag354G.png Serial Console Schematic]

Configure teminal with 38400 bauds, 8 bits, no parity, 1 stop bit (38400 8N1)

----
 . '''JTAG'''
Jtag pins are located in JP1, but the connector lacks. The pinout should be the same of others AR7 devices.

to be written (& tested)...

----
 . '''Gpio'''
One gpio for the reset button. One gpio for switching between internal/external antenna.

to be written (& tested)...

----
 . '''Mods'''
Possible mods:

 * Replace wireless card with one more supported, e.g. with atheros chipset.
 * Replace wireless card with a [http://www.neutronexpress.com/prod.cfm/374905/AAEON_SYSTEMS/PER-C20U-A10/MINI_PCI_4_PORT_USB_2.0_MODULE_WITH_NEC minipci usb module]
 * Add an SD card reader.
to be written (& tested)...

-----

=== Software ===
'''Bootloader'''

["PSPBoot"] 1.2 rev: 0.22.17

'''Code Patterns'''

''WA31'' for Annex A (ADSL over POTS) devices.

''WA32'' for Annex B devices.

----
 . '''Flash layout'''
{{{
0x900e0000,0x903d0000 fs (mtd0)
0x90020000,0x903d0000 kernel (mtd1)  (The end address is the same as fs...)
0x90000000,0x90020000 Bootloader (mtd2)
0x903d0000,0x903f0000 Lang partition (mtd4)
0x903f0000,0x90400000 NVRAM (mtd3)
_____________________________________
TOTAL = 4096K = 4M
}}}
----------

== Running OpenWRT ==
The target platform to select for building the firmware is AR7. At now openwrt comes with a 2.4 and a 2.6 kernel, and both of theme works. However I suggest you the latest 2.6 kernel, because it has more recent ADSL drivers that support ADSL2+, and a preliminary support for the wireless card, using the open soure drivers by the [http://acx100.sourceforge.net/ ACX100 project] . The configuration that follows applies only to the 2.6 version.

=== Network Configuration ===
All the network interfaces can be configured via the /etc/config/network file.

'''eth0 (ethernet) interface'''

 * Static IP
 * DHCP
'''ppp0 (adsl) interface'''

 * PPPoA
'''
''' * PPPoE
'''
'''

'''wlan0 (wifi) interface'''

 * Master (Access point)
'''
''' * Client mode
'''
'''
=== Old notes ===
'''WARNING''' This page is a work in progress.  So far I (IanJackson) am just collecting information found in various other places (eg, IRC logs) together.

Known problems:

* `Crashes occasionally' for some people or with some devices.  Currently not known whether this is a hardware problem.

* Using the tftp procedure to upload an openwrt image seems for some people to disable the tftp facility in PSPBoot, so that future upgrades have to be done from within openwrt.  However this didn't happen to me -IanJackson.

----
 . ["CategoryAR7Device"]
