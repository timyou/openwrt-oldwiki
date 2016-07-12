#acl Known:read,write All:read
##   
## Note: these pages document the firmware itself, not packages
##       questions/comments should be posted to the forum
##        
[:OpenWrtDocs]
[[TableOfContents]]
= Will OpenWrt work on my hardware ? =
See [:TableOfHardware]

= Obtaining the firmware =

'''Stable Release'''

At the moment we have no stable supported release. You can get release candidates for the next stable OpenWrt release in binary format:
[http://downloads.openwrt.org/whiterussian/ http://downloads.openwrt.org/whiterussian/]

'''Stable Source'''

If you like to get the source code and compile on your own use our CVS repository. You will need to compile this from scratch, but this is not recommended for beginners.

{{{
cvs -d:pserver:anonymous@openwrt.org:/openwrt co -rwhiterussian openwrt
}}}

'''Development'''

Development take place in CVS. We have no regularly binary snapshots, if you like to help, compile on your own. You get the source via:

{{{
cvs -d:pserver:anonymous@openwrt.org:/openwrt co openwrt
}}}

If you find any bugs, please use our forum or irc channel to report.

You may find some binary snapshots in the directories of our developers http://downloads.openwrt.org/people/


= Installing OpenWrt =
/!\ '''LOADING AN UNOFFICIAL FIRMWARE MAY VOID YOUR WARRANTY'''

OpenWrt is an unofficial firmware which is neither endorsed or supported by the vendor of your router. OpenWrt is provided "AS IS" and without any warranty under the terms of the [http://www.gnu.org/copyleft/gpl.html GPL]. You can always flash back your original firmware, so please be sure you have it downloaded and saved locally.

To avoid potentially serious damage to your router caused by an unbootable firmware you should read the documentation for your specific router model.

/!\ '''We strongly suggest you also read [:OpenWrtDocs/Troubleshooting] before installing'''

/!\ '''The jffs2 versions of  may take several minutes for the first bootup and will require a reboot before being usable'''

== General instructions ==

On most of the supported routers OpenWrt can be initially installed via Trivial File Transfer Protokoll (TFTP) with a TFTP client on your PC or Mac. 
When the device boots it runs a bootloader. It's the responsibility of this bootloader to perform basic system initialization along with validating and loading the actual firmware; think of it as the BIOS of the device before control is passed over to the operating system. Should the firmware fail to pass a CRC check, the bootloader will presume the firmware is corrupt and wait for a new firmware to be uploaded over the network. The type of the preinstalled bootloader depends on your model. Broadcom based routers use CFE - Common Firmware Environment (older Boards use PMON), Texas Instruments based routers use Adam2.  

The basic procedure of using a tftp client to upload a new firmware to your router:
  * unplug the power to your router
  * start your tftp client
    * give it the router's address (always 192.168.1.1)
    * set mode to octet
    * tell the client to resend the file, until it succeeds.
    * put the file
  * plug your router, while having the tftp client running and constantly probing for a connection
  * the tftp client will receive an ack from the bootloader and starts sending the firmware

/!\ '''Please be patient, the reflashing occurs AFTER the firmware has been transferred. DO NOT unplug the router, it will automatically reboot into the new firmware.''' 
On routers with a DMZ led, OpenWrt will light the DMZ led while booting, after bootup it will turn the DMZ led off. Sometimes automatic rebooting does not work, so you can 
safely reboot after 10 minutes.

The tftp commands might vary across different implementations. Here are two examples, netkit's tftp client and Advanced TFTP (available from: [ftp://ftp.mamalinux.com/pub/atftp/])

netkit's tftp commands:
{{{
tftp 192.168.1.1
tftp> binary
tftp> rexmt 1
tftp> timeout 60
tftp> trace
Packet tracing on.
tftp> put openwrt-xxx-x.x-xxx.bin
}}}
Setting "rexmt 1" will cause the tftp client to constantly retry to send the file to the given address. As advised above, plug in your box after typing the commands, and as soon as the bootloader starts to listen, your client will successfully connect and send the firmware. You can try to run "ping -f 192.168.1.1" (as root) in a separate window and enter the line "put openwrt-xxx-x.x-xxx.bin" as the colons stop running over your terminal when you power-recycle your router. 

Advanced TFTP commands:
{{{ 
atftp
tftp> connect 192.168.1.1
tftp> mode octet
tftp> trace
tftp> put openwrt-xxx-x.x-xxx.bin
}}}
You don't have to tell atftp to retry file sending because that's the default.

Please note, netkit tftp has failed to work for some people. Try to use Advanced TFTP. Don't forget about your firewall settings, if you use one.

||'''TFTP Error'''||'''Reason'''||
||Code pattern is incorrect||The firmware image you're uploading was intended for a different model.||
||Invalid Password||The firmware has booted and you're connected to a password protected tftp server contained in the firmware, not the bootloader's tftp server.||
||Timeout||Ping to verify the router is online[[BR]]Try a different tftp client (some are known not to work properly)||

If your computer is directly connected to the router and you are consistently getting "Invalid Password" failures, try connecting your computer and the router to a hub or switch.  Doing so will keep the link up and prevent the computer from disabling its interface while the router is off.

Windows 2000 has a TFTP server, and it [http://martybugs.net/wireless/openwrt/flash.cgi can be used] to flash with OpenWrt firmware. Note that the Windows PC needs to be configured with a static IP address in the 192.168.1.0/24 subnet, and cannot use a DHCP IP address when flashing the firmware.

== Linksys WRT54G and WRT54GS ==

The bootloader on the Linksys WRT54G and WRT54GS models, either CFE or PMON, doesn't automatically accept a firmware image via TFTP. 
The first step you need to do, is to enable boot_wait.

=== Enabling boot_wait ===

If the boot_wait variable is set, the bootup process is delayed by few seconds allowing a new firmware to be installed through the bootloader using tftp. Setting of the boot_wait variable is done through a bug in the Ping.asp administration page by pinging the certain "addresses" listed below.  '''You find ping.asp by navigating through the administration page and selecting diagnostics.'''.  

First, for this to work the '''internet port must have a valid ip address''', either from dhcp or manually configured from the main page - the port itself doesn't need to be connected unless using dhcp. Next, navigate to the Ping.asp page and enter exactly each line listed below, one line at a time into the "IP Address" field, pressing the Ping button after each entry.

/!\ '''The last versions of the firmware to support the Ping.asp bug described below are [ftp://ftp.linksys.com/pub/network/WRT54GV2_3.01.3_US_code.zip 3.01.3] for the WRT54G (up to/including v3.0) and [ftp://ftp.linksys.com/pub/network/WRT54GS_3.37.2_US_code.zip 3.37.2] for the WRT54GS (up to/including v2.0). Downgrading to these firmwares is required to enable boot_wait.'''

{{{
;cp${IFS}*/*/nvram${IFS}/tmp/n
;*/n${IFS}set${IFS}boot_wait=on
;*/n${IFS}commit
;*/n${IFS}show>tmp/ping.log
}}}

When you get to the last command the ping window should be filled with a long list of variables including '''boot_wait=on''' somewhere in that list.

This ping exploit definitely works with WRT54G v2.0, WRT54G v.2.2, WRT54GS v1.0 and WRT54GSv1.1. You must have an address on the WAN port.  In the Setup/Basic Setup/Internet Setup section you may wish to select Static IP and set IP=10.0.0.1, Mask=255.0.0.0, Gateway=10.0.0.2.  Those values are meaningless; you'll be overwriting them soon with new firmware. Note: flashing a Linksys WRT54GS v1.1 by using TFTP is only possible using the Port 1 of the switch!

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

=== Using boot_wait to upload the firmware ===

Although the firmware can be installed through more traditional means, we recommend that you use tftp for your first install. This will confirm boot_wait is correctly enabled and provide a firmware recovery experience without the stress of a broken router.

While in the bootloader the Linksys WRT54G(S) will be forced to a lan ip of 192.168.1.1. To use the bootloader's tftp server you need to use a standard tftp client -- the tftp clients provided by linksys will not work for this. The file to be uploaded depends on your model.

||'''Model'''||'''Firmware (JFFS2)'''||'''Firmware (SQUASHFS)'''||
||WRT54G||openwrt-wrt54g-jffs2.bin||openwrt-wrt54g-squashfs.bin||
||WRT54GS||openwrt-wrt54gs-jffs2.bin||openwrt-wrt54gs-squashfs.bin||


||'''LED pattern'''||'''reason'''||
||Solid power & DMZ||OpenWrt is booting or (if prolonged) has failed to boot, try [:OpenWrtDocs/Troubleshooting: failsafe mode]. (Usually caused by old/corrupt jffs2 data from a previous OpenWrt install)||
||flashing power, slow flashing dmz||Error flashing / Corrupt firmware||


== ASUS WL-500G ==

Pull the plug, press and hold the reset button, plug the device and wait until the PWR LED starts flashing slowly (almost immediately). Now release the reset button and upload the firmware by TFTP using the following commands:

TFTP commands:
{{{
tftp 192.168.1.1
tftp> binary
tftp> trace
tftp> get ASUSSPACELINK\x01\x01\xa8\xc0 /dev/null
tftp> put openwrt-xxx-x.x-xxx.trx ASUSSPACELINK
}}}

After this, wait until the PWR LED stops flashing and the device to reboot and you should be set. There's also nice shell script doing this work for you to be at [http://openwrt.org/downloads/utils/flash.sh].

As an alternative (or if this installation routine doesn't do the trick for you) you can always use the ASUS Recovery tool from your utilities CD to upload your openwrt firmware.

Another thing is that the ASUS WL500G doesn't seem to revert to the 192.168.1.1 address when starting the bootloader, but seems to use the LAN IP address set in NVRAM, so try this address or use the recovery tool if you've got problems flashing your firmware. 

== ASUS WL-500G Deluxe ==

Pull the plug, press and hold the reset button, plug the device and wait until the PWR LED starts flashing slowly (almost immediately). Now release the reset button and upload the firmware by TFTP using the following commands:

TFTP commands:
{{{
tftp 192.168.1.1
tftp> binary
tftp> trace
tftp> put openwrt-xxx-x.x-xxx.trx 
}}}

After this, wait until the PWR LED stops flashing and the device to reboot and you should be set. There's also nice shell script doing this work for you to be at [http://openwrt.org/downloads/utils/flash.sh].

As an alternative (or if this installation routine doesn't do the trick for you) you can always use the ASUS Recovery tool from your utilities CD to upload your openwrt firmware.

Another thing is that the ASUS WL500G doesn't seem to revert to the 192.168.1.1 address when starting the bootloader, but seems to use the LAN IP address set in NVRAM, so try this address or use the recovery tool if you've got problems flashing your firmware. 


== Siemens Gigaset SE505 ==

The installation procedure is essentially the same as the generic one described above. The only differences are that the bootloader listens based on nvram lan_ipaddr= variable (default: 192.168.2.1) and the IP of the machine sending the new firmware has to be 192.168.x.100 or the router will only accept the first packet.
boot_wait is enabled on these devices.

You can erase nvram settings by pressing reset button while powering on the router.

== Motorola ==

Who knows how it works on this model?

= Using OpenWrt =
Please see [:OpenWrtDocs/Using]

= Troubleshooting =
If you have any trouble flashing to OpenWrt please refer to [:OpenWrtDocs/Troubleshooting]
