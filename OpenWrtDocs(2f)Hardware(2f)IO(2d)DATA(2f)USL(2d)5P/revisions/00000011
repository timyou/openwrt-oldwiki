'''IO-DATA USL-5P'''


This is a NAS with 5 USB ports and 1 ethernet interface.

 * Bootloader: SH IPL+g with modifications from IO-DATA
 * CPU: SH7751R @ 240MHz (SH4)
 * Flash size: 512Kbyte (only for the bootloader)
 * RAM: 64MByte
 * Ethernet: Realtek RTL8139C+
 * Serial: yes, pinouts follow
 * CF slot: yes, the bootloader boots the OS from a CF card
 * USB: Yes, NEC USB 2.0 controller with 5 ports
 * Other: Buzzer, RTC


=== Serial pinout ===


{{{
   o   o   o   o     [battery]
  GND RxD TxD 3.3V
}}}

Serial settings are 9600, 8n1.

=== Boot ===

The original firmware boots immediately after the bootloader initialization is complete, there is no way to abort it. Also there is no known way to login to it, so the only way to install OpenWrt on this device is to change the contents of the CF card.


'''OpenWrt dmesg'''

This is based on the 2.6.22-rc4 patchset made by Kaloz, so don't let the revision number cheat you. Patches will be done after a major cleanup, since the toolchain, the kernel, the kenel modules and the userland is a bit messy right now. Anyway, we've got a lift-off, Houston.

[http://trash.uid0.hu/openwrt/usl-5p_openwrt-dmesg.txt dmesg]


UPDATE: port updated to 2.6.22-rc6.


'''Original dmesg'''

This is out-of-date, but you can still reach it [http://trash.uid0.hu/openwrt/usl-5p_original-dmesg.txt here].


=== Installation instructions ===

This is going to be very dirty, so check your hats.

First you'll need the following [http://trash.uid0.hu/openwrt/landisk-install.tgz tarball], which I collected from various places. You'll also need an empty CF card with virtually any size you like - the original one could be used also, but save its contents in case if anything goes wrong.

I'll assume /dev/sdb as the CF card. 

 * Create a new partition on it.

{{{
# fdisk /dev/sdb

Command (m for help): p

Disk /dev/sdb: 32 MB, 32047104 bytes
1 heads, 62 sectors/track, 1009 cylinders
Units = cylinders of 62 * 512 = 31744 bytes

   Device Boot      Start         End      Blocks   Id  System

Command (m for help): n
Command action
   e   extended
   p   primary partition (1-4)
p
Partition number (1-4): 1
First cylinder (2-1009, default 2): 
Using default value 2
Last cylinder or +size or +sizeM or +sizeK (2-1009, default 1009): 
Using default value 1009

Command (m for help): w
The partition table has been altered!

Calling ioctl() to re-read partition table.
Syncing disks.
#
}}}

 * Create an EXT3 filesystem on it.

{{{
# mkfs.ext3 /dev/sdb1
mke2fs 1.40-WIP (14-Nov-2006)
[...]

#
}}}

 * Mount the new filesystem into /mnt and untar the compressed file of the rootfs created by the toolchain onto the CF.

{{{
# tar xzvf openwrt-landisk-2.6-rootfs.tgz -C /mnt
[...]
#
}}}

Everything went normal up to this point, now comes the dirty part.

 * Untar the landisk-install.tgz onto the CF

{{{
# tar xzvf landisk-install.tgz -C /mnt
[...]
#
}}}

 * Copy the kernel into CF's /boot

{{{
# cp openwrt-landisk-2.6-zImage /mnt/boot
}}}

 * Check /mnt/etc/lilo.conf.cross to get familiar with it

 * Create devices for sda, sda1, sdb, sdb1 on the CF - this is required for LILO

NOTE: If your CF card is not shown as sdb, rather than as sdc or sdd, you have to use the correct device name and its minor numbers, and modify /mnt/etc/lilo.conf.cross according to it.

{{{
# mknod /mnt/dev/sda b 8 0
# mknod /mnt/dev/sda1 b 8 1
# mknod /mnt/dev/sdb b 8 16
# mknod /mnt/dev/sdb1 b 8 17
}}}

 * Run LILO

{{{
# /mnt/sbin/lilo.x86 -r /mnt -C /etc/lilo.conf.cross
Added openwrt *
#
}}}

Now you can boot the CF in your USL-5P.
