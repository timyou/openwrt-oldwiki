#acl Known:read,write All:read
[:OpenWrtDocs]
= Obtaining the firmware =

'''Compiled binaries'''

Compiled snapshots of the firmware can be obtained from http://openwrt.org/downloads/snapshots/

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

To avoid potentially serious damage to your router we strongly enabling a setting known as '''boot_wait'''.

'''Setting boot_wait'''

The router does not boot directly into the firmware, instead it boots into a program known as a bootloader which is responsible for initializing the hardware and loading the firmware. If the boot_wait variable is set, the bootup process is delayed by few seconds allowing a new firmware to be installed through the bootloader using tftp.

Setting of the boot_wait variable is done through a bug in the Ping.asp administration page by pinging the following "addresses":

(Note that for this to work the internet port must have a valid ip address, either from dhcp or manually configured from the main page.)

{{{
;cp${IFS}*/*/nvram${IFS}/tmp/n
;*/n${IFS}set${IFS}boot_wait=on
;*/n${IFS}commit
;*/n${IFS}show>tmp/ping.log
}}}

When you get to the last command the ping window should be filled with a long list of variables including '''boot_wait=on''' somewhere in that list.

= To be written =

(The rest of this document has yet to be written)
