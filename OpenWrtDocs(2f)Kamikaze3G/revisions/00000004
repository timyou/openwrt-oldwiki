= Using OpenWRT with GPRS / EDGE / UMTS / 3G modems =

Your OpenWRT supported router has a PCMCIA-Slot (so it probably is a WRT54G3G) or an USB port? So the idea to connect some 3G mobile wireless modem to it sound logical. There are many potential use cases, such as sharing a 3G connection with others in a meeting, using 3G as backup for your fixed Internet line or you may live in a non-DSL capable area and 3G is your primary Internet connection. In the days of HSDPA you will not be that bad off.

Trying to put this into practice, your mileage may vary. At the time of writing (late Oct 2008, Kamikaze 7.09) this will most likely '''not''' work out of the box unless you really have a WRT54G3G and some matching hardware which will mean it has to be quite outdated, unfortunately.

But there is hope ... in SVN and on this page.

== Why it doesn't work in the first place ==

Seen from the kernel's perspective, the form factor of your modem matters less than you think. Most PCMCIA card are actually PCMCIA based USB controllers with the modem attached while USB based modems attach directly to the USB bus. This is why there is little need to distinguish between USB modems and PCMCIA modems. But there is a need to distinguish at least three different types of devices:

 * Plain modems. They will be recognoied as ttyUSBx devices and will work with the stock usbserial driver in the kernel. Unfortunately, none of the more recent modems falls into this category.

 * "Flip / flop" enabled devices. See: http://www.draisberghof.de/usb_modeswitch/ In short words, these are modems which claim they are USB mass storage devices and expect their drivers to swtich them to the modem mode. The idea is quite nice for Windows users. If you plug the device for the first time into a Windows computer, autostart will install the driver for it. On subsequent connects the driver will recognize the device and switch it to modem mode before Windows will recognize it as a mass storage device. Unfortunately, this doesn't work on Linux. (The question is: why, BTW), so you will not have a modem but a mass storage device on which you will find a Windows driver that's unfortunately next to useless on Linux. The solution is simple: Use usb_modeswitch. Unfortunately, there is not package for OpenWRT (yet). Other tools that do the same are rezero and ozercdoff, see http://www.pharscape.org/. Unfortunately, again, no OpenWRT packages yet. But these class of devices turn again into nice ttyUSBx devices as soon as you switch them - if you can. Needless to say, this needs to happen every time you plug the device or reboot the router; no way to switch the mass storage mode off permanently.

 * HSO devices. Frequently found in case of HSDPA enabled devices, such as the Option Icon 225 with the 7.2 MBis/t firmware, for example. These devices are also flip / flop (i.e. need switching) but after that, still refuse to act as ttyUSBx devices. Actually, these deviced need an entirely different kernel driver, known as the HSO driver. Again, this can be found at http://www.pharscape.org/ as well as in the most recent Linux kernel (as of 2.6.27). But ... guess what ... no OpenWRT yet with that kernel version and no HSO package for OpenWRT yet.

== Making it work ==

As soon as you know in what category your device belongs, all it takes is on or both of:

 * usb_modeswitch for OpenWRT
 * kmod-hso for OpenWRT

== Where can I get these packages? ==

Try the attachments on this Wiki page ... at your own risk of course.

In case the binary packages don't work for you, you need to compile yourself. That means:

 1. Check out the OpenWRT trunk to $BUILDROOT - see https://dev.openwrt.org/
 2. Check out the libusb package and copy to $BUILDROOT/package - see https://dev.openwrt.org/ as well; packages are separate from the trunk!
 3. Download kmod-hso.tar.gz and usb_modeswitch.tar.gz and extract to $BUILDROOT/package
 4. Manually download hso-1.6.tar.gz from http://www.pharscape.org/ and place in $BUILDROOT/dl
 5. make menuconfig and make sure you choose:
  * Kernel 2.6
  * Enable libusb (Libraries)
  * Enable usb_modeswitch (Utilities)
  * Enable kmod-hso (Other modules)
 6. make

== Comments ==

At least Huawei E169 seems to hold the usb_modeswitched state for some seconds after unplugging. I used it with usb_modeswitch on a linux PC and then plugged it into an openwrt router which did not have the switch tool itself. I guess this works also with windows. Your router must never loose power for too long. Can someone confirm this phenomenon?
In usb_modeswitched state E169 exports 4 usb-serial lines. Before the switch it exports only one.
