= Adding an MMC/SD Card =
''This is one very cool mod! Credit goes to [http://kiel.kool.dk kiel.kool.dk] for this awesome work. They have also pioneered some other interesting mods as well. Check out http://duff.dk/wrt54gs/ for info. They created this mod for the wrt54g version 2, then I (INH) ported it to version 3. If you have another version, you are going to have to figure out how to port it.. but it shouldn't be too hard.''

'''Introduction'''

This mod allows you to read and write from a MMC/SD card. This is awesome as it can literally give you 555 time the storage space. You can now have over one gigabyte of memory to store and run programs from, store packet logs, etc etc.. It's not a very hard mod to do, unless you have something other than a wrt54g version 2 or 3. If thats the case, please read on, as I go over how I ported this mod to my version 3.

== Installing on a WRT54G v2 and v2.2 ==
''The following is the guide from [http://kiel.kool.dk kiel.kool.dk] (seems to be down, [http://web.archive.org/http://kiel.kool.dk/ archive.org mirror]) by Rasmus Rohde and Mads Ulrik Kristoffersenon about installing an MMC/SD card reader/writer in a wrt54g version 2, with added commentary where I feel is appropriate''

''I added now comments for WRT HW-version 2.2 where the GPIO locations are different, but the general procedure is the same.''

This project is for people who would like to add a little storage to their Linksys WRT54G router besides the builtin 4MB flash ram. What we will do is connect an SD card reader to some of the GPIO pins of the CPU found inside the Linksys and with the help of a little driver we can use as a block device from Linux. This means that if you compile your kernel for the Linksys with e.g. support for MSDOS partitions and VFAT you will be able to mount, read, write, partition and so on your normal SD cards. The speed obtainable for reading and writing seems to be about 200 KB/s.

'''Pictures'''

 * The insides of the router with SD card reader installed<br>attachment:kiel.kool.dk-AllSolderingDone.jpg
 * The finished product with SD card reader installed<br>attachment:kiel.kool.dk-Reuter_complete.jpg

'''What you need'''

 * A soldering iron and a bit of tin solder (and a little bit of soldering skills)
 * An SD card reader unless of course you want to solder directly on the card
   (hint: mini-SD cards come with an adapter. You can solder to the adapter and use it as a socket)
 * 6 pieces of thin wire
 * A Linksys WRT54G (hardware version 2)

'''How to proceed'''

 1. For the SD card to work we need to attach 6 wires inside the router. This drawing of the SD card should give an idea of the pins that come into play:

||<style="text-align: center;"|7> http://downloads.OpenWrt.org/inh/reference/mmc.gif ||1. CS - Chip Select for the SD card ||GPIO7 ||
||2. DI - Data in on the SD card. ||GPIO5 ||
||3. VSS - Ground is a good thing ||GND ||
||4. VDD - We need power of course. 3.3V will do the job ||3.3v ||
||5. CLK - The clock we generate for the SD card ||GPIO3 ||
||6. VSS2 - Another ground is also a good thing ||GND ||
||7. DO - Data out from the SD card ||GPIO4 ||


 . We will be driving the SD card in SPI mode, meaning that only one of the four data out pins are used (pin 7). Obtaining the specs for driving the card in the native SD mode is VERY costly and furthermore the limited number of GPIO pins available inside the router also mandates the use of some sort of serial protocol. The two VSS pins can simply be wired together for this project (VSS2 is used to control the sleep mode of the card). With this in mind lets look at the solder points in the router.
  1. [http://kiel.kool.dk/pics/solderpoint_1_annotated.jpg The first three solder points] are located at RP3
  1. [http://kiel.kool.dk/pics/solderpoint_2_annotated.jpg The next two solder points] are located at JP1
  1. [http://kiel.kool.dk/pics/solderpoint_3_annotated.jpg The last solder point] is at the DMZ LED

 . '''Important note for V2 hardware and some WRT54GS:''' It is worth double-checking the GPIO pin allocations on RP3. The picture above was not correct for my V2 WRT54G. The CLK and DO, which are GPIO3 and GPIO4, were swapped compared to the picture. ''(Further unverified evidence supports that the wrt54gs v1.1 hardware also has gpio 3 and 4 switched. Can definitely confirm this swapped CLK/DO for my WRT54GS V1.0, so it's likely that the V1.1 statement before is correct, too) I soldered to the right-hand side of RP3 as shown in the picture with GPIO5 (DI) at the bottom, GPIO4 (DO) next up and GPIO3 (CLK) up from that.[[BR]] A good way to test the pin allocations is with the [http://downloads.openwrt.org/utils/gpio.tar.gz gpio utility] and a script to toggle the GPIO pin periodically, then search for the pin with a digital multimeter or oscilloscope probe. I toggled the pins with the following single line in the shell (example for GPIO 5): ''

 . {{{
 while true; do gpio enable 5; sleep 1; gpio disable 5; sleep 1; done}}}
 I then used my multimeter to detect the pin toggling between 0V and 3.3V every second. I seriously recommend that you do this to verify which pins you are working on prior to doing any soldering.

 . On a WRT54G Version 2 the tests on GPIO4 failed. According to http://forum.openwrt.org/viewtopic.php?pid=31968 the reason is an incomplete initialization of the GPIOs. Using the mmc.o downloadable at the end of the thread the MMC is detected and working, the GPIO test is also working after loading this module.

'''For Version 2.2 hardware:'''

 . GPIO 3 can be found on Pin 3 of RP4 (near the BCM switch IC), just left of it you can find GPIO 5 next to the RA10 Text label. GPIO 4 is located near the RA13 Text label (near to the Power LED)

attachment:linuxbench.org-wrt54gs.jpg

 . This is a picture of the GPIO 3+5 for wrt-Version 2.2 taken from http://linuxbench.org

Proceed by soldering a wire to each of the 6 solder points. Pay special attention not to short circuit the pins of RP3 - even though these solder points were chosen because they provide the most spacious access point to the GPIO lines needed, it's still pretty tight quarters, so watch out!

 1. By now the wires should be attached nicely inside the router, so that we may continue to connect them to the SD card (reader). This picture shows the SD card reader. It is pretty easy to solder on that one.
 1. Mount the card reader somewhere inside your router. We chose the right hand side of the top cover, using double sided duct tape to make it stick and drilled a small slot to allow cards to be inserted and removed with the cover closed. See the picture links at the top of the page to see what this looks like and check this picture of the actual hole.
 1. That was easy. We are now ready for the software part.

'''Software'''

First of all we suggest that you configure a kernel with support for MSDOS partitions and VFAT. Partition support must be built into the kernel whereas VFAT can be built both as a module or into the kernel. These are some things you may want to include in your .config:

{{{
CONFIG_PARTITION_ADVANCED=y
CONFIG_MSDOS_PARTITION=y
CONFIG_FAT_FS=y
CONFIG_MSDOS_FS=y
CONFIG_VFAT_FS=y
}}}

Now get the [http://kiel.kool.dk/mmc.c driver] and the [http://kiel.kool.dk/Makefile Makefile]. You will need to modify the Makefile to point to where your OpenWRT linux kernel headers are and also the mipsel compiler location. When that is done just type make (ignore the warnings - they are OK).
But you may just as well install the freifunk-sdcard and freifunk-sdinit mmc module packages which work fine on my whiterussian RC5.

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

Using OpenWRT RC5 no msdos kernel module is needed. The mount-option -tmsdos has to be omitted.

'''A little help with kernel compilation'''

The easiest way to get a kernel running with the needed fs support is probably by downloading OpenWRT and building the flash image. When you are familiar with this process, it is quite easy to change the settings for your kernel. Just go to buildroot/build_mipsel/linux and type make menuconfig. Go to file systems -> Partition Types and check "Advanced partition selection" and "PC BIOS (MSDOS partition tables) support". In "File systems" you should also check "DOS FAT fs support" and optionally "VFAT (Windows 95) fs support". When done just exit saving the changed and type make dep zImage to force a rebuild of the kernel. Then you can just rebuild your OpenWRT image and the new kernel will be included automatically. GPIO pins, eh?

The integrated Broadcom CPU BCM4712 used in the WRT54G provides a number of General Purpose Input/Output pins (or GPIO pins) that are used for various purposes in the router. We have been able to identify 8 such pins until now and these are assigned as follows:

||Pin ||Direction ||Name ||
||GPIO 0 ||(Output) ||WLAN LED ||
||GPIO 1 ||Output ||POWER LED ||
||GPIO 2 ||Output ||ADM_EECS ||
||GPIO 3 ||Output ||ADM_EESK ||
||GPIO 4 ||Input ||ADM_EEDO ||
||GPIO 5 ||Output ||ADM_EEDI ||
||GPIO 6 ||Input ||Reset button ||
||GPIO 7 ||Output ||DMZ LED ||


The pins used in this project are the ADM_EESK, ADM_EEDO, ADM_EEDI and DMZ LED pins. The ADM_* pins constitute an interface used to configure the ADMTek switch chip. Since this only happens during the boot process, we are free to use these pins to our likings afterwards (the corresponding pins on the switch chip will be tri-state after configuration). The names of the other pins should be self explanatory. The direction of the pins can be individually programmed (even though this of course does not make sense for every pin).

== Installing on a WRT54G v3 and 3.1 ==
*to be written, in the meantime you can find [http://www.allaboutjake.com/network/linksys/wrt54g/hack/ version 3 info] here.

Basically the same as above, but different GPIO points on the board.

Power - 3.3v (red), and GND (black). I looped through the board for strength of connection:

attachment:otago.ac.nz-power.jpg

GPIO 3, as mentioned in the URL above, on the right hand side of the amber LED:

attachment:otago.ac.nz-button.jpg

GPIO 4 and 7:

attachment:otago.ac.nz-underside.jpg

GPIO 5 - definitely right next to the "RA10" label:

attachment:otago.ac.nz-gpio5.jpg

Picture taken from [http://www.otago.ac.nz/mjb/wrt54g/ otago.ac.nz].

== Installing on a wrt54g version 4 and wrt54gl ==
Almost the same as for version 3, except GPIO 5 seems to be missing from the board, so use GPIO 2 instead and edit the driver accordingly. Here is more [http://support.warwick.net/~ryan/wrt54g-v4/v4_sd_done.html version 4 info] someone has made available, including pictures and modified driver source and binary.
Sadly this link is dead, so you currently have to use the wayback machine to see where to solder the cables. [http://web.archive.org/web/20060406214348/http://support.warwick.net/~ryan/wrt54g-v4/v4_sd_done.html that site from web.archive.org]

Here is another mod done for a version 4 wrt54gs [http://theattic.thruhere.net/mmc-sd-mod.html]


=== WRT54GL v1.1 + WRT54G-TM ===

+3.3V and GND:

attachment:cascade.dyndns.org-linksys-wrt54gl-v1.1-3.3v+GND.jpg

GPIO 2 and 3:

attachment:cascade.dyndns.org-linksys-wrt54gl-v1.1-gpio-2+3.jpg

GPIO 4 and 7:

attachment:cascade.dyndns.org-linksys-wrt54gl-v1.1-gpio-4+7.jpg]

Pictures taken from [http://cascade.dyndns.org/~datagarbage/wrt350n.html cascade.dyndns.org].

== Porting to other platforms ==
*almost done being written

Buffalo WHR-HP-G54 connections are:

'''GPIO3''' Output (uninstalled LED) to CLK (SD Card #5) Connect to the very small pad above "R4" in the picture.[[BR]]
'''GPIO6''' Output (AOSS LED) to DO (SD Card #2) Connect to the bottom of the resistor in the picture.[[BR]] 
'''GPIO7''' Output (Diag LED) to CS (SD Card #1) Connect to the left side of the resistor shown in the picture.[[BR]]

attachment:flatsurface.com-whr-sdcard1.jpg

'''GPIO5''' Input (Bridge/Auto switch) to DI (SD Card #7) Connect to the C242 on the side nearest R151 in the picture. ''The switch '''must''' remain in the "auto" position for proper operation.''[[BR]]
'''3.3v''' (near voltage regulator) to Vcc (SD Card #4)Connect to the pad shown in the picture.[[BR]]
'''GND''' (Bridge/Auto switch frame) to Gnd (SD Card #3&6) Available in many places - the frame of the switch is convenient.[[BR]]

attachment:flatsurface.com-whr-sdcard2.jpg

Use mmc.c found at http://www.partners.biz/dd-wrt/mmc-buffalo.tar It will automatically adapt to the connections given. 

'''echo 0xe8 > /proc/diag/gpiomask''' to avoid hotplug problems.

Pictures taken from [http://www.flatsurface.com flatsurface.com].

=== SDcard on WAP54G V31 (EU) ===

Here is a link that describes how to add a SD card to a WAP54G V31 (EU), this project uses the card read only,
first a cramfs is created on the card with the PC (this is the native system the Linksys software uses),
so no MSDOS stuff needs to be added to the kernel (there is only 2MB FLASH in WAP54G V31 EU). 
http://panteltje.com/panteltje/wap54g/to-linksys-wap54g-forum-2.txt




== Yay, it works, now what? ==



Now to configure OpenWrt or X-Wrt firmware you can go to Digital Incursion: http://www.digitalincursion.net/wrt54gl.html for a easy configuration instructions for both with the mmc/sd. Some people in the past have had problems configuring the device with OpenWrt and or X-Wrt the above website makes it simple.

For Package installation Please see PackagesOnExternalMediaHowTo
