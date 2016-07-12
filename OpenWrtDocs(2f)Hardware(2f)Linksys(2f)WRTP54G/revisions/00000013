= Linksys WRTP54G =
The Linksys WRTP54G and Linksys RTP300 linux-powered units are Voice-over-IP enabled routers based on the TI AR7 chipsets.

|| ||'''WRTP54G''' http://www1.linksys.com/products/image180/WRTP54G.jpg ||'''RTP300''' http://www1.linksys.com/products/image180/RTP300.jpg||
||Base Hardware||1 Ethernet uplink port, 4x 10/100MBps switch ports, 2 phone jacks|| 1 Ethernet uplink port, 4x 10/100MBps switch ports, 2 phone jacks||
||Wifi Support:||54MBps 802.11b/g|| None ||
||Linksys webpage||[http://www1.linksys.com/products/product.asp?grid=33&prid=692 Product Page] [http://www.linksys.com/servlet/Satellite?childpagename=US%2FLayout&packedargs=page%3D2%26cid%3D1115416835852%26c%3DL_Content_C1&pagename=Linksys%2FCommon%2FVisitorWrapper&SubmittedElement=Linksys%2FFormSubmit%2FProductDownloadSearch&sp_prodsku=1118334626380 Downloads]|| [http://www1.linksys.com/products/product.asp?grid=33&prid=695 Product Page] [http://www.linksys.com/servlet/Satellite?childpagename=US%2FLayout&packedargs=page%3D2%26cid%3D1115416835852%26c%3DL_Content_C1&pagename=Linksys%2FCommon%2FVisitorWrapper&SubmittedElement=Linksys%2FFormSubmit%2FProductDownloadSearch&sp_prodsku=1119460383933 Downloads]||
||CyberTAN equiv model||  [http://www.cybertan.com.tw/product/wgv614.asp WGV614] http://www.cybertan.com.tw/product/productpic/wgv614.jpg|| [http://www.cybertan.com.tw/product/brv614.asp BRV614] http://www.cybertan.com.tw/product/productpic/brv614.jpg||
||__Firmware Releases__||||||
||1.00.37:||[http://httpconfig.vonage.net/wrt-11.1.0-r016-1.00.37-r050624.img Firmware Image] [http://www1.linksys.com/support/opensourcecode/WRTP54G/1.00.37/wrtp54g_cyt_1_00_37_gpl.tgz Source Code]|| [http://httpconfig.vonage.net/rt-11.1.0-r016-1.00.37-r050624.img Firmware Image] [ftp://ftp.linksys.com/opensourcecode/rtp300/1.00.37/rtp300_cyt_1_00_37_gpl.tgz Source Code]||
||1.00.43:||[http://httpconfig.vonage.net/wrt-11.1.0-r021-1.00.43-r050816.img Firmware Image] No Source|| ||
||1.00.45:|| ||[http://httpconfig.vonage.net/rt-11.1.0-r021-1.00.45-r050823.img Firmware Image] No Source||
||1.00.55:||[http://httpconfig.vonage.net/wrt-11.1.0-r021-1.00.55-r051013.img Firmware Image] No Source||[http://httpconfig.vonage.net/rt-11.1.0-r021-1.00.55-r051013.img Firmware Image] No Source||

'''Notes'''

 * CyberTAN is a subcontractor for Linksys and their name appears in the router's source code (even the archive name: _cyt_).

 * The WRTP54G and RTP300 both run dropbear SSH and some time ago root access was gained to an RTP300 box.

 * Source code is incomplete, it's missing some of the binary files (cm_*, lib_cm, webcm) which are used in changing config settings and flashing new firmware updates.  Binaries can be found in the zip file of the FS dump below.

 * The nearly complete contents of that router's file system were extracted and stored [http://www.northern.ca/projects/openwrt/RTP300-1.0.55-fs-dump.zip here]

 * All of the entries in the ''/proc'' directory were cat-ed out to a log file found [http://www.northern.ca/projects/openwrt/rtp300-1.0.55-proc-dump.txt here]

 * A number of the common montavista router linux tools are found (cm_logic, webcm, etc) on these routers... the following page describles some very interesting hacking techniques that likely also apply to the WRTP54G / RTP300: http://sub.st/index.php?page=hacking_actiontec

See also:
[:AR7Port]

= Memory layout of RTP300 =
== /proc/mtd ==
{{{dev:    size   erasesize  name
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
 * mtd0 ''root'' is mounted as / (squashfs file system) since ''/proc/version'' is {{{Linux version 2.4.17_mvl21-malta-mips_fp_le (myron@dhcp-2123-3084) (gcc version 2.95.3 20010315 (release/MontaVista)) #1 Thu Oct 13 10:23:23 CST 2005}}} this FS is most likely a 1.x sqaushfs image like that in the Actiontec [http://wiki.openwrt.org/OpenWrtDocs/Hardware/Actiontec/GT701-WG GT701].
 * mtd5 and mtd6 begin with a "LMMC" header (hex 4C 4D 4D 43 00 03 00 00), each containing approximately 8-10kb worth of data almost the same exact size a backup config.bin file.  After removing the padding, neither file matches the config.bin taken from the running router's backup page.
 * mtd7 ''RESERVED_BOOTLOADER'' appears to contain a [:PSPBoot] bootloader, it has all of the environment variables which are available after boot time via ''/proc/ticfg/env''

== /proc/ticfg/env ==
(HWA_0, HWA_1, and SerialNumber have been anonymized)
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



= Pinouts =
== WRTP54G Serial Console ==

{{{________________________________________
|                                         |
|                                         led
|                   Pin 1: GND   ---> @   |
|                                         led
|         Pin 2: Not Connected   ---> @   |
|                                         led
|                   Pin 3: RX   ----> @   |                 Front of WRTP54G
|                                         led
|                   Pin 4: TX   ----> @   |
|                                         |
|                   Pin 5: VCC  ----> @   led
|                                         |
|                                         |
|                                         |
 \________________________________________|
}}}
The WRTP54G is *almost* a photo replica of the wag54gv2 hence the fccid of wag54gv2m.  The board layout differs slightly, although enough that the serial and jtag headers are positioned parallel to the front of the unit as opposed to the perpendicular alignment on the wag54gv2

== WRTP54G JTAG Pinout ==

{{{
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

The AR7 is based on ejtag version 2.6.

This ejtag layout should support all ar7 based boards with a 14 pin jtag pinout.  The same cable as used for the standard wrt54g (based on the xilinx III/dlc-5) as demonstrated by !HairyDairyMaid can be constructed and is well documented.  Debug INT pin 13 is optional and pin 14 can be left unhooked for passive cabling.

Since DMA Routines do '''not''' exist for this ejtag version (compared to ejtag v2.0 supported on the wrt54g) interfacing requires a rewrite utilizng prAcc routines of the v2.6 standard.

[http://www.dlinkpedia.net/index.php/Jtag_su_30xT JTAG for a similar AR7 device], [http://www.dlinkpedia.net/index.php/Interfaccia_JTAG JTAGInterface] (Italian!)

----
CategoryModel ["CategoryAR7Device"]
