'''USB storage howto'''

[[TableOfContents]]
= Intro =
It's useful to extend the storage capacity of your USB enabled Wrt router f. e. making a central file server. This can easily be done with connecting USB storage devices (like a USB stick or a external USB harddisc) to the USB port on your router.

= Requirements =
 * Supported router by OpenWrt with USB (f. e. the Asus [:OpenWrtDocs/Hardware/Asus/WL500G:WL-500G] or the Asus [:OpenWrtDocs/Hardware/Asus/WL500GD:WL-500G deluxe])
 * a recent !OpenWrt version installed (at least White Russian RC3)
 * some kind of a USB storage device (a USB stick or a external USB harddisc) supported by Linux
 * a USB hub (optional) to add more USB ports (it's probably a good idea to use an active USB hub with it's own PSU)

'''NOTE: '''[:WithUSBv2:Devices supporting USB v2.0]

= Installation =
'''TIP:''' Some routers are USB 1.1 and 2.0 compatible. To use both devices with both versions install the modules for USB 1.1 and 2.0.

== Modules for USB 1.1 ==
For USB 1.1 you need to install

{{{
ipkg install kmod-usb-uhci
}}}

'''TIP:''' Most USB chips have UHCI controllers. If that is not working for you install the {{{kmod-usb-ohci}}} package instead of the {{{kmod-usb-uhci}}} one. The BCM4710 and BCM4712 will need {{{kmod-usb-ohci}}}!  

== Modules for USB 2.0 ==
This package includes the modules for USB 2.0.

'''NOTE:''' USB 2.0 support in White Russian is broken. There are some threads in the forum and some tickets as well if you like to read about what happens.

{{{
ipkg install kmod-usb2
}}}

== Modules for storage ==
To add storage support finally install

{{{
ipkg install kmod-usb-storage
}}}

== Clean up ==
'''TIP:''' The {{{max_scsi_luns=8}}} bit is needed for multi-card readers and should be added to the end of the {{{scsi_mod}}} line in the {{{/etc/modules.d/60-usb-storage}}} file.

!OpenWrt uses {{{/etc/modules.d}}} directory to load the modules automatically on the next reboot. So reboot the router with

{{{
reboot
}}}

Now check if !OpenWrt sees your USB device (of course inserting it into your Wrt router). If it's correct you should see similar messages as on the {{{dmesg}}} dump below.

{{{
dmesg
}}}

{{{
usb.c: registered new driver usbdevfs
usb.c: registered new driver hub
uhci.c: USB Universal Host Controller Interface driver v1.1
PCI: Enabling device 01:02.0 (0000 -> 0001)
uhci.c: USB UHCI at I/O 0x100, IRQ 2
usb.c: new USB bus registered, assigned bus number 1
hub.c: USB hub found
hub.c: 2 ports detected
PCI: Enabling device 01:02.1 (0000 -> 0001)
uhci.c: USB UHCI at I/O 0x120, IRQ 2
usb.c: new USB bus registered, assigned bus number 2
hub.c: USB hub found
hub.c: 2 ports detected
hub.c: new USB device 01:02.0-2, assigned address 2
usb.c: USB device 2 (vend/prod 0xd7d/0x100) is not claimed by any active driver.
Initializing USB Mass Storage driver...
usb.c: registered new driver usb-storage
scsi0 : SCSI emulation for USB Mass Storage devices
  Vendor: Apacer    Model: Drive             Rev: 1.05
  Type:   Direct-Access                      ANSI SCSI revision: 02
Attached scsi removable disk sda at scsi0, channel 0, id 0, lun 0
SCSI device sda: 256000 512-byte hdwr sectors (131 MB)
sda: Write Protect is off
Partition check:
 /dev/scsi/host0/bus0/target0/lun0: p1
WARNING: USB Mass Storage data integrity not assured
USB Mass Storage device found at 2
USB Mass Storage support registered.
}}}

= Configuration =
== Usage as a storage device to extend storage ==
First install the kernel file system modules, for example:

{{{
ipkg install kmod-vfat
reboot
}}}

'''TIP:''' The modules can also be loaded using {{{insmod}}} to avoid rebooting.

'''TIP:''' You can install support for more file systems by installing the appropriate packages.

||'''File system''' ||'''Package name''' ||'''Comment''' ||
||VFAT/MSDOS ||kmod-vfat ||File system generally used in USB devices and older Windows ||
||EXT2 ||kmod-ext2 || ||
||EXT3 ||kmod-ext3 || ||


Now install the {{{fdisk}}} package from the White Russian's backports repository. How to use the backports repository see ["OpenWrtDocs/Packages"].

{{{
ipkg install fdisk
}}}

Create the {{{/mnt}}} directory for the mount point on the flash

{{{
mkdir -p /mnt
}}}

Check what partition you like to mount from your USB device

{{{
fdisk -l
}}}

Finally you can mount and use your USB device (with relevant modules for your file system in memory and created directory for mount):

{{{
mount /dev/scsi/host0/bus0/target0/lun0/part1 /mnt
}}}

Be happy and use your USB device like on every other GNU/Linux system or create a file server using Samba.

== How do I boot from the USB device ==
For this to work you need the same kernel modules for USB as described above. You also need the modules for the EXT3 file system:

{{{
ipkg install kmod-ext2 kmod-ext3
}}}

After installing the modules, you should either reboot the device or load the installed modules manually:

{{{
insmod ext2
insmod jbd
insmod ext3
}}}

The next step is to partition the USB device and create an EXT3 FS partition. This requires {{{fdisk}}} (install it as described above). You can do the partioning in !OpenWrt it self or on a normal PC.

'''In !OpenWrt do'''

{{{
fdisk /dev/scsi/host0/bus0/target0/lun0/disc
}}}

'''On a GNU/Linux desktop PC do'''

{{{
fdisk /dev/sda
}}}

/!\ '''IMPORTANT:''' Make sure you are modifying the right device. If you have any other USB drives, or a SCSI or SATA drive, your USB device might be at {{{/dev/sdb}}} or {{{/dev/sdc}}} (and so on) instead!

For more information about using {{{fdisk}}}, see http://www.tldp.org/HOWTO/Partition/partition-5.html.

Next, "format" the newly created partition.

'''In !OpenWrt do'''

For doing this in !OpenWrt you first have to install the {{{e2fsprogs}}} package from the White Russian's backports repository. How to use the backports repository see ["OpenWrtDocs/Packages"].

{{{
ipkg install e2fsprogs
}}}

Then "format" your partition with

{{{
mke2fs -j /dev/scsi/host0/bus0/target0/lun0/part1
}}}

If you keep getting errors like:

{{{
Creating journal (4096 blocks): mke2fs: No such file or directory
        while trying to create journal
}}}

then run the following command:

{{{
ln -s /proc/mounts /etc/mtab
}}}

Now, we will copy everything from the flash to the USB device (make sure the EXT3 modules are loaded):

{{{
# mount it
mount -t ext3 /dev/scsi/host0/bus0/target0/lun0/part1 /mnt

# now, we need to mount the root contents somewhere so we can copy
# them without copying /mnt and /proc to the new usb device

mkdir /tmp/root

# if you're using squashfs, you want to copy the squashfs contents,
# not the jffs2 symlinks, so use the command:
mount -o bind /rom /tmp/root

# if you're using jffs2 then use the command /
mount -o bind / /tmp/root

# now /tmp/root contains the root filesystem with no extra directories mounted
# so we just copy this to the usb device

cp /tmp/root/* /mnt -a

# and now we unmount both the usb and our /tmp/root
umount /tmp/root
umount /mnt
}}}

/!\ Problems with booting from USB storage were reported with WhiteRussian RC4 or later, which is the version that introduced USB hotplug support. If you encounter problems as well, try disabling USB hotplug. (more info on this?)

As earlier stated on this page (to remove {{{/etc/hotplug.d/usb/01-mount}}}) is NOT a good idea, as this is where usbfs is mounted, so usb-storage might work fine but lsusb wohn't list your devices, and most software using USB won't be able to find devices since /proc/bus/usb will remain empty?

So either remove the file and mount usbfs somewhere else, or everything inside except the line which goes: [ -f /proc/bus/usb/devices ] || mount -t usbfs none /proc/bus/usb

Next, remove {{{/sbin/init}}} from the JFFS2 partition (this is just a symlink to !BusyBox anyway):

{{{
rm /sbin/init
}}}

And replace it with this script:

{{{
#!/bin/sh

# change this to your boot partition
boot_dev="/dev/scsi/host0/bus0/target0/lun0/part1"

# install needed modules for usb and the ext3 filesystem
# **NOTE** for usb2.0 replace "uhci" with "ehci-hcd"
# **NOTE** for ohci chipsets replace "uhci" with "usb-ohci"

for module in usbcore uhci scsi_mod sd_mod usb-storage jbd ext3; do {
        insmod $module
}; done

# this may need to be higher if your disk is slow to initialize
sleep 4s

# mount the usb stick
mount "$boot_dev" /mnt

# if everything looks ok, do the pivot root
[ -x /mnt/sbin/init ] && {
        mount -o move /proc /mnt/proc && \
        pivot_root /mnt /mnt/mnt && {
                mount -o move /mnt/dev /dev
                mount -o move /mnt/tmp /tmp
                mount -o move /mnt/jffs2 /jffs2 2>&-
                mount -o move /mnt/sys /sys 2>&-
        }
}

# finally, run the real init (from USB hopefully).
exec /bin/busybox init
}}}

Make sure your new {{{/sbin/init}}} is executable:

{{{
chmod a+x /sbin/init
}}}

Now just reboot, and if you did everything right it should boot from the USB device automatically.

If it could not boot from the USB device it will boot normally from the file system found on the flash as fallback.

== Installing and using IPKG packages in mount point other than root ==
/!\ '''NOTE:''' This is not tested. Please report if it's working for you.

-Works for me (MikkoKorkalo)

/!\ '''NOTE:''' PackagesOnExternalMediaHowTo contains additional important infos.

/!\ '''NOTE:''' Destination needs not to have trailing slash in order to make following script work (Nijel).

Configure {{{ipkg}}} for a non-root destination

{{{
echo dest usb /mnt/usb >> /etc/ipkg.conf
}}}

then install a package to a non-root destination

{{{
ipkg -dest usb install kismet-server
}}}

Copy & paste this script into {{{/bin/ipkg-link}}} (or somewhere in your {{{$PATH}}}).

{{{
COMMAND=$1
PACKAGE=$2

setdest () {
        for i in `grep dest /etc/ipkg.conf | cut -d ' ' -f 3`; do
                if [ -f $i/usr/lib/ipkg/info/$PACKAGE.list ]; then
                        DEST=$i
                fi
        done

        if [ "x$DEST" = "x" ]; then
                echo "Can not locate $PACKAGE."
                echo "Check /etc/ipkg.conf for correct dest listings";
                echo "Check name of requested package: $PACKAGE"
                exit 1
        fi

}

addlinks () {
        setdest;

        cat $DEST/usr/lib/ipkg/info/$PACKAGE.list | while read LINE; do
                SRC=$LINE
                DST=`echo $SRC | sed "s|$DEST||"`
                DSTNAME=`basename $DST`
                DSTDIR=`echo $DST | sed "s|$DSTNAME\$||"`
                test -f "$SRC"
                if [ $? = 0 ]; then
                        test -e "$DST"
                        if [ $? = 1 ]; then
                                mkdir -p $DSTDIR
                                ln -sf $SRC $DST
                        else
                                echo "Not linking $SRC to $DST"
                                echo "$DST Already exists"
                        fi
                else
                        test -d "$SRC"
                        if [ $? = 0 ]; then
                                test -e $DST
                                if [ $? = 1 ]; then
                                        mkdir -p $DST
                                else
                                        echo "directory already exists"
                                fi
                        else
                                echo "Source directory $SRC does not exist"
                        fi
                fi
        done

}

removelinks () {
        setdest;

        cat $DEST/usr/lib/ipkg/info/$PACKAGE.list | while read LINE; do
                SRC=$LINE
                DST=`echo $LINE | sed "s|$DEST||"`
                DSTNAME=`basename $DST`
                DSTDIR=`echo $DST | sed "s|$DSTNAME\$||"`
                test -f $DST
                if [ $? = 0 ]; then
                        rm -f $DST
                        test -d $DSTDIR && rmdir $DSTDIR 2>/dev/null
                else
                        test -d $DST
                        if [ $? = 0 ]; then
                                rmdir $DST
                        else
                                echo "$DST does not exist"
                        fi
                fi
        done

}

mountdest () {
        test -d $PACKAGE
        if [ $? = 1 ]; then
                echo "Mount point does not exist"
                exit 1
        fi

        for i in $PACKAGE/usr/lib/ipkg/info/*.list; do
                $0 add `basename $i .list`
        done
}

umountdest () {
        test -d $PACKAGE
        if [ $? = 1 ]; then
                echo "Mount point does not exist"
                exit 1
        fi

        for i in $PACKAGE/usr/lib/ipkg/info/*.list; do
                $0 remove `basename $i .list`
        done
}

case "$COMMAND" in
  add)
        addlinks
  ;;

  remove)
        removelinks
  ;;

  mount)
        mountdest
  ;;

  umount)
        umountdest
  ;;

  *)
        echo "Usage: $0 <cmd> <target>"
        echo "       Commands: add, remove, mount, umount"
        echo "       Targets: <package>, <mount point>"
        echo "Example:  $0 add kismet-server"
        echo "Example:  $0 remove kismet-server"
        echo "Example:  $0 mount /mnt/usb"
        echo "Example:  $0 umount /mnt/usb"
        exit 1
        ;;

esac

exit 0
}}}

Send questions/bugs on this script to mbarclay@openfbo.com (Matt Barclay).

Make sure the {{{/bin/ipkg-link}}} script is executable:

{{{
chmod a+x /bin/ipkg-link
}}}

Examples howto use the script:

Link a single package to root:

{{{
ipkg-link add kismet-server
}}}

Link all packages on a mount point to root:

{{{
ipkg-link mount /mnt/usb
}}}

Remove symlinks:

{{{
ipkg-link remove kismet-server
}}}

Remove all symlinks for all packages:

{{{
ipkg-link umount /mnt/usb
}}}

= Links =
 * Linux USB [[BR]]- http://www.linux-usb.org/

 * Linux USB device support [[BR]]- http://www.linux-usb.org/devices.html

----
 . CategoryHowTo 
