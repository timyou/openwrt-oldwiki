#pragma section-numbers off
#pragma keywords Asus, WL-HDD, Yakumo Wireless Storage 60
#pragma description This page contains information of the Asus WL-HDD and Yakumo Wireless Storage 60 NAS.
= Asus WL-HDD =

The device is supported in OpenWrt 1.0 (White Russian) and later. You need to install the openwrt-brcm-2.4-<type>.trx firmware images.

{{{
Bootloader: PMON
System-On-Chip:  Broadcom BCM4702KPB
CPU Speed: 200 MHz (125 for some)
Flash size: 4 MB, MX 29LV320ATTC-90
RAM: 16 MB, Hynix HY57V283220T-7
Wireless: integrated Broadcom BCM4306 802.11b/g Wireless LAN Controller
Ethernet: 1x network controller, no switch
IDE-Controller: Yes, PROMISE PDC20265R 
USB: 1x USB 1.1   
Serial: no, but possible to add an external UART
JTAG: no
}}}

The boot_wait NVRAM variable is '''on''' by default. Resetting to factory defaults via reset button or mtd erase nvram is '''not safe''' on this unit.

== Installation ==

See  [:OpenWrtDocs/Hardware/Asus/Flashing: Hardware/Asus/Flashing].

'''WARNING:''' After installation, you must manually perform "nvram set wan_proto=none; nvram commit". Otherwise you will have a spurious dhcp client running on eth1, which is actually the LAN interface, and this can cause problems. See https://dev.openwrt.org/ticket/580 and http://forum.openwrt.org/viewtopic.php?pid=35411

=== IDE drivers and usage ===

See IdeStorageHowTo then LocalFileSystemHowTo.

=== USB drivers and usage ===

See UsbStorageHowto then LocalFileSystemHowTo.

Run the following to install the modules and tools:
{{{
  ipkg install kmod-usb-ohci kmod-usb-storage kmod-vfat kmod-usb-printer lsusb
}}}

Add the usb modules to '''/etc/modules''':
{{{
...
usbcore
usb-ohci
scsi_mod
sd_mod
usb-storage
fat
vfat
}}}

=== Run root filesystem from the harddisk ===

GerardBraad describes some additional steps on how to make the root filesystem run from the harddisk. These instructions can be found in the forum at http://forum.openwrt.org/viewtopic.php?id=7373

== Network Configuration ==

As listed in [http://wiki.openwrt.org/OpenWrtDocs/Configuration OpenWrtDocs/Configuration] the network interfaces are configured as eth1 (wired) and eth2 (wireless). They are bridged in default installation. 

=== Device as Router ===
To open the bridge you have to change the interfaces for lan only to eth2, set the wan device to eth1 and configure these devices as you like (static, dynamic, etc) ([http://forum.openwrt.org/viewtopic.php?pid=37730])

{{{
lan_ifnames=eth2
lan_ifname=br0
wan_ifname=eth1
wan_device=eth1
}}}

If you want to use the wireless interface as lan and the ethernet as wan device, you also have to change the init script for the nvram because it restores it to default bridge behavier at startup. Uncomment two lines in /etc/init.d/S05nvram (maybe there should be a used nvram variable for optional bridge/router mode?):

{{{
# hacks for asus    
[ "$boardnum" = "asusX" ] && {     
        debug "### asus hacks ###"
        case "$(($(nvram get et1phyaddr)))" in                                 
                1) # WL-HDD                                                    
# don't need this as a router                              
#                    lan=eth1                              
#                    wan=none
}}} 


== Hardware ==
=== Internal Images ===

[:OpenWrtDocs/Hardware/Asus/WL-HDD/InternalImages:Internal Images]

If you want to open the device (maybe for exchanging the disk) remove the screws below the two little rubber-pads. Then slide the mainboard with the HD on it out of the case by carefully pulling the front plate.

=== Power Consumption ===

The device ships with a 2A 5V switch-mode power supply terminating to a DC plug.
The 2A rating may be to cover maximum spin-up current for the disk drive and the maximum USB 1.1 device current.

JamesCameron tested a device as follows:
 * !OpenWrt 1.0 White Russian RC5,
 * hdparm 6.3,
 * ASUSTeK Computer Inc. WL-HDD 2.5,
 * with an 80GB 5400RPM 8MB cache Seagate Momentus ST98823A drive (Asus specify a 40GB limit, but it is not clear why),
 * without USB devices attached,
 * without network cable attached,
 * with an association to a WORT54G access point two metres away (also !OpenWrt 1.0 White Russian RC5),
 * at room temperature of 19 degrees C,
 * horizontal,
 * using regulated 4.96V input,
 * using a digital multimeter on 10A scale.

||'''state'''||'''current'''||'''comment'''||
||spin-up||0.91A||disk drive by default spun itself up on power up||
||booting||0.64A|| ||
||booted||0.76A||disk drive consumes more power if it is recently accessed||
||idle||0.63A||disk drive may have a self-directed standby mode||
||active||0.91A||running an md5sum of a large file on disk drive||
||standby||0.48A||disk drive in host-directed standby mode, using ''hdparm -y'', further access by kernel spun the drive up||
||sleep||0.48A||disk drive in host-directed sleep mode, using ''hdparm -Y'', no apparent effect on power, but prevented further access to drive by kernel||

=== External Interface ===

This devices have some solder pads for a external interface likt the WL-500G. For using it please read [http://forum.openwrt.org/viewtopic.php?id=7083 this forum postings].

----
CategoryModel
