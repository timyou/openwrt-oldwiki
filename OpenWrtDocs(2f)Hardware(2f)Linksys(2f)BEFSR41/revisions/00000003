=== BEFSR41 ===
There are a few versions of the hardware.

== Revision 2 ==
Uses an ARM processor.

found a bzip2 signature (0x42, 0x5A, 0x68) at 208 byte offset in the firmware from linksys website.

this standard linksys header goes like this:

3E0000EA410000EA4F0000EA420000EA440000EA460000EA4E0000EA470000EA

after that there are some bytes that differ.


To extract some interesting firmware internals:

wget ftp://ftp.linksys.com/pub/network/BEFSR41V3_v1.05.00_code.bin

dd if=BEFSR41V3_v1.05.00_code.bin of=output.bz2 bs=16 skip=13 seek=0

then you end up with a bzip2 (100k block size compressed) file that has garbage at the end of it.

if you re-compress it using 100k block sizes, and run 'cmp', you find the two files are identical except that the original has '0xFF' values to pad out the full 239408 bytes of the bzip2 archive filesize.

we can safetly ignore the junk at the end and decompress.

bunzip2 output.bz2

now this file has strings we can see in a hex editor. interesting!
