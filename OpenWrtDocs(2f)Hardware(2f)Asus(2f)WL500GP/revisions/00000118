#pragma section-numbers off
[[TableOfContents]]

== Status ==
With Kamikaze 7.07 and target system Broadcom BCM947xx/953xx [2.4] the ASUS WL-500g Premium is fully supported and runs stable.

== Hardware ==
=== Info ===
||'''Architecture''' ||MIPS ||
||'''Vendor''' ||Broadcom ||
||'''Bootloader''' ||CFE ||
||'''System-On-Chip''' ||Broadcom 5365 ||
||'''CPU Speed''' ||266 Mhz ||
||'''Flash size''' ||8 MiB ||
||'''RAM''' ||32 MiB (some older units have only 16 MiB enabled) ||
||'''Wireless''' ||MiniPCI Broadcom 802.11b/g BCM4318 802.11 Wireless LAN Controller ||
||'''Ethernet''' ||Robo switch BCM5325 ||
||'''USB''' ||2x USB 2.0 ||
||'''Serial''' ||yes ||
||'''JTAG''' ||no ||
=== Serial Port ===
Serial is located on pin soldering points (ready for soldering of 8-pin connector for use with detachable cable) on the centre of the right upper side (viewing from front panel) under ventilation holes. At right from these points, you can see printed pin descriptions:
||RESET || ||
||GND ||3.3V_OUT ||
||UART_TX1 ||UART_TX0 ||
||UART_RX1 ||UART_RX0 ||


Pin 1 (with the square solder pad) is RX0.

These serial ports use TTL levels. You need an additional voltage convertor to get a standard serial port.

=== Photos ===
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
== Installation ==
You can try the ASUS web GUI in case it works, or skip directly to the TFTP part.  If the TFTP part fails, you can try the installation with the ASUS firmware restoration tool (Windows only).

=== Using the ASUS web GUI ===
Does not work yet. The TRX utility needs a rewrite (Sep. 1st 2007, confirmed by nbd on IRC).

=== Using diag mode ===
To install !OpenWrt using TFTP or the ASUS firmware restoration tool you have to put the router in diag mode. To put the router in the diag mode, do this:

 * Connect the router's LAN1 port directly to your PC.
 * Unplug the router's power cord.
 * Push the black RESTORE button using a pen or such, and keep the button pushed down.
 * Plug the power on while keeping the RESTORE button pushed for few seconds.
 * If you see a slowly blinking power light, you are in diag mode.
 * Now the router should accept an image via TFTP or the ASUS firmware restoration tool.
==== TFTP ====
It is possible to install !OpenWrt using a TFTP client when the router is in diag mode.

 * Execute the TFTP commands below:
 {{{
tftp 192.168.1.1
tftp> binary
tftp> trace
tftp> put openwrt-brcm-2.4-squashfs.trx}}}
 * After the TFTP upload is complete, wait at least 6 minutes.
 * ASUS WL-500g Premium does not seem to reboot automatically after the upgrade is complete. You need to plug off the power, and plug it back on to make the router alive again.
 * You are done! You should be able to telnet to your router (IP address: 192.168.1.1) and start configuring.
'''NOTES:'''

 * Netkit's tftp doesn't work quite often; use atftp.
 * After TFTP upload is complete, DON'T reboot (replug) too early! It might brick your router.
 * The ASUS WL-500g Premium does not revert to the 192.168.1.1 address when starting the CFE bootloader, but uses the LAN IP address set in NVRAM. Try this address if you have difficulties.
==== ASUS firmware restoration tool (Windows only) ====
If you are on Windows it is recommended to use the ASUS firmware restoration tool to install !OpenWrt. The ASUS firmware restoration tool can be found on the CD. Make sure the router is in diag mode.

 * Browse the .trx file (openwrt-brcm-2.4-squashfs.trx).
 * Press Upload. The router will reboot itself.
 * You are done! You should be able to telnet to your router (IP address: 192.168.1.1) and start configuring.
== Asus WL500g Premium specific configuration ==
=== Interfaces ===
The default network configuration is:

||<tablewidth="541px" tableheight="129px" tablealign="">'''Interface Name'''||'''Description'''||'''Default configuration'''||
||eth0.0||LAN ports||192.168.1.1/24||
||eth0.1||WAN port||DHCP||
||eth1||WiFi||Disabled by default
||
LAN and WiFi is bridged to br-lan. WiFi is disabled by default for security reasons (to prevent an open access point).

=== Enabling all RAM ===
On newer Asus WL500g Premium routers all RAM is enabled by default.

If you look at "dmesg | grep Memory" or "free" command's output, you will probably see that there's only 16MB of RAM. Specs says there should be 32MB.

And these values defined in Asus firmware 1.9.7.2 NVRAM enable 32MB properly:

{{{
nvram set sdram_init=0x0009
nvram set sdram_ncdl=0x10308
nvram commit
reboot
}}}
== Few problems with the Asus WL500g Premium ==
With Kamikaze 7.07 and WhiteRussian 0.9 and later (Kernel 2.4) the buttons working correctly.

The reset button does not work (due largely to mis-mapped /proc/sys/reset)

[wiki:WikiPedia:GPIO gpio] 0 = RESTORE button (reset) (00 = unpressed, 01 = pressed)

gpio 1 = Power LED (enable = off, disable = on)

gpio 4 = EZ SETUP button (similar to linksys "button"?) (00 = unpressed, 01 = pressed)

----
=== PPPoE ===
With firmware version 0.9 PPPoE works out of the box. The following problems affect older firmware versions. VespaTS: Couldn't get WikiPedia:PPPoE to work. To get PPPoE running I had to change again some settings:

wan_device=eth0 (it was set to vlan1)

But probably better is to make vlan1 working (see above and below).

Could an experienced Asus WL500g Premium user update [:OpenWrtDocs/Configuration#NetworkInterfaceNames:this table]?

The above does not work for me (on a clean OpenWrt squashfs firmware), I've to use these setting after configure in the web ui:

/!\ '''Note:''' You may want to do a 'ifdown wan' first, to suppress pppd messages.

{{{
nvram set wan_ifname=ppp0
nvram set pppoe_ifname=vlan1
nvram set wan_device=vlan1}}}
With WhiteRussian RC6, it's sufficient to set (you still have to make vlan1 working - see above):

{{{
nvram set pppoe_ifname=vlan1}}}
=== DHCP server & client settings ===
To act as a DHCP client towards WAN set the following:

{{{
nvram set wan0_proto=dhcp
nvram set wan_proto=dhcp
nvram commit}}}
To act as a DHCP server towards LAN set the following:

{{{
nvram set default_lan_proto=dhcp_server
nvram set lan_dhcp=1
nvram set dhcp_enable_x=1
nvram commit}}}
These settings are optional and not necessary for DHCP to function:

{{{
# to set DHCP IP address pool begin at 192.168.1.222
nvram set dhcp1_start=192.168.1.222
nvram set dhcp_start=222
# to set DHCP IP address pool end at 192.168.1.254
nvram set dhcp1_end=192.168.1.254
nvram set dhcp_end=254
nvram set dhcp_lease=86400 # DHCP lease time 86400 in seconds( use h=hours, m=minutes: example 2h)
nvram commit}}}
To act as a DHCP server towards WiFi set the following:

{{{
nvram set wifi_proto=dhcp
nvram commit}}}
=== Installing WiFi Protected Access (WPA) ===
By default in de WhiteRussian V0.9 the WPA was available on the web console, but was not installed. It took me some time to find it. This because the Wifi could connected with WPA-PSK, WPA1 and RC4 (TKIP) and everything looks ok. Only the DHCP server did not give me an IP address. To install WPA, look at

http://wiki.openwrt.org/Faq#head-241867b49a4ff86751c7a12f3120a47bd939b10e

or

http://wiki.openwrt.org/Faq How do I use WiFi Protected Access (WPA)?

== Asus WL500g Premium info ==
FCC ID: MSQWL500GP [https://gullfoss2.fcc.gov/prod/oet/forms/blobs/retrieve.cgi?attachment_id=640814&native_or_pdf=pdf FCC pictures] (link dead) [http://www.xbitlabs.com/articles/other/display/asus-wl500g-premium_3.html Review of the 500gP with pictures]

HardwareAcceleratedCrypto

----
 . Here are some links to forum threads related to the Asus WL500g Premium:
 * [http://forum.openwrt.org/viewtopic.php?id=6090 Problems with WLAN encryption]
 * [http://forum.openwrt.org/viewtopic.php?id=6071 CPU Power]
 * [http://forum.openwrt.org/viewtopic.php?id=5688 Some more compatiblity information]
 * [http://wl500g.info/forumdisplay.php?f=61 wl500g.info]
 * [http://forum.bsr-clan.de/viewtopic.php?t=8813&highlight=500 Does anyone know what exactly are the 8 (2x4) pins near the bigger capacitor on the PCB?] They are 2 serial connections
 * [http://forum.openwrt.org/viewtopic.php?id=6362 configure WAN-interface]
== Trunk with Kernel 2.6 ==
'''P:''' The line ''b44: eth1: BUG! Timeout waiting for bit 80000000 of register 428 to clear.'' may appear in log. ''' '''

'''S:''' As written in http://forum.openwrt.org/viewtopic.php?pid=29017 this can be fixed by editing /etc/init.d/S10boot

'''P:''' USB 1.1 devices are not recognized, USB 2.0 devices like harddrives etc. work perfectly. How come? ''' '''

'''S:''' The WL-500gP ehci-hcd module handles all USB2 transfer well, but the external ports use uhci-hcd for usb1. To make it even worse, the current trunk version has issues with this module to load but it can be fixed like mentioned in the forum http://forum.openwrt.org/viewtopic.php?id=7149. The broadcom chip seems to have a "buried" ohci controller that can not be used with the external connectors.

----
 . CategoryModel
