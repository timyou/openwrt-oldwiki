## Please add only OpenWrt and WRT54G related things to this page! Thanks.

'''Linksys WRT54G'''

There are currently many versions of the WRT54G. With the exception of v5
devices the WRT54G units are supported by OpenWrt 1.0 (White Russian)
and later. The version number is found on the label on the bottom of the
front part of the case below the Linksys logo.

Some consider the [:OpenWrtDocs/Hardware/Linksys/WRT54GL: WRT54GL] and
[:OpenWrtDocs/Hardware/Linksys/WRT54G3G: WRT54G3G] versions of this model.

{{{boot_wait}}} is '''off''' by default on these routers, so you should
turn it on, see [:OpenWrtDocs/BootWait].


'''Identification by S/N'''

Useful for identifying shrinkwrapped units. The '''S/N''' can be found on
the box, below the UPC barcode.
||||<tablestyle="width 50%"> (!) '''Please contribute to this list.''' (!) ||||'''!OpenWrt'''||
||'''Model'''||<:> '''S/N'''||<:>  '''Stable[[BR]]White Russian'''||<:>  '''Development[[BR]]Kamikaze'''||
||<(|2>WRT54G v1.0||<:> CDF0||<:|2> (./) ||<:|2> (./) ||
||<:> CDF1||
||<(|3>WRT54G v1.1||<:> CDF2||<:|3> (./) ||<:|3> (./) ||
||<:> CDF3||
||<:> CDF4||
||WRT54G v2||<:> CDF5||<:> (./) ||<:> (./) ||
||WRT54G v2.2||<:> CDF7||<:> (./) ||<:> (./) ||
||WRT54G v3||<:> CDF8||<:> (./) ||<:> (./) ||
||WRT54G v3.1 (AU?, DE, and UK)||<:> CDF9||<:> (./) ||<:> (./) ||
||WRT54G v4||<:> CDFA||<:> (./) ||<:> (./) ||
||WRT54G v5||<:> CDFB||<:> {X} ||<:> {X} ||


'''WRT54G v1.0'''

The WRT54G v1.0 is based on the Broadcom 4710 board. It has a 125 MHz CPU, 4 MB
flash and 16 MB SDRAM. The wireless NIC is a mini-PCI card. The switch is an
ADM6996. Resetting to factory defaults via reset button or mtd erase nvram is '''not safe''' on this unit.


'''WRT54G v1.1'''

The WRT54G v1.1 is based on the Broadcom 4710 board. It has a 125 MHz CPU, 4 MB
flash and 16 MB SDRAM. The wireless NIC is soldered to the board. The switch is
an ADM6996. Resetting to factory defaults via reset button or mtd erase nvram is '''not safe''' on this unit.


'''WRT54G v2.0'''

The WRT54G v2.0 is based on the Broadcom 4712 board. It has a 200 MHz CPU, 4 MB
flash and 16 MB SDRAM. The wireless NIC is integrated to the board. The switch is
an ADM6996. Resetting to factory defaults via reset button or mtd erase nvram is '''not safe''' on this unit.


'''WRT54G v2.2'''

The WRT54G v2.2 is based on the Broadcom 4712 board. It has a 200 MHz CPU, 4 MB
flash and 16 MB DDR-SDRAM. The wireless NIC is integrated to the board. The switch
is a BCM5325. Resetting to factory defaults via reset button or mtd erase nvram is '''not safe''' on this unit.


'''WRT54G v3.0 & WRT54G v3.1'''

This unit is just like v2.2 except it has an extra button on the left front panel
behind a Cisco logo. This button can be illuminated by either a yellow or white
LED, and is used for the "Secure Easy Setup" encryption setup feature.
Resetting to factory defaults via reset button or mtd erase nvram is '''not safe''' on this unit.

To remove the front cover from a v3.1, you must first remove the small screws under the
rubber covers of the front feet!

If you have such a thing you can try 
http://192.168.1.1/Cysaja.asp
to identify

There is "Module Name=WRT54G; Firmware Version=v4.01.1,..." or something like that. 


'''WRT54G v4.0'''

New more integrated board layout
([http://www.linksysinfo.org/modules.php?name=Content&pa=showpage&pid=6#wrt54g4 photos here]),
switch is now in SoC.

To remove the front cover from this unit you must first remove the small screws under the
rubber covers of the front feet!
Resetting to factory defaults via reset button or mtd erase nvram is '''not safe''' on this unit.


'''WRT54G v5'''

/!\ '''NOTE:''' WRT54G V5 IS '''NOT''' SUPPORTED. IT WILL NEVER BE SUPPORTED. WE ARE SICK OF
HEARING ABOUT THE V5!

This version has switched to a proprietary non-Linux OS (WikiPedia:VxWorks). It appears from
pictures that it is nearly identical to v4 with an updated rev on the processor, less
flash (2 MB) and less RAM (8 MB). It is unknown at this time if v5 can be supported by
!OpenWrt.

[http://wrt-wiki.bsr-clan.de/index.php?title=Flash_Your_Version_5_WRT54G Currently only a downstripped DD-WRT is supported on WRT54G/GS v5 and v5.1]

'''Table summary'''

How to get info:

 * board info: {{{nvram show | grep board | sort}}}[[BR]]
 * cpu model: {{{grep cpu /proc/cpuinfo}}}

||'''Model'''       ||'''boardrev'''||'''boardtype'''||'''boardflags'''||'''boardflags2'''||'''boardnum'''||'''wl0_corerev'''||'''cpu model'''||'''boot_ver'''||'''pmon_ver'''||
||WRT54G v1.0       ||     -        ||  bcm94710dev  ||      -         ||       -         ||  42          ||       4         || BCM4710 V0.0  ||  v1.0        ||  3.11.30.5   ||
||WRT54G v1.1       ||     -        ||  bcm94710dev  ||      -         ||       -         ||  42          ||       5         || BCM4710 V0.0  ||       -      ||       -      ||
||WRT54G v2.0       || 0x10         ||  0x0101       ||  0x0188        ||  0              ||  42          ||       -         || BCM3302 V0.7  ||  v2.1, v2.3   ||  3.51.21.0   ||
||WRT54G v2.2       || 0x10         ||  0x0708       ||  0x0118        ||  0              ||  42          ||       7         || BCM3302 V0.7  ||  v3.4        ||  3.61.13.0   ||
||WRT54G v3.0       || 0x10         ||  0x0708       ||  0x0118        ||  0              ||  42          ||       7         || BCM3302 V0.7  ||       -      ||       -      ||
||WRT54G v3.1 (AU?) || 0x10         ||  0x0708       ||  0x0118        ||  0              ||  42          ||       7         || BCM3302 V0.7  ||       -      ||       -      ||
||WRT54G v4.0       || 0x10         ||  0x0708       ||  0x0118        ||  0              ||  42          ||       7         || BCM3302 V0.7  ||       -      ||       -      ||

Other NVRAM variables of interest :  firmware_version, os_version

Please complete this table. Look at the
[http://openwrt.org/forum/viewtopic.php?pid=8127#p8127 Determining WRT54G/GS model using nvram variables]
thread. May be this table should move up to [:OpenWrtDocs/Hardware].


'''Hardware hacking'''

There are revision XH units of the WRT54G v2.0. These units have 32 MB of memory, but
they are locked to 16 MB. You can unlock the remaining memory with changing some of the
variables. Afterburner (aka. Speedbooster) mode can be enabled with some variables, too.

/!\ '''NOTE:''' However, there are no guaranties that these will work, and changing the
memory configuration on a non-XH unit will give you a brick. Check the forums for more info.

If you have a look at the WRT54G v2.2 board, you can find on the left corner, near the power
LED, an empty place for a 4 pins button. On the board it is printed as SW2. This is the
second reset button you can find on WRT54G v3.0, except that it has not been soldered.

Many versions of this model have a (possibly unpopulated) serial header, for more info see
[http://www.rwhitby.net/wrt54gs/serial.html].

||Pin 1||3.3V||Pin 2||3.3V||
||Pin 3||Tx (ttyS1)||Pin 4||Tx (ttyS0)||
||Pin 5||Rx (ttyS1)||Pin 6||Rx (ttyS0)||
||Pin 7||NC||Pin 8||NC||
||Pin 9||GND||Pin 10||GND||

'''Opening the case'''

'''WRT54G v1.0'''

Check [http://www.servomagazine.com/forum/viewtopic.php?p=34263&sid=821e1885f8c530e26278d85d701631ff here] for instructions and [http://seattlewireless.net/~mattw/photos/linksyswrt54g/gallery/ here] for pictures. A 9/16 socket wrench or similar tool can be used to remove the antenna.

'''WRT54G v3.1'''

Check [http://www.byteclub.net/wiki/Wrt54g#Opening_the_case here] for instructions.

----
CategoryModel
