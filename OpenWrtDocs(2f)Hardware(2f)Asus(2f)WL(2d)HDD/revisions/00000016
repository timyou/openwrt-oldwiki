'''Asus WL-HDD'''

The device is supported in OpenWrt 1.0 (White Russian) and later. You need to install the openwrt-brcm-2.4-<type>.trx firmware images.

{{{
Bootloader: CFE 
System-On-Chip:  Broadcom BCM4702KPB
CPU Speed: 200 MHz (125 for some)
Flash size: 4 MB, MX 29LV320ATTC-90
RAM: 16 MB, Hynix HY57V283220T-7
Wireless: integrated Broadcom BCM4306 802.11b/g Wireless LAN Controller
Ethernet: 1x network controller, no switch
IDE-Controller: Yes, PROMISE PDC20265R 
USB: 1x USB 1.1   
Serial: no
JTAG: no
}}}

The boot_wait NVRAM variable is '''on''' by default. Resetting to factory defaults via reset button or mtd erase nvram is '''not safe''' on this unit.

'''Installation'''

See  [:OpenWrtDocs/Hardware/Asus/Flashing: Hardware/Asus/Flashing].

'''WARNING:''' After installation, you must manually perform "nvram set wan_proto=none; nvram commit". Otherwise you will have a spurious dhcp client running on eth1, which is actually the LAN interface, and this can cause problems. See https://dev.openwrt.org/ticket/580

'''IDE drivers and usage'''

See IdeStorageHowTo then LocalFileSystemHowTo.

'''USB drivers and usage'''

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


'''Internal Images'''

[:OpenWrtDocs/Hardware/Asus/WL-HDD/InternalImages:Internal Images]


'''Power Consumption'''

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


----
CategoryModel
