= Asus WL-HDD =

The WL-HDD contains an IDE controller and a connector for a 2.5" disk drive. It has one Ethernet port and a !WiFi device, along with USB 1.1

== Installing OpenWrt ==

Follow the instructions in [:OpenWrtDocs/Installing:] ([http://wiki.openwrt.org/OpenWrtDocs/Installing#head-1ef14adf63da4e6b832bc324de813b846883e78a deep link])

== IDE device configuration ==

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
et
wl
jbd
ext3
}}}

The device still is missing '''fdisk''' and '''mkfs.*'''

== USB configuration ==

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
