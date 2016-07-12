[[TableOfContents]]
= Disclaimer =
The contents of this section of the wiki can have serious consequences. While every effort has been made to test and verify the items herein, if executed incorrectly, or if you just happen to have a bad day you '''COULD SERIOUSLY DAMAGE YOUR HARDWARE'''. Neither I (inh) nor anyone else will be held responsible for anything you do.

= Hardware =
== Serial Console ==

Serial ports allow you to do a myriad of things, including connect to your computer, connect to other devices such as LCDs and GPSes, etc... With a little programming, you could even connect a bunch of routers together. This mod doesn't '''add''' serial ports; those are already there. This just makes them much easier to use with just about any hardware you want.

For the developer, a serial port will also allow you to recover a bricked router when all other methods have failed (tftp, failsafe mode, shorting pins, etc.)

=== Serial port pinouts ===
Pinouts for your model can often be found on your model's page in [:CategoryModel].

=== Home-made RS-232 kit ===

'''Background'''

Most OpenWrt compatible devices have one or two serial ports on the router's PCB (printed circuit board.) The problem is they operate on 3.3v, which means '''they will get fried if you connect them to your computer's serial port''', which operates at 12v. Luckily, this is more common a thing than you would think, and as such, Maxim (no, not the magazine) has made a few handy little ICs for us to use. The best (IMHO) is the MAX233, or more specifically, the MAX233a, which has a higher speed capacity and uses less power. This guide will tell you how to solder everything together to get a pc-compatible serial port on your OpenWrt router.

http://jdc.parodius.com/wrt54g/serial.html

http://www.nslu2-linux.org/wiki/HowTo/AddASerialPort

http://www.rwhitby.net/wrt54gs/serial.html

=== USB Kit ===

A USB based data cable for a mobile cell phone is another possibility.

http://www.nslu2-linux.org/wiki/HowTo/AddASerialPort

note: For the serial console on a WRT54G with a USB cell phone cable, the following pins are used: 4(tx), 6(rx), 10(gnd)

=== Terminal software ===

 * Hyperterm (comes with many versions of MS Windows)
 * Minicom (for POSIX systems)
 * cu(1) (part of the Taylor UUCP package, for POSIX systems)

=== Finding Serial Console ===

(stolen from the [:AR7Port:AR7Port] page) This method used to find the serial port was suggested to me on irc; use a piezo buzzer and attach it's ground (usually black) wire to a ground point on the router - the back of the power regulators are usually good candidates, but check this with a multimeter/voltmeter... Use the other wire to probe any of the header pins which may be pre-installed, or any of the component holes which look like they could have header pins installed into. Once you get the right pin, the piezo should make a screeching sound much like that of a 56kbps connection.

Make sure you reset the router after probing each pin. The bootloader/linux bootup messages will only happen for a few seconds, after that the serial console will be silent - so even if you have the right pin you will not hear anything.

A more accurate method would be to use either a logic analyzer or an oscilloscope, but these are expensive and for the basic task of locating a serial pin a little overkill. ;)

=== Adding a UART to some BCM4702KPB-based boards ===

Unfortunately, BCM4702KPB SoC shares some UART pins with Ethernet0 port, so UART is disabled via GPIO. You have to use '''external''' 3.3V LVTTL or CMOS NS16c550-compatible UART or DUART for devices based on this SoC (i.e. [:WAP54GHowto:WAP54Gv1], Belkin F5D7330 or Asus [:OpenWrtDocs/Hardware/Asus/WL300G:WL-300G]). (Philips [http://www.semiconductors.philips.com/pip/SC16C550IA44.html SC16c550]). Use a 12.75 MHz (25.5MHz/2) crystal for 115200 baud (the UART clock divider is 7). There is the large 20-pin jumper block connected to the CPU I/O data lines, which can be connected to an external UART.

{{{
              -----
   D0      1>| 0 o | 20  A0
   D1      2 | o o | 19  A1
   D2      3 | o o | 18  A2
   D3      4 | o o | 17  CHSL
   D4      5 | o o | 16  /CS
   D5      6 | o o | 15  /RD
   D6      7 | o o | 14  /WR
   D7      8 | o o | 13  MR
   VDD     9 | o o | 12  INTR1, INTR2
VSS (GND) 10 | o o | 11  SIN
              -----
}}}

ASUS WL-500b/g: http://wl500g.info/showthread.php?t=587&page=1&pp=15

== Adding an MMC/SD Card ==
''This is one very cool mod! Credit goes to [http://kiel.kool.dk:27 kiel.kool.dk] for this awesome work. They have also pioneered some other interesting mods as well. Check out http://duff.dk/wrt54gs/ for info. They created this mod for the wrt54g version 2, then I (INH) ported it to version 3. If you have another version, you are going to have to figure out how to port it.. but it shouldn't be too hard.''

'''Introduction'''

This mod allows you to read and write from a MMC/SD card. This is awesome as it can literally give you 555 time the storage space. You can now have over one gigabyte of memory to store and run programs from, store packet logs, etc etc.. It's not a very hard mod to do, unless you have something other than a wrt54g version 2 or 3. If thats the case, please read on, as I go over how I ported this mod to my version 3.

=== Installing on a wrt54g version 2 and 2.2 ===
''The following is the guide from [http://kiel.kool.dk:27 kiel.kool.dk] by Rasmus Rohde and Mads Ulrik Kristoffersenon about installing an MMC/SD card reader/writer in a wrt54g version 2, with added commentary where I feel is appropriate''

''I added now comments for WRT HW-version 2.2 where the GPIO locations are different, but the general procedure is the same.''

This project is for people who would like to add a little storage to their Linksys WRT54G router besides the builtin 4MB flash ram. What we will do is connect an SD card reader to some of the GPIO pins of the CPU found inside the Linksys and with the help of a little driver we can use as a block device from Linux. This means that if you compile your kernel for the Linksys with e.g. support for MSDOS partitions and VFAT you will be able to mount, read, write, partition and so on your normal SD cards. The speed obtainable for reading and writing seems to be about 200 KB/s.

'''Pictures'''

    * [http://kiel.kool.dk:27/pics/AllSolderingDone.jpg The insides of the router with SD card reader installed]
    * [http://kiel.kool.dk:27/pics/Reuter_complete.jpg The finished product with SD card reader installed]

'''What you need'''

    * A soldering iron and a bit of tin solder (and a little bit of soldering skills)
    * An SD card reader unless of course you want to solder directly on the card
    * 6 pieces of thin wire
    * A Linksys WRT54G (hardware version 2)

'''How to proceed'''

   1. For the SD card to work we need to attach 6 wires inside the router. This drawing of the SD card should give an idea of the pins that come into play:

||<|7> http://downloads.OpenWrt.org/inh/reference/mmc.gif||1. CS - Chip Select for the SD card||GPIO7||
||2. DI - Data in on the SD card.||GPIO5||
||3. VSS - Ground is a good thing||GND||
||4. VDD - We need power of course. 3.3V will do the job||3.3v||
||5. CLK - The clock we generate for the SD card||GPIO3||
||6. VSS2 - Another ground is also a good thing||GND||
||7. DO - Data out from the SD card||GPIO4||

      We will be driving the SD card in SPI mode, meaning that only one of the four data out pins are used (pin 7). Obtaining the specs for driving the card in the native SD mode is VERY costly and furthermore the limited number of GPIO pins available inside the router also mandates the use of some sort of serial protocol. The two VSS pins can simply be wired together for this project (VSS2 is used to control the sleep mode of the card). With this in mind lets look at the solder points in the router.

         1. [http://kiel.kool.dk:27/pics/solderpoint_1_annotated.jpg The first three solder points] are located at RP3
         2. [http://kiel.kool.dk:27/pics/solderpoint_2_annotated.jpg The next two solder points] are located at JP1
         3. [http://kiel.kool.dk:27/pics/solderpoint_3_annotated.jpg The last solder point] is at the DMZ LED

  '''Further note for V2 hardware:''' It is worth double-checking the GPIO pin allocations on RP3.  The picture above was not correct for my V2 WRT54G.  The CLK and DO, which are GPIO3 and GPIO4, were swapped compared to the picture. ''(Further unverified evidence supports that the wrt54gs v1.1 hardware also has gpio 3 and 4 switched.) I soldered to the right-hand side of RP3 as shown in the picture with GPIO5 (DI) at the bottom, GPIO4 (DO) next up and GPIO3 (CLK) up from that.[[BR]]  A good way to test the pin allocations is with the [http://downloads.openwrt.org/utils/gpio.tar.gz gpio utility] and a script to toggle the GPIO pin periodically, then search for the pin with a digital multimeter or oscilloscope probe.  I toggled the pins with the following single line in the shell (example for GPIO 5):
 {{{
 while true; do gpio enable 5; sleep 1; gpio disable 5; sleep 1; done}}}
 I then used my multimeter to detect the pin toggling between 0V and 3.3V every second.  I seriously recommend that you do this to verify which pins you are working on prior to doing any soldering.

'''For Version 2.2 hardware:'''
  GPIO 3 can be found on Pin 3 of RP4 (near the BCM switch IC), just left of it you can find
  GPIO 5 next to the RA10 Text label.
  GPIO 4 is located near the RA13 Text label (near to the Power LED)
[http://www.linuxbench.org/wrt54g/wrt54gs.jpg]
 This is a picture of the GPIO 3+5 for wrt-Version 2.2 taken from http://linuxbench.org

Proceed by soldering a wire to each of the 6 solder points. Pay special attention not to short circuit the pins of RP3 - even though these solder points were chosen because they provide the most spacious access point to the GPIO lines needed, it's still pretty tight quarters, so watch out!
   2. By now the wires should be attached nicely inside the router, so that we may continue to connect them to the SD card (reader). This picture shows the SD card reader. It is pretty easy to solder on that one.
   3. Mount the card reader somewhere inside your router. We chose the right hand side of the top cover, using double sided duct tape to make it stick and drilled a small slot to allow cards to be inserted and removed with the cover closed. See the picture links at the top of the page to see what this looks like and check this picture of the actual hole.
   4. That was easy. We are now ready for the software part.

'''Software'''

First of all we suggest that you configure a kernel with support for MSDOS partitions and VFAT. Partition support must be built into the kernel whereas VFAT can be built both as a module or into the kernel. These are some things you may want to include in your .config:
{{{
CONFIG_PARTITION_ADVANCED=y
CONFIG_MSDOS_PARTITION=y
CONFIG_FAT_FS=y
CONFIG_MSDOS_FS=y
CONFIG_VFAT_FS=y
}}}

Now get the [http://kiel.kool.dk:27/mmc.c driver] and the [http://kiel.kool.dk:27/Makefile Makefile]. You will need to modify the Makefile to point to where your OpenWRT linux kernel headers are and also the mipsel compiler location. When that is done just type make (ignore the warnings - they are OK).

The module is now ready to be inserted. Make sure a card is placed in the reader and then load the module. Check with dmesg that everything went OK, and hopefully you should now have some new devices in /dev/mmc/... Here is a little snippet of a "conversation" with the router
{{{
root@radio:~# ls -al /lib/modules/2.4.20/
drwxr-xr-x    1 root     root            0 Jan  1 00:08 .
drwxr-xr-x    1 root     root            0 Jan  1 00:01 ..
lrwxrwxrwx    1 root     root           28 Jan  1 00:01 et.o -> /rom/lib/modules/2.4.20/et.o
-rw-r--r--    1 root     root        50616 Jan  1 00:02 fat.o
-rw-r--r--    1 root     root        12780 Jan  1 00:08 mmc.o
-rw-r--r--    1 root     root        11244 Jan  1 00:03 msdos.o
-rw-r--r--    1 root     root        19156 Jan  1 00:05 vfat.o
lrwxrwxrwx    1 root     root           28 Jan  1 00:01 wl.o -> /rom/lib/modules/2.4.20/wl.o
root@radio:~# insmod mmc
Using /lib/modules/2.4.20/mmc.o
root@radio:~# dmesg | tail -7
mmc Hardware init
mmc Card init
mmc Card init *1*
mmc Card init *2*
Size = 249856, hardsectsize = 512, sectors = 499712
Partition check:
 mmca: p1
root@radio:~# insmod fat
Using /lib/modules/2.4.20/fat.o
root@radio:~# insmod msdos
Using /lib/modules/2.4.20/msdos.o
root@radio:~# mount /dev/mmc/disc0/part1 /mnt -tmsdos
root@radio:~# ls -al /mnt
drwxr-xr-x    2 root     root        16384 Jan  1  1970 .
drwxr-xr-x    1 root     root            0 Jan  1 00:01 ..
-rwxr-xr-x    1 root     root            0 Jan  1 00:07 bossepr0.pic
-rwxr-xr-x    1 root     root        22646 Jan  1 00:02 ld-uclib.so
-rwxr-xr-x    1 root     root        12780 Jan  1  2000 mmc.o
-rwxr-xr-x    1 root     root      1048576 Jan  1  2000 temp.bin
-rwxr-xr-x    1 root     root     16777216 Jan  1  2000 temp2.bin
-rwxr-xr-x    1 root     root     16777216 Jan  1  2000 temp3.bin
-rwxr-xr-x    1 root     root          693 Jan  1  2000 temp4.bin
root@radio:~# df
Filesystem           1k-blocks      Used Available Use% Mounted on
/dev/root                  896       896         0 100% /rom
/dev/mtdblock/4           2176      1580       596  73% /
/dev/mmc/disc0/part1    249728     33856    215872  14% /mnt
}}}

'''A little help with kernel compilation'''

The easiest way to get a kernel running with the needed fs support is probably by downloading OpenWRT and building the flash image. When you are familiar with this process, it is quite easy to change the settings for your kernel. Just go to buildroot/build_mipsel/linux and type make menuconfig. Go to file systems -> Partition Types and check "Advanced partition selection" and "PC BIOS (MSDOS partition tables) support". In "File systems" you should also check "DOS FAT fs support" and optionally "VFAT (Windows 95) fs support". When done just exit saving the changed and type make dep zImage to force a rebuild of the kernel. Then you can just rebuild your OpenWRT image and the new kernel will be included automatically.
GPIO pins, eh?

The integrated Broadcom CPU BCM4712 used in the WRT54G provides a number of General Purpose Input/Output pins (or GPIO pins) that are used for various purposes in the router. We have been able to identify 8 such pins until now and these are assigned as follows:

||Pin||Direction||Name||
||GPIO 0||(Output)||WLAN LED||
||GPIO 1||Output||POWER LED||
||GPIO 2||Output||ADM_EECS||
||GPIO 3||Output||ADM_EESK||
||GPIO 4||Input||ADM_EEDO||
||GPIO 5||Output||ADM_EEDI||
||GPIO 6||Input||Reset button||
||GPIO 7||Output||DMZ LED||

The pins used in this project are the ADM_EESK, ADM_EEDO, ADM_EEDI and DMZ LED pins. The ADM_* pins constitute an interface used to configure the ADMTek switch chip. Since this only happens during the boot process, we are free to use these pins to our likings afterwards (the corresponding pins on the switch chip will be tri-state after configuration). The names of the other pins should be self explanatory. The direction of the pins can be individually programmed (even though this of course does not make sense for every pin).

=== Installing on a wrt54g version 3 and 3.1 ===
*to be written, in the meantime you can find [http://www.allaboutjake.com/network/linksys/wrt54g/hack/ version 3 info] here.

Basically the same as above, but different GPIO points on the board.

Power - 3.3v (red), and GND (black). I looped through the board for strength of connection:

[http://www.ethernal.org/wrt54g/pics/power.jpg]

GPIO 3, as mentioned in the URL above, on the right hand side of the amber LED:

[http://www.ethernal.org/wrt54g/pics/button.jpg]

GPIO 4 and 7:

[http://www.ethernal.org/wrt54g/pics/underside.jpg]

GPIO 5 - definitely right next to the "RA10" label:

[http://www.ethernal.org/wrt54g/pics/gpio5.jpg]

=== Installing on a wrt54g version 4 and wrt54gl ===

Almost the same as for version 3, except GPIO 5 seems to be missing from the board, so use GPIO 2 instead and edit the driver accordingly.  Here is more [http://support.warwick.net/~ryan/wrt54g-v4/v4_sd_done.html version 4 info] someone has made available, including pictures and modified driver source and binary.

=== Porting to other platforms ===
*almost done being written

== USB ==
If your WRT* has a USB port, you could attach a lot of USB devices.

 * http://www.linux-usb.org/
 * [http://www.nslu2-linux.org/wiki/Info/USBDeviceSupport USBDeviceSupport] @NSLU2 Linux

=== First steps ===
First of all you should check if the necessary USB-kernel-modules are installed (check /lib/modules/<kernel-version> for usb*.o) and loaded (lsmod is doing this).

Generic modules are in the following packages:

- kmod-usb-core

- kmod-usb-ohci or kmod-usb-uhci or kmod-usb2 (depends on hardware)

Details instructions can be found in ["UsbStorageHowto"].

=== add USB to your Siemens SE505  ===
On the side with the powerplug you will find some 'C's

- add C906 with 100µF 16Volt

- add C986 with 10µF  16Volt

- add U981 with an LM7805

This will support the +5 Volt to your USB-Port.



Go to the other side of the PCB wehre the antenna is placed.

- add wire to F51 as Fuse

- add to 'R' about 15kOhm to R723 and R724

- shorten R733 R734

- put an USB-Plug to J51

Thats all.


=== USB Hard Drive ===

Already done, see ["UsbStorageHowto"].

All "USB Mass Storage" class devices will work too: USB-to-IDE, some cellphones, come digital cams e.t.c.

=== USB Serial port/Modem ===

It is possible to connect a USB HUB and up to 127 USB-to-RS232 convertors.

Some USB cellphone datacables are dirt cheap and contains a USB-to-RS232 convertor (i.e. [http://gimel.esc.cam.ac.uk/james/resources/pl2303/ Prolific PL2303]).

=== USB Keyboard/Joystick ===

Hmmm...

=== USB Sound devices ===

http://wiki.openwrt.org/UsbAudioHowto

http://www.nslu2-linux.org/wiki/HowTo/SlugAsAudioPlayer

[http://www.logitech.com/index.cfm/products/details/US/EN,CRID=2258,CONTENTID=6730 Logitech USB Headset for PlayStation 2]

[http://www.micronas.com/products/documentation/multimedia/uac355xb/index.php Micronas UAC355xB] USB Codec

=== USB Webcam ===

Check out this page: http://www.nslu2-linux.org/wiki/HowTo/AddUsbWebcam

Asus [:OpenWrtDocs/Hardware/Asus/WL500GD:WL-500G-Deluxe] has a Webcam support and Motion Detection software in the default firmware.

If you have a Philips-based cam (Philips and many Logitechs, also others) and a USB port, you can try the following (tested by me on an ASUS WL500GX):
   1. Grab the "Tom" package from here: http://wl500g.info/showpost.php?p=8610&postcount=17 (and be sure to read through some of the posts) and install it, then erase the /lib/modules/2.4.20/pwc.o file
   2. Download the kmod-videodev and kmod-pwc packages from http://downloads.openwrt.org/people/nico/whiterussian/packages/
   3. Install them :)
   4. Plug in you camera and enjoy! You can use camsrv to stream images, mvc as a simple motion detector... or compile your own programs.

Note: the video device will most likely be /dev/v4l/video0 instead of the common /dev/video0, because of devfs. Just use the correct parameters when you invoke the programs.

=== USB Ethernet ===

If you need one (2..3..127) additional Ethernet ports, it is possible to use USB-to-Ethernet adaptor.

As example, Genius (KYE) GF3000U, Linksys USB100TX, D-Link DSB-650TX which are based on the [http://www.nslu2-linux.org/wiki/HowTo/AddEthernetAdapter ADMtek Pegasus] AN986.

Most of this devices has 10/100Mbit/s Full-Duplex Ethernet interface, but transfer rate is about 10Mbit/s only.

=== USB Bluetooth ===

It is possible, see this thread in the [http://forum.openwrt.org/viewtopic.php?id=1650 Forum].

=== USB VGA ===

http://www.winischhofer.at/linuxsisusbvga.shtml

== Mini PCI and PCI ==

According to [http://www.pcisig.com/specifications/conventional/mini_pci/ PCI-SIG]: ''The Mini PCI specification defines an alternate implementation for small form factor PCI cards referred to in this specification as a Mini PCI card. This specification uses a qualified subset of the same signal protocol, electrical definitions, and configuration definitions as the Conventional PCI Specification.''

In other words it is a compact 3.3V version of venerable PCI. Many Mini PCI devices are available today: sound cards, IDE/ATA and SATA controllers, and even accelerated SVGA cards. For example:

 * [http://www.globalamericaninc.com/other/mini_PCI_&_AGP.php miniPCI and miniAGP Cards]
 * ADLINK [http://www.adlinktech.com/products/LonglifeEmbedded/mPCI-8219.htm Single Channel Ultra160 SCSI]
 * ADLINK [http://www.adlinktech.com/products/LonglifeEmbedded/mPCI-8220.htm Dual Intel 82559 10/100Mbps Ethernet]
 * Kontron [http://www.kontron.com.tw/products/HTML/accessory/accessory.htm MiniPCI cards]

It is possible to remove a Wi-Fi Mini PCI card and insert another device. Fortunately, some A/G dual-standart WRT* models have two Mini PCI slots.

Because Mini PCI and PCI are cousins, you can use '''regular PCI cards''' with your Mini PCI-equipped hardware using Mini PCI-to-PCI converter. Information on some Mini PCI-to-PCI converters can be found here:

 * [http://www.interfacemasters.com/products/pci_tools/mini_pci_to_pci/ IM300 Mini PCI Type III to PCI Adapter Card]
 * [http://www.interfacemasters.com/products/pci_tools/im380/index.html IM380 Mini PCI Type III to PCI Adapter Card ] with '''two''' PCI slots, one 3.3V and one 5V --- check out juicy pictures! :)
 * [http://www.costronic.com/ Costronic's] Mini PCI-to-PCI [http://www.costronic.com/Eindexp.htm#Mini%20PCI CV09MP-P] series.
 * Catalyst [http://www.getcatalyst.com/adapter_moreInfo_pci2mini3-3.html PCI2MINI3-3], [http://www.getcatalyst.com/adapter_moreInfo_pci2mini3-5.html PCI2MINI3-5]

== Adding a GPS ==
''Adding a GPS to your router may seem like an odd idea, but it does have it's uses. If you like to war drive, this combined with the SD card mod would let you simply plug in the router to your cigarette lighter and go, logging the networks to the sd card. It also isn't a hard mod to do. Depending on your GPS, this may be as simple as soldering 3 wires to your router. In my case it was a little more complicated, but by no means hard. It was just like adding a serial port, but instead of adding the serial port, I added the GPS.''

See a [http://iboone.net/blog.bin/IMGP2949.JPG picture] or [http://iboone.net/blog/000047.html read here] for more information.

A package for gpsd is available in [http://openwrt.org/downloads/people/nico/testing/mipsel/packages/ Nico's test repository].

== Adding a Weather Station ==
''Connect a WX200 / WM918 / WMR918 / WMR968 weather station ''
[http://david.zope.nl/hardware/wl500g/wx200wl500g/]


== Adding an LCD ==
See the [http://www.duff.dk/wrt54gs/pics/reuter_lcd.jpg picture].

== Adding VGA Output ==
See the [http://www.duff.dk/wrt54gs/pics/Complete_VGA_Setup.jpg picture]
and this [http://www.duff.dk/wrt54gs/pics/HW_VGA_Setup.jpg picture]

== Adding Second Reset Button (v2.2 only) ==
[http://www.duff.dk/wrt54gs/pics/02_Covox_Top.jpg]

== Adding Sound Output ==
[http://www.duff.dk/wrt54gs/pics/07_Finished_product.jpg]

See also: http://wiki.openwrt.org/UsbAudioHowto
== Adding a Power Button ==
== Adding a Power Reset Button ==
== Making it Mobile ==
[http://www.ranvik.net/privat/yasha/pics/4m.jpg]

[http://yasha.okshtein.net/wrt54g/] How to Mobilize a WRT54g
== Adding i2c bus ==
i2c bus allows you to extend the IO ability beyond just 8 bits of IO.

Inital docs are here http://www.byteclub.net/wiki/index.php?title=Wrt54g

== Power Over Ethernet/Power Requirements ==
The internal voltage regulators on the WRT54g (version 3) are made by Anachip Corp. http://www.anachip.com

The 1509-33 is actually a AP1509 part, and is the 3.3V regulator.

The 1509-50 is actually a AP1509 part as well, and is the 5.0V regulator.

The minimum operating voltage of the 5V regulator is 7VDC, absolute maximum is 24VDC, per the datasheet http://www.anachip.com/downloads/datasheets/power/sw_reg/AP1509.pdf

== WRT Datalogger and Water tank Leve Monitor ==

Using Maxim / Dallas 1-wire devices it is simple to turn a OpenWrt platform into a datalogger. This project is looking at the level of water in a tank, but its trival to do all sorts of other things with this.

http://www.frazer.net.nz/wrting/wrtprojects.htm

= Software =
== Things not to compile in ==
When you change things in the configs yourself, only active the following if you realy know what you are doing.


Busybox Configuration - General Configuration - Support NSA Security Enhanced Linux = N

Busybox Configuration - Init Utilities - halt = N

Busybox Configuration - Init Utilities - poweroff = N

Busybox Configuration - Networking Utilities - ifupdown = N

== Software Tools ==
=== Networking ===
||[http://www.hetos.de/bwlog.html WRTbwlog]||A tool that shows internet traffic on all wired and wireless interfaces, as well as many other useful and related functions||
||BandwithTestPage||A simple CGI script for testing the instantaneous bandwidth to the wireless router.  Just drop into /www/cgi-bin and chmod+x. ||
=== System ===
=== Wireless ===
||[http://wiviz.natetrue.com WiViz]||A very nice wireless network visualization tool||
== Software Guides ==
=== Wireless ===
==== Client Mode ====
See [:ClientModeHowto]

=== System ===
==== LED System Load Monitor ====
''Credit goes to SeRi for starting this mod. He had it use the wrt's white and amber LEDs (version 3 only) to show system load.  I thought it was a very nifty mod, but I couldn't use it, as the white and amber LEDs are used for the read/write lines on the SD card mod. So what did I do? I modded the mod of course! Now anyone with a spare LED can use this mod. you just need to set the correct GPIO pin. For wrt54g's version 2-3, gpio 7 is for the DMZ LED, which is what I use. You can modify the source accordingly. This will flash the LED once per second under normal useage, twice per second under medium load, and when there is a high load on the system, the LED flashes 3 times per second.''

'''NOTE: You will need to compile your kernel with the Busybox option for usleep enabled. This is what is used for the LED strobing'''

'''Installing Necessary Software'''

First of, grab the [http://downloads.openwrt.org/inh/programs/loadmon.sh loadmon.sh] script, and [mbm]'s [http://downloads.openwrt.org/gpio.tar.gz GPIO tool]. Then untar the gpio tool, and copy the files to your /usr/sbin directory. A typical way to do this on a jffs2 install would go as follows. If you are using squash fs, then you shoudl know what to do.
{{{
cd /tmp
wget http://downloads.openwrt.org/inh/programs/loadmon.sh
wget http://downloads.openwrt.org/gpio.tar.gz
gzip -d gpio.tar.gz
tar xvf gpio.tar
mv gpio /usr/sbin
mv loadmon.sh /usr/sbin
}}}

Now that everything is in place, you need to edit your configuration files to start up the script manually when the router boots. To do this, create a script in /etc/init.d to start loadmon.sh. Here's a simple way to do that:
{{{
echo "#!/bin/sh" > /etc/init.d/S60loadmon
echo "/usr/sbin/loadmon.sh &" >> /etc/init.d/S60loadmon
chmod +x /etc/init.d/S60loadmon
}}}

Now reboot and test it out :)

If you dont want to build your own firmware, and you own a router with the white and orange lights, you can try this script.  It will show the white light if load is low, white and orange at medium load, and orange at high load:

{{{
#!/bin/sh

#Set GPIO to the GPIO of the LED you wish to use.
# Default is 7 for DMZ LED on most routers..
GPIOG=2
GPIOR=3
DELAY=2
HIGHLOAD="70"
MEDLOAD="30"

while sleep $DELAY; do
   load=$(cat /proc/loadavg | cut -d " " -f1 | tr -d ".")
   #echo $load

    if [ "$load" -gt "$HIGHLOAD" ]; then
        gpio enable $GPIOG
        gpio disable $GPIOR
    elif [ "$load" -gt "$MEDLOAD" ]; then
        gpio disable $GPIOG
        gpio disable $GPIOR
    else
        gpio disable $GPIOG
        gpio enable $GPIOR
    fi
done
}}}

==== Transparent Firewall ====
See [:TransparentFirewall]



= Firmware =

== Changing CFE defaults ==
''The following is a guide from http://wl500g.dyndns.org/wrt54g.html that I've copied here, with added commentary. I am not the original author, that credit goes to Oleg.''

Copyright (c) 2005 Oleg I. Vdovikin
IMPORTANT: This information provided AS IS, without any warranties. If in doubt leave this page now. This information applies to WRT54G hw rev 2.0, 2.2, 3.0. No other units were tested, but most likely WRT54GS units should be the same. WRT54G hw rev 1.x use different layout, so you need to adjust things accordingly.

The wrt54g v.2.2 unit was kindly donated to me by maxx, the member of the forum.chupa.nl forum. I would like to publically say thank you to him.

'''Extracting default values'''

Telnet/ssh to your router running your favorite firmware and type the following
{{{
dd if=/dev/mtdblock/0 bs=1 skip=4116 count=2048 | strings > /tmp/cfe.txt
dd if=/dev/mtdblock/0 of=/tmp/cfe.bin
}}}

Copy both cfe.bin and cfe.txt to your linux box (this is required).

''To copy files from your router to your computer, make sure the Dropbear package is installed, and type:
{{{
scp root@<router ip>:/tmp/cfe.bin /directory/on/your/computer
scp root@<router ip>:/tmp/cfe.txt /directory/on/your/computer
}}}
''
Check cfe.txt, it should look like this (this is from v.2.2):
{{{
boardtype=0x0708
boardnum=42
boardrev=0x10
boardflags=0x0118
boardflags2=0
sromrev=2
clkfreq=200
sdram_init=0x000b
sdram_config=0x0062
sdram_refresh=0x0000
sdram_ncdl=0x0
et0macaddr=00:90:4C:00:00:00
et0phyaddr=30
et0mdcport=0
gpio5=robo_reset
vlan0ports=1 2 3 4 5*
vlan0hwname=et0
vlan1ports=0 5
vlan1hwname=et0
wl0id=0x4320
il0macaddr=00:90:4C:00:00:00
aa0=3
ag0=255
pa0maxpwr=0x4e
pa0itssit=62
pa0b0=0x15eb
pa0b1=0xfa82
pa0b2=0xfe66
wl0gpio2=0
wl0gpio3=0
cctl=0
ccode=0
dl_ram_addr=a0001000
os_ram_addr=80001000
os_flash_addr=bfc40000
lan_ipaddr=192.168.1.1
lan_netmask=255.255.255.0
scratch=a0180000
boot_wait=off
watchdog=5000
bootnv_ver=2
}}}

'''Changing defaults'''

Open cfe.txt using text editor and change defaults in the way you like (but be extremely careful, as some changes could prevent device from booting and you will need to use JTAG cable to bring it back to life). For me I've decided to enable both Afterburner (Speedbooster) and set boot_wait to on by default, so reset to default no longer messes the things, so I've applied this pseudo-patch (please note, that I've added bit 0x200 to boardflags to enable afterburner):
{{{
-boardflags=0x0118
-boot_wait=off
+boardflags=0x0318
+boot_wait=on
}}}

''To make life easier for me, I added "reset_gpio=6" to the cfe.txt file. This way, if I do set something wrong, like clkfreq, and the router just locks up, I wont have to try over and over again to hit a very slim window with the JTAG to erase the nvram. I can just hold reset when the router powers on, and it will use the default nvram values stored in the cfe.''

If you do not understand some things in this file, do not try to edit it. This is also applies to afterburner. I've also tried to change default lan_ipaddr, but this does not work in the way I expect: CFE started to answer to ping request to new lan_ipaddr, but it does not accept tftp transfers...

'''Creating new CFE image'''

You will need a nvserial utility which comes with several GPL tarballs. Linksys supplies it in the wrt54g.1.42.3, wrt54g.1.42.2, wap55ag.1.07, wap54gv2.2.06. Launch nvserial in the way like this on your x86 linux box:
''You can get nvserial from http://downloads.openwrt.org/people/inh/programs/nvserial''
{{{
nvserial -i cfe.bin -o cfe_new.bin -b 4096 -c 2048 cfe.txt
}}}
It works really slow, but it should finally create cfe_new.bin file for you, which has new embedded nvram.

'''Recompiling kernel with writable pmon partition'''

By default most firmwares has pmon partition write protected, i.e. you can't flash anything to this first 256k of flash. This is to prevent corrupting PMON/CFE. To remove this "lock" you will need to compile your own firmare with the following patch, you will need to copy the patch into "target/linux/linux-2.4/patches/brcm". (This patch works with WHITERUSSIAN RC3)
{{{
--- linux-2.4.30/arch/mips/bcm947xx/setup.c.orig	2005-09-21 11:24:09.000000000 -0400
+++ linux-2.4.30/arch/mips/bcm947xx/setup.c	2005-09-21 13:48:46.853425632 -0400
@@ -174,7 +174,7 @@
 #ifdef CONFIG_MTD_PARTITIONS

 static struct mtd_partition bcm947xx_parts[] = {
-	{ name: "pmon",	offset: 0, size: 0, mask_flags: MTD_WRITEABLE, },
+	{ name: "pmon",	offset: 0, size: 0 /*, mask_flags: MTD_WRITEABLE,*/ },
 	{ name: "linux", offset: 0, size: 0, },
 	{ name: "rootfs", offset: 0, size: 0, },
 	{ name: "nvram", offset: 0, size: 0, },
}}}

'''Flashing new CFE image'''

So, once you've recompiled and flashed your new firmware you need you upgrade CFE. This process is dangerous, as flash failure during it will prevent your unit from booting. Copy cfe_new.bin to your wrt54g and flash it. The exact commands are dependent on the firmware. With OpenWrt I've used the following:

{{{
mtd unlock pmon
mtd write -f /tmp/cfe_new.bin pmon
}}}

''I recommend using the JTAG cable method for re-flashing your CFE. If something were to go wrong, you would end up needing the JTAG cable anyways. It's really cheap and easy to build, and makes it possible to recover from almost any error you make when writing to the flash. Check out http://openwrt.org/OpenWrtDocs/Troubleshooting ''

'''Checking it'''

Embedded nvram is only used, when real nvram is either corrupted or empty (CRC/magic checks fails), so you will need to erase nvram or to reset to defaults. With OpenWrt type this:
{{{
mtd erase nvram
}}}
Then cross your fingers and reboot your unit. And remember - I'm not responsible for any damage to your unit, as this information is provided AS IS for my own pleasure. oleg@cs.msu.su
Posted: 2005-04-03

== Customizing Firmware Image ==

It is relatively easy to create a custom firmware image which is pre-loaded with particular software packages and your own files. Please use the !OpenWrt [:ImageBuilderHowTo:Image Builder].
