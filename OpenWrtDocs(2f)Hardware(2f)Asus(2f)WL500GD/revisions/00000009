= Asus WL-500G Deluxe =

The WL-500G Deluxe is based on the Broadcom 5365 board. It has a 200MHz CPU, 4Mb flash and 32Mb RAM (on a few older units only 16Mb is enabled by default).
The wireless NIC is integrated to the board, and it also has a VIA USB2.0 controller. boot_wait is on by default.

== Hardware overview ==

{{{
   Devices that pop up on the Silicon backplane, these are emulated as PCI devices on bus 0:

   Physical    Vendor  Core    CoreRev sbbidlow        Description
   18000000    4243    800     5       100422dd        Common core: chip 5365 rev 1
   18001000    4243    806     6       110422c5        enet mac core
   18002000    4243    80b     1       110422c5        ipsec core
   18003000    4243    808     2       110422c5        usb 1.1 host/device core
   18004000    4243    804     8       101422d5        pci core
   18005000    4243    816     1       100522c5        mips3302 core
   18006000    4243    80f     0       1000225d        memc sdram core

   Is this the same as on 0x18005000?
   40001000    4243    816     1       100522c5        mips 3302 core

   The external SB cells for the BCM4306:
   40004000    4243    812     5       110422c5        802.11 MAC core
   40005000    4243    804     9       101522d5        pci core


   Devices that pop up on the "real" PCI bus:

   Bus.dev.func  registers          vend:prod     Description
   1.0.0         iomem 0x40000000   14e4:5365     BCM5365P Sentry5 Host Bridge
                     - 0x40001fff
   1.2.0         io 0x100-0x11f     1106:3038     VT82xxxxx UHCI USB 1.1 Controller
   1.2.1         io 0x120-0x13f     1106:3038     VT82xxxxx UHCI USB 1.1 Controller
   1.2.2         iomem 0x40002000   1106:3104     VIA USB 2.0
                     - 0x400020ff
   1.3.0         iomem 0x40004000   14e4:4320     BCM4306 802.11b/g Wireless LAN Controller
                     - 0x40005fff

   Devices that pop up on the MII bus, accesible via the mac core:

   bcm5325e or compatible, MII (MDC/MDIO)  5 ports switch

}}}

== Software Overview ==

Experimental supports these units.

== USB Storage ==

For information about how to use a USB storage device (such as a memory stick or a hard drive) and even boot from it, see UsbStorageHowto.
