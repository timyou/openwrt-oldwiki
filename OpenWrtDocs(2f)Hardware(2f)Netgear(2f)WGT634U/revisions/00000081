[[TableOfContents]]


= Netgear WGT634U =

The WGT634U is based on the Broadcom 5365P board. It has a 200 MHz CPU, 8 MB flash
and 32 MB RAM. The wireless NIC is an Atheros Mini-PCI capable of 802.11b/g, and it
also has an USB 2.0 controller.


== Status of OpenWrt ==

The kernel boots on the system, we have drivers for the ethernet interface (b44) and
the new switch driver is integrated (robocfg will be obsolete). We have drivers for the
wireless radio (madwifi-ng). The Kernel is 2.6.15.3.

If you want to help with development, attach a serial console and build an image from
Subversion (Kamikaze). Choose "Broadcom BCM47xx/53xx [2.6]" in make menuconfig.

Please always use the newest subversion code. Report any bugs via the
[https://dev.openwrt.org ticket system].


= Installing OpenWrt =

== Using Netgear's web interface ==

If you want to upgrade to !OpenWrt using the web interface, you need to download a special
config file and upload it to your router using the '''Backup Settings''' option.

The file is available here: http://downloads.openwrt.org/utils/wgt634u-upgrade.cfg

After that, clear your browser cache, give the router some time to reboot, and then you should
find a new entry in the menu bar, called '''Upgrade to !OpenWrt'''. Use this function to upload
the !OpenWrt WGT634U image to the router. After a while it should be reachable under the default
IP {{{192.168.1.1}}}


== Using the serial console ==

Images smaller than 4MB can be flashed via TFTP. You need to run a TFTP server on your
local PC.

  * attach a serial console cable to the WGT634U
  * attach ethernet to the WAN port (next to the USB socket)
  * hold down {{{CTRL-C}}} while inserting power to enter CFE
  * configure ethernet from CFE (e.g. with a local DHCP server):

  {{{CFE> ifconfig eth0 -auto
Device eth0:  hwaddr 00-0F-B5-97-1C-3D, ipaddr 192.168.0.200, mask 255.255.255.0
        gateway 192.168.0.1, nameserver 192.168.0.1, domain foo.com
*** command status = 0}}}

  * for manual configuration use something like this:

  {{{
ifconfig eth0 -addr=192.168.1.250 -mask=255.255.255.0
}}}

  * then, flash the new openwrt-wgt634u-2.6-{squashfs,jffs2}.bin image:

  {{{CFE> flash -noheader 192.168.0.3:wgt634u/openwrt-wgt634u-2.6-squashfs.bin flash0.os
Reading 192.168.0.3:wgt634u/openwrt-wgt634u-2.6-squashfs.bin: Done. 1892352 bytes read
Programming...done. 1892352 bytes written
*** command status = 0}}}

  * reboot with

  {{{
CFE> reboot
}}}

Flashing may take over a minute or more. After that you can use {{{reboot}}} to start !OpenWrt.


= Restoring original firmware =

To restore the original firmware a serial console is required. You can use TFTP for the original
images. It seems CFEs TFTP client will only read 4194304 bytes from the TFTP server. To get around
the 4MB limit, we can split larger images into smaller chunks and then use the -offset flag to flash
the parts.

  * boot the router normally and wipe !OpenWrt with
  {{{
mtd -r erase linux
}}}

  * get the original firmware image from Netgear's [http://kbserver.netgear.com/products/WGT634U.asp WGT634U support web site].

  * set the original kernel_args and configure the network interface
  {{{CFE> setenv -p kernel_args "console=ttyS1,115200 root=/dev/ram0 init=linuxrc rw syst_size=8M"
*** command status = 0
CFE> ifconfig eth0 -addr=192.168.1.1 -mask=255.255.255.0;
Device eth0:  hwaddr 00-0F-B5-0E-49-D6, ipaddr 192.168.1.1, mask 255.255.255.0
        gateway not set, nameserver not set
*** command status = 0}}}

  * first you have to flash the full image. Notice, how many bytes it writes to the flash (in this
  example it wrote 3932160 bytes).
  {{{CFE> flash -noheader tftp_host:wgt634u_1_4_1_10.img flash0.os
Reading tftp_host:wgt634u_1_4_1_10.img: Done. 3932160 bytes read
Programming...done. 3932160 bytes written
*** command status = 0}}}

  * split the image, bs=<bytes> are the bytes you should noticed in the previous step.
  {{{
dd if=wgt634u_1_4_1_10.img of=foo.img.1 bs=3932160 skip=1
}}}

  * flash the second part of the image, use the correct offset
  {{{CFE> flash -noheader -offset=3932160 tftp_host:foo.img.1 flash0.os
Reading tftp_host:foo.img.2: Done. 786256 bytes read
Programming...done. 786256 bytes written
*** command status = 0}}}

  * after some minutes it's done. Finally execute
  {{{
CFE> reset
}}}


= Configuration =

The !OpenWrt port for Netgear WGT634U will '''not''' use any NVRAM configuration.
Everything is configured in {{{/etc}}}. For network configuration please modify
{{{/etc/config/network}}}. The NVRAM partition is your old config partition, so please
back it up. You eventually need it to restore your original firmware.

= Using usb drive for Root =

Normally, using the usb drive for root requires making a custom image with a proper
bootline such as:

console=ttyS1,115200 root=/dev/scsi/host0/bus0/target0/lun0/part1 rootdelay=20 rw


However, here is a script for using the usb drive as root without having to recompile using the default 2.6 images provided by flyashi @  http://flyashi.dyndns.org:81/bin

If you want to utilize a swap partition when customizing this script, as I have, remember
that you need the swap-utils package loaded as well.

'''MAKE SURE YOU READ THROUGH THE SCRIPT BEFORE COPYING AND EXECUTING IT BLINDLY!  There
are custom variables at the top that you'll need to make sure complies with the partition table on the usb drive you are using.'''


You should have the minimum of the following modules loaded as well:

 *ehci_hcd 
 *uhci_hcd  
 *usb_storage 
 *sd_mod 
 *scsi_mod 
 *usbcore 
 
First create a /usb directory under the root directory and cut and paste this script i call linuxrc also under the root directory, and remember to customize the
variables according to the partitions on your usb drive.  The current variables assume three partitions on the drive with the second partition being a swap partition.

{{{
#!/bin/sh
#/linuxrc script to mount usb drive as root and pivot current root to /jffs

#it is important that you customize these settings to fit your drive!
boot_dev="/dev/discs/disc0/part1"
swap_dev="/dev/discs/disc0/part2"
usb_dev="/dev/discs/disc0/part3"

# mount the usb stick
mount -t ext3 -o rw "$boot_dev" /usb

# if everything looks ok, do the pivot root
if [ -x /usb/sbin/init ] && [ -d /usb/jffs ]; then
        pivot_root /usb /usb/jffs

        umount /jffs/proc/bus/usb
        umount /jffs/proc
        umount /jffs/dev/pts
        sleep 1s
        mv /jffs/tmp/* /tmp
        umount /jffs/tmp
        umount /jffs/dev
        umount /jffs/sys

        mount none /proc -t proc
        mount none /dev -t devfs
        mount none /tmp -t tmpfs size=50%
        mkdir -p /dev/pts
        mount none /dev/pts -t devpts

   swapon "$swap_dev"
   mount -t sysfs sys /sys
   mount -t ext3 -o rw "$usb_dev" /mnt/usb
   mount -o bind,ro /mnt/usb/snapshot /snapshot

fi

exec /bin/busybox init


We're not done yet, it's also imperative that you add a line into your init scripts to execute
this script, so add the following line to the end of the /etc/init.d/S99done file:

[ -f /linuxrc ] && . /linuxrc
}}}

There!  Now when you go to reboot, your usb drive will be mounted as root as according to the linuxrc script.




= Serial console =

Default parameters for the serial console on J7 are 115200 N81. You can build a suitable serial console using a [http://www.maxim-ic.com/quick_view2.cfm/qv_pk/1068 MAX3232] chip.  You can also build a serial console cable using a cell phone data cable.  For example, the [http://www.radioshack.com/product/index.jsp?productId=2103605 Radio Shack "Mobile Phone Data Cable, Cable 22"] (part number 170-0762) works, clipping off the cell phone end and attaching the exposed wires as follows: green wire to GND; orange wire to RX; and white wire to TX; leaving VCC unconnected.  Plug into your linux box's USB port and connect minicom to /dev/ttyUSBn.

J6 (left from J7) is a second serial port, but has no header on it. It has the same pinout as J7.

{{{
------------------------------------------
| |     |    LAN-Ports   |          |    |
|       ------------------               |
|                                        |
|        USB                             |
|                         VCC .  VCC .   |
|  WiFi                    TX .  TX  .   |
|                 CPU      RX .  RX  .   |
|         RAM             GND .  GND .   |
|                             J6     J7  |
|                           FLASH        |
|                                        |
------------------------------------------
   |    |     |     |     |     |     |
}}}


= Other projects and information =

 * More info in the forum:
 [[BR]]- [http://openwrt.org/forum/viewtopic.php?id=33]

 * External developer's Wiki
 [[BR]]- [http://wgt634u.nomis52.net/]

 * OpenWGT project (this project is not currently under active development)
 [[BR]]- [http://openwgt.informatik.hu-berlin.de/]

 * Another firmware project
 [[BR]]- [http://router.4th.be/]


= End Of Life =

I got confirmation from Janine Bodwin of NetGear that the WGT634U was EOL'ed on 01-Oct-2005


----
CategoryModel
