This explanation taken from [http://openwrt.org/forum/viewtopic.php?p=3123#3123].

You should probably also read the more recent posting at [http://forum.openwrt.org/viewtopic.php?pid=24157#p24157]
---------------------------

Everything is stored on the flash chip. The size of the flash chip depends on what type of hardware you're using but it's generally 4M. The layout of the flash chip is as follows:

{{{[bootloader][firmware][nvram]}}}

There's no actual partition table, the layout is simply hardcoded.

The first 256k is reserved for the bootloader, either [:OpenWrtDocs/Customizing/Firmware/CFE:CFE] or PMON. Both bootloaders are identical as far as the user is concerned, performing the task of initializing the hardware, validating and loading the firmware. If boot_wait is set or the firmware fails to validate or boot then the bootloader is also responsible for the tftp server that allows the firmware to be recovered.

The last 64k is reserved for nvram, holding the configuration for the router. As a precaution, if nvram doesn't exist it gets automatically created by the bootloader using defaults stored in the bootloader.

The firmware starts at the 256k mark and can potentially take all space between the bootloader and nvram. Generally speaking the firmware does not take the entire space, leaving a large gap between the end of firmware and the start of nvram.

The openwrt layout -- Way too much information

When booted into linux, the kernel's mtd driver is responsible for access to the flash (memory technology device). The flash layout is hardcoded into the mtd code, creating a set of /dev/mtd* devices to represent the various partitions.

If you look at /proc/mtd you'll see the partitions created by mtd:
{{{
dev:    size   erasesize  name
mtd0: 00040000 00010000 "pmon"
mtd1: 003b0000 00010000 "linux"
mtd2: 000d1408 00010000 "rootfs"
mtd3: 00010000 00010000 "nvram"
mtd4: 00230000 00010000 "OpenWrt"
}}}

If you're paying close attention, you might notice that the sizes actually add up to 7M when the device this was taken from only has a 4M flash. The reason for this is that the mtd partitions are actually overlapped.

{{{[pmon][linux [rootfs][OpenWrt]][nvram]}}}

The bootloader from the previous diagram has been replaced by "pmon" -- pmon is just the name of the partition, we don't bother to check if it actually is PMON or CFE. Nvram is still at the end and the space beteen has been replaced by "linux".

The linux partition is more than just the firmware, it's the entire space between the bootloader and the nvram. At the start of the linux partition is the actual firmware which contains the kernel and squashfs filesystem.

The rootfs partition is calculated at kernel bootup to be the location of the squashfs filesystem contained within the firmware. Squashfs is the readonly filesystem which contains just barely enough applications to boot the router and perform the basic tasks. The idea is to have the squashfs filesystem as small as possible to give as much space as possible to the writable filesystem. Idealy everyone would use the same firmware (squashfs) and only customize it via packages.

Between the end of the firmware and the start of nvram is the OpenWrt partition. This is holds the writable jffs2 partition, by default nearly everything in this partition is just a symlink to files on the squashfs filesystem mounted as /rom. The only actual files on this partition are those installed from packages or customized copies of files from the squashfs filesystem.
Note: As of White Russian RC6 and Kamikaze svn r5544 (for brcm platforms) mini_fo is used to overlay the rom and jffs2 partitons, thereby eliminating the need for symlinks on the jffs2 partition to files located in /rom.
