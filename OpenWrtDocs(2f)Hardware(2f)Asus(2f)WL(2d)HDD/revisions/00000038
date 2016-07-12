#pragma section-numbers off
#pragma keywords Asus, WL-HDD, Yakumo Wireless Storage 60
#pragma description This page contains information of the Asus WL-HDD and Yakumo Wireless Storage 60 NAS.
= Asus WL-HDD / Yakumo Wireless Storage 60 =

The device is supported in OpenWrt (White Russian and later). Confirmed running Version are WhiteRussian RC6 and 0.9 (and Kamikaze too, see [http://forum.openwrt.org/viewtopic.php?id=7510 this forum post]). You need to install the openwrt-brcm-2.4-<type>.trx firmware images. 

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

See UsbStorageHowto then LocalFileSystemHowTo. For a second usb-port see in the hardware section. 

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
wan_gateway=<SomeIp>
wan_netmask=<SomeMask>
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


=== Device as WLAN client ===

I got some strange double pings and lots of 
{{{
Feb 15 19:27:00 (none) kern.warn kernel: eth2: received packet with  own address as source address
}}}
entries in the logfile when using it as wireless client. this is a interference with the br0 and physical ethernet device; you can get rid of them by changing the lan interface to the physical instead of the virtual (br0) device.
{{{
# when wireless is the LAN interface and wired the WAN
nvram set lan_ifname=eth2
nvram commit
}}}

== Hardware ==
=== Internal Images ===

[:OpenWrtDocs/Hardware/Asus/WL-HDD/InternalImages:Internal Images]

If you want to open the device (maybe for exchanging the disk) remove the screws below the two little rubber-pads (could be that there are no screws, as on my yakumo. just pull on). Then slide the mainboard with the HD on it out of the case by carefully pulling the front plate.

=== Nvram Reset ===

If you made a mistake while configuring the router and it isn't reachable anymore via network, there is a posibility to reset the device config. To do that, plug the power off during booting, much times, at different timings. You can exploit a bug in the bootloader. The new ip is 192.168.1.1 then (attention, not the standard 192.168.1.220) and boot_wait is on. Now you are able to use tftp for uploading new images. [https://wiki.graz.funkfeuer.at/nvram_reset source]

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

=== Internal RTC ===

The internal RTC can be acessed with the proprietary module , which will taint the kernel. 

{{{
insmod rtcdrv.o
mknod /dev/rtc c 12 0
}}}
And this will show the hardware time:
{{{
cat /dev/rtc
}}}
I haven't found any posibillity to set the rtc, but setting the system time with a script with --hctosys works):
{{{
#!/bin/sh
case "$1" in
         --hctosys)
                [ -c /dev/rtc ] && /bin/cat /dev/rtc|(IFS=:;read Y M D dow h m s; /bin/date -s $M$D$h$m$Y.$s)
                ;;
         --systohc)
                [ -c /dev/rtc ] && /bin/date +%Y:%m:%d:%w:%H:%M:%S >/dev/rtc
                ;;
         *)
                echo "Usage: $0 {--systohc|--hctosys}" >&2
                ;;
esac
}}}

All stolen from [http://forum.openwrt.org/viewtopic.php?id=5606] and [http://wl500g.info/showthread.php?t=1642]

=== Second USB Port ===

Found on [http://wl500g.info/showthread.php?s=65d1ded33283574e7d0c3d86a9ec31fe&t=3571 wl500g.info] that on a wl500g it is possible to use the second port of the internal hub. As it looks the same on the wl-hdd, i tried this and it works too. Benefits of this hardware mod? First, no need for a external hub if using a printer or something permanently. Second, using it as internal port for another mods (audio?) without external cables. 

What to do? Not difficult, just put some wires with two resistors on the pcb, that's it. But: '''Build it at your own risk, you'll loose the warranty, and i'm not responsible for any damages of the router or of any device connected to it!'''

Step for step:

Maybe you've seen the log entries of the usb driver: 
{{{
Jan  1 00:00:15 (none) kern.info kernel: usb.c: new USB bus registered, assigned bus number 1
Jan  1 00:00:15 (none) kern.info kernel: hub.c: USB hub found
Jan  1 00:00:15 (none) kern.info kernel: hub.c: 2 ports detected
}}}
The two ports of the hub have on each data line a resistor to the ground. So we solder two wires on the third and fourth pin of the resistor array. In the posting mentioned above they use a resistor serial in each data line of 15 Ohms. I haven't had them, so i'm using somes with 10 Ohms. In the original connection between these resistors and the usb-socket is a resistance of 1.5 Ohms, so maybe that's enough too? Anyway. To get the power supply for the port i'm using the pads of a not assembled capacitor. It's not really correct, as there must be a control of the power consumption uf the usb device, but it works. I use the socket of a usb extension cable. Voila, here it is: 
{{{
Feb 25 20:48:36 (none) kern.info kernel: hub.c: new USB device 00:04.0-2, assigned address 2
}}}
See the [:OpenWrtDocs/Hardware/Asus/WL-HDD/usb_mod:usb_mod photos] with the details. 
=== External Interface ===

This device has some solder pads for a external interface likt the WL-500G. For using it please read [http://forum.openwrt.org/viewtopic.php?id=7083 this forum postings].

----
CategoryModel
