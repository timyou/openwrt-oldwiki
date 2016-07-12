#acl Known:read,write All:read
##
## Note: these pages document the firmware itself, not packages
##       questions/comments should be posted to the forum
##
OpenWrtDocs [[TableOfContents]]

= Introduction =
----------

!OpenWrt is free software, provided AS-IS under the terms of the GNU General Public License. Users are expected to have working knowledge of the GNU/Linux command line and basic networking concepts. Support may be provided on a voluntary basis by developers and fellow users, but support is not guaranteed.. 

/!\ '''WARNING  LOADING AN UNOFFICIAL FIRMWARE WILL VOID YOUR WARRANTY''' /!\


----------
= Will OpenWrt work on my hardware? =
See TableOfHardware.

= Obtaining the firmware =
'''Stable Release'''

You can get the latest OpenWrt White Russian at: http://downloads.openwrt.org/whiterussian/

Please test our release candidates and report back any problems, so that we can actually release OpenWrt 1.0. 

There are different pre-compiled firmware images for every supported router model in these folders:

||'''Folder''' ||'''Description''' ||'''Package list''' ||
||bin=default ||standard image with pppoe and webif||base-files, base-files-brcm, bridge, busybox, dnsmasq, dropbear, haserl, ipkg, iptables, iwlib, kmod-switch, kmod-brcm-wl, kmod-diag, kmod-ppp, kmod-pppoe, kmod-wlcompat, mtd, nvram, ppp, ppp-mod-pppoe, uclibc, webif, wificonf, wireless-tools||
||micro ||the minimal set of packages no webif||base-files, base-files-brcm, bridge, busybox, dnsmasq, dropbear, ipkg-sh, iptables, iwlib, kmod-switch, kmod-brcm-wl, kmod-diag, kmod-wlcompat, mtd, nvram, uclibc, wificonf||
||pptp ||standard image with pptp and webif ||base-files, base-files-brcm, bridge, busybox, dnsmasq, dropbear, haserl, ipkg, iptables, iwlib, kmod-switch, kmod-brcm-wl, kmod-diag, kmod-ppp, kmod-gre, kmod-wlcompat, mtd, nvram, ppp, pptp, uclibc, webif, wificonf, wireless-tools||

You can choose between two different types of firmware images, squashfs or JFFS2 root filesystem. Squashfs does higher compression, but is read-only. If you choose this image type, you can not update any base packages without reflashing or loosing of a lot of space. The rest of the flash will be used for a writable JFFS2 filesystem. JFFS2 does not compress as well as squashfs, but you have 
a complete writable root filesystem. It is your choice!  

. /!\ '''WARNING  !OpenWrt White Russian prior rc5 has no failsafe mode for JFFS2 firmware images.''' /!\

Choose the right firmware image for your router model and installation method, xxxx stands for the root filesystem type.

Installation via Webupgrade of the original firmware:
||'''Filename'''||'''Models'''||
||openwrt-brcm-2.4-xxxx-4MB.trx||Asus WL500g, Asus WL500gx, Buffalo AirStation WBR2-G54S||
||openwrt-wrt54g-xxxx.bin||Linksys WRT54G (v1.0,v1.1,v2.0,v2.2,v3,v4)||
||openwrt-wrt54gs-xxxx.bin||Linksys WRT54GS (v1.0, v1.1, v2, v3)||
||openwrt-wrt54gs_v4-xxxx.bin||Linksys WRT54GS v4||
||openwrt-wrtsl54gs-xxxx.bin||Linksys WRTSL54GS||
||openwrt-wa840g-xxxx.bin||Motorola WA840g||
||openwrt-we800g-xxxx.bin||Motorola WE800g||
||openwrt-wr850g-xxxx.bin||Motorola WR850g||


After downloading the firmware image you should make sure that the file is not corrupt. This can be verified by comparing the md5sum from your downloaded image with the md5sum listed in the [http://downloads.openwrt.org/whiterussian/newest/default/md5sums md5sums] file found in the download directory. For win32 platforms use [http://www.pc-tools.net/win32/ md5sums.exe] for GNU/Linux systems use the {{{md5sum}}} command.

'''Getting the buildsystem'''

Take a look at our development platform at http://dev.openwrt.org/

= Installing OpenWrt =
/!\ '''LOADING AN UNOFFICIAL FIRMWARE WILL VOID YOUR WARRANTY'''

!OpenWrt is an unofficial firmware which is neither endorsed or supported by the vendor of your router. OpenWrt is provided "AS IS" and without any warranty under the terms of the [http://www.gnu.org/copyleft/gpl.html GPL]. You can always flash back your original firmware, so please be sure you have it downloaded and saved locally.

To avoid potentially serious damage to your router caused by an unbootable firmware you should read the documentation for your specific router model.

/!\ '''We strongly suggest you also read ["OpenWrtDocs/Troubleshooting"] before installing'''

== General instructions (router specific instructions later) ==

Although you can install the firmware  through more traditional means (via webpage), we recommend that you use TFTP for your first install. This is '''NOT''' a requirement, simply a damned good idea; if anything goes wrong you can just TFTP the old firmware back.

When the device boots it runs a bootloader. It's the responsibility of this bootloader to perform basic system initialization along with validating and loading the actual firmware; think of it as the BIOS of the device before control is passed over to the operating system. Should the firmware fail to pass a CRC check, the bootloader will presume the firmware is corrupt and wait for a new firmware to be uploaded over the network. The type of the preinstalled bootloader depends on your model. Broadcom based routers use CFE - Common Firmware Environment (older Boards use PMON), Texas Instruments based routers use ["ADAM2"].

The basic procedure of using a tftp client to upload a new firmware to your router:

 * unplug the power to your router
 * start your tftp client
  * give it the router's address (usually 192.168.1.1)
  * set mode to octet
  * tell the client to resend the file, until it succeeds.
  * put the file
 * plug your router, while having the tftp client running and constantly probing for a connection
 * the tftp client will receive an ack from the bootloader and starts sending the firmware

/!\ '''Please be patient, the reflashing occurs AFTER the firmware has been transferred. DO NOT unplug the router, it will automatically reboot into the new firmware.'''

On routers with a DMZ LED, !OpenWrt will light the DMZ LED while booting, after the bootup scriptes are finished it will turn off the DMZ LED. Sometimes automatic rebooting does not work, so you can safely reboot (power cycle) after waiting 5 minutes.

The TFTP commands vary across different implementations. Here are two examples, netkit's TFTP client and Advanced TFTP.  (Note that Advanced TFTP used to be available from ftp://ftp.mamalinux.com/pub/atftp/ but that server seems to have gone offline permanently.  Please post another source for it if you know where one is!)

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

Note: for some versions of the CFE bootloader, the last line may need to be "put openwrt-xxx-x.x-xxx.bin code.bin".

Advanced TFTP commands:

{{{
atftp
tftp> connect 192.168.1.1
tftp> mode octet
tftp> trace
tftp> timeout 1
tftp> put openwrt-xxx-x.x-xxx.bin

Or use the command-line:
atftp --trace --option "timeout 1" --option "mode octet" --put --local-file openwrt-xxx-x.x-xxx.bin 192.168.1.1
}}}

MacTFTP Client commands: (For use with OS X. tftp in terminal did not work for me)

{{{
Download MacTFTP Client [http://www.mactechnologies.com/pages/downld.html] 
 * Choose Send
 * Address: 192.168.1.1
 * Choose the openwrt-xxx-x.x-xxx.bin file
 * Click on start while applying power to the WRT54G
}}}

Another MacOS X note: I was able to get OS X to use tftp to flash a WRT54G V2. The trick seems to be that OS X takes a a few seconds to configure the network connection when the router is powered on. My fix was to configure the Ethernet tab of 'built-in ethernet' (System Prefences, Network) to:

 * Configure: Manual (Advanced)
 * Speed: 10 BaseT/UTP
 * Duplex: full-duplex

This seems to reduce the startup time of the ethernet port. On the second try the TFTP methode worked (where the 10+ tries before the fix did not). I also disabled the AirPort during this procedure.

Please note, netkit tftp has failed to work for some people. Try to use Advanced TFTP. Don't forget about your firewall settings, if you use one. It is best to run the "put" command and then immediately apply power to the router, since the upload window is extremely short and very early in boot.

||'''TFTP Error''' ||'''Reason''' ||
||Code pattern is incorrect ||The firmware image you're uploading was intended for a different model. ||
||Invalid Password ||The firmware has booted and you're connected to a password protected tftp server contained in the firmware, not the bootloader's tftp server. ||
||Timeout ||Ping to verify the router is online[[BR]]Try a different tftp client (some are known not to work properly) ||


Some machines will disable the ethernet when the router is powered off and not enable it until after the router has been powered on for a few seconds. If you're consistantly getting "Invalid Password" failures try connecting your computer and the router to a hub or switch. Doing so will keep the link up and prevent the computer from disabling its interface while the router is off.

Windows 2000 and Windows XP have a built-in TFTP client and it [http://martybugs.net/wireless/openwrt/flash.cgi can be used] to flash with !OpenWrt firmware.

'''Important:''' If you have a personal firewall, make sure it is disabled for this part. Some personal firewalls will not give any indication that they have blocked the tftp client. Please bear in mind that you should only be connected to the router when your personal firewall is disabled to avoid any nastiness, and remember to re-enable it when you are done.

Windows 2000/XP TFTP Client short Instructions

 * Open two command windows (Start-Run-Enter "cmd")
 * In one window, type "ping -t 192.168.1.1" and press enter. 192.168.1.1 is the router IP.
 * Ping will continuously try to contact the wrt. Keep this running
 * In the other window, prepare the tftp command "tftp -i 192.168.1.1 PUT OpenWrt-gs-code.bin". Do not press enter yet!
 * Now you may plug in the router (unplug it first if it was plugged).
 * In the ping window it will start saying "Hardware Error"
 * Return to the tftp window. As soon as the ping window starts to answer again, press enter in the tftp window.
 * The image should now be flashed without multiple tries.
 * If ping starts with "Hardware Error", then starts to answer, and then returns to  "Hardware Error" again for a short moment, you waited too long.

== Linksys WRT54G and WRT54GS ==

To use the TFTP method above you need to enable boot_wait. Plug your ethernet cable into one of the LAN ports.  Once enabled, the router will wait for ~3 seconds for a firmware before booting. While in boot_wait the router is '''always 192.168.1.1, regardless of configuration''' --  you'll have to force your computer to use 192.168.1.x (netmask 255.255.255.0) address for the purpose of reflashing. Also be sure the 192.168.1.x subnet is connected to LAN port 1 of the router.

/!\ '''Do not use the Linksys TFTP program. IT WILL NOT WORK.'''

||'''Model''' ||'''Firmware (SquashFS)''' ||'''Firmware (JFFS2)''' ||
||WRT54G ||openwrt-wrt54g-squashfs.bin ||openwrt-wrt54g-jffs2.bin ||
||WRT54GS ||openwrt-wrt54gs-squashfs.bin ||openwrt-wrt54gs-jffs2.bin ||


SquashFS files:

 . The firmwares with "squashfs" in the filename use a combination of a readonly SquashFS partition and a writable JFFS2 partition. This gives you a /rom with all the files that shipped with the firmware and a writable root containing symlinks to /rom. This is considered the standard install. Note that this image has almost the same functionality as JFFS2 image and is much more secure.

JFFS2 files:

 . The firmwares with "jffs2" in the name are JFFS2 only; all of the files are fully writable. The "4M" and "8M" in the filenames is a reference to the flash block size; most 4M flash chips use a block size of 64k while most 8M chips tend to use a 128k block size -- there are some exceptions. The JFFS2 partition needs to be formatted for the correct block size and hence the two versions. The JFFS2 versions are for experienced users only -- these firmwares only have minimal support for failsafe mode.

For more information, see the [http://downloads.openwrt.org/whiterussian/00-README 00-README] file that comes with the release.

=== Enabling boot_wait ===
If the boot_wait variable is set, the bootup process is delayed by few seconds allowing a new firmware to be installed through the bootloader using tftp. Setting of the boot_wait variable is done through a bug in the Ping.asp administration page by pinging the certain "addresses" listed below.  '''You find ping.asp by navigating through the administration page and selecting diagnostics.'''.

First, for this to work the '''internet port must have a valid ip address''', either from DHCP or manually configured from the main page - the port itself doesn't need to be connected unless using dhcp. Next, navigate to the Ping.asp page and enter exactly each line listed below, one line at a time into the "IP Address" field, pressing the Ping button after each entry.

;*/n${IFS}set${IFS}boot_wait=on
;*/n${IFS}commit
;*/n${IFS}show>tmp/ping.log
}}}

When you get to the last command the ping window should be filled with a long list of variables including '''boot_wait=on''' somewhere in that list.

This ping exploit definitely works with ALL WRT54G/GS VERSIONS. You must have an address on the WAN port. In the Setup/Basic Setup/Internet Setup section you may wish to select Static IP and set IP=10.0.0.1, Mask=255.0.0.0, Gateway=10.0.0.2. Those values are meaningless; you'll be overwriting them soon with new firmware. Note: flashing a Linksys WRT54GS v1.1 by using TFTP is only possible using the Port 1 of the switch!

You can also use the [https://aachen.uni-dsl.de/download/wrt/Snapshots/rev121/buildroot-rev121/takeover takeover] script to make ping hack in a single command (need a shell command line interpreter). This script expects to find the to-be flashed firmware in a file called '''openwrt-g-code.bin''', which is in the ''current'' directory.

There is another bug still present in Ping.asp (firmware revision 3.03.1) where you can put your shell code into the ping_times variable. See http://www.linksysinfo.org/modules.php?name=Forums&file=viewtopic&t=448 This means you don't have to downgrade your firmware first and it removes the input size restrictions so you can use more obvious shell commands like:

{{{
`/usr/sbin/nvram set boot_wait=on`
`/usr/sbin/nvram commit`
`/usr/sbin/nvram show > /tmp/ping.log`
}}}

For instance, if you are in Unix and have Perl and LWP installed, you may issue this command:

{{{
echo 'submit_button=Ping&submit_type=start&action=Apply&change_action=gozila_cgi&ping_ip=10.0.0.1&ping_times=`/usr/sbin/nvram show > /tmp/ping.log`'|POST -C admin:admin http://192.168.1.1/apply.cgi
}}}

=== Setting boot_wait from a serial connection ===
With a serial connection to your WRT, you don't have to use the ping bug or change your Linksys firmware. You can set boot_wait from the console, using the commands

{{{
#nvram set boot_wait=on
#nvram get boot_wait           (just to confirm, should respond with "on")
#nvram commit                  (takes a few seconds to complete)
}}}

You can also set boot_wait from the CFE boot loader (to enter CFE, reboot the router with "# reboot" while hitting {{{CTRL-C}}} continously)

{{{
CFE> nvram set boot_wait=on
CFE> nvram get boot_wait       (just to confirm, should respond with "on")
CFE> nvram commit              (takes a few seconds to complete)
}}}

== ASUS WL-HDD, WL-500G and WL-300G ==
Pull the plug, press and hold the reset button, plug the device and wait until the PWR LED starts flashing slowly (almost immediately). Now release the reset button and upload the firmware by TFTP using the following commands:

TFTP commands:

{{{
tftp 192.168.1.1
tftp> binary
tftp> trace
tftp> get ASUSSPACELINK\x01\x01\xa8\xc0 /dev/null
tftp> put openwrt-xxx-x.x-xxx.trx ASUSSPACELINK
}}}

After this, wait until the PWR LED stops flashing and the device to reboot and you should be set. There's also nice shell script doing this work for you to be at http://openwrt.org/downloads/utils/flash.sh.

As an alternative (or if this installation routine doesn't do the trick for you) you can always use the ASUS Recovery tool from your utilities CD to upload your !OpenWrt firmware.

Another thing is that the ASUS [:OpenWrtDocs/Hardware/Asus/WL500G:WL-500G]/[:OpenWrtDocs/Hardware/Asus/WL300G:WL-300G] doesn't seem to revert to the 192.168.1.1 address when starting the bootloader, but seems to use the LAN IP address set in NVRAM, so try this address or use the recovery tool if you've got problems flashing your firmware.

There are several helpful tutorials especially for the ASUS routers at http://www.macsat.com.

== ASUS WL-500G Deluxe ==
This device is based on the Broadcom chipset so the openwrt-brcm-x image is required.

Enable '''Failure Mode''' - remove the power, press and hold the reset button while returning power. Within a few seconds the PWR LED starts flashing slowly (once second on, one second off). Release the reset button and continue.

You should be able to ping the unit:

{{{
ping 192.168.1.1
}}}

/!\ Note, the ASUS WL-500GD doesn't revert to the 192.168.1.1 address when starting the bootloader, but uses the LAN IP address set in NVRAM. Try this address if you have difficulties.

(!) If you can’t ping the unit retry enabling "'Failure Mode'", even if the LED is blinking it sometimes does not respond. Turn it off and then on first. You can even do a factory reset.

=== Send image with TFTP ===
{{{
tftp 192.168.1.1
tftp> binary
tftp> trace
tftp> get ASUSSPACELINK\x01\x01\xa8\xc0 /dev/null
tftp> put openwrt-xxx-x.x-xxx.trx ASUSSPACELINK
}}}

After this, wait for the PWR LED to stop flashing and the device to reboot and you should be set. There's also nice shell script to do this work for you at http://openwrt.org/downloads/utils/flash.sh. This script is also included in the source under scripts/flash.sh.

(!) Some devices don't require you to download the firmware first (in fact, it doesn't work at all). So don't worry if the router won't reply to the {{{get}}} but accepts the {{{put}}}. You can even leave out the {{{ASUSSPACELINK}}}. For some reason though, the device doesn't reboot after flashing. Just wait a little, unplug the power and reconnect. After a while (1-2 minutes), the WLAN LED should light and OpenWRT is up and running.

=== Send image with Firmware Restoration technique ===
You can use the ASUS Firmware Restoration tool to send am image from a Windows PC to the router (including OpenWrt). The tool is on the supplied CD or available from the ASUS web site.

/!\ Before you start the Firmware Restoration tool, disable all interfaces on the PC except for the one connected to the Router. The software seems to pick an interface at random.

Put the Router in '''Failure Mode''' (see above) and start the '''Firmware Restoration''' program. Select the desired firmware and click on Upload. The software will search for the router - the status is ''Connect to the wireless device'', it will do this for about 32 seconds.

/!\ The software will only find the router if it is in recovery mode.

The tool provides status as it works:

 * Uploading (LAN interface LED blinks during transfer)
 * Recovery is in progress
 * Success

After this you should be able to connect to the Router.

== Siemens Gigaset SE505 ==
The installation procedure is essentially the same as the generic one described above. The only differences are that the bootloader listens based on nvram lan_ipaddr= variable (default: 192.168.2.1) and the IP of the machine sending the new firmware has to be 192.168.x.100 or the router will only accept the first packet. boot_wait is enabled by default on these devices.

You can erase nvram settings by pressing reset button while powering on the router.

== Motorola WR850G ==
Flashing the Motorola ["OpenWrtDocs/Hardware/Motorola/WR850G"] is fairly easy. Just follow these easy steps!

 1. Use the web interface to set the router's IP address to 192.168.1.1. This will mitigatethe issue where dnsmasq doesn't properly read the subnet from the configuration.
 1. Download the motorola firmware image (either the squashfs or the jffs2-8mb version) from the website. (Note: The motorola has 4mb flash, but requires the 8mb version.  This is due to the paging size of the flash rom that is used, and is not related to the ignominously confusing names used for the files.  At the moment the motorola-jffs2-4mb is entirely useless [64k page size, 8mb is 128k page size].)
 1. Change the extension of the firmware image to .trx, because the Motorola web interface will not accept files with different extensions.
 1. Use the Control Panel -> Firmware page of the Motorola web interface to upload !OpenWrt. The power light on the WR850G will flash between red and green.  DO NOT INTERRUPT THE POWER TO THE WR850G WHILE THIS IS HAPPENING. Doing so has been shown by the state of California to cause birth defects such as low birth weight, miscarriage, and the Black Lung.
 1. You will receive a message in your browser telling you the flash is complete and that you should restart the router.  Do so, either using the web interface or power cycling the router.
 1. When you're finished, telnet to 192.168.1.1, issue the 'reboot' command if you're using jffs2, and change your password to activate dropbear.
 1. If you're having trouble getting an IP, try setting your IP manually to 192.168.1.2.  Sometimes dnsmasq doesn't work properly with the WR850G routers. An nvram reset ((('mtd erase nvram; reboot'))) may solve this issue (Note: erasing nvram resets the router's IP to 192.168.10.1) /!\ '''NOTE:''' user reports that v2 resets the router's IP to 192.168.1.1

/!\ '''If you're using TFTP to flash the firmware, put to the host 192.168.10.1.''' /!\ '''I left the host as 192.168.10.1 and it was fine on my WRT850G V2.'''

== Buffalo Airstation WLA-G54 ==
This device is based on the Broadcom chipset so the openwrt-brcm-x image is required. The web interface will not allow you to install the openwrt firmware so you will need to use tftp. Pull the power plug, press and hold the reset button, plug the device and wait until the PWR LED starts flashing slowly (almost immediately). Now release the reset button and upload the firmware. This unit keeps the IP address that it was set to whilst in this mode. Factory setting is 192.168.11.2.

TFTP commands:

{{{
tftp 192.168.11.2
tftp> binary
tftp> trace
tftp> rexmt 1
tftp> timeout 60
tftp> put openwrt-xxx-x.x-xxx.trx
}}}

After this, wait until the PWR LED stops flashing and the device to reboot and you should be set. You should be able to telnet to 192.168.11.2 or whatever the unit was set to prior to the installation.

'''Does not work on the Buffalo WLA2-G54C. The boot loader keeps the ip set before uploading OpenWrt so was able to TFTP the Buffalo firmware back after removing the relevant parts in a hex editor.'''

WLA2-G54C has the following chips inside, Broadcom BCM4712KPB, Intel TE28F320 flash.

I tried the openwrt-brcm-2.4-squashfs.trx file which I presume is the correct one.


== Buffalo AirStation WBR2-G54S ==
Here too you need an openwrt-brcm-*.trx image. The device has boot_wait=on by default, so you can just begin sending the file from your TFTP client, power up the device, and let it install. The TFTP loader uses the IP address to which you've configured the device; 192.168.11.1 by default.  If you ping the device, the TFTP loader will respond with TTL=100, but both the Buffalo firmware and !OpenWrt will respond with TTL=64.

The firmware provided by Buffalo has some extra headers at the beginning.  If you load it via TFTP, you must first remove the extras so that the file begins with "HDR0". Otherwise, it won't boot (but you can still replace it via TFTP).

With the Buffalo firmware (at least version 2.30), if you save the settings to a file, it will obfuscate the output by inverting each bit.  To undo this and see the NV-RAM settings, filter the file through: perl -pe 's/(.)/chr(ord($1)^0xFF)/seg; tr/\0/\n/'

= Using OpenWrt =
See ["OpenWrtDocs/Using"].

= Troubleshooting =
If you have any trouble flashing to !OpenWrt please refer to ["OpenWrtDocs/Troubleshooting"].
