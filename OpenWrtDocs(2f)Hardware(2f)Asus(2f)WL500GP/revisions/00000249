#pragma section-numbers off
||<tablebgcolor="#f1f1ed" tablewidth="40%" tablestyle="margin: 0pt 0pt 1em 1em; float: right; font-size: 0.9em;"style="padding: 0.5em;">[[TableOfContents]]||
== ASUS WL-500g Premium ==
With Kamikaze 7.09 and target system Broadcom BCM947xx/953xx [2.4] the ASUS WL-500g Premium is fully supported and runs stable.
||||<style="text-align: center;">'''Target System''' ||||<style="text-align: center;">'''!WiFi Support''' ||<style="text-align: center;">'''Comments''' ||
||||<style="text-align: center;"> ||'''Broadcom''' ||'''Atheros''' || ||
||||<style="text-align: center;">Broadcom BCM947xx/953xx [2.'''4'''] ||<style="text-align: center;"> (./) ||<style="text-align: center;"> (./) || ||
||||<style="text-align: center;">Broadcom BCM947xx/953xx [2.'''6'''] ||<style="text-align: center;"> {X} ||<style="text-align: center;"> (./) ||Random segfaults -- [https://dev.openwrt.org/changeset/9285 Fixed in SVN 9285] ||


[[Anchor(hardware)]] [[Anchor(Hardware)]]

== Hardware ==
=== Info ===
||'''Architecture''' ||MIPS ||
||'''Vendor''' ||Broadcom ||
||'''Bootloader''' ||CFE ||
||'''System-On-Chip''' ||Broadcom BCM94704 ||
||'''CPU Speed''' ||266 Mhz ||
||'''Flash size''' ||8MiB ||
||'''RAM''' ||32MiB (some older units have only 16MiB enabled) ||
||'''Wireless''' ||MiniPCI Broadcom 802.11b/g BCM4318 802.11 Wireless LAN Controller ||
||'''Ethernet''' ||Robo switch BCM5325 ||
||'''USB''' ||2x USB 2.0 ||
||'''Serial''' ||Yes ||
||'''JTAG''' ||No ||
[[Anchor(serial)]] [[Anchor(Serial)]]

=== Wireless LAN Controller ===
The standard wireless LAN controller is the BCM4318 on a MiniPCI card.  Some people have replaced this with an Atheros MiniPCI card.  The advantage is that the Atheros card has an open source driver. For example it works with Wistron CM9 (some people say that signal quality is poor), Tp-Link TL-WN560G (signal quality is as with original controller).

=== Serial Port ===
Serial is located on pin soldering points (ready for soldering of 8-pin connector for use with detachable cable) on the centre of the right upper side (viewing from front panel) under ventilation holes. At right from these points, you can see printed pin descriptions:
||RESET || ||
||GND ||3.3V_OUT ||
||UART_TX1 ||UART_TX0 ||
||UART_RX1 ||UART_RX0 ||


Pin 1 (with the square solder pad) is RX0.

These serial ports use TTL levels. You need an additional voltage convertor to get a standard serial port. The parameters are 115200 baud and 8-n-1.

[[Anchor(photos)]] [[Anchor(Photos)]] [[Anchor(pics)]]

=== Photos ===
[[ImageLink(IMG_0007_thumbnail.JPG, ./OpenWrtDocs/Hardware/Asus/WL500GP/IMG_0007 )]][[BR]] With a Atheros Wistron CM9[[BR]] MiniPCI !WiFi card

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
 * Create the backup with 'sh /tmp/harddisk/part0/asus.sh /tmp/harddisk/part0'. Enter the command in the System Command text field and hit the Refresh button. This may take up to 10-15 seconds.
 * You can enter in the System Command text field 'ls -l ''''''/tmp/harddisk/part0' and see your first_config.trx file.
 * Remove the USB pen drive and check on your PC if the first_config.trx file is there
=== Restore ===
To restore the original ASUS firmware you have three options:

 * TFTP
 * mtd (from the !OpenWrt console)
 * ASUS firmware restoration tool (Windows only)
[[Anchor(install)]] [[Anchor(Install)]] [[Anchor(installation)]] [[Anchor(Installation)]]

== Installation ==
If the TFTP part fails, you can try the installation with the ASUS firmware restoration tool (Windows only).

You can download [http://downloads.openwrt.org/kamikaze/7.09/ official 7.09] images or build the images by yourself using the build-system.

=== Using the ASUS web GUI ===
Does not work yet. The TRX utility needs a rewrite (Sep. 1st 2007, confirmed by nbd on IRC).

The ASUS GUI requires a trailer to be added to the .trx file (similar to the way other firmwares require headers).  The rather simple structure can be inferred from work done for the FreeWRT project http://osdir.com/ml/embedded.freewrt.cvs/2006-09/msg00226.html

[[Anchor(diag)]] [[Anchor(Diag)]]

=== Using diag mode ===
To install !OpenWrt using TFTP or the ASUS firmware restoration tool you have to put the router in diag mode. To put the router in the diag mode, do this:

 * Unplug the router's power cord.
 * Confirm your PC is configured to request an address via DHCP.
 * Connect the router's LAN1 port directly to your PC.
 * Push the black RESTORE button using a pen or such, and keep the button pushed down.
 * Plug the power on while keeping the RESTORE button pushed for few seconds.
 * When you see a slowly blinking power light, you are in diag mode.
 * Now the router should accept an image via TFTP or via the ASUS firmware restoration tool.
[[Anchor(tftp)]] [[Anchor(TFTP)]]

In diag mode, the router takes address 192.168.1.1. It responds to ping, so you can confirm that it is in diag mode and ready for the tftp by using "ping 192.168.1.1".

Note: I used the Asus tool to reflash the orginal asus firmware over kamikaze 7.09.  In diag mode the asus kept the IP address assigned to it in kamikaze, which was not 192.168.1.1.  The asus firmware restoration tool worked even though the asus in diag mode did not assign my PC an IP via DHCP and even though I could not ping the asus at 192.168.1.1.  I had to use ethereal/wireshark to monitor traffic on LAN1 to figure out what I had set the IP address to.  Then, using the proper IP address I could access the stock Asus web pages to use the "Reset to Factory Default" function and restore all settings to factory state.

==== TFTP ====
It is possible to install !OpenWrt using a TFTP client when the router is in diag mode.

 * Execute the TFTP commands below:
 {{{
tftp 192.168.1.1
tftp> binary
tftp> trace
tftp> put openwrt-brcm-2.4-squashfs.trx}}}
 * After the TFTP upload is complete, wait at least six minutes. The firmware is first loaded into the RAM, and then flashed. This process takes a little time, and to ensure that the router is not bricked you should wait six minutes.
 * The router will reboot itself automatically after the upgrade is complete. Rebooting may take a while. It might be the case that the router does not reboot by itself; if this happens it should be safe to wait for the period mentioned and then to do a manual reboot (pull the power-cord).
 * You are done! You should be able to telnet to your router (IP address: 192.168.1.1) and start configuring.
'''NOTES:'''

 * Netkit's tftp doesn't work quite often; use atftp.
 * After TFTP upload is complete, DON'T reboot (replug) too early! It might brick your router.
 * The ASUS WL-500g Premium does not revert to the 192.168.1.1 address when starting the CFE bootloader, but uses the LAN IP address set in NVRAM. Try this address if you have difficulties.
[[Anchor(restore)]] [[Anchor(Restore)]] [[Anchor(restoration)]] [[Anchor(Restoration)]]

'''If you have problems to flash a brand new Asus WL500gP. (Asus restoration tool fails or no tftp prompt) You can try this...'''

 * Download the <yourfirmware>.trx firmware.
 * Open a command prompt and 'cd' to the directory where you downloaded the firmware (.trx file).
 * Type 'tftp -i 192.168.1.1 PUT <yourfirmware>.trx' but DO NOT HIT ENTER!
 * Unplug the power to the router.
 * Hold down the reset/restore button while reconnecting the power. Wait until the power light starts blinking before releasing the reset/restore button.
 * Hit enter in your command prompt window (to run 'tftp -i 192.168.1.1 <yourfirmware>.trx').
 * Wait 15-30 seconds for the image to upload. If you receive a TFTP timeout message start the process over again
 * Wait 4-5 minutes and power cycle the router.
==== ASUS firmware restoration tool (Windows only) ====
If you are on Windows it is recommended to use the ASUS firmware restoration tool to install !OpenWrt. The ASUS firmware restoration tool can be found on the CD. Make sure the router is in diag mode.

 * Browse the .trx file (openwrt-brcm-2.4-squashfs.trx).
 * Press Upload. The router will reboot itself automatically after the upgrade is complete. Rebooting may take a while.
 * You are done! You should be able to telnet to your router (IP address: 192.168.1.1) and start configuring.
If the firmware restoration tool can't seem find your router even though you are certain that it is in diag mode, it may be because the restoration tool is not very smart about which network interface to use. Disable all network interfaces except for the correct (LAN) network interface and try again.

=== Using the mtd command line tool ===
If you have already installed !OpenWrt or like to flash from any other firmware (which has the mtd tool), do this:

{{{
cd /tmp/
wget http://downloads.openwrt.org/kamikaze/7.09/brcm-2.4/openwrt-brcm-2.4-squashfs.trx
mtd write openwrt-brcm-2.4-squashfs.trx linux && reboot}}}
[[Anchor(config)]] [[Anchor(Config)]]

== ASUS WL-500g Premium specific configuration ==
=== Interfaces ===
The default network configuration is:
||<tablewidth="541px" tableheight="129px">'''Interface Name''' ||'''Description''' ||'''Default configuration''' ||
||br-lan ||LAN & !WiFi ||192.168.1.1/24 ||
||vlan0 ||LAN ports (1 to 4) || ||
||vlan1 ||WAN port ||DHCP ||
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
 mtd -r erase rootfs_data[[BR]]
If you are done with failsafe mode power cycle the router and boot in normal mode.[[BR]]

[[Anchor(Buttons)]] [[Anchor(buttons)]]

=== Buttons ===
The ASUS WL-500g Premium has two buttons. They are RESTORE and EZSETUP. The buttons can be used with hotplug events. E. g. [#wifitoggle WiFi toggle].
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
With Kamikaze 7.09 PPPoE works out-of-the-box. All required packages are already installed in the default image. To configure PPPoE with UCI, do this:

{{{
uci set network.wan.proto=pppoe
uci set network.wan.username=<pppoe_psername>
uci set network.wan.password=<pppoe_password>
uci commit network && ifup wan}}}
=== QoS ===
Install the qos-scripts package

{{{
ipkg install qos-scripts
}}}
Basic QoS configuration using UCI:

{{{
uci set qos.wan.upload=192            # Upload speed in KB
uci set qos.wan.download=2048         # Download speed in KB
uci commit qos}}}
Start QoS and enable on next boot

{{{
/etc/init.d/qos boot
/etc/init.d/qos start
/etc/init.d/qos enable
}}}
=== Dynamic DNS ===
Please see [:DDNSHowTo:Dynamic DNS].

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
Set TX Antenna and RX Antenna to 2 to get better signal quality with 1 original antenna.

==== WiFi encryption ====
Plese see OpenWrtDocs/KamikazeConfiguration/WiFiEncryption.

[[Anchor(WiFi toggle)]] [[Anchor(wifitoggle)]]

==== WiFi toggle ====
Turn !WiFi on/off with the EZSETUP or RESTORE [#Buttons button]. Please see the [:OpenWrtDocs/Customizing/Software/WifiToggle:WiFi toggle] Wiki page.

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

=== Webcam with the Linux UVC driver ===
Below works to configure and use a Logitech Quickcam Pro for Notebooks (2007) webcam. Tested with trunk.

{{{
ipkg install kmod-video-uvc kmod-usb2 uvc-streamer}}}
A UCI configuration file and init script for the uvc-streamer:

/etc/config/uvc-streamer

{{{
config uvc-streamer
        option device          '/dev/video0'
        option resolution      '640x480'
        option framespersecond '5'
        option port            '8080'
        option enabled         '1'}}}
/etc/init.d/uvc-streamer

{{{
#!/bin/sh /etc/rc.common
# Copyright (C) 2007 OpenWrt.org
START=50
SSD=start-stop-daemon
NAME=uvc_stream
PIDF=/var/run/$NAME.pid
PROG=/sbin/$NAME
append_bool() {
        local section="$1"
        local option="$2"
        local value="$3"
        local _val
        config_get_bool _val "$section" "$option" '0'
        [ "$_val" -gt 0 ] && append args "$3"
}
append_string() {
        local section="$1"
        local option="$2"
        local value="$3"
        local _val
        config_get _val "$section" "$option"
        [ -n "$_val" ] && append args "$3 $_val"
}
start_service() {
        local section="$1"
        args=""
        append_string "$section" device "-d"
        append_string "$section" resolution "-r"
        append_bool "$section" framespersecond "-f"
        append_string "$section" port "-p"
        config_get_bool "enabled" "$section" "enabled" '1'
        [ "$enabled" -gt 0 ] && $SSD -S -p $PIDF -q -x $PROG -- -b $args
}
stop_service() {
        killall $NAME 2>&1 > /dev/null
        # FIXME: Fix Busybox start-stop-daemon to work with multiple PIDs
        # $SSD -K -p $PIDF -q
}
start() {
        config_load "uvc-streamer"
        config_foreach start_service "uvc-streamer"
}
stop() {
        config_load "uvc-streamer"
        config_foreach stop_service "uvc-streamer"
}
}}}
Make the init script executable

{{{
chmod a+x /etc/init.d/uvc-streamer}}}
Make changes to the config file if needed.

Start uvc-streamer
{{{
/etc/init.d/uvc-streamer start}}}
To activate uvc-streamer on next boot
{{{
/etc/init.d/uvc-streamer enable}}}
Now open the URL [http://192.168.1.1:8080/] in the Firefox browser or VLC and watch the MJPEG stream.
Also see["webcam"]page in the wiki if your webcam needs other drivers.
=== Turn your router into a networked music player ===
Work in progress. Please see the UsbAudioHowto.

[[Anchor(2.6)]]
== Trunk with Kernel 2.6 ==
'''P:''' The line ''b44: eth1: BUG! Timeout waiting for bit 80000000 of register 428 to clear.'' may appear in log. ''' '''

'''S:''' As written in http://forum.openwrt.org/viewtopic.php?pid=29017 this can be fixed by editing /etc/init.d/S10boot

'''P:''' USB 1.1 devices are not recognized, USB 2.0 devices like harddrives etc. work perfectly. How come? ''' '''

'''S:''' The WL-500gP ehci-hcd module handles all USB2 transfer well, but the external ports use uhci-hcd for usb1. To make it even worse, the current trunk version has issues with this module to load but it can be fixed like mentioned in the forum http://forum.openwrt.org/viewtopic.php?id=7149. The broadcom chip seems to have a "buried" ohci controller that can not be used with the external connectors.

== ASUS WL-500g Premium info ==
 * FCC ID: MSQWL500GP [https://gullfoss2.fcc.gov/prod/oet/forms/blobs/retrieve.cgi?attachment_id=640814&native_or_pdf=pdf FCC pictures]
 * [http://www.xbitlabs.com/articles/other/display/asus-wl500g-premium.html Review of the 500gP (pictures starting on page 3)]
 * HardwareAcceleratedCrypto

----

[[Anchor(links)]] [[Anchor(Links)]]

== External Links ==
=== Tutorials ===
 * [http://wl500g.info/showthread.php?t=12962 RAM Upgrade] 
 * [http://www.marcusbrutus.soho.on.net/blog/?p=67 Adding a Bluetooth PAN] by Marcus Brown
 * [http://sr.uz/index.php?p=220&more=1&c=1&tb=1&pb=1 Tips for configuration Atheros MiniPCI card on wl-500gP]  in Russian and [http://sr.uz/index.php?p=223&more=1&c=1&tb=1&pb=1 English translation]
 * [http://josefsson.org/grisslan/wlan.html Setting up WDS/PSK2 on two Asus WL-500gP] by Simon Josefsson
=== Product Info Pages ===
 * [http://usa.asus.com/search.aspx?searchitem=1&searchkey=WL-500g+Premium ASUS WL-500g Premium]
 * [http://www.broadcom.com/products/Wireless-LAN/802.11-Wireless-LAN-Solutions/BCM94704 Broadcom BCM94704 Reference SoC]
 * [http://www.broadcom.com/products/BCM5325 Broadcom BCM5325 Ethernet Switch]
 * [http://www.spansion.com/products/S29GL064M.html Spansion S29GL064M90 Flash Memory Module]
 * [http://www.hynix.com/datasheet/pdf/dram/HY5DU284(8,16)22ETP(Rev0.3).pdf Hynix HY5DU281622ETP-K SDRAM Datasheet]
 * [http://www.via.com.tw/en/products/peripherals/usb/vt6212l/ VIA Vectro VT6212L USB 2.0 Host Controller]
 * [http://www.delta.com.tw/product/cp/telecom/networking/download/pdf/LF8258_and_more.pdf Delta Electronics LF8731 Ethernet PHY Datasheet]
 * [http://www.delta.com.tw/product/cp/telecom/networking/download/pdf/LF8275%208504%208505%208508.pdf Delta Electronics LF8505 Ethernet PHY Datasheet]
=== Forum Threads ===
 * [http://wl500g.info/forumdisplay.php?f=61 Dedicated Forum]
 * [http://forum.openwrt.org/viewtopic.php?id=6090 Problems with WLAN encryption]
 * [http://forum.openwrt.org/viewtopic.php?id=6071 CPU Power]
 * [http://forum.openwrt.org/viewtopic.php?id=5688 OpenWRT compatibility information]
 * [http://forum.openwrt.org/viewtopic.php?id=6362 How-to configure WAN-interface]
----
 . CategoryModel
