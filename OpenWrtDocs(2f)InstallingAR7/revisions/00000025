/!\ ~+'''WARNING'''+~ '''THIS GUIDE IS CURRENTLY WORK IN PROGRESS!'''

[:OpenWrtDocs]
[[TableOfContents]]

= Will OpenWrt work on my AR7 hardware? =

'''Supported hardware'''

See the [:TableOfHardware].


= Obtaining the firmware =

'''Stable Release'''

At the moment we have no stable supported release.

'''Stable Source'''

At the moment we have no stable supported release.

'''Development'''

Development takes place in SVN. You get the source via:

{{{
svn checkout https://svn.openwrt.org/openwrt/trunk/openwrt .
}}}

/!\ Note: Currently the AR7 code is disabled in the menu, as it is currently work in progress.

/!\ Note: patches to boot siemens se154and smc SMC7908VoWBRB devices can be found http://ar7-firmware.berlios.de/openwrt/patches.html.en

= Installing OpenWrt =

== Disclaimer ==

/!\ '''LOADING AN UNOFFICIAL FIRMWARE WILL VOID YOUR WARRANTY'''

OpenWrt is an unofficial firmware which is neither endorsed or supported by the vendor of your router. OpenWrt is provided "AS IS" and without any warranty under the terms of the GPL. You can always flash back your original firmware, so please be sure you have it downloaded and saved locally.

To avoid potentially serious damage to your router caused by an unbootable firmware you should read the documentation for your specific router model.

/!\ '''We strongly suggest you also read [:OpenWrtDocs/TroubleshootingAR7] before installing'''

/!\ '''The jffs2 versions of OpenWrt may take several minutes for the first bootup and will require a reboot before being usable'''

== Model specific information ==
See [:CategoryAR7Device]

== Boot sequence ==

Most AR7 hardware uses ["ADAM2"] as the bootloader. The following sequence details how the hardware boots.

 * Switch on
 * 2 seconds while bootloader initialises
 * 5 second window to begin upgrading firmware
 * Kernel boots

As you can see there is only a small window available in which to initiate the firmware upgrade.

Some AR7 hardware uses a different bootloader from Broad Net Technologies.
See [http://ar7-firmware.berlios.de/openwrt/] for modifications which support
this kind of hardware.

ZyXEL [:Prestige 660HW-61] even uses [:Bootbase] as Bootloader.

== Flashing using the bootloader ==

Depending on which router you have will depend on what method you can use to flash it with. Please refer to the table in section 1 for the available methods to use with your router.

The methods below can also be used to flash the official firmware back on to the router if required.

=== Flashing via ftp: one image file ===

ADAM2 stores the mtd partition layout in env variables. Depending on your hardware, there will be different numbers of mtd partitions with slightly different layout. Most devices have separated partitions for the kernel and the filesystem, which is not supported by OpenWrt. But it is possible to add a partition where kernel and rootfs will be together.

The first step is to determine the original layout:
{{{
$ telnet <router> 21
220 ADAM2 FTP Server ready.
USER adam2
331 Password required for adam2.
PASS adam2
230 User adam2 successfully logged in.
GETENV mtd0
mtd0                  0x900a0000,0x903f0000
200 GETENV command successful
GETENV mtd1
mtd1                  0x90010000,0x900a0000
200 GETENV command successful
GETENV mtd2
mtd2                  0x90000000,0x90010000
200 GETENV command successful
GETENV mtd3
mtd3                  0x903f0000,0x90400000
200 GETENV command successful
GETENV mtd4
501 mtd4 environment variable not set.
}}}

Here we can see that {{{mtd1}}} (kernel) and {{{mtd0}}} (filesystem) together go from {{{0x90010000}}} to {{{0x903f0000}}}, these values can vary by some KBytes depending on your machine.

We can also see that {{{mtd3}}} is the last partition and that there is no partition spanning kernel '''and''' filesystem. So we just add it:
{{{
SETENV mtd4,0x90010000,0x903f0000
200 SETENV command successful
}}}

After that, we can flash {{{openwrt-ar7-2.4-squashfs.bin}}} to {{{mtd4}}} via ftp:

'''Not all AR7 devices will use mtd4.  Double check which mtd you are flashing.'''

'''Replace X with the correct mtd.'''

'''During the pause before the upload, ADAM2 erases the mtd block (I think)'''
{{{
ftp> binary
ftp> quote MEDIA FLSH
ftp> put "openwrt-ar7-2.4-squashfs.bin" "openwrt-ar7-2.4-squashfs.bin mtdX"
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

If you have any trouble flashing to OpenWrt please refer to [:OpenWrtDocs/TroubleshootingAR7]
