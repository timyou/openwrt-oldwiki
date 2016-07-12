= USB =
If your OpenWRT compatible device has an USB port, you could attach a lot of USB devices.

 * http://www.linux-usb.org/
 * [http://www.nslu2-linux.org/wiki/Info/USBDeviceSupport USBDeviceSupport] @NSLU2 Linux
A list of OpenWRT compatible devices with [:WithUSBv2:USB v2.0 support] can be found in this wiki.

== First steps ==
Install and verify that the USB modules (~= drivers) are installed. The command {{{ipkg install kmod-usb-core kmod-usb-ohci kmod-usb-uhci kmod-usb2}}} will install all differnt kinds of usb controller. It is not necessary to install modules, but it will just work if you do not care. This wastes a little bit of RAM if you are loading modules that have no hardware to operate, that's all.

Hints:

 * Modules are stored in the AP/Router at {{{/lib/modules/<kernel-version>/}}}. List this directory with {{{ls}}} and pay attention to the files having "usb" in their name.
 * check if modules are loaded with the command {{{lsmod}}}
 * modules that are loaded at boot time will be added to the folder {{{/etc/modules.d}}}, if you install the kmod packages the modules will be automatically loaded after rebooting.
Detailed instructions can be found in UsbStorageHowto.

== Add USB to your Siemens SE505 ==
See ["OpenWrtDocs/Hardware/Siemens/SE505"]

== USB Devices ==
=== USB Hard Drive ===
Already done, see UsbStorageHowto.

All "USB Mass Storage" class devices will work too: USB-to-IDE, some cellphones, come digital cams e.t.c.

=== USB Serial port/Modem ===
It is possible to connect a USB HUB and up to 127 USB-to-RS232 convertors.

Some USB cellphone datacables are dirt cheap and contains a USB-to-RS232 convertor (i.e. [http://gimel.esc.cam.ac.uk/james/resources/pl2303/ Prolific PL2303]).

refer to ["OpenWrtDocs/Customizing/Serial Console"] for further information about serial console.

=== USB Webcam ===
Infos on how to attach a ["webcam"] to OpenWRT compatible devices can be found on a dedicated page.

=== USB Ethernet ===
If you need additional Ethernet ports, it is possible to use USB-to-Ethernet adaptor.

For example, Genius (KYE) GF3000U, [http://www.linksysbycisco.com/UK/en/support/USB100TX Linksys USB100TX], D-Link DSB-650TX which are based on the [http://www.nslu2-linux.org/wiki/HowTo/AddEthernetAdapter ADMtek Pegasus] AN986 may be suitable.

Most have 10/100Mbit/s Full-Duplex Ethernet capability but transfer rates will likely be less than 10Mbit/s (presumably due to limitations of USB 2.0).

=== USB Bluetooth ===
It is possible. See this thread in the [http://forum.openwrt.org/viewtopic.php?id=1650 Forum].

=== USB VGA ===
There is no reference to openwrt on that page, but if you wanna try: [http://www.winischhofer.at/linuxsisusbvga.shtml http://www.winischhofer.eu/linuxsisusbvga.shtml]

=== USB Swap Space ===
See LocalFileSystemHowTo

See also http://www.opensourcerebels.org/forums/viewtopic.php?t=14

## incorrect instructions, the author creates a filesystem, then blows it away with mkswap. Revision 2.0 Released on 2/4/2007 Sorry for the mistake!
=== USB Sound devices ===
http://wiki.openwrt.org/UsbAudioHowto

http://www.nslu2-linux.org/wiki/HowTo/SlugAsAudioPlayer

[http://www.logitech.com/index.cfm/products/details/US/EN,CRID=2258,CONTENTID=6730 Logitech USB Headset for PlayStation 2]

[http://www.micronas.com/products/documentation/multimedia/uac355xb/index.php Micronas UAC355xB] USB Codec
