#acl Known:read,write All:read
##   
## Note: these pages document the firmware itself, not packages
##       questions/comments should be posted to the forum
##        
[:OpenWrtDocs]
[[TableOfContents]]
= Will OpenWrt work on my hardware ? =
See [:OpenWrtDocs/Hardware]

= Obtaining the firmware =

'''Stable binaries'''

We recommend using the daily snapshots, these are compiled versions of the latest openwrt firmware. You'll find the snapshots [http://openwrt.org/downloads/snapshots/ here]. These snapshots will not work with G v2.2+ or GS v1.1 hardware.

'''Experimental binaries'''

If you own an WRT G v2.2+ or GS v1.1+ hardware, you will need to use the current experimental binary. These can be found [http://openwrt.org/downloads/experimental/bin/ here]. We recommend to use the squashfs versions for the [http://openwrt.org/downloads/experimental/bin/openwrt-wrt54g-squashfs.bin WRT54G] and [http://openwrt.org/downloads/experimental/bin/openwrt-wrt54gs-squashfs.bin WRT54GS]. More information on the experimental releases can be found on [http://openwrt.org/forum/viewtopic.php?t=1029 the forum].

'''jffs2 vs SquashFS'''

{{{
(irc logs)
[18:18] <[mbm]> the difference is in the filesystem layout
[18:18] <[mbm]> up until experimental, the filesystem was split
[18:18] <[mbm]> you had a small readonly squashfs partition, and the remaining space was jffs2
[18:18] <[mbm]> firstboot would symlink everything in the squashfs partition to the jffs2 partition and you'd use the jffs2 partition as the root device
[18:19] <[mbm]> you could never actually change anything on the squashfs partition, so if you wanted to alter a file you had to delete the symlink and create a new copy on jffs2
[18:20] <[mbm]> one of the advantages though, was that since you always had the squashfs filesystem you could always use it as part of the failsafe boot
[18:20] <[mbm]> to bypass issues with bootup scripts
[18:20] <[mbm]> experimental now gives you the option of no squashfs partition; everything goes onto jffs2
[18:21] <[mbm]> advantage there is that you don't have the redundancy, if you want to alter a file, you alter it
[18:21] <[mbm]> and there's the possibility of upgrading from one release to another release with just ipkg (you could try that on squashfs but you'd eat all the space with duplicate programs)
[18:22] <[mbm]> they both give you failsafe
[18:22] <[mbm]> just to different degrees
[18:22] <[mbm]> obviously there's no original copy of the filesystem on the jffs2 only images
[18:22] <[mbm]> so the only real difference between a normal boot and a failsafe boot is some nvram overrides
[18:23] <[mbm]> forces the networking to 192.168.1.1
[18:23] <[mbm]> if you've screwed up the startup that's not going to help much
[18:23] <[mbm]> and you'd need to reflash
[18:23] <[mbm]> reflashing with a jffs2 image erases everything on the filesystem
[18:24] <[mbm]> the squashfs firmware images only contain the squashfs files, which means basically that you can reflash and your jffs2 will be exactly as you left it
[18:25] <[mbm]> total filesystem space on a wrt54g is around 3M, basic filesystem will eat up about a meg of that
[18:26] <[mbm]> so ~2m free
[18:26] <[mbm]> on a wrt54gs it's ~6M free
[18:26] <[mbm]> when the squashfs boots up, it checks for the existance of the jffs2 partition and attempts to use it (unless you've booted failsafe)
[18:27] <[mbm]> if you want to think about it in terms of the flash .. your basic layout is [bootloader][firmware][free space][nvram]
[18:27] <[mbm]> firmware can take the whole space between the bootloader and nvram, but never actually does
[18:28] <[mbm]> in the squashfs layout, the firmware is [kernel][squashfs]
[18:28] <[mbm]> and [free space] becomes jffs2
[18:28] <[mbm]> as long as the firmware remains roughly the same size, jffs2 doesn't get touched
[18:29] <[mbm]> if the firmware gets larger, it starts to take over that free space, and any jffs2 data there gets overwritten
[18:29] <[mbm]> firmware gets smaller and the space just gets added onto the jffs2 partition with no corruption
[18:30] <[mbm]> the jffs2 firmwares are a little harder to explain
[18:30] <[mbm]> it's still the basic [bootloader][firmware][free space][nvram] layout
[18:30] <[mbm]> and the firmware (atleast initially) is [kernel][jffs2]
[18:31] <[mbm]> the trick is that on bootup it performs some magic to change the firmware to be just [kernel], making it basically [bootloader][kernel][free space ...][nvram]
[18:31] <[mbm]> and jffs2 gets migrated to the free space after the kernel (firmware)
[18:32] <[mbm]> actual technicalities aren't too important
[18:32] <[mbm]> but understand that reflashing to a jffs2 image will basically wipe everything between bootloader and nvram
}}}


'''Stable Source'''

The source can be obtained from http://www.openwrt.org/cgi-bin/viewcvs.cgi/buildroot/buildroot.tar.gz or via CVS using the following commands:

{{{
cvs -d:pserver:anonymous@openwrt.org:/openwrt login
cvs -d:pserver:anonymous@openwrt.org:/openwrt co buildroot
}}}

(It's the same source either way)

'''Experimental Source'''

If you have hardware that is not supported by the above verion of OpenWRT, you can use the [http://openwrt.org/downloads/experimental experimental version] of the code. You will need to compile this from scratch, and this is not recommended for beginners. The experimental code includes support for GS v1.1 and G v2.2 hardware. It may also work with G v3.0 hardware, however this has not yet been confirmed. More information on the experimental releases can be found on [http://openwrt.org/forum/viewtopic.php?t=1029 the forum].

= Installing OpenWrt =
/!\ '''LOADING AN UNOFFICIAL FIRMWARE WILL VOID YOUR WARRANTY'''

OpenWrt is an unofficial firmware which is neither endorsed or supported by Linksys or any other vendor. OpenWrt is provided "AS IS" and without any warranty under the terms of the [http://www.gnu.org/copyleft/gpl.html GPL].

To avoid potentially serious damage to your router caused by an unbootable firmware we strongly suggest enabling a setting known as '''boot_wait'''.

/!\ '''We strongly suggest you also read [:OpenWrtDocs/Troubleshooting] before installing'''

/!\ '''The jffs2 versions of the experimental build may take several minutes for the first bootup and will require a reboot before being usable'''

== Enabling boot_wait ==

The router does not boot directly into the firmware, instead it boots into a program known as a bootloader which is responsible for initializing the hardware and loading the firmware. If the boot_wait variable is set, the bootup process is delayed by few seconds allowing a new firmware to be installed through the bootloader using tftp. Setting of the boot_wait variable is done through a bug in the Ping.asp administration page by pinging the certain "addresses" listed below

First, for this to work the '''internet port must have a valid ip address''', either from dhcp or manually configured from the main page - the port itself doesn't need to be connected unless using dhcp. Next, navigate to the Ping.asp page and enter exactly each line listed below, one line at a time into the "IP Address" field, pressing the Ping button after each entry.

/!\ '''Linksys' 3.37.6 patches the ping.asp bug; downgrading to 3.37.2  is required before the following will work.'''

/!\ '''Old firmware is available at [ftp://ftp.linksys.com/pub/network/]. These are ''official'' firmware images from Linksys'''

{{{
;cp${IFS}*/*/nvram${IFS}/tmp/n
;*/n${IFS}set${IFS}boot_wait=on
;*/n${IFS}commit
;*/n${IFS}show>tmp/ping.log
}}}

When you get to the last command the ping window should be filled with a long list of variables including '''boot_wait=on''' somewhere in that list.

This ping exploit definitely works with WRT54G v2.0/GS v1.0 and there are documented cases of it working for the latest hardware release WRT54G v2.2/GS v1.1.  You must have an address on the WAN port.  In the Setup/Basic Setup/Internet Setup section you may wish to select Static IP and set IP=10.0.0.1, Mask=255.0.0.0, Gateway=10.0.0.2.  Those values are meaningless; you'll be overwriting them soon with new firmware. Note : flashing a Linksys WRT54GS v1.1 via TFTP using is only possible using the Port 1 of the switch !

You can also use the [http://openwrt.org/forum/viewtopic.php?t=507&highlight=takeover take-over] script to make ping hack in a single command (need a shell command line interpreter).

=== Setting boot_wait from a serial connection ===

With a serial connection to your WRT, you don't have to use the ping bug or change your Linksys firmware. You can set boot_wait from the console, using the commands
{{{
#nvram set boot_wait=on
#nvram get boot_wait           (just to confirm, should respond with "on")
#nvram commit                  (takes a few seconds to complete)
}}}

You can also set boot_wait from the CFE boot loader (to enter CFE, reboot the router with "# reboot" while hitting "Ctrl C" continously)
{{{
CFE> nvram set boot_wait=on
CFE> nvram get boot_wait           (just to confirm, should respond with "on")
CFE> nvram commit                  (takes a few seconds to complete)
}}}

== Using boot_wait to upload the firmware ==

Although the firmware can be installed through more traditional means, we recommend that you use boot_wait for your first install. This will confirm boot_wait is correctly enabled and provide a firmware recovery experience without the stress of a broken router.

While in the bootloader the linksys wrt54g(s) will be forced to a lan ip of 192.168.1.1. To use the bootloader's tftp server you need to use a standard tftp client -- the tftp clients provided by linksys will not work for this. The file to be uploaded depends on the model; non linksys models take a TRX file while linksys models take a BIN file.

||'''Model'''||'''Firmware'''||
||WRT54G||openwrt-g-code.bin||
||WRT54GS||openwrt-gs-code.bin||
||(other)||openwrt-linux.trx||

The BIN file is simply a TRX with some extra information at the start to indicate the model. The only difference between openwrt-g-code.bin and openwrt-gs-code.bin is the first 4 bytes which determine the model.

The basic procedure of using boot_wait is:
  * unplug the power to your router
  * start your tftp client
    * give it the router's address (always 192.168.1.1)
    * set mode to octet
    * tell the client to resend the file, until it succeeds.
    * put the file
  * plug your router, while having the tftp client running and constantly probing for a connection
  * the tftp client will receive an ack from the bootloader and starts sending the firmware

/!\ '''Please be patient, the reflashing occurs AFTER the firmware has been transferred. DO NOT unplug the router, it will automatically reboot into the new firmware.''' OpenWrt will light the DMZ led while booting, after bootup it will turn the DMZ led off.

||'''LED pattern'''||'''reason'''||
||Solid power & DMZ||OpenWrt is booting or (if prolonged) has failed to boot, try [:OpenWrtDocs/Troubleshooting: failsafe mode]. (Usually caused by old/corrupt jffs2 data from a previous OpenWrt install)||
||flashing power, slow flashing dmz||Error flashing / Corrupt firmware||

The tftp commands might vary across different implementations. Here are two examples, netkid's tftp client and Advanced TFTP (available from: [ftp://ftp.mamalinux.com/pub/atftp/])

netkit's tftp commands:
{{{
tftp 192.168.1.1
tftp> binary
tftp> rexmt 1
tftp> trace
Packet tracing on.
tftp> put openwrt-g-code.bin
}}}
Setting "rexmt 1" will cause the tftp client to constantly retry to send the file to the given address. As advised above, plug your box after typing the commands, and as soon as WRT54G's bootloader start to listen, your client will successfully connect and send the firmware. You can try to run # ping -f 192.168.1.1 (as root) in a seperate window and fire the line put openwrt-g-code.bin as the colons stop running over your terminal when you power-recycle your linksys. 

Advanced TFTP commands:
{{{ 
atftp
tftp> connect 192.168.1.1
tftp> mode octet
tftp> trace
tftp> put openwrt-g-code.bin
}}}
You don't have to tell atftp to retry file sending, that's default.

Please note, netkit tftp has failed to work for some people. Try to use Advanced TFTP. Don't forget about your firewall settings, if you have one.

Note: At least netkit-tftp on gentoo failed me (EpA). All I got was Just one ACK reply and nothing more.
I tried with aftp and it worked straight away.

||'''TFTP Error'''||'''Reason'''||
||Code pattern is incorrect||The firmware image you're uploading was intended for a different model.||
||Invalid Password||The firmware has booted and you're connected to a password protected tftp server contained in the firmware, not the bootloader's tftp server.||
||Timeout||Ping to verify the router is online[[BR]]Try a different tftp client (some are known not to work properly)||

If your computer is directly connected to the router and you are consistently getting "Invalid Password" failures, try connecting your computer and the router to a hub or switch.  Doing so will keep the link up and prevent the computer from disabling its interface while the router is off.

Windows 2000 has a TFTP server, and it [http://martybugs.net/wireless/openwrt/flash.cgi can be used] to flash with OpenWrt firmware. Note that the Windows PC needs to be configured with a static IP address in the 192.168.1.0/24 subnet, and cannot use a DHCP IP address when flashing the firmware.

== Installing via CFE - Common Firmware Environment ==

If you managed to get a serial connection to your router and can stop CFE from booting the firmware with strg-c, you can update your router
via network. You need to configure a TFTP-server on one of your systems and connect it to the same network as your lan port of your router.
Put the correct trx file for your router and task to your tftpboot/tftp directory.
If you see the command line of your Bootloader like this: 
{{{
CFE>
}}}

For example flashing a linksys WRT54GS v1.0:
{{{
CFE>flash -noheader 192.168.1.2:/openwrt-generic-jffs2-8MB.trx flash1.trx
}}}

This is useful for unsupported models, because you can skip the header check.
Otherwise some WRT54GS are very picky about the 2 second timeout, so you can definitely flash it without any timing problems.

== ASUS WL-500G routers ==
The installation procedure there is slightly different from the Linksys routers:
Pull the plug, press and hold the reset button, plug the device and wait until the PWR LED starts flashing slowly (almost immediately). Now release the reset button and upload the firmware by TFTP using the following commands:

TFTP commands:
{{{
tftp 192.168.1.1
tftp> binary
tftp> trace
tftp> get ASUSSPACELINK\x01\x01\xa8\xc0 /dev/null
tftp> put openwrt-linux.trx ASUSSPACELINK
}}}

After this, wait until the PWR LED stops flashing and the device to reboot and you should be set. There's also nice shell script doing this work for you to be at [http://openwrt.openbsd-geek.de/flash.sh].

As an alternative (or if this installation routine doesn't do the trick for you) you can always use the ASUS Recovery tool from your utilities CD to upload your openwrt firmware.

Another thing is that the ASUS WL500G doesn't seem to revert to the 192.168.1.1 address when starting the boot manager but seems to use the LAN IP address set in NVRAM, so try this address or use the recovery tool if you've got problems flashing your firmware. On the other hand, boot_wait seems to be enabled by default on these devices.



== Siemens Gigaset SE505 ==
The installation procedure is essentially the same as the generic one described above. The only differences are that the bootloader listens on 192.168.2.1 and the IP of the machine sending the new firmware has to be 192.168.2.100 or the router will only accept the first packet.

boot_wait seems to be enabled on these devices.



= Using OpenWrt =
Please see [:OpenWrtDocs/Using]

= Troubleshooting =
If you have any trouble flashing to OpenWrt please refer to [:OpenWrtDocs/Troubleshooting]
