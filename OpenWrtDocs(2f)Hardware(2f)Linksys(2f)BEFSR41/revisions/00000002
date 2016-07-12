=== BEFSR41 ===
There are a few versions of the hardware.

== Revision 2 ==
Uses an ARM processor.

found a bzip2 signature (0x42, 0x5A, 0x68) at 208 byte offset in the firmware from linksys website.

To extract some interesting firmware internals:

wget ftp://ftp.linksys.com/pub/network/BEFSR41V3_v1.05.00_code.bin

dd if=BEFSR41V3_v1.05.00_code.bin of=output.bz2 bs=16 skip=13 seek=0

then you end up with a bzip2 file that has garbage at the end of it.
