= Linksys WRT160N / BootMessages =

[http://wiki.openwrt.org/OpenWrtDocs/Hardware/Linksys/WRT160N Return to WRT160N]

This is what shows on the serial console when booting Trunk OpenWRT 8-19-2008 with an additional kernel option enabled. 

 * Memory Technology Devices (MTD) -> RAM/ROM/Flash chip drivers -> Support 8-bit buswidth

Wireless looks to detect correctly by choosing the OpenWRT target profile (Generic, Broadcom WiFi (MIMO))

{{{Start to blink diag led ...


CFE version 1.0.37 for BCM947XX (32bit,SP,LE)
Build Date: Wed Dec 19 17:45:45 CST 2007 (root@localhost.localdomain)
Copyright (C) 2000,2001,2002,2003 Broadcom Corporation.

Initializing Arena
Initializing Devices.

No DPN
This is a Parallel Flash
Boot partition size = 262144(0x40000)
Partition information:
boot    #00   00000000 -> 0003FFFF  (262144)
trx     #01   00040000 -> 0004001B  (28)
os      #02   0004001C -> 003F7FFF  (3899364)
nvram   #03   003F8000 -> 003FFFFF  (32768)
Partition information:
boot    #00   00000000 -> 0003FFFF  (262144)
trx     #01   00040000 -> 003F7FFF  (3899392)
nvram   #02   003F8000 -> 003FFFFF  (32768)
et0: Broadcom BCM47xx 10/100 Mbps Ethernet Controller 4.150.10.16
et1: Broadcom BCM47xx 10/100 Mbps Ethernet Controller 4.150.10.16
CPU type 0x29006: 264MHz
Total memory: 16384 KBytes

Total memory used by CFE:  0x80700000 - 0x807963C0 (615360)
Initialized Data:          0x8072D210 - 0x8072F970 (10080)
BSS Area:                  0x8072F970 - 0x807303C0 (2640)
Local Heap:                0x807303C0 - 0x807943C0 (409600)
Stack Area:                0x807943C0 - 0x807963C0 (8192)
Text (code) segment:       0x80700000 - 0x8072D210 (184848)
Boot area (physical):      0x00797000 - 0x007D7000
Relocation Factor:         I:00000000 - D:00000000

Boot version: v4.7
The boot is CFE
mac_init(): Find mac [00:21:29:ab:94:7d] in location 1
Nothing...
CMD: [ifconfig eth0 -addr=192.168.1.1 -mask=255.255.255.0]
Device eth0:  hwaddr 00-21-29-AB-94-7D, ipaddr 192.168.1.1, mask 255.255.255.0
        gateway not set, nameserver not set
CMD: [go;]
Check CRC of image1
  Len:     0x1E0000     (1966080)       (0xBC040000)
  Offset0: 0x1C         (28)            (0xBC04001C)
  Offset1: 0x904        (2308)  (0xBC040904)
  Offset2: 0x7F000      (520192)        (0xBC0BF000)
  Header CRC:    0x335421EA
  Calculate CRC: 0x335421EA
Image 1 is OK
Try to load image 1.
Waiting for 5 seconds to upgrade ...
CMD: [load -raw -addr=0x807963c0 -max=0x770000 :]
Loader:raw Filesys:tftp Dev:eth0 File:: Options:(null)
Loading: _tftpd_open(): retries=0/5
_tftpd_open(): retries=1/5
_tftpd_open(): retries=2/5
_tftpd_open(): retries=3/5
_tftpd_open(): retries=4/5
Failed.
Could not load :: Timeout occured
CMD: [boot -raw -z -addr=0x80001000 -max=0x770000 flash0.os:]
Loader:raw Filesys:raw Dev:flash0.os File: Options:(null)
Loading: .. 3760 bytes read
Entry at 0x80001000
Closing network.
et0: link down
Starting program at 0x80001000
CPU revision is: 00029006
Primary instruction cache 16kB, physically tagged, 2-way, linesize 16 bytes.
Primary data cache 16kB, 2-way, linesize 16 bytes.
Linux version 2.4.35.4 (tpwn3r@bt) (gcc version 3.4.6 (OpenWrt-2.0)) #4 Fri Aug
22 19:39:10 GMT 2008
Setting the PFC to its default value
Determined physical RAM map:
 memory: 01000000 @ 00000000 (usable)
On node 0 totalpages: 4096
zone(0): 4096 pages.
zone(1): 0 pages.
zone(2): 0 pages.
Kernel command line: root=/dev/mtdblock2 rootfstype=squashfs,jffs2 init=/etc/pre
init noinitrd console=ttyS0,115200
CPU: BCM4704 rev 9 at 264 MHz
Using 132.000 MHz high precision timer.
Calibrating delay loop... 262.96 BogoMIPS
Memory: 14192k/16384k available (1486k kernel code, 2192k reserved, 100k data, 8
8k init, 0k highmem)
Dentry cache hash table entries: 2048 (order: 2, 16384 bytes)
Inode cache hash table entries: 1024 (order: 1, 8192 bytes)
Mount cache hash table entries: 512 (order: 0, 4096 bytes)
Buffer cache hash table entries: 1024 (order: 0, 4096 bytes)
Page-cache hash table entries: 4096 (order: 2, 16384 bytes)
Checking for 'wait' instruction...  unavailable.
POSIX conformance testing by UNIFIX
PCI: Initializing host
PCI: Enabling CardBus
PCI: Fixing up bus 0
PCI: Fixing up bridge
PCI: Fixing up bus 1
Linux NET4.0 for Linux 2.4
Based upon Swansea University Computer Society NET3.039
Initializing RT netlink socket
Starting kswapd
Registering mini_fo version $Id$
devfs: v1.12c (20020818) Richard Gooch (rgooch@atnf.csiro.au)
devfs: boot_options: 0x1
JFFS2 version 2.1. (C) 2001 Red Hat, Inc., designed by Axis Communications AB.
squashfs: version 3.0 (2006/03/15) Phillip Lougher
pty: 256 Unix98 ptys configured
Serial driver version 5.05c (2001-07-08) with MANY_PORTS SHARE_IRQ SERIAL_PCI en
abled
ttyS00 at 0xb8000300 (irq = 3) is a 16550A
ttyS01 at 0xb8000400 (irq = 3) is a 16550A
b44.c:v0.93 (Mar, 2004)
eth0: Broadcom 47xx 10/100BaseT Ethernet 00:21:29:ab:94:7d
eth1: Broadcom 47xx 10/100BaseT Ethernet 00:88:88:88:00:2a
 Amd/Fujitsu Extended Query Table v1.1 at 0x0040
number of CFI chips: 1
cfi_cmdset_0002: Disabling fast programming due to code brokenness.
Flash device: 0x400000 at 0x1c000000
bootloader size: 262144
Physically mapped flash: Filesystem type: squashfs, size=0x1522b4
Creating 5 MTD partitions on "Physically mapped flash":
0x00000000-0x00040000 : "cfe"
0x00040000-0x003f0000 : "linux"
0x000bf000-0x00220000 : "rootfs"
mtd: partition "rootfs" doesn't start on an erase block boundary -- force read-o
nly
0x003f0000-0x00400000 : "nvram"
0x00220000-0x003f0000 : "rootfs_data"
Initializing Cryptographic API
NET4: Linux TCP/IP 1.0 for NET4.0
IP Protocols: ICMP, UDP, TCP, IGMP
IP: routing cache hash table of 512 buckets, 4Kbytes
TCP: Hash tables configured (established 1024 bind 2048)
ip_conntrack version 2.1 (5953 buckets, 5953 max) - 344 bytes per conntrack
ip_tables: (C) 2000-2002 Netfilter core team
NET4: Unix domain sockets 1.0/SMP for Linux NET4.0.
NET4: Ethernet Bridge 008 for NET4.0
802.1Q VLAN Support v1.8 Ben Greear <greearb@candelatech.com>
All bugs added by David S. Miller <davem@redhat.com>
VFS: Mounted root (squashfs filesystem) readonly.
Mounted devfs on /dev
Freeing unused kernel memory: 88k freed
Algorithmics/MIPS FPU Emulator v1.5
mount: mounting sysfs on /sys failed: No such device
mount: mounting devfs on /dev failed: Device or resource busy
- preinit -
Press CTRL-C for failsafe
diag: Detected 'Linksys WRT54G/GS/GL'
b44: eth0: Link is up at 100 Mbps, full duplex.
b44: eth0: Flow control is off for TX and off for RX.
roboswitch: Probing device eth0: found!
switch-robo             5084   0 (unused)
switching to jffs2
mini_fo: using base directory: /
mini_fo: using storage directory: /jffs
- init -

Please press Enter to activate this console. jffs2.bbc: SIZE compression mode ac
tivated.
b44: eth0: Link is up at 100 Mbps, full duplex.
b44: eth0: Flow control is off for TX and off for RX.
b44: eth1: Link is up at 100 Mbps, full duplex.
b44: eth1: Flow control is off for TX and off for RX.
BFL_ENETADM not set in boardflags. Use force=1 to ignore.
PCI: Enabling device 01:01.0 (0004 -> 0006)
PCI/DMA
wl0: wlc_attach: chiprev 3 coreunit 0 corerev 12 cccap 0x864000d maccap 0x0 band
 2.4G, phy_type 4 phy_rev 2 ana_rev 5
wl0: Broadcom BCM4321 802.11 Wireless Controller 4.150.10.5
CSLIP: code copyright 1989 Regents of the University of California
PPP generic driver version 2.4.2
ipt_time loading



BusyBox v1.11.1 (2008-08-22 19:10:25 GMT) built-in shell (ash)
Enter 'help' for a list of built-in commands.

  _______                     ________        __
 |       |.-----.-----.-----.|  |  |  |.----.|  |_
 |   -   ||  _  |  -__|     ||  |  |  ||   _||   _|
 |_______||   __|_____|__|__||________||__|  |____|
          |__| W I R E L E S S   F R E E D O M
 KAMIKAZE (bleeding edge, r12360) -------------------
  * 10 oz Vodka       Shake well with ice and strain
  * 10 oz Triple sec  mixture into 10 shot glasses.
  * 10 oz lime juice  Salute!
 ---------------------------------------------------
root@OpenWrt:/#}}}
