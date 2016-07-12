= USB =
If your OpenWRT compatible device has an USB port, you could attach a lot of USB devices.

 * http://www.linux-usb.org/
 * [http://www.nslu2-linux.org/wiki/Info/USBDeviceSupport USBDeviceSupport] @NSLU2 Linux

A list of OpenWRT compatible devices with [:WithUSBv2:USB v2.0 support] can be found in this wiki.

== First steps ==
Install and verify that the USB modules (~= drivers) are installed.
The command {{{ipkg install kmod-usb-core kmod-usb-ohci kmod-usb-uhci kmod-usb2}}} will install all differnt kinds of usb controller. It is not necessary to install modules, but it will just work if you do not care. This wastes a little bit of RAM if you are loading modules that have no hardware to operate, that's all.

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
Attaching a webcam is a very common wish. Companies like Asus for example have integrated webcam support (ov511, pwc 8.11 --> low resultion only) to their stock firmware including motion detection and streaming ([:OpenWrtDocs/Hardware/Asus/WL500GD:WL-500G-Deluxe]). By installing the OpenWRT firmware it is possible to circumvent disadvantages like usage of ActiveX for the webcam stream, limited resoultion etc.

What to do:

 * First step is to determine the driver that can grab pictures of the webcam. Many cameras are covered by the pwc driver or the ov511. Please consult the project websites to get a list of supported webcams or try to use them with a linux PC.
 * Install USB modules for your AP/Router device.
 * Install the V4L (video for linux) driver
 * Install webcam driver.
 * Install a programm that  takes the video from the video device and turns them into a stream, or react to movements for instance. Of course you are not limited to those examples if you are aware of another programm that can do somthing fancy with your webcam. Most likely you want to install the package "motion" since it handles the most common usages like streaming AND motion detection at once.
For instance, if you have a Asus WL-500g Premium running OpenWRT RC5 and you want to install a Philips Webcam (like PCVC690k) to it, enter the shell of the AP and perform the following commands:

 * {{{ipkg install kmod-usb-core kmod-usb-ohci kmod-usb-uhci kmod-usb2 kmod-videodev}}}
 * {{{ipkg install http://naaa.de/programme/philips-webcam/philips-webcam_0.2_mipsel.ipk}}}
 * {{{reboot}}}
The webcam can be accessed at http://<IP>/CamClient.html after the device has rebooted.

If you prefer MJPEG streams and motion detection at once (and a higher framerate of ~1 to 2 frames per second) use motion. A backported version of "motion" can be installed with the following command:

 * {{{ipkg install kmod-usb-core kmod-usb-ohci kmod-usb-uhci kmod-usb2 kmod-videodev}}}
 * {{{ipkg install http://naaa.de/programme/philips-webcam/philips-webcam_0.2_mipsel.ipk}}}
 * {{{ipkg install http://naaa.de/programme/motion/libjpeg_6b-1_mipsel.ipk}}}
 * {{{ipkg install http://naaa.de/programme/motion/motion_3.2.6-1_mipsel.ipk}}}
 * edit the {{{/etc/init.d/S90webcam}}} starup script and place a {{{motion.conf}}} file at {{{/etc/motion.conf}}}.
Do not expect to much performance like a real IP-Cam has. This solution will deliver one or two frames per second without audio. But on the other hand even cheap wired IP-Cam cost about 100 EUR,-. An Asus with webcam costs about the same but can do more things and is wireless.

Hint: The pwc, pwcx packages were just tested with Asus WL-500gP so far. There is no guarantee that your device will not break!

Important Hint: The video device will most likely be /dev/v4l/video0 instead of the common /dev/video0, due of the devfs. Just use the correct parameters when you invoke the programs since most assume it to be /dev/video0.

OV511 users may have to look for modules for their cameras a little bit more, but it was done before. For those models an update of this description is needed and welcome. It's a wiki so please contribute ;-)

More Links:
 * http://www.nslu2-linux.org/wiki/HowTo/AddUsbWebcam
 * http://forum.openwrt.org/viewtopic.php?id=143
 * http://wl500g.info/showpost.php?p=8610&postcount=17

 * Plain modules for 2.4.30 mipsel:
  * http://naaa.de/programme/module_2.4.30/ov511.o
  * http://naaa.de/programme/module_2.4.30/quickcam.o
  * http://naaa.de/programme/module_2.4.30/pwc.o
  * http://naaa.de/programme/module_2.4.30/pwcx.o

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
