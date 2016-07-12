[[TableOfContents]]
= Status of the AR7 port of OpenWrt =

== What is this AR7 stuff? ==

[http://focus.ti.com/pdfs/bcg/ar7wi_fact_sheet.pdf AR7]  is a router platform by Texas
Instruments, which is used for routers and ADSL gateways.

See the [:TableOfHardware] for supported AR7 routers.

See [:OpenWrtDocs/InstallingAR7] if you are brave enough to test it.


== Finished tasks ==

Our Kernel support for AR7 is in SVN trunk and disabled by default.
Here's what we have integrated so far:

   * A kernel that boots up to the part where it tries to mount the root filesystem
   * A simple mtd flash map driver that uses the boot loader's partition map
   * Running a shell with a modified OpenWrt rootfs works!
   * We have working (and free) drivers for Ethernet and ADSL in SVN!
   * The flash map driver is working, but needs more testing
   * We have the source for the TI WLAN driver
   * With the new stuff in SVN, it now sets up the networking stuff, so you can log in via telnet on 192.168.1.1 (or whatever you configured in menuconfig). That can be changed in /etc/config/network
   * The VLYNQ bus works
   * The LZMA loader works and is integrated
   * Support for WAG354G is integrated, still needs testing...
   * ADSL works! New init scripts for PPPoE are integrated.
   * Scripts for flashing DSL-G664T and G604T

== Bugs / Ugly-Hacks ==

I would like to keep a list of the bugs and ugly-hacks used to make the ar7 work, so that they can be removed.

   * '''arch/mips/ar7/reset.c''': the functions are empty. Please impliment this '''without''' using the tnetd code, if possible. (reboot works now, shutdown/halt does not yet.) -- nbd: for halt, you probably only need {{{ __cli() + while(1); }}} z3ro: there are some tnetd functions for halt... hopefully we can use the code from these without needing all of the tnetd code. enrik: I have some improvements for the code including a jump back to ADAM2 on halt. Will send patch soon.

   * '''arch/mips/kernel/setup.c''': We have some #ifdef CONFIG_AR7 ... #else ... #endif because of the memory offset, we should use the generics here and modify the functions in mm/bootmem.c (this will kill some #ifdef CONFIG_AR7's in other files, too.)
   * '''arch/mips/mm/init.c''': These #ifdef CONFIG_AR7's are related to not having the proper code in mm/bootmem.c, see previous list item. enrik: I have generalized the arch/mips/kernel and .../setup code to always use the more general bootmem-functions and done some initialization cleanup, too. Will send patch soon.

   * LED/pin driver is in a mess. Proc entry is named /proc/led/led instead of /proc/led_mod/led as was in original 2.4.17_mvl21-malta-mips_fp_le kernel, writing to in does nonthing, reading leads to "Unable to handle kernel paging request" exception. Entry /proc/led_mod/ar7reset, that was present in original kernel and was reading state of "reset" pin in back of device, is completely missing.

   * Please document any more bugs/ugly-hacks found.

== TODO ==

   * Complete the init scripts, remove nvram dependencies where they are still present...
   * Test WAG354G support
   * Fix the wireless driver
   * Fix VLYNQ interrupt and reset handling (needed for the wireless driver). See http://forum.openwrt.org/viewtopic.php?id=2654 for possible patches.
   * Generalize scripts/dlink.pl so that it works with other ADAM2 versions as well (like FritzBox)
   * Get voicedump (VP101X120C) supported (Voice over ip chip on Siemens and SMC based hardware)

   * Get Marvel 88E6060 switch supported (on sx541 and smc)


See also https://dev.openwrt.org/report/ (all tickets with AR7 in the summary).

== Firmware/Bootloader ==

There are at least 3 variants

 * Telogy Networks, Inc ["ADAM2"] + Linux - most Linux based AR7 devices
 * TI PSP bootloader ["PSPBoot"] + Linux - WAG354G, WRTP54G, ADSL2MUE, maybe others?
 * Broad Net Technology, Inc. BRN bootloader and VxWorks (realtime OS with SOHO.BIN) - most (all?) VxWorks based devices, e.g. Sinus 154 DSL Basic, Siemens SX 541, SMC SMC7908VoWBRB.

Note: Even on VxWorks based routers with the BRN bootloader, it is possible to install Linux and OpenWrt!
See http://forum.openwrt.org/viewtopic.php?id=2654 for more details.

There are also at least two variants of ADAM2. My version (0.22.06) allows flashing of each mtdblock by ftp, others have reported they must flash a complete image via '''t'''ftp
TFTP is probably specific to CyberTAN-based stuff (almost exclusively Linksys). All other vendors seem to use FTP

There are two ADAM2 environment controlling boot process:

 * autoload = 0|1
 * autoload_timeout = N sec.


= How to help =

If you want to help and got some basic kernel hacking knowledge, you should start by familiarizing yourself with the OpenWrt build system. It now has support for building images for non-broadcom hardware.
All the kernel and image stuff is in the target/ subdirectory.

AR7-specific kernel patches go into {{{target/linux/linux-2.4/patches/ar7}}}. The build system part that constructs the firmware images for AR7 based routers is in {{{target/linux/image/ar7}}}. You can also find the kernel loader there.

If you'd like to help out and maybe have a patch or two, please talk to one of the developers working on this via IRC in the OpenWrt channel. Some people working on this are: nbd, wbx, wickus, z3ro, ralf, mache, sw_ and ydef.


= Other stuff =
== Model-specific information ==
Mode-specific information can be found on that model's page. See ["CategoryAR7Device"].
== JTAG ==

The AR7 is based on ejtag version 2.6.

This ejtag layout should support all ar7 based boards with a 14 pin jtag pinout.  The same cable as used for the standard wrt54g (based on the xilinx III/dlc-5) as demonstrated by HairyDairyMaid can be constructed and is well documented.  Debug INT pin 13 is optional and pin 14 can be left unhooked for passive cabling.

Since DMA Routines do NOT exist for this ejtag version (compared to ejtag v2.0 supported on the wrt54g) interfacing requires a rewrite utilizng prAcc routines of the v2.6 standard.

[http://www.dlinkpedia.net/index.php/Jtag_su_30xT JTAG for D-Link DSL-30xT], [http://www.dlinkpedia.net/index.php/Interfaccia_JTAG JTAGInterface] (Italian!)
----
CategoryOpenWrtPort
