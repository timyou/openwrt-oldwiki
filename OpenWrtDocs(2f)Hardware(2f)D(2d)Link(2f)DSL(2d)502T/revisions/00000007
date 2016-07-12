= Work in Progress =
Porting OpenWrt to the DSL-502T is a work in progress. This page is to assist those working in that direction.

Thanks Strider for starting the page off & thank you nbd + all the openwrt guys for making this work - Z3r0 Kamikaze build 5174 works on the DSL-502T AU & AT

== Specifications ==
ADSL modem with ADSL2 support to 8Mbit/s, it has port 1 LAN port

Flash chip: 4MBytes - Samsung K8D3216UBC a 32Mbit NOR-type Flash Memory organized as 4M x 8

SDRAM: 16Mbytes - Nanya NT5SV8M16DS-6K

CPU: TNETD7300GDU Texas Instruments AR7 MIPS based ''' '''

== How to get OpenWRT onto the router: ==
UPDATE ME: Please see the forum page below

You will need to compile your own firmware, it's simple enough, if you have ubuntu grab build essentials using synaptic and also grab flex, bison and subversion Download the latest trunk using

svn co https://svn.openwrt.org/openwrt/trunk

or get the same revision as myself and use

svn -r 5174 co https://svn.openwrt.org/openwrt/trunk

Enter into the folder and run make menuconfig, select processor as TI AR7 [2.4], quit and save the config.

Run make to download and compile the firmware

 . To flash your new firmware you must first understand how the memory is divided into blocks, with the default DLink firmware it is this:
mtd0 0x90091000,0x903f0000" - filesystem

mtd1 0x90010090,0x90090000" - kernel

mtd2 0x90000000,0x90010000" - bootloader (adam2 mostly)

mtd3 0x903f0000,0x90400000" - configuration mtd4

0x90010090,0x903f0000" - this just covers filesystem/kernel

The default firmware flashes to mtd4 It is divided like so (hex):

0-90 header used by the web interface to verify the firmware is compatible

 90-80FFF kernel with padded 0s at the end

81000-20EFFF filesystem with padded 0s

20F000-20F007 checksum for the entire file made with TICHKSUM (8 Bytes or 16 Hex chars)

But we are flashing OpenWRT to our router and the Openwrt-ar7-2.4-squashfs.bin is set up like this:

Openwrt is usually

0-x kernel

x-eof squashfs

Basically OpenWRT doesn't waste space and where the kernel ends the filesystem starts.

This means you need to change your mtd3 configuration variables so that the mappings are correct and the filesystem can be found by OpenWRT.

Just grab ghex2 (linux) or xvi (windows), open up the firmware and search for the hsq or hsqs this is the start of the squashfs.

In my case this position was 0x000750E0 Now we adjust our mtd variables by setting our IP to 10.8.8.1 and telnetting to 10.8.8.8 21 we do

quote "SETENV mtd0,0x900850E0,0x9003f0000" (fs)

quote "SETENV mtd1,0x90010000,0x900850E0" (kernel)

quote "SETENV mtd4,0x90010000,0x9003f0000" (fs+kernel)

DO NOT CHANGE mtd2 or mtd3 Next we must add a tichksum to our file otherwise the adam2 bootloader will reject it when we try to flash

You just need to get the Source code from DLINK and find the tichksum and perhaps compile it then execute it

 Now you are ready to flash ftp into adam2

quote "MEDIA FLSH"

binary

debug

hash

put "openwrt-ar7-2.4-squashfs.bin" "c mtd4"  (c can be anything)

quote REBOOT

quit

now try to get an IP from the router by using dhclient eth0 or just unsetting IP variables in XP telnet into 192.168.1.1 and you're done :)

== How to Debrick: ==
See the forum for how to debrick the DSL-502T[[BR]]http://forum.openwrt.org/viewtopic.php?id=7742[[BR]]
