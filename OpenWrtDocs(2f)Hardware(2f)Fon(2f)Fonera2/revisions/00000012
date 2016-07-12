= Installation =

== Bill of Materials ==

You will need:
 * A tftp server
 * A telnet client
 * A copy of the OpenWRT kernel (openwrt-atheros-vmlinux.lzma)
 * A copy of either the squashfs or jffs image (openwrt-atheros-root.squashfs or openwrt-atheros-root.jffs2-64k)

== Process ==

 1. Connect your computer's ethernet port to the router's LAN port.
 2. Set your computer's IP to 192.168.1.254.
 3. Place the two images in the same directory on your computer, and start your tftp server serving that directory.
 4. Unplug the router.
 5. Start your computer pinging 192.168.1.1.
 6. Plug in the router.
 7. As soon as you see a reply to the ping, telnet 192.168.1.1 on port 9000.
 8. As soon as you see the connection made, type ^C.  You have 2 seconds from the router first booting to press ctrl-C.
 9. Now issue the following commands to copy the flash, note that each fis create command will take a significant amount of time.  The first will take aproximately 5 minutes, while the second about 10-15.  During this time the router will lock up totally and become unpingable.  Do not touch it:
{{{fis init
load -r -v -b 0x80041000 openwrt-atheros-vmlinux.lzma
fis create kernel
load -r -v -b 0x80041000 openwrt-atheros-root.squashfs
fis create -l 0x6f0000 rootfs}}}
(replacing squashfs with jffs2-64k as required).
 10.#10 Use {{{fis edit}}} to set the router to boot from kernel.
 11. Issue the following commands to start OpenWRT.  Once you have done this, you should see the OpenWRT banner, and a normal bash prompt:
{{{fis load -l kernel
exec}}}
 12.#12 Configure OpenWRT!  You're done.

= Other Information =

Serial port pinout (front to rear) is GND,RX (input to the Fonera),TX (output from the Fonera),3.3V

{{{
+Ethernet eth0: MAC address 00:18:84:d0:00:10
IP: 192.168.1.1/255.255.255.0, Gateway: 0.0.0.0
Default server: 192.168.1.254

RedBoot(tm) bootstrap and debug environment [ROMRAM]
OpenWrt certified release, version 1.1 - built 12:40:38, Sep  3 2007

Copyright (C) 2000, 2001, 2002, 2003, 2004 Red Hat, Inc.

Board: FON 2202
RAM: 0x80000000-0x82000000, [0x80040290-0x80fe1000] available
FLASH: 0xa8000000 - 0xa87f0000, 128 blocks of 0x00010000 bytes each.
== Executing boot script in 2.000 seconds - enter ^C to abort
^C
RedBoot> fis list
Name              FLASH addr  Mem addr    Length      Entry point
RedBoot           0xA8000000  0x8003F400  0x00030000  0xA8000000
loader            0xA8030000  0x80100000  0x00010000  0x80100000
image             0xA8040000  0x80040400  0x00310004  0x80040400
image2            0xA8660000  0xA8660000  0x00140000  0x8003F400
FIS directory     0xA87E0000  0xA87E0000  0x0000F000  0x00000000
RedBoot config    0xA87EF000  0xA87EF000  0x00001000  0x00000000
RedBoot> fis list -d
Name              FLASH addr  Mem addr    Datalen     Entry point
RedBoot           0xA8000000  0x8003F400  0x000283D8  0xA8000000
loader            0xA8030000  0x80100000  0x00010000  0x80100000
image             0xA8040000  0x80040400  0x00310004  0x80040400
image2            0xA8660000  0xA8660000  0x00140000  0x8003F400
FIS directory     0xA87E0000  0xA87E0000  0x00000000  0x00000000
RedBoot config    0xA87EF000  0xA87EF000  0x00000000  0x00000000
RedBoot> fis list -c
Name              FLASH addr  Checksum    Length      Entry point
RedBoot           0xA8000000  0x721BFE07  0x00030000  0xA8000000
loader            0xA8030000  0xA8C647E7  0x00010000  0x80100000
image             0xA8040000  0x349F72F2  0x00310004  0x80040400
image2            0xA8660000  0xA3DE818C  0x00140000  0x8003F400
FIS directory     0xA87E0000  0x00000000  0x0000F000  0x00000000
RedBoot config    0xA87EF000  0x00000000  0x00001000  0x00000000
RedBoot> fconfig -l
Run script at boot: true
Boot script:
.. fis load -b 0x80100000 loader
.. go 0x80100000

Boot script timeout (1000ms resolution): 2
Use BOOTP for network configuration: false
Gateway IP address: 0.0.0.0
Local IP address: 192.168.1.1
Local IP address mask: 255.255.255.0
Default server IP address: 192.168.1.254
Console baud rate: 9600
GDB connection port: 9000
Force console for special debug messages: false
Network debug at boot time: false
RedBoot>
}}}

To backup the flash, take a copy of the following partitions:

{{{
dev:    size   erasesize  name
mtd0: 00030000 00010000 "RedBoot"
mtd1: 00010000 00010000 "loader"
mtd2: 00620000 00010000 "image"
mtd3: 0055c000 00010000 "rootfs"
mtd4: 00310000 00010000 "rootfs_data"
mtd5: 00010000 00010000 "config"
mtd6: 00140000 00010000 "image2"
mtd7: 0000f000 00010000 "FIS directory"
mtd8: 00001000 00010000 "RedBoot config"
mtd9: 00010000 00010000 "board_config"
}}}

Note that rootfs, rootfs_data and config are all inside "image", so you don't need to backup partitions 3, 4 and 5.

As long as you only modify the loader, image and image2 partitions, and take care to restore them back to their original settings, then you should be able to use RedBoot to reflash the saved partitions.  Be careful with the load address and entry point for image (0x80040400).

To load openwrt, just do the following on the redbood console:
(You need to make sure that the two files in the "load" commands are retrivable via tftp or http)
{{{
fis init
load -r -v -b 0x80041000 openwrt-atheros-vmlinux.lzma
fis create kernel
}}}
Then create the rootfs partition in the rest of the empty space using:
{{{
load -r -v -b 0x80041000 openwrt-atheros-root.squashfs
fis create -l 0x6f0000 rootfs
}}}
(make sure that 0x6f0000 corresponds to the amount of free space left in the flash)

To start openwrt just issue:
{{{
fis load -l kernel
exec
}}}

Note: You also need to change the redboot boot script to the above, otherwise openwrt won't boot after a reboot/power cycle by itself:
