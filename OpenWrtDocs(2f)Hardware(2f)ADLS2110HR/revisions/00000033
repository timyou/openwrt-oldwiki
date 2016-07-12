== Specifications ==
ADSL modem with ADSL2/2+ support to 24Mbit/s+, it has port 1 LAN port.

STAR-NET ADSL 2110EHR V7.20M+

PCB: 2110EH V7.20+ 2005.11.30

PCB Photo: attachment:2110EH_V720plus_2005_11_30.jpg

serial console 9600,n,8,1,hw jp1:

1 VCC 2 TX 3 RX 4 -- 5--  6 GND 7 GND

Flash chip: 2MBytes KH KH29LV160CBTC-70G KH29LV160CBTC 29LV160

SDRAM: 8Mbytes Winbound W9864G6GH-6 W9864G6GH 4Mx16 4 Banks CL3 3.3 V TSOP II 54 (400 mil) -6 166 MHz http://www.winbond-usa.com/mambo/content/view/123/238/

CPU: Texas Instruments AR7 MIPS based TI TNETD7100GDW TNETD7100

http://focus.ti.com/general/docs/bcg/bcgprodcontent.tsp?templateId=6116&navigationId=12111&contentId=4001

http://focus.ti.com/pdfs/bcg/ar7_prod_bulletin.pdf

== Original settings ==
The Flash memory is divided into blocks:
||||||||<style="TEXT-ALIGN: center">'''Default memory mappings''' ||
||Name ||Start ||End ||Description ||
||mtd0 ||0x90096000 ||0x90200000 ||Filesystem ||
||mtd1 ||0x90020090 ||0x90096000 ||Kernel ||
||mtd2 ||0x90000000 ||0x90010000 ||Bootloader ||
||mtd3 ||0x90010000 ||0x90020000 ||Configuration ||
||mtd4 ||0x90020000 ||0x90200000 ||Filesystem + Kernel ||

{{{
BUILD_OPS             0x301
bootloaderVersion     1.3.7.15
ProductID             AR7RD
HWRevision            Unknown
SerialNumber          none
MAC_PORT              0
MEMSZ                 0x00800000
FLASHSZ               0x00200000
MODETTY0              9600,n,8,1,hw
MODETTY1              9600,n,8,1,hw
CPUFREQ               211968000
MIPSFREQ              211968000
PROMPT                (psbl)
IPA                   192.168.1.1
mtd2                  0x90000000,0x90010000
mtd3                  0x90010000,0x90020000
mtd4                  0x90020000,0x90200000
BOOTCFG               m:f:"mtd1"
StaticBuffer          120
mtd1                  0x90020090,0x90096000
mtd0                  0x90096000,0x90200000
vcc_encaps0           0.0
vcc_encaps1           0.0
vcc_encaps2           0.0
vcc_encaps3           0.0
vcc_encaps4           0.0
vcc_encaps5           0.0
vcc_encaps6           0.0
vcc_encaps7           0.0
usb_vid               0x0451
usb_pid               0x6060
HWA_RNDIS             00:E0:A6:66:41:EB
HWA_HRNDIS            00:E0:A6:66:41:E1
connection0           0x1b00
connection1           0xf00
SYSFREQ               105984000
modulation            0xff
HWA_0                 00:D0:F8:73:0D:AD
HWA_2                 00:D0:F8:73:0D:AE
HWA_3                 00:D0:F8:73:0D:AE
}}}

== Default Telnet login/password ==
2110EHR v7.20M+ login: root password: admin

== Dump Original Firmware ==
mtd4: 001e0000 00010000 "mtd4" 0x1e0000=1966080/2=983040

{{{
# mkdir /var/dump
# /usr/sbin/thttpd -d /var/dump -u root -p 1080 -g
# dd if=/dev/mtdblock/2 of=/var/dump/mtd2-boot.bin
# dd if=/dev/mtdblock/3 of=/var/dump/mtd3-nvram.bin
# dd if=/lib/modules/ar0700xx.bin of=/var/dump/ar0700xx.bin
http://192.168.1.1:1080/mtd2-boot.bin
http://192.168.1.1:1080/mtd3-nvram.bin
http://192.168.1.1:1080/ar0700xx.bin
#reboot

# mkdir /var/dump
# /usr/sbin/thttpd -d /var/dump -u root -p 1080 -g
# dd if=/dev/mtdblock/4 of=/var/dump/mtd4-fs-kern1.bin count=983040 bs=1
http://192.168.1.1:1080/mtd4-fs-kern1.bin
#reboot

# mkdir /var/dump
# /usr/sbin/thttpd -d /var/dump -u root -p 1080 -g
# dd if=/dev/mtdblock/4 of=/var/dump/mtd4-fs-kern2.bin skip=983040 count=983040 bs=1
http://192.168.1.1:1080/mtd4-fs-kern2.bin
#reboot

}}}

cat mtd4-fs-kern1.bin mtd4-fs-kern2.bin > mtd4-fs-kern.bin 


== Boot Log ==
{{{
Basic POST completed...     Success.
Last reset cause: Hardware reset (Power-on reset)
PSPBoot1.3 rev: 1.3.7.15
(c) Copyright 2002-2005 Texas Instruments, Inc. All Rights Reserved.
Press ESC for monitor... 3321
(psbl) 
Booting...
Launching kernel decompressor.
Starting LZMA Uncompression Algorithm.
Copyright (C) 2003 Texas Instruments Incorporated; Copyright (C) 1999-2003 Igor Pavlov.
Compressed file is LZMA format.
Kernel decompressor was successful ... launching kernel.
LINUX started...
Config serial console: ttyS0,9600
Auto Detection OHIO chip
This SOC has MDIX cababilities on chip.
CPU revision is: 00018448
Primary instruction cache 16kb, linesize 16 bytes (4 ways)
Primary data cache 8kb, linesize 16 bytes (4 ways)
Number of TLB entries 16.
Linux version 2.4.17_mvl21-malta-mips_fp_le (root@localhost.localdomain) (gcc version 2.95.3 20010315 (release/MontaVista)) #16 Т> 2ФВ 13 16:52:30 CST 2006
Determined physical RAM map:
 memory: 14000000 @ 00000000 (reserved)
 memory: 00020000 @ 14000000 (ROM data)
 memory: 007e0000 @ 14020000 (usable)
On node 0 totalpages: 2048
zone(0): 2048 pages.
zone(1): 0 pages.
zone(2): 0 pages.
Kernel command line: 
calculating r4koff... 00102c00(1059840)
CPU frequency 211.97 MHz
Calibrating delay loop... 211.35 BogoMIPS
Freeing Adam2 reserved memory [0x14001000,0x0001f000]
Memory: 6344k/8192k available (1456k kernel code, 1848k reserved, 99k data, 60k init)
Dentry-cache hash table entries: 1024 (order: 1, 8192 bytes)
Inode-cache hash table entries: 512 (order: 0, 4096 bytes)
Mount-cache hash table entries: 512 (order: 0, 4096 bytes)
Buffer-cache hash table entries: 1024 (order: 0, 4096 bytes)
Page-cache hash table entries: 2048 (order: 1, 8192 bytes)
Checking for 'wait' instruction...  unavailable.
POSIX conformance testing by UNIFIX
Linux NET4.0 for Linux 2.4
Based upon Swansea University Computer Society NET3.039
TI Optimizations: Allocating TI-Cached Memory Pool.
Using 120 Buffers for TI-Cached Memory Pool.
DEBUG: Using Hybrid Mode.
NSP Optimizations: Succesfully allocated TI-Cached Memory Pool.
Initializing RT netlink socket
Starting kswapd
Disabling the Out Of Memory Killer
devfs: v1.7 (20011216) Richard Gooch (rgooch@atnf.csiro.au)
devfs: boot_options: 0x1
pty: 32 Unix98 ptys configured
Serial driver version 5.05c (2001-07-08) with no serial options enabled
ttyS00 at 0xa8610e00 (irq = 15) is a 16550A
block: 64 slots per queue, batch=16
DEBUG: Initializing the voice port management module. 
DEBUG: Initialization of the voice port management module successful..
Error getting CPMAC Configuration params for instance:0
Environment Variable:MACCFG_A not set in bootloader
Setting Default configuration params for CPMAC instance:0
Default Asymmetric MTU for eth0 1500
TI CPMAC Linux DDA version 1.8 - CPMAC DDC version 0.2
Cpmac: Installed 1 instances.
Cpmac driver is allocating buffer memory at init time.
PPP generic driver version 2.4.1
avalanche flash device: 0x400000 at 0x10000000.
 Amd/Fujitsu Extended Query Table v1.0 at 0x0040
number of CFI chips: 1
Looking for mtd device :mtd0:
Found a mtd0 image (0x96000), with size (0x16a000).
Creating 1 MTD partitions on "Physically mapped flash:0":
0x00096000-0x00200000 : "mtd0"
mtd: partition "mtd0" doesn't start on an erase block boundary -- force read-only
Looking for mtd device :mtd1:
Found a mtd1 image (0x20090), with size (0x75f70).
Creating 1 MTD partitions on "Physically mapped flash:0":
0x00020090-0x00096000 : "mtd1"
mtd: partition "mtd1" doesn't start on an erase block boundary -- force read-only
Looking for mtd device :mtd2:
Found a mtd2 image (0x0), with size (0x10000).
Creating 1 MTD partitions on "Physically mapped flash:0":
0x00000000-0x00010000 : "mtd2"
Looking for mtd device :mtd3:
Found a mtd3 image (0x10000), with size (0x10000).
Creating 1 MTD partitions on "Physically mapped flash:0":
0x00010000-0x00020000 : "mtd3"
Looking for mtd device :mtd4:
Found a mtd4 image (0x20000), with size (0x1e0000).
Creating 1 MTD partitions on "Physically mapped flash:0":
0x00020000-0x00200000 : "mtd4"
NET4: Linux TCP/IP 1.0 for NET4.0
IP Protocols: ICMP, UDP, TCP, IGMP
IP: routing cache hash table of 512 buckets, 4Kbytes
TCP: Hash tables configured (established 512 bind 512)
Linux IP multicast router 0.06 plus PIM-SM
ip_conntrack version 2.0 (64 buckets, 512 max) - 364 bytes per conntrack
ip_tables: (c)2000 Netfilter core team
netfilter PSD loaded - (c) astaro AG
NET4: Unix domain sockets 1.0/SMP for Linux NET4.0.
NET4: Ethernet Bridge 008 for NET4.0
Initializing the WAN Bridge.
Please set the MAC Address for the WAN Bridge.
Set the Environment variable 'wan_br_mac'. 
MAC Address should be in the following format: xx.xx.xx.xx.xx.xx
VFS: Mounted root (squashfs filesystem) readonly.
Mounted devfs on /dev
Freeing unused kernel memory: 60k freed
serial console detected.  Disabling virtual terminals.
console=/dev/tts/0
init started:  BusyBox v0.61.pre (2006.02.13-04:01+0000) multi-call binary
Starting pid 9, console /dev/tts/0: '/etc/init.d/rcS'
Algorithmics/MIPS FPU Emulator v1.5
 Reading Standard Configuration File /etc/led.conf
 Configured 15 states 
Using /lib/modules/2.4.17_mvl21-malta-mips_fp_le/kernel/drivers/net/avalanche_usb/avalanche_usb.o
USB: Entering USB_init_module.
USB Driver built for RNDIS-CDC protocols.
Error getting protocol configuration from bootloader environment.
Defaulting to "RNDIS-CDC" mode.
VID = 0x451
PID = 0x6060
No Serial Number String present.
Manufacturer = Texas Instruments                      
Product description = Texas Instruments CDC Ethernet/RNDIS Adapter        
USB: Entering USB_Init.
USB: Leaving USB_Init.
Default Asymmetric MTU for usb0 1500
USB: Leaving USB_init_module.
Using /lib/modules/2.4.17_mvl21-malta-mips_fp_le/kernel/drivers/atm/tiatm.o
registered device TI Avalanche SAR
Ohio250(7200/7100A2) detected
DSP binary filesize = 356930 bytes
tn7dsl_set_modulation : Setting mode to 0xff
Texas Instruments ATM driver: version:[6.00.01.00]
Waiting for enter to start '/bin/sh' (pid 35, terminal /dev/tts/0)
Please press Enter to activate this console. SIOCGIFFLAGS: No such device
SIOCGIFFLAGS: No such device
SIOCGIFFLAGS: No such device
Sep  8 12:00:14 cfgmgr(sar):  Error: Could not find oam_ping_interval
}}}

== Information ==
{{{
# cat /proc/iomem
odulation_schemes
00000000-13ffffff : reserved
14000000-1401ffff : System RAM
14020000-147fffff : System RAM
  14020000-1418c28f : Kernel code
  1419d300-141b5fff : Kernel data
a8610000-a86107ff : eth0

# cat /proc/mounts
/dev/mtdblock/0 / squashfs ro 0 0
none /dev devfs rw 0 0
proc /proc proc rw 0 0
ramfs /var ramfs rw 0 0

# cat /proc/tty/driver/serial
serinfo:1.0 driver:5.05c revision:2001-07-08
0: uart:16550A port:A8610E00 irq:15 baud:667 tx:3741 rx:0 RTS|DTR
1: uart:unknown port:A8610F00 irq:16

# cat /proc/cpuinfo
processor               : 0
cpu model               : MIPS 4KEc V4.8
BogoMIPS                : 211.35
wait instruction        : no
microsecond timers      : yes
extra interrupt vector  : yes
hardware watchpoint     : yes
VCED exceptions         : not available
VCEI exceptions         : not available

# cat /proc/mtd
dev:    size   erasesize  name
mtd0: 0016a000 00010000 "mtd0"
mtd1: 00075f70 00010000 "mtd1"
mtd2: 00010000 00008000 "mtd2"
mtd3: 00010000 00010000 "mtd3"
mtd4: 001e0000 00010000 "mtd4"

# cat /proc/version
Linux version 2.4.17_mvl21-malta-mips_fp_le (root@localhost.localdomain) (gcc version
 2.95.3 20010315 (release/MontaVista)) #16 T┐ 2LT 13 16:52:30 CST 2006

# cat /proc/avalanche/avsar_ver
ATM Driver version:[6.00.01.00]
DSL HAL version: [6.00.01.00]
DSP Datapump version: [6.00.02.00] Annex A
SAR HAL version: [01.07.2b]
PDSP Firmware version:[0.54]
Chipset ID: [Ohio250(7200/7100A2)]

# cat /proc/avalanche/cpmac_ver
Texas Instruments : CPMAC Linux DDA version 1.8
Texas Instruments : CPMAC DDC version 0.2

# cat /proc/avalanche/psp_version
Linux OS DSL-PSP version 4.6.1.9 on BasePSP Version 7.1.0.8 Feb 13 2006 11:58:03 Aval
anche SOC Version: 0x11002b operating in cached, write back, write allocate mode Cpu
Frequency:211 MHZ System Bus frequency: 105 MHZ

# cat /proc/avalanche/usb0_ver
Texas Instruments USB CDC/RNDIS Driver Version 1.1.1
Built for CDC-RNDIS protocol(s).
}}}

== ACORP LAN120M firmware ==
http://mcmcc.bat.ru/acorp/LAN120M/Acorp_nsp_LAN120_V.1.1.00.RU.23102007_AnnexA_DSP74.zip

{{{
mtd0 0x90094000,0x901F0000
mtd1 0x90020090,0x90094000
mtd2 0x90000000,0x90010000
mtd3 0x90010000,0x90020000
mtd4 0x90020000,0x901F0000
mtd5 0x901F0000,0x90200000
}}}

Add mtd5 and change mtd0 & mtd4
{{{
# echo "mtd5 0x901F0000,0x90200000" > /proc/ticfg/env 
# echo "mtd4 0x90020000,0x901F0000" > /proc/ticfg/env
# echo "mtd0 0x90094000,0x901F0000" > /proc/ticfg/env
}}}

DATA led fix:
{{{
# cd /var/var
# tftp -g -l mycfg.tar.gz 192.168.0.90
# cat mycfg.tar.gz > /dev/mtdblock/5
}}}

attachment:mycfg.tar.gz

----
 . ["CategoryAR7Device"]
