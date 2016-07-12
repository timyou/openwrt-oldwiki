## Please add only OpenWrt and WRT54G related things to this page! Thanks.
= Linksys WRT54G =
There are currently many versions of the WRT54G. With the exception of v5 devices the WRT54G units are supported by OpenWrt 1.0 (White Russian) and later. The version number is found on the label on the bottom of the front part of the case below the Linksys logo.

Some consider the ["L"] and ["3G"] versions of this model.

{{{boot_wait}}} is '''off''' by default on these routers, so you should turn it on, see OpenWrtDocs/BootWait.

== Identification by S/N ==
Useful for identifying shrinkwrapped units. The '''S/N''' can be found on the box, below the UPC barcode.
||||<style="text-align: center;"> (!) '''Please contribute to this list.''' (!) ||||<style="text-align: center;">'''!OpenWrt''' ||
||'''Model''' || '''S/N Prefix''' ||  '''Stable[[BR]]White Russian''' ||  '''Development[[BR]]Kamikaze''' ||
||WRT54G v1.0 || CDF0 or CDF1 || (./) || (./) ||
||WRT54G v1.1 || CDF2 or CDF3 or CDF4 || (./) || (./) ||
||WRT54G v2 || CGN10 (Canada)/CDF5 || (./) || (./) ||
||WRT54G v2.2 || CDF7 || (./) || (./) ||
||WRT54G v3 || CDF8 || (./) || (./) ||
||WRT54G v3.1 (AU?, DE, and UK) || CDF9 || (./) || (./) ||
||WRT54G v4 || CDFA || (./) || (./) ||
||WRT54G v5 * || CDFB || (./) || {X} ||
||WRT54G v5.1* || CDFC || (./) || {X} ||
||WRT54G v6 * ||CDFD || (./) || {X} ||


*Works without requiring a JTAG interface, but requires slightly more work to install than a WRT54G v1-4 or WRT54GL

=== WRT54G v1.0 ===
The WRT54G v1.0 is based on the Broadcom 4710 board. It has a 125 MHz CPU, 4 MB flash and 16 MB SDRAM. The wireless NIC is a mini-PCI card. The switch is an ADM6996. Resetting to factory defaults via reset button or mtd erase nvram is '''not safe''' on this unit.

=== WRT54G v1.1 ===
The WRT54G v1.1 is based on the Broadcom 4710 board. It has a 125 MHz CPU, 4 MB flash and 16 MB SDRAM. The wireless NIC is soldered to the board. The switch is an ADM6996. Resetting to factory defaults via reset button or mtd erase nvram is '''not safe''' on this unit.

=== WRT54G v2.0 ===
The WRT54G v2.0 is based on the Broadcom 4712 board. It has a 200 MHz CPU, 4 MB flash and 16 MB SDRAM. The wireless NIC is integrated to the board. The switch is an ADM6996. Resetting to factory defaults via reset button or mtd erase nvram is '''safe''' on this unit.

=== WRT54G v2.2 ===
The WRT54G v2.2 is based on the Broadcom 4712 board. It has a 200 MHz CPU, 4 MB flash and 16 MB DDR-SDRAM. The wireless NIC is integrated to the board. The switch is a BCM5325. Resetting to factory defaults via reset button or mtd erase nvram is '''safe''' on this unit.

=== WRT54G v3.0 & WRT54G v3.1 ===
This unit is just like v2.2 except it has an extra button on the left front panel behind a Cisco logo. This button can be illuminated by either a yellow (amber?) or white LED, and is used for the "Secure Easy Setup" encryption setup feature. Resetting to factory defaults via reset button or mtd erase nvram is '''safe''' on this unit.

To remove the front cover from a v3.1, you must first remove the small screws under the rubber covers of the front feet! The 3.1 model was also sold at least in limited numbers within the US (S/N table appears to state otherwise). ~~~

If you have such a thing you can try  http://192.168.1.1/Cysaja.asp to identify

There is "Module Name=WRT54G; Firmware Version=v4.01.1,..." or something like that.

This board has a BCM3302 processor, revision 0.7.

=== WRT54G v4.0 ===
New more integrated board layout ([http://www.linksysinfo.org/modules.php?name=Content&pa=showpage&pid=6#wrt54g4 photos here]), switch is now in SoC.

To remove the front cover from this unit you simply pop the front of the case off after removing the antennas. There are no screws! Resetting to factory defaults via reset button or mtd erase nvram is '''safe''' on this unit.

This board has a BCM3302 processor, revision 0.8.

=== WRT54G v5, v5.1, and v6 ===
This version has switched to a proprietary non-Linux OS (WikiPedia:VxWorks). It has less flash (2 MB) and less RAM (8 MB). The WRT54G V5 is not officially supported, but a flashing procedure has been developed that will allow you to load a micro OpenWrt installation onto this device. For it to be of much use, packages must be pre-included in the squashfs filesystem image. For more information, see: [http://www.bitsum.com/openwiking/owbase/ow.asp?WRT54G5_CFE http://www.bitsum.com/openwiking/owbase/ow.asp?WRT54G5%5FCFE] .

The flashing procedure linked to above utilizes the capability of the VxWorks boot loader to flash over itself to upload a proper CFE on this unit that then allows flashing a 'normal' TRX firmware image.

=== Table summary ===
How to get info:

 * board info: {{{nvram show | grep board | sort}}}[[BR]]
 * cpu model: {{{grep cpu /proc/cpuinfo}}}
||'''Model''' ||'''boardrev''' ||'''boardtype''' ||'''boardflags''' ||'''boardflags2''' ||'''boardnum''' ||'''wl0_corerev''' ||'''cpu model''' ||'''boot_ver''' ||'''pmon_ver''' ||
||WRT54G v1.0 ||-- ||  bcm94710dev ||      - ||-- ||  42 ||       4 || BCM4710 V0.0 ||  v1.0 ||  3.11.30.5 ||
||WRT54G v1.1 ||-- ||  bcm94710dev ||      - ||-- ||  42 ||       5 || BCM4710 V0.0 || v1.5 || 3.31.15.0 ||
||WRT54G v2.0 || 0x10 ||  0x0101 ||  0x0188 ||  0 ||  42 ||       - || BCM3302 V0.7 ||  v2.1, v2.3 ||  3.51.21.0 ||
||WRT54G v2.2 || 0x10 || 0x0708 || 0x0118 || 0 || 42 ||       7 || BCM3302 V0.7 ||  v3.4 ||  3.61.13.0 ||
||WRT54G v3.0 || 0x10 || 0x0708 || 0x0118 || 0 || 42 ||       7 || BCM3302 V0.7 ||-- ||-- ||
||WRT54G v3.1 (AU?) || 0x10 ||  0x0708 ||  0x0118 ||  0 ||  42 ||       7 || BCM3302 V0.7 ||-- ||-- ||
||WRT54G v4.0 || 0x10 ||  0x0467 ||  0x2558 ||  0 ||  42 ||       7 || BCM3302 V0.8 ||v3.6 ||       - ||
||WRT54G v5.0 || 0x13 || 0x0467 ||  0x2558 ||  0 ||42 ||       7 || BCM3302 V0.8 ||-- ||-- ||
||WRT54G v5.1 || 0x13 || 0x0467 ||  0x2558 || 0 ||42 ||       7 || BCM3302 V0.8 ||-- || 3.90.7.0 ||
||WRT54G v6.0 || 0x13 || 0x0467 ||  0x2558 ||  0 ||42 ||       7 || BCM3302 V0.8 ||-- ||-- ||
WARNING: WRT54G v5.0, v5.1, and v6.0 board flags shown above may not be accurate because the CFE used to enable flashing to Windows is actually a modified WAP54Gv3 CFE, and depending on the version of the vxworks_killer used, the boardflags and other nvram variables may be different.

Other NVRAM variables of interest :  firmware_version, os_version

Please complete this table. Look at the [http://openwrt.org/forum/viewtopic.php?pid=8127#p8127 Determining WRT54G/GS model using nvram variables] thread. May be this table should move up to ["OpenWrtDocs/Hardware"].

== Overclocking ==
These models can be overclocked, though it should not be done if you don't have a JTAG cable to recover in case things go horribly wrong.

=== Why overclock? ===
'''The argument for:'''

Even if your processor average load is low, this doesn't mean you won't benefit from overclocking. A load average is an average use over a period of time. However, at any given time a processor is either actively executing pertinent code or its not. So at any given moment it's all or none. This means that, in theory, operations can be sped up in cases where the CPU is the bottleneck.

One example is that those users who've added SD card mods to their WRT54G/S see gains in I/O speed proportional to the CPU/SB clock speed. Furthermore, webif, scripts, and everything CPU or memory dependent should run proportionally faster to the amount the CPU/SB clock is increased.

Even Linksys overclocked the WRT54GS v2.x to 216mhz to fix a bug with the system memory, so clearly it's not such a risk to overclock these boxes. Since they have a set of frequencies they are allowed to run at, one wonders if Broadcom hasn't designed them to run at these frequencies when proper cooling is applied.

Most importantly though, why not overclock these units if they run perfectly stable when overclocked? With proper cooling mods these processors can run fine even at their maximum frequencies (depending on the CPU).

'''The argument against: '''

Most people aren't doing things with their WRT54G/S that will be substantially affected by increases in CPU/SB clock speed, so why risk the stability of your box by overclocking it?

=== Overclocking for the v4 and v5 ===
The WRT54G v4 and WRT54G v5 are different from the v2 and v3 models in that they have a BCM5352/BCM3302 revision v0.8 (instead of v0.7). This processor defaults to 200mhz with an sbclock setting of 100mhz. The highest valid CPU frequency for this processor is 250mhz, which yields an sbclock frequency of 125mhz.

Although the v4 and v5 will boot up to frequencies greater than 250mhz (for example, 252 mhz), the CPU clock frequency will actually only be set to its default clock frequency. The nvram variables will not have changed, so some firmwares (i.e. DD-WRT) may mis-report the clock frequency.

To determine the actual clock frequency, use 'cat /proc/cpuinfo' or examine the first few lines of the output from 'dmsg'.

Although it is common practice to set the nvram clkfreq variable so that it includes the sbclock setting, the sbclock is actually ignored for this processor revision since it has a locked CPU/SB clock ratio. For example, clkfreq=240,126 actually ends up with an sbclock setting of 120mhz, since 126mhz is not in a valid ratio with a CPU clock frequency of 240mhz. Therefore, it is recommended to not set the sbclock value (the number after the ',').

Users wishing to set their WRT54G v4 or WRT54G v5 to its maximum clock frequency should execute these commands at the terminal

{{{
nvram set clkfreq=250
nvram commit
reboot }}}
==== Valid BCM5352/BCM3302 r0.8 (WRT54G v4 and v5) Frequencies ====
||__'''CPU'''__ ||__'''SB'''__ || __'''Note'''__ ||
||183 ||92 || ||
||187 ||94 || ||
||198 ||98 || ||
||200 ||100 ||default ||
||216 ||108 || ||
||225 ||113 || ||
||233 ||116 || ||
||237 ||119 || ||
||250 ||125 || ||
==== Overclocking Experiences ====
1.) I've had a WRT54G v4 running at the maximum valid frequency of 250mhz for a couple weeks with no stability problems. I do have a heat-sink (though not a very good one since it only partially covers the CPU) and a fan installed internally. The box ends up running quite cool. 2.) I've had a WRT54G v5 running at 240mhz for a couple weeks with no stability problems. It has a heat-sink but no fan. It does get pretty hot. 250mhz seemed to be less stable after the unit heated up. A fan addition should allow the v5 to run as well as the v4 mentioned above at 250mhz.

==== Recovery From a Bad Overclock ====
The CFE of these units handles overclocking very well and will simply reject values greater than 250mhz and find a closest match to values less than or equal to 250mhz. Therefore, it is unlikely you'll brick your router. However, be careful just in case you have a different CFE or this information is incorrect!

If things do go wrong, the WRT54G v4 and WRT54G v5 do reset the clkfreq variable to the default of 200mhz when the reset button is held down for a few seconds. Other versions with different CFEs may not do this.

If the clock frequency results in an unstable processor, there may be only a few seconds to initiate a JTAG based nvram erase.

'''TIP''': If you do overclock and find your router becomes too unstable to login and reset the clock frequency, this hack may save you. The usual disclaimers apply.

First, take the router out of it's case. Place it on a non-conductive surface where you can work on it and still have it connected to your network and power, as well as near a computer which you can use to SSH into it.

Next, get yourself an ice pack. It must be flexible. I used the plastic bag type filled with a gel. Freeze the pack until it reaches your freezer temp.

Now take the bag out and place it in a heavy duty plastic freezer bag. Lay the bag on top of the now bare router motherboard making sure it presses flat on the processor (see the HW guide). Wait a few minutes until the bottom of the motherboard feels cool. Next place a small weight on top of the gel pack to hold it to the board while you work. I used the power brick from my laptop. Make sure your network cable is connected and plug the power into the router. Wait until it has booted and try SSH'ing into it from your computer. If you are lucky, this homebrew cooling hack will allow the router's CPU to run long enough to let you reset the CPU clock using the following commands:

{{{
nvram set clkfreq=<default MHZ>
nvram commit
reboot
}}}
If you are lucky, your router is now back to normal.

'''Note''': I have only used this once on a WRT54G V2 that was clocked to 240MHz. Other models and overclock speeds may not respond to this hack. Good luck.

=== Overclocking for the v2, v2.2, and v3 ===
Other models use the commonly documented clock frequencies, with a max CPU clock of 300mhz. They do not appear to have CFEs that will prevent the clock from being set to invalid frequencies, or that recover to default clkfreq via a nvram reset. Be even more careful with these versions of the WRT54G.

==== Valid BCM5352/BCM3302 r0.7 Frequencies (WRT54G v2 - v3) ====
||__'''CPU'''__ ||__'''SB'''__ || __'''Note'''__ ||
||192 ||96 || ||
||200 ||100 || default ||
||216 ||108 || ||
||228 ||114 || ||
||240 ||120 || ||
||252 ||126 || ||
||264 ||132 || ||
||280 ||120 || ||
||300 ||120 || ||
=== Overclocking for the v1 ===
This processor runs at 125mhz by default. Overclocking is reported to not be possible, but this has not been confirmed.

== Hardware hacking ==
=== Opening the case ===
==== WRT54G v1.0 ====
Check [http://www.servomagazine.com/forum/viewtopic.php?p=34263&sid=821e1885f8c530e26278d85d701631ff here] for instructions and [http://seattlewireless.net/~mattw/photos/linksyswrt54g/gallery/ here] for pictures. A 9/16 socket wrench or similar tool can be used to remove the antenna.

==== WRT54G v3.1 and later ====
Check [http://www.byteclub.net/wiki/Wrt54g#Opening_the_case here] for instructions.

=== Serial Ports ===
Most (all?) versions of this model have an unpopulated 10-pin header that exposes two serial ports. The pins are defined as:
||Pin 1 ||3.3V ||Pin 2 ||3.3V ||
||Pin 3 ||Tx (ttyS1) ||Pin 4 ||Tx (ttyS0) ||
||Pin 5 ||Rx (ttyS1) ||Pin 6 ||Rx (ttyS0) ||
||Pin 7 ||NC ||Pin 8 ||NC ||
||Pin 9 ||GND ||Pin 10 ||GND ||


The CFE and OpenWRT use ttyS0 to emit boot and log messages. OpenWRT offers shell acess through ttyS0 by simply pressing <ENTER> to activation the console.

The serial port settings are 115k, 8, N, 1 with no flow control.

For more info see http://www.rwhitby.net/wrt54gs/serial.html.

=== JTAG ===
A 12-pin unpopulated JTAG header is included on all versions of this router. It is usually found beside the serial port headers.

A simple unbuffered JTAG cable works fine. See HairyDairyMaid's WRT54G Debricking Tool for pin defintions, cable schematics, and software to utilize the JTAG interface.

=== WRT54G v2.0 revision XH RAM Increase ===
There are revision XH units of the WRT54G v2.0. These units have 32 MB of memory, but they are locked to 16 MB. You can unlock the remaining memory with changing some of the variables. Afterburner (aka. Speedbooster) mode can be enabled with some variables, too.

/!\ '''NOTE:''' However, there are no guaranties that these will work, and changing the memory configuration on a non-XH unit will give you a brick. Check the forums for more info.

=== SES Button ===
The SES Button was introduced in the WRT54G v3.0, though a firmware upgrade for the WRT54G v2.0 enabled it for that version too.

If you have a look at the WRT54G v2.2 board, you can find on the left corner, near the power LED, an empty place for a 4 pins button. On the board it is printed as SW2. This is the SES button you can find on WRT54G v3.0 and above, except that it has not been soldered.

----
 . CategoryModel
