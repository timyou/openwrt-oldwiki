= USB =
If your WRT* has a USB port, you could attach a lot of USB devices.

 * http://www.linux-usb.org/
 * [http://www.nslu2-linux.org/wiki/Info/USBDeviceSupport USBDeviceSupport] @NSLU2 Linux

'''NOTE:''' "OpenWrt" devices offering [:WithUSBv2:USB v2.0 support].

== First steps ==
First of all you should check if the necessary USB-kernel-modules are installed (check /lib/modules/<kernel-version> for usb*.o) and loaded (lsmod is doing this).

Generic modules are in the following packages:

- kmod-usb-core

- kmod-usb-ohci or kmod-usb-uhci or kmod-usb2 (depends on hardware)

Details instructions can be found in UsbStorageHowto.

== add USB to your Siemens SE505 ==
On the side with the powerplug you will find some 'C's

- add C906 with 100µF 16Volt

- add C986 with 10µF 16Volt

- add U981 with an LM7805

This will support the +5 Volt to your USB-Port.

Go to the other side of the PCB wehre the antenna is placed.

- add wire to F51 as Fuse

- add to 'R' about 15kOhm to R723 and R724

- shorten R733 R734

- put an USB-Plug to J51

Thats all.

== USB Hard Drive ==
Already done, see UsbStorageHowto.

All "USB Mass Storage" class devices will work too: USB-to-IDE, some cellphones, come digital cams e.t.c.

== USB Serial port/Modem ==
It is possible to connect a USB HUB and up to 127 USB-to-RS232 convertors.

Some USB cellphone datacables are dirt cheap and contains a USB-to-RS232 convertor (i.e. [http://gimel.esc.cam.ac.uk/james/resources/pl2303/ Prolific PL2303]).

refer to ["OpenWrtDocs/Customizing/Serial Console"] for further information about serial console.

=== USB Webcam ===
Check out this page: http://www.nslu2-linux.org/wiki/HowTo/AddUsbWebcam

Asus [:OpenWrtDocs/Hardware/Asus/WL500GD:WL-500G-Deluxe] has a Webcam support and Motion Detection software in the default firmware.

If you have a Philips-based cam (Philips and many Logitechs, also others) and a USB port, you can try the following (tested by me on an ASUS WL500GX):

 1. Grab the "Tom" package from here: http://wl500g.info/showpost.php?p=8610&postcount=17 (and be sure to read through some of the posts) and install it, then erase the /lib/modules/2.4.20/pwc.o file
 1. Download the kmod-videodev and kmod-pwc packages from http://downloads.openwrt.org/people/nico/whiterussian/packages/
 1. Install them :)
 1. Plug in you camera and enjoy! You can use camsrv to stream images, mvc as a simple motion detector... or compile your own programs.

Note: the video device will most likely be /dev/v4l/video0 instead of the common /dev/video0, because of devfs. Just use the correct parameters when you invoke the programs.

=== USB Ethernet ===
If you need one (2..3..127) additional Ethernet ports, it is possible to use USB-to-Ethernet adaptor.

As example, Genius (KYE) GF3000U, Linksys USB100TX, D-Link DSB-650TX which are based on the [http://www.nslu2-linux.org/wiki/HowTo/AddEthernetAdapter ADMtek Pegasus] AN986.

Most of this devices has 10/100Mbit/s Full-Duplex Ethernet interface, but transfer rate is about 10Mbit/s only.

=== USB Bluetooth ===
It is possible, see this thread in the [http://forum.openwrt.org/viewtopic.php?id=1650 Forum].

=== USB VGA ===
http://www.winischhofer.at/linuxsisusbvga.shtml

=== USB Sound devices ===
http://wiki.openwrt.org/UsbAudioHowto

http://www.nslu2-linux.org/wiki/HowTo/SlugAsAudioPlayer

[http://www.logitech.com/index.cfm/products/details/US/EN,CRID=2258,CONTENTID=6730 Logitech USB Headset for PlayStation 2]

[http://www.micronas.com/products/documentation/multimedia/uac355xb/index.php Micronas UAC355xB] USB Codec
