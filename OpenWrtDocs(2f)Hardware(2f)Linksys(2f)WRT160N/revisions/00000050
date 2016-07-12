#pragma section-numbers off

||<tablebgcolor="#f1f1ed" tablewidth="40%" tablestyle="FONT-SIZE: 0.9em; FLOAT: right; MARGIN: 0pt 0pt 1em 1em"style="PADDING-RIGHT: 0.5em; PADDING-LEFT: 0.5em; PADDING-BOTTOM: 0.5em; PADDING-TOP: 0.5em">[[TableOfContents]]||

= Linksys WRT160N =

The Linksys WRT160N is the Linksys Ultra Range Plus Wireless-N Broadband Router. It runs Linux out of the box. The source code tarball is available from the [http://www.linksys.com/servlet/Satellite?c=L_Content_C1&childpagename=US%2FLayout&cid=1115416836002&pagename=Linksys%2FCommon%2FVisitorWrapper Linksys GPL Code Center]

OpenWRT will run on WRT160N v1.1.  It is not directly supported by any pre-built firmware images on the download page yet, You need to [http://wiki.openwrt.org/OpenWrtDocs/Hardware/Linksys/WRT160N#head-6bc46006cdfb30edaf9f048ef09ad1250a2aee2d compile it yourself] or try an image from [http://snipes420.googlepages.com/ Here].

'''NOTE:''' The device only supports the 2.4 Kernel version of Kamikaze. We need to figure out the correct kernel configuration to support the flash chip on the 2.6 Kernel. At this point in time the wl.o binary driver from Broadcom is only available for 2.4 Kernels and the opensource b43 driver is not ready yet. As such the wireless does not work if you flash a image with a 2.6 Kernel. 802.11N is not supported until the upstream provider can support it.

Please update this wiki page if this information is proven false or further support is added.

Link to Product info page at linksys.com -> [http://www.linksys.com/servlet/Satellite?c=L_Product_C2&childpagename=US%2FLayout&cid=1175239516849&pagename=Linksys%2FCommon%2FVisitorWrapper WRT160N Product_Page]

= Supported Versions =

Please see what version you have and add information to the wiki or post in this [http://forum.openwrt.org/viewtopic.php?id=15321 forum thread].

According to Wikipedia there is more than one version of this device. [http://en.wikipedia.org/wiki/Linksys_WRT300N_series#WRT160N Reference]

DD-Wrt [http://www.dd-wrt.com/wiki/index.php/Supported_Devices#Linksys Devices list] also mentions more than one.

Please add/confirm info here if you can.

||'''Model''' ||'''CPU''' ||'''Wireless''' ||'''Flash''' ||'''RAM''' ||'''S/N''' ||'''FCC ID''' ||'''!OpenWrt Kamikaze''' ||
||WRT160N v1.0 ||? ||? ||4MB ||32MB || ? || || X ||
||WRT160N v1.1 || BCM4703||BCM4321 ||4MB ||16MB ||CSE01 ||Q87WRT160N || X (See Below)||

---- /!\ '''Edit conflict - other version:''' ----
||WRT160N v2.0 || RT2880F||Ralink || 4MB ||16MB ||CSE11 ||Q87WRT160NV2 || not supported ||



---- /!\ '''Edit conflict - your version:''' ----
||WRT160N v2.0 || RT2880F||Ralink || 4MB ||16MB ||CSE11 ||Q87WRT160NV2 || not supported ||



---- /!\ '''End of edit conflict''' ----


= Hardware =

== Info ==

||<tablestyle="FLOAT: right; margin: -15px 0 0 0; padding: 0;">attachment:wrt160N_CPU_systeminfo_.jpg||

||'''Version''' ||1.0/1.1 || 2.0||
||'''Architecture''' ||MIPS || MIPS ||
||'''Vendor''' ||Broadcom || Ralink ||
||'''Bootloader''' ||CFE || U-Boot ||
||'''System-On-Chip'''||Broadcom 4703KFBG|| RT2880 Soc ||
||'''CPU Speed''' ||266 Mhz || 266 Mhz ||

---- /!\ '''Edit conflict - other version:''' ----
||'''Flash size''' ||4 MiB || 32 MiB ||
||'''RAM''' ||32/16 MiB || 128 Mib ||

---- /!\ '''Edit conflict - your version:''' ----
||'''Flash size''' ||4 MiB || 32 MiB ||
||'''RAM''' ||32/16 MiB || 128 Mib ||

---- /!\ '''End of edit conflict''' ----
||'''Wireless''' ||Broadcom BCM4321 802.11b/g/n Wireless LAN (integrated) || RT2880 Soc ||
||'''Ethernet''' ||Switch in CPU || - ||
||'''USB''' ||No || - ||
||'''Serial'''||Yes || Yes ||

== Chips on the PCB ==

=== V1.0/1.1 ===
 * CPU - BCM4703 [http://www.broadcom.com/collateral/pb/4703_4704-PB00-R.pdf Product_Brief] (the original linksys firmware calls it a BCM4704 in /proc/cpuinfo)

 * BCM5325 [http://www.broadcom.com/collateral/pb/5325-PB05-R.pdf Product_Brief]


---- /!\ '''Edit conflict - other version:''' ----
 * Flashchip - EN29LV320AB.  This device is capable of operating in 8-bit or 16-bit mode. [http://www.eonsdi.com/pdf/EN29LV320.pdf Data Sheet]

---- /!\ '''Edit conflict - your version:''' ----
 * Flashchip - EN29LV320AB.  This device is capable of operating in 8-bit or 16-bit mode. [http://www.eonsdi.com/pdf/EN29LV320.pdf Data Sheet]

---- /!\ '''End of edit conflict''' ----

 * BCM4321 [http://www.broadcom.com/collateral/pb/4321_2055-PB02-R.pdf Product_Brief]

 * BCM2055 (under the shield) [http://www.broadcom.com/collateral/pb/4321_2055-PB02-R.pdf Product_Brief]

=== V2.0 ===


---- /!\ '''Edit conflict - other version:''' ----
There has been a lot of discussion about what exactly is on this board, and a lot of complaints about it having reduced memory.  The messages appear to be mixed, what's presented here is as accurate as possible.

 * CPU: RaLink RT2880F [http://www.ralinktech.com.tw/data/RT2880.pdf Product_brief]

 * CPU speed is reported by users as 266 MHz.  However, when the stock (linksys) kernel boots, it reports the speed as 133 MHz.  The manufacturer describes the core as 266 MHz.

 * CPU Core is MIPS4Kec with 16K instruction, 16K data caches

 * RTL8306SD - a 6-port fast ethernet switch with five integrated physical layer 10BaseT/100BaseT transceivers

 * RAM is provided by two WindBond EN29LV320AB-70TCP SDRAMS.  Each chip is 1 MB x 4 BANKS x 16 BITS for a total of 64MBits per chip, or 128MBits total = 16 megabytes.  This is confirmed by the stock kernel boot messages.

 * Flashchip - first reported on this wiki as a Samsung 813; K8P3215UQB.  However, the most recent version 2 board shipped has one EON Silicon EN29LV320AB, which is a 32 megabit (configurable as 4MB x 8 or 2MB x 16) chip.

---- /!\ '''Edit conflict - your version:''' ----
There has been a lot of discussion about what exactly is on this board, and a lot of complaints about it having reduced memory.  The messages appear to be mixed, what's presented here is as accurate as possible.

 * CPU: RaLink RT2880F [http://www.ralinktech.com.tw/data/RT2880.pdf Product_brief]

 * CPU speed is reported by users as 266 MHz.  However, when the stock (linksys) kernel boots, it reports the speed as 133 MHz.  The manufacturer describes the core as 266 MHz.

 * CPU Core is MIPS4Kec with 16K instruction, 16K data caches

 * RTL8306SD - a 6-port fast ethernet switch with five integrated physical layer 10BaseT/100BaseT transceivers

 * RAM is provided by two WindBond EN29LV320AB-70TCP SDRAMS.  Each chip is 1 MB x 4 BANKS x 16 BITS for a total of 64MBits per chip, or 128MBits total = 16 megabytes.  This is confirmed by the stock kernel boot messages.

 * Flashchip - first reported on this wiki as a Samsung 813; K8P3215UQB.  However, the most recent version 2 board shipped has one EON Silicon EN29LV320AB, which is a 32 megabit (configurable as 4MB x 8 or 2MB x 16) chip.

---- /!\ '''End of edit conflict''' ----

== Pads/headers on PCB ==

=== V1.0/1.1 ===

There is 3 sets of pads on the PCB of the WRT160N.
 
Half of the JP1 and JP3 pads are on the reverse side of the PCB.
JP1 is the JTAG port.
JP2 is a serial port and it works if you use a 3.3v TTL to RS-232.

'''JP1'''

JTAG
|| On Reverse ||'''Pad 2''' ||GND ||'''Pad 4''' ||GND ||'''Pad 6''' ||GND ||'''Pad 8''' ||GND ||'''Pad 10''' ||GND ||'''Pad 12''' || ? ||
|| On Front ||'''Pad 1''' || RESET# ||'''Pad 3''' || TDI ||'''Pad 5''' || TD0 ||'''Pad 7''' || TMS ||'''Pad 9''' || TCK ||'''Pad 11''' || GND ||

# Reset# of Flash Memory

'''JP2'''

3.3v TTL Serial
|| On Front ||'''Pad 1''' || 3.3v ||'''Pad 2''' || TX ||'''Pad 3''' || RX ||'''Pad 4''' || Not Connected ||'''Pad 5''' || GND ||

'''JP3'''
|| On Reverse ||'''Pad 2''' ||GND ||'''Pad 4''' ||GND ||'''Pad 6''' ||GND ||'''Pad 8''' ||GND ||'''Pad 10''' ||GND ||'''Pad 11''' || ? ||
|| On Front ||'''Pad 1''' || ? ||'''Pad 3''' || ? ||'''Pad 5''' || ? ||'''Pad 7''' || ? ||'''Pad 9''' || ? ||'''Pad 12''' || ? ||

=== V2.0 ===


---- /!\ '''Edit conflict - other version:''' ----
J10 is an empty 5-pin header, and is likely a serial port (console)

J11 is an empty 14-pin header and is likely a JTAG port to the CPU.

---- /!\ '''Edit conflict - your version:''' ----
J10 is an empty 5-pin header, and is likely a serial port (console)

J11 is an empty 14-pin header and is likely a JTAG port to the CPU.

---- /!\ '''End of edit conflict''' ----

'''J10'''

||'''Pin 1''' || ? ||'''Pin 2''' || ? ||'''Pin 3''' || ? ||'''Pin 4''' || ? ||'''Pin 5''' || ? ||

'''J11'''

||'''Pin 1''' || ? ||'''Pin 3''' || ? ||'''Pin 5''' || ? ||'''Pin 7''' || ? ||'''Pin 9''' || ? ||'''Pin 11''' || ? ||'''Pin 13''' || ? ||
||'''Pin 2''' || ? ||'''Pin 4''' || ? ||'''Pin 6''' || ? ||'''Pin 8''' || ? ||'''Pin 10''' || ? ||'''Pin 12''' || ? ||'''Pin 14''' || ? ||


== JTAG Port ==

The JTAG software needs to support 8-bit operation.

tjtag v3-RC1 by Tornado can be used to read the flash chip. Get it from [http://www.dd-wrt.com/dd-wrtv2/down.php?path=downloads%2Fothers%2Ftornado%2Fjtag%2Ftjtagv3-RC-1/ here].
 
Reference [http://www.dd-wrt.com/phpBB2/viewtopic.php?p=243652#243652 Here]

== Serial Ports ==

JP2 is a 3.3v serial port.  Boot messages can be seen if you connect a 3.3v level shifter here and monitor with a serial port. 

DO NOT CONNECT DIRECTLY TO A PC SERIAL PORT. Use a 3.3v TTL level shifter. 
Details at this page:
 * http://wiki.openwrt.org/OpenWrtDocs/Customizing/Hardware/Serial_Console

== Boot Messages ==

=== V1.1 ===

 * Boot messages from original Linksys firmware are [http://wiki.openwrt.org/OpenWrtDocs/Hardware/Linksys/WRT160N/BootMessages here]
 * Boot messages from DD-WRT v24 [http://wiki.openwrt.org/OpenWrtDocs/Hardware/Linksys/WRT160N/BootMessages-DD-WRT_v24 here]
 * Boot messages from OpenWRT Trunk 8-17-2008 [http://wiki.openwrt.org/OpenWrtDocs/Hardware/Linksys/WRT160N/BootMessages-OpenWRT-Trunk_8-17-2008 here]
 * Boot messages from OpenWRT Trunk 8-19-2008 [http://wiki.openwrt.org/OpenWrtDocs/Hardware/Linksys/WRT160N/BootMessages-OpenWRT-Trunk_8-19-2008+options1 here] Adding some kernel options makes the flash appear in the boot messages.
 * Boot messages from OpenWRT Trunk Rev12360 [http://wiki.openwrt.org/OpenWrtDocs/Hardware/Linksys/WRT160N/BootMessages-OpenWRT-Trunk_Rev12360+options1 here] Adding some kernel options makes the flash appear in the boot messages and boot correctly.
 * Boot messages from OpenWRT Trunk Rev12360 [http://wiki.openwrt.org/OpenWrtDocs/Hardware/Linksys/WRT160N/BootMessages-OpenWRT-Trunk_Rev12360+options2 here] Adding some kernel options makes the flash appear in the boot messages, wireless appears to detect correctly and boots to a shell.

=== V2 ===

 * Boot messages from original Linksys 2.0.01 firmware are [http://wiki.openwrt.org/OpenWrtDocs/Hardware/Linksys/WRT160N/BootMessages-linksys_2.0.01 here]

= Installation =

== How To Build ==

=== V1.1 ===
You will need to use a Linux machine with development tools to compile the firmware.
See [https://dev.openwrt.org/browser/trunk/README here] to see what are the dependencies of the buildroot.

1. Get trunk. ie:

{{{
svn checkout https://svn.openwrt.org/openwrt/trunk/ ~/trunk/
}}}

2. Download and apply patch. (This may not be necessary. It only lets the system know it is a WRT160N and not a WRT54G or other type of WRT)

{{{
cd ~/
wget http://snipes420.googlepages.com/openwrt-wrt160n-detection-rev12384.diff
cd ~/trunk/
patch -p0 -i ~/openwrt-wrt160n-detection-rev12384.diff
}}}

3. Enter the configuration menu and change target profile to 'Generic, Broadcom !WiFi (MIMO)', then exit saving changes.

{{{
make menuconfig
}}}

Target Profile ---> (Generic, Broadcom !WiFi (MIMO))

4. build the image once first. (This will take a while)

{{{
make
}}}

5. Enter kernel config options menu.

{{{
make kernel_menuconfig
}}}

6. go to 'Memory Technology Devices (MTD)  --->' 
    then 'RAM/ROM/Flash chip drivers  --->'
and enable 'Support  8-bit buswidth'

7. Exit the configuration menu and save the settings.

8. build the whole thing again with the new config. (This time wont take as long)

{{{
make
}}}

Now you can flash the firmware image in /bin to your WRT160N using the Linksys web interface. (I tried the openwrt-wrt150n-squashfs.bin and it worked; openwrt-brcm-2.4-squashfs.trx also works if using the tftp install method)
 * The wireless works when you enable it in /etc/config/wireless 

= Recovery =

== V1.1 ==
If the device becomes bricked, (and this can happen very easily with this device) you should attach a serial port to it to view the console and see why it has stopped booting. 

Boot_wait does not seem to work on this device. 

One common reason for it to stop booting is, after loading a image that doesn't recognize the 8-bit flash, it will be stuck in a endless reboot loop as seen [http://wiki.openwrt.org/OpenWrtDocs/Hardware/Linksys/WRT160N/BootMessages-OpenWRT-Trunk_8-17-2008 here]. 

Once the serial console is installed you can use a terminal emulator to stop the boot and manually flash a good image to it.

Connect to the device using 115200 baud 8-n-1 and No Flow Control.

press Ctrl + C very early in the boot to break into the CFE prompt.
Enter this command to make the router accept an image via tftp.
{{{
flash -ctheader : flash1.trx
}}}

= Linksys WRT160N specific configuration =

== NVRAM ==

=== V1.1 ===

|| '''boardtype''' || 0x0472 ||
|| '''boardnum''' || 42 ||
|| '''boardflags''' || 0x0010 ||

= TODO =

 * Confirm existence of different versions of this model
 * Figure out what JP3 is for and the exact pin out.

= Other Categories this device is in =

 . Category80211nDevice
 . CategoryNotSupported
