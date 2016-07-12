## Please add only OpenWrt and WAP54G related things to this page! Thanks.

'''Linksys WAP54G'''

This device is intended as an ACCESS POINT by manufacturer (one ethernet interface, smaller flash and RAM than WRT54G). Running OpenWrt is possible in limited form only.

See the Seattle Wireless page: SeattleWireless:WAP54G.
Also see [:WAP54GHowto].

[[TableOfContents]]


=== Hardware versions ===


===== Identification by S/N =====

Useful for identifying shrinkwrapped units. The '''S/N''' can be found on
the bottom side of the box.
||||<tablestyle="width 50%"> (!) '''Please contribute to this list.''' (!) ||||'''!OpenWrt'''||
||'''Model'''||<:> '''S/N'''||<:>  '''Stable[[BR]]White Russian'''||<:>  '''Development[[BR]]Kamikaze'''||
||WAP54G v1.0||<:> MDG0||<:> WiP ||<:> WiP ||
||WAP54G v1.1|| ? ||<:> ? ||<:> ? ||
||WAP54G v2|| ? ||<:> WiP ||<:> WiP ||
||WAP54G v3|| ? ||<:> WiP ||<:> WiP ||


==== WAP54G v1.0 ====

The WAP54G v1.0 is based on the Broadcom 4710 board. It has a 125 MHz CPU, 2 MB
flash and 8 MB SDRAM. The wireless NIC is a mini-PCI card. There are 7 status leds on the front panel. The reset button is next to the ethernet connector (left side of the ethernet connector).

To take the front cover off of this unit you must first remove the small screws under the
rubber covers of the front feet!

The label on the bottom reads just "Model No WAP54G", version 1.0 is not marked.

Version 1.0 is really special edition: full of bugs, easy to brick. Better stay away. If you insist, read carefully [:OpenWrtDocs/Hardware/Linksys/WAP54Gv10]

=== Table summary ===

How to get info:

 * board info: {{{nvram show | grep board | sort}}}[[BR]]
 * cpu model: {{{cat /proc/cpuinfo | grep cpu}}}

||'''Model'''       ||'''boardrev'''||'''boardtype'''||'''boardflags'''||'''boardflags2'''||'''boardnum'''||'''wl0_corerev'''||'''cpu model'''||'''boot_ver'''||'''pmon_ver'''||
||WAP54G v1.0       ||     -        ||  bcm94710dev  ||      -         ||       -         ||   2          ||       4         ||  BCM4702KPB   ||       -      ||    5.3.22    ||

Other NVRAM variables of interest :  firmware_version, os_version

Please complete this table. Look at the
[http://openwrt.org/forum/viewtopic.php?pid=8127#p8127 Determining WRT54G/GS model using nvram variables]
thread. May be this table should move up to [:OpenWrtDocs/Hardware].


=== Hardware hacking ===
----
CategoryModel
