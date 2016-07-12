= How do I enable the USB stick on Asus WL-500g / Asus WL500g Deluxe? =

Good idea is to read http://rotz.org/archives/2005/03/wl500g_usb_stic.html

Also, if using a multi-card reader read http://www.cs.sfu.ca/~ggbaker/personal/cf-linux

You can see which packages are available:
{{{
root@OpenWrt:~#ipkg list | grep USB
kmod-usb-core - Kernel Support for USB
kmod-usb-ohci - Kernel driver for OHCI USB controllers
kmod-usb-printer - Kernel modules for USB Printer support
kmod-usb-storage - Kernel modules for USB storage support
kmod-usb-uhci - Kernel driver for UHCI USB controllers
kmod-usb2 - Kernel driver for USB2 controllers
libusb - a Library for accessing Linux USB devices
lsusb - A program to list USB devices
}}}

For Asus WL500g:
Install these packages: 
{{{ipkg install kmod-usb-core kmod-usb-uhci kmod-usb-storage}}}

and add next lines to /etc/modules
{{{
scsi_mod max_scsi_luns=8
sd_mod
sg
usbcore
uhci
usb-ohci
usb-storage
}}}

The ''max_scsi_luns=8'' bit is needed for multi-card readers.

Some models of the Asus WL-500g use an ohci controller - so you need to load the usb-ohci module, not uhci.

NOTE:
The WhiteRussian-RC2 release of OpenWRT loads modules in the /etc/modules.d directory (although the /etc/modules file is still also used)



For Asus WL-500g Deluxe: 

If you plan to use USB 2.0 only devices install these packages: 
{{{ipkg install kmod-usb2 kmod-usb-storage}}} ({{{kmod-usb-core}}} will added as dependency)

and add next lines to /etc/modules
{{{
usbcore
ehci
scsi_mod
sd_mod
sg
usb-storage
}}}

If you want use your old USB 1.1 stick with USB 2.0 you must also install:
{{{ipkg install kmod-usb-uhci}}}

and then and add next line to /etc/modules
{{{
uhci
}}}
then your /etc/modules looks like
{{{
usbcore
ehci
uhci
scsi_mod
sd_mod
sg
usb-storage
}}}

You can use command {{{vi /etc/modules}}} or {{{echo -e "usbcore\nehci\nscsi_mod\nsd_mod\nsg\nusb-storage\n" >> /etc/modules}}} for USB 2.0 and {{{echo -e "usbcore\nehci\nuhci\nscsi_mod\nsd_mod\nsg\nusb-storage\n" >> /etc/modules}}} for USB 1.1. Either reboot or load the modules in this order manually with insmod.

NOTE: ehci is now replaced by ehci-hcd (whiterussian rc2)

Now check if you see your USB stick (of course joining in your ASUS): {{{dmesg}}}

If it correct you see similar as below

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
  Vendor: Apacer    Model: HandyDrive        Rev: 1.05
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

Install a filesystem kernel module:
 * ext2/3: {{{ipkg install kmod-ext2 kmod-ext3}}} and add {{{ext2 jbd ext3}}} to /etc/modules
 * vfat (filesystem generally used in usb sticks and older windows): {{{ipkg install kmod-vfat}}} and add {{{fat vfat}}} to /etc/modules

Next you can mount and use your USB stick (with relevant modul for your file system in memory and created directory for mount): {{{mount /dev/scsi/host0/bus0/target0/lun0/part1 /mnt}}}


= How do I boot from USB stick on ASUS WL-500gx (WL-500g Deluxe, wl500gx) ? =
This guide assumes that you're using a jffs root, with squashfs root some steps might be a little different.

For this to work you need the same kernel modules for USB as described above. You also need the modules for the ext3 filesystem: 
{{{
ipkg install kmod-ext2 kmod-ext3
}}}

The next step is to partition the USB stick and create an ext3fs partition. This requires fdisk. As fdisk isn't included in the default OpenWrt distribution, you'll have to either build it yourself and include fdisk, or use Linux on a desktop computer. (A Linux Live CD works fine). This is the command for doing it from OpenWrt:
{{{
fdisk /dev/scsi/host0/bus0/target0/lun0/disc
}}}

From a desktop Linux distribution, it's more like:
{{{
fdisk /dev/sda
}}}
/!\ ''Make sure you're modifying the right device. If you have any other USB drives, or a SCSI or SATA drive, your USB stick might be at /dev/sdb or /dev/sdb (and so on) instead!''

For more information about using fdisk, see: http://www.tldp.org/HOWTO/Partition/partition-5.html

Next, "format" the newly created partition

OpenWrt:
{{{
mke2fs -j /dev/scsi/host0/bus0/target0/lun0/part1
}}}
Desktop Linux:
{{{
mke2fs -j /dev/sda
}}}
Same warning as above applies here.

Make sure you have /usb and /mnt directories on the jffs partition:
{{{
mkdir /usb /mnt
}}}

Now, we will copy everything from the flash to the USB:
{{{
# load modules
insmod jbd && insmod ext3
# mount it
mount -t ext3 /dev/scsi/host0/bus0/target0/lun0/part1 /mnt
# copy everything
tar cvO -C / bin/ etc/ lib/ sbin/ usr/ www/ var/ | tar x -C /mnt
# create required dirs
mkdir -p /mnt/tmp && mkdir -p /mnt/dev && mkdir -p /mnt/proc && mkdir -p /mnt/jffs
# unmount
umount /mnt
}}}

Next, remove /sbin/init from the jffs partition (this is just a symlink to busybox anyway):
{{{
rm /sbin/init
}}}

And replace it with this script:
{{{
#!/bin/sh
boot_dev="/dev/scsi/host0/bus0/target0/lun0/part1"

# install needed modules for usb and the ext3 filesystem
insmod usbcore
insmod uhci && sleep 2s
insmod scsi_mod && insmod sd_mod && insmod sg && insmod usb-storage
insmod ext2 && insmod jbd && insmod ext3
sleep 2s

# mount the usb stick
mount -t ext3 -o rw "$boot_dev" /usb

# if everything looks ok, do the pivot root
if [ -x /usb/sbin/init ] && [ -d /usb/jffs ]; then
   pivot_root /usb /usb/jffs
   mount none /proc -t proc
   mount none /dev -t devfs
   mount none /tmp -t tmpfs size=50%
   mkdir -p /dev/pts
   mount none /dev/pts -t devpts
   umount /jffs/proc /jffs/dev/pts
   sleep 1s
   umount /jffs/tmp /jffs/dev
fi

# finally, run the real init (from usb hopefully).
exec /bin/busybox init
}}}
/!\ ''If you use USB 2.0 you have to replace the line '''insmod uhci && sleep 2s''' by '''insmod ehci-hcd && sleep 2s'''.''

Make sure your new /sbin/init is executable:
{{{
chmod a+x /sbin/init
}}}

Now just reboot, and it should boot from the USB storage automatically.

= Installing and using ipkgs in mount point other than root with ipkg-link =

Configure ipkg for a non-root destination
{{{
echo dest usb /mnt/usb >> /etc/ipkg.conf
}}}

then install a package to a non-root destination
{{{
ipkg -dest usb install kismet-server
}}}

copy and paste this script into /bin/ipkg-link (or somewhere in your $PATH
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
