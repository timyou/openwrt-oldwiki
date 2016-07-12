'''Linksys WRT54G'''


[[TableOfContents]]


=== Hardware versions ===

There are currently eight versions of the WRT54G (v1.0, v1.1, v2.0, v2.2,
v3.0, v3.1, v4.00, v5). With the exception of v5 devices the WRT54G units
are full supported by OpenWrt 1.0 (White Russian) and later. {{{boot_wait}}}
is off by default on these routers, so you should turn it on. The version
number is found on the label on the bottom of the front part of the case
below the Linksys logo.


===== Identification by S/N =====

Useful for identifying shrinkwrapped units. The '''S/N''' can be found on
the box, below the UPC barcode.
||||<tablestyle="width 50%"> (!) '''Please contribute to this list.''' (!) ||||'''!OpenWrt'''||
||'''Model'''||'''S/N'''||<:>  '''Stable[[BR]]White Russian'''||<:>  '''Unstable[[BR]]development'''||
||<(|2>WRT54G v1.0||CDF0xxxxxxx||<:|2> (./) ||<:|2> (./) ||
||CDF1xxxxxxx||
||<(|2>WRT54G v1.1||CDF2xxxxxxx||<:|2> (./) ||<:|2> (./) ||
||CDF3xxxxxxx||
||WRT54G v2||CDF5xxxxxxx||<:> (./) ||<:> (./) ||
||WRT54G v2.2||CDF7xxxxxxx||<:> (./) ||<:> (./) ||
||WRT54G v3||CDF8xxxxxxx||<:> (./) ||<:> (./) ||
||WRT54G v3.1 (AU?)||CDF9xxxxxxx||<:> (./) ||<:> (./) ||
||WRT54G v4||CDFAxxxxxxx||<:> (./) ||<:> (./) ||
||WRT54G v5||CDFBxxxxxxx||<:> {X} ||<:> {X} ||


==== WRT54G v1.0 ====

The WRT54G v1.0 is based on the Broadcom 4710 board. It has a 125 MHz CPU, 4 MB
flash and 16 MB SDRAM. The wireless NIC is a mini-PCI card. The switch is an
ADM6996.


==== WRT54G v1.1 ====

The WRT54G v1.1 is based on the Broadcom 4710 board. It has a 125 MHz CPU, 4 MB
flash and 16 MB SDRAM. The wireless NIC is soldered to the board. The switch is
an ADM6996.


==== WRT54G v2.0 ====

The WRT54G v2.0 is based on the Broadcom 4712 board. It has a 200 MHz CPU, 4 MB
flash and 16 MB SDRAM. The wireless NIC is integrated to the board. The switch is
an ADM6996.


==== WRT54G v2.2 ====

The WRT54G v2.2 is based on the Broadcom 4712 board. It has a 200 MHz CPU, 4 MB
flash and 16 MB DDR-SDRAM. The wireless NIC is integrated to the board. The switch
is a BCM5325.


==== WRT54G v3.0 & WRT54G v3.1 ====

This unit is just like v2.2 except it has an extra button on the left front panel
behind a Cisco logo. This button can be illuminated by either a yellow or white
LED, and is used for the "Secure Easy Setup" encryption setup feature.

/!\ '''NOTE:''' To take the front cover off of v3.1, you must first remove the small
screws under the rubber covers of the front feet!


==== WRT54G v4.00 ====

New more integrated board layout
([http://www.linksysinfo.org/modules.php?name=Content&pa=showpage&pid=6#wrt54g4 photos here]),
switch is now in SoC.

/!\ '''NOTE:''' To take the front cover off of this unit you must first remove the small
screws under the rubber covers of the front feet!


==== WRT54G v5 ====

/!\ '''NOTE:''' !OpenWrt does '''NOT''' currently support the WRT54G '''v5'''!

Initial reports are that this version has switched to a non-Linux OS (!VxWorks).  It appears
from pictures that it is nearly identical to v4 with an updated rev on the processor, less
flash (2 MB) and less RAM (8 MB). It is unknown at this time if v5 can be supported by
!OpenWrt.


=== Table summary ===

How to get info:

 * board info: {{{nvram show | grep board | sort}}}[[BR]]
 * cpu model: {{{cat /proc/cpuinfo | grep cpu}}}

||'''Model'''       ||'''boardrev'''||'''boardtype'''||'''boardflags'''||'''boardflags2'''||'''boardnum'''||'''wl0_corerev'''||'''cpu model'''||
||WRT54G v1.1       ||     -        ||  bcm94710dev  ||      -         ||       -         ||  42           ||       5         || BCM4710 V0.0  ||
||WRT54G v2.0       ||     -        ||  0x0101       ||  0x0188        ||       -         ||      -       ||       -         || BCM3302 V0.7  ||
||WRT54G v2.2       ||     -        ||  0x0708       ||  0x0118        ||       -         ||      -       ||       7         || -             ||
||WRT54G v3.0       || 0x10         ||  0x0708       ||  0x0118        ||  0              ||  42          ||       7         || BCM3302 V0.7 ||
||WRT54G v3.1 (AU?) || 0x10         ||  0x0708       ||  0x0118        ||  0              ||  42          ||       7         || BCM3302 V0.7 ||
||WRT54G v4.0       || 0x10         ||  0x0708       ||  0x0118        ||  0              ||  42          ||       7         || BCM3302 V0.7 ||

Other NVRAM variables of interest :  boot_ver, pmon_ver, firmware_version, os_version

Please complete this table. Look at the
[http://openwrt.org/forum/viewtopic.php?pid=8127#p8127 Determining WRT54G/GS model using nvram variables]
thread. May be this table should move up to [:OpenWrtDocs/Hardware].


=== Hardware hacking ===

There are revision XH units of the WRT54G v2.0. These units have 32 MB of memory, but
they are locked to 16 MB. You can unlock the remaining memory with changing some of the
variables. Afterburner (aka. Speedbooster) mode can be enabled with some variables, too.

/!\ '''NOTE:''' However, there are no guaranties, that these will work, and changing the
memory configuration on a non-XH unit will give You a brick. Check the forums for more info.

If you have a look at the WRT54G v2.2 board, you can find on the left corner, near the power
LED, an empty place for a 4 pins button. On the board it is printed as SW2. This is the
second reset button you can find on WRT54G v3.0, except that it has not been soldered.

Many versions of this model have a (possibly unpopulated) serial header, for more info see [http://www.rwhitby.net/wrt54gs/serial.html].
