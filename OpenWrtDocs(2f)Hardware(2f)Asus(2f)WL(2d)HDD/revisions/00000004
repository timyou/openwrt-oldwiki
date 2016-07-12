'''Asus WL-HDD'''

The device is supported in OpenWrt 1.0 (White Russian) and later. You need to install the openwrt-brcm-2.4-<type>.trx firmware images.

{{{
Bootloader: CFE 
System-On-Chip:  Broadcom
CPU Speed: 200 Mhz
Flash size: 4 MB
RAM: 16 MB
Wireless: integrated Broadcom BCM4306 802.11b/g Wireless LAN Controller
Ethernet: 1x network controller, no switch
IDE-Controller: Yes
USB: 1x USB 1.1   
Serial: no
JTAG: no
}}}

The boot_wait NVRAM variable is '''on''' by default. Resetting to factory defaults via reset button or mtd erase nvram is '''not safe''' on this unit.

'''Installation'''

See OpenWrtDocs/Hardware/Asus/Flashing

'''IDE drivers and usage'''

To get the IDE device working, you should install the following packages:

{{{
  ipkg install kmod-ide kmod-ext3 nfs-server
}}}

Further you have to load the kernel modules in the correct order. My '''/etc/modules''' looks like this:
{{{
ide-core
pdc202xx_old
ide-detect
ide-disk
wl
jbd
ext3
}}}

The device still is missing '''fdisk''' and '''mkfs.*'''

'''USB drivers and usage'''

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
