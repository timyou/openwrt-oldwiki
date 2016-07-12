#PRAGMA section-numbers off

= Boot from external media HowTo =

This is about how to swap in external media, such as MMC/SD cards or USB drives, as the root filesystem using the existing init.d/rc.d and uci/config infrastructure. In contrast to OpenWrtDocs/KamikazeConfiguration/PackagesOnExternalMediaHowTo, this is done without replacing files and will keep the original /etc tree in place in order to ensure consistency of your configuration.

At the moment it is designed for Kamikaze 8.09 with kernel 2.4. I haven't tried it with other releases. Also I haven't tried it with the kernel 2.6 flavour, but I suspect the necessary adjustments to be minimal - if they are required at all.


== Motivation ==

While OpenWrtDocs/KamikazeConfiguration/PackagesOnExternalMediaHowTo also describes a way to use your mass storage devices on your router for package installation etc., I felt I wanted to use a more robust way to achieve that and also wanted to have consistent configuration, no matter if my SD card was mounted as / or not.

So my first idea was to stack another mini_fo filesystem on top of the existing one (which overlays /jffs over /rom), which would enable me to keep both the files from the read only squashfs partition plus the changes I made on the jffs2 partition while writing subsequent changes to my SD card. Unfortunately, this turned out to crash my system and I suspect mini_fo being unable to provide 2 instances at the same time (at least on top of each other).

Well, the alternative that remains is that you first have to duplicate most of the original filesystem tree to the mass storage device, so that you don't shoot yourself in the foot when pivoting to the new root.

Unfortunately, duplicating all of it would mean you would have two separate configurations under /etc, one when the original filesystem is in place and the other when the mass storage devices takes over. This is not a good idea not only since it would be headache to keep in sync, but also because the new root is not swapped in at the very beginning - at the time our script gets executed we're already in the middle of the /etc/rc.d/* process and /etc/init.d/rcS has already determined the scripts to execute and would thus be umimpressed by changes under rc.d due to a pivoted root, meaning it would not notice scripts that have newly appeared (due, for instance, to a service which you installed on your mass storage device) and would try to execute scripts that have vanished. Also, the scripts executed before this bootext script may have referred to configuration on the original tree while scripts executed thereafter will refer to configuration on the mass storage device.

This is calling for trouble, so our solution is to bind mount the original /etc tree to the same place on the new root. This works quite well (also for squashfs+jffs2-images with mini_fo overlay) and means you only have to deal with a single config at all times, mass storage swapped in or not.


== Preparing your router and mass storage device ==

/!\ The command line examples provided here are for the MMC/SD card modification of broadcom chipsets and an ext3 filesystem, but would easily be adapted to other combinations.

=== Collecting important information ===

Find out everything necessary to have OpenWRT access your mass storage device, like:
 * required kernel modules for the block device itself
 * required kernel modules for the intended filesystem
 * name of the block device under /dev/
 * correct gpiomask in case of MMC/SD
 * delay between inserting the kernel modules and the node appearing under /dev/ for USB

=== Install kernel module packages for the block device ===

For MMC/SD on broadcom:
{{{
opkg install kmod-broadcom-mmc
insmod mmc
ls /dev/mmc/*/*
}}}

If that fails, you may have to get a [:OpenWrtDocs/Customizing/Hardware/MMC:different MMC driver].

=== Install kernel module packages for the filesystem ===

For ext3:
{{{
opkg install kmod-fs-ext3
insmod ext3
grep ext3 /proc/filesystems
}}}

=== Install utilities to set up your mass storage device ===

For ext3 and cfdisk:
{{{
opkg install cfdisk e2fsprogs 
}}}

Of course, you can also use fdisk instead of cfdisk if you are more comfortable with that.

=== Set up at least one partition ===

/!\ You can skip that step if your mass storage device is already partitioned.

For MMC/SD on broadcom:
{{{
cfdisk /dev/mmc/disc0/disc
dmesg | tail
cat /proc/partitions
}}}

If the new partition didn't turn up, try removing and inserting the kernel module for the block device. You could also try rebooting.

=== Create a filesystem on the partition ===

/!\ You can skip that step if you already have the correct filesystem in place.

For ext3 on MMC/SD on broadcom:
{{{
mkfs.ext3 /dev/mmc/disc0/part1
}}}

=== Create a mountpoint and mount the filesystem there ===

For ext3 on MMC/SD on broadcom:
{{{
[ -d /mnt ] || mkdir /mnt
mount -t ext3 -o noatime /dev/mmc/disc0/part1 /mnt
grep /mnt /proc/mounts
}}}

=== Duplicate the existing tree on the mass storage device ===

{{{
mkdir /tmp/orig
mount -o bind / /tmp/orig   # this is necessary to prevent duplicating /proc /dev and so forth
tar -c -C /tmp/orig -f - . | tar -xv -C /mnt -f -
umount /tmp/orig
rmdir /tmp/orig
rm -r /mnt/etc/*   # we don't need a duplicate /etc tree
umount /mnt
}}}


== Preparing the script ==

=== Putting up the script ===

Put the following script at '''/etc/init.d/bootext''' by copy&pasting it into vi, transfering it via scp or any other method you prefer:
## [[Include(/EtcConfigBootExt,,editlink)]]

Don't forget to make the script executable:
{{{
chmod a+x /etc/init.d/bootext
}}}

=== Configuring the script ===

Configure the script either by using '''uci''' or by editing the file '''/etc/config/bootfromexternalmedia''' to look similar to this:
{{{
config bootfromexternalmedia
	option enabled	'1'
	option device	'/dev/mmc/disc0/part1'
	option name	'mmc'
	option target	'/mnt'
	option putold	'/mnt'
	option modules	'mmc jbd ext3'
	option gpiomask	'0x9c'
	option waitdev	'0'
	option filesys	'ext3'
	option mountopt	'noatime'
}}}

==== option enabled ====

Set to 1 to enable or to 0 to disable switching to your mass storage device, respectively. Default is enabled.

==== option device ====

This option is required. It determines the block special device node under /dev your mass storage device uses.

==== option name ====

Name of your mass storage device for error message display purposes only. If not specified, defaults to the device name.

==== option target ====

Path of the mountpoint where to mount your mass storage device under the original root. Defaults to the filesystem name if specified, otherwise to '''/new'''.

==== option putold ====

Path of the mountpoint where to move the original root to under the new root filesystem. Defaults to the same as the target mountpoint if specified, otherwise to '''/old'''.

==== option modules ====

Explicitly specify all modules required to access your block device as well as mount your filesystem here. Don't rely on any other script having loaded these modules.

==== option gpiomask ====

When using the MMC/SD card mod, set up the correct gpiomask before inserting the kernel module (which must also be in the list of modules for this to work automatically). Find the correct value at OpenWrtDocs/Customizing/Hardware/MMC.

==== option waitdev ====

For USB devices, it usually takes a couple of seconds after inserting the kernel module for the device node to appear. Specify here the maximum delay it will take in seconds. To be on the safe side, add a couple of seconds. The script won't wait this fixed amount, but will rather check for the device in one second intervals up to the maximum of the waitdev value.

==== option filesys ====

Specify the filesystem you are using. If omitted, it will try all known and inserted filesystems in turn.

==== option mountopt ====

If you need to hand any options to mount, you can give them here.


== Testing the script with your setup ==

/!\ I strongly recommend you don't enable the script for startup at boot time unless you have verified that it works without problems.

First, make sure you don't have your device mounted anymore or alternatively, that it is mounted at the same path as your configured target mountpoint.

Then check if the script is working as it should:
{{{
/etc/init.d/bootext stop    # should report that device is not on /
/etc/init.d/bootext start   # should perform the switch without producing any output
grep '^[^ ]* / '            # verify that the device is now on /
grep '^[^ ]* /etc '         # verify that there is now a mounted /etc
/etc/init.d/bootext start   # should report that device is already on /
/etc/init.d/bootext stop    # should switch back without producing any output
grep '^[^ ]* / '            # verify that the original tree is back on /
grep '^[^ ]* /etc '         # verify that there is no /etc mounted anymore
/etc/init.d/bootext stop    # should report that device is not on /
}}}

== Enabling the script for automatic start at boot time ==

/!\ Be sure you have followed the above procedures and checked that everything works before enabling start at boot time, since otherwise there is a chance that you lock yourself out of your router if something goes wrong. To prepare yourself for this event, no matter how unlikely, find out in advance how to gain failsafe access to your router in such a case.

Then simply execute this and reboot afterwards:
{{{
/etc/init.d/bootext enable
}}}
