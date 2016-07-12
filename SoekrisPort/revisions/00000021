[[TableOfContents]]
== Introduction ==
The SoekrisPort is an attempt to use OpenWrt on PC-based embedded computer boards sold by [http://www.soekris.com/ Soekris Engineering], starting with the [http://www.soekris.com/net4801.htm net4801] board.

The net4801 has a CompactFlash socket, as well as an IDE interface for 2.5" HDD. The installation procedure described here is for CF setup. You can use whatever size (from 8MB to 1GB) for your CF.


== Installation ==

When compiling OpenWrt, it can generate the following images (depending on your filesystem selection), which you can copy on the CF device using dd directly:

openwrt-x86-2.6-jffs2-128k.image
openwrt-x86-2.6-jffs2-64k.image
openwrt-x86-2.6-ext2.image

You no longer need to partition the CF card or create the filesystems manually

== Old installation method (Only use if you know what you're doing!) ==
I assume the CF is available on a linux system, using a card reader for example. The block device for the CF on this system is {{{/dev/sda}}} and will be mounted on {{{/mnt/cf}}}. The CF will be setup with the GRUB bootloader, an OpenWrt linux kernel and an OpenWrt JFFS2 image, mounted using MTD block emulation.

=== Creating the boot & root partitions ===
The CF needs 2 partitions : one for the bootloader + kernel and the other for the root filesystem. Partition 1 (boot) should be around 1MB in size. Partition 2 (root) could be any size you want, but the larger it is, the longer it will take to mount at boot time, because of JFFS2.

You can use {{{fdisk}}} to partition the CF :
{{{
# fdisk /dev/sda

Command (m for help): p

Disk /dev/sda: 256 MB, 256204800 bytes
15 heads, 48 sectors/track, 695 cylinders
Units = cylinders of 720 * 512 = 368640 bytes

   Device Boot      Start         End      Blocks   Id  System
/dev/sda1               1           4        1416   83  Linux
/dev/sda2               5          89       30600   83  Linux

}}}

Or you can use {{{cfdisk}}} to create more easily two partitions:

{{{
cfdisk /dev/sda
}}}

=== Formatting the boot partition ===

Use {{{mke2fs}}} to create a linux ext2 filesystem on the boot partition :
{{{
# mke2fs /dev/sda1
# tune2fs -c 0 /dev/sda1
}}}


=== Mounting the boot partition ===

Use {{{mount}}} to mount the boot partition somewhere on your system :
{{{
# mount /dev/sda1 /mnt/cf
}}}


=== Installing GRUB ===

Use {{{grub-install}}} to install the GRUB bootloader on the boot partition :
{{{
# grub-install --no-floppy --root-directory=/mnt/cf /dev/sda
}}}


=== Installing the kernel ===

Dowload the kernel: http://downloads.openwrt.org/people/nico/testing/x86-2.4/openwrt-x86-2.4-vmlinuz

Use {{{cp}}} to install the linux kernel on the boot partition :
{{{
# cp openwrt-x86-2.4-vmlinuz /mnt/cf/boot/
}}}


=== Installing the JFFS2 image ===

If the root partition is larger than the jffs2 image, it should first be 'erased'
to avoid a bunch of warnings about invalid jffs2 sectors:
{{{
# perl -e '$buf = "\xff" x 4096; while (print $buf) {}' > /dev/sda2
}}}

Downloade the JFFS2 file: http://downloads.openwrt.org/people/nico/testing/x86-2.4/openwrt-x86-2.4-jffs2-8MB.img

Use {{{dd}}} to transfer the jffs2 image on the root partition :
{{{
# dd if=openwrt-x86-2.4-jffs2-8MB.img of=/dev/sda2
2048+0 records in
2048+0 records out
1048576 bytes transferred in 1.453255 seconds (721536 bytes/sec)
}}}

=== Configuring GRUB ===

Use your favorite editor to create and edit the GRUB configuration file :
{{{
# vi /mnt/cf/boot/grub/menu.lst
}}}

and put the following lines in it :
{{{
serial --unit=0 --speed=19200 --word=8 --parity=no --stop=1
terminal --timeout=10 serial

default 0
timeout 5

title   OpenWrt
root    (hd0,0)
kernel  /boot/openwrt-x86-2.6-vmlinuz block2mtd.block2mtd=/dev/hda2 root=/dev/mtdblock0 rootfstype=jffs2 init=/etc/preinit noinitrd console=ttyS0,19200n8
boot

}}}

If you use a WRAP board instead of a Soekris, add
{{{
reboot=bios
}}}
to the kernel command line, as the WRAP has no keyboard controller that would be needed for hard reboot.

=== Checking ===

Use {{{find}}} or {{{ls}}} and check that you have something like that :
{{{
# pwd
/mnt/cf
# find . -ls
     2    1 drwxr-xr-x   3 root     root         1024 Sep 21 02:11 .
    12    1 drwxr-xr-x   3 root     root         1024 Sep 21 02:19 ./boot
    13    1 drwxr-xr-x   2 root     root         1024 Sep 21 02:18 ./boot/grub
    14    1 -rw-r--r--   1 root     root           30 Sep 21 02:07 ./boot/grub/device.map
    15    1 -rw-r--r--   1 root     root          512 Sep 21 02:07 ./boot/grub/stage1
    16  107 -rw-r--r--   1 root     root       108168 Sep 21 02:07 ./boot/grub/stage2
    17    8 -rw-r--r--   1 root     root         7776 Sep 21 02:07 ./boot/grub/e2fs_stage1_5
    18    8 -rw-r--r--   1 root     root         7504 Sep 21 02:07 ./boot/grub/fat_stage1_5
    19    9 -rw-r--r--   1 root     root         8320 Sep 21 02:07 ./boot/grub/jfs_stage1_5
    20    7 -rw-r--r--   1 root     root         7008 Sep 21 02:07 ./boot/grub/minix_stage1_5
    21    9 -rw-r--r--   1 root     root         9216 Sep 21 02:07 ./boot/grub/reiserfs_stage1_5
    22   10 -rw-r--r--   1 root     root         9288 Sep 21 02:07 ./boot/grub/xfs_stage1_5
    11    1 -rw-r--r--   1 root     root          279 Sep 21 02:18 ./boot/grub/menu.lst
    23  690 -rw-r--r--   1 root     root       701778 Sep 21 02:19 ./boot/openwrt-x86-2.4-vmlinuz
}}}


=== Cleaning-up ===

Use {{{umount}}} to unmount the boot partition :
{{{
# umount /dev/sda1
}}}

Now your CF is ready


== Booting ==

You have plugged the CF in the CF socket of the board and have a serial connection attached.

At comBIOS prompt, hit {{{Ctrl+P}}} to enter comBIOS monitor :
{{{
comBIOS ver. 1.28  20050529  Copyright (C) 2000-2005 Soekris Engineering.

net4801

0128 Mbyte Memory                        CPU Geode 266 Mhz

Pri Mas  Hitachi XX.V.3.3.0.0            LBA 695-15-48  250 Mbyte
Pri Sla  HITACHI_DK23DA-20               LBA Xlt 1024-255-63  19535 Mbyte

Slot   Vend Dev  ClassRev Cmd  Stat CL LT HT  Base1    Base2   Int
-------------------------------------------------------------------
0:00:0 1078 0001 06000000 0107 0280 00 00 00 00000000 00000000
0:06:0 100B 0020 02000000 0107 0290 00 3F 00 0000E101 A0000000 10
0:07:0 100B 0020 02000000 0107 0290 00 3F 00 0000E201 A0001000 10
0:08:0 100B 0020 02000000 0107 0290 00 3F 00 0000E301 A0002000 10
0:10:0 1260 3873 02800001 0117 0290 08 3C 00 A0003008 00000000 11
0:18:2 100B 0502 01018001 0005 0280 00 00 00 00000000 00000000
0:19:0 0E11 A0F8 0C031008 0117 0280 08 38 00 A0004000 00000000 05

 5 Seconds to automatic boot.   Press Ctrl-P for entering Monitor.

comBIOS Monitor.   Press ? for help.

>
}}}


Use the {{{show}}} command and ensure that your CF is Primary :
{{{
> show FLASH
 = Primary

}}}


Use the {{{boot}}} command to boot from the first IDE device :
{{{
> boot 80
GRUB Loading stage1.5.

GRUB loading, please wait...

}}}


Hit {{{Enter}}} at the GRUB menu to boot OpenWrt :
{{{
    GNU GRUB  version 0.95  (639K lower / 130048K upper memory)

 +-------------------------------------------------------------------------+
 | OpenWrt                                                                 |
 |                                                                         |
 |                                                                         |
 |                                                                         |
 |                                                                         |
 |                                                                         |
 |                                                                         |
 |                                                                         |
 |                                                                         |
 |                                                                         |
 |                                                                         |
 |                                                                         |
 +-------------------------------------------------------------------------+
      Use the ^ and v keys to select which entry is highlighted.
      Press enter to boot the selected OS, 'e' to edit the
      commands before booting, or 'c' for a command-line.


   The highlighted entry will be booted automatically in 1 seconds.
}}}


OpenWrt is booting...
{{{
  Booting 'OpenWrt'

root (hd0,0)
 Filesystem type is ext2fs, partition type 0x83
kernel /boot/openwrt-x86-2.4-vmlinuz blkmtd_device=/dev/hda2 blkmtd_sync=1 
root=/dev/mtdblock0 init=/etc/preinit noinitrd console=ttyS0,19200n8
   [Linux-bzImage, setup=0xa00, size=0xaa952]
boot
Linux version 2.4.30 (nthill@debian) (gcc version 3.4.4) #2 Tue Sep 20 04:20:11 CEST 2005
BIOS-provided physical RAM map:
 BIOS-e820: 0000000000000000 - 000000000009fc00 (usable)
 BIOS-e820: 000000000009fc00 - 00000000000a0000 (reserved)
 BIOS-e820: 00000000000f0000 - 0000000000100000 (reserved)
 BIOS-e820: 0000000000100000 - 0000000008000000 (usable)
 BIOS-e820: 00000000fff00000 - 0000000100000000 (reserved)
128MB LOWMEM available.
On node 0 totalpages: 32768
zone(0): 4096 pages.
zone(1): 28672 pages.
zone(2): 0 pages.
DMI not present.
Kernel command line: blkmtd_device=/dev/hda2 blkmtd_sync=1 root=/dev/mtdblock0 init=/etc/preinit noinitrd console=ttyS0,19200n8
Initializing CPU#0
Detected 266.645 MHz processor.
Calibrating delay loop... 532.48 BogoMIPS
Memory: 127516k/131072k available (1070k kernel code, 3168k reserved, 208k data, 64k init, 0k highmem)
Checking if this processor honours the WP bit even in supervisor mode... Ok.
Dentry cache hash table entries: 16384 (order: 5, 131072 bytes)
Inode cache hash table entries: 8192 (order: 4, 65536 bytes)
Mount cache hash table entries: 512 (order: 0, 4096 bytes)
Buffer cache hash table entries: 8192 (order: 3, 32768 bytes)
Page-cache hash table entries: 32768 (order: 5, 131072 bytes)
CPU: NSC Unknown stepping 01
Checking 'hlt' instruction... OK.
POSIX conformance testing by UNIFIX
PCI: PCI BIOS revision 2.01 entry at 0xf7861, last bus=0
PCI: Using configuration type 1
PCI: Probing PCI hardware
PCI: Probing PCI hardware (bus 00)
Linux NET4.0 for Linux 2.4
Based upon Swansea University Computer Society NET3.039
Initializing RT netlink socket
Starting kswapd
devfs: v1.12c (20020818) Richard Gooch (rgooch@atnf.csiro.au)
devfs: boot_options: 0x1
JFFS2 version 2.1. (C) 2001 Red Hat, Inc., designed by Axis Communications AB.
Squashfs 2.2 (released 2005/07/03) (C) 2002-2004, 2005 Phillip Lougher
pty: 256 Unix98 ptys configured
Serial driver version 5.05c (2001-07-08) with MANY_PORTS SHARE_IRQ SERIAL_PCI enabled
ttyS00 at 0x03f8 (irq = 4) is a 16550A
ttyS01 at 0x02f8 (irq = 3) is a 16550A
Software Watchdog Timer: 0.05, timer margin: 60 sec
Uniform Multi-Platform E-IDE driver Revision: 7.00beta4-2.4
ide: Assuming 33MHz system bus speed for PIO modes; override with idebus=xx
SC1200: IDE controller at PCI slot 00:12.2
SC1200: chipset revision 1
SC1200: not 100% native mode: will probe irqs later
    ide0: BM-DMA at 0xe000-0xe007, BIOS settings: hda:pio, hdb:pio
    ide1: BM-DMA at 0xe008-0xe00f, BIOS settings: hdc:pio, hdd:pio
hda: Hitachi XX.V.3.3.0.0, CFA DISK drive
hdb: HITACHI_DK23DA-20, ATA DISK drive
SC1200: set xfer mode failure
hdb: sc1200_set_xfer_mode(UDMA 2)
blk: queue c028b53c, I/O limit 4095Mb (mask 0xffffffff)
ide0 at 0x1f0-0x1f7,0x3f6 on irq 14
hda: attached ide-disk driver.
hda: 500400 sectors (256 MB) w/1KiB Cache, CHS=695/15/48
hdb: attached ide-disk driver.
hdb: host protected area => 1
hdb: 39070080 sectors (20004 MB) w/2048KiB Cache, CHS=2432/255/63, UDMA(33)
Partition check:
 /dev/ide/host0/bus0/target0/lun0: p1 p2
 /dev/ide/host0/bus0/target1/lun0: p1 p2 p3
 /dev/ide/host0/bus0/target0/lun0: p1 p2
blkmtd: mtd0: [/dev/hda2] erase_size = 128KiB
blkmtd: version 1.10
Initializing Cryptographic API
NET4: Linux TCP/IP 1.0 for NET4.0
IP Protocols: ICMP, UDP, TCP, IGMP
IP: routing cache hash table of 1024 buckets, 8Kbytes
TCP: Hash tables configured (established 8192 bind 16384)
ip_conntrack version 2.1 (5953 buckets, 5953 max) - 320 bytes per conntrack
ip_tables: (C) 2000-2002 Netfilter core team
NET4: Unix domain sockets 1.0/SMP for Linux NET4.0.
NET4: Ethernet Bridge 008 for NET4.0
802.1Q VLAN Support v1.8 Ben Greear <greearb@candelatech.com>
All bugs added by David S. Miller <davem@redhat.com>
VFS: Mounted root (jffs2 filesystem) readonly.
Mounted devfs on /dev
Freeing unused kernel memory: 64k freed
insmod: diag.o: no module by that name found
/etc/preinit: 6: cannot create /proc/sys/diag: Directory nonexistent
cat: /proc/sys/reset: No such file or directory
[: 1: unknown operand
Could not open mtd device: rootfs
init started:  BusyBox v1.00 (2005.09.18-23:01+0000) multi-call binary

Please press Enter to activate this console. jffs2.bbc: SIZE compression mode activated.
natsemi dp8381x driver, version 1.07+LK1.0.17, Sep 27, 2002
  originally by Donald Becker <becker@scyld.com>
  http://www.scyld.com/network/natsemi.html
  2.4.x kernel port by Jeff Garzik, Tjeerd Mulder
eth0: NatSemi DP8381[56] at 0xc88ab000, 00:00:24:c2:47:c0, IRQ 10.
eth1: NatSemi DP8381[56] at 0xc88ad000, 00:00:24:c2:47:c1, IRQ 10.
eth2: NatSemi DP8381[56] at 0xc88af000, 00:00:24:c2:47:c2, IRQ 10.
device eth0 entered promiscuous mode
eth0: link up.
eth0: Setting full-duplex based on negotiated link capability.
eth0: Promiscuous mode enabled.
eth0: Promiscuous mode enabled.
eth0: Promiscuous mode enabled.
eth0: Promiscuous mode enabled.
eth0: Promiscuous mode enabled.
br0: port 1(eth0) entering learning state
br0: port 1(eth0) entering forwarding state
br0: topology change detected, propagating
}}}

== See also ==

 * [http://www.brixandersen.dk/papers/net4801/net4801.html GNU/Linux on a Soekris net4801]
----
CategoryOpenWrtPort
