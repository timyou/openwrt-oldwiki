'''Linksys WRT54G'''

=== Hardware versions ===

There are currently five versions of the WRT54G (v1.0, v1.1, v2.0, v2.2, v3.0). Except the last two (v2.2 and v3.0), the WRT54G units are supported by the current CVS version of OpenWrt). boot_wait is off by default on these routers, so You should turn it on. The version number is found on the label on the bottom of the front part of the case, below the Linksys logo.

===== Identification by S/N =====
Useful for identifying shrinkwrapped units. The '''S/N''' can be found on the box, below the UPC barcode.
||||<tablestyle="width 50%"> (!) '''Please contribute to this list.''' (!) ||||'''OpenWRT'''||
||'''Model'''||'''S/N'''||'''CVS'''||'''EXP'''||
||<(|2>WRT54G v1.1||CDF20xxxxxxx||<:|2> (./) ||<:|2> (./) ||
||CDF30xxxxxxx||
||WRT54G v2||CDF50xxxxxxx||<:> (./) ||<:> (./) ||
||WRT54G v2.2||CDF70xxxxxxx||<:> {X} ||<:> (./) ||
||WRT54G v3||CDF80xxxxxxx||<:> {X} ||<:> (./) ||
==== WRT54G v1.0 ====
The WRT54G v1.0 is based on the Broadcom 4710 board. It has a 125MHz CPU, 4Mb flash and 16Mb SDRAM.
The wireless NIC is a mini-PCI card. The switch is an ADM6996.

==== WRT54G v1.1 ====
The WRT54G v1.1 is based on the Broadcom 4710 board. It has a 125MHz CPU, 4Mb flash and 16Mb SDRAM.
The wireless NIC is soldered to the board. The switch is an ADM6996.

Hardware informations (nvram) :

{{{boardtype=bcm94710dev}}}

==== WRT54G v2.0 ====
The WRT54G v2.0 is based on the Broadcom 4712 board. It has a 200MHz CPU, 4Mb flash and 16Mb SDRAM.
The wireless NIC is integrated to the board. The switch is an ADM6996.

Hardware informations (nvram) :

{{{boardtype=0x0101
boardflags=0x0188}}}


==== WRT54G v2.2 ====
The WRT54G v2.2 is based on the Broadcom 4712 board. It has a 200MHz CPU, 4Mb flash and 16Mb DDR-SDRAM.
The wireless NIC is integrated to the board. The switch is a BCM5325.

/!\ '''The current version OpenWrt doesn't support these units, yet.'''

Hardware informations (nvram) :

{{{boardtype=0x0708
boardflags=0x0118}}}

==== WRT54G v3.0 ====
This unit is just like the V2.2 Except it has an extra reboot button on the left front panel behind a Cisco logo.
Experimental works with it.

/!\ '''To take the front cover off of this unit you must first remove the small screws under the rubber covers of the front feet!'''


/!\ '''The current version OpenWrt doesn't support these units, yet.'''



=== Hardware hacking ===
There are revision XH units of the WRT54G v2.0. These units have 32Mb of memory, but they are locked to 16Mb. You can unlock the remaining memory with changing some of the variables.
Afterburner (aka. Speedbooster) mode can be enabled with some variables, too.

/!\ '''However, there are no guaranties, that these will work, and changing the memory configuration on a non-XH unit will give You a brick. Check the forums for more info.'''


If you have a look at the WRT54G v2.2 board, you can find on the left corner, near the power LED, an empty place for a 4 pins button. On the board it is printed as SW2. This is the second reset button you can find on WRT54G v3.0, except that it has not been soldered.
