OpenWrtDocs/KamikazeConfiguration/PackagesOnExternalMediaHowTo under construction ...

This guide is based on http://forum.openwrt.org/viewtopic.php?id=11495.

= TODO =
 * Rewrite the init scripts to use UCI
= /sbin/init for e.g. ASUS WL-500g Premium =
{{{
#!/bin/sh
boot_dev="/dev/scsi/host0/bus0/target0/lun0/part1"
for module in usbcore ehci-hcd scsi_mod sd_mod usb-storage jbd ext3; do {
        insmod $module
}; done
sleep 2s
mount -o rw "$boot_dev" /mnt
[ -x /mnt/sbin/init ] && {
        . /bin/firstboot
        pivot /mnt /mnt
}
exec /bin/busybox init}}}
= /sbin/init script for e.g. ASUS WL-700g Encore =
{{{
#!/bin/sh
boot_dev="/dev/ide/host0/bus0/target0/lun0/part1"
for module in ide-core aec62xx ide-detect ide-disk jbd ext3; do {
        insmod $module
}; done
sleep 5s
mount -o rw "$boot_dev" /opt
[ -x /opt/sbin/init ] && {
        . /bin/firstboot
        pivot /opt /opt
}
exec /bin/busybox init}}}
= /sbin/init for e.g. Linksys WRT54GL with SD/MMC mod =
{{{
#!/bin/sh
. /etc/functions.sh
config_load "mmcmod"
local section="cfg1"
config_get      "target"   "$section" "target"
config_get      "device"   "$section" "device"
config_get      "gpiomask" "$section" "gpiomask"
config_get      "modules"  "$section" "modules"
config_get_bool "enabled"  "$section" "enabled" '1'
[ "$enabled" -gt 0 ] && {
        echo "$gpiomask" > /proc/diag/gpiomask
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
= /etc/config/bootfromexternalmedia =
{{{
config mmcmod
        option target   '/mnt'
        option device   '/dev/mmc/disc0/part1'
        option gpiomask '0x9c'
        option modules  'mmc jbd ext3'
        option enabled  '0'}}}
the gpiomask option is only required for the MMC/SD card mod.
= Copy the flash content to the external media =
Then we make a /tmp/root mount it to /rom and copiing the files (and at last unmount it and the stick)

{{{
mkdir /tmp/root
mount -o bind /rom /tmp/root
cp /tmp/root/* /mnt -a
umount /tmp/root
umount /mnt}}}
