= Status of the AR7 port of OpenWrt =

== What is this AR7 stuff? ==

AR7 is a router platform by Texas Instruments, which is used for routers and ADSL gateways, including 
   * AVM Fritz!Box
   * Linksys WAG54G v2
   * Linksys ADSL2MUE
   * Linksys WRTP54G
   * Netgear DG834G
   * D-Link DSL-G604T

and many more.

== Finished tasks ==

Our Kernel support for AR7 is in CVS HEAD and disabled by default.
Here's what we have integrated so far:

   * A kernel that boots up to the part where it tries to mount the root filesystem
   * A simple mtd flash map driver that uses the boot loader's partition map

== TODO ==

   * Implement a proper mtd flash map driver
   * Make Oleg's LZMA loader work
   * Port the open source drivers from the vendors' GPL releases (avalanche_cpmac, avalanche_vmac, vlynq, etc.)
   * Make the wireless interface work (either by trying the driver from http://acx100.sf.net or by making the binary blob work)
   * Make the binary-only ADSL driver work with our new Kernel

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
