=== Conceptronic C54APRA ===

The Conceptronic C54APRA is a router with built-in ADSL modem for Annex A connections. It uses the AR7 chipset.

=== Opening the case ===

On the bottom there are 4 scews underneath the little rubbers.

=== Picture ===

attachment:c54apra.jpg

=== Serial ===

=== JTAG ===

There are two 14 pin solder pads on the device. Which one is JTAG is unknown.

=== Installing OpenWrt ===

There are several models out in the wild (at least, I have seen different ones). The first thing you should do is change a few settings so you can ftp into ADAM2:

{{{
# cd /proc/ticfg
# echo "autoload_timeout 7" > env
}}}

After a reboot you should be able to get into ADAM2 using FTP (most probably on 10.8.8.8).

You might also want to check if there is an entry for mtd4. If there is none, you can add it either via the ADAM2 FTP prompt, or using the same method as above.

The layout for the mtds should be:

{{{
mtd0    0x90091000,0x903f0000
mtd1    0x90010000,0x90090000
mtd2    0x90000000,0x90010000
mtd3    0x903f0000,0x90400000
mtd4    0x90010000,0x903f0000
}}}

A stock AR7 build (kamikaze, subversion revision 6866) should install painlessly on this device.
----
["CategoryAR7Device"] CategoryModel
