= WRT54G3G on 3G/UMTS, using Merlin U630 Card =
The WRT54G3G, has a PCMCIA slot on it.  Linksys created this beast for Vodafone, as a kind of take anywhere wireless access point.    The Merlin U630 card essentially presents itself as a serial modem.  By loading the appropriate modules, and setting up ppp, you can make this work under OpenWRT.

The standard White Russian binarys don't contain all of the required bits in order to get it to work. You will need to compile your own binarys, using buildroot.

 . You will need to include kmod-pcmcia-serial, and kmod-ppp.

= Using a Novatel MC950D with kamikaze trunk (2008-09-08) =

It's not trivial, so I give a small walk-through.

I'm using a NSLU2 which is going to be a UMTS-Router for my wired network. The steps should be the same for every other kamikaze-trunk build.

Compiling trunk is pretty straight forward:
{{{$ svn checkout https://svn.openwrt.org/openwrt/trunk
$ cd trunk
$ make menuconfig
[select Target System (Intel XScale IXP4xx [2.6]) and Target Profile (Linksys NSLU2)]
$ nice -n 19 make -j 2
... when everything is done... put NSLU2 in upgrade mode (hold the reset-button while powering up and wait, till the led goes red)
$ sudo upslug2 --device=eth1 --image=bin/openwrt-nslu2-squashfs.bin
...
Rebooting... done                                                               

$ telnet 192.168.1.1 (with user root)
// Change password with passwd

$ ssh -l root 192.168.1.1}}}

change ip in /etc/config/network and add the following lines 
{{{
 option gateway x.y.z.a
 option dns x.y.z.a
}}}

reboot and internet should be working, install the usb-serial package and the eject tool in sdparm

{{{
# opkg update
Downloading http://downloads.openwrt.org/snapshots/ixp4xx/packages/Packages
...
# opkg install kmod-usb-serial
# opkg install sdparm
...
}}}
the novatel umts stick will appear as a usb mass storage device with windows drivers on it and will only change it's functionality, when this mass-storage-thing is ejected, so here we go:
create the file /etc/hotplug.d/usb/20-novatel_switch

{{{
#!/bin/sh

case "$ACTION" in
        add) ( grep -q 'Vendor=1410 ProdID=5010' /proc/bus/usb/devices  && sleep 3 &&  /usr/bin/sdparm --command=eject /dev/sg0 2>&1  )
        ;;
esac
}}}
I found this in the forum, but there wasn't the sleep 3 and it didn't work for me without it, because the /dev/sg0 isn't there, when this script is called. Also doesn't this version depend on lsusb, which I didn't have and didn't need...

Next problem is, that usbserial doesn't know the vendor and product id from novatel...

so modify /etc/modules.d/60-usb-serial to look like that:
{{{
usbserial vendor=0x1410 product=0x4400 # Novatel MC950D
}}}

The eject doesn't work when booting with this stick, but if you plug that umts-stick in once kamikaze is running, dmesg now should look like this:

{{{
usb 2-1: new full speed USB device using ohci_hcd and address 4
usb 2-1: configuration #1 chosen from 1 choice
scsi0 : SCSI emulation for USB Mass Storage devices
usb-storage: device found at 4
usb-storage: waiting for device to settle before scanning
scsi 0:0:0:0: CD-ROM            Novatel  Mass Storage     1.00 PQ: 0 ANSI: 2
scsi 0:0:0:0: Attached scsi generic sg0 type 5
usb-storage: device scan complete
usb 2-1: USB disconnect, address 4
usb 2-1: new full speed USB device using ohci_hcd and address 5
usb 2-1: configuration #1 chosen from 1 choice
usbserial_generic 2-1:1.0: generic converter detected
usb 2-1: generic converter now attached to ttyUSB0
usbserial_generic 2-1:1.1: generic converter detected
usb 2-1: generic converter now attached to ttyUSB1
}}}

The hard part is done, you have the working serial devices and you overcame the mass-storage and usb-serial-vendor-id problem.

Next thing to configure is gcom. (To be continued tomorrow)
