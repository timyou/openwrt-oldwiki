## Please add only OpenWrt and WAP54G related things to this page! Thanks.
'''Linksys WAP54G'''

This device is intended as an ACCESS POINT by manufacturer (one ethernet interface, smaller flash and RAM than WRT54G). Running OpenWrt is possible in limited form only.

See the Seattle Wireless page: SeattleWireless:WAP54G. Also see ["WAP54GHowto"].

[[TableOfContents]]

=== Hardware versions ===
===== Identification by S/N =====
Useful for identifying shrinkwrapped units. The '''S/N''' can be found on the bottom side of the box.
||||<style="text-align: center;"> (!) '''Please contribute to this list.''' (!) ||||<style="text-align: center;">'''!OpenWrt''' ||
||'''Model''' ||'''S/N''' ||'''Stable[[BR]]White Russian''' ||'''Development[[BR]]Kamikaze''' ||
||WAP54G v1.0 ||MDG0 ||WiP [[BR]] No working official image yet! [[BR]] RC5 with default nvram bricks the device! [[BR]] Do NOT flash until you have serial console! [[BR]] See instructions to see if you can install. ||WiP [[BR]] No working official image yet! [[BR]] Do NOT flash until you have serial console! [[BR]] See instructions to see if you can install. ||
||WAP54G v1.1 ||MDG1 ||? ||? ||
||WAP54G v2 ||MDG2 ||RC5 micro image works with default nvram. ||WiP ||
||WAP54G v3 ||MDG3 ||WiP ||WiP ||


==== WAP54G v1.0 ====
The label on the bottom reads just "Model No WAP54G", version 1.0 is not marked.

The WAP54G v1.0 is based on the Broadcom 4710 board. It has a 125 MHz CPU, 2 MB flash and 8 MB SDRAM. The wireless NIC is a mini-PCI card. There are 7 status leds on the front panel. The reset button is next to the ethernet connector (left side of the ethernet connector).

There are confirmed other revisions of v1.0 box with 4MB flash but how to reconnize them??? If there is a [http://www.spansion.com/products/Am29LV160D.html AM29LV160DB] chip, then you have 2MB flash only.

No UART on the board. To get serial console you have connect UART to 20 pin header or solder it on board. More info on SeattleWireless:WAP54G

There is no JTAG header.

To take the front cover off of this unit you must first remove the small screws under the rubber covers of the front feet!

Version 1.0 is really special edition: full of bugs, easy to brick, hard to unbrick. Better stay away. If you insist, read carefully ["OpenWrtDocs/Hardware/Linksys/WAP54Gv10"] and ["WAP54GHowto"].

But if you understand what you are doing and not just follow point by point instructions, it is highly possible to succeed. Read everything from the wiki pages and documentation, make your strategy and you will not regret.

==== WAP54G v1.1 ====
 * No version number on the bottom sticker.
 * Serial number starts with MDG1.
 * A couple of nvram variables differ from v1.0
 * Mini-pci
 * 3 lights: power, act, link
 * Reset left of ethernet and closer to ethernet than antenna when looking at the rear.

==== WAP54G v2.0 ====
According to [http://freifunk.net/wiki/FreifunkFirmwareEnglish Freifunk site] there are two subversions:

 * 4 MB AMD flash memory, 16 MB RAM and 7 LEDs on front panel
 * 2 MB Intel flash memory, 8 MB RAM and 3 LEDs on front panel
==== WAP54G v3.0 ====
'''Outside:''' Label on the bottom reads: "WAP54G ver:3". The serial number starts with: "MDG3" It features three LED's on the front panel: Power/Act/Link, colored red/green/yellow. There's also a "Easy secure" button to the front. On the back, there's one power connector, a single LAN connector, a reset button (in this order, counted from left). This version has 2MB of flash, and 8 MB of RAM.

'''Inside:''' The same Broadcom CPU is used that can be found in the WRT54GS V4, labeled: BCM 5352EKPB, 200MHz. The same applies to the LAN: It's connected to the CPU after decoupling, no additional hardware used. Wireless circuitry on the PCB, no mini-PCI. A JTAG header seems to be there, as well as a RS232 header. However, to use the 2nd RS232, you'll need to solder two 0 Ohm bridge dummy SMD resistors. SMD0805 package should do here.

The flash chip is NOT a intel one, as one might expect. It's a SST SST39VF160-70-4c-eke 16MBit instead, and it's NOT completely pin compatible to the intel 28F160C3 found on V2. Reviving the V3 therefor needs a different approach, see http://wiki.openwrt.org/WAP54GHowto.

Both antennas are connected via coax cable to the back TNC connectors, so no PBC mounted connectors here. Cheap micro coax is used for this, the lines are quite long. Nifty new feature on the v3 PCB: Resoldering a single capacitor from the currently used microstrip to a 3rd one prior to the antenna switch ending with solder pads, where a (probably better and shorter) coax cable can be soldered with your connector of choice on the other end.

PCB measurements: ~ 12 cm x 10 cm

'''Power:''' The WAP54G v3 needs much less current than it's brothers WRT54G(/S), about half (250 .. 350 mA on 12V DC). According to this, the shipped power brick only yields 500mA/12V max, compared to 1A/12V max for the WRT series.

=== Table summary ===
How to get info:

 * board info: {{{nvram show | grep board | sort}}}[[BR]]
 * version info: {{{nvram show | grep ver | sort}}}[[BR]]
 * cpu model: {{{cat /proc/cpuinfo | grep cpu}}}
||'''Model''' ||'''boardrev''' ||'''boardtype''' ||'''boardflags''' ||'''boardflags2''' ||'''boardnum''' ||'''wl0_corerev''' ||'''cpu model''' ||'''boot_ver''' ||'''pmon_ver''' ||'''os_version''' ||'''firmware_version''' ||
||WAP54G v1.0 ||- ||bcm94710dev ||- ||- ||2 ||4 ||BCM4702KPB ||- ||5.3.22 ||- ||- ||
||WAP54G v1.1 ||- ||bcm94710dev ||- ||- ||2 ||5 ||BCM4702KPB ||- ||{{{GemtekPmonVer = "10" ?}}} ||3.61.13.0 ||v2.08.08(USA) ||
||WAP54G v2 ||0x10 ||0x0446 ||8 ||0 ||1024 ||7 ||BCM3302 V0.7 ||- ||CFE 3.51.21.0 ||3.51.21.0 ||- ||
||WAP54G v3 || 0x13 || 0x0467 || 0x0758 || - || WAP54GV3_8M_0614 || - || BCM3302 V0.8(?) || - || CFE 3.91.39.0 || 3.91.39.0 || v3.05.03(EU) ||
Please complete this table. Look at the [http://openwrt.org/forum/viewtopic.php?pid=8127#p8127 Determining WRT54G/GS model using nvram variables] thread. May be this table should move up to ["OpenWrtDocs/Hardware"].

=== Enabling boot_wait ===
If the boot_wait variable is set, the bootup process is delayed by few seconds allowing a new firmware to be installed through the bootloader using tftp. There is no ping in web interface so "ping bug" method of WRT54G do not work.

==== Using configuration restore ====
Download one of mini configs:

[http://www.volny.cz/vanekt/openwrt/boot_wait_on_wap54g_fw2.07_config.bin config.bin] for LinkSys worldwide firmware versions 2.0x

[http://www.volny.cz/vanekt/openwrt/boot_wait_on_wap54g_fw2.07eu_config.bin config.bin] for LinkSys EU firmware versions 2.0x

Use web interface, navigate to <Setup> <Password> [Restore] and upload {{{config.bin}}}. This config changes just {{{boot_wait=on}}}, other configuration stays unchanged.

Verify that setting has worked by navigating to http://192.168.1.245/apply.cgi?action=Nvram

Tested only on original LinkSys firmwares version 2.07, 2.07EU, 3.04. Please report success on other fw versions.

This method is known '''not to work on LinkSys fw 1.0x''', nor on '''fw 3.05'''

Works on v1.1 fw 2.08 - -- BrianWhite [[DateTime(2006-11-03T21:50:41Z)]]

==== Setting boot_wait from a serial connection ====
Same as for [:OpenWrtDocs/Installing:WRT54G].

==== Setting boot_wait from 3rd party firmware ====
telnet to the device and use nvram command.

----
 . CategoryModel
