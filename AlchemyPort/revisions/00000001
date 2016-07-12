[[TableOfContents]]
= Status of the AMD Alchemy port of OpenWrt =

== What is this AMD Alchemy stuff? ==

[http://www.amd.com/us-en/ConnectivitySolutions/ProductInformation/0,,50_2330_6625,00.html AMD Alchemy] is a processor developped by AMD focused on small Web/Network applicances.

See the [:TableOfHardware] for supported AMD Alchemy routers.

See [:OpenWrtDocs/InstallingAlchemy] if you are brave enough to test it.


== Finished tasks ==

The support for AMD Alchemy is almost completed :

   * Kernel compiles fine and should
   * The default hardware is supported

== TODO ==

   * Flash the AccessCube with the new firmware

== Firmware/Bootloader ==

The bootloader is [http://www.linux-mips.org/wiki/YAMON Yamon], and supports TFTP booting.

= How to help =

Since the board is really well supported with both Linux 2.4 and 2.6, you can test the firmware built with kamikaze.


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
