## Please add only OpenWrt and WAP54G related things to this page! Thanks.
'''Linksys WAP54G'''

This device is intended as an ACCESS POINT by manufacturer (one ethernet interface, smaller flash and RAM than WRT54G). Running OpenWrt is possible in limited form only.

See the Seattle Wireless page: SeattleWireless:WAP54G. Also see ["WAP54GHowto"].

[[TableOfContents]]
=== Hardware versions ===
===== Identification by S/N =====
Useful for identifying shrinkwrapped units. The '''S/N''' can be found on the bottom side of the box.

|||| (!) '''Please contribute to this list.''' (!) ||||'''!OpenWrt''' ||
||'''Model''' ||<style="TEXT-ALIGN: center">'''S/N''' ||<style="TEXT-ALIGN: center">'''Stable[[BR]]White Russian''' ||<style="TEXT-ALIGN: center">'''Development[[BR]]Kamikaze'''||
||WAP54G v1.0 ||<style="TEXT-ALIGN: center">MDG0 ||<style="TEXT-ALIGN: center">WiP [[BR]] No working official image yet! [[BR]] Do NOT flash until you have serial console! ||<style="TEXT-ALIGN: center">WiP [[BR]] No working official image yet! [[BR]] Do NOT flash until you have serial console! ||
||WAP54G v1.1 ||? ||<style="TEXT-ALIGN: center">? ||<style="TEXT-ALIGN: center">? ||
||WAP54G v2 ||<style="TEXT-ALIGN: center">MDG2 ||<style="TEXT-ALIGN: center">WiP ||<style="TEXT-ALIGN: center">WiP ||
||WAP54G v3 ||<style="TEXT-ALIGN: center">MDG3 ||<style="TEXT-ALIGN: center">WiP ||<style="TEXT-ALIGN: center">WiP ||


==== WAP54G v1.0 ====
The label on the bottom reads just "Model No WAP54G", version 1.0 is not marked.

The WAP54G v1.0 is based on the Broadcom 4710 board. It has a 125 MHz CPU, 2 MB flash and 8 MB SDRAM. The wireless NIC is a mini-PCI card. There are 7 status leds on the front panel. The reset button is next to the ethernet connector (left side of the ethernet connector).

No UART on the board. To get serial console you have connect UART to 20 pin header or solder it on board. More info on SeattleWireless:WAP54G

There is no JTAG header.

To take the front cover off of this unit you must first remove the small screws under the rubber covers of the front feet!

Version 1.0 is really special edition: full of bugs, easy to brick, hard to unbrick. Better stay away. If you insist, read carefully ["OpenWrtDocs/Hardware/Linksys/WAP54Gv10"]

==== WAP54G v1.1 ====
==== WAP54G v2.0 ====
According to [http://freifunk.net/wiki/FreifunkFirmwareEnglish Freifunk site] there are two sub versions:

 * 4 MB AMD flash memory, 16 MB RAM and 7 LEDs on front panel
 * 2 MB Intel flash memory, 8 MB RAM and 3 LEDs on front panel

==== WAP54G v3.0 ====
=== Table summary ===
How to get info:

 * board info: {{{nvram show | grep board | sort}}}[[BR]]
 * cpu model: {{{cat /proc/cpuinfo | grep cpu}}}

||'''Model''' ||'''boardrev''' ||'''boardtype''' ||'''boardflags''' ||'''boardflags2''' ||'''boardnum''' ||'''wl0_corerev''' ||'''cpu model''' ||'''boot_ver''' ||'''pmon_ver''' ||
||WAP54G v1.0 ||- ||bcm94710dev'''[:OpenWrtDocs/Hardware/Linksys/WAP54Gv10#cr+in+nvram:\r]''' ||- ||- ||2'''[:OpenWrtDocs/Hardware/Linksys/WAP54Gv10#cr+in+nvram:\r]''' ||4 ||BCM4702KPB ||- ||5.3.22 ||


Other NVRAM variables of interest : firmware_version, os_version

Please complete this table. Look at the [http://openwrt.org/forum/viewtopic.php?pid=8127#p8127 Determining WRT54G/GS model using nvram variables] thread. May be this table should move up to ["OpenWrtDocs/Hardware"].

=== Enabling boot_wait ===
If the boot_wait variable is set, the bootup process is delayed by few seconds allowing a new firmware to be installed through the bootloader using tftp. There is no ping in web interface so "ping bug" method of WRT54G do not work.

==== Using configuration restore ====
Download one of mini configs:

[http://www.volny.cz/vanekt/openwrt/boot_wait_on_wap54g_fw2.07_config.bin config.bin] for LinkSys worldwide firmware versions 2.0x and 3.0x

[http://www.volny.cz/vanekt/openwrt/boot_wait_on_wap54g_fw2.07eu_config.bin config.bin] for LinkSys EU firmware versions 2.0x and 3.0x

Use web interface, navigate to <Setup> <Password> [Restore] and upload {{{config.bin}}}. This config changes just {{{boot_wait=on}}}, other configuration stays unchanged.

Verify that setting has worked by navigating to http://192.168.1.245/apply.cgi?action=Nvram

Tested only on original LinkSys firmwares version 2.07, 2.07EU, 3.04. Please report success on other fw versions.

This method is known '''not to work on LinkSys fw 1.0x'''

==== Setting boot_wait from a serial connection ====
Same as for [:OpenWrtDocs/Installing:WRT54G].

==== Setting boot_wait from 3rd party firmware ====
telnet to the device and use nvram command.

----
CategoryModel
