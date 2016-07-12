= Linksys WRTP54G =
The Linksys WRTP54G and Linksys RTP300 linux-powered units are Voice-over-IP enabled routers based on the TI AR7 chipsets.
|| ||'''WRTP54G''' http://www1.linksys.com/products/image180/WRTP54G.jpg ||'''RTP300''' http://www1.linksys.com/products/image180/RTP300.jpg ||
||Base Hardware ||1 Ethernet uplink port, 4x 10/100MBps switch ports, 2 phone jacks || 1 Ethernet uplink port, 4x 10/100MBps switch ports, 2 phone jacks ||
||Wifi Support: ||54MBps 802.11b/g || None ||
||Linksys webpage ||[http://www1.linksys.com/products/product.asp?grid=33&prid=692 Product Page] [http://www.linksys.com/servlet/Satellite?childpagename=US/Layout&packedargs=page=2&cid=1115416835852&c=L_Content_C1&pagename=Linksys/Common/VisitorWrapper&SubmittedElement=Linksys/FormSubmit/ProductDownloadSearch&sp_prodsku=1118334626380 Downloads] || [http://www1.linksys.com/products/product.asp?grid=33&prid=695 Product Page] [http://www.linksys.com/servlet/Satellite?childpagename=US/Layout&packedargs=page=2&cid=1115416835852&c=L_Content_C1&pagename=Linksys/Common/VisitorWrapper&SubmittedElement=Linksys/FormSubmit/ProductDownloadSearch&sp_prodsku=1119460383933 Downloads] ||
||CyberTAN equiv model ||  [http://www.cybertan.com.tw/product/wgv614.asp WGV614] http://www.cybertan.com.tw/product/productpic/wgv614.jpg || [http://www.cybertan.com.tw/product/brv614.asp BRV614] http://www.cybertan.com.tw/product/productpic/brv614.jpg ||
||__Firmware Releases__ ||||<style="text-align: center;"> ||
||1.00.37: ||[http://httpconfig.vonage.net/wrt-11.1.0-r016-1.00.37-r050624.img Firmware Image] [http://www1.linksys.com/support/opensourcecode/WRTP54G/1.00.37/wrtp54g_cyt_1_00_37_gpl.tgz Source Code] || [http://httpconfig.vonage.net/rt-11.1.0-r016-1.00.37-r050624.img Firmware Image] [ftp://ftp.linksys.com/opensourcecode/rtp300/1.00.37/rtp300_cyt_1_00_37_gpl.tgz Source Code] ||
||1.00.43: ||[http://httpconfig.vonage.net/wrt-11.1.0-r021-1.00.43-r050816.img Firmware Image] No Source || ||
||1.00.45: || ||[http://httpconfig.vonage.net/rt-11.1.0-r021-1.00.45-r050823.img Firmware Image] No Source ||
||1.00.52: || No Firmware Image [ftp://ftp.linksys.com/opensourcecode/wrtp54g/1.00.52/WRTP54G_v1.00.52.tgz Source Code] || No Firmware Image [ftp://ftp.linksys.com/opensourcecode/rtp300/1.00.52/RTP300_v1.00.52.tgz Source Code] ||
||1.00.55: ||[http://httpconfig.vonage.net/wrt-11.1.0-r021-1.00.55-r051013.img Firmware Image] No Source ||[http://httpconfig.vonage.net/rt-11.1.0-r021-1.00.55-r051013.img Firmware Image] No Source ||
||1.00.58: ||[http://httpconfig.vonage.net/wrt-11.1.0-r021-1.00.58-r051202.img Firmware Image] No Source ||[http://httpconfig.vonage.net/rt-11.1.0-r021-1.00.58-r051202.img Firmware Image] No Source ||
||1.00.60: ||[http://httpconfig.vonage.net/wrt-11.1.0-r021-1.00.60-r060123.img Firmware Image] [ftp://ftp.linksys.com/opensourcecode/wrtp54g/1.00.60/WRTP54G_v1.00.60.tgz Source Code] ||[http://httpconfig.vonage.net/rt-11.1.0-r021-1.00.60-r060120.img Firmware Image] [ftp://ftp.linksys.com/opensourcecode/rtp300/1.00.60/RTP300_v1.00.60.tgz Source Code] ||
||1.00.62: ||[http://httpconfig.vonage.net/wrt-11.1.0-r021-1.00.62-r060327.img Firmware Image] No Source ||[http://httpconfig.vonage.net/rt-11.1.0-r021-1.00.62-r060327.img Firmware Image] No Source ||

'''Notes'''

 * CyberTAN is a subcontractor for Linksys and their name appears in the router's source code (even the source code archive's name: _cyt_).
 * In the initial configuration the LAN IP address is 192.168.15.1.  There is a web server with a management interface running on port 80.  The default username is "admin" with a password of "admin".  If there is no web server or you can not log in, you can reset the router to factory defaults by using a paper clip to hold down the reset button while powering the router up.  Continue to hold down the reset button for about 50 seconds.
 * The "admin" account does not have sufficient privileges to reflash the firmware.  If your router is configured to be "provisioned" by Vonage, let it connect to the Internet in order to download its configuration from Vonage's server.  The Vonage configuration has a user named "user" with a password of "tivonpw".  The user "user" can reflash the firmware.  (That is right, user has more access than admin.)  After logging in as admin/admin change the URL to http://192.168.15.1/update.html.  At the new password prompt enter "user" and "tivonpw".  A web form for uploading the new firmware will pop up.
 * The WRTP54G and RTP300 both run dropbear SSH (limited to 2 concurrent connections) and some time ago 'root' access was gained to a RTP300 box using the Admin account (Admin is uid 0).  (Could somebody clarify this statement?  Was this due to some special circumstance or is it something we can reproduce?)
 * The source code supplied by Linksys is incomplete, it's missing the source for some of the utilities (cm_*, lib_cm, webcm) which are used in changing config settings and flashing new firmware updates.  Binaries can be found in the zip file of the FS dump below.
 * The nearly complete contents of a RTP300 router's mounted file system (version 1.00.55) were dumped, zipped and uploaded to [http://www.northern.ca/projects/openwrt/RTP300-1.0.55-fs-dump.zip here]
 * The nearly complete contents of a WRTP54G router's mounted file system present on firmware version 1.00.60 has been dumped, zipped and uploaded to [http://www.m-a-g.net/wrt-11.1.0-r021-1.00.60-r060123.tar.bz2 here]
 * All of the entries in a RTP300's ''/proc'' directory were cat-ed out to a log file found [http://www.northern.ca/projects/openwrt/rtp300-1.0.55-proc-dump.txt here]
 * A number of the common [http://www.mvista.com/ MontaVista] linux router tools are found (cm_logic, webcm, etc) on these devices... the following page describles some very interesting hacking techniques that likely also apply to the WRTP54G / RTP300: http://sub.st/articles/hacking-the-actiontec-gt701-wg-wireless-gateway.html
 * The VoIP daemon appears to be "RADVISION SIP TOOLKIT 3.0.5.1" (/usr/sbin/ggsip)
 * The telephony chipset seems to be produced by Telogy Networks (/lib/modules/2.4.17_mvl21-malta-mips_fp_le/kernel/drivers/*.o). The driver source code has not been released.
 * A channel on Freenode #wrtp54g is where those devoted to hacking the wrtp54g and rtp300 hang out.
See also: ["AR7Port"]

= Memory layout of RTP300 =
== /proc/mtd ==
{{{
dev:    size   erasesize  name
mtd0: 00320000 00010000 "root"                           (3MB - 3,276,800 bytes)
mtd1: 00080000 00010000 "RESERVED_PRIMARY_KERNEL"        (512K - 524,288 bytes)
mtd2: 00320000 00010000 "RESERVED_PRIMARY_ROOT_FS"       (3MB -3,276,800 bytes)
mtd3: 003d0000 00010000 "RESERVED_PRIMARY_IMAGE"         (3.8MB - 3,997,696 bytes)
mtd4: 003d0000 00010000 "RESERVED_SECONDARY_IMAGE"       (3.8MB - 3,997,696 bytes)
mtd5: 00010000 00010000 "RESERVED_PRIMARY_XML_CONFIG"    (64K - 65,536 bytes)
mtd6: 00010000 00010000 "RESERVED_SECONDARY_XML_CONFIG"  (64K - 65,536 bytes)
mtd7: 00010000 00002000 "RESERVED_BOOTLOADER"            (64K - 65,536 bytes)
mtd8: 00010000 00010000 "cyt_private"                    (64K - 65,536 bytes)}}}
Notes:

 * A dump of all the RTP300's blocks is available [http://www.northern.ca/projects/openwrt/RTP300-1.0.55-fs-dump.zip here]!  This is different the the FS dump made available earlier (which contained only files from the mounted root).
 * All memory blocks are padded at the ends with ASCII 255 characters (Hex FF).
 * mtd0 ''root'' is mounted as / (squashfs file system) since ''/proc/version'' is {{{Linux version 2.4.17_mvl21-malta-mips_fp_le (myron@dhcp-2123-3084) (gcc version 2.95.3 20010315 (release/MontaVista)) #1 Thu Oct 13 10:23:23 CST 2005}}} this FS is most likely a 1.x sqaushfs image like that in the Actiontec ["OpenWrtDocs/Hardware/Actiontec/GT701-WG"].
 * mtd5 and mtd6 begin with a "LMMC" header (hex 4C 4D 4D 43 00 03 00 00), each containing approximately 8-10kb worth of data almost the same exact size a backup config.bin file.  After removing the padding, neither file matches the config.bin taken from the running router's backup page.
 * mtd7 ''RESERVED_BOOTLOADER'' appears to contain a ["PSPBoot"] bootloader, it has all of the environment variables which are available after boot time via ''/proc/ticfg/env''

= Firmware Update File Format =
Here is a partial description of the format of the firmware update file format which is accepted by the web interface and the slightly different format which can be written into flash from the boot loader console (accessible through the serial interface).
 * The first four bytes are "CDTM".  This appearently identifies the file as a firmware.
 * Bytes 0x14--0x17 must match the value of ProductID from the boot loader environment or the web interface will refuse to load the firmware and if you write it into flash from the boot loader console, the boot loader will refuse to boot it.
 * Byte 0x0B must be 0xFF for the web interface and 0x17 if written directly into flash.
 * Bytes 0x70--0xAF contain the file name of the firmware, presumably so that it can be identified even if renamed.
 * Something which may be the kernel but is more likely a second-stage boot loader starts at offset 0x10000.
 * The squashfs for the root filesystem starts at offset 0x90000 (576K into the file) and continues to the end of the file (which the exception noted below).  The first four bytes of the squashfs are "hsqs".
 * If the file is to be written directly into flash it must be 3,866,624 bytes long.  The web interface require an eight bit CRC at the end for a total of 3,866,632 bytes.

= Boot Loader Environment =
The PSPBOOT boot loader and a set of environment variables, some of which are used by the boot loader itself, while others are used by the firmware after boot.

At the serial console the printenv command displays the whole environment while the setenv, unsetenv, and setpermenv commands modify it.  The difference between the setenv and the setpermenv commands is unknown.

After boot, the boot environment can be read and written through the pseudo-file /proc/ticfg/env.  Reading the file returns the environment, one variable per line, with a tab between name and value.  Writing a line in the same format changes a variable, as long as it is not read-only.  A space may be substituted for a tab when writing.

Here is a sample boot environment from an RTP300 as read from /proc/ticfg/env.  HWA_0, HWA_1, andSerialNumberhave been anonymized.

{{{
BUILD_OPS 0x541
bootloaderVersion 1.3.3.11.2.6
HWRevision 1.00.03
max_try 4
IMAGE_A 0x90020000,0x903f0000
CONFIG_A 0x903f0000,0x90400000
IMAGE_B 0x90400000,0x907d0000
CONFIG_B 0x907d0000,0x907e0000
BOOTCFG_A m:f:"IMAGE_A"
BOOTCFG_B m:f:"IMAGE_B"
HW_COMPANDING linear
FSX_FSR 16
TELE_IF INTERNAL
BOOTLOADER 0x90000000,0x90010000
save_voice_config yes
DSP_CLK 12288000:10
boot_env 0xb0010000,0xb0020000
cyt_private 0xb07f0000,0xb0800000
TELE_ID VE882XX:AUTO
WIFI_LED_GPIO 13
WIFI_LED_RATE 50
SUBNET_MASK 255.255.255.0
MAC_PORT 0
MEMS Z0x01000000
FLASHS Z0x00800000
MODETTY 0115200,n,8,1,hw 
CPUFREQ 162500000
SYSFREQ 125000000
PROMPT (psbl)
IPA 192.168.6.15
IPA_GATEWAY 192.168.6.254
ProductID CYLL
CONSOLE_STATE locked
TFTPU_STATE OFF
SerialNumber CJM00E5xxxxx
HASH_DIR 8wA2fClJsg
CRYPT_KEY 47035165D59457E16ACA0EFC747AC05C9985F36DDD60B5641B25E1EC581AEFE3
ADMIN_PWD ABPPRAHK55QVA
HWA_0 00:13:10:AC:02:AB
HWA_1 00:13:10:AC:02:AA
BOOTCFG m:f:"IMAGE_A"}}}

== CONSOLE_STATE ==

Setting this variable to "locked" causes PSPBoot to load the firmware without giving the user an oportunity to go to the PSPBoot prompt by pressing escape.  Setting it to "unlocked" restores friendly behavior.  See the Serial Console section for a way to unlock the console.

== IPA, IPA_GATEWAY, SUBNET_MASK ==

These variables define the IP settings used by the tftp command.  It makes sense to change IPA to "192.168.15.1" since this is the IP address which the standard firmwares assign to the router.

== ProductID ==

This is a four character code which identifies the hardware.  For the RTP300 it is CYLL.  For the WRTP54G it is appearently CYWM.  Bytes 0x14-0x17 of the firmware file must match this code or you will not be able to load it.

== IMAGE_A, CONFIG_A, IMAGE_B, CONFIG_B ==

The router has room for two firmwares and a configuration area for each.  Factory defaults can be restored by formatting the configuration area of the currently active firmware.  (There are other ways to do this including a screen in the web interface and holding down the reset button for a few seconds once the device has booted.)  The command to clear the conifguration area of the first firmware is:

{{{fmt CONFIG_A}}}

A new firmware can be loaded into one of the spaces by formatting the space and copying in a properly formated firmware file using TFTP.  If you have a firmware called new_firmware.bin on a TFTP server on a computer attached to one of the yellow ports with an IP address of 192.168.15.100, the commands are like this:

{{{
setenv IPA 192.168.15.1
fmt IMAGE_A
tftp -i 192.168.15.100 new_firmware.bin IMAGE_A
}}}

== BOOTCFG_A, BOOTCFG_B, BOOTCFG ==

The firmware to be booted is defined by BOOTCFG.  The significance of the m and the f are unknown.  The variables BOOTCFG_A and BOOTCFG_B are appearently models for setting BOOTCFG.

Unfortunately, there does not seem to be a direct and reliable way to set BOOTCFG.  If there are two firmwares installed and one formats the image partition of the one named in BOOTCFG, BOOTCFG will automatically switch to the other one.

= Serial Console =
{{{
________________________________________
|                                         |
|                                         led
|                   Pin 1: GND   ---> @   |
|                                         led
|         Pin 2: Not Connected   ---> @   |
|                                         led
|                   Pin 3: RX   ----> @   |                 Front of RTP300 or WRTP54G
|                                         led
|                   Pin 4: TX   ----> @   |
|                                         |
|                   Pin 5: VCC  ----> @   led
|                                         |
|                                         |
|                                         |
 \________________________________________|
}}}

Do not connect the router's serial port directly to your computer's RS232 port.  The signal voltage levels are not the same and you may damage the router's serial port.  This is because your computer's serial port has a line driver which converts the computer's signal voltage levels to RS232 levels while the line driver was left out of the router to save money.  So, you will have to attach a line driver to your router and plug your computer into the line driver.  If you are handy with a soldering iron you can order a AD233AK 233A kit and assemble it to make a line driver.

The default settings for the serial port are 115200 BPS, 8 bit words, no parity, hardware flow control.  These settings may be changable by setting the boot environment variable MODETTY.

The serial port is the boot loader console.  If the boot-loader environment variable CONSOLE_STATE is set to "unlocked" (rather than "locked") then you will have three seconds to stop the boot and receive a boot loader prompt. Most if not all firmwares allow login on the serial port once they are booted.  Some run /bin/login whereas others simply run /bin/sh.  The 3.1.10 firmware which is floating around the internet, though said to be unstable, does have the advantage that it accepts "Admin" as a username with a blank password.  Once you have logged into a running firmware you can change CONSOLE_STATE with the command:

{{{
# echo "CONSOLE_STATE unlocked" >/proc/ticfg/env}}}
= JTAG =
JTAG is a standard way to gain access to the system bus of an embedded device.  It can be used to reprogram the flash even if the boot loader has been damaged.

== WRTP54G JTAG Pinout ==
{{{grep '128\.95' /etc/dhcpd.conf
__________________________________________
|                     J3                  |
|                                         led
| Pin 1: TRST  ----> @   @ <-- Pin 2:GND  |
|                                         led
| Pin 3: TDI   ----> @   @ <-- Pin 4:GND  |
|                                         led
| Pin 5: TDO   ----> @   @ <-- Pin 6:GND  |
|                                         led
| Pin 7: TMS   ----> @   @ <-- Pin 8:GND  |   Front of WRTP54G
|                                         |
| Pin 9: TCK   ----> @   @ <-- Pin 10:GND led
|                                         |
| Pin 11:RST   ----> @   @ <-- Pin 12:NC  |
|                                         |
| Pin 13:DINT  ----> @   @ <-- Pin 14:VIO*|
 \________________________________________|
    *voltage reference @ 3.3 volts
}}}
The AR7 implements ejtag version 2.6.

This ejtag layout should work with all ar7 based boards with a 14 pin jtag pinout.  The same cable as used for the wrt54g (based on the xilinx III/dlc-5) as demonstrated by !HairyDairyMaid can be constructed and is well documented.  Debug INT pin 13 is optional and pin 14 can be left unhooked for passive cabling.

Since DMA Routines do '''not''' exist for this ejtag version (compared to ejtag v2.0 supported on the wrt54g) interfacing requires a rewrite utilizng prAcc routines of the v2.6 standard.

The JTAG utility authored by HairyDairyMaid that is in common use as a debugger for the wrt54g originally did not support the v2.6 routines due to the need to rewrite the prAcc routines.  After some lobbying, he has purportedly added support that is *supposed* to work with the wrtp54g as well as other ar7 based routers although at last check (which was some while ago) this additional feature had yet to be successfully confirmed to work as intended, although I had heard through a third party that it had in fact worked this needs to be confirmed by someone on this page with firsthand knowledge.

 * [http://www.dlinkpedia.net/index.php/Jtag_su_30xT JTAG for a similar AR7 device]
 * [http://www.dlinkpedia.net/index.php/Interfaccia_JTAG JTAGInterface] (Italian!)
 * ["OpenWrtDocs/Customizing/Hardware/JTAG Cable"] guide
----
 . CategoryModel ["CategoryAR7Device"]
