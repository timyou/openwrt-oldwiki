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

'''Compiled binaries'''

We recommend using the daily snapshots, these are compiled versions of the latest openwrt firmware. You'll find the snapshots in http://openwrt.org/downloads/snapshots/

'''Source'''

The source can be obtained from http://www.openwrt.org/cgi-bin/viewcvs.cgi/buildroot/buildroot.tar.gz or via CVS using the following commands:

{{{
cvs -d:pserver:anonymous@openwrt.org:/openwrt login
cvs -d:pserver:anonymous@openwrt.org:/openwrt co buildroot
}}}

(It's the same source either way)

'''Experimental Code'''

If you have hardware that is not supported by the above verion of OpenWRT, you can use the [http://openwrt.org/download/experimental Experimental version] of the code. You will need to compile this from scratch, and this is not recommended for beginners. The experimental code includes support for GS v1.1 and G v2.2 hardware. It may also work with G v3.0 hardware, however this has not yet been confirmed.

= Installing OpenWrt =
/!\ '''LOADING AN UNOFFICIAL FIRMWARE WILL VOID YOUR WARRANTY'''

OpenWrt is an unofficial firmware which is neither endorsed or supported by Linksys or any other vendor. OpenWrt is provided "AS IS" and without any warranty under the terms of the [http://www.gnu.org/copyleft/gpl.html GPL].

To avoid potentially serious damage to your router caused by an unbootable firmware we strongly suggest enabling a setting known as '''boot_wait'''.

== Enabling boot_wait ==

The router does not boot directly into the firmware, instead it boots into a program known as a bootloader which is responsible for initializing the hardware and loading the firmware. If the boot_wait variable is set, the bootup process is delayed by few seconds allowing a new firmware to be installed through the bootloader using tftp. Setting of the boot_wait variable is done through a bug in the Ping.asp administration page by pinging the certain "addresses" listed below

First, for this to work the '''internet port must have a valid ip address''', either from dhcp or manually configured from the main page - the port itself doesn't need to be connected unless using dhcp. Next, navigate to the Ping.asp page and enter exactly each line listed below, one line at a time into the "IP Address" field, pressing the Ping button after each entry.

/!\ '''Linksys' 3.37.6 patches the ping.asp bug; downgrading to 3.37.2 is required before the following will work:'''

{{{
;cp${IFS}*/*/nvram${IFS}/tmp/n
;*/n${IFS}set${IFS}boot_wait=on
;*/n${IFS}commit
;*/n${IFS}show>tmp/ping.log
}}}

When you get to the last command the ping window should be filled with a long list of variables including '''boot_wait=on''' somewhere in that list.

This ping exploit definitely works with WRT54G v2.0/GS v1.0 and there are documented cases of it working for the latest hardware release WRT54G v2.2/GS v1.1.  You must have an address on the WAN port.  In the Setup/Basic Setup/Internet Setup section you may wish to select Static IP and set IP=10.0.0.1, Mask=255.0.0.0, Gateway=10.0.0.2.  Those values are meaningless; you'll be overwriting them soon with new firmware.

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
Setting "rexmt 1" will cause the tftp client to constantly retry to sent the file to the given address. As advised above, plug your box after typing the commands, and as soon as WRT54G's bootloader start to listen, your client will successfully connect and send the firmware. You can try to run # ping -f 192.168.1.1 (as root) in a seperate window and fire the line put openwrt-g-code.bin as the colons stop running over your terminal when you power-recycle your linksys. 

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

||'''TFTP Error'''||'''Reason'''||
||Code pattern is incorrect||The firmware image you're uploading was intended for a different model.||
||Invalid Password||The firmware has booted and you're connected to a password protected tftp server contained in the firmware, not the bootloader's tftp server.||
||Timeout||Ping to verify the router is online[[BR]]Try a different tftp client (some are known not to work properly)||

Windows 2000 has a TFTP server, and it [http://martybugs.net/wireless/openwrt/flash.cgi can be used] to flash with OpenWrt firmware. Note that the Windows PC needs to be configured with a static IP address in the 192.168.1.0/24 subnet, and cannot use a DHCP IP address when flashing the firmware.

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

= Using OpenWrt =
Please see [:OpenWrtDocs/Using]
