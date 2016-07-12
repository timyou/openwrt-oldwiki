[[TableOfContents]]
= Status of the AR7 port of OpenWrt =

== What is this AR7 stuff? ==

AR7 is a router platform by Texas Instruments, which is used for routers and ADSL gateways, including
 * [http://www.seattlewireless.net/index.cgi/ActiontecGT701 Actiontec GT-701]
 * [http://www.wehavemorefun.de/fritzbox/ AVM Fritz!Box] (German language)
 * [http://www.seattlewireless.net/index.cgi/DlinkDslG604t D-Link DSL-G604T] (and DSL-G664T)
 * Linksys WAG54G v2 (Note: v1 '''DOES NOT''' run Linux and is therefor unsupported)
 * Linksys ADSL2MUE
 * Linksys WRTP54G
 * Netcomm NB5
 * [http://www.seattlewireless.net/index.cgi/NetgearDG834G Netgear DG834G]
 * Siemens [http://bs.netgaroo.com/sx541/ SX541] (uses realtime OS (SOHO.BIN) and BRN Boot Loader from the Broad Net Technology, Inc.)
 * Sitecom [http://www.trasduzione.com/WL-108 WL-108]

and many more.

http://www.linux-mips.org/wiki/AR7

See [:OpenWrtDocs/InstallingAR7] if you are brave enough to test it.

== Finished tasks ==

Our Kernel support for AR7 is in CVS HEAD and disabled by default.
Here's what we have integrated so far:

   * A kernel that boots up to the part where it tries to mount the root filesystem
   * A simple mtd flash map driver that uses the boot loader's partition map
   * Running a shell with a modified OpenWrt rootfs works!
   * We have working (and free) drivers for Ethernet and ADSL in CVS!
   * The flash map driver is working, but needs more testing
   * We have the source for the TI WLAN driver
   * With the new stuff in CVS, it now sets up the networking stuff, so you can log in via telnet on 192.168.1.1 (or whatever you configured in menuconfig). That can be changed in /etc/config/network
   * The VLYNQ bus seems to work
   * The LZMA loader works and is integrated
   * '''NEW:''' ADSL seems to work, needs testing...
   * '''NEW:''' Support for WAG354G is integrated, needs testing...

== Bugs / Ugly-Hacks ==

I would like to keep a list of the bugs and ugly-hacks used to make the ar7 work, so that they can be removed.

   * '''arch/mips/ar7/printf.c''': not inline with the generic '''arch/mips/mips-boards/generic/printf.c''', and requires '''arch/mips/lib/promlib.c''' to have an #ifndef CONFIG_AR7 around the entire file.
   * '''arch/mips/lib/promlib.c''': see above.
   * '''arch/mips/ar7/irq.c''': not inline with the generic irc.c files for any of the other platforms under arch/mips, this still uses the (very) old way of dealing with irq's - not the new, standard way.
   * '''arch/mips/ar7/reset.c''': the functions are empty. Please impliment this '''without''' using the tnetd code, if possible. (reboot works now, shutdown/halt does not yet.) -- nbd: for halt, you probably only need __cli() + while(1);
   * '''arch/mips/kernel/traps.c''', '''arch/mips/mm/tlb-r4k.c''': a lot of "KSEG0+CONFIG_AR7_MEMORY" we might need to keep this, the ar7 has a small ammount of ram/rom on-chip where the exception code goes... strange that it loads the generic linux exception code, as well as the ar7 exception code in arch/mips/ar7.
   * '''arch/mips/kernel/setup.c''': the bootmap_size for ar7 needs fixing, and I killed all of arch/mips/ar7/ar7_paging.c (it's now merged with setup.c and is a lot more compact.) (note: this is in my latest patch at http://z3ro.geek.nz/ar7/2005-07-28 which is not merged into the openwrt buildroot yet.)
   * '''arch/mips/mm/init.c''': see above, this has changes related to the old ar7_paging.c file, some of which can probably be removed now that we use the "proper" bootmem code in setup.c (I'll do this next)

   * Please document any more bugs/ugly-hacks found.

== TODO ==

   * Complete the init scripts, remove nvram dependencies
   * Test ADSL driver
   * Fix the wireless driver

== Firmware/Bootloader ==

There are at least 3 variants

 * Telogy Networks, Inc ["ADAM2"] + Linux
 * TI PSP bootloader ["PSPBoot"] + Linux
 * Broad Net Technology, Inc. BRN bootloader and realtime OS (SOHO.BIN)

There are also at least two variants of ADAM2. My version (0.22.06) allows flashing of each mtdblock by ftp, others have reported they must flash a complete image via '''t'''ftp
TFTP is probably specific to CyberTAN-based stuff (almost exclusively Linksys). All other vendors seem to use FTP

There are two ADAM2 environment controlling boot process:

 * autoload = 0|1
 * autoload_timeout = N sec.


= How to help =

If you want to help and got some basic kernel hacking knowledge, you should start by familiarizing yourself with the OpenWrt build system. It now has support for building images for non-broadcom hardware.
All the kernel and image stuff is in the target/ subdirectory.

AR7-specific kernel patches go into {{{target/linux/linux-2.4/patches/ar7}}}. The build system part that constructs the firmware images for AR7 based routers is in {{{target/linux/image/ar7}}}. You can also find the kernel loader there.

If you'd like to help out and maybe have a patch or two, please talk to one of the developers working on this via IRC in the OpenWrt channel. Some people working on this are: nbd, wbx, wickus, z3ro.


= Other stuff =


== WAG54G Serial Console ==

{{{
|
|    __
|   |  |        <--- Pin 1: GND
|    --
|   |  |        <--- Pin 2: Not Connected
|    --
|   |  |        <--- Pin 3: Router's Serial RX
|    --
|   |  |        <--- Pin 4: Router's Serial TX
|    --
|   |  |        <--- Pin 5: VCC
|    --
|
|
 \__led__led__led__led____________________
                Front of WAG54G
}}}


The method used to find the serial port was suggested to me on irc; use a piezo buzzer and attach it's ground (usually black) wire to a ground point on the router - the back of the power regulators are usually good candidates, but check this with a multimeter/voltmeter... Use the other wire to probe any of the header pins which may be pre-installed, or any of the component holes which look like they could have header pins installed into. Once you get the right pin, the piezo should make a screeching sound much like that of a 56kbps connection.

Make sure you reset the router after probing each pin. The bootloader/linux bootup messages will only happen for a few seconds, after that the serial console will be silent - so even if you have the right pin you will not hear anything.

A more accurate method would be to use either a logic analyzer or an oscilloscope, but these are expensive and for the basic task of locating a serial pin a little overkill. ;)
