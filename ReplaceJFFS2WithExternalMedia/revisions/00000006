First of all, credit for this discovery goes to forum2006. I am reposting his <url>original forum post</url> here to keep it from getting buried.

== 1. Introduction ==
This guide describes how to use your USB stick or your MMC/SD card for storing pakages and files instead of using the JFFS2 partion on your flash chip. / in this case is the SquashFS partition on the flash chip and the writable EXT2 partion is on your external media. With little modifications you can use this guide also for MMC/SD card. Tested with Kamikaze pre1 on a Asus WL-500GD and a 512MB Sundisk Cruzer Mini USB 2.0 stick. With little modifications it will also work with WhiteRussian 0.9. With this guide you do not have to mess around with PATH, LD_LIBRARY_PATH or create symlinks anymore.

NOTE: This notes are taken out of my personal notes. They may be incomplete or does not fit your needs.

Makes the following Wiki pages obsolete:

 . - PackagesOnExternalMediaHowTo
 - UsbStorageHowto (section 4)
== 2. Requirements ==
 . - a router with external storage media like USB stick or MMC/SD card
 - the OpenWrt ImageBuilder
== 3. USB media ==
The script which we will be editing is called mount_root. It can be found in the /sbin directory on your wrt enabled router. If you have not yet installed OpenWRT or are going to a new version (From WhiteRussian to Kamikaze) you can find it at ./package/base-files/files/sbin/mount_root in your ImageBuilder directory.

1. Create the directory you will keep your modified files in:

{{{
mkdir -p /openwrt/files/sbin/
}}}
2. Copy that mount_root file mentioned earlier into the directory you just created and chomod it to make it executable

{{{
cp .packages/base-fies/files/sbin/mount_root /openwrt/files/sbin/mount_root
chmod +x /openwrt/files/sbin/mount_root
}}}
3. Create a new image with the ImageBuilder

{{{
make clean image \
    PACKAGES="fdisk e2fsprogs kmod-fs-ext2 kmod-usb-core kmod-usb-ohci kmod-usb-storage kmod-usb-uhci kmod-usb2"\
    FILES="/openwrt/files/"
Note: the packages listed under PACKAGES should be in your OpenWRT-ImageBuilder/packages/ directory.
}}}
4. Reflash your router with the new image. See ["Installing"]

5. Next partition and format your USB stick with EXT2 filesystem.

 a. Figure out where your drive is mounted. This can usually be discovered by running 'dmesg'.
 a. Fdisk the media, create a partition scheme that suits you.
 a. Format that partition with whichever filesystem you chose. Note that this example supports ext2, any extra filesystems would require the proper modules to be included, and loaded.
dmesg output on Kamikaze pre1 Broadcom 2.4:

{{{
scsi0 : SCSI emulation for USB Mass Storage devices
  Vendor:   CENTON  Model: DS    PRO    2GB  Rev: 0.00
  Type:   Direct-Access                      ANSI SCSI revision: 02
Attached scsi removable disk sda at scsi0, channel 0, id 0, lun 0
SCSI device sda: 4030463 512-byte hdwr sectors (2064 MB)
sda: Write Protect is off
Partition check:
 /dev/scsi/host0/bus0/target0/lun0: p1 p2
WARNING: USB Mass Storage data integrity not assured
USB Mass Storage device found at 2
}}}
This example tells me that my USB flash drive is at /dev/scsi/host0/bus0/target0/lun0/disc (disc is the physical drive, just like /dev/hda is the physical drive), we'll use this to fdisk.

{{{
fdisk /dev/scsi/host0/bus0/target0/lun0/disc
<we made 1 partition the full size of the drive>
mke2fs /dev/scsi/host0/bus0/target0/lun0/part1
}}}
Note: If your device isn't the same as what you set in /openwrt/files/sbin/mount_root, then modify it and re-build and reflash your router.

6. Reboot again and check with 'df -h' if /jffs is on your USB stick. Your df -h output should be similar to this, with your /jffs directory mounted on whichever device your usb media was placed at.

{{{
root@OpenWrt:/# df -h
Filesystem                Size      Used Available Use% Mounted on
none                     14.7M     20.0k     14.7M   0% /tmp
tmpfs                   512.0k         0    512.0k   0% /dev
/dev/scsi/host0/bus0/target0/lun0/part1
                        480.9M      9.0M    447.4M   2% /jffs <--- this is my USB stick with EXT2 filesystem
/jffs                   960.0k    960.0k         0 100% /
root@OpenWrt:/#
}}}
From now on you can use ipkg the normal way and all packages or modified files will be stored on your USB stick.

modified /sbin/mount_root script:

=== Kamikaze 2.6 ===
{{{
                . /bin/firstboot
                mtd unlock rootfs_data
                jffs2_ready && {
                       echo "loading USB and ext2 modules"
                       insmod usbcore
                       insmod ext2
                       insmod ohci-hcd
                       insmod uhci-hcd
                       insmod ehci-hcd
                       insmod scsi_mod
                       insmod sd_mod
                       insmod usb-storage
                       # lsmod > /tmp/x.txt
                       sleep 2
                       mknod /dev/sda b 8 0
                       mknod /dev/sda1 b 8 1
                       # ls -al /dev/sda* >> /tmp/x.txt
                       echo "switching to jffs2"
                       # mount "$(find_mtd_part rootfs_data)" /jffs -t jffs2 && \
                       mount /dev/sda1 /jffs -t ext2 && \
                               fopivot /jffs /rom
                } || {
                       echo "jffs2 not ready yet; using ramdisk"
}}}
=== Kamikaze 2.4 ===
Note: This contains extra debugging output, you can remove it if you wish.

{{{
               . /bin/firstboot
                #mtd unlock rootfs_data
                jffs2_ready && {
                        echo "....loading modules...." > /tmp/usbstorage.log
                        insmod usbcore >> /tmp/usbstorage.log 2>> /tmp/usbstorage.log
                        insmod ext2 >> /tmp/usbstorage.log 2>> /tmp/usbstorage.log
                        insmod jbd >> /tmp/usbstorage.log 2>> /tmp/usbstorage.log
                        insmod ext3 >> /tmp/usbstorage.log 2>> /tmp/usbstorage.log
                        insmod usb-ohci >> /tmp/usbstorage.log 2>> /tmp/usbstorage.log
                        insmod ehci-hcd >> /tmp/usbstorage.log 2>> /tmp/usbstorage.log
                        insmod scsi_mod >> /tmp/usbstorage.log 2>> /tmp/usbstorage.log
                        insmod sd_mod >> /tmp/usbstorage.log 2>> /tmp/usbstorage.log
                        insmod usb-storage >> /tmp/usbstorage.log 2>> /tmp/usbstorage.log
                        echo "....loaded modules....." >> /tmp/usbstorage.log
                        lsmod >> /tmp/usbstorage.log
                        sleep 2
                        echo "....usb devices...." >> /tmp/usbstorage.log
                        ls -al /dev/scsi/host*/bus*/target*/lun*/* >> /tmp/usbstorage.log
                        echo "....switching  jffs device...." >> /tmp/usbstorage.log
                        mount /dev/scsi/host0/bus0/target0/lun0/part2 /jffs -t ext3 >> /tmp/usbstorage.log 2>> /tmp/usbstorage.log && \
                                fopivot /jffs /rom >> /tmp/usbstorage.log 2>> /tmp/usbstorage.log
                } || {
                        echo "jffs2 not ready yet; using ramdisk"
}}}
=== WhiteRussian 0.9 ===
{{{
                . /bin/firstboot
                is_dirty
                [ $? != 0 ] && {
                        echo "loading USB and EXT2/EXT3 modules"
                        insmod usbcore
                        insmod ext2
                        insmod jbd
                        insmod ext3
                        insmod ohci-hcd
                        insmod uhci-hcd
                        insmod ehci-hcd
                        insmod scsi_mod
                        insmod sd_mod
                        insmod usb-storage
                        sleep 2
                        echo "switching to jffs2"
                        # mount /dev/mtdblock/4 /jffs -t jffs2
                        mount /dev/scsi/host0/bus0/target0/lun0/part1 /jffs -t ext3
                        fopivot /jffs /rom
                } || {
                        echo "jffs2 not ready yet; using ramdisk"
}}}
=== Packages to include with ImageBuilder ===
{{{
e2fsprogs
fdisk
kmod-ext2
kmod-ext3
kmod-usb-core
kmod-usb-ohci
kmod-usb-uhci
kmod-usb2
kmod-usb-storage
Note: Some of these come from the kamikaze backports.
}}}
== SD/MMC ==
SD and MMC users must load the mmc module instead of the usb ones.
The node for MMC devices is /dev/mmc/disk0/part1

Other than these simple changes, using an SD or MMC card with this mod is the same (UNTESTED)
If you do this mod with an MMC or SD card, please update this page with your configuration!
== Notes ==
For now you have to create the device files manually with mknod. Nbd said, this will change in the future.
