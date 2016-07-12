'''How the OpenWRT system boots and notes on the configuration files used'''

= Introduction =
There is not much documentation on how the OpenWRT system starts, so I'm putting my notes here in case someone else wants to try to customize the boot sequence as well.

== NOTE ==
These are my notes on the boot sequence - they are just observations that I've made. Hopefully, they will help you as well.

These notes are based on the default Kamikaze boot sequence from the ext2 image

Partition layout for the ext2 image is:

 * /dev/hda1 - Boot partition
   * /boot/vmlinuz - kernel
   * /boot/grub - directory for grub bootloader

 * /dev/hda2 - OpennWRT system files

= Cliff Notes boot sequence =

 * boot loader starts the kernel with "init=..." option (default is "/etc/preinit")
 * preinit does pre-initialization setups (create directories, mount fs, /proc, /sys, ... )
 * If "INITRAMFS" is not defined, calls /sbin/init (the mother of all processes)
 * init reads /etc/inittab for the "sysinit" entry (default is "::sysinit:/etc/init.d/rcS S boot")
 * init calls "/etc/init.d/rcS S boot"
 * rcS executes the startup scripts located in /etc/rc.d/S##xxxxxx with options "S" and "start"
   * Script names follow the SysVInit format ( similar to RedHat(tm) )
 * After rcS finishes, system should be up and running
 * On a shutdown command, init reads /etc/inittab for shutdown (default is "::shutdodwn:/etc/init.d/rcS K stop")
 * init calls "/etc/init.d/rcS K stop"
 * rcS executes the shutdown scripts located in /etc/rc.d/K##xxxxxx with options "K" and "stop"
 * system halts/reboots

= Detailed boot sequence =
== Boot loader ==
The first program called after the kernel loads is located at the kernel options entry of the boot loader. For grub, the entry is located in the openwrt-<cpu>-<filesystem>.image.kernel image in the /boot/grub/menu.lst file.

Example from the openwrt-x86-ext2-image.kernel file entry for normal boot:
  "kernel  /boot/vmlinuz root=/dev/hda2 init=/etc/preinit <rest of options>"

In this example, the entry "init=/etc/preinit" tells the kernel that the first program to run after initializing is  "preinit" found in the "/etc" directory located on the disk "/dev/hda" and partition "hda2".
