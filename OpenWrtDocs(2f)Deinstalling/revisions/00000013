##
## Note: these pages document the firmware itself, not packages
##       questions/comments should be posted to the forum
##
OpenWrtDocs [[TableOfContents]]

= How can I remove OpenWrt ? =
These steps can also be used to reflash !OpenWrt (f. e. when you like to upgrade).

== Using the mtd utility ==
If you are unhappy with our distribution you can go back to the original firmware you have used before. For that please use the following commands:

{{{
cd /tmp
wget http://www.example.org/original.trx
mtd -e linux -r write original.trx linux
}}}
Replace the file {{{original.trx}}} with the filename of the firmware you like to install. This will erase the flash (-e linux) and write the new image. The -r will reboot the router after successfully writing the file.

If you get a error message on the above {{{mtd}}} command like "no valid command given" you are using an old version of {{{mtd}}} which doesn't support the {{{-r}}} or {{{-e}}} parameters. Download a newer statically compiled version ({{{mtd.static}}}):

{{{
cd /tmp
wget http://downloads.openwrt.org/people/wbx/mtd.static
chmod a+x mtd.static
wget http://www.example.org/original.trx
./mtd.static -e linux -r write original.trx linux
}}}
'''TIP:''' [http://forum.openwrt.org/viewtopic.php?id=3474 PLEASE READ - Common mistakes] thread section 2 also. It describes when you should use the {{{openwrt-brcm-2.4-squashfs.trx}}} image.

If you only have a Linksys {{{.bin}}} firmware file, this is not a problem, simply cut off the header before using the commands above:

{{{
dd bs=32 skip=1 if=original.bin of=original.trx
}}}
'''TIP:''' If your replacement firmware has a web interface, remember to flush your browser cache, sessions etc. This will avoid misleading 404 errors.

== Using the webif ==
Since White Russian RC4 you can use the webif to go back to the original firmware. The webif automatically recognizes a firmware image uploaded in BIN or TRX format and converts it accordingly.

 * Load the webif in your web browser and goto the System / Firmware upgrade page
 * make sure Erase the JFFS2 partition is checked
 * choose the BIN or TRX firmware file (downloaded before from the manufactures website onto your PC)
 * click on the button upload
== Using TFTP ==
The other way you can use is the [:Installing/TFTP:TFTP] method.  The TFTP page explains how to install OpenWrt via TFTP, but this method should also work for other firmware.

/!\ '''Note:''' On many versions, the TFTP server is only able to accept smaller firmwares at bootup. Firmwares that are over approximately 3 MB will fail with a {{{no space}}} error. If this happens you'll need to either use a different firmware or reflash using the {{{mtd}}} commands above instead.
