'''Linksys WRT54G'''
[[TableOfContents]]

=== Hardware versions ===

There are currently seven versions of the WRT54G (v1.0, v1.1, v2.0, v2.2, v3.0, v3.1, v4.00). With the exception of v4.00 devices (it is currently marked as untested for White Russian RC1), the WRT54G units are supported by OpenWrt 1.0 (White Russian) and later. boot_wait is off by default on these routers, so you should turn it on. The version number is found on the label on the bottom of the front part of the case below the Linksys logo.

===== Identification by S/N =====
Useful for identifying shrinkwrapped units. The '''S/N''' can be found on the box, below the UPC barcode.
||||<tablestyle="width 50%"> (!) '''Please contribute to this list.''' (!) ||||'''OpenWRT'''||
||'''Model'''||'''S/N'''||'''CVS'''||'''EXP'''||
||<(|2>WRT54G v1.1||CDF20xxxxxxx||<:|2> (./) ||<:|2> (./) ||
||CDF30xxxxxxx||
||WRT54G v2||CDF50xxxxxxx||<:> (./) ||<:> (./) ||
||WRT54G v2.2||CDF70xxxxxxx||<:> {X} ||<:> (./) ||
||WRT54G v3||CDF80xxxxxxx||<:> {X} ||<:> (./) ||
||WRT54G v3.1 (AU?)||CDF90xxxxxxx||<:> {X} ||<:> (./) ||
||WRT54G v4||CDFA0xxxxxxx||<:> {X} ||<:> ? ||

==== WRT54G v1.0 ====
The WRT54G v1.0 is based on the Broadcom 4710 board. It has a 125MHz CPU, 4Mb flash and 16Mb SDRAM.
The wireless NIC is a mini-PCI card. The switch is an ADM6996.

==== WRT54G v1.1 ====
The WRT54G v1.1 is based on the Broadcom 4710 board. It has a 125MHz CPU, 4Mb flash and 16Mb SDRAM.
The wireless NIC is soldered to the board. The switch is an ADM6996.

Hardware informations (nvram) :

{{{boardtype=bcm94710dev
}}}

==== WRT54G v2.0 ====
The WRT54G v2.0 is based on the Broadcom 4712 board. It has a 200MHz CPU, 4Mb flash and 16Mb SDRAM.
The wireless NIC is integrated to the board. The switch is an ADM6996.

Hardware informations (nvram) :

{{{boardtype=0x0101
boardflags=0x0188}}}


==== WRT54G v2.2 ====
The WRT54G v2.2 is based on the Broadcom 4712 board. It has a 200MHz CPU, 4Mb flash and 16Mb DDR-SDRAM.
The wireless NIC is integrated to the board. The switch is a BCM5325.

Hardware informations (nvram) :

{{{boardtype=0x0708
boardflags=0x0118}}}

==== WRT54G v3.0 & WRT54G v3.1 ====
This unit is just like the V2.2 Except it has an extra reboot button on the left front panel behind a Cisco logo.

==== WRT54G v4.00 ====
New more integrated board layout (photos [http://www.linksysinfo.org/modules.php?name=Content&pa=showpage&pid=6#wrt54g4 here]), switch is now in SoC.

Hardware informations (nvram) :

{{{boardrev=0x10
boardtype=0x0708
boardflags2=0
boardflags=0x0118
boardnum=42}}}

/!\ '''To take the front cover off of this unit you must first remove the small screws under the rubber covers of the front feet!'''

=== Table summary ===

how to get info :

* board info: nvram show | grep board | sort[[BR]]
* cpu model: cat /proc/cpuinfo | grep cpu

||'''Model'''       ||'''boardrev'''||'''boardtype'''||'''boardflags'''||'''boardflags2'''||'''boardnum'''||'''wl0_corerev'''||'''cpu model'''||
||WRT54G v1.1       ||     -        ||  bcm94710dev  ||      -         ||       -         ||  42           ||       5         || BCM4710 V0.0  ||
||WRT54G v2.0       ||     -        ||  0x0101       ||  0x0188        ||       -         ||      -       ||       -         || BCM3302 V0.7  ||
||WRT54G v2.2       ||     -        ||  0x0708       ||  0x0118        ||       -         ||      -       ||       7         || -             ||
||WRT54G v3.0       || 0x10         ||  0x0708       ||  0x0118        ||  0              ||  42          ||       7         || BCM3302 V0.7 ||
||WRT54G v3.1 (AU?) || 0x10         ||  0x0708       ||  0x0118        ||  0              ||  42          ||       7         || BCM3302 V0.7 ||
||WRT54G v4.0       || 0x10         ||  0x0708       ||  0x0118        ||  0              ||  42          ||       7         || BCM3302 V0.7 ||
||WRT54GS v1.0      || 0x10         ||  0x0101       ||  0x0388        ||  0              ||  42          ||       7         || BCM3302 V0.7  ||
||WRT54GS v1.1      || 0x10         ||  0x0708       ||  0x0318        ||  0              ||  42          ||       7         || BCM3302 V0.7  ||
||WRT54GS v2.0      ||    ?         ||       ?       ||  ?             ||  ?             ||  ?           ||       -         || -             ||
||WRT54GS v2.1      ||    ?         ||       ?       ||  ?             ||  ?             ||  ?           ||       -         || -             ||
||Allnet all0277   || 0x10         ||  bcm94710dev   ||  0x0388        ||  0              ||  42          ||       4         || BCM4710 V0.0  ||
||Buffalo WBR-54G   || 0x10         ||  bcm94710ap   ||  0x0188        ||  2              ||  42          ||       -         || -             ||
||Toshiba WRC1000   || -            ||  bcm94710r4   ||  -             ||  -              ||  100         ||       -         || -             ||
||Buffalo WBR2-G54S || 0x10         ||  0x0101       ||  0x0188        ||  0              ||  00          ||       -         || -             ||
||Asus WL-500G Deluxe|| 0x10        ||  bcm95365r    ||      -         ||       -         ||  45          ||       5         || BCM3302 V0.7 ||
||Asus WL-500G          ||               || bcm94710dev ||                  ||                 ||  asusX    ||                  || BCM4710 V0.0 ||

*other variables (nvram) of interest :  boot_ver, pmon_ver, firmware_version, os_version


please complete this table. Look at this thread : http://openwrt.org/forum/viewtopic.php?pid=8127#p8127
May be this table should move up to OpenWrtDocs/Hardware.


=== Hardware hacking ===
There are revision XH units of the WRT54G v2.0. These units have 32Mb of memory, but they are locked to 16Mb. You can unlock the remaining memory with changing some of the variables.
Afterburner (aka. Speedbooster) mode can be enabled with some variables, too.

/!\ '''However, there are no guaranties, that these will work, and changing the memory configuration on a non-XH unit will give You a brick. Check the forums for more info.'''


If you have a look at the WRT54G v2.2 board, you can find on the left corner, near the power LED, an empty place for a 4 pins button. On the board it is printed as SW2. This is the second reset button you can find on WRT54G v3.0, except that it has not been soldered.
