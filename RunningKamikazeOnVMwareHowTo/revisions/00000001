This !HowTo explains how to get OpenWRT running on VMware. This only works with the development version (kamikaze), the old stable version (whiterussian) is not supported. This has been tested on a WindowsXP and Linux host system.

= Using prebuilt images =

 1. Download the free VMware Player (recommended and enough for most users) or Server from [http://www.vmware.com/ VMware] and install it
 1. Download a precompiled Kamikaze (x86-2.6) VMware image and VMware configuration file from [http://www2.informatik.hu-berlin.de/~nachtiga/openwrt/openwrt-x86-2.6-ext2_VMware-image-and-config.zip openwrt-x86-2.6-ext2_VMware-image-and-config.zip] (1.9 MB) and unzip the archive (the image was built with a kamikaze version freshly checked out on 24 Feb 2007)
 1. Open the vmx file with VMWare Player (or simply double click on it)

Virtual disk size set to 128MB with EXT2 filesystem. Virtual RAM size set to 128MB. Default IP address is 192.168.1.1. VGA output and keyboard support (english) are enabled.

On a Windows host-system the virtual serial console is accessible e. g. using PuTTY connected to \\.\pipe\com_1 @ 115200 8n1.

= Doing it yourself =
== Building your own image ==

To build your own Kamikaze VMware image you need a OpenWrt development environment (with ''qemu-img'' (part of the [http://packages.debian.org/qemu qemu package] on Debian) installed on the Linux host-system to convert the image):
 1. check out with "{{{svn co https://svn.openwrt.org/openwrt/trunk/}}}" 
 1. Then you need to apply the following patches to the freshly checked out OpenWrt Kamikaze build-system (these are not yet in official repository):
  * [http://openwrt.ertl-net.net/kamikaze/fix-console-tty.patch fix-console-tty.patch]
  * [http://openwrt.ertl-net.net/kamikaze/add-vmware-images.patch add-vmware-images.patch]
  * [http://www2.informatik.hu-berlin.de/~nachtiga/openwrt/x86-2.6_vt_01.patch x86-2.6_vt_01.patch]
  * [http://www2.informatik.hu-berlin.de/~nachtiga/openwrt/x86-2.6_vt_02.patch x86-2.6_vt_02.patch]
 1. After applying the patches run 'make menuconfig' and select:
  * Target System (x86 [2.6])
  * Target Profile (VMware image)
  * Target Images
   * [ ] jffs2 <-- N
   * (115200) Serial port baud rate
   * (128) Filesystem part size (in MB)
 1. run "{{{make}}}" to build the VMWare image (which ends up in {{{bin/openwrt-x86-2.6-ext2.vmdk}}})

== Creating the VMware configuration file ==
The openwrt-x86-2.6-ext2.vmx file as included in the above [http://www2.informatik.hu-berlin.de/~nachtiga/openwrt/openwrt-x86-2.6-ext2_VMware-image-and-config.zip zip file] was creating at http://www.easyvmx.com with the following settings:

 * Basic Configuration
  * Virtual Machine Name: OpenWrt Kamikaze (x86-2.6)
  * Select GuestOS: Generic Linux 2.6.x
  * Memory Size: 128 MB
 * Network Configuration
  * Ethernet0:
   * Enabled: checked
   * Connection Type: Bridged
   * VirtualDevice Intel(R) Pro/1000
  * Ethernet1:
   * Enabled: checked
   * Connection Type: Bridged
   * VirtualDevice Intel(R) Pro/1000
 * Disk Configuration
  * SCSI: Disable SCSI
  * IDE0:Master:
   * Enabled: checked
   * File Name / Floppy Device: openwrt-x86-2.6-ext2.vmdk
   * Start Connected: checked
   * WriteThru: checked
   * Autodetect Name: checked
 * Other Configuration Options
  * VMWare Tools: Don't Remind to Install VMWare Tools
  * Startup Hints: Hide Startup Hints
  * USB: Disable USB
  * LPT1: Disable LPT1
  * Soundcard: No soundcard support
  * Logging: Disable Logging

You have to make a few changes to the generated vmx file:
{{{
+serial0.fileType = "pipe"
-serial0.fileName = "COM1"
+serial0.fileName = "\\.\pipe\com_1"
+serial0.pipe.endPoint = "server"
+floppy0.present = "FALSE"
}}}

Save the file to openwrt-x86-2.6-ext2.vmx in the same folder as your VMware vmdk image file.

When you've done all that open the vmx file with VMWare Player (or simply double click on it) and have fun.

= Questions =

Please use [http://forum.openwrt.org/viewtopic.php?pid=42826 this forum thread] to get help.
