This !HowTo explains how to get !OpenWrt running on VMware. This only works with Kamikaze (X86 [2.6]), the old stable version (!WhiteRussian) is not supported. This has been tested on a Windows XP and Linux host-system.

See also: ["RunningKamikazeOnQEMUHowTo"]

= Using prebuilt images =
 1. Download the free VMware Player (recommended and enough for most users) or Server from [http://www.vmware.com/ VMware] and install it

 1. Download a [http://downloads.openwrt.org/kamikaze/7.06/x86-2.6/openwrt-x86-2.6-ext2.image precompiled Kamikaze for x86-2.6] and create a VMware image from it (you need ''qemu-img'' (part of the [http://packages.debian.org/qemu qemu package] on Debian and Ubuntu): {{{qemu-img convert -f raw openwrt-x86-2.6-ext2.image -O vmdk openwrt-x86-2.6-ext2.vmdk}}} (You can also get the resulting file from [http://www2.informatik.hu-berlin.de/~nachtiga/openwrt/openwrt-x86-2.6-ext2.vmdk openwrt-x86-2.6-ext2.vmdk (4.3MB)] or zipped version at [http://www2.informatik.hu-berlin.de/~nachtiga/openwrt/openwrt-x86-2.6-ext2_VMware-image.zip openwrt-x86-2.6-ext2_VMware-image.zip (1.8MB)])
 1. Get the VMware configuration file from [http://www2.informatik.hu-berlin.de/~nachtiga/openwrt/openwrt-x86-2.6-ext2.vmx here] and store it in the same directory as the vmdk image.
 1. Open the vmx file with VMWare Player (or simply double click on it)
You can access via VMware, or via serial: On a Windows host-system the virtual serial console is accessible e.g. using PuTTY connected to \\.\pipe\com_1 @ 115200 8n1 (N.B.: I do not know if the baud rate of 115200 is still correct). You can also ssh to openwrt (run 'passwd' beforehand in the vmware, Usually you need to run "udhcpc -i eth0" to get an IP from your local network)

The 8.09 Kamikaze builds don't include the kmod-e1000 package which results in booting without the eth0 and eth1 interfaces (some versions of VMWare use the kmod-pcnet32 module, also not installed).  You can build your own image to include it or you can create a second hard disk image with the additional packages you wish to install:

 1. Create a blank hard disk image: {{{dd if=/dev/zero of=disk.img bs=1M count=1}}} (creates a 1 'M'egabyte image)
 1. Make a filesystem in the image: {{{mkfs.ext2 disk.img}}}
 1. Make a temporary mount point: {{{mkdir mnt.img}}}
 1. Mount the image: {{{mount -o loop -t ext2 disk.img mnt.img}}}
 1. [http://downloads.openwrt.org/kamikaze/8.09_RC2/x86/packages/kmod-e1000_2.6.25.17-x86-1_i386.ipk Download] and copy the packages you want into the image: {{{cp kmod-e1000_xxxx.ipk mnt.img/}}}
 1. Un-mount the image: {{{umount mnt.img}}}
 1. Convert the image to VMDK format: {{{qemu-img convert -f raw disk.img -O vmdk disk.vmdk}}}
 1. Add the following the .vmx file:
   {{{ide0:1.fileName = "disk.vmdk"
ide0:1.deviceType = "disk"
ide0:1.mode = "persistent"
ide0:1.redo = ""
ide0:1.startConnected = "TRUE"
ide0:1.writeThrough = "TRUE"
ide0:1.autodetect = "TRUE"}}}
 1. Boot the VM.
 1. Login via the console.
 1. Mount the new disk: {{{mkdir /mnt/hdb && mount -t ext2 /dev/hdb /mnt/hdb}}}
 1. Install the package: {{{opkg install /dev/hdb/kmod-e1000_xxxx.ipkg}}}

= Doing it yourself =
== Building your own image ==
To build your own Kamikaze VMware image you need a !OpenWrt development environment (with ''qemu-img'' (part of the [http://packages.debian.org/qemu qemu package] on Debian and Ubuntu) installed on the Linux host-system to convert the image):

 1. check out with 'svn co https://svn.openwrt.org/openwrt/trunk/' (or download the [http://downloads.openwrt.org/kamikaze/7.06/kamikaze_7.06.tar.bz2 stable kamikaze 7.06 release])

 1. After applying the patches run 'make menuconfig' and select:
  * Target System (x86 [2.6])
  * Target Profile (VMware image)
  * Target Images
   * [ ] jffs2 <-- N
   * [ ] squashfs <-- N
   * (115200) Serial port baud rate
   * (128) Filesystem part size (in MB)
  * Kernel Modules
   * Network Devices
    * kmod-e1000   (the vmware network interfaces need this)
 1. run 'make' to build the x86 image (which ends up in {{{bin/openwrt-x86-2.6-ext2.image}}})
 1. {{{qemu-img convert -f raw openwrt-x86-2.6-ext2.image -O vmdk openwrt-x86-2.6-ext2.vmdk}}}  (you need ''qemu-img'' (part of the [http://packages.debian.org/qemu qemu package] on Debian and Ubuntu)
== Creating the VMware configuration file ==
The openwrt-x86-2.6-ext2.vmx file can also simply be downloaded from above. Anyway, it was creating at http://www.easyvmx.com with the following settings:

 * Basic Configuration
  * Virtual Machine Name: !OpenWrt Kamikaze (x86-2.6)
  * Select GuestOS: Generic Linux 2.6.x
  * Memory Size: 128 MB
 * Network Configuration
  * Ethernet0:
   * Enabled: checked
   * Connection Type: Bridged
   * !VirtualDevice Intel(R) Pro/1000
  * Ethernet1:
   * Enabled: checked
   * Connection Type: Bridged
   * !VirtualDevice Intel(R) Pro/1000
 * Disk Configuration
  * SCSI: Disable SCSI
  * IDE0:Master:
   * Enabled: checked
   * File Name / Floppy Device: openwrt-x86-2.6-ext2.vmdk
   * Start Connected: checked
   * !WriteThru: checked
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
