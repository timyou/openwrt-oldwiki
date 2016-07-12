First of all, credit for this discovery goes to forum2006. I am reposting his <url>original forum post</url> here to keep it from getting buried.

== 1. Introduction ==
This guide describes how to use your USB stick or your MMC/SD card for storing pakages and files instead of
using the JFFS2 partion on your flash chip. / in this case is the SquashFS partition on the flash chip and the
writable EXT2 partion is on your external media. With little modifications you can use this guide also for MMC/SD
card. Tested with Kamikaze pre1 on a Asus WL-500GD and a 512MB Sundisk Cruzer Mini USB 2.0 stick. With little
modifications it will also work with WhiteRussian 0.9.
With this guide you do not have to mess around with PATH, LD_LIBRARY_PATH or create symlinks anymore.

NOTE: This notes are taken out of my personal notes. They may be incomplete or does not fit your needs.

Makes the following Wiki pages obsolete:
 - PackagesOnExternalMediaHowTo

 - UsbStorageHowto (section 4)


== 2. Requirements ==
 - a router with external storage media like USB stick or MMC/SD card
 - the OpenWrt ImageBuilder

== 3. USB media ==
Use the modified /sbin/mount_root script.
mkdir -p ~/files/sbin/
chmod +x ~/files/sbin/mount_root

Create a new image with the ImageBuilder
make clean image \
    PACKAGES="fdisk e2fsprogs kmod-fs-ext2 kmod-usb-core kmod-usb-ohci kmod-usb-storage kmod-usb-uhci kmod-usb2" \
    FILES="/home/ubuntu/files/"

Reflash your router with the new image.

Next partition and format your USB stick with EXT2 filesystem.

Check if you have /dev/sda1. If it's different change it in ~/files/sbin/mount_root. Rebuild the image and reflash again.

Finally reboot again and check with 'df -h' if /jffs is on your USB stick.

Patch:
{{{
root@OpenWrt:/# df -h
Filesystem                Size      Used Available Use% Mounted on
none                     14.7M     20.0k     14.7M   0% /tmp
tmpfs                   512.0k         0    512.0k   0% /dev
/dev/sda1               480.9M      9.0M    447.4M   2% /jffs <--- this is my USB stick with EXT2 filesystem
/jffs                   960.0k    960.0k         0 100% /
root@OpenWrt:/#
}}}
From now on you can use ipkg the normal way and all packages or modified files will be stored on your USB stick.

modified /sbin/mount_root script:
Code:
{{{
--- mount_root.orig     2007-05-19 23:50:27.000000000 +0200
+++ files/sbin/mount_root       2007-05-20 01:17:55.000000000 +0200
@@ -42,8 +42,25 @@
                . /bin/firstboot
                mtd unlock rootfs_data
                jffs2_ready && {
+                       echo "loading USB and ext2 modules"
+                       insmod usbcore
+                       insmod ext2
+                       insmod ohci-hcd
+                       insmod uhci-hcd
+                       insmod ehci-hcd
+                       insmod scsi_mod
+                       insmod sd_mod
+                       insmod usb-storage
+                       # lsmod > /tmp/x.txt
+                       sleep 2
+                       mknod /dev/sda b 8 0
+                       mknod /dev/sda1 b 8 1
+                       # ls -al /dev/sda* >> /tmp/x.txt
+
                        echo "switching to jffs2"
-                       mount "$(find_mtd_part rootfs_data)" /jffs -t jffs2 && \
+                       # mount "$(find_mtd_part rootfs_data)" /jffs -t jffs2 && \
+
+                       mount /dev/sda1 /jffs -t ext2 && \
                                fopivot /jffs /rom
                } || {
                        echo "jffs2 not ready yet; using ramdisk"
}}}
For now you have to create the device files manually with mknod. Nbd said, this will change in the future.
