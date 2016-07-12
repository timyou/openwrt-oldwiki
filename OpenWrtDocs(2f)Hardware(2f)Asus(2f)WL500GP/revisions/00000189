#pragma section-numbers off
||<tablebgcolor="#f1f1ed" tablewidth="40%" tablestyle="margin: 0pt 0pt 1em 1em; float: right; font-size: 0.9em;"style="padding: 0.5em;">[[TableOfContents]]||
== ASUS WL-500g Premium ==
With Kamikaze 7.07 and target system Broadcom BCM947xx/953xx [2.4] the ASUS WL-500g Premium is fully supported and runs stable.
||||<style="text-align: center;">'''Target System''' ||||<style="text-align: center;">'''!WiFi Support''' ||<style="text-align: center;">'''Comments''' ||
||||<style="text-align: center;"> ||'''Broadcom''' ||'''Atheros''' || ||
||||<style="text-align: center;">Broadcom BCM947xx/953xx [2.'''4'''] ||<style="text-align: center;"> (./) ||<style="text-align: center;"> {X} / (./) ||With Atheros !WiFi the router reboots in a loop (fixed for PRE-7.09 in subversion) ||
||||<style="text-align: center;">Broadcom BCM947xx/953xx [2.'''6'''] ||<style="text-align: center;"> {X} ||<style="text-align: center;"> (./) ||Random segfaults (confirmed by nbd) ||


[[Anchor(hardware)]] [[Anchor(Hardware)]]

== Hardware ==
=== Info ===
||'''Architecture''' ||MIPS ||
||'''Vendor''' ||Broadcom ||
||'''Bootloader''' ||CFE ||
||'''System-On-Chip''' ||Broadcom 5365 ||
||'''CPU Speed''' ||266 Mhz ||
||'''Flash size''' ||8MiB ||
||'''RAM''' ||32MiB (some older units have only 16MiB enabled) ||
||'''Wireless''' ||MiniPCI Broadcom 802.11b/g BCM4318 802.11 Wireless LAN Controller ||
||'''Ethernet''' ||Robo switch BCM5325 ||
||'''USB''' ||2x USB 2.0 ||
||'''Serial''' ||yes ||
||'''JTAG''' ||no ||
[[Anchor(serial)]] [[Anchor(Serial)]]

=== Serial Port ===
Serial is located on pin soldering points (ready for soldering of 8-pin connector for use with detachable cable) on the centre of the right upper side (viewing from front panel) under ventilation holes. At right from these points, you can see printed pin descriptions:
||RESET || ||
||GND ||3.3V_OUT ||
||UART_TX1 ||UART_TX0 ||
||UART_RX1 ||UART_RX0 ||


Pin 1 (with the square solder pad) is RX0.

These serial ports use TTL levels. You need an additional voltage convertor to get a standard serial port.

[[Anchor(photos)]] [[Anchor(Photos)]] [[Anchor(pics)]]

=== Photos ===
[[ImageLink(IMG_0007_thumbnail.JPG, ./OpenWrtDocs/Hardware/Asus/WL500GP/IMG_0007 )]]

=== Opening the case ===
Remove the 4 nubs under the case, now you can see some screws. Unscrew them. You're done. When you're finished you can put the rubbers back into the gadgets. They'll stick alone.

## http://wiki.openwrt.org/OpenWrtDocs/Hardware/Asus/WL500GP?action=AttachFile&do=view&target=IMG_0007.JPG&t=.jpg
== Original Firmware ==
=== Backup ===
You can backup the original firmware with the hidden admin page. This requires you to have a USB pen drive to copy the backup firmware file (TRX) of the router.

 * To create the backup you need to put a small shell script on your USB pen drive. I name the script asus.sh. The shell script has only the following two lines:
 {{{
#!/bin/sh
dd if=/dev/mtdblock/1 > $1/first_config.trx}}}
 * Connect the USB pen drive to the lower USB port on the router
 * Point your browser to the hidden admin page at http://192.168.1.1/Main_AdmStatus_Content.asp
 * In the System Command text field enter 'mount' and hit the Refresh button. Here you should see your USB pen drive's mount point. Something like:
 {{{
/dev/discs/disc0/part1 on /tmp/harddisk/part0 type ext2 (rw,sync)}}}
 * Create the backup with 'sh /tmp/harddisk/part0/asus.sh /tmp/harddisk/part0'. Enter the command in the System Command text field and hit the Refresh button. This may take up to 10-15 minutes
 * Remove the USB pen drive and check on your PC if the first_config.trx file is there
=== Restore ===
To restore the original ASUS firmware you have three options:

 * TFTP
 * mtd (from the !OpenWrt console)
 * ASUS firmware restoration tool (Windows only)
[[Anchor(install)]] [[Anchor(Install)]] [[Anchor(installation)]] [[Anchor(Installation)]]

== Installation ==
You can try the ASUS web GUI in case it works, or skip directly to the TFTP part.  If the TFTP part fails, you can try the installation with the ASUS firmware restoration tool (Windows only).

=== Using the ASUS web GUI ===
Does not work yet. The TRX utility needs a rewrite (Sep. 1st 2007, confirmed by nbd on IRC).

[[Anchor(diag)]] [[Anchor(Diag)]]

=== Using diag mode ===
To install !OpenWrt using TFTP or the ASUS firmware restoration tool you have to put the router in diag mode. To put the router in the diag mode, do this:

 * Unplug the router's power cord.
 * Connect the router's LAN1 port directly to your PC.
 * Push the black RESTORE button using a pen or such, and keep the button pushed down.
 * Plug the power on while keeping the RESTORE button pushed for few seconds.
 * If you see a slowly blinking power light, you are in diag mode.
 * Now the router should accept an image via TFTP or the ASUS firmware restoration tool.
[[Anchor(tftp)]] [[Anchor(TFTP)]]

==== TFTP ====
It is possible to install !OpenWrt using a TFTP client when the router is in diag mode.

 * Execute the TFTP commands below:
 {{{
tftp 192.168.1.1
tftp> binary
tftp> trace
tftp> put openwrt-brcm-2.4-squashfs.trx}}}
 * After the TFTP upload is complete, wait at least 6 minutes.
 * The router will reboot itself automatically after the upgrade is complete. Rebooting may take a while.
 * You are done! You should be able to telnet to your router (IP address: 192.168.1.1) and start configuring.
'''NOTES:'''

 * Netkit's tftp doesn't work quite often; use atftp.
 * After TFTP upload is complete, DON'T reboot (replug) too early! It might brick your router.
 * The ASUS WL-500g Premium does not revert to the 192.168.1.1 address when starting the CFE bootloader, but uses the LAN IP address set in NVRAM. Try this address if you have difficulties.
[[Anchor(restore)]] [[Anchor(Restore)]] [[Anchor(restoration)]] [[Anchor(Restoration)]]

==== ASUS firmware restoration tool (Windows only) ====
If you are on Windows it is recommended to use the ASUS firmware restoration tool to install !OpenWrt. The ASUS firmware restoration tool can be found on the CD. Make sure the router is in diag mode.

 * Browse the .trx file (openwrt-brcm-2.4-squashfs.trx).
 * Press Upload. The router will reboot itself automatically after the upgrade is complete. Rebooting may take a while.
 * You are done! You should be able to telnet to your router (IP address: 192.168.1.1) and start configuring.
=== Using the mtd command line tool ===
If you have already installed !OpenWrt or like to flash from any other firmware (which has the mtd tool), do this:

{{{
cd /tmp/
wget http://downloads.openwrt.org/kamikaze/7.07/brcm-2.4/openwrt-brcm-2.4-squashfs.trx
mtd write openwrt-brcm-2.4-squashfs.trx linux && reboot}}}
[[Anchor(config)]] [[Anchor(Config)]]

== ASUS WL-500g Premium specific configuration ==
=== Interfaces ===
The default network configuration is:
||<tablewidth="541px" tableheight="129px">'''Interface Name''' ||'''Description''' ||'''Default configuration''' ||
||br-lan ||LAN & !WiFi ||192.168.1.1/24 ||
||vlan0 (eth0.0) ||LAN ports || ||
||vlan1 (eth0.1) ||WAN port ||DHCP ||
||wl0/ath0 ||!WiFi ||Disabled by default ||


LAN and !WiFi is bridged to br-lan. !WiFi is disabled by default for security reasons (to prevent an open access point).

[[Anchor(failsafe)]] [[Anchor(Failsafe)]]

=== Failsafe mode ===
If you forgot your password, broken one of the startup scripts, firewalled yourself or corrupted the JFFS2 partition, you can get back in by using !OpenWrt's failsafe mode.

==== Boot into failsafe mode ====
 * Unplug the router's power cord.
 * Connect the router's LAN1 port directly to your PC.
 * Configure your PC with a static IP address between 192.168.1.2 and 192.168.1.254. E. g. 192.168.1.2 (gateway and DNS is not required).
 * Plug the power on and wait for the power LED to switch off
 * While the power LED is off press any button (RESTORE and EZSETUP will work) a few times
 * Power LED goes fast-blinking (about 1 time per second)
 * You should be able to telnet to the router at 192.168.1.1 now (no username and password)
==== What to do in failsafe mode? ====
'''NOTE:''' The root file system in failsafe mode is the SquashFS partition mounted in readonly mode. To switch to the normal writable root file system run mount_root and make any changes. Run mount_root now.

 1. Forgot/lost your password and you like to set a new one
 passwd[[BR]]
 1. Forgot the routers IP address
 uci get network.lan.ipaddr[[BR]]
 1. You accidentally run 'ipkg upgrade' or filled up the flash by installing to big packages (clean the JFFS2 partition and start over)
 mtd -r erase !OpenWrt[[BR]]
If you are done with failsafe mode power cycle the router and boot in normal mode.[[BR]]

=== Buttons ===
The ASUS WL-500g Premium has two buttons. They are RESTORE and EZSETUP. The buttons can be used with hotplug events.
||'''BUTTON''' ||'''Event''' ||
||RESTORE ||reset ||
||EZSETUP ||ses ||


ACTION: released or pressed

=== Enabling all RAM ===
On newer ASUS WL-500g Premium router's all RAM is enabled by default. If you look at "dmesg | grep Memory" command's output, you will probably see that there's only 16MiB of RAM. Specs says there should be 32MiB. To enable 32MiB change the sdram_init and sdram_ncdl NVRAM variables as showed:

{{{
nvram set sdram_init=0x0009
nvram set sdram_ncdl=0x10308
nvram commit
reboot
}}}
== Basic configuration ==
=== PPPoE ===
With Kamikaze 7.07 PPPoE works out-of-the-box. All required packages are already installed in the default image.

To configure PPPoE with UCI, do this:

{{{
uci set network.wan.proto=pppoe
uci set network.wan.username=<pppoe_psername>
uci set network.wan.password=<pppoe_password>
uci commit network && ifup wan
}}}
=== WiFi ===
==== Enable WiFi ====
===== Broadcom WiFi =====
{{{
uci set wireless.wl0.disabled=0
uci commit wireless && wifi}}}
===== Atheros WiFi =====
{{{
uci set wireless.wifi0.disabled=0
uci commit wireless && wifi}}}
[[Anchor(wpa)]] [[Anchor(WPA)]]

==== WiFi Protected Access ====
===== Broadcom WiFi =====
For Broadcom the nas package is required

{{{
ipkg install nas}}}
===== Atheros WiFi =====
For Atheros the hostapd package is required

{{{
ipkg install hostapd}}}
===== Configure WPA (PSK) =====
Configure WPA (PSK) encryption using UCI.

{{{
uci set wireless.cfg2.encryption=psk
uci set wireless.cfg2.key=<password>
uci commit wireless && wifi}}}
===== Configure WPA2 (PSK) =====
Configure WPA2 (PSK) encryption using UCI.

{{{
uci set wireless.cfg2.encryption=psk2
uci set wireless.cfg2.key=<password>
uci commit wireless && wifi}}}
[[Anchor(usb)]] [[Anchor(USB)]]

=== USB ===
USB is supported and needs a few extra packages to be installed to work probably. USB hubs are working. Active hubs with external power supply are better.

==== USB 1.1 ====
{{{
ipkg install kmod-usb-uhci-iv}}}
==== USB 2.0 ====
{{{
ipkg install kmod-usb2}}}
=== Print Server ===
Please see the PrinterSharingHowto.

== ASUS WL-500g Premium info ==
FCC ID: MSQWL500GP [https://gullfoss2.fcc.gov/prod/oet/forms/blobs/retrieve.cgi?attachment_id=640814&native_or_pdf=pdf FCC pictures] (link dead) [http://www.xbitlabs.com/articles/other/display/asus-wl500g-premium_3.html Review of the 500gP with pictures]

HardwareAcceleratedCrypto

----
 . Here are some links to forum threads related to the ASUS WL-500g Premium:
 * [http://forum.openwrt.org/viewtopic.php?id=6090 Problems with WLAN encryption]
 * [http://forum.openwrt.org/viewtopic.php?id=6071 CPU Power]
 * [http://forum.openwrt.org/viewtopic.php?id=5688 Some more compatiblity information]
 * [http://wl500g.info/forumdisplay.php?f=61 wl500g.info]
 * [http://forum.bsr-clan.de/viewtopic.php?t=8813&highlight=500 Does anyone know what exactly are the 8 (2x4) pins near the bigger capacitor on the PCB?] They are 2 serial connections
 * [http://forum.openwrt.org/viewtopic.php?id=6362 configure WAN-interface]
[[Anchor(2.6)]]

== Trunk with Kernel 2.6 ==
'''P:''' The line ''b44: eth1: BUG! Timeout waiting for bit 80000000 of register 428 to clear.'' may appear in log. ''' '''

'''S:''' As written in http://forum.openwrt.org/viewtopic.php?pid=29017 this can be fixed by editing /etc/init.d/S10boot

'''P:''' USB 1.1 devices are not recognized, USB 2.0 devices like harddrives etc. work perfectly. How come? ''' '''

'''S:''' The WL-500gP ehci-hcd module handles all USB2 transfer well, but the external ports use uhci-hcd for usb1. To make it even worse, the current trunk version has issues with this module to load but it can be fixed like mentioned in the forum http://forum.openwrt.org/viewtopic.php?id=7149. The broadcom chip seems to have a "buried" ohci controller that can not be used with the external connectors.

[[Anchor(links)]] [[Anchor(Links)]]

== External Links ==
|| '''Link''' || '''Author''' ||
|| [http://www.marcusbrutus.soho.on.net/blog/?p=67 Adding a Bluetooth PAN to the WL-500gP Wifi Router] || MarcusBrown ||
----
 . CategoryModel
