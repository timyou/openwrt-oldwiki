'''How the OpenWRT system boots and notes on the configuration files used'''

= Introduction =
There is not much documentation on how the OpenWRT system starts, so I'm putting my notes here in case someone else wants to try to customize the boot sequence as well.

== NOTE ==
These are my notes on the boot sequence - they are just observations that I've made. Hopefully, they will help you as well.

These notes are based on the default Kamikaze boot sequence from the ext2 image

Partition layout for the ext2 image is:

 * '''/dev/hda1''' - Boot partition
   * '''/boot/vmlinuz''' - The linux kernel
   * '''/boot/grub''' - directory for grub bootloader

 * '''/dev/hda2''' - OpenWRT system files

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
After the bootloader (grub, in this example) initializes and parses any options that are presented at the boot menu, the bootloader loads the kernel.

Example from the openwrt-x86-ext2-image.kernel file entry for normal boot:
  "kernel  /boot/vmlinuz root=/dev/hda2 init=/etc/preinit <rest of options>"

This entry in the boot/grub/menu.lst file tells grub that the kernel is located under the /boot directory and the filename is vmlinuz. The rest of the lines are the options that are passed to the kernel. To see how the kernel was started, you can view the options by reading the /proc/cmdline file. You can see what options were passed from grub by logging into the device and typing "cat /proc/cmdline".

For my test system, the options that were passed to the kernel at load time was:
  "root=/dev/hda2 rootfstype=ext2 init=/etc/preinit  noinitrd console=ttyS0,38400,n,8,1 reboot=bios"

The options are:
 A. '''root''': root device/partition where the rest of the OpenWRT system is located
 A. '''rootfstype''': Format for the root partition - ext2 in this example
 A. '''init''': The first program to call after the kernel is loaded and initialized
 A. '''noinitrd''': All drivers for access to the rest of the system are built into the kernel, so no need to load an initial ramdisk with extra drivers
 A. '''console''': Which device to accept console login commands from - talk to ttyS0 (first serial port) at 38400 speed using no flow control, eight data bits and one stop bit. See the kernel documentation for other options
 A. '''reboot''': Not sure, but I believe that this option tells the kernel how to perform a reboot

The first program called after the kernel loads is located at the kernel options entry of the boot loader. For grub, the entry is located in the openwrt-<cpu>-<filesystem>.image.kernel image in the /boot/grub/menu.lst file.

In this example, the entry "init=/etc/preinit" tells the kernel that the first program to run after initializing is  "preinit" found in the "/etc" directory located on the disk "/dev/hda" and partition "hda2".

== /etc/preinit script ==
The preinit script's primary purpose is initial checks and setups for the rest of the startup scripts. One primary job is to mount the /proc and /sys pseudo filesystems so access to status information and some control functions are made available. Another primary function is to prepare the /dev directory for access to things like console, tty, and media access devices. The final job of preinit is to start the init daemon process itself.

== Busybox init ==
Init is considered the "Mother Of All Processes" since it controls things like starting daemons, changing runlevels, setting up the console/pseudo-consoles/tty access daemons, as well as some other housekeeping chores.

Once init is started, it reads the /etc/inittab configuration file to tell it what process to start, monitor for certain activities, and when an activity is triggered to call the relevant program.

The init program used by busybox is a minimalistic daemon. It does not have the knowledge of runlevels and such, so the config file is somewhat abbreviated from the normal init config file. If you are running a full linux desktop, you can "man inittab" and read about the normal init process and entries. Fields are separated by a colon and are defined as:

 [ID] : [Runlevel(s)] : [Action] : [Process to execute ]

For purposes of busybox init, the only fields needed are the "ID" (1st), "Action" (3rd) and "Process" (4th) entries. Busybox init has several caveats from a normal init: the ID field is used for controlling TTY/Console, and there are no defined runlevels. A minimalistic /etc/inittab would look like:

  1. ::sysinit:/etc/init.d/rcS S boot
  1. ::shutdown:/etc/init.d/rcS K stop
  1. tts/0::askfirst:/bin/ash --login
  1. ttyS0::askfirst:/bin/ash --login
  1. tty1::askfirst:/bin/ash --login

Lines 1 and 2 with a blank ID field indicate they are not specific to any terminal or console. The other lines are directed to specific terminals/consoles.

Notice that both the "sysinit" and "shutdown" actions are calling the same program (the "/etc/init.d/rcS" script). The only difference is the options that are passed to the rcS script. This will become clearer later on.

At this point, init has parsed the configuration file and is looking for what to do next. So, now we get to the "sysinit" entry: call /etc/init.d/rcS with the options "S" and "boot"

== /etc/rc.d/rcS Script At Startup ==
At this point, all basic setup has been done, all programs and system/configuration files are accessible, and we are now ready to start the rest of the processes.

The rcS script is pretty simplistic in it's function - it's sole purpose is to execute all of the scripts in the /etc/rc.d directory with the appropriate options. if you paid attention to the sysinit entry, the rcS script was called with the "S" and "boot" options. Since we called rcS with 2 options ("S" and "boot"), the rcS script will substitute $1 with "S" and $2 with "boot". The relevant lines in rcS are:
 * for i in /etc/rc.d/$1*; do
 *   [ -x $i ] && $i $2
 * done

The basic breakdown is:
 1. Execute the following line once for every entry (file/link) in the /etc/rc.d directory that begins with "S"
 1. If the file is executable, execute the file with the option "boot"
 1. Repeat at step 1, replacing $i with the next filename until there are no more files to check

Unlike Microsoft programs, Linux uses file permissions rather than filename extensions to tell it if this entry is executable or not. For an explanation of file permissions, see "man chmod" on a Linux/Unix machine on explanations for permissions and executable files.

== Startup/Shutdown Scripts Hilights ==
A basic description of the startup/shutdown scripts directories are /etc/init.d contains the actual scripts, and /etc/rc.d contains a link to the file in /etc/init.d but the name includes either an "S" for "START", or "K" for "KILL", followed by a sequence number, then the rest of the script name.

The format of the script name is "X##nnnn" where:
 * X = either "S" for "Start" or "K" for "Kill"
 * ## = a sequence number with a leading zero (if less than 10)
 * nnnn = the script name as found in /etc/init.d

For example - the real script /etc/init.d/network is the script that brings up/takes down network interfaces. The relevant startup link is /etc/rc.d/S40network and the shutdown link is /etc/rc.d/K40network.

If you look at the /etc/rc.d directory, you may notice that some scripts have relevant links for startup, but no shutdown (i.e., /etc/init.d/httpd), while some others have no startup script, but do have a shutdown script (i.e., /etc/init.d/umount).

In the case of httpd (the webserver), it doesn't matter if it dies or not, there's nothing to clean up before quitting.

On the other hand, the umount script MUST be executed before shutdown to ensure a clean unmounting of any relevant storage media, otherwise data corruption could occur. There's no need to call unmount at startup, since storage media mounting is handled somewhere else (like /etc/preinit), so there's no startup script for this one.

After the last startup script is executed, you should have a fully operational OpenWRT system.


----
CategoryHowTo CategoryOpenWrtPort
