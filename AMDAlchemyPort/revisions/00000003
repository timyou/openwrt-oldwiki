[[TableOfContents]]
= Status of the AMD Alchemy port of OpenWrt =

== What is this AMD Alchemy stuff? ==

[http://www.amd.com/us-en/ConnectivitySolutions/ProductInformation/0,,50_2330_6625,00.html AMD Alchemy] is a processor developped by AMD focused on small Web/Network applicances.

See the [:TableOfHardware] for supported AMD Alchemy routers.

See [:OpenWrtDocs/InstallingAlchemy] if you are brave enough to test it.


== Finished tasks ==

The support for AMD Alchemy is completed :

   * The images are working and you can do some more testing

== TODO ==

   * Port the I2C driver to 2.6 kernel

== Firmware/Bootloader ==

The bootloader is [http://www.linux-mips.org/wiki/YAMON Yamon], and supports TFTP booting. The firmware can only be booted when it is in SREC format. OpenWrt images are in the right format already.

= How to help =

Since the board is really well supported with both Linux 2.4 and 2.6, you can test the firmware built with kamikaze and report any problems you may encounter.

Known problems :

    * madwifi-ng driver may crash and does not always work in client mode (madwifi-ng related problem)
    * original 2.4 LED driver does not work and may crash the board, it has therefore not been ported


=== Flashing images ===

The YAMON bootloader allows you to either run a kernel in RAM (for testing purpose), or a filesystem in RAM, or both, but you can also write these two components on the flash.

==== Loading a kernel in RAM ====

Once you have YAMON access just :

{{{
load <IP address>/<kernel filename>
}}}

Then modify the {{{start}}} variable in order to load the kernel in ram and not on the flash, for that do :

{{{
go . rootfstype=<your fs type> init=<your init script>
}}}

==== Loading filesystem from RAM ====

Almost same thing as before, except that you are likely to use either the {{{$start}}} variable, or the {{{go}}} command after having loaded your filesystem via {{{load}}}

===== Writing combined images to Flash ====


First you need to erase the two sections of the flash which contain filesystem and kernel :

{{{
erase 0xbfd00000 0xf0000
erase -s
load <your combined image>
}}}

This will first erase the kernel, then filesystem, the box will reboot, and next time you load a combined image, it will be written to the flash.

==== Writing kernel to Flash ====

Almos the same idea as before :

{{{
erase 0xbfd00000 0xf0000
load <your kernel>
}}}

Next time you load a kernel via TFTP it will be written in the flash


==== Writing filesystem to Flash ====

Once again, almost the same thing :

{{{
erase -s system
load <your system>
}}}


= Other stuff =
== Model-specific information ==

Mode-specific information can be found on that model's page. See ["CategoryAlchemyDevice"].

== JTAG ==

The JTAG is an EJTAG and can be easily accessible :
 
[http://www.meshcube.org/meshwiki/DebugConnector?action=AttachFile&do=get&target=connectors.png]

The 12-pin connectors superposes a serial console, and a JTAG interface :

[http://www.meshcube.org/meshwiki/DebugConnector?action=AttachFile&do=get&target=debug-pinout.png]

Here is the pinout :

|| 01 || TXD (3.3v) || serial  ||
|| 02 || RXD (3.3v) || serial  ||
|| 03 || VCC (3.3v) ||   ||
|| 04 || TCK     || EJTAG ||
|| 05 || RST#     || EJTAG ||
|| 06 || TMS     || EJTAG ||
|| 07 || DINT     || EJTAG ||
|| 08 || TDO     || EJTAG ||
|| 09 || GND        ||  ||
|| 10 || TDI     || EJTAG ||
|| 11 || GND        ||  ||
|| 12 || TRST     || EJTAG ||

Standard EJTAG interface, as the one you can build for a WRT54G will work. Same thing for the serial port.

Happy debugging !

----
CategoryOpenWrtPort
