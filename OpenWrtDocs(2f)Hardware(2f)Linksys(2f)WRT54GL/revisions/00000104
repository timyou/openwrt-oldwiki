#pragma section-numbers off

||<tablebgcolor="#f1f1ed" tablewidth="40%" tablestyle="FONT-SIZE: 0.9em; FLOAT: right; MARGIN: 0pt 0pt 1em 1em"style="PADDING-RIGHT: 0.5em; PADDING-LEFT: 0.5em; PADDING-BOTTOM: 0.5em; PADDING-TOP: 0.5em">[[TableOfContents]]||
= Linksys WRT54GL =
The WRT54GL is basically a v4.0 ["OpenWrtDocs/Hardware/Linksys/WRT54G"] that still runs Linux. The 1.0 version of this model has serial numbers starting with {{{CL7A}}}; version 1.1 models have serial numbers starting with {{{CL7B}}} and {{{CL7C}}}. As of August 2006, version 1.1 appears to be shipping worldwide. See the [http://forum.openwrt.org/viewtopic.php?pid=15672 WRT54GL] thread in the forum. The model number shown on the package, the front panel, and the sticker on the underside of the unit is WRT54GL. The FCC ID sticker says it is [https://gullfoss2.fcc.gov/prod/oet/cf/eas/reports/ViewExhibitReport.cfm?mode=Exhibits&RequestTimeout=500&calledFromFrame=N&application_id=615033&fcc_id='Q87-WT54GV40' WT54GV40], so it is substantially identical to a WRT54G v4.0/WRT54GS v3.0.

'''NOTE:''' This howto is written for !OpenWrt Kamikaze 7.09 and later versions.

= Supported Versions =

||'''Model''' ||'''S/N''' ||'''!OpenWrt Kamikaze''' ||
||WRT54GL v1 ||CL7A || (./) ||
||WRT54GL v1.1 ||CL7B || (./) ||
||WRT54GL v1.1 ||CL7C || (./) ||

'''NOTE:''' The wireless part is only supported on the 2.4 Kernel version of Kamikaze. The 2.6 Kernel runs fine on the box, but (because the wl.o driver from Broadcom is only available for 2.4 Kernels and the opensource b43 driver is not ready yet) the wireless does not work if you flash a image with a 2.6 Kernel.

= Hardware =
== Info ==
||'''Architecture''' ||MIPS ||
||'''Vendor''' ||Broadcom ||
||'''Bootloader''' ||CFE ||
||'''System-On-Chip''' ||Broadcom 5352EKPB ||
||'''CPU Speed''' ||200 Mhz ||
||'''Flash size''' ||4 MiB ||
||'''RAM''' ||16 MiB ||
||'''Wireless''' ||Broadcom BCM43xx 802.11b/g Wireless LAN (integrated) ||
||'''Ethernet''' ||Switch in CPU ||
||'''USB''' ||No ||
||'''Serial''' ||Yes ||
||'''JTAG''' ||Yes ||
== Serial port ==
The WRT54GL has a 10 pin connection slot on the board called JP1 (JP2 on some v1.1 boards). This slot provides two TTL serial ports at 3.3V. Neither of the ports use hardware flow control, you need to use software flow control instead. Other routers may have similar connections. These two TTL serial ports on the WRT54GL router can be used as standard Serial Ports similiar to the serial ports you may have on your PC. In order to do this though you need a line driver chip that can raise the signal levels to RS-232 levels. You can not directly connect a serial port header to the board and expect it to work. That method will only work with devices that can connect to TTL serial ports at 3.3V. Connecting two which have 3.3V directly will work (TX - RX, RX - TX, GND - GND). Standard RS-232 devices cannot be directly connected which accounts for nearly all serial PC devices.

Once the modification is made you can have at most two serial ports to use for connecting devices etc. By default, !OpenWrt uses the first serial port to access the built-in serial console on the router. You can connect to it at 115200,8,N,1 using a terminal program like Putty, SecureCRT or minicom for example. This is helpful because if you have problems communicating with your router this method will allow you easy access connecting over a serial console. By default this leaves you with one serial port left, however, there is a method to turn the console off giving you access to both ports if you really need them. It isn't recommended but it can be done.
||<tablewidth="1084px" tableheight="65px">'''Pin 2''' ||3.3V ||'''Pin 4''' ||TX_0 ||'''Pin 6''' ||RX_0 ||'''Pin 8''' ||Not connected ||'''Pin 10''' ||GND ||
||'''Pin 1''' ||3.3V ||'''Pin 3''' ||TX_1 ||'''Pin 5''' ||RX_1 ||'''Pin 7''' ||Not connected ||'''Pin 9''' ||GND ||


== JTAG ==
== Photos ==
''Front:''

[http://wiki.openwrt.org/OpenWrtDocs/Hardware/Linksys/WRT54GL?action=AttachFile&do=view&target=wrt54gl_v11_front_hires.jpg http://wiki.openwrt.org/OpenWrtDocs/Hardware/Linksys/WRT54GL?action=AttachFile&amp;do=get&amp;target=wrt54gl_v11_front_thumb___.jpg]

''Back:''

[http://wiki.openwrt.org/OpenWrtDocs/Hardware/Linksys/WRT54GL?action=AttachFile&do=view&target=wrt54gl_v11_back_hires.jpg http://wiki.openwrt.org/OpenWrtDocs/Hardware/Linksys/WRT54GL?action=AttachFile&amp;do=get&amp;target=wrt54gl_v11_back_thumb___.jpg]

== Opening the case ==
= Installation =
Right after flashing at your first login set a few NVRAM parameters.

{{{
nvram set boot_wait=on
nvram set boot_time=10
nvram commit && reboot}}}
NOTE: You do not have to touch any other NVRAM parameters. After this point NVRAM is no longer used.

== Using the Linksys web GUI ==
It is possible to install !OpenWrt directly with the Linksys web GUI. If you are initially installing !OpenWrt use the Linksys web GUI. This is the easiest way.

 * Download the openwrt-wrt54g-2.4-squashfs.bin firmware image to your PC
 * Open http://192.168.1.1/Upgrade.asp in your browser or manually go to http://192.168.1.1 -> Administration -> Firmware Upgrade
 * Upload openwrt-wrt54g-2.4-squashfs.bin
 * Wait 2 minutes. The router will reboot itself automatically after the upgrade is complete.
 * You are done! You should be able to telnet to your router (IP address: 192.168.1.1) and start configuring.
== Using the TFTP method ==
Once you have set the NVRAM parameters above it is possible to use a TFTP client to flash !OpenWrt. The TFTP method is also the recommended way to restore the original Linksys firmware or switch to other third-party firmwares.

 * Unplug the router's power cord.
 * Connect the router's LAN1 port directly to your PC.
 * Configure your PC with a static IP address between 192.168.1.2 and 192.168.1.254. E. g. 192.168.1.2 (gateway and DNS is not required).
 * Download the openwrt-wrt54g-2.4-squashfs.bin firmware image to your PC
 * Execute the TFTP commands (the commands are for Linux) below:
 {{{
tftp 192.168.1.1
tftp> binary
tftp> trace
tftp> put openwrt-wrt54g-2.4-squashfs.bin}}}
 * Plug the power on and the TFTP transfer should start immediately
 * Wait 2 minutes. The router will reboot itself automatically after the upgrade is complete.
 * You are done! You should be able to telnet to your router (IP address: 192.168.1.1) and start configuring.
== Using the mtd command line tool ==

If you have already installed !OpenWrt and like to reflash for e.g. upgrading to a new !OpenWrt version. It is important that you put the firmware image into the ramdisk (/tmp) before you start flashing.

{{{
cd /tmp/
wget http://downloads.openwrt.org/kamikaze/7.09/brcm-2.4/openwrt-brcm-2.4-squashfs.trx
mtd write /tmp/openwrt-brcm-2.4-squashfs.trx linux && reboot}}}

= Linksys WRT54GL specific configuration =

== Interfaces ==
The default network configuration is:
||<tablewidth="541px" tableheight="129px">'''Interface Name''' ||'''Description''' ||'''Default configuration''' ||
||br-lan ||LAN & !WiFi ||192.168.1.1/24 ||
||vlan0 (eth0.0) ||LAN ports (1 to 4) ||None ||
||vlan1 (eth0.1) ||WAN port ||DHCP ||
||wl0 ||!WiFi ||Disabled ||


== Switch Ports (for VLANs) ==
Numbers 0-3 are Ports 1-4 as labeled on the unit, number 4 is the Internet (WAN) on the unit, 5 is the internal connection to the router itself. Don't be fooled: Port 1 on the unit is number 3 when configuring VLANs. vlan0 = eth0.0, vlan1 = eth0.1 and so on.
||<tablewidth="369px" tableheight="243px">'''Port''' ||'''Switch port''' ||
||Internet (WAN) ||4 ||
||LAN 1 ||3 ||
||LAN 2 ||2 ||
||LAN 3 ||1 ||
||LAN 4 ||0 ||


== Failsafe mode ==
If you forgot your password, broken one of the startup scripts, firewalled yourself or corrupted the JFFS2 partition, you can get back in by using !OpenWrt's failsafe mode.

=== Boot into failsafe mode ===
 * Unplug the router's power cord.
 * Connect the router's LAN1 port directly to your PC.
 * Configure your PC with a static IP address between 192.168.1.2 and 192.168.1.254. E. g. 192.168.1.2 (gateway and DNS is not required).
 * Plug the power on and wait for the DMZ LED to light up.
 * While the DMZ LED is on immediately press any button (Reset and Secure Easy Setup will work) a few times .
 * If done right the DMZ LED will quickly flash 3 times every second.
 * You should be able to telnet to the router at 192.168.1.1 now (no username and password)
=== What to do in failsafe mode? ===
'''NOTE:''' The root file system in failsafe mode is the SquashFS partition mounted in readonly mode. To switch to the normal writable root file system run mount_root and make any changes. Run mount_root now.

 1. Forgot/lost your password and you like to set a new one
 passwd[[BR]]
 1. Forgot the routers IP address
 uci get network.lan.ipaddr[[BR]]
 1. You accidentally run 'ipkg upgrade' or filled up the flash by installing to big packages (clean the JFFS2 partition and start over)
 mtd -r erase rootfs_data[[BR]]
If you are done with failsafe mode power cycle the router and boot in normal mode.[[BR]]

== Buttons ==
The Linksys WRT54GL has two buttons. They are Reset and Secure Easy Setup. The buttons can be used with hotplug events. E. g. [#wifitoggle WiFi toggle].
||'''BUTTON''' ||'''Event''' ||
||Reset ||reset ||
||Secure Easy Setup ||ses ||


= Basic configuration =
== Configure WAN for Internet access ==
=== DHCP (e.g. for cable internet) ===
DHCP on the WAN port of the router is the default configuration.

{{{
uci set network.wan.proto=dhcp
uci commit network
ifup wan}}}
TIP: Do not forget to power cycle your cable modem so it knows of the new MAC address of your router. Also make sure you use different subnets for the WAN and LAN networks.

If you need to clone MAC address on the WAN port use MAC address cloning. This is done with the macaddr option in the wan section.

{{{
uci set network.wan.macaddr=11:22:33:aa:bb:cc
uci commit network
ifup wan}}}
=== PPPoE ===
With Kamikaze 7.09 PPPoE works out-of-the-box. All required packages are already installed in the default image. To configure PPPoE with UCI, do this:

{{{
uci set network.wan.proto=pppoe
uci set network.wan.username=<pppoe_psername>
uci set network.wan.password=<pppoe_password>
uci commit network
ifup wan}}}
== QoS ==
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
/etc/init.d/qos start
/etc/init.d/qos enable
}}}
== Dynamic DNS ==
Please see [:DDNSHowTo:Dynamic DNS].

== WiFi ==
=== Enable WiFi ===
{{{
uci set wireless.wl0.disabled=0
uci commit wireless && wifi}}}
=== WiFi encryption ===
Plese see OpenWrtDocs/KamikazeConfiguration/WiFiEncryption.

=== WiFi toggle ===
Turn !WiFi on/off with the Reset or Easy Secure Setup [#Buttons button]. Please see the [:OpenWrtDocs/Customizing/Software/WifiToggle:WiFi toggle] Wiki page.

= Hardware mods =
This section is under construction...

== Adding an MMC/SD card ==
Here we use the[http://forum.openwrt.org/viewtopic.php?id=9653 optimized version of mmc.c].

||<style="TEXT-ALIGN: center" |7> http://wiki.openwrt.org/OpenWrtDocs/Hardware/Linksys/WRT54GL/mmc_gif?action=AttachFile&do=get&target=mmc.gif ||1. CS - Chip Select for the SD card ||GPIO 7 (0x80) ||

||2. DI - Data in on the SD card. ||GPIO 2 (0x04) ||
||3. VSS - Ground is a good thing ||GND ||
||4. VDD - We need power of course. 3.3 V will do the job ||3.3 V ||
||5. CLK - The clock we generate for the SD card ||GPIO 3 (0x08) ||
||6. VSS2 - Another ground is also a good thing ||GND ||
||7. DO - Data out from the SD card ||GPIO 4 (0x10) ||


Photos for the soldering points:

 * [http://cascade.dyndns.org/~datagarbage/linksys-wrt54gl-v1.1-3.3v+GND.jpg +3.3V and GND]
 * [http://cascade.dyndns.org/~datagarbage/linksys-wrt54gl-v1.1-gpio-2+3.jpg GPIO 2 and 3]
 * [http://cascade.dyndns.org/~datagarbage/linksys-wrt54gl-v1.1-gpio-4+7.jpg GPIO 4 and 7]
=== /sbin/init script ===
{{{
#!/bin/sh
. /etc/functions.sh
config_load "bootfromexternalmedia"
local section="cfg1"
config_get      "target"   "$section" "target"
config_get      "device"   "$section" "device"
config_get      "gpiomask" "$section" "gpiomask"
config_get      "modules"  "$section" "modules"
config_get_bool "enabled"  "$section" "enabled" '1'
[ "$enabled" -gt 0 ] && {
        [ -n "$gpiomask" ] && {
                echo "$gpiomask" > /proc/diag/gpiomask
        }
        for module in $modules; do {
                insmod $module
        }; done
        sleep 5s
        mount -o rw "$device" $target
        [ -x $target/sbin/init ] && {
                . /bin/firstboot
                pivot $target $target
        }
}
exec /bin/busybox init}}}
=== /etc/config/bootfromexternalmedia ===
{{{
config bootfromexternalmedia
        option target   '/mnt'
        option device   '/dev/mmc/disc0/part1'
        option gpiomask '0x9c'
        option modules  'mmc jbd ext3'
        option enabled  '1'}}}
= Other Info =
== v1.2 ==
I have seen revision v1.2 in the shop. The sales guy told me it would not run homebrew linux. So i ended up buying a [:OpenWrtDocs/Hardware/Linksys/WRT54GS:WRTG54GS] which i now sucks and works. :) Has anyone seen a v1.2 revision to work?


---- /!\ '''Edit conflict - other version:''' ----
just bought a WRT54GL (22 Nov 2007), and it'a v1.1 CL7B*** (manufactured 09/2007 ? date on the FCC/CE label) - NathaelPajani

I bought a WRT54GL today and received a v1.1 so I would expect that this is still the latest version. OTOH LinkSys claimed that the GL version is specifically targeted at hackers that customize their WRT, so why would they sell one that can not be customized? Did anybody else already see a v1.2 at all? -- TorstenLandschoff

---- /!\ '''Edit conflict - your version:''' ----
just bought a WRT54GL (22 Nov 2007), and it'a v1.1 CL7B*** (manufactured 09/2007 ? date on the FCC/CE label) - NathaelPajani

I bought a WRT54GL today and received a v1.1 so I would expect that this is still the latest version. OTOH LinkSys claimed that the GL version is specifically targeted at hackers that customize their WRT, so why would they sell one that can not be customized? Did anybody else already see a v1.2 at all? -- TorstenLandschoff

---- /!\ '''End of edit conflict''' ----

I tell you. I had the Package in my Hand. I backed of buying i because, as i sayed, had no confimation it will work. It was at Arlt in Freiburg im Breisgau, Germany. Possibly only a -DE Version?

I bought an WRT54GL-DE last week (11/07) from amazon and the device looks like an international version (I think there are no german versions). The version is 1.1, it was manufactured in 08/2007. --x3k6a2

Mine is the same version and manufacturing date, v1.1 made in 08/2007, brought here 27-Dec-2007 at a local store. The "-DE" label seems to be sort of a marketing trick. In fact, even the manual on CD-ROM is labeled "english-only". -- StHoffmann

I bought a new WRT54GL in Germany at amazon.de (in May 07) The Revision is v1.1. The router was manufactured in 01/2007. I can see this date on a sticker on the bottom of the router. -- ThomasBrinkmann


The WRT54GL is Linksys' response to angry customers. For a long time, they had the original WRT54G, which was hackable, but when they joined with Cisco they made it so you were unable to hack the router. Thus, the 54GL. Version 1.1 is the current release, and as of yet there is no v1.2. --CharlesEddy

----
 . CategoryModel
