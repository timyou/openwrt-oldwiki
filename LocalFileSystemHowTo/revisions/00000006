OpenWrtDocs [[TableOfContents]]

== Introduction ==

This HOWTO describes how to manage local filesystems on your router, and how you can access this filesystem on remote machines.

== Creating Local Filesystem ==

There are several types of local filesystem:

 * all !OpenWrt devices can support a small memory based filesystem, the contents of which are lost on reboot ... create files in /tmp,

 * all !OpenWrt devices can support a small flash based filesystem, the contents of which are kept across reboots, but changes to which may reduce the remaining endurance of the flash memory chips ... create files in /,

 * some !OpenWrt devices can support USB storage based filesystems, see UsbStorageHowto for how to configure !OpenWrt for USB storage,

 * some !OpenWrt devices can support IDE storage based filesystems, see IdeStorageHowTo for how to configure !OpenWrt for IDE storage,

=== Configure Block Device ===

 * skip this subsection if you wish to use the memory or flash filesystem,
 * for USB storage, see UsbStorageHowto,
 * for IDE storage, see IdeStorageHowTo,
 * for USB or IDE, the file ''/proc/partitions'' will show the unpartitioned disk space, for example for an 80GB IDE disk on an Asus WL-HDD:
 {{{
major minor  #blocks  name

   3     0   78150744 ide/host0/bus0/target0/lun0/disc
}}}

=== Partition Block Device ===

 * configure your device to use the backports repository, see ["OpenWrtDocs/Packages"] for instructions, then install the ''fdisk'' package:
 {{{
ipkg install fdisk
}}}
 * run ''fdisk BLOCKDEVICE'',
 * create partitions, write, exit,
 * check that ''/proc/partitions'' has been updated to show the partitions created, for example:
 {{{
major minor  #blocks  name

   3     0   78150744 ide/host0/bus0/target0/lun0/disc
   3     1   39053983 ide/host0/bus0/target0/lun0/part1
   3     2   39054015 ide/host0/bus0/target0/lun0/part2
   3     3      40162 ide/host0/bus0/target0/lun0/part3
}}}

=== Configure Swap Partition (Optional) ===

 * install the ''swap-utils'' package (http://downloads.openwrt.org/backports/rc5/swap-utils_2.12r-1_mipsel.ipk),
 * run ''mkswap PARTITION'', where PARTITION is the partition block device you wish to use as swap partition,
 * write an init.d script to run ''swapon PARTITION'',
 * test the script before rebooting,

=== Create Filesystem ===

 * configure your device to use the backports repository, see ["OpenWrtDocs/Packages"] for instructions, then install the ''e2fsprogs'' package:
 {{{
ipkg install e2fsprogs
}}}
 * create a symbolic link required by ''mke2fs'', using the command ''ln -s /proc/mounts /etc/mtab'',
 * run ''mke2fs -j PARTITION'', where PARTITION is the partition block device you wish to use for the filesystem,

=== Check Filesystem on Reboot ===

 * write an init.d script to run ''e2fsck PARTITION'',
 * test the script before rebooting,
 * ''e2fsck'' may fail on large disks if there is not enough memory, consider adding a swap partition, even if it is only used during ''e2fsck'',

=== Mount Filesystem on Reboot ===

 * write an init.d script to run ''mount -t ext3 PARTITION'',
 * test the script before rebooting,

== Sharing Local Filesystem ==

You may wish to be able to access the !OpenWrt local filesystem from remote hosts.  There are several methods available.

=== NFS ===

 * install the ''nfs-server'' package,
 * configure ''/etc/exports'' file,
 * reboot.

Note: there is no need to install ''kmod-nfs'', as this is only used for mounting remote filesystems over NFS.  See RemoteFileSystemHowTo.

=== scp ===

 * already installed by default,
 * files can be copied to or from local filesystems,
 * example, command on a remote system to copy ipkg.conf from the !OpenWrt device to disk:
 {{{
scp root@openwrt:/etc/ipkg.conf .
}}}

=== rsync ===

 * install the ''rsync'' package,
 * configure ''/etc/rsyncd.conf'',
 * write an init.d script to start ''rsync --daemon'',

=== Samba ===

 * see the SambaHowto
