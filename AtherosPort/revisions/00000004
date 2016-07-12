[[TableOfContents]]
= Status of the Atheros 531x/231x port of OpenWrt =

== What is this stuff? ==

The AR531x and 231x is a router platform by Atheros, which is used for dual-band and single-band 108Mb/s routers, including
 * [:OpenWrtDocs/Hardware/Netgear/WGT624:Netgear WGT624] [http://www.netgear.com/products/details/WGT624.php Product link]
 * [http://www1.linksys.com/products/product.asp?grid=33&scid=35&prid=664 Linksys WRT55AG v2] (Note: v1 '''IS Broadcom based''', so this porting effort doesn't have anything to do with it.)

and many more.


== TODO ==

   * Write docs on the VxWorx bootloader
   * Port the kenrel patches to recent kernels
   * Get JTAG on the go
   * Port the ethernet driver from RedBoot to Linux
   * Get it work, tested, and later into the OpenWrt buildroot. 

== Firmware/Bootloader ==

There are at least 2 variants

 * VxWorx' own bootloader - most AR7 devices
 * RedBoot

If you managed to get serial working, you can interrupt the vxworks bootloader if you press escape just after powering up. It'll look like this (WGT624) :

{{{
ar531x rev 0x00005743 firmware startup...            
SDRAM TEST...PASSED                                  
                                                     
boardData checksum failed!

Atheros AR5001AP default version 0.0.0.225

[Boot]: help

 ?                     - print this list
 @                     - boot (load and go)
 p                     - print boot params
 c                     - change boot params
 e                     - print fatal exception
 v                     - print version
 B                     - change board data
 S                     - show board data
 n netif               - print network interface device address
 $dev(0,procnum)host:/file h=# e=# b=# g=# u=usr [pw=passwd] f=# 
                           tn=targetname s=script o=other 
 boot device: tffs=drive,removable     file name: /tffs0/vxWorks 
 Boot flags:           
   0x02  - load local system symbols 
   0x04  - don't autoboot 
   0x08  - quick autoboot (no countdown) 
   0x20  - disable login security 
   0x40  - use bootp to get boot parameters 
   0x80  - use tftp to get boot image 
   0x100 - use proxy arp 

available boot devices:Enhanced Network Devices
 et0 et1 tffs

}}}

= How to help =

If you want to help and got some basic kernel hacking knowledge, you should start by familiarizing yourself with the OpenWrt build system. It now has support for building images for non-broadcom hardware.
All the kernel and image stuff is in the target/ subdirectory.

All the sources we have for this platform is at http://downloads.openwrt.org/reference/

AR531x/231x-specific kernel patches will go into {{{target/linux/linux-2.4/patches/ar531x}}}. The build system part that constructs the firmware images for AR531x based routers will be in {{{target/linux/image/ar531x}}}.
