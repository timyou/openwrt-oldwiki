This is a table of peripheral devices (such as USB audio, video, serial, printer, HID or network storage) which have been tested or are known to work (or not work, as indicated) under control of a unit running embedded Linux. This is not a test of whether the device itself can be run as an embedded stand-alone processor - these are peripherals only. See the main TableOfHardware for devices on which to run OpenWrt. 

'''Status Legend''':

 * '''Supported''' - supported in White Russian (previous release)
 * '''Partial''' - partially supported, such as multifunction devices in which only some functions work.
 * '''Untested''' - should work in theory but never tested
 * '''Kamikaze''' - this device is only supported in Kamikaze (current release)
 * '''Kamikaze/2.6''' - this device is only supported in Linux 2.6 kernels under Kamikaze (current release)
 * '''WiP''' - Work in Progress 
 * '''Forked''' - Vendor has released some source, but it has not been merged into the main !OpenWrt source tree
 * '''No''' - confirmed that this device is not supported 
 * '''Info entered''' - Information about the device is entered in this list, for reference.

Devices are grouped by interface, which will typically be USB, network or (rarely) direct internal connection of serial or flash memory interfaces as hardware modifications. They are then sub-grouped by device type.

As of 2007, USB-capable platforms include the Linksys WRTSL54GS, the ASUS WL-500g series and the ASUS WL-700 routers. The Linksys NSLU2 network attached storage interface may also be used to control various USB devices.

== USB devices ==

=== Printers ===
There are two printing subsystems in common use on this platform. The P910nd server is a simple pass-through with no capabilities for spooling or processing data before it is sent to the printer; its capabilities are limited but it will work with most USB printers. The CUPS common unified printing system is a spooler, it does process data into a form specific for each individual printer and it does allow printers to be shared through Samba, the Windows-compatible network device subsystem.

To work with CUPS, a device must have a driver that will run directly on the embedded Linux platform. As such, devices for which no Linux drivers exist or for which Linux desktop-PC object code with no sources are provided cannot be listed as being fully compatible in this section. They may work adequately with P910nd's passthrough (as the conversion to printer-specific data formats remains on the desktop) but do not work at all under CUPS.

||'''Manufacturer'''||'''Model''' ||'''Version''' ||'''Status''' 
||Samsung||SCX4521||n/a||'''Unknown.''' Multifunction device. The Linux drivers shipped with this unit are object-code only and compiled for x86 and amd64 desktop PC's; the manufacturer's drivers therefore will not run on embedded platforms.

=== Scanners ===
SANE (Scanner Access Now Easy) is designed in such a way as to allow scanners to be shared over a TCP/IP network. The processor which controls the scanner runs a server, the processor on a desktop PC runs a SANE client in order to use the shared scanning device. There is an application (!SaneTwain) which allows a Windows PC to access these shared servers.

To be compatible with a networked device-sharing configuration, the scanner must have SANE drivers which run under embedded Linux. Unlike the printers, there is no p910nd-style passthrough driver. Scanners designed to connect to parallel or SCSI ports will not work (the USB-parallel adapters control actual parallel printers only, but cannot control any other devices such as removable storage, scanners or EPROM device programmers that connect to desktop PC parallel ports in place of printers). Some of the scanners which support USB directly may work, but compatibility varies between models.

=== Multifunction printers ===
These devices consist of a scanner, a printer and (most often) a FAX modem as one integrated unit. As such, they physically resemble photocopiers or facsimile machines.

Interface is most often USB, or a combination of USB and some other connection type (such as parallel or network, often for the printer only).

=== Human interface devices ===
This category exists primarily for interface to keyboards and mice. USB joysticks and game adapters typically also fall into this category, as well as calculator-style numeric keypads designed for use with USB laptops. There is a standard USB device class for these; usually there is no requirement for manufacturer-specific drivers. 

These are supported in the standard distribution, although bugs have been reported: https://dev.openwrt.org/ticket/2184

Support for a few oddball devices (such as the Microsoft force-measuring joysticks) is still 'experimental'.

=== Storage devices ===
External USB hard drives, CD/DVD readers, flash memory card readers and flash memories are supported by a standard USB storage device class. These require usb-core.ko, usb-storage.ko usb2 (preferably) and drivers for the appropriate file system (vfat.ko, fat.ko, ext3.ko and others for HDD/flash devices, isofs for CD/DVD's); the drivers are part of the standard distribution and, in general, this class of device is well-supported.

=== Network interfaces ===
USB could be used to add an additional wired-LAN port; these are not often needed, but some models do work with usbnet.ko and a device-specific driver.

||'''Manufacturer'''||'''Model''' ||'''Version''' ||'''Status''' 
||ASIX||88772||n/a||'''Kamikaze/2.6''' Supported by asix.ko + usbnet.ko modules in standard Kamikaze 2.6 distributions. No Linux 2.4 drivers exist for this interface.

=== Wireless network interfaces ===

=== Bluetooth ===

=== Personal digital assistants ===
Palm OS-based devices apparently operate under a Linux-like OS and may be compatible. The same is not true of the Pocket PC.

Pocket PC devices such as HP/Compaq's iPAQ line are Windows-based and poorly/not fully supported. It may be possible to get a TCP/IP connection for standard Internet applications such as telnet or web (there is a PuTTY available as an SSH client to run on these) but synchronisation to the Windows desktop is by proprietary means.

=== Digital cameras ===
These fall into two categories: Many appear simply as standard USB network storage devices and may be accessed in the same manner as any USB flash memory reader; these in general are compatible. A few use USB as a means to control the camera itself, these may work if an application such as gphoto2 is installed to access them.

=== Video capture ===
There is a standard device class for USB video, used primarily for webcams and video capture devices. This is supported by the video4linux drivers.

Some webcams may require device-specific drivers; the level of support for these is model-dependent.

=== Other multifunction devices ===

== NAS servers ==

These appear on the network as SMB servers; often other protocols such as FTP are optionally supported.

||'''Manufacturer'''||'''Model''' ||'''Version''' ||'''Status''' 
||?||LanDrive||n/a||'''Compatible''' with Linux under smbfs; not recognised by some Linux CIFS drivers. A low-end Taiwanese unit, cloned in mainland China as the LanServer knock-off, provides NAS and USB but does not allow both to be used at once. On USB, acts as standard storage-class device. File system is VFAT only. 

== NAS clients ==
||'''Manufacturer'''||'''Model''' ||'''Version''' ||'''Status''' 
||Hauppauge||MediaMVP||previous to H1||'''Compatible''', boots as diskless workstation from network. Requires that DHCP provide the name of a boot file, which is then retrieved via TFTP. See MediaMVPHowTo for more info on this small Linux-based (250MHz PowerPC) device.
||Hauppauge||MediaMVP||H1 through H4||'''Kamikaze''', boots as diskless workstation from network. Requires installation of an application (MVPrelay) to provide the name of a boot file, which is then retrieved via TFTP. This app is included in Kamikaze but is not currently in the stable Whiterussian distributions unless you build it yourself.

== Serial ==
Some Linux-based routers provide the ability to add one (or sometimes two) serial ports by connecting level-translation hardware inside the device. These serial ports provide bidirectional data but do not provide control signals; as such, hardware handshake will not work. See the hardware modification how-to for details.

== SD/MMC ==
It is typically possible to connect these flash memory cards directly to GPIO lines inside the unit, however this is normally much slower in operation than USB flash readers.  Not for the faint of heart; see the hardware modification how-to for details.
----
CategoryCategory
