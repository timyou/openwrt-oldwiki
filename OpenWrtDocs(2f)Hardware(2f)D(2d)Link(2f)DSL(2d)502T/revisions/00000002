= Work in Progress =

== Details ==
ADSL port
4 lan ports

Flash chip: 4Meg - Samsung K8D3216UBC a 32Mbit NOR-type Flash Memory organized as 4M x 8 

Dlink web site: http://support.dlink.com/products/view.asp?productid=DSL%2D504T#

D-Link Systems, Inc. has issued an End of Life (EOL) Notice for the DSL-504T and has discontinued it as of Tuesday, August 01, 2006. Technical and RMA support for this product shall continue, with proof of purchase, until Friday, August 01, 2008.

== How to debrick ==
See the forum for how to debrick the DSL-502T [[BR]]
http://forum.openwrt.org/viewtopic.php?id=7742 [[BR]]

== Hints from the forum article ==
Hints from Z3r0 

If you want to upload a custom OpenWRT firmware you will need to have a deeper understanding on the way the router works.

The single combined firmware is divided as so:

HEX
0-90 header
90-80FFF kernel with padded 0s at the end
81000-20EFFF filesystem with padded 0s
20F000-20F007 checksum for the entire file made with TICHKSUM (8 Bytes)

Please remember that a hex number is 4 bits, so each byte contains 2 hex numbers, this means 8 bytes = 16 hex numbers.

The TICHKSUM is not a standard 4 Byte CRC32 or 8 Byte CRC64, it is firstly a fixed set of 8 hex numbers 23DE53C4 (magic numbers) and then an 8 hex checksum such as:

23DE53C4 07D74626

Ok so.. what am I getting at here?

Well, if you compile the openwrt trunk and examine the ar7 firmware with a hex editor you will see that the squashfs.bin uses totally different mappings, openwrt does not waste space by padding to boundaries with extra 0s.

Openwrt is usually
0-x kernel
x-eof squashfs

so for this file system to boot, you will need to find the hex values of the start of the squashfs filesystem (use ghex under linux or XVI under windows) and search for 'hsq' this signifies the start of the squashfs. Now adjust mtd0 and mtd1 variables accordingly.

You also need to add a checksum to the end of the file by running ./tichksum under Linux or by compiling tichksum under windows.

TICHKSUM can be found in the DSL-502T source code.
