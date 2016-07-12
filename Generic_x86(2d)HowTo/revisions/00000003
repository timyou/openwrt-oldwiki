## Please edit system and help pages ONLY in the moinmaster wiki! For more
## information, please see MoinMaster:MoinPagesEditorGroup.
##acl MoinPagesEditorGroup:read,write,delete,revert All:read
##master-page:HelpTemplate
##master-date:Unknown-Date
#format wiki
#language en
== Running OpenWRT on any x86 machine ==
WARNING: If you are not familiar with configuring the linux kernel to work on specific hardware, you should not be attempting this.

The purpose of this HowTo is mostly focused around making OpenWRT use a vga console instead of a serial console.  It is assumed you will know how to select other necessary kernel modules for your specific hardware.  Network cards will most likely be the first hardware you will have to add to get it to work on your particular hardware.

This HowTo was developed using Kamikaze revision 6435.  Unless support for Generic x86 hardware is added to OpenWRT this information will undoubtedly become stale.

=== Getting started: ===
The Soekris port is almost enough to get OpenWRT running on any x86 machine.  Follow the Soekris page to get started:SoekrisPort

Once you have built OpenWRT for the Soekris you can proceed to modify it for your hardware.

=== Files to modify: ===
 * trunk/target/linux/x86-2.6/config/default
 * trunk/target/linux/x86-2.6/image/grub/menu.lst
 * trunk/package/base-files/etc/inittab
=== Kernel config changes: ===
At the minimum you will need to add the following lines to'''trunk/target/linux/x86-2.6/config/default:'''

{{{
#
# Console display driver support
#
CONFIG_VGA_CONSOLE=y
# CONFIG_VGACON_SOFT_SCROLLBACK is not set
CONFIG_VIDEO_SELECT=y
CONFIG_MDA_CONSOLE=m
CONFIG_DUMMY_CONSOLE=y
CONFIG_FRAMEBUFFER_CONSOLE=y
# CONFIG_FRAMEBUFFER_CONSOLE_ROTATION is not set
# CONFIG_FONTS is not set
CONFIG_FONT_8x8=y
CONFIG_FONT_8x16=y
# CONFIG_BT_HIDP is not set
CONFIG_INPUT=y
# CONFIG_INPUT_FF_MEMLESS is not set
#
# Userland interfaces
#
# CONFIG_INPUT_MOUSEDEV is not set
# CONFIG_INPUT_JOYDEV is not set
# CONFIG_INPUT_TSDEV is not set
# CONFIG_INPUT_EVDEV is not set
# CONFIG_INPUT_EVBUG is not set
#
# Input Device Drivers
#
CONFIG_INPUT_KEYBOARD=y
CONFIG_KEYBOARD_ATKBD=y
# CONFIG_KEYBOARD_SUNKBD is not set
# CONFIG_KEYBOARD_LKKBD is not set
# CONFIG_KEYBOARD_XTKBD is not set
# CONFIG_KEYBOARD_NEWTON is not set
# CONFIG_KEYBOARD_STOWAWAY is not set
# CONFIG_INPUT_MOUSE is not set
# CONFIG_INPUT_JOYSTICK is not set
# CONFIG_INPUT_TOUCHSCREEN is not set
# CONFIG_INPUT_MISC is not set
CONFIG_SERIO=y
CONFIG_SERIO_I8042=y
CONFIG_SERIO_SERPORT=y
# CONFIG_SERIO_CT82C710 is not set
# CONFIG_SERIO_PCIPS2 is not set
CONFIG_SERIO_LIBPS2=y
# CONFIG_SERIO_RAW is not set
# CONFIG_SONYPI is not set
# CONFIG_USB_KBD is not set
# CONFIG_USB_MOUSE is not set
# CONFIG_USB_AIPTEK is not set
# CONFIG_USB_WACOM is not set
# CONFIG_USB_ACECAD is not set
# CONFIG_USB_KBTAB is not set
# CONFIG_USB_POWERMATE is not set
# CONFIG_USB_TOUCHSCREEN is not set
# CONFIG_USB_YEALINK is not set
# CONFIG_USB_XPAD is not set
# CONFIG_USB_ATI_REMOTE is not set
# CONFIG_USB_ATI_REMOTE2 is not set
# CONFIG_USB_KEYSPAN_REMOTE is not set
# CONFIG_USB_APPLETOUCH is not set
CONFIG_VT=y
CONFIG_VT_CONSOLE=y
CONFIG_HW_CONSOLE=y
# CONFIG_VT_HW_CONSOLE_BINDING is not set
#
# Console display driver support
#
CONFIG_VGA_CONSOLE=y
# CONFIG_VGACON_SOFT_SCROLLBACK is not set
# CONFIG_VIDEO_SELECT is not set
# CONFIG_MDA_CONSOLE is not set
CONFIG_DUMMY_CONSOLE=y
}}}
This will enable the keyboard and vga console in the linux kernel.

You still need to make OpenWRT use the vga console.  In order to do this you need to modify two other files:

 * trunk/target/linux/x86-2.6/image/grub/menu.lst
Comment out the first two lines that put the grub menu on the serial console and remove the console kernel parameter on the "kernel" line:

{{{
#serial --unit=0 --speed=@BAUDRATE@ --word=8 --parity=no --stop=1
#terminal --timeout=10 serial
default 0
timeout 5
title   OpenWrt
root    (hd0,0)
kernel  /boot/vmlinuz @CMDLINE@ noinitrd reboot=bios
boot
 }}}
 * trunk/package/base-files/etc/inittab
Busybox's init will use the console the kernel finds by removing the device from the "askfirst" line:

{{{
::askfirst:/bin/ash --login}}}
=== Additional work: ===
==== Other hardware modules: ====
If your x86 machine uses network adapters other than those natively built with OpenWRT you will have to add them to the default kernel config.  The easiest way that I know of doing this is by first building OpenWRT and then working in the'''trunk/build_i386/linux'''directory.

 1. Make a backup copy of '''.config''' and run '''make menuconfig''' while in the '''trunk/build_i386/linux '''directory.
 1. Select your new kernel modules and save the kernel config.
 1. Do a diff between '''.config''' and the backup of the previous version
 1. Add the changes back to '''trunk/target/linux/x86-2.6/config/default'''
(I personally have been using the four port ethernet adapter from Soekris and have not had to add any additional modules, so if these steps are incomplete please correct this page.)

==== Fix the network config: ====
Once you have OpenWRT booting and running on your x86 hardware you will need to modify '''/etc/config/network''' to suit your hardware.

==== Kernel optimizations: ====
By default the x86 build for OpenWRT is optimized only for 486 processors.  Additional speed will undoubtedly be had by selecting kernel optimizations specific to your processors.  However, I have my doubts that building a 64 bit kernel will be usable without making other changes to buildroot system.
