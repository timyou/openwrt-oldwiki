#pragma section-numbers off

||<tablebgcolor="#f1f1ed" tablewidth="40%" tablestyle="FONT-SIZE: 0.9em; FLOAT: right; MARGIN: 0pt 0pt 1em 1em"style="PADDING-RIGHT: 0.5em; PADDING-LEFT: 0.5em; PADDING-BOTTOM: 0.5em; PADDING-TOP: 0.5em">[[TableOfContents]]||

= Linksys WRT160N =

The Linksys WRT160N is the Linksys Ultra Range Plus Wireless-N Broadband Router. It runs Linux out of the box. The source code tarball is available from the [http://www.linksys.com/servlet/Satellite?c=L_Content_C1&childpagename=US%2FLayout&cid=1115416836002&pagename=Linksys%2FCommon%2FVisitorWrapper Linksys GPL Code Center]

OpenWRT will run on WRT160N v1.1. Please see what version you have and add information to the wiki or post in this [http://forum.openwrt.org/viewtopic.php?id=15321 forum thread]. It is not directly supported by any pre-built firmware images on the download page yet, You need to [http://wiki.openwrt.org/OpenWrtDocs/Hardware/Linksys/WRT160N#head-6bc46006cdfb30edaf9f048ef09ad1250a2aee2d compile it yourself] or try an image from [http://snipes420.googlepages.com/ Here].

'''NOTE:''' The wireless part is only supported on the 2.4 Kernel version of Kamikaze. The 2.6 Kernel runs fine on the box, but (because the wl.o driver from Broadcom is only available for 2.4 Kernels and the opensource b43 driver is not ready yet) the wireless does not work if you flash a image with a 2.6 Kernel. 802.11N is not supported until the upstream provider can support it.

Please update this wiki page if this information is proven false or further support is added.

Link to Product info page at linksys.com -> [http://www.linksys.com/servlet/Satellite?c=L_Product_C2&childpagename=US%2FLayout&cid=1175239516849&pagename=Linksys%2FCommon%2FVisitorWrapper WRT160N Product_Page]

= Supported Versions =

According to Wikipedia there is more than one version of this device. [http://en.wikipedia.org/wiki/Linksys_WRT300N_series#WRT160N Reference]

Please add info here if you can.

||'''Model''' ||'''CPU''' ||'''Wireless''' ||'''Flash''' ||'''RAM''' ||'''S/N''' ||'''!OpenWrt Kamikaze''' ||
||WRT160N v1.0 ||? ||? ||4MB ||32MB || ? || X ||
||WRT160N v1.1 || BCM4703||BCM4321 ||4MB ||16MB ||CSE01 || X (See Below)||
||WRT160N v2.0 ||? ||? || ||? ||CSE11 || X ||


= Hardware =

== Info ==

||<tablestyle="FLOAT: right; margin: -15px 0 0 0; padding: 0;">attachment:wrt160N_CPU_systeminfo_.jpg||

||'''Architecture''' ||MIPS ||
||'''Vendor''' ||Broadcom ||
||'''Bootloader''' ||CFE ||
||'''System-On-Chip'''||Broadcom 4703KFBG||
||'''CPU Speed''' ||266 Mhz ||
||'''Flash size''' ||4 MiB ||
||'''RAM''' ||16 MiB ||
||'''Wireless''' ||Broadcom BCM4321 802.11b/g/n Wireless LAN (integrated) ||
||'''Ethernet''' ||Switch in CPU ||
||'''USB''' ||No ||
||'''Serial'''||Yes ||

== Chips on the PCB ==

 * CPU - BCM4703 [http://www.broadcom.com/collateral/pb/4703_4704-PB00-R.pdf Product_Brief] (the original linksys firmware calls it a BCM4704 in /proc/cpuinfo)

 * BCM5325 [http://www.broadcom.com/collateral/pb/5325-PB05-R.pdf Product_Brief]

 * Flashchip - EN29LV320AB [http://www.eonsdi.com/pdf/EN29LV320.pdf Data Sheet]

 * BCM4321 [http://www.broadcom.com/collateral/pb/4321_2055-PB02-R.pdf Product_Brief]

 * BCM2055 (under the shield) [http://www.broadcom.com/collateral/pb/4321_2055-PB02-R.pdf Product_Brief]

== Pads on PCB ==

There is 3 sets of pads on the PCB of the WRT160N.

JP1 and JP3 seem to be missing some surface mount components so may not actually work. 
Half of the JP1 and JP3 pads are on the reverse side of the PCB.

JP2 works if you use a 3.3v TTL to RS-232.

'''JP1'''
|| On Reverse ||'''Pad 2''' ||GND ||'''Pad 4''' ||GND ||'''Pad 6''' ||GND ||'''Pad 8''' ||GND ||'''Pad 10''' ||GND ||'''Pad 11''' || ? ||
|| On Front ||'''Pad 1''' || ? ||'''Pad 3''' || ? ||'''Pad 5''' || ? ||'''Pad 7''' || ? ||'''Pad 9''' || ? ||'''Pad 12''' || ? ||

'''JP2'''

3.3v TTL Serial
|| On Front ||'''Pad 1''' || 3.3v ||'''Pad 2''' || TX ||'''Pad 3''' || RX ||'''Pad 4''' || Not Connected ||'''Pad 5''' || GND ||

'''JP3'''
|| On Reverse ||'''Pad 2''' ||GND ||'''Pad 4''' ||GND ||'''Pad 6''' ||GND ||'''Pad 8''' ||GND ||'''Pad 10''' ||GND ||'''Pad 11''' || ? ||
|| On Front ||'''Pad 1''' || ? ||'''Pad 3''' || ? ||'''Pad 5''' || ? ||'''Pad 7''' || ? ||'''Pad 9''' || ? ||'''Pad 12''' || ? ||

== JTAG Port ==

Not yet documented.

== Serial Ports ==

JP2 is a 3.3v serial port.  Boot messages can be seen if you connect a 3.3v level shifter here and monitor with a serial port. 

DO NOT CONNECT DIRECTLY TO A PC SERIAL PORT. Use a 3.3v TTL level shifter. 
Details at this page:
 * http://wiki.openwrt.org/OpenWrtDocs/Customizing/Hardware/Serial_Console

== Boot Messages ==

 * Boot messages from original Linksys firmware are [http://wiki.openwrt.org/OpenWrtDocs/Hardware/Linksys/WRT160N/BootMessages here]
 * Boot messages from DD-WRT v24 [http://wiki.openwrt.org/OpenWrtDocs/Hardware/Linksys/WRT160N/BootMessages-DD-WRT_v24 here]
 * Boot messages from OpenWRT Trunk 8-17-2008 [http://wiki.openwrt.org/OpenWrtDocs/Hardware/Linksys/WRT160N/BootMessages-OpenWRT-Trunk_8-17-2008 here]
 * Boot messages from OpenWRT Trunk 8-19-2008 [http://wiki.openwrt.org/OpenWrtDocs/Hardware/Linksys/WRT160N/BootMessages-OpenWRT-Trunk_8-19-2008+options1 here] Adding some kernel options makes the flash appear in the boot messages.
 * Boot messages from OpenWRT Trunk Rev12360 [http://wiki.openwrt.org/OpenWrtDocs/Hardware/Linksys/WRT160N/BootMessages-OpenWRT-Trunk_Rev12360+options1 here] Adding some kernel options makes the flash appear in the boot messages and boot correctly.
 * Boot messages from OpenWRT Trunk Rev12360 [http://wiki.openwrt.org/OpenWrtDocs/Hardware/Linksys/WRT160N/BootMessages-OpenWRT-Trunk_Rev12360+options2 here] Adding some kernel options makes the flash appear in the boot messages, wireless appears to detect correctly and boots to a shell.

= Installation =

== How To Build ==

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

= Linksys WRT160N specific configuration =

== NVRAM ==

|| '''boardtype''' || 0x0472 ||
|| '''boardnum''' || 42 ||
|| '''boardflags''' || 0x0010 ||

== TODO ==

 * Find the data sheets for the chips used in this device.
 * Figure out what JP1, JP3 are for and the exact pin outs.

== Other Categories this device is in ==

 . Category80211nDevice
 . CategoryNotSupported
