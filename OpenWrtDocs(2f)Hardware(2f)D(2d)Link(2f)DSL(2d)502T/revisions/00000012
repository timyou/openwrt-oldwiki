= Work in Progress =
Porting OpenWrt to the DSL-502T is a work in progress. This page is to assist those working in that direction.

Thanks Strider for starting the page off & thank you nbd + all the openwrt guys for making this work - Z3r0

Kamikaze build 5174 works on the DSL-502T AU & AT

Maybe someone can edit this properly and give it some nice formatting :)

== Specifications ==
ADSL modem with ADSL2 support to 8Mbit/s, it has port 1 LAN port

Flash chip: 4MBytes - Samsung K8D3216UBC a 32Mbit NOR-type Flash Memory organized as 4M x 8

SDRAM: 16Mbytes - Nanya NT5SV8M16DS-6K

CPU: TNETD7300GDU Texas Instruments AR7 MIPS based ''' '''

== How to get OpenWRT onto the router: ==
'''Getting and compiling the firmware'''

You will need to compile your own firmware, it's simple enough, if you have ubuntu grab build essentials using synaptic and also grab flex, bison and subversion Download the latest trunk using

svn co https://svn.openwrt.org/openwrt/trunk

or get the same revision as myself and use

svn -r 5174 co https://svn.openwrt.org/openwrt/trunk

Enter into the folder and run make menuconfig, select processor as TI AR7 [2.4], quit and save the config.

Run make to download and compile the firmware

'''Setting up the memory layout'''

To flash your new firmware you must first understand how the memory is divided into blocks, with the default DLink firmware it is this:

mtd0 0x90091000,0x903f0000" - filesystem

mtd1 0x90010090,0x90090000" - kernel

mtd2 0x90000000,0x90010000" - bootloader (adam2 mostly)

mtd3 0x903f0000,0x90400000" - configuration

mtd4 0x90010090,0x903f0000" - this just covers filesystem/kernel

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

user adam2

pass adam2

quote "SETENV mtd0,0x900850E0,0x9003f0000" (fs)

quote "SETENV mtd1,0x90010000,0x900850E0" (kernel)

quote "SETENV mtd4,0x90010000,0x9003f0000" (fs+kernel)

DO NOT CHANGE mtd2 or mtd3 Next we must add a tichksum to our file otherwise the adam2 bootloader will reject it when we try to flash

'''Adding a checksum'''

You just need to get the Source code from DLINK and find the tichksum and perhaps compile it then execute it

'''Flashing the new firmware'''

Now you are ready to flash ftp into adam2

quote "MEDIA FLSH"

binary

debug

hash

put "openwrt-ar7-2.4-squashfs.bin" "c mtd4"  (c can be anything)

quote REBOOT

quit

'''Congratulations you are successful :)'''

now try to get an IP from the router by using dhclient eth0 or just unsetting IP variables in XP telnet into 192.168.1.1 and you're done :)

== How to Debrick and further information: ==
See the forum for how to debrick the DSL-502T[http://forum.openwrt.org/viewtopic.php?id=7742[[BR http://forum.openwrt.org/viewtopic.php?id=7742]

You can generally use the methods on DLinks site or just change ur mtd0/1/4 variables back to defaults and upload the dlink firmware.

But if you've accidentally destroyed your mtd2 adam2 bootloader or mtd3 config file you will need a JTAG cable.

I grabbed one from ebay but you can make your own with 4/5 resistors, pin schematics are here:

 http://wiki.openwrt.org/AR7Port

 http://wiki.openwrt.org/OpenWrtDocs/Customizing/Hardware/JTAG_Cable

The cable I purchased from Ebay was for the WRT54G, it had a 12 pin header, whereas my router had an already soldered 14 pin header, the WRT54G uses EJTAG 2.0 and the AR7 uses EJTAG 2.6, to make the JTAG cable work I simple connected pin 1 TRST with pin 8 VCC/VIO/VRED via a 100 ohm resistor (I didn't  bother soldering it on) and then placed the 12 pin JTAG on top squashing it into place, bending back the extra 2 pins.

My pins are numbered as so:

1 (TRST) - 14

2 - 13

3 - 12

4 - 11

5 - 10

6 - 9

7 - 8 (VIO/VCCC/VREF)

My BIOS settings for my printer port were: ECP+EPP, 0x378.

Once you do this you can use HairyDairyMaids debrick utility 4.8 Get it here:http://downloads.openwrt.org/utils/

Under Windows: load giveio.sys by running loaddrv.exe and adding 'giveio.sys' to the end of the line and clicking install+start.

Under Linux (Ubuntu): Get the build essentials package, compile the binary using 'make' from the folder you extracted the files to, then you need to do this to read the parallel port: rmmod lp, modprobe parport, mknod /dev/parport0 c 99 0

You can now do ./wrt54g -probeonly to test if the unit can be detected

Grab Olegs Adam2 bootloader: http://star.oai.pp.ru/jtag/adam2-oleg.zip

rename the adam2 file to CUSTOM.BIN then do:

./wrt54g -flash:custom  /noerase /nobreak /nodma /window:0x90000000 /start:0x90000000 /length:0x10000  /nocwd

Grab mtd3 config http://mcmcc.bat.ru/dlinkt/restore_mtd3_50xT.rar

rename this to CUSTOM.BIN then do:

./wrt54g -flash:custom  /noerase /nobreak /nodma /window:0x903f0000 /start:0x903f0000 /length:0x10000  /nocwd

You may not have to do /noerase /nobreak or /nocwd but /nodma is required

Once this is done, set you lan IP as 10.8.8.1 subnet 255.0.0.0 (on Linux u need to do ifconfig eth0 10.8.8.1 to set your IP) and then reboot the router, ftp into 10.8.8.8 21 using the command prompt FTP (not anything else) and you will see an adam2 prompt (gratz!).

ping 10.8.8.8 to see if adam2 is working

To get back to dlinks default firmware grab the singleimage.bin from them, if you want to flash OpenWRT see above!

root@ZPC:~# ftp 10.8.8.8 21

ftp: connect: No route to host

ftp> o

(to) 10.8.8.8 21

Connected to 10.8.8.8.

220 ADAM2 FTP Server ready.

Name (10.8.8.8:z): adam2

331 Password required for adam2.

 Password: 230 adam2

logged in.

ftp> quote MEDIA FLSH 200 media set to FLASH

ftp> binary 200 Type set to I.

ftp> hash Hash mark printing on (1024 bytes/hash mark).

ftp> debug Debugging on (debug=1).

ftp> put "fw" "fs mtd4"

local: fw remote: fs mtd4

---> PORT 10,8,8,7,170,251 200 Port command successful.

---> STOR fs mtd4 150 Opening BINARY mode

226 Transfer complete. 1996699 bytes sent in 27.36 secs (71.3 kB/s)

ftp> quote REBOOT

---> REBOOT 221 Goodbye.

 But let me guess... you didn't get the firmware to upload?

 Did you get 550 can not erase or 550 flash erase failed I think I know why!!

 This is because the configuration file we just uploaded had the old firmware version 1 memory map (or you used a different map for OpenWRT) and we are trying to upload a firmware version 2 which has a different memory mapping. You can solve this by issuing SETENV commands with the correct memory mappings before uploading the firmware

quote "SETENV mtd0,0x90091000,0x903f0000" - filesystem

quote "SETENV mtd1,0x90010090,0x90090000" - kernel

quote "SETENV mtd2,0x90000000,0x90010000" - bootloader (adam2 mostly)

quote "SETENV mtd3,0x903f0000,0x90400000" - configuration

quote "SETENV mtd4,0x90010090,0x903f0000" - this just covers filesystem/kernel

 (p.s. the extra , is no mistake, I think it's needed)

Ok so, power cycle the router and it should now work... lights should come on after 30 secs or so.

