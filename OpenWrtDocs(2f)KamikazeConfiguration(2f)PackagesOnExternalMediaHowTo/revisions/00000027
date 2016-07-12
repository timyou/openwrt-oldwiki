#pragma section-numbers off
||<tablebgcolor="#f1f1ed" tablewidth="40%" tablestyle="margin: 0pt 0pt 1em 1em; float: right; font-size: 0.9em;"style="padding: 0.5em;">[[TableOfContents]]||
'''Packages on external media !HowTo'''

= Introduction =
This guide describes how to use your USB pen drive, USB or IDE harddrive or your MMC/SD card for storing packages and files instead of using the JFFS2 partition on your flash chip. / in this case is the SquashFS partition on the flash chip and the writable partition is on your external media. With this guide you do not have to mess around with PATH, LD_LIBRARY_PATH or create symlinks anymore.

This guide is based on http://forum.openwrt.org/viewtopic.php?id=11495.

= Configuration files for the different routers =
Save the configuration file to /etc/config/bootfromexternalmedia.

== For e.g. ASUS WL-500g Premium ==
{{{
config bootfromexternalmedia
        option target   '/mnt'
        option device   '/dev/scsi/host0/bus0/target0/lun0/part1'
        option modules  'usbcore ehci-hcd scsi_mod sd_mod usb-storage jbd ext3'
        option enabled  '1'}}}
== For e.g. ASUS WL-700g Encore ==
{{{
config bootfromexternalmedia
        option target   '/mnt'
        option device   '/dev/ide/host0/bus0/target0/lun0/part1'
        option modules  'ide-core aec62xx ide-detect ide-disk jbd ext3'
        option enabled  '1'}}}
== For e.g. Linksys WRT54GL with SD/MMC card ==
{{{
config bootfromexternalmedia
        option target   '/mnt'
        option device   '/dev/mmc/disc0/part1'
        option gpiomask '0x9c'
        option modules  'mmc jbd ext3'
        option enabled  '1'}}}
The gpiomask option is only required for the MMC/SD card.

= /sbin/init script replacement =
{{{
#!/bin/sh
. /etc/functions.sh
config_load "bootfromexternalmedia"
local section="cfg1"
config_get      "target"   "$section" "target"
config_get      "device"   "$section" "device"
config_get      "gpiomask" "$section" "gpiomask"
config_get      "modules"  "$section" "modules"
config_get_bool "enabled"  "$section" "enabled" '1'
[ "$enabled" -gt 0 ] && {
        [ -n "$gpiomask" ] && {
                echo "$gpiomask" > /proc/diag/gpiomask
        }
        for module in $modules; do {
                insmod $module
        }; done
        sleep 5s
        mount -o rw "$device" $target
        [ -x $target/sbin/init ] && {
                . /bin/firstboot
                pivot $target $target
        }
}
exec /bin/busybox init}}}
Remove the old /sbin/init script, which is just a symbolic link to the Busybox binary.

{{{
rm -f /sbin/init}}}
Save (copy & paste) the new init script above to /sbin/init.

Do not forget to set executable permissions on the script with:

{{{
chmod a+x /sbin/init}}}
= Install required packages =
To prepare your external media you need to install extra packages on the flash chip. E.g. fdisk or cfdisk to partition your external media, e2fsprogs to format and check the filesystem, kmod-fs-ext2 or kmod-fs-ext3 for the filesystem support, the IDE related packages for IDE support, the USB related packages for USB support or copy the mmc.o driver to /lib/modules/2.4.34.

= Copy the flash content to the external media =
Then we create /tmp/root, mount it to /rom and copying the files, sync it and at last unmount it.

{{{
mkdir -p /tmp/root
mount -o bind /rom /tmp/root
cp /tmp/root/* /mnt -a
sync
umount /tmp/root
umount /mnt}}}
Finally reboot or power cycle your router.
