##   
## Note: these pages document the firmware itself, not packages
##       questions/comments should be posted to the forum
##        
[:OpenWrtDocs]
[[TableOfContents]]

= How I remove OpenWrt ? =

If you are unhappy with our distribution you can go back to the original firmware you have used before.

For that please use the following commands:

{{{
cd /tmp
wget http://www.example.org/original.trx
mtd -e linux -r write original.trx linux
}}}

Replace the file "original.trx" with the filename of the firmware you like to install. "linux" is the partition you need
to write. -e linux will remove old stuff, before writing the new image. -r will reboot the router after successfully writing the file.

If you only have a .BIN formatted firmware file, this is not a problem, simply cut of the header before using the commands above:
{{{
dd bs=32 skip=1 if=original.bin of=original.trx
}}}

= Can I use TFTP to go back to the original firmware ? =

Sure, the other way you can use is the TFTP method.

/!\ Note: On many versions, the TFTP server is only able to accept smaller firmwares at bootup. Firmwares that are over approximately 3M will fail with a "no space" error. If this happens you'll need to either use a different firmware or reflash using the mtd commands above instead.
