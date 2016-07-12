#pragma section-numbers off
||<tablebgcolor="#f1f1ed" tablewidth="40%" tablestyle="FONT-SIZE: 0.9em; FLOAT: right; MARGIN: 0pt 0pt 1em 1em"style="PADDING-RIGHT: 0.5em; PADDING-LEFT: 0.5em; PADDING-BOTTOM: 0.5em; PADDING-TOP: 0.5em">[[TableOfContents]]||

= Linksys WRT160N =

The Linksys WRT160N is the Linksys Ultra Range Plus Wireless-N Broadband Router.

OpenWRT will run on WRT160N. It is not directly supported by any prebuilt firmware images on the downoad page yet, You need to compile it yourself.

Please update this wiki page if this information is proven false or further support is added.

Link to Product info page at linksys.com -> [http://www.linksys.com/servlet/Satellite?c=L_Product_C2&childpagename=US%2FLayout&cid=1175239516849&pagename=Linksys%2FCommon%2FVisitorWrapper WRT160N Product_Page]

== How To ==

'''''Telnet is working once OpenWRT is installed but to be on the safe side a serial connection is recommended.'''''

1. Get trunk. ie:

{{{
svn checkout https://svn.openwrt.org/openwrt/trunk/ ~/trunk/
}}}

2. Download and apply patch.

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

4. Enter kernel config options menu (this will download the kernel source then open the menu)

{{{
make kernel_menuconfig
}}}

5. go to 'Memory Technology Devices (MTD)  --->' 
    then 'RAM/ROM/Flash chip drivers  --->'
and enable 'Support  8-bit buswidth'

6. Exit the configuration menu and save the settings. [[BR]] Note: When you exit it errors while looking for stuff in staging_dir/host/ (which is not built yet), but it doesn't seem to affect anything. Just continue with step 7.

7. build the whole thing with the new config

{{{
make
}}}

Now you can flash the image in /bin to your WRT160N.

== Hardware Info ==
||<tablestyle="FLOAT: right; margin: -15px 0 0 0; padding: 0;">attachment:wrt160N_CPU_systeminfo_.jpg||

||'''Architecture''' ||MIPS ||
||'''Vendor''' ||Broadcom ||
||'''Bootloader''' ||CFE ||
||'''CPU Speed''' ||266 Mhz ||
||'''Flash size''' ||4 MiB ||
||'''RAM''' ||16 MiB ||
||'''Wireless''' ||Broadcom BCM47xx 802.11b/g/n Wireless LAN (integrated) ||
||'''Ethernet''' ||Switch in CPU ||
||'''USB''' ||No ||

=== Chipset ===

 * CPU - BCM4703 [http://www.broadcom.com/collateral/pb/4703_4704-PB00-R.pdf Product_Brief] (the original linksys firmware calls it a BCM4704 in /proc/cpuinfo)
 * BCM4321 [http://www.broadcom.com/collateral/pb/4321_2055-PB02-R.pdf Product_Brief]
 * BCM5325 [http://www.broadcom.com/collateral/pb/5325-PB05-R.pdf Product_Brief]

=== Flashchip ===

 * EN29LV320AB [http://www.eonsdi.com/pdf/EN29LV320.pdf Data Sheet]

=== Wireless Chip ===

 * BCM2055 (under the shield) [http://www.broadcom.com/collateral/pb/4321_2055-PB02-R.pdf Product_Brief]

=== NVRAM ===

|| '''boardtype''' || 0x0472 ||
|| '''boardnum''' || 42 ||
|| '''boardflags''' || 0x0010 ||

=== Pads on PCB ===

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

=== JTAG Port ===

Not yet documented.

=== Serial Ports ===

JP2 is a 3.3v serial port.  Boot messages can be seen if you connect a 3.3v level shifter here and monitor with a serial port. 

DO NOT CONNECT DIRECTLY TO A PC SERIAL PORT. Use a 3.3v TTL level shifter. 
Details at this page:
 * http://wiki.openwrt.org/OpenWrtDocs/Customizing/Hardware/Serial_Console

=== Boot Messages ===

 * Boot messages from original Linksys firmware are [http://wiki.openwrt.org/OpenWrtDocs/Hardware/Linksys/WRT160N/BootMessages here]
 * Boot messages from DD-WRT v24 [http://wiki.openwrt.org/OpenWrtDocs/Hardware/Linksys/WRT160N/BootMessages-DD-WRT_v24 here]
 * Boot messages from OpenWRT Trunk 8-17-2008 [http://wiki.openwrt.org/OpenWrtDocs/Hardware/Linksys/WRT160N/BootMessages-OpenWRT-Trunk_8-17-2008 here]
 * Boot messages from OpenWRT Trunk 8-19-2008 [http://wiki.openwrt.org/OpenWrtDocs/Hardware/Linksys/WRT160N/BootMessages-OpenWRT-Trunk_8-19-2008+options1 here] Adding some kernel options makes the flash appear in the boot messages.
 * Boot messages from OpenWRT Trunk Rev12360 [http://wiki.openwrt.org/OpenWrtDocs/Hardware/Linksys/WRT160N/BootMessages-OpenWRT-Trunk_Rev12360+options1 here] Adding some kernel options makes the flash appear in the boot messages and boot correctly.
 * Boot messages from OpenWRT Trunk Rev12360 [http://wiki.openwrt.org/OpenWrtDocs/Hardware/Linksys/WRT160N/BootMessages-OpenWRT-Trunk_Rev12360+options2 here] Adding some kernel options makes the flash appear in the boot messages, wireless appears to detect correctly and boots to a shell.

== TODO ==

 * Wireless does not work at all. The device appears as wl0 in iwconfig/ifconfig but trying to scan or connect gives an 'invalid argument' error. 
 * Find the data sheets for the chips used in this device.
 * Figure out what JP1, JP3 are for and the exact pinouts.

== Other Categories this device is in ==

 . Category80211nDevice
 . CategoryNotSupported
