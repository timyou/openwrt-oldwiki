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

massstorage () {
        grep -q 'Vendor=1410 ProdID=5010' /proc/bus/usb/devices 2> /dev/null && /bin/true || /bin/false
}

tryeject () {
        /usr/bin/sdparm --command=eject /dev/sg0
}

case "$ACTION" in
        add) (  while $(massstorage) ; do tryeject ; sleep 2; done )
        ;;
esac

}}}
This small script doesn't depend on lsusb and tries to eject the mass-storage as long it's there. The while loop is needed, because it might not be ready for ejection, when the script is called first. We just try every 2 seconds until the mass-storage is gone.

Next problem is, that usbserial doesn't know the vendor and product id from novatel...

so modify /etc/modules.d/60-usb-serial to look like that:
{{{
usbserial vendor=0x1410 product=0x4400 # Novatel MC950D
}}}

If you plug MC950D in once kamikaze is running, dmesg now should look like this:

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
When you boot with the mc950d inserted, the order might be slightly different, but it automatically register the two serial devices just fine.

The hard part is done, you have the working serial devices and you overcame the mass-storage and usb-serial-vendor-id problem.

== testing with minicom ==

{{{
# opkg install minicom
}}}
run minicom and configure the serial-port with CTRL+A O -> Serial port setup -> Serial Device -> /dev/ttyUSB0 -> Save setup as dfl.
Restart minicom and it should be connecting to the mc950d

{{{
AT
OK

AT+CPIN?
+CPIN: SIM PIN
OK

AT+CPIN=1234
OK

AT+CPIN?
+CPIN: READY
OK

}}}

The led on the mc950d should now stop blinking red and show whatever network is usable (blue = umts, yellow = hsdpa, green = GPRS, lila = EDGE)

'''Note: if you don't run minicom once (you don't have to do anything, just start minicom and quit it with CTRL-A Q), gcom doesn't work and the kernel usb-serial module gets [http://pastebin.com/f42c97a28 hickup].'''

It seems that the serial port initialization by minicom does something important, have to figure out, what it is.



== gcom / gtcom ==

Install the needed stuff with

{{{
# opkg install chat
# opkg install ppp
# opkg install comgt
}}}

Edit /etc/config/network through adding the following:

{{{
config interface ppp0
        option ifname   'ppp0'
        option proto    '3g'
        option device   '/dev/ttyUSB0'
        option apn      'access.vodafone.de'
        option pincode  '1234'
}}}
Make sure, you change the pincode line to your pin code, if your sim asks for one.

Test gcom
{{{
root@OpenWrt:~# gcom info -d /dev/ttyUSB0
##### Wireless WAN Modem Configuration #####
Product text:
====

Manufacturer: Novatel Wireless Incorporated
Model: Ovation MC950D Card
Revision: 3.18.02.0-00  [2008-04-15 16:18:23]
IMEI: xxx
+GCAP: +CGSM,+DS
OK
====
Manufacturer:           Novatel Wireless Incorporated
IMEI and Serial Number: xxx
Manufacturer's Revision:
3.18.02.0-00  [2008-04-15 16:18:2
Hardware Revision:

Network Locked:         0
Customisation:

Band settings:          (
)
APN:                    1,"IP","access.vodafone.de","",0,0
##### END #####
}}}

you can try, whether setting the pin works:

{{{
root@OpenWrt:~# COMGTPIN=1234 gcom PIN -d /dev/ttyUSB0
SIM ready
}}}

Now try connecting:

{{{
root@OpenWrt:~# ifup ppp0
grep: /proc/diag/model: No such file or directory
grep: /proc/diag/model: No such file or directory
Manufacturer: Novatel Wireless Incorporated
SIM ready
PIN set successfully
Trying to set mode
grep: /proc/diag/model: No such file or directory
}}}

The /proc/diag/model doesn't exist, but it doesn't seem to cause any problems...

You can use logread to check, if it worked:

{{{
# logread
Aug 10 16:34:02 OpenWrt daemon.notice pppd[2918]: pppd 2.4.3 started by root, uid 0
...
Aug 10 16:34:04 OpenWrt daemon.info pppd[2918]: Serial connection established.
Aug 10 16:34:04 OpenWrt daemon.info pppd[2918]: Using interface ppp0
Aug 10 16:34:04 OpenWrt daemon.notice pppd[2918]: Connect: ppp0 <--> /dev/ttyUSB0
Aug 10 16:34:08 OpenWrt daemon.warn pppd[2918]: Could not determine remote IP address: defaulting to 10.64.64.64
Aug 10 16:34:08 OpenWrt daemon.info dnsmasq[2445]: reading /tmp/resolv.conf.auto
Aug 10 16:34:08 OpenWrt daemon.info dnsmasq[2445]: using nameserver 139.7.30.126#53
Aug 10 16:34:08 OpenWrt daemon.info dnsmasq[2445]: using nameserver 139.7.30.125#53
Aug 10 16:34:08 OpenWrt daemon.info dnsmasq[2445]: using local addresses only for domain lan
Aug 10 16:34:08 OpenWrt daemon.notice pppd[2918]: replacing old default route to br-lan [192.168.1.1]
Aug 10 16:34:08 OpenWrt daemon.notice pppd[2918]: local  IP address 10.248.245.1
Aug 10 16:34:08 OpenWrt daemon.notice pppd[2918]: remote IP address 10.64.64.64
Aug 10 16:34:08 OpenWrt daemon.notice pppd[2918]: primary   DNS address 139.7.30.125
Aug 10 16:34:08 OpenWrt daemon.notice pppd[2918]: secondary DNS address 139.7.30.126
}}}

So, you are up and running...


Routing should work automatically, if you name that interface 'wan'.
