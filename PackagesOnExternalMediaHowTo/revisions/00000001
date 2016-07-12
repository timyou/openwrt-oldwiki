[[TableOfContents]]


= Introduction =
== What is this Howto? ==
This howto describes the process of installing and using packages on external 
media.  I used this information to install packages on my SD card.

== What External Media Can I Use? ==
I used this technique for my SD card mod.  I assume that the same (or similar) 
can be used for just about any external media but I have not tried.

= Formatting the Media =
While this step may not be needed, I preferred to have an ext2 file system to 
better support various links and other *nix specific features. 

To format the media I installed the e2fsprogs package with the following 
command
{{{
ipkg install http://openwrt.org/downloads/people/nico/\
testing/mipsel/packages/e2fsprogs_1.38-1_mipsel.ipk
}}}

Once installed you can format the target partition like this
{{{
mkfs.ext2 /dev/mmc/disc0/part1
}}}
Replace '/dev/mmc/disc0/part1' with the device that you want to format.

= Mount the Drive =
== Loading the Ext2 Kernel Module ==
Once the drive is formatted the kernel module needs to be installed and loaded 
for the partition to be used.  Install and load the kmod-ext2 package with the 
following commands
{{{
ipkg install kmod-ext2
insmod ext2
}}}

To load the Ext2 module automatically on every boot
{{{
echo 'ext2' > /etc/modules.d/30-ext2
}}}

== Mounting ==
When mounting a mount-point is needed.  A mount-point is the folder where the 
device will be attached.  Once mounted the device will appear to e inside this 
folder.  A typical place to put these points is in the /mnt folder.  Since I am 
using this for my SD card my mount point is /mnt/sd.  Create the mount point 
for your installation like this:
{{{
mkdir -p /mnt/sd
}}}

To make mounting in the future easier it is best to create an entry in the 
/etc/fstab file.  Since the file is not in the default install of OpenWrt you 
will probably have to create it.  Add the following line to /etc/fstab.
{{{
/dev/mmc/disc0/part1 /mnt/sd ext2 defaults 0 0
}}}
Replace '/dev/mmc/disc0/part1' with the device that you want to mount and 
'/mnt/sd' with the mount-point you made above.

Mount the drive using the following command:
{{{
mount /dev/mmc/disc0/part1 /mnt/sd
}}}

To mount the drive automatically on boot, use the following command:
{{{
echo 'mount /dev/mmc/disc0/part1 /mnt/sd' > /etc/init.d/S20externalmount
}}}

== Configuring ipkg ==
To install packages to the external drive, add the following line in 
/etc/ipkg.conf
{{{
dest sd /mnt/sd
}}}
Where the syntax of the above line is "dest [name of destination] 
[destination]".
The "name of destination" can be anything you want, I chose "sd" as 
I am using the SD card.

== Modifying Your Environment ==
In the file /etc/profile, modify the line that reads
{{{
export PATH=/bin:/sbin:/usr/bin:/usr/sbin
}}}
to read
{{{
export PATH=/bin:/sbin:/usr/bin:/usr/sbin:/mnt/sd/bin:/mnt/sd/sbin:/mnt/sd/usr/bin:/mnt/sd/usr/sbin
}}}
Note: as with everything else in this howto you must replace /mnt/sd with 
YOUR mount-point.

Also in /etc/profile, add the following line:
{{{
export LD_LIBRARY_PATH=/lib:/usr/lib:/mnt/sd/lib:/mnt/sd/usr/lib
}}}

= Installing Packages =
To install packages to the external drive use the -d option and specify the 
destination name that you created earlier.  An example of the command for my 
setup is
{{{
ipkg -d sd install tcpdump
}}}

= Using the Packages =
To use the packages just execute them as if they were installed on the local 
drive.  In the "Modifying Your Environment" section of this guide you set the 
needed variables to allow the system to recognize programs installed on the 
external drive.
