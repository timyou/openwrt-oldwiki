[[TableOfContents]]

== Hardware ==

This unit is based on a Broadcom BCM5354 core, with a BCM3302 V2.9 CPU.  Detailed specs are available [http://mightyohm.com/blog/2008/10/detailed-specs-for-the-asus-wl-520gu-uber-hacking-platform/ here].  Note that the hardware is similar to that of the WL500GPV2, and the information there is relevant to this unit too.

== Flashing ==

The {{{boot_wait}}} nvram variable is set by default, but a special procedure is required for uploading a new flash via tftp at boot.  Beginning with the router powered off, press and hold the reset button while powering the router on.  Release the reset button when the power led begins to slowly blink on and off.  The router will now be in Firmware Restoration Mode, and it can be flashed with a new firmware at your leisure.  This is a good router to experiment with OpenWrt, since it is very easy to recover from a bad flash; if the bootloader doesn't like the firmware, the router may automatically enters Firmware Restoration Mode, and it can apparently always be forced into Firmware Recovery Mode via the reset button.  See [http://www.dd-wrt.com/wiki/index.php/Asus_WL-520GU] for more information.

-----

The router's firmware upgrade page wouldn't accept my OpenWrt firmwares, but I was able to flash it via tftp by first putting it into Firmware Restoration Mode via the above procedure, and then [http://wiki.openwrt.org/OpenWrtDocs/Installing/TFTP flashing via tftp].  Note that the router will apparently not reboot automatically when flashed while in Firmware Restoration Mode; I had to power cycle the router to activate OpenWrt.

== 2.6 Kernels ==

Booting images with 2.4 kernels on this unit is straightforward, but booting 2.6 based images is quite tricky and a WIP:
 * http://forum.openwrt.org/viewtopic.php?pid=75486
 * http://forum.openwrt.org/viewtopic.php?id=17117
 * http://forum.openwrt.org/viewtopic.php?pid=67164
 * http://forum.openwrt.org/viewtopic.php?id=15443
I did eventually manage to get a 2.6 image running (r13270), although without wireless.  Here is the procedure I used, based on the last of the above threads and the instructions at WL500GPV2:
 1. Configure:
  1. Select the Broadcom BCM947xx/953xx [2.6] target system
  1. Select the No Wifi target profile
  1. Make sure that {{{kmod-b43}}} is ''not'' configured
 1. Make
 1. Edit {{{$BUILD_ROOT/build_dir/linux-brcm47xx/linux-2.6.xx.x/arch/mips/bcm47xx/prom.c}}}, and comment out the calls toward the end to {{{prom_init_cfe}}}, {{{prom_init_console_cfe}}} and {{{prom_init_cmdline_cfe}}} as per [http://forum.openwrt.org/viewtopic.php?pid=69645#p69645 sbrown's patch].
 1. Edit {{{$BUILD_ROOT/build_dir/linux-brcm47xx/linux-2.6.xx.x/arch/mips/kernel/setup.c}}} and comment out the calls toward the end to {{{setup_early_printk}}} as per the above patch.
 1. Make (again)

The {{{.trx}}} image in {{{$BUILD_ROOT/bin}}} can now be flashed to the router.

== B43 ==

The open source b43 driver does not yet support the unit's wireless chipset, which contains an LP PHY.

== USB Storage ==

To attach a USB storage device, configure the following, under Kernel Modules:

 * Under USB Support:
  * kmod-usb-core
  * kmod-usb-ohci
  * kmod-usb-storage
 * Under Filesystems
  * Whatever filesystems you plan to use

See UsbStorageHowto for more information.

== Miscellaneous Reports ==

My steps were to do a {{{make menuconfig}}} to set the target to 'wl500g' and make sure kmod-usb-ohci was enabled for usb support. I would stay away from the USB 2.0 drivers. Many people have been having stability problems with the 2.0 drivers despite the blue text mentioning USB 2.0 support. Even ASUS keeps USB 2.0 disabled in their kernel .config.

I was also able to mount a USB flash drive after recompiling with USB storage support (kmod-usb-storage) and vfat filesystem support.

If you want a web interface (x-wrt), try updating the packages and enabling "webif" during a {{{make menuconfig}}}. It worked for me.

-----

Tomato 1.17 ND.trx works for this model. But there's no USB.

-----

using the stock ASUS firmware, you can get a limited shell through the net interface of the router at http://192.168.1.1/Main_AdmStatus_Content.asp by copying the netcat mipsel binary to the root of a USB stick and then entering "/tmp/harddisk/part1/nc -l -p 31337 -e /bin/sh" and then returning to your usual computer already equipped with nc and entering "nc 192.168.1.1 31337" neat, but almost completely useless unless the only reason you are looking at openwrt is to support one or two additional programs that won't automatically run as services :(

I was informed that the "trunk" release of kamikaze supports the BCM5354, so I tried it. After brute forcing some things that may have been related only to my configuration choices (iptables forwarding was broken for me but easily 'fixed'), it works!

...unless you are comfortable with compiling a kernel, this is not the USB-enabled OpenWRT router for you. Not quite yet.

But if you are comfortable compiling a kernel, then it's a very nice 4/16MB router with USB support, if I do say so myself!!

USB ohci as well as ehci-hcd 2.0 drivers are working just fine with vfat using openwrt. Crash. the 2.0 drivers that is. When sending or reading data to any filesystem at the faster speed, a reboot can occur.

on the WL-520U ** DO NOT USE THE USB STICK WITH 2.0 DRIVERS TO LOAD NEW KERNELS ** I did, and during the process the router rebooted. I'm very, very lucky to have recovered and re-flashed it. Since that time I have verified that transferring large amounts of data to or from the memory stick reboots the router when using EHCI-HCD USB.

Even ASUS does not build the 2.0 driver, as proven by their .config. If anybody wants to have fun with a truth-in-advertising lawsuit, point out to ASUS that they advertise a USB 2.0 Controller on the WL-520GU, but that it is only running a 1.1 (OHCI) driver :P

The USB 2.0 part is written in blue on the specs, either because printing specifications in blue has a special meaning to ASUS, or because they actually wanted to draw attention to the fact that they are lying. Look out for future blue text on ASUS specifications!

this is why it's cheap, I guess.

So indeed, ohci is all that can be expected to work longer than an hour at the moment.

Still testing, now with the USB 1.1 Mass storage...

...still a WIP

-----
 . I just noticed on the dd-wrt forum a comment referring to a USB fix.  I have not investigated (I don't have one of these routers). http://www.dd-wrt.com/phpBB2/viewtopic.php?t=38777&postdays=0&postorder=asc&highlight=wl520gu&start=18  and  http://www.dd-wrt.com/phpBB2/viewtopic.php?p=215724&sid=e021ff65c0a8f249b6a73a61398b04b6#215724
 

-----

This router is being used to build a Wifi Radio at http://mightyohm.com


An article on installing OpenWrt (including compiled image and package files) is here:
http://mightyohm.com/blog/2008/11/building-a-wifi-radio-part-4-installing-openwrt/


The build is based on Kamikaze 7.09 trunk r12857 and the linux-2.4 kernel.  This build is very stable.  No issues have been reported with USB OHCI mode or the wireless support.  The same image can be used on the WL-500gP v2 without modification.

There is also an article on installing a serial port on this router here:
http://mightyohm.com/blog/2008/10/building-a-wifi-radio-part-3-hacking-the-asus-wl-520gu/

----
 . CategoryModel
