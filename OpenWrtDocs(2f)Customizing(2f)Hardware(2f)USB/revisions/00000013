= USB =
If your OpenWRT compatible device has an USB port, you could attach a lot of USB devices.

 * http://www.linux-usb.org/
 * [http://www.nslu2-linux.org/wiki/Info/USBDeviceSupport USBDeviceSupport] @NSLU2 Linux
A list of OpenWRT compatible devices with [:WithUSBv2:USB v2.0 support] can be found in this wiki.

== First steps ==
Install and verify that the USB modules (~= drivers) are installed. The command {{{ipkg install kmod-usb-core kmod-usb-ohci kmod-usb-uhci kmod-usb2}}} will install all differnt kinds of usb controller. It is not necessary to install modules, but it will just work if you do not care. This wastes a little bit of RAM if you are loading modules that have no hardware to operate, that's all.

Hints:

 * Modules are stored in the AP/Router at {{{/lib/modules/<kernel-version>/}}}. List this directory with ls and pay attention to the files having "usb" in their name.
 * check if modules are loaded with the command {{{lsmod}}}
 * modules that are loaded at boot time will be added to the folder {{{/etc/modules.d}}}, if you install the kmod packages the modules will be automatically loaded after rebooting.
Detailed instructions can be found in UsbStorageHowto.

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
Infos on how to attach a [:webcam] to OpenWRT compatible devices can be found on a dedicated page.

=== USB Ethernet ===
If you need one (2..3..127) additional Ethernet ports, it is possible to use USB-to-Ethernet adaptor.

As example, Genius (KYE) GF3000U, Linksys USB100TX, D-Link DSB-650TX which are based on the [http://www.nslu2-linux.org/wiki/HowTo/AddEthernetAdapter ADMtek Pegasus] AN986.

Most of this devices has 10/100Mbit/s Full-Duplex Ethernet interface, but transfer rate is about 10Mbit/s only.

=== USB Bluetooth ===
It is possible, see this thread in the [http://forum.openwrt.org/viewtopic.php?id=1650 Forum].

=== USB VGA ===
http://www.winischhofer.at/linuxsisusbvga.shtml

=== USB Swap Space ===

See LocalFileSystemHowTo

See also http://www.opensourcerebels.org/forums/viewtopic.php?t=14
## incorrect instructions, the author creates a filesystem, then blows it away with mkswap. Revision 2.0 Released on 2/4/2007 Sorry for the mistake!

=== USB Sound devices ===
http://wiki.openwrt.org/UsbAudioHowto

http://www.nslu2-linux.org/wiki/HowTo/SlugAsAudioPlayer

[http://www.logitech.com/index.cfm/products/details/US/EN,CRID=2258,CONTENTID=6730 Logitech USB Headset for PlayStation 2]

[http://www.micronas.com/products/documentation/multimedia/uac355xb/index.php Micronas UAC355xB] USB Codec
