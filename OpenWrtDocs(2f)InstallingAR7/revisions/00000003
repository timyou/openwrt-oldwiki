/!\ ~+'''WARNING'''+~ '''THIS GUIDE IS CURRENTLY WORK IN PROGRESS!'''

[:OpenWrtDocs]
[[TableOfContents]]

= Will OpenWrt work on my AR7 hardware? =

'''Supported hardware'''

||'''Manufacturer'''||'''Model'''||'''Version'''||'''Method'''||'''Code Pattern'''||
||ALLNet||ALL130DSL|| || || ||
||D-Link||DSL-G604T/G664T|| ||ftp||-||
||Linksys||WAG54G||V2-AU||ftp||WAG2||
||Linksys||WAG54G||V2-DE|| ||WA22||
||Linksys||WAG54G||V2-EU||linksys-tftp||WA21||
||Linksys||WAG54G||V2-FR|| ||WA21||
||Linksys||WAG54G||V2-UK||tftp||WA21||
||Linksys||WRTP54G|| || || ||

## D-Link DSL-G664T/EU V.A1 = ADAM2 Revision 0.22.02
## Linksys WAG54G V2-AU = ADAM2 Revision 0.22.06
## Linksys WAG54G V2-DE = ADAM2 Revision 
## Linksys WAG54G V2-EU = ADAM2 Revision 0.22.12
## Linksys WAG54G V2-UK = ADAM2 Revision 0.22.12

* If the tftp method doesn't work, try using the linksys-tftp method

= Obtaining the firmware =

'''Stable Release'''

At the moment we have no stable supported release.

'''Stable Source'''

At the moment we have no stable supported release.

'''Development'''

Development takes place in CVS. You get the source via:

{{{
cvs -d:pserver:anonymous@openwrt.org:/openwrt login
cvs -d:pserver:anonymous@openwrt.org:/openwrt co openwrt
}}}

/!\ Note: Currently the AR7 code is disabled in the menu, as it is currently work in progress.

= Installing OpenWrt =

== Disclaimer ==

/!\ '''LOADING AN UNOFFICIAL FIRMWARE WILL VOID YOUR WARRANTY'''

OpenWrt is an unofficial firmware which is neither endorsed or supported by the vendor of your router. OpenWrt is provided "AS IS" and without any warranty under the terms of the GPL. You can always flash back your original firmware, so please be sure you have it downloaded and saved locally.

To avoid potentially serious damage to your router caused by an unbootable firmware you should read the documentation for your specific router model.

/!\ '''We strongly suggest you also read [:OpenWrtDocs/TroubleshootingAR7] before installing (To be written)'''

/!\ '''The jffs2 versions of OpenWrt may take several minutes for the first bootup and will require a reboot before being usable'''

== Boot sequence ==

AR7 hardware uses adam2 as the bootloader. The following sequence details how the hardware boots.

 * Switch on
 * 2 seconds while bootloader initialises
 * 5 second window to begin upgrading firmware
 * Kernel boots

As you can see there is only a small window available in which to initiate the firmware upgrade.

== Flashing using the bootloader ==

Depending on which router you have will depend on what method you can use to flash it with. Please refer to the table in section 1 for the available methods to use with your router.

The methods below can also be use the flash the official firmware back on to the router if required.

=== Flashing via ftp method ===

Firstly you will need to obtain the appropriate version of OpenWrt for your router. In this case you will need to obtain two files, the kernel image, and the rootfs image. You have a choice of using squashfs or jffs2 for the rootfs.

The basic procedure of using a ftp client to upload a new firmware to your router is as follows:

 * First start with the router switched off.
 * Turn on your router
 * Wait 3 seconds
 * Initiate a connection with your ftp client. Using the router's address (usually 192.168.1.1), username adam2, and password adam2.
 * Set mode to binary
 * Enter the following command in your ftp client: quote MEDIA FLSH
 * Put the kernel image. eg: put "openwrt-ar7-zimage.bin" "openwrt-ar7-zimage.bin mtd1"
 * Put the rootfs image. eg: put "openwrt-ar7-rootfs.bin" "openwrt-ar7-rootfs.bin mtd0"  ### TODO FILENAME ###
 * Enter the following command in your ftp client: quote REBOOT

'''Example using ftp (linux)'''
{{{
ftp
}}}
Turn on router, and wait 3 seconds.
{{{
ftp> open 192.168.1.1
}}}
Enter username and password, both are adam2
{{{
ftp> binary
ftp> quote MEDIA FLSH
ftp> put "openwrt-ar7-zimage.bin" "openwrt-ar7-zimage.bin mtd1"
ftp> put "openwrt-ar7-rootfs.bin" "openwrt-ar7-rootfs.bin mtd0"  ### TODO FILENAME ###
ftp> quote REBOOT
ftp> quit
}}}

For more detailed infomation about adam2's ftp capabilities, have a look at:

[http://www.seattlewireless.net/index.cgi/ADAM2]

=== Flashing via ftp: one image file (requires serial console) ===

ADAM2 stores the mtd partition layout in env variables. It is possible to change that layout so that kernel and rootfs will be in one partition:

{{{
Adam2_AR7RD > setenv mtd1 0x90010000,0x903f0000
}}}

After that, you can flash {{{openwrt-ar7-2.4-squashfs.bin}}} to {{{mtd1}}} via ftp:
{{{
ftp> binary
ftp> quote MEDIA FLSH
ftp> put "openwrt-ar7-2.4-squashfs.bin" "fs mtd1"
ftp> quote REBOOT
ftp> quit
}}}
(As of 2005-07-24, this method doesn't work with jffs2 images)

=== Flashing via tftp method ===

Firstly you will need to obtain the appropriate version of OpenWrt for your router. Different routers have different code patterns assigned to their firmware. Use the table in section 1 to select the correct firmware with matching code pattern for your router. This should be a single image containing the kernel and rootfs. You have a choice of using squashfs or jffs2.

The basic procedure of using a tftp client to upload a new firmware to your router is as follows:

 * First start with the router switched off.
 * Start your tftp client
 * Give it the router's address (usually 192.168.1.1)
 * Set mode to octet
 * Turn on your router
 * Wait 3 seconds
 * Put the file

'''Notes:'''

The target filename of the new firmware '''MUST''' be called upgrade_code.bin otherwise it'll be rejected. Your tftp client may allow you to specify this as an extra parameter to the put command, otherwise you'll have to rename the file.

If you timed the send correctly, the firmware should be successfully sent to the router. If your tftp client gives this indication you can type quit to exit the tftp client. If the send fails you will have to try again.

/!\ IMPORTANT: If the send if successful, do not touch your router even once the tftp client has finished! The bootloader saves the firmware into memory first, then it erases the previous firmware, before flashing the new. Once it finishes flashing it will automatically reboot. At this point you should then be able to telnet into the router.

'''Example using tftp-hpa (linux)'''
{{{
tftp
tftp> connect 192.168.1.1
tftp> mode octet
tftp> trace
}}}
Turn on router, and wait 3 seconds.
{{{
tftp> put openwrt-ar7-2.4-squashfs-WA21.bin upgrade_code.bin
tftp> quit
}}}

=== Flashing via linksys-tftp method (linux only) ===

Firstly you will need to obtain the appropriate version of OpenWrt for your router. Different routers have different code patterns assigned to their firmware. Use the table in section 1 to select the correct firmware with matching code pattern for your router. This should be a single image containing the kernel and rootfs. You have a choice of using squashfs or jffs2.

Next you will need to download and compile a modified tftp client. This is because the bootloader only accepts firmware upgrades with a password provided. You can get the modified tftp client from here:

[http://www.redsand.net/projects/linksys-tftp/linksys-tftp.php]

The basic procedure of using a tftp client to upload a new firmware to your router is as follows:

 * First start with the router switched off.
 * Start your tftp client
 * Give it the router's address (usually 192.168.1.1)
 * Set mode to octet
 * Turn on your router
 * Wait 3 seconds
 * Put the file using the password adam2

'''Notes:'''

The target filename of the new firmware '''MUST''' be called upgrade_code.bin otherwise it'll be rejected. You will need to rename the firmware file to use with this tftp client, as the second parameter to the put command is the password.

If you timed the send correctly, the firmware should be successfully sent to the router. If your tftp client gives this indication you can type quit to exit the tftp client. If the send fails you will have to try again.

/!\ IMPORTANT: If the send if successful, do not touch your router even once the tftp client has finished! The bootloader saves the firmware into memory first, then it erases the previous firmware, before flashing the new. Once it finishes flashing it will automatically reboot. At this point you should then be able to telnet into the router.

'''Example using linksys-tftp (linux)'''
{{{
linksys-tftp
linksys-tftp> connect 192.168.1.1
linksys-tftp> mode octet
linksys-tftp> trace
}}}
Turn on router, and wait 3 seconds.
{{{
linksys-tftp> put upgrade_code.bin adam2
linksys-tftp> quit
}}}

== Flashing notes ==

'''Tftp errors'''

||'''TFTP Error'''||'''Reasons'''||
||Code pattern is incorrect||The firmware image you're uploading was intended for a different model.||
||<rowspan=2> Invalid Password||The firmware has booted and you're connected to a password protected tftp server contained in the firmware.||
||Your router requires a tftp client using a password to upgrade via the bootloader's tftp server.||
||Timeout||You missed the window. If this persists try a different tftp client (some are known not to work properly).||

Some machines will disable the ethernet when the router is powered off and not enable it until after the router has been powered on for a few seconds. If you're consistently getting "Invalid Password" failures try connecting your computer and the router to a hub or switch. Doing so will keep the link up and prevent the computer from disabling its interface while the router is off.

'''Other methods of upgrading'''

While some official firmware's have a tftpd server running once loaded. It is not a recommended way to upgrade the router using this method, it has been found to be unreliable.

Currently the OpenWrt firmware's don't include the checksum to allow firmware upgrading via the web inferface of official firmware's. This may change in the future. However the recommended method is via tftp/ftp (depending on which is available) at bootloader time. Unless the bootloader is damaged this should allow recovery from any failed flashes.

= Using OpenWrt =

Please see [:OpenWrtDocs/Using]

= Troubleshooting =

If you have any trouble flashing to OpenWrt please refer to [:OpenWrtDocs/TroubleshootingAR7] (To be written)
