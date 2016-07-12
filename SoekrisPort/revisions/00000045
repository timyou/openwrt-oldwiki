[[TableOfContents]]
== Introduction ==
The SoekrisPort is an attempt to use OpenWrt on PC-based embedded computer boards sold by [http://www.soekris.com/ Soekris Engineering], starting with the [http://www.soekris.com/net4801.htm net4801] board.

The net4801 has a CompactFlash socket, as well as an IDE interface for 2.5" HDD. The installation procedure described here is for CF setup. You can use whatever size (from 8MB to 4GB) for your CF.

It also works on the slightly cheaper but less powerful net4501

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
(aside:  speed=38400 make also work for you)

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

== Booting with qemu ==

This boots the image within a virtual machine on your desktop PC, and is very easy to do. See ["RunningKamikazeOnQEMUHowTo"]

It lets you try out the various flash partitioning schemes without having to burn anything to flash, or indeed, without having a real Soekris :-)

== Booting using PXE ==

You can boot the Soekris directly over a network. This is done automatically
if there is no compact flash card installed, or you can force it by hitting
Ctrl-P then typing "boot f0" at the combios prompt.

You need to set up a server for the machine to boot against. The
instructions here are for an Ubuntu Linux system; you may have to adjust
them for your own system.

=== static IP address ===

Configure your server with a static IP address on a spare interface.
Here I'm assuming it's eth0 and you are going to use 192.168.1.250

/etc/network/interfaces
{{{
...
auto eth0
iface eth0 inet static
address 192.168.1.250
netmask 255.255.255.0
...
}}}

=== dhcp server ===

{{{
# apt-get install dhcp3-server
}}}

/etc/dhcp3/dhcpd.conf
{{{
ddns-update-style none;

#option domain-name "example.org";
#option domain-name-servers ns1.example.org, ns2.example.org;

default-lease-time 600;
max-lease-time 7200;

log-facility daemon;

subnet 192.168.1.0 netmask 255.255.255.0 {
  range 192.168.1.100 192.168.1.199;
  option routers 192.168.1.250;
  next-server 192.168.1.250;
  filename "pxelinux.0";
}
}}}

/etc/default/dhcp3-server
{{{
INTERFACES="eth0"
}}}

=== tftp server ===

The special requirement here is that your tftp server must support the
'tsize' extension. The standard Ubuntu one doesn't; you need tftpd-hpa

{{{
# apt-get install tftpd-hpa
}}}

/etc/inetd.conf
{{{
tftp           dgram   udp     wait    root  /usr/sbin/in.tftpd /usr/sbin/in.tftpd -s /var/lib/tftpboot
}}}

/etc/default/xinetd
{{{
XINETD_OPTS="-stayalive -inetd_compat"
}}}

=== pxelinux.0 ===

{{{
# apt-get install syslinux
# cd /var/lib/tftpboot
# cp /usr/lib/syslinux/pxelinux.0 .
# mkdir pxelinux.cfg
}}}

Now also copy your kernel image and/or init ramdisk into this directory. For
example, if you are using the single kernel+ramdisk image, you could copy it
here as vmlinuz.ram

Now you need to create the pxeboot config file:

/var/lib/tftpboot/pxelinux.cfg/default
{{{
serial 0 38400 0x303
console 0
label linux
  kernel vmlinuz.ram
  append init=/etc/preinit console=tty0 console=ttyS0,38400n8 reboot=bios
}}}

("console 0" stops the loader from writing to the video console as well, which the Soekris BIOS redirects to the serial port, causing characters to be doubled)

=== Final checks ===

Make sure everything is running:

{{{
# ifup eth0
# /etc/init.d/dhcp3-server start
# killall -1 xinetd
}}}

Plug in your Soekris and cross your fingers. For some reason pxeboot seems
to give its output in a tiny 16-character window; you can use the 'capture
to file' option in minicom (ctrl-A L) to get more readable info.

More info on pxelinux.0 is at http://syslinux.zytor.com/pxe.php, and the
configuration file format at http://syslinux.zytor.com/faq.php

=== PXE boot ramdisk with additional files ===

A 'ramdisk' kernel is actually a kernel with a built in cpio.gz archive which
is expanded into an initramfs.

If you want to add extra files, this can be done very
easily. You don't need to rebuild the kernel to change its cpio.gz; you can
supply a second cpio.gz file at boot time, and the kernel will unpack
this one as well. Any files in this archive will override ones with the same
name in the kernel's archive.

If you look in the kernel source, this process is explained in
[http://www.mjmwired.net/kernel/Documentation/filesystems/ramfs-rootfs-initramfs.txt Documentation/filesystems/ramfs-rootfs-initramfs.txt]
and it also includes a script which will build a suitable cpio.gz image for
you.

Once you have one, all you need to do is copy it to /var/lib/tftpboot/ and
update your pxelinux.cfg/default file to reference it:
{{{
serial 0 38400 0x303
label linux
  kernel vmlinuz.ram
  append initrd=root.cpio.gz init=/etc/preinit console=tty0 console=ttyS0,38400n8 reboot=bios
}}}

When the device next boots, the root filesystem will be the original
Kamikaze initramfs with your cpio files added.

=== Writing to flash after PXE booting ===

Some Soekris models, e.g. net4526, have flash soldered on board and no CF slot. In this case, you'll have to use PXE boot to install the first flash image.

Options for doing this include:

 * Boot an OpenWrt image over PXE as above, then use the command line to fetch an image and burn it to flash (e.g. wget and dd)
 * [http://pyramid.metrix.net/trac/wiki/InstallingPyramid Metrix pyramid liveCD] or [http://dl.metrix.net/support/pxeboot/ pxeboot files]
 * [http://www.feyrer.de/g4u/ g4u] ("ghost for unix")

== Flash partitioning ==

A Compact Flash card contains in-built hardware to map itself to an
IDE-compatible interface, and so when the Soekris boots it thinks it is
talking to a hard drive.

=== ext2 ===

The ext2 image contains two DOS-style partitions:

 * /dev/hda1: ext2 filesystem containing /boot (grub + kernel)
 * /dev/hda2: ext2 filesystem containing /

At bootup, /dev/hda2 is mounted directly onto / in the same way as a normal
desktop system.

If using the ext2 image with a compact flash card, you should be aware that
the 'noatime' mount option is NOT set by default. This means that every time
you *read* a file, a *write* is done to update the access time in the inode.
Since CF cards have limited write cycles, you may wish to avoid this. To do
so, modify /sbin/mount_root as follows:

{{{
...
    mount -o remount,rw,noatime /dev/root /
}}}

This approach is probably the simplest way to run OpenWrt, but it relies on
the flash card performing its own wear levelling. The other problem is that
the default startup scripts don't run e2fsck; if you unplug the power without
shutting down cleanly, you can end up with a corrupted root filesystem which
won't be repaired.

=== jffs2 ===

The jffs2 image contains two DOS-style partitions:

 * /dev/hda1: ext2 filesystem containing /boot (grub + kernel)
 * /dev/hda2: flash emulation
    * /dev/mtdblock0: "rootfs": jffs2 filesystem containing /

(FIXME: should you choose the 64K, 128K or 256K jffs2 image? Does it
matter?)

When you are running the image, you can mount hda1 to look at its contents
or update it. /dev/hda2 is mapped to /dev/mtdblock0 using block2mtd, so as
to emulate a "real" flash device with its own partitioning scheme; you
should not touch /dev/hda2 directly.

{{{
root@OpenWrt:/# mkdir /tmp/mnt
root@OpenWrt:/# mount /dev/hda1 /tmp/mnt
root@OpenWrt:/# ls -lR /tmp/mnt
/tmp/mnt:
drwxr-xr-x    3 1000     100          1024 Jul 23  2007 boot
drwx------    2 root     root       230400 Jul 26  2007 lost+found

/tmp/mnt/boot:
drwxr-xr-x    2 1000     100          1024 Jul 23  2007 grub
-rw-r--r--    1 1000     100        978192 Jul 26  2007 vmlinuz

/tmp/mnt/boot/grub:
-rw-r--r--    1 1000     100          7584 Jul 23  2007 e2fs_stage1_5
-rw-r--r--    1 1000     100           570 Jul 26  2007 menu.lst
-rw-r--r--    1 1000     100           512 Jul 23  2007 stage1
-rw-r--r--    1 1000     100        102378 Jul 23  2007 stage2

root@OpenWrt:/# cat /proc/mtd
dev:    size   erasesize  name
mtd0: 01020000 00020000 "rootfs"
root@OpenWrt:/#
}}}

=== squashfs ===

The squashfs image contains two DOS-style partitions:

 * /dev/hda1: ext2 filesystem containing /boot as above
 * /dev/hda2: flash emulation
   * /dev/mtdblock0: "rootfs": squashfs root filesystem
   * /dev/mtdblock1: "rootfs_data": jffs2 filesystem unioned over root

This works in the same way as the traditional OpenWrt Broadcom platform: any
spare space in /dev/hda2 is dynamically created as a jffs2 partition, which
overlays the fixed squashfs root. Should this become corrupted, you should
still be able to boot using squashfs on its own. You can also type
"firstboot" to forcibly erase the jffs2 part.

(Presumably, grub doesn't have sufficient knowledge of mtd partitioning
and/or squashfs in order to boot directly, and which is why the boot
partition is still needed)

=== tgz ===

If you build from source, another image option available is "tgz". This just
gives you the following files:

{{{
openwrt-x86-2.6-rootfs.tgz    # the root filesystem
openwrt-x86-2.6-vmlinuz       # the kernel
}}}

It's up to you to install them in a way which makes sense on your target
platform.

If you convert the .tar.gz file to .cpio.gz, you can boot the kernel plus
the root filesystem in a ramdisk like this:

{{{
title   OpenWrt (sep ramdisk)
root    (hd0,0)
kernel  /boot/openwrt-x86-2.6-vmlinuz init=/etc/preinit console=tty0 console=ttyS0,38400n8 reboot=bios
initrd  /boot/openwrt-x86-2.6-rootfs.cpio.gz
boot
}}}

A simple way to convert the tar file to cpio is like this:

{{{
# mkdir tmp
# cd tmp
# tar -xvzf ../openwrt-x86-2.6-rootfs.tgz
# find . | cpio -o -H newc | gzip -9 > ../openwrt-x86-2.6-rootfs.cpio.gz
# cd ..
# rm -rf tmp
}}}

=== ramdisk ===

If you build from source, the final image option available is "ramdisk". If
you select this, all the other images are disabled.

This gives you a single file, containing both the kernel and a ramdisk:

{{{
openwrt-x86-2.6-vmlinuz
}}}

This is particularly convenient for pxebooting. However you can also put it
into a single partition with grub (or [http://syslinux.zytor.com/ syslinux], or even freedos and loadlin). This
should make it very easy to manage remote upgrading of devices, since only a
single file needs to be replaced.

It can be booted using something like this (grub):

{{{
title   OpenWrt ramdisk
root    (hd0,0)
kernel  /boot/vmlinuz init=/etc/preinit console=tty0 console=ttyS0,38400n8 reboot=bios
boot
}}}

You can also add an initrd file, which is a cpio.gz archive, to add additional
files to the root filesystem at boot time, by adding "initrd /boot/root.cpio.gz"

Running with the root filesystem in RAM will obviously use more RAM, but on a Soekris
with 64MB or more, this probably is
not an issue. The downside is that no state is kept between reboots, not
even the dropbear ssh host key.

=== Updating the image files offline ===

If you wish to modify the image files on the build system rather than on the target,
you can do this using a loopback mount. However this is a bit tricky because the
image consists of a partition table followed by /dev/hda1 partition followed by
/dev/hda2 partition. To mount either of the partitions you have to tell the loopback
device what offset to use.

Example: let's suppose you want to mount the first partition (the boot partition)
to update the grub menu.lst. First, use fdisk to find the offset to the first
partition:

{{{
$ fdisk bin/openwrt-x86-2.6-ext2.image
You must set cylinders.
You can do this from the extra functions menu.

Command (m for help): x

Expert command (m for help): p

Disk bin/openwrt-x86-2.6-ext2.image: 16 heads, 63 sectors, 0 cylinders

Nr AF  Hd Sec  Cyl  Hd Sec  Cyl     Start      Size ID
 1 80   1   1    0  15  63    8         63       9009 83
 2 00   1   1    9  15  63   41       9135      33201 83
 3 00   0   0    0   0   0    0          0          0 00
 4 00   0   0    0   0   0    0          0          0 00

Expert command (m for help): q
}}}

Here you can see the start offset of the first partition is 63 sectors, which is
63 x 512 = 32256 bytes.

{{{
# losetup -o 32256 /dev/loop0 bin/openwrt-x86-2.6-ext2.image
# mount /dev/loop0 /mnt
# vi /mnt/boot/grub/menu.lst
... make changes and save
# umount /mnt
# losetup -d /dev/loop0
}}}

The last two steps - unmounting the filesystem ''and'' disconnecting the loopback device from the
image file - are very important. If you miss them, you are likely to corrupt the image.

== User data partition ==

Given that 1-4GB flash cards are now very cheap, you probably want the rest
of the space to be available for data storage. One option is to make a
bigger hda2 partition, but this risks losing your user data when you upgrade
Openwrt itself.

A safer option is to create a new partition /dev/hda3 for the remaining
space on the card, and create another filesystem within it.

=== ext2 data partition ===

The partitioning can be done on the target device:

{{{
# ipkg update
# ipkg install fdisk
# fdisk /dev/hda
-- create new primary partition 3 (see below)
-- a reboot may now be required
}}}

Alternatively the partition table can be updated offline within the image,
which is useful if you need to burn the image onto multiple flash cards.
Beware that you need to know the exact size of your flash card, or else
allow sufficient leeway, because cards are not as big as they advertise. For
example, if I insert a Fuji "4GB" 40x card into a PC reader, I see

{{{
[18997894.296000] SCSI device sdb: 7928928 512-byte hdwr sectors (4060 MB)
}}}

Ignore the "4060MB". The actual size is 7,928,928/2 = 3,964,464KB, which is
about 3871.5MB.

Now convert this into the number of cylinders, here using 1008 sectors per
cylinder to match the existing partition table: 7928928 / 1008 = 7866
cylinders exactly. Round down if necessary.

{{{
$ fdisk -C 7866 openwrt-x86-2.6-jffs2-128k.image

The number of cylinders for this disk is set to 7866.
There is nothing wrong with that, but this is larger than 1024,
and could in certain setups cause problems with:
1) software that runs at boot time (e.g., old versions of LILO)
2) booting and partitioning software from other OSs
   (e.g., DOS FDISK, OS/2 FDISK)

Command (m for help): p

Disk openwrt-x86-2.6-jffs2-128k.image: 0 MB, 0 bytes
16 heads, 63 sectors/track, 7866 cylinders
Units = cylinders of 1008 * 512 = 516096 bytes

                           Device Boot      Start         End      Blocks   Id System
openwrt-x86-2.6-jffs2-128k.image1   *           1           9        4504+  83 Linux
openwrt-x86-2.6-jffs2-128k.image2              10          42       16600+  83 Linux

Command (m for help): n
Command action
   e   extended
   p   primary partition (1-4)
p
Partition number (1-4): 3
First cylinder (43-7866, default 43):
Using default value 43
Last cylinder or +size or +sizeM or +sizeK (43-7866, default 7866):
Using default value 7866

Command (m for help): t
Partition number (1-4): 3
Hex code (type L to list codes): 83

Command (m for help): p

Disk openwrt-x86-2.6-jffs2-128k.image: 0 MB, 0 bytes
16 heads, 63 sectors/track, 7866 cylinders
Units = cylinders of 1008 * 512 = 516096 bytes

                           Device Boot      Start         End      Blocks   Id System
openwrt-x86-2.6-jffs2-128k.image1   *           1           9        4504+  83 Linux
openwrt-x86-2.6-jffs2-128k.image2              10          42       16600+  83 Linux
openwrt-x86-2.6-jffs2-128k.image3              43        7866     3943296   83 Linux

Command (m for help): w
The partition table has been altered!

Calling ioctl() to re-read partition table.

WARNING: Re-reading the partition table failed with error 25: Inappropriate ioctl for device.
The kernel still uses the old table.
The new table will be used at the next reboot.
Syncing disks.
}}}

(You can ignore those warnings when writing the partition table)

Creating the ext3 filesystem itself is best done on the target system,
otherwise you'll end up with a 4GB image to copy.

{{{
# ipkg install e2fsprogs
# mke2fs /dev/hda3     # quite slow as it writes inode tables and superblocks (~7.5mins for 4GB)
...
# mkdir /opt
# mount -o noatime /dev/hda3 /opt
}}}

The "noatime" option minimises flash wear; without it, the access time in
the inode is updated each time you read a file.

By default 5% of storage space is reserved for root. Use "-m 0" on mke2fs
command line to make the whole space available, or install tune2fs and use
that.

In a startup script, you should run 'e2fsck -y /dev/hda3' (from the e2fsprogs
package) to correct any problems due to unclean shutdown, and then mount the device.

Kamikaze 7.10 will gain a feature to mount filesystems at bootup by listing them
in /etc/config/fstab - however at the time of writing it did not perform an
fsck.

Add '-j' to the mke2fs command line to get an ext3 journal, which should speed
up recovery after an unclean shutdown. (Or use 'tune2fs -j' to add a journal
to an existing ext2 partition). You also need to ''mount -t ext3 ...' of course,
and this requires the kmod-fs-ext3 package.

=== jffs data partition ===

/!\ This gives kernel panics after rebooting if you use it with the jffs or squashfs images,
presumably because they already have a block2mtd partition. Maybe block2mtd
can't keep track of multiple partitions at once. Therefore this is only safe
if you are using the ext2 or ramdisk images.

First create a /dev/hda3 partition as above using fdisk. Then on the target
system:

{{{
# echo "/dev/hda3,131072,user_data" > /sys/module/block2mtd/parameters/block2mtd
# mtd unlock user_data
# mtd erase user_data    # takes a VERY LONG time on 4GB flash
# cat /proc/mtd
... look for the user_data line, check it's /dev/mtdblock0
# mkdir /opt
# mount /dev/mtdblock0 /opt -t jffs2
}}}

You should also be able to perform this set offline, if your desktop system
has mtdblock and loopback, as described
[http://gentoo-wiki.com/Mounting_a_block_device_with_JFFS2 here]

Now all you need is a startup script to mount this at boot time:

{{{
#!/bin/sh /etc/rc.common
# Copyright (C) 2006 OpenWrt.org

START=11

partition="user_data"
mountpoint="/opt"

jffs2_ready () {
        mtdpart="$(find_mtd_part $partition)"
        magic=$(hexdump $mtdpart -n 4 -e '4/1 "%02x"')
        [ "$magic" != "deadc0de" ]
}

start() {
        grep $partition /proc/mtd >/dev/null 2>/dev/null || {
                echo '/dev/hda3,131072,user_data' > /sys/module/block2mtd/parameters/block2mtd
                sleep 2
        }
        mtd unlock $partition
        jffs2_ready && {
                mount "$(find_mtd_part $partition)" $mountpoint -t jffs2
        }
}

stop() {
        umount $mountpoint
}
}}}

== Hardware real-time clock (RTC) ==

The net4501/4801 has an on-board RTC. To use it, build busybox with hwclock support. In 'make menuconfig':

{{{
Base System > Busybox
              Configuration > Linux System Utilities > hwclock
}}}

To initialise the RTC, set the system date using 'date' (or 'ntpclient') and then write it to the RTC using 'hwclock -w'.
To load the system time from the RTC at bootup, you will need a script like this in /etc/init.d

{{{
#!/bin/sh /etc/rc.common
# Hardware clock
#
# This file handles setting the system time from hardware clock at boot
START=11

start()
{
        hwclock -s
}
}}}

Enable it with '/etc/init.d/hwclock enable'

== Error LED ==

net48xx integrated peripheral drivers are built if you choose the 'Soekris net48xx' target.
(FIXME: document how to use them)

For the net4501, you can just build the Generic target as it doesn't have any of the net48xx hardware.
To control the error LED on net4501, see https://dev.openwrt.org/ticket/2634

== See also ==

 * ["RunningKamikazeOnQEMUHowTo"]
 * ["RunningKamikazeOnVMwareHowTo"]
 * [http://www.brixandersen.dk/papers/net4801/net4801.html GNU/Linux on a Soekris net4801]
 * [http://pyramid.metrix.net/trac/wiki/InstallingPyramid/PxeBootLiveCD Pyramic PxeBoot Live CD]
 * [http://gentoo-wiki.com/Mounting_a_block_device_with_JFFS2 Mounting a block device with JFFS2 (Gentoo wiki)]
 * [http://maemo.org/community/wiki/ModifyingRootImage Modifying a JFFS2 image]

----
CategoryOpenWrtPort
Categoryx86Device
