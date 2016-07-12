= NanoStation2 =
== Hardware ==
 * Bootloader: RedBoot
 * CPU: Atheros AR2315 according to the datasheet and cpuinfo, but chip is marked as AR2316A !!
 * CPU Speed: 180 Mhz
 * Flash size: 4 MB
 * RAM: 16 MB
 * Wireless: Atheros 802.11b/g (in CPU, 400mW)
 * Ethernet: 1 port connected to the CPU
 * Power: passive POE (pairs 4,5+; 7,8 return) 12 to 18 VDC (POE injector included in the package)
 * Serial: internal (HE-10 connector, 3.3V)
 * [:OpenWrtDocs/Customizing/Hardware/JTAG Cable:JTAG]: yes, internal (solder pads, 3.3V)
This device is an integrated wifi spot designed to be used outdoor. With Ubiquiti Firmware, AirOS 3 actually, it can act as station, station WDS, client, client wds... There is a dual patch antenna system able to work in vertical or horizontal polarity, or to send RF to an external RP-SMA female or SMA female connector (depending of date of manufacturing) - This feature is software selectable with AirOS.

http://ubnt.com/downloads/press_nano.jpg

The Nanostation comes with a 12V powersupply, the internal DC-Converter seems to be realized with a AP1510 PWM Control 3A Step-Down Converter. This can handle up to 23V. (untested)

=== Opening the case ===
There are two screws under the label on the back.  After removing these, the board can be removed.

#http://www.flickr.com/photos/mattw/2401470901/
attachment:unscrewed_ns2.jpg

#http://www.flickr.com/photos/mattw/2402299466/
attachment:opening_ns2.jpg

attachment:serial_ns2.jpg

== OpenWrt ==
The NanoStation2 is supported by the OpenWrt AtherosPort.  It is available as a pre-built image and can be built through buildroot.

=== Installing ===
The OpenWrt buildroot generates images that can be directly flashed to the NS2, usually with a name like openwrt-atheros-ubnt2-squashfs.bin. The Ubiquiti web interface will warn that it's an unsupported third-party firmware, but that's just a warning.

=== Upgrading ===
In order to upgrade from OpenWrt to a newer version, both the kernel mtd and filesystem mtd must be reflashed.  The kernel is likely lzma compressed.  If either mtd block isn't big enough, reflashing can not be completed through OpenWrt, but must be done through the [:OpenWrtDocs/Bootloaders/RedBoot:RedBoot bootloader].

=== Recovery ===
==== Requirements ====
 * Ethernet cable connection between PC and NanoStation.  A switched connection or a bridged connection seems to work fine.
 * Network settings of PC: 192.168.1.254/255.255.255.0
 * TFTP client on PC
 * NanoStation firmware file from Ubiquiti (not an OpenWrt image)
==== Procedure ====
 1. Turn off the device
 1. Press the reset button
 1. Turn on the device
 1. Release the reset button ~10 seconds (but not longer) after turning the device on
 1. Ping 192.168.1.20.  If it works, you're ready to upload an image, if not, go back to step 1.
 1. Rename the firmware image to {{{flash_update}}} (might not be required if a recent Ubiquiti firmware has been installed)
 1. Use a tftp client to upload {{{flash_update}}} to the device in binary mode
{{{
tftp 192.168.1.20
tftp> bin
tftp> put flash_update
Sent 1965199 bytes in 28.8 seconds
tftp> quit
}}}
 7. Signal LEDs might be blinking during the upgrade
 7. Wait ~7 minutes before restarting
 7. Restart.  The device should be back to its old configuration (OpenWrt doesn't overwrite or modify the NVRAM settings).
=== External antenna ===
The two internal antennas work more or less automatically, using the driver's "diversity" setting to choose the correct one.  Using an external antenna requires manually setting a few things:

{{{
sysctl set dev.wifi0.softled 0
gpioctl 7 0
}}}
These can be added to an init file in /etc/rc.d and /etc/init.d

----
#### DO NOT REMOVE THIS NOTICE WITHOUT REMOVING ATTACHED IMAGES
Some photos on this page (c) [http://www.flickr.com/photos/mattw/ Matt Westervelt] and available for use under a [http://creativecommons.org/licenses/by-nc-sa/2.0/deed.en Creative Commons license] for non-commercial works.
