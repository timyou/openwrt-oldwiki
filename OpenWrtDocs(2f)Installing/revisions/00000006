#acl Known:read,write All:read
##   
## Note: these pages document the firmware itself, not packages
##       questions/comments should be posted to the forum
##        
[:OpenWrtDocs]
[[TableOfContents]]
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

= Installing OpenWrt =
/!\ '''LOADING AN UNOFFICIAL FIRMWARE WILL VOID YOUR WARRANTY'''

OpenWrt is an unofficial firmware which is neither endorsed or supported by Linksys or any other vendor. OpenWrt is provided "AS IS" and without any warranty under the terms of the [http://www.gnu.org/copyleft/gpl.html GPL].

To avoid potentially serious damage to your router caused by an unbootable firmware we strongly suggest enabling a setting known as '''boot_wait'''.

== Enabling boot_wait ==

The router does not boot directly into the firmware, instead it boots into a program known as a bootloader which is responsible for initializing the hardware and loading the firmware. If the boot_wait variable is set, the bootup process is delayed by few seconds allowing a new firmware to be installed through the bootloader using tftp.

Setting of the boot_wait variable is done through a bug in the Ping.asp administration page by pinging the following "addresses": (Note that for this to work the internet port must have a valid ip address, either from dhcp or manually configured from the main page -- the port itself doesn't need to be connected)

{{{
;cp${IFS}*/*/nvram${IFS}/tmp/n
;*/n${IFS}set${IFS}boot_wait=on
;*/n${IFS}commit
;*/n${IFS}show>tmp/ping.log
}}}

When you get to the last command the ping window should be filled with a long list of variables including '''boot_wait=on''' somewhere in that list.

== Using boot_wait to upload the firmware ==

Although the firmware can be installed through more traditional means, we recommend that you use boot_wait for your first install. This will confirm boot_wait is correctly enabled and provide a firmware recovery experience without the stress of a broken router.

While in the bootloader the linksys wrt54g(s) will be forced to a lan ip of 192.168.1.1. To use the bootloader's tftp server you need to use a standard tftp client -- the tftp clients provided by linksys will not work for this. The file to be uploaded depends on the model; non linksys models take a TRX file while linksys models take a BIN file.

||'''Model'''||'''Firmware'''||
||WRT54G||openwrt-g-code.bin||
||WRT54GS||openwrt-gs-code.bin||
||(other)||openwrt-linux.trx||

The BIN file is simply a TRX with some extra information at the start to indicate the model. The only difference between openwrt-g-code.bin and openwrt-gs-code.bin is the first 4 bytes which determine the model.

To upload the firmware to a WRT54GS, unplug your box and enter the commands given would be
{{{
tftp 192.168.1.1
tftp> binary
tftp> rexmt 1
tftp> trace
Packet tracing on.
tftp> put openwrt-g-code.bin
}}}
Your output may look slightly different depending on the tftp client used. Setting "rexmt 1" will cause the tftp client to constantly retry to sent the file to the given address. While this is happening, plug your box, and as soon as bootloader's tftp client starts to listen, your client will successfully connect and send the firmware.

||'''TFTP Error'''||'''Reason'''||
||Code pattern is incorrect||The firmware image you're uploading was intended for a different model.||
||Invalid Password||The firmware has booted and you're connected to a password protected tftp server contained in the firmware, not the bootloader's tftp server.||
||Timeout||Ping to verify the router is online[[BR]]Try a different tftp client (some are known not to work properly)||

= Using OpenWrt =
Please see [:OpenWrtDocs/Using]
