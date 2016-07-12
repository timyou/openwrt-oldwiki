= Linksys WRTP54G =
The Linksys WRTP54G and Linksys RTP300 linux-powered units are Voice-over-IP enabled routers based on the TI AR7 chipsets.
|| ||'''WRTP54G''' http://www1.linksys.com/products/image180/WRTP54G.jpg ||'''RTP300''' http://www1.linksys.com/products/image180/RTP300.jpg ||
||Base Hardware ||1 Ethernet uplink port, 4x 10/100MBps switch ports, 2 phone jacks || 1 Ethernet uplink port, 4x 10/100MBps switch ports, 2 phone jacks ||
||Wifi Support: ||54MBps 802.11b/g || None ||
||Linksys webpage ||[http://www1.linksys.com/products/product.asp?grid=33&prid=692 Product Page] [http://www.linksys.com/servlet/Satellite?childpagename=US/Layout&packedargs=page=2&cid=1115416835852&c=L_Content_C1&pagename=Linksys/Common/VisitorWrapper&SubmittedElement=Linksys/FormSubmit/ProductDownloadSearch&sp_prodsku=1118334626380 Downloads] || [http://www1.linksys.com/products/product.asp?grid=33&prid=695 Product Page] [http://www.linksys.com/servlet/Satellite?childpagename=US/Layout&packedargs=page=2&cid=1115416835852&c=L_Content_C1&pagename=Linksys/Common/VisitorWrapper&SubmittedElement=Linksys/FormSubmit/ProductDownloadSearch&sp_prodsku=1119460383933 Downloads] ||
||CyberTAN equiv model ||  [http://www.cybertan.com.tw/product/wgv614.asp WGV614] http://www.cybertan.com.tw/product/productpic/wgv614.jpg || [http://www.cybertan.com.tw/product/brv614.asp BRV614] http://www.cybertan.com.tw/product/productpic/brv614.jpg ||
||__Firmware Releases__ ||||<style="text-align: center;"> ||
||1.00.37: ||[http://httpconfig.vonage.net/wrt-11.1.0-r016-1.00.37-r050624.img Firmware Image] [http://www1.linksys.com/support/opensourcecode/WRTP54G/1.00.37/wrtp54g_cyt_1_00_37_gpl.tgz Source Code]If both line are configured to connect to Asterisk and registration is used, they may not stay registered reliably.  The exact circumstances under which this problem manifests itself are yet to be determined. || [http://httpconfig.vonage.net/rt-11.1.0-r016-1.00.37-r050624.img Firmware Image] [ftp://ftp.linksys.com/opensourcecode/rtp300/1.00.37/rtp300_cyt_1_00_37_gpl.tgz Source Code] ||
||1.00.43: ||[http://httpconfig.vonage.net/wrt-11.1.0-r021-1.00.43-r050816.img Firmware Image] No Source || ||
||1.00.45: || ||[http://httpconfig.vonage.net/rt-11.1.0-r021-1.00.45-r050823.img Firmware Image] No Source ||
||1.00.52: || No Firmware Image [ftp://ftp.linksys.com/opensourcecode/wrtp54g/1.00.52/WRTP54G_v1.00.52.tgz Source Code] || No Firmware Image [ftp://ftp.linksys.com/opensourcecode/rtp300/1.00.52/RTP300_v1.00.52.tgz Source Code] ||
||1.00.55: ||[http://httpconfig.vonage.net/wrt-11.1.0-r021-1.00.55-r051013.img Firmware Image] No Source ||[http://httpconfig.vonage.net/rt-11.1.0-r021-1.00.55-r051013.img Firmware Image] No Source ||
||1.00.58: ||[http://httpconfig.vonage.net/wrt-11.1.0-r021-1.00.58-r051202.img Firmware Image] No Source ||[http://httpconfig.vonage.net/rt-11.1.0-r021-1.00.58-r051202.img Firmware Image] No Source ||
||1.00.60: ||[http://httpconfig.vonage.net/wrt-11.1.0-r021-1.00.60-r060123.img Firmware Image] [ftp://ftp.linksys.com/opensourcecode/wrtp54g/1.00.60/WRTP54G_v1.00.60.tgz Source Code] ||[http://httpconfig.vonage.net/rt-11.1.0-r021-1.00.60-r060120.img Firmware Image] [ftp://ftp.linksys.com/opensourcecode/rtp300/1.00.60/RTP300_v1.00.60.tgz Source Code] ||
||1.00.62: ||[http://httpconfig.vonage.net/wrt-11.1.0-r021-1.00.62-r060327.img Firmware Image] No Source ||[http://httpconfig.vonage.net/rt-11.1.0-r021-1.00.62-r060327.img Firmware Image] No Source ||


== Firmware Dumps for Study ==
 * The nearly complete contents of a RTP300 router's mounted file system (version 1.00.55) were dumped, zipped and uploaded to [http://www.northern.ca/projects/openwrt/RTP300-1.0.55-fs-dump.zip here]
 * The nearly complete contents of a WRTP54G router's mounted file system present on firmware version 1.00.60 has been dumped, zipped and uploaded to [http://www.m-a-g.net/wrt-11.1.0-r021-1.00.60-r060123.tar.bz2 here]
 * All of the entries in a RTP300's ''/proc'' directory were cat-ed out to a log file found [http://www.northern.ca/projects/openwrt/rtp300-1.0.55-proc-dump.txt here]
 * A dump of all the flash blocks from an RTP300 with firmware 1.0.55 is available [http://www.northern.ca/projects/openwrt/RTP300-1.0.55-fs-dump.zip here]!  This is different the mounted file system dumps which contain only the files from the mounted root
== Misc Notes ==
 * CyberTAN is a subcontractor for Linksys and their name appears in the router's source code (even the source code archive's name: _cyt_).
 * The VoIP daemon appears to be "RADVISION SIP TOOLKIT 3.0.5.1" (/usr/sbin/ggsip)
 * The telephony chip is the Legerity Le88221, part of the VE880 series.  There is a website with product liturature and example code at http://www.legerity.com/products.php?cid=&sid=1&bpid=33
 * A channel on Freenode #wrtp54g is where those devoted to hacking the wrtp54g and rtp300 hang out.
See also: ["AR7Port"]

= Source Code Supplied by Linksys =
 * The source code supplied by Linksys is incomplete, it's missing the source for some of the utilities (cm_*, lib_cm, webcm) which are used in changing config settings and flashing new firmware updates.
 * There appear to be pieces missing which make the code as a whole unbuildable.  At any rate, though several people in various forums have asked how to build the source code, nobody has posted instructions.
 * The source code supplied for some similiar Linksys routers, such as the WAG354GV2, has a more complete build system.
 * You can rebuild parts of the source code using the Montavista AR7 cross-compiler toolchain.
 * If rebuild parts of the source code using the OpenWrt AR7 cross-compiler toolchain, you will get unusable binaries which the system mistakes for shell scripts.
= Related Sites =
 * A number of the common [http://www.mvista.com/ MontaVista] linux router tools are found (cm_logic, webcm, etc) on these devices... the following page describles some very interesting hacking techniques that likely also apply to the WRTP54G / RTP300: [http://sub.st/articles/hacking-the-actiontec-gt701/ http://sub.st/articles/hacking-the-actiontec-gt701/ ]
 * The Seattle Wireless site has a page about the Dlink DSLG604T which has similiar firmware: http://www.seattlewireless.net/index.cgi/DlinkDslG604t#head-db677a483bdc0cc440a9deb157e737a99a078edb
 * Linux-MIPS port page about the AR7: http://www.linux-mips.org/wiki/AR7
 * Some of the information on this page is derived from Linksysinfo.org: http://www.linksysinfo.org/portal/forums/archive/index.php/t-37891.html

= The Supplied Firmwares =
All of the known firmwares have the following characteristics in common:

 * Linux 2.4.17 kernel with Montavista patches
 * uClibc
 * Busybox

== Characteristics of Version 1.00.XX ==
As of September 2006, Vonage loads firmware version 1.00.62.  This firmware has the following distinguishing characteristics:

 * Busybox is built without the more command
 * Rotary phones work
 * The voice status page displays very little information, basically just whether the last registration suceeded or not
 * Voice configuration is badly broken
  * The "Voice" tab is a dud which suggests that one contact one's service provider for "more information"
  * There are no links to the voice pages
  * The voice tabs do not include the higher level tab bar, so there is no easy way to move out of "Voice"
 * Distinctive can be used by setting ALERT_INFO to &lt;Bellcore-dr<i>X</i>&gt; where X is 1--7.
 * Some people have reported that the lines will not stay registered with an Asterisk server, especially if both are registered.  This is discussed below.
 * There are no visible settings for an outgoing SIP proxy or an STUN server.  There is a setting which may be for sending NOTIFY messages to keep a NAT mapping active, but it does not seem to work.
 * The default register interval is 1 minute.  This is rather short and may be intended to keep the NAT mapping active.

If your phone lines will not register with the SIP server or will not stay registered, check these things:

 * Make sure there are no DNS servers entered in the provisioning tab (may be labeled "Vonage DNS Servers")
 * Use server names, not IP addresses.
 * If you can, log in using SSH or the serial console and make sure /etc/resolv.conf lists only good DNS servers.

== Characteristics of Version 3.1.XX ==

In July and August 2006 Linksys released firmware 3.1.17 for the WRTP54G-NA and RTP300-NA respectively.  Previous versions in the 3.1.X series, such as 3.1.10 which is floating around the Internet have problems registering with some SIP server or connecting to PPPOE servers.

Firmware 3.1.17 has the following distinguishing characteristics:

 * Busybox is built with the more command
 * Rotary phones do not work
 * The voice static page displays a wealth of information about registration as well as current and previous calls
 * The voice tab works and the voice pages display the top level tab bar
 * Distrinctive ring works
 * There are visible settings for NAT traversal features including NAT keepalive, an outgoing SIP proxy, and an STUN server.
 * The default SIP register interval is one hour.

= Accounts in the Supplied Firmwares =

In the default configuration, the RTP and WRTP54G have three usernames, one with each of the defined access levels.

== admin ==
This user has an access level of "ROUTER".  This appears to be the level of access required to log into the top page of the router.  The default password is "admin".

== user ==
This user has an access level of "USER".  Oddly, this access level permits flashing the firmware whereas level "ROUTER" does not.  Level "USER" does not permit to log onto router independently.  One must first log in as a user with "ROUTER" level access and then present enter the name and password of a "USER" level user at the login prompt which appears when the "username and password supplied by your service provider" are demanded.

== Admin ==
This is the only user represented in /etc/passwd which means that this is the only user that can be used to log in using SSH and on the serial console when /etc/inittab specifies that /bin/login is to be run on the console rather than /bin/sh.  This user has the access level  "ADMIN" which also permits flashing the firmware but does not allow independent login.

= Web Access =
The primary way to configure these devices is through a web interface.  In the initial configuration the LAN IP address is 192.168.15.1.  There is a web server with a management interface running on port 80.  The default username is "admin" with a password of "admin".  If there is no web server or you can not log in, you can reset the router to factory defaults by using a paper clip to hold down the reset button while powering the router up.  Continue to hold down the reset button for about 50 seconds.

= SSH Access =
Version 1.00.XX firmwares for both the WRTP54G and RTP300 both can run the Dropbear SSH server.  This feature must be enable using the web interface.  The only username in /etc/passwd is "Admin" (note the upper case A).  Reliably setting the password for this account is problematic.

== Programs and Files in the 3.1.XX Firmware ==
 * /etc/inittab
  . Starts /etc/init.d/rcS and starts /bin/login or /bin/sh on the serial console.
 * /etc/init.d/rcS
  . System startup script.  Not much to see since most of the work is done by the mysterious "lightbox".
 * /usr/bin/foxy
  . an HTTP proxy server which implements the "filter JavaScript" and other "security" functions
 * /usr/bin/wget
  . GNU Wget (why not Busybox wget?).  This is appearently used to download new firmwares.
 * /usr/bin/lightbox
  . Mystery program run from /etc/init.d/rcS.  It seems that it must start most of the daemons
 * /usr/bin/cm_convert
  . Converts old voice configuration to the 3.1.XX format.  Run once per boot.
 * /usr/bin/cm_logic
  . Seems to load the configuration ether from a specified flash block or from an XML file.
 * /usr/bin/cm_config
  . Seems to have something to do with saving the current configuration to flash.
 * /usr/lib/updatedd
  . dynamic DNS client
 * /usr/www/cgi-bin/firmwarecfg
  . Target of POST request which uploads a new firmware
 * /var/upgrader (from var.tar)
  . Appearently the program which does the actual firmware flashing
 * reboot
  . Restart the router
= Flash Memory layout of RTP300 =
== /proc/mtd ==
{{{
dev:    size   erasesize  name
mtd0: 00320000 00010000 "root"                           (3MB - 3,276,800 bytes)
mtd1: 00080000 00010000 "RESERVED_PRIMARY_KERNEL"        (512K - 524,288 bytes)
mtd2: 00320000 00010000 "RESERVED_PRIMARY_ROOT_FS"       (3MB - 3,276,800 bytes)
mtd3: 003d0000 00010000 "RESERVED_PRIMARY_IMAGE"         (3.8MB - 3,997,696 bytes)
mtd4: 003d0000 00010000 "RESERVED_SECONDARY_IMAGE"       (3.8MB - 3,997,696 bytes)
mtd5: 00010000 00010000 "RESERVED_PRIMARY_XML_CONFIG"    (64K - 65,536 bytes)
mtd6: 00010000 00010000 "RESERVED_SECONDARY_XML_CONFIG"  (64K - 65,536 bytes)
mtd7: 00010000 00002000 "RESERVED_BOOTLOADER"            (64K - 65,536 bytes)
mtd8: 00010000 00010000 "cyt_private"                    (64K - 65,536 bytes)}}}
Notes:

 * The flash contains space for two firmwares.  This is presumably so that the system can boot from a backup firmware firmware flashing fails.  mtd3 and mtd4 contain the two firmwares.  Which firmware is active seems to be determined by the setting of the boot loader environment variable BOOTCFG.
 * Unused space at the end of memory blocks is filled with the value 0xFF.
 * mtd0 ''root'' is mounted as /.  It is a 1.x squashfs image with LZMA compression instead of Zlib.  A new squash file system can be built using the mksquashfs from the src/squashfs directory of the source tarball.  This mksquashfs has been patched to use LZMA compression instead of Zlib.
 * mtd5 and mtd6 contain a 20 byte header beginning with a "LMMC" (hex 4C 4D 4D 43 00 03 00 00), followed by a Zlib compressed copy of the XML configuration file.  There is one configuration partition for each firmware.  The format of the compressed configuration file is described elsewhere in this document.
 * mtd7 ''RESERVED_BOOTLOADER'' contains a ["PSPBoot"] bootloader code and environment variables.  The environment variables can be read from ''/proc/ticfg/env'' after boot.  Some of them can be set by writing to /proc/ticfg/env.
 * These partitions are accessible after boot as /dev/mtdblock/0-9 (block device mode, suitable for mounting) or /dev/mtd/0-9 (character mode, suitable for reading or writing with dd).  A partition must be erase before it can be written to.  Flashing firmware is fully described elsewhere in this document.
 * The directory /dev/ti_partitions/ contains symbolic links to serveral of the flash partitions.  The intent seems to be to give them meaningful names.

= Firmware Update File Format =
Here is a partial description of the format of the firmware update file format which is accepted by the web interface and the slightly different format which can be written into flash from the boot loader console (accessible through the serial interface).

 * Bytes 0x00 thru 0x03 are "CDTM".  This is presumably a magic number identifying the file as a firmware.
 * Byte 0x0B must be 0xFF for the web interface and 0x17 if written directly into flash.  The web interface changes this byte to 0x17 before writing the firmware into flash.
 * Bytes 0x14 thru 0x17 must match the value of ProductID from the boot loader environment or the web interface will refuse to load the firmware and if you write it into flash from the boot loader console, the boot loader will refuse to boot it.
 * Bytes 0x70 thru 0xAF contain the file name of the firmware, presumably so that it can be identified even if renamed.
 * Bytes 0xb0 thru ?? appear to be a partion table defining partions "kernel" and "root"
 * From the end of the partition table to 0xFFFF is filled with the value 0xFF.
 * Bytes 0x010000 thru 0x08FFFF are the kernel.  Unused space at the end is filled with the value 0xFF.
 * Bytes 0x90000 thru 0x3AFFFF are the squashfs root filesystem.  The first four bytes of the squashfs are "hsqs".  
 * Firmware images intended to be written directly into flash end at this point.
 * Bytes 0x003b0000 thru 0x003b0003 are a little-endian magic number of 0xC453DE23.
 * Bytes 0x003b0004 thru 0x003b0007 are a little-endian CRC of all bytes from the start until just before the magic number.

If the file is to be written directly into flash it must be 3,866,624 (0x03B0000) bytes long.  A firmware uploaded through the web interface will be eight bytes longer.

== Working with the Squashfs ==

Standard Linux kernels cannot mount the squashfs file system and the standard mksquashfs can not generate it because the compression method is LZMA instead of Zlib.  Possibly helpful information on working with Squashfs and LZMA can be found at [http://www.beyondlogic.org/nb5/squashfs_lzma.htm].  It is also possible that the WRT54G Firmware Modification Kit [http://www.bitsum.com/firmware_mod_kit.htm] would be of help.

If you manage to patch your Linux kernel to include support for Squashfs with LZMA compression, you can extract and mount a firmware's root file system like this:

{{{
# dd if=fw.bin of=fw.fs bs=1024 skip=576
# mount -o loop fw.fs /mnt
}}}

== Tools for Firmware Files ==

Here are some short Perl programs for manipulating firmware upgrade files:

 * Set CRC: attachment:set_ti_checksum
 * Set ProductID and flag at byte 0x0B: attachment:set_ProductID
 * Unpack and pack firmwares: coming soon

= Configuration File Format =
The configuration of the router is stored in a single XML file.  This file is stored compressed in a raw flash partition.  If when the router boots the flash partition is found to be empty, the configuration is initialized by loading /etc/config.xml from the root partition.

The configuration can be extracted using the web interface (Administration/Management/Backup and Restore).  The configuration file produced by the backup function is incomplete.  Particularly, it omits the voice configuration.  The backup configuration file format is as follows:

 * Bytes 0x0000 thru 0x0003 contain "LMMC".  This is appearently a magic number
 * Bytes 0x0004 thru 0x0005 are 0x00 and 0x03 respectively.  This may be a continuation of the magic number.
 * Bytes 0x0006 thru 0x0007 should be set to zero
 * Bytes 0x0008 thru 0x000B contain the length of the compressed configuration file in little-endian format
 * Bytes 0x000C thru 0x000F contain a CRC of the compressed configuration file
 * Bytes 0x0010 thru 0x0013 contain the length of the uncompressed configuration file
 * Bytes from 0x0014 on contain the configuration file in Zlib's deflate format
= Boot Loader Environment =
The PSPBOOT boot loader contains a set of environment variables, some of which are used by the boot loader itself, while others are used by the firmware after boot.

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
IMAGE_B 0x90400000,0x907d0000http://www.bitsum.com/firmware_mod_kit.htm
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
MEMSZ 0x01000000
FLASHSZ 0x00800000
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
This is a four character code which identifies the hardware.  Bytes 0x14-0x17 of the firmware file must match this code or you will not be able to install it using the web interface.  If you write it to flash by some other means, PSPboot will refuse to load it.

Known ProductID values:

 * RTP300-NA: CYLM
 * RTP300 from Vonage: CYLL
 * WRTP54G-NA: CYWM
 * WRTP54G from Vonage: ?
One trick a device into loading a firmware which was not intended for it by changing the ProductID in the firmware and updating the CRC at the end of it.  (Refer to the description of the firmware update file format above.)  Loading an incompatible firmware may brick your device, so be careful.  In particular, loading an WRTP54G firmware on an RTP300 will brick it, but only when you do a factory reset.  The reason for this is that /etc/config.xml in the WRTP54G firmware is incompatible with the RTP300.  It seems that a system daemon crashes when it attempts to configure the wireless hardware.  As long as the configuration created by the RTP300 firmware remains in place, all is well, but a factory reset copies config.xml into the configuration area.  If you do this, you will have to use a serial console to regain access.

== IMAGE_A, CONFIG_A, IMAGE_B, CONFIG_B ==
The router has room for two firmwares and a configuration area for each.  Factory defaults can be restored by formatting the configuration area of the currently active firmware.  (There are other ways to do this including a screen in the web interface and holding down the reset button for a few seconds once the device has booted.)  The command to clear the conifguration area of the first firmware is:

{{{fmt CONFIG_A}}}

Possible ways to write a new firmware to IMAGE_A or IMAGE_B are described elsewhere in this document.

== BOOTCFG_A, BOOTCFG_B, BOOTCFG ==
The firmware to be booted is defined by BOOTCFG.  The significance of the m and the f are unknown.  The variables BOOTCFG_A and BOOTCFG_B are appearently models for setting BOOTCFG.

Unfortunately, there does not seem to be a direct and reliable way to set BOOTCFG.  But, if there are two firmwares installed and one formats the image partition of the one named in BOOTCFG, BOOTCFG will automatically switch to the other one.

= Serial Console =
{{{
________________________________________
|                                         |
|                                         ledhttp://www.bitsum.com/firmware_mod_kit.htm
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
{{{
grep '128\.95' /etc/dhcpd.conf
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

= Firmware Flashing =
There are several proven ways to write a new firmware into flash:

 * Using the web interface
 * Using firmware update on the provisioning page
 * Using command line tools under a running firmware
 * From the PSPBoot prompt using the serial port console
It is presumably possible to write a firmware using JTAG, but so far nobody has reported success.

The PSPBoot page suggests that there is a one second window during PSPBoot startup during which a TFTP server is ready to accept a new firmware named upgrade_code.bin, but this feature does not seem to be included in the build of PSPBoot installed on the RTP300.

== Using the Web Interface ==
This method ranges from very easy to somewhat tricky depending on what firmware is currently installed.  The basic procedure is as follows:

 * Connect a computer to one of the yellow ports of the router
 * Set the computer to gets its IP address by DHCP and make sure it does so before proceeding
 * Connect to http://192.168.15.1 using a web browser.  If it does not respond, hold down the reset button for at least five seconds.  When it reboots, try again.
 * Log in using the default username and password of "admin" and "admin"
 * Click on the "Administration" tab
 * Click on the "Firmware Update" tab.  If there is no "Firmware Update" tab, enter http://192.168.15.1/update.html in your browser's location bar.
 * Log in as a user who is permitted to update the firmware.  For generic firmwares, the username may be "Admin" with a blank password or "user" with a password of "user".  If your router was last used with Vonage, you can set a username of "user" and a password of "tivonpw" by following this procedure:
  * Plug the router into the Internet if it is not plugged in already.
  * Got to Administration tab and choose Factory Defaults.  Choose "Restore Router Defaults" and "Restore Voice Defaults"
  * Enter a username of "user" and a password of "tivonpw"
  * Give the router a minute to reboot and then return to step four.
 * Click on Browse and choose a firmware image.  (If you get an error page instead of the firmware upgrade page, enter http://192.168.15.1/update.html into your browser's location bar.  Some firmwares have a broken link.)
 * If the Internet cable is connected to the router, disconnect it.
 * Click on Update.  A progress bar will move accross the screen.  When the bar reaches about 10% the product ID will be checked.  After it reaches 100%, the CRC will be checked.  If both of these hurdles are passed, a screen will appear announcing that the device is rebooting.
 * If your router was last used with Vonage, log in again and go to Administration->Factory Defaults and reset both router and voice defaults again.  The router has two configuration areas, and the old settings may not be cleared out of active configuration area.  If they are not, the router may download and install a firmware that you do not want.
 * Reconnect the router to the Internet.

If the web server does not respond in step three, or the default password does not work in step four, make sure the router has been powered up for at least 50 seconds and then hold down the reset button for at least five seconds.  The router will restore its factory defaults and reboot.  Return to step three.

If your router is running an NA firmware, the username needed in step seven is probably "Admin" (note the capital A verses the lower case a in step four).  The password will be blank.

If your router has Vonage firmware on it, the procedure is slightly more complicated.  First, you should plug your router into the Internet so that it can load its configuration from Vonage's servers.  This will give you a user name of "user" and a password of "tivonpw" which you can use in step seven.  Second, there will be no "Firmware Update" tab in step six.  Instead, enter http://192.168.15.1/update.html.  (Note: this procedure is incomplete and not entirely correct.  One must at some point also go to Administration/Factory Defaults and reset the router and voice configuration to factory defaults.)

If you get a page-not-found error after logging in in step seven, do not dispair.  This is bug in some firmwares.  Simply enter the address http://192.168.15.1/update.html into your browser and continue from there.

== Using Firmware Update on the Provisioning Page ==

VOIP providers can configure these routers to periodically download a VOIP configuration file.  This file contains VOIP settings and login credentials for the provider's SIP server.  This process is called "provisioning".  The "provisioning" file can also instruct the router to download and install a new firmware.  The Provisioning page in the web interface can also be used to initiate this process.  This may be helpful if you loose access the firmware upgrade page but still have access to the Provisioning page.  Here is the procedure for the 3.1.XX series firmware:

 * Connect to the web interface and log in as admin
 * Click on the Voice tab
 * Click on "Admin Login" hyperlink under the second menu bar
 * Click on the "switch to advanced view"
 * Click on the "Provisioning" tab
 * Enter the URL of the firmware file (HTTP is fine) in the "upgrade rule" field.
 * Press "Save"
 * Watch your HTTP server logs to see if the router grabs the firmware

The firmware should be in the same format as for upgrading through the web interface.

== Using command line tools ==

Using this procedure, you can write a firmware into one of the two firmware partitions.  Note that while you can overwrite the running firmware and reboot, it may not be a safe practice.  One can presumably overwrite the inactive firmware, but it is unclear how to then make it the active firmware.  This procedure describes how to overwrite the inactive firmware.

 * You will need the flash erase tool (erase.c in the GPL tarball) compiled to run on the router.  (attachment:flash_erase)
 * Create a new firmware image.  See Firmware Upgrade File Format above.  (Briefly, byte 0x000B should be 0x17, there should be no CRC, and the firmware should be exactly 3,866,624 bytes long.)
 * Download <b>erase</b> and the firmware to the router:
{{{
# cd /var
# wget http://myhost/dir/flash_erase
# chmod 755 erase
# wget http://myhost/dir/rtp300-XXXXX.bin
}}}
 * Erase and write flash:
{{{
# /var/flash_erase /dev/mtd/4 0 60 && dd if=/var/rtp300-XXXXX.bin of=/dev/mtd/4
}}}

== From the PSPBoot prompt ==
In order to use this method you must obtain or make a voltage converter for your router's serial port and hook it up as described in the section Serial Port.  You must also change the value of CONSOLE_STATE as described in the same section.  Since you need shell access to the router in order to change CONSOLE_STATE, you will not be able to use this method unless the existing firmware allows shell access.

The PSPBoot boot loader has predefined environment variables called IMAGE_A and IMAGE_B which contain the start and stop addresses of the mtd3 and mtd4 flash partitions.  A new firmware can be loaded into one of the spaces by formatting the space and copying in a properly formated firmware file using TFTP.  For example, if you have a firmware called new_firmware.bin on a TFTP server on a computer attached to one of the yellow ports with an IP address of 192.168.15.100, the commands are like this:

{{{
setenv IPA 192.168.15.1
fmt IMAGE_A
tftp -i 192.168.15.100 new_firmware.bin IMAGE_A
}}}
If your TFTP server is not in the same subnet or the subnet mask is not 255.255.255.0 you will have to set additional environment variables as described under Boot Loader Environment.
