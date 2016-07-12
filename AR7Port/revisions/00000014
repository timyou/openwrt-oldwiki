[[TableOfContents]]
= Status of the AR7 port of OpenWrt =

== What is this AR7 stuff? ==

AR7 is a router platform by Texas Instruments, which is used for routers and ADSL gateways, including 
 * [http://www.seattlewireless.net/index.cgi/ActiontecGT701 Actiontec GT-701]
 * [http://www.wehavemorefun.de/fritzbox/ AVM Fritz!Box] (German language)
 * [http://www.seattlewireless.net/index.cgi/DlinkDslG604t D-Link DSL-G604T]
 * Linksys WAG54G v2 (Note: v1 '''DOES NOT''' run Linux and is therefor unsupported)
 * Linksys ADSL2MUE
 * Linksys WRTP54G
 * Netcomm NB5
 * [http://www.seattlewireless.net/index.cgi/NetgearDG834G Netgear DG834G]
 * Siemens [http://bs.netgaroo.com/sx541/ SX541] (uses realtime OS (SOHO.BIN) and BRN Boot Loader from the Broad Net Technology, Inc.)
  
and many more.

http://www.linux-mips.org/wiki/AR7

== Finished tasks ==

Our Kernel support for AR7 is in CVS HEAD and disabled by default.
Here's what we have integrated so far:

   * A kernel that boots up to the part where it tries to mount the root filesystem
   * A simple mtd flash map driver that uses the boot loader's partition map
   * Running a shell with a modified OpenWrt rootfs works!
   * We have working (and free) drivers for Ethernet and ADSL in CVS!
   * '''NEW:''' The flash map driver is working, but needs more testing
   * '''NEW:''' We have the source for the TI WLAN driver

== TODO ==

   * Make Oleg's LZMA loader work
   * Port open source drivers from the vendors' GPL releases (avalanche_vmac, vlynq, etc.)
   * Fix the wireless driver

== Firmware/Bootloader ==

There are at least 3 variants

 * Telogy Networks, Inc ["ADAM2"] + Linux
 * TI PSP bootloader + Linux
 * Broad Net Technology, Inc. BRN bootloader and realtime OS (SOHO.BIN)

There are also at least two variants of ADAM2. My version (0.22.06) allows flashing of each mtdblock by ftp, others have reported they must flash a complete image via '''t'''ftp

There are two ADAM2 environment controlling boot process:

 * autoload = 0|1
 * autoload_timeout = N sec.

== Some ideas on the mtd flash map driver ==

To make the flash partitioning as flexible as it is in the Broadcom stuff, I'd like to use TRX for it, too.
Because the boot loader ADAM2 doesn't support TRX, we need to leave the kernel out of it.
The firmware image could be constructed like this:

> [ kernel + loader ] [ padding to blocksize - trx header size ] [ filesystem in .trx container ]

That way the kernel can walk through the flash blocks and look for a trx header at the end. It should be put at the end of the block, so that the jffs2 part is aligned properly. 
Then we need an implementation of jffs2root in the kernel, which (if JFFS2 is detected) erases everything outside of the TRX in the data partition that ADAM2 provides and extends the TRX partition to the full size.

= How to help =

If you want to help and got some basic kernel hacking knowledge, you should start by familiarizing yourself with the OpenWrt build system. It now has support for building images for non-broadcom hardware. 
All the kernel and image stuff is in the target/ subdirectory.

AR7-specific kernel patches go into {{{target/linux/linux-2.4/patches/ar7}}}. The build system part that constructs the firmware images for AR7 based routers is in {{{target/linux/image/ar7}}}. You can also find the kernel loader there.

If you'd like to help out and maybe have a patch or two, please talk to one of the developers working on this via IRC in the OpenWrt channel. Some people working on this are: nbd, wbx, wickus, z3ro.


= Other stuff =


=== WAG54G Serial Console ===

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
