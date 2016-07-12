## Please add only OpenWrt and WRT54G related things to this page! Thanks.

'''Linksys WRT54G'''

There are currently many versions of the WRT54G. With the exception of v5
devices the WRT54G units are supported by OpenWrt 1.0 (White Russian)
and later. The version number is found on the label on the bottom of the
front part of the case below the Linksys logo.

{{{boot_wait}}} is '''off''' by default on these routers, so you should
turn it on, see [:OpenWrtDocs/BootWait].

[[TableOfContents]]

=== Setting boot_wait to on ===

see 

'''Ping.asp Bug'''

If the boot_wait variable is set, the bootup process is delayed by few seconds allowing a new firmware to be installed through the bootloader using tftp. Setting of the boot_wait variable is done through a bug in the Ping.asp administration page by pinging the certain "addresses" listed below.  '''You find ping.asp by navigating through the administration page and selecting diagnostics.'''.

First, for this to work the '''internet port must have a valid ip address''', either from DHCP or manually configured from the main page - the port itself doesn't need to be connected unless using dhcp. Next, navigate to the Ping.asp page and enter exactly each line listed below, one line at a time into the "IP Address" field, pressing the Ping button after each entry.

{{{
;*/n${IFS}set${IFS}boot_wait=on
;*/n${IFS}commit
;*/n${IFS}show>tmp/ping.log
}}}

When you get to the last command the ping window should be filled with a long list of variables including '''boot_wait=on''' somewhere in that list.

This ping exploit definitely works with ALL WRT54G VERSIONS. You must have an address on the WAN port. In the Setup/Basic Setup/Internet Setup section you may wish to select Static IP and set IP=10.0.0.1, Mask=255.0.0.0, Gateway=10.0.0.2. Those values are meaningless; you'll be overwriting them soon with new firmware. Note: flashing a Linksys WRT54GS v1.1 by using TFTP is only possible using the Port 1 of the switch!

You can also use the [https://aachen.uni-dsl.de/download/wrt/Snapshots/rev121/buildroot-rev121/takeover takeover] script to make ping hack in a single command (need a shell command line interpreter). This script expects to find the to-be flashed firmware in a file called '''openwrt-g-code.bin''', which is in the ''current'' directory.

There is another bug still present in Ping.asp (firmware revision 3.03.1) where you can put your shell code into the ping_times variable. See http://www.linksysinfo.org/modules.php?name=Forums&file=viewtopic&t=448 This means you don't have to downgrade your firmware first and it removes the input size restrictions so you can use more obvious shell commands like:

{{{
`/usr/sbin/nvram set boot_wait=on`
`/usr/sbin/nvram commit`
`/usr/sbin/nvram show > /tmp/ping.log`
}}}

For instance, if you are in Unix and have Perl and LWP installed, you may issue this command:

{{{
echo 'submit_button=Ping&submit_type=start&action=Apply&change_action=gozila_cgi&ping_ip=10.0.0.1&ping_times=`/usr/sbin/nvram show > /tmp/ping.log`'|POST -C admin:admin http://192.168.1.1/apply.cgi
}}}

'''Via serial console'''

With a serial connection to your WRT, you don't have to use the ping bug or change your Linksys firmware. You can set boot_wait from the console, using the commands

{{{
#nvram set boot_wait=on
#nvram get boot_wait           (just to confirm, should respond with "on")
#nvram commit                  (takes a few seconds to complete)
}}}

You can also set boot_wait from the CFE boot loader (to enter CFE, reboot the router with "# reboot" while hitting {{{CTRL-C}}} continously)

{{{
CFE> nvram set boot_wait=on
CFE> nvram get boot_wait       (just to confirm, should respond with "on")
CFE> nvram commit              (takes a few seconds to complete)
}}}



=== Hardware versions ===

There are currently many versions of the WRT54G. With the exception of v5
devices the WRT54G units are supported by OpenWrt 1.0 (White Russian)
and later. {{{boot_wait}}} is off by default on these routers, so you should
turn it on. The version number is found on the label on the bottom of the
front part of the case below the Linksys logo.

Some consider the [:OpenWrtDocs/Hardware/Linksys/WRT54GL: WRT54GL] and
[:OpenWrtDocs/Hardware/Linksys/WRT54G3G: WRT54G3G] versions of this model.

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


==== WRT54G v1.0 ====

The WRT54G v1.0 is based on the Broadcom 4710 board. It has a 125 MHz CPU, 4 MB
flash and 16 MB SDRAM. The wireless NIC is a mini-PCI card. The switch is an
ADM6996. Resetting to factory defaults via reset button or mtd erase nvram is '''not safe''' on this unit.


==== WRT54G v1.1 ====

The WRT54G v1.1 is based on the Broadcom 4710 board. It has a 125 MHz CPU, 4 MB
flash and 16 MB SDRAM. The wireless NIC is soldered to the board. The switch is
an ADM6996. Resetting to factory defaults via reset button or mtd erase nvram is '''not safe''' on this unit.



==== WRT54G v2.0 ====

The WRT54G v2.0 is based on the Broadcom 4712 board. It has a 200 MHz CPU, 4 MB
flash and 16 MB SDRAM. The wireless NIC is integrated to the board. The switch is
an ADM6996. Resetting to factory defaults via reset button or mtd erase nvram is '''not safe''' on this unit.


==== WRT54G v2.2 ====

The WRT54G v2.2 is based on the Broadcom 4712 board. It has a 200 MHz CPU, 4 MB
flash and 16 MB DDR-SDRAM. The wireless NIC is integrated to the board. The switch
is a BCM5325. Resetting to factory defaults via reset button or mtd erase nvram is '''not safe''' on this unit.


==== WRT54G v3.0 & WRT54G v3.1 ====

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

==== WRT54G v4.0 ====

New more integrated board layout
([http://www.linksysinfo.org/modules.php?name=Content&pa=showpage&pid=6#wrt54g4 photos here]),
switch is now in SoC.

To remove the front cover from this unit you must first remove the small screws under the
rubber covers of the front feet!
Resetting to factory defaults via reset button or mtd erase nvram is '''not safe''' on this unit.

==== WRT54G v5 ====

/!\ '''NOTE:''' WRT54G V5 IS '''NOT''' SUPPORTED. IT WILL NEVER BE SUPPORTED. WE ARE SICK OF
HEARING ABOUT THE V5!

This version has switched to a proprietary non-Linux OS (WikiPedia:VxWorks). It appears from
pictures that it is nearly identical to v4 with an updated rev on the processor, less
flash (2 MB) and less RAM (8 MB). It is unknown at this time if v5 can be supported by
!OpenWrt.

=== Table summary ===

How to get info:

 * board info: {{{nvram show | grep board | sort}}}[[BR]]
 * cpu model: {{{grep cpu /proc/cpuinfo}}}

||'''Model'''       ||'''boardrev'''||'''boardtype'''||'''boardflags'''||'''boardflags2'''||'''boardnum'''||'''wl0_corerev'''||'''cpu model'''||'''boot_ver'''||'''pmon_ver'''||
||WRT54G v1.0       ||     -        ||  bcm94710dev  ||      -         ||       -         ||  42          ||       4         || BCM4702KPB ?  ||       -      ||       -      ||
||WRT54G v1.1       ||     -        ||  bcm94710dev  ||      -         ||       -         ||  42          ||       5         || BCM4710 V0.0  ||       -      ||       -      ||
||WRT54G v2.0       || 0x10         ||  0x0101       ||  0x0188        ||  0              ||  42          ||       -         || BCM3302 V0.7  ||  v2.3        ||  3.51.21.0   ||
||WRT54G v2.2       || 0x10         ||  0x0708       ||  0x0118        ||  0              ||  42          ||       7         || BCM3302 V0.7  ||  v3.4        ||  3.61.13.0   ||
||WRT54G v3.0       || 0x10         ||  0x0708       ||  0x0118        ||  0              ||  42          ||       7         || BCM3302 V0.7  ||       -      ||       -      ||
||WRT54G v3.1 (AU?) || 0x10         ||  0x0708       ||  0x0118        ||  0              ||  42          ||       7         || BCM3302 V0.7  ||       -      ||       -      ||
||WRT54G v4.0       || 0x10         ||  0x0708       ||  0x0118        ||  0              ||  42          ||       7         || BCM3302 V0.7  ||       -      ||       -      ||

Other NVRAM variables of interest :  firmware_version, os_version

Please complete this table. Look at the
[http://openwrt.org/forum/viewtopic.php?pid=8127#p8127 Determining WRT54G/GS model using nvram variables]
thread. May be this table should move up to [:OpenWrtDocs/Hardware].


=== Hardware hacking ===

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
----
CategoryModel
