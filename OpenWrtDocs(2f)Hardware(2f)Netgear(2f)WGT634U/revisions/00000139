[[TableOfContents]]

= Netgear WGT634U =
attachment:wgt634u.jpg

The WGT634U is based on the Broadcom 5365P board that features a 200 MHz MIPS CPU along with a built-in IPSEC co-processor [http://wiki.openwrt.org/HardwareAcceleratedCrypto details], allowing encrypted VPNs (up to AES256) a bonus of a performance boost up to 75Mbps (quoted) IPSec throughput - far more than the MIPS32 CPU alone can produce. It also comes standard with 8 MB flash and 32 MB RAM.

The wireless NIC is an Atheros Mini-PCI capable of 802.11b/g, and has a [http://www.hirose.co.uk/productreleases/ms156.htm MS-156] test point and a soldered antenna.  The WGT634U also has a USB 2.0 controller.

== Status of OpenWrt ==
The kernel boots on the system, we have drivers for the ethernet interface (b44) and the new switch driver is integrated (robocfg will be obsolete). We have drivers for the wireless radio (madwifi-ng). Everything is working now (except failsafe).

If you want to help with development, attach a serial console and build an image from Subversion (Kamikaze). Choose "Broadcom BCM947xx/953xx [2.6]" in make menuconfig, and join the discussions in the forum at http://forum.openwrt.org/viewforum.php?id=3 regarding the WGT634U.

Please always use the newest Subversion code. Report any bugs via the [https://dev.openwrt.org ticket system].

Note that the failsafe mode doesn't work yet, so the system cannot be recovered (except by serial cable) when something goes wrong.

= Installing OpenWrt =
== Using Netgear's web interface ==
If you want to upgrade to !OpenWrt using the web interface, you need to download a special config file and upload it to your router using the '''Backup Settings''' option. The supplied config file is for version 1.4.1.10 of the Netgear supplied firmware. If the version number doesn't match the version number of the config file it will just not 'take'

The file is available here: http://downloads.openwrt.org/utils/wgt634u-upgrade.cfg

After that, ''clear your browser cache'', give the router some time to reboot, and then you should find a new entry in the menu bar, called '''Upgrade to !OpenWrt'''.  Use this function to upload the !OpenWrt WGT634U image to the router.  Note:  After that custom configuration file is uploaded and the router reboots, you will be unable to obtain a DHCP address from the machine.  Set a static IP for the network interface you have connected to the router.

After a while (and we mean ''a while'') it should be reachable under the default IP {{{192.168.1.1}}}.  Do '''not''' classify the router as dead until you have given it 10 minutes, rebooted it, and given it 10 more.

== Using Serial Console ==
Images smaller than 4MB can be flashed via TFTP. You need to run a TFTP server on your local PC.

 * attach a serial console cable to the WGT634U
 * attach ethernet to the WAN port (next to the USB socket)
 * hold down {{{CTRL-C}}} while inserting power to enter CFE
 * configure ethernet from CFE (e.g. with a local DHCP server):
 {{{
CFE> ifconfig eth0 -auto
Device eth0:  hwaddr 00-0F-B5-97-1C-3D, ipaddr 192.168.1.250, mask 255.255.255.0
        gateway 192.168.1.1, nameserver 192.168.1.1, domain foo.com
*** command status = 0}}}
 * for manual configuration use something like this:
 {{{
ifconfig eth0 -addr=192.168.1.250 -mask=255.255.255.0
}}}
 * then, flash the new openwrt-wgt634u-2.6-{squashfs,jffs2}.bin image:
 {{{
CFE> flash -noheader 192.168.1.3:wgt634u/openwrt-wgt634u-2.6-squashfs.bin flash0.os
Reading 192.168.1.3:wgt634u/openwrt-wgt634u-2.6-squashfs.bin: Done. 1892352 bytes read
Programming...done. 1892352 bytes written
*** command status = 0}}}
 * reboot with
 {{{
CFE> reboot
}}}
Flashing may take over a minute or more. After that you can use {{{reboot}}} to start !OpenWrt.

= Restoring lost nvram settings =
The default settings are:
{{{
CFE_VERSION          1.0.34
CFE_BOARDNAME        BCM95365R
CFE_MEMORYSIZE       32
BOOT_CONSOLE         uart1
et0mdcport           0
et0phyaddr           254
configvlan           0x1
et0macaddr           00-09-5b-53-de-ad
boardtype            bcm95365r
et1macaddr           00-00-00-53-de-ad
STARTUP              ifconfig eth0 -auto; boot -elf flash0.os:
}}}


= Restoring original firmware =
To restore the original firmware a serial console is required. You can use TFTP for the original images. It seems CFE's TFTP client will only read 4194304 bytes from the TFTP server. To get around the 4MB limit, we can split larger images into smaller chunks and then use the -offset flag to flash the parts.

 * boot the router normally and wipe !OpenWrt with
 {{{
mtd -r erase linux
}}}
 * get the original firmware image from Netgear's [http://kbserver.netgear.com/products/WGT634U.asp WGT634U support web site].
 * set the original kernel_args and configure the network interface
 {{{
CFE> setenv -p kernel_args "console=ttyS1,115200 root=/dev/ram0 init=linuxrc rw syst_size=8M"
*** command status = 0
CFE> ifconfig eth0 -addr=192.168.1.1 -mask=255.255.255.0;
Device eth0:  hwaddr 00-0F-B5-0E-49-D6, ipaddr 192.168.1.1, mask 255.255.255.0
        gateway not set, nameserver not set
*** command status = 0}}}
 * first you have to flash the full image. Notice, how many bytes it writes to the flash (in this example it wrote 3932160 bytes).
 {{{
CFE> flash -noheader tftp_host:wgt634u_1_4_1_10.img flash0.os
Reading tftp_host:wgt634u_1_4_1_10.img: Done. 3932160 bytes read
Programming...done. 3932160 bytes written
*** command status = 0}}}
 * split the image, bs=<bytes> are the bytes you should noticed in the previous step.
 {{{
dd if=wgt634u_1_4_1_10.img of=foo.img.1 bs=3932160 skip=1
}}}
 * flash the second part of the image, use the correct offset
 {{{
CFE> flash -noheader -offset=3932160 tftp_host:foo.img.1 flash0.os
Reading tftp_host:foo.img.2: Done. 786256 bytes read
Programming...done. 786256 bytes written
*** command status = 0}}}
 * after some minutes it's done. Finally execute
 {{{
CFE> reset
}}}
= Configuration =
The !OpenWrt port for Netgear WGT634U will '''not''' use any NVRAM configuration. Everything is configured in {{{/etc}}}. For network configuration please modify {{{/etc/config/network}}}. The NVRAM partition is your old config partition, so please back it up. You eventually need it to restore your original firmware. The WGT634U uses the madwifi driver for the wireless card. See [http://madwifi.org/wiki madwifi wiki] for several examples of how to configure access point/client mode/monitor mode and the up to date docs on the madwifi driver.

== Client-mode for the wireless card ==
The WGT634U also supports client-mode (aka managed mode). You need kmod-madwifi, which is probably already installed since it's selected by default.

Modes cannot be changed with iwconfig. You need wlanconfig. For help run it without parameters.

The usual commands would probably be:

{{{
ifconfig ath0 down    # if it isn't already down
wlanconfig ath0 destroy
wlanconfig ath0 create wlandev wifi0 wlanmode sta
iwconfig ath0 essid your_essid
}}}
You can then configure ath0 as usual with ifconfig and iwconfig. Iwconfig will display Mode: Managed, but the card will be in client-mode.

= Using USB drive for Root =
Normally, using the usb drive for root requires making a custom image with a proper bootline such as:

console=ttyS1,115200 root=/dev/scsi/host0/bus0/target0/lun0/part1 rootdelay=20 rw

However, here is a script for using the usb drive as root without having to recompile using the default 2.6 images.

If you want to utilize a swap partition when customizing this script, as I have, remember that you need the swap-utils package loaded as well.

'''MAKE SURE YOU READ THROUGH THE SCRIPT BEFORE COPYING AND EXECUTING IT BLINDLY!  There are custom variables at the top that you'll need to make sure complies with the partition table on the usb drive you are using.'''

You should have the minimum of the following modules loaded as well:

 * ehci_hcd
 * uhci_hcd
 * usb_storage
 * sd_mod
 * scsi_mod
 * usbcore
First create a /usb directory under the root directory and cut and paste this script i call linuxrc also under the root directory, and remember to customize the variables according to the partitions on your usb drive.  The current variables assume three partitions on the drive with the second partition being a swap partition.

 . {{{
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
}}}
We're not done yet, it's also imperative that you add a line into your init scripts to execute this script, so add the following line to the end of the /etc/init.d/S99done file:

 . {{{
[ -f /linuxrc ] && . /linuxrc
}}}
There!  Now when you go to reboot, your usb drive will be mounted as root as according to the linuxrc script.

= Serial console =
Default parameters for the serial console on J7 are 115200 N81.  

Options for serial console wiring include:
 * a Meraki Mini Serial adapter on J7, with the PCB hanging over the outside of the router (USB connector pointed towards the front fo the unit).
 * using a [http://www.maxim-ic.com/quick_view2.cfm/qv_pk/1068 MAX3232] chip.  If you want to build your own, a project and PCB are detailed at [http://members.shaw.ca/swstuff/wgt634u.html http://members.shaw.ca/swstuff/]. 
 * a cell phone data cable, for example the [http://www.radioshack.com/product/index.jsp?productId=2103605 Radio Shack "Mobile Phone Data Cable, Cable 22"] (part number 170-0762) works, clipping off the cell phone end and attaching the exposed wires as follows: green wire to GND; orange wire to RX; and white wire to TX; leaving VCC unconnected (may not be available any longer)  
 * some variant of the [http://www.ftdichip.com/Products/EvaluationKits/TTL-232R-WE.htm FTDI TTL-232R-3V3-WE].
 * build something with this: [http://www.sparkfun.com/commerce/product_info.php?products_id=718]

On a linux box, the USB tty devices usually show up at /dev/ttyUSBn.  You can point minicom (or similar) there.

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
= Switch port map =
{{{
--------------------------
| NETGEAR  p i w 1 2 3 4 |
--------------------------
}}}
||{{{p}}} ||power/status leds ||
||{{{i}}} ||port 4 ||
||{{{w}}} ||wireless ||
||{{{1}}} ||port 3 ||
||{{{2}}} ||port 2 ||
||{{{3}}} ||port 1 ||
||{{{4}}} ||port 0 ||
||SoC ||port 5 ||
= GPIO lines =
Several GPIO lines appear on little gold testpoints near the Broadcom chip.
|| GPIO bit || location ||
|| 0x80 || TP1 ||
|| 0x40 || TP2 ||
|| 0x20 || TP3 ||
|| 0x10 || TP4 ||
|| 0x08 || U6.13 to yellow Power LED ||
|| 0x04 || reset pushbutton ||
|| 0x02 || TP5 ||
|| 0x01 || ?? ||


More info at http://openwrt.pbwiki.com/GPIO

= Mini-PCI Upgrade =
The mini-pci card has been confirmed to be replaceable with an atheros AR5212 ABG Mini-PCI card, so likely any mini-pci card supported by the madwifi drivers can be used without fear of non-compatibility.

There seems to be some restriction to the power available to the mini-pci port. I've confirmed good driver compatibility with ubnt.com's SR2 and SR5, but at default (full) power levels significantly increased packet loss (15%, link runs solid with sub 0.1% loss @ 15 dBm)) is observed.  Use of a 16V/1.5A wall transformer did not improve performance. If the power problem is due to the bad stability of the original transformer, An transformer with a more accurate power output should work better. My Netgear wall tranformer used to have peaks about 17 Volt, that brings heavy load on the volt regulator inside the router. 

== Antenna Mod ==
The WGT634U comes equipped with an integrated antenna, which is soldered to the radio.  If you wish to use a different antenna, the most practical solution is to unsolder the pigtail and disassemble the antenna and collar.  Once the pigtail end is freed from the radio, it is a fairly simple task to remove both the antenna and the collar.  The [http://www.hirose.co.uk/productreleases/ms156.htm Hirose MS-156] test point is not a suitable attachment for a new pigtail.  The connector is not readily available and is not designed for attaching a permanent antenna.  Better is to solder on a new pigtail and run the coax outside the case where an antenna or more robust antenna coax can be attached.  See [http://cipheralgo.org/~jason/solder_b.jpg this picture] for an example of how it might be done.

= Other projects and information =
 * Some infos about setting up kamikaze [[BR]] - http://openwrt.loswillios.de/
 * A WGT-oriented Kamikaze wiki: [[BR]]- http://openwrt.pbwiki.com/
 * An OpenWrt-fork which concentrates on fewer routers (WGT634U included): [[BR]]- http://www.FreeWRT.org/
 * A Debian on WGT project: [[BR]] - http://www.cyrius.com/debian/bcm947xx/wgt634u/
 * More info in the forum: [[BR]]- http://openwrt.org/forum/viewtopic.php?id=33
 * External developer's Wiki [[BR]]- http://wgt634u.nomis52.net/
 * OpenWGT project (this project is not currently under active development) [[BR]]- http://openwgt.informatik.hu-berlin.de/
 * Another firmware project [[BR]]- http://router.4th.be/
 * Note on uploading large images (not openwrt) to the WGT634U (from [https://dev.openwrt.org/ticket/368 Ticket#368] ) [[BR]]- When using the wgt634u web upgrader (wgt634u-upgrade.cfg), you can't upload a file of more than 5120k. This is a problem for some images, such as the MIT roofnet openwrt image. I've fixed the problem, and posted the new version to http://xa.net/wgt634u-upgrade.cfg. The fix is to change the file etc/boa/boa.conf file, set the option SinglePostLimit from 5120 to 8192
= End Of Life =
I got confirmation from Janine Bodwin of Netgear that the WGT634U was EOL'ed on 01-Oct-2005

----
 . CategoryModel
