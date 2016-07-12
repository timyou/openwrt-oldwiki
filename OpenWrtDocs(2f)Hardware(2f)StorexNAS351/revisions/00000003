= Briefly =
Works fine with openwrt-brcm-2.4-squashfs.trx.

Also works with openwrt-brcm47xx-squashfs.trx, but USB won't work.

= Software =
For IDE: kmod-ide-aec62xx kmod-ide-core

For USB (USB Storage, USB Printer sharing): kmod-usb2 kmod-usb-storage kmod-usb-printer usbutils p910nd kmod-usb-core kmod-usb-ohci kmod-usb-printer kmod-usb-uhci-iv

= dmesg =
{{{
CFE version 1.5.0 for BCM94780 (32bit,SP,LE)
Build Date: Wed Oct 11 18:05:28 PDT 2006 (builder@lc-sj1-703)
Copyright (C) 2000,2001,2002,2003 Broadcom Corporation.
Initializing Arena.
Initializing PCI. [normal]
PCI: Disabled
SB PCI init done
PCI bus 0 slot 0/0: vendor 0x14e4 product 0x0800 (flash memory, rev 0x08)
PCI bus 0 slot 1/0: vendor 0x14e4 product 0x4713 (ethernet network, rev 0x08)
PCI bus 0 slot 2/0: vendor 0x14e4 product 0x4713 (ethernet network, rev 0x08)
PCI bus 0 slot 3/0: vendor 0x14e4 product 0x4715 (USB serial bus, interface 0x10
, rev 0x08)
PCI bus 0 slot 5/0: vendor 0x14e4 product 0x0816 (MIPS processor, rev 0x08)
PCI bus 0 slot 6/0: vendor 0x14e4 product 0x4712 (modem communications, rev 0x08
)
PCI bus 0 slot 7/0: vendor 0x14e4 product 0x4718 (network/computing crypto, rev
0x08)
PCI bus 0 slot 8/0: vendor 0x14e4 product 0x080f (RAM memory, rev 0x08)
Initializing Devices.
et0: Broadcom BCM47xx 10/100 Mbps Ethernet Controller 3.90.39.0
CPU type 0x29006: 180MHz
Total memory: 0x4000000 bytes (64MB)
Total memory used by CFE:  0x80500000 - 0x80642570 (1320304)
Initialized Data:          0x8053BC80 - 0x8053EF20 (12960)
BSS Area:                  0x8053EF20 - 0x80540570 (5712)
Local Heap:                0x80540570 - 0x80640570 (1048576)
Stack Area:                0x80640570 - 0x80642570 (8192)
Text (code) segment:       0x80500000 - 0x8053BC80 (244864)
Boot area (physical):      0x00643000 - 0x00683000
Relocation Factor:         I:00000000 - D:00000000
ncdl value 0xfe0b
restoring NVRAM...done
CFE version 1.5.0 for BCM94780 (32bit,SP,LE)
Build Date: Wed Oct 11 18:05:28 PDT 2006 (builder@lc-sj1-703)
Copyright (C) 2000,2001,2002,2003 Broadcom Corporation.
Initializing Arena.
Initializing PCI. [normal]
PCI: Disabled
SB PCI init done
PCI bus 0 slot 0/0: vendor 0x14e4 product 0x0800 (flash memory, rev 0x08)
PCI bus 0 slot 1/0: vendor 0x14e4 product 0x4713 (ethernet network, rev 0x08)
PCI bus 0 slot 2/0: vendor 0x14e4 product 0x4713 (ethernet network, rev 0x08)
PCI bus 0 slot 3/0: vendor 0x14e4 product 0x4715 (USB serial bus, interface 0x10
, rev 0x08)
PCI bus 0 slot 5/0: vendor 0x14e4 product 0x0816 (MIPS processor, rev 0x08)
PCI bus 0 slot 6/0: vendor 0x14e4 product 0x4712 (modem communications, rev 0x08
)
PCI bus 0 slot 7/0: vendor 0x14e4 product 0x4718 (network/computing crypto, rev
0x08)
PCI bus 0 slot 8/0: vendor 0x14e4 product 0x080f (RAM memory, rev 0x08)
Initializing Devices.
et0: Broadcom BCM47xx 10/100 Mbps Ethernet Controller 3.90.39.0
CPU type 0x29006: 180MHz
Total memory: 0x4000000 bytes (64MB)
Total memory used by CFE:  0x80500000 - 0x80642570 (1320304)
Initialized Data:          0x8053BC80 - 0x8053EF20 (12960)
BSS Area:                  0x8053EF20 - 0x80540570 (5712)
Local Heap:                0x80540570 - 0x80640570 (1048576)
Stack Area:                0x80640570 - 0x80642570 (8192)
Text (code) segment:       0x80500000 - 0x8053BC80 (244864)
Boot area (physical):      0x00643000 - 0x00683000
Relocation Factor:         I:00000000 - D:00000000
ncdl value 0xfffefd
Using default boot cmd: CFE 3.91.39.0
Waiting to load image on IP , ^C to abort...Failed.: Error
Loader:raw Filesys:raw Dev:flash0.os File: Options:(null)
Loading: .. 3760 bytes read
Entry at 0x80001000
Starting program at 0x80001000
CPU revision is: 00029006
Primary instruction cache 16kB, physically tagged, 2-way, linesize 16 bytes.
Primary data cache 16kB, 2-way, linesize 16 bytes.
Linux version 2.4.35.4 (nbd@baustelle) (gcc version 3.4.6 (OpenWrt-2.0)) #27 Wed
 Jan 21 02:43:07 CET 2009
Setting the PFC to its default value
Determined physical RAM map:
 memory: 04000000 @ 00000000 (usable)
On node 0 totalpages: 16384
zone(0): 16384 pages.
zone(1): 0 pages.
zone(2): 0 pages.
Kernel command line: root=/dev/mtdblock2 rootfstype=squashfs,jffs2 init=/etc/pre
init noinitrd console=ttyS0,115200
CPU: BCM4704 rev 8 at 180 MHz
Using 90.000 MHz high precision timer.
Calibrating delay loop... 179.81 BogoMIPS
Memory: 62884k/65536k available (1425k kernel code, 2652k reserved, 100k data, 8
4k init, 0k highmem)
Dentry cache hash table entries: 8192 (order: 4, 65536 bytes)
Inode cache hash table entries: 4096 (order: 3, 32768 bytes)
Mount cache hash table entries: 512 (order: 0, 4096 bytes)
Buffer cache hash table entries: 4096 (order: 2, 16384 bytes)
Page-cache hash table entries: 16384 (order: 4, 65536 bytes)
Checking for 'wait' instruction...  unavailable.
POSIX conformance testing by UNIFIX
PCI: Initializing host
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
eth0: Broadcom 47xx 10/100BaseT Ethernet de:ad:de:ad:de:ad
eth1: Broadcom 47xx 10/100BaseT Ethernet 00:00:00:00:00:00
 Amd/Fujitsu Extended Query Table v1.3 at 0x0040
number of CFI chips: 1
cfi_cmdset_0002: Disabling fast programming due to code brokenness.
Flash device: 0x800000 at 0x1c000000
bootloader size: 262144
Physically mapped flash: Filesystem type: squashfs, size=0x180c3f
Creating 5 MTD partitions on "Physically mapped flash":
0x00000000-0x00040000 : "cfe"
0x00040000-0x007f0000 : "linux"
0x000bb000-0x00240000 : "rootfs"
mtd: partition "rootfs" doesn't start on an erase block boundary -- force read-o
nly
0x007f0000-0x00800000 : "nvram"
0x00240000-0x007f0000 : "rootfs_data"
Initializing Cryptographic API
NET4: Linux TCP/IP 1.0 for NET4.0
IP Protocols: ICMP, UDP, TCP, IGMP
IP: routing cache hash table of 512 buckets, 4Kbytes
TCP: Hash tables configured (established 4096 bind 8192)
NET4: Unix domain sockets 1.0/SMP for Linux NET4.0.
NET4: Ethernet Bridge 008 for NET4.0
802.1Q VLAN Support v1.8 Ben Greear <greearb@candelatech.com>
All bugs added by David S. Miller <davem@redhat.com>
VFS: Mounted root (squashfs filesystem) readonly.
Mounted devfs on /dev
Freeing unused kernel memory: 84k freed
Algorithmics/MIPS FPU Emulator v1.5
mount: mounting sysfs on /sys failed: No such device
mount: mounting devfs on /dev failed: Device or resource busy
- preinit -
Press CTRL-C for failsafe
diag: Router model not detected.
b44: eth0: Link is up at 100 Mbps, full duplex.
b44: eth0: Flow control is off for TX and off for RX.
roboswitch: Probing device eth0: No Robo switch in managed mode found
roboswitch: Probing device eth1: No Robo switch in managed mode found
roboswitch: Probing device eth2: No such device
roboswitch: Probing device eth3: No such device
switching to jffs2
jffs2_scan_empty(): Empty block at 0x005a000c ends at 0x005a8000 (with 0x48534c4
6)! Marking dirty
jffs2_scan_eraseblock(): Magic bitmask 0x1985 not found at 0x005a8000: 0x4c46 in
stead
jffs2_scan_eraseblock(): Magic bitmask 0x1985 not found at 0x005a8004: 0x00b8 in
stead
jffs2_scan_eraseblock(): Magic bitmask 0x1985 not found at 0x005a8008: 0x02d0 in
stead
jffs2_scan_eraseblock(): Magic bitmask 0x1985 not found at 0x005a800c: 0x8032 in
stead
jffs2_scan_eraseblock(): Magic bitmask 0x1985 not found at 0x005a8014: 0x7465 in
stead
jffs2_scan_eraseblock(): Magic bitmask 0x1985 not found at 0x005a8018: 0x6361 in
stead
jffs2_scan_eraseblock(): Magic bitmask 0x1985 not found at 0x005a801c: 0x7264 in
stead
jffs2_scan_eraseblock(): Magic bitmask 0x1985 not found at 0x005a8020: 0x2d65 in
stead
jffs2_scan_eraseblock(): Magic bitmask 0x1985 not found at 0x005a8024: 0x642d in
stead
Further such events for this erase block will not be printed
mini_fo: using base directory: /
mini_fo: using storage directory: /jffs
- init -
Uniform Multi-Platform E-IDE driver Revision: 7.00beta4-2.4
ide: Assuming 33MHz system bus speed for PIO modes; override with idebus=xx
AEC6X80: IDE controller at PCI slot 01:02.0
PCI: Enabling device 01:02.0 (0000 -> 0003)
AEC6X80: chipset revision 16
AEC6X80: not 100% native mode: will probe irqs later
ide: Assuming 33MHz system bus speed for PIO modes; override with idebus=xx
    ide0: BM-DMA at 0x0180-0x0187, BIOS settings: hda:pio, hdb:pio
    ide1: BM-DMA at 0x0188-0x018f, BIOS settings: hdc:pio, hdd:pio
hda: Hitachi HDT725040VLA380, ATA DISK drive
ide0 at 0x100-0x107,0x10a on irq 2
hda: attached ide-disk driver.
hda: host protected area => 1
hda: 781422768 sectors (400088 MB) w/7372KiB Cache, CHS=48641/255/63, UDMA(33)
Partition check:
 /dev/ide/host0/bus0/target0/lun0: p1 p2
reiserfs: found format "3.6" with standard journal
reiserfs: checking transaction log (device ide0(3,1)) ...
for (ide0(3,1))
reiserfs: replayed 26 transactions in 0 seconds
ide0(3,1):Using r5 hash to sort names
Please press Enter to activate this console. jffs2.bbc: SIZE compression mode ac
tivated.
b44: eth0: Link is up at 100 Mbps, full duplex.
b44: eth0: Flow control is off for TX and off for RX.
b44: eth0: Link is up at 100 Mbps, full duplex.
b44: eth0: Flow control is off for TX and off for RX.
SCSI subsystem driver Revision: 1.00
roboswitch: Probing device eth0: No Robo switch in managed mode found
roboswitch: Probing device eth1: No Robo switch in managed mode found
roboswitch: Probing device eth2: No such device
roboswitch: Probing device eth3: No such device
usb.c: registered new driver usbdevfs
usb.c: registered new driver hub
Journalled Block Device driver loaded
CSLIP: code copyright 1989 Regents of the University of California
PPP generic driver version 2.4.2
ip_tables: (C) 2000-2002 Netfilter core team
ip_conntrack version 2.1 (5953 buckets, 5953 max) - 360 bytes per conntrack
SB USB 1.1 init
usb-ohci.c: USB OHCI at membase 0xb8003000, IRQ 6
usb-ohci.c: usb-00:03.0, PCI device 14e4:4715
usb.c: new USB bus registered, assigned bus number 1
hub.c: USB hub found
hub.c: 2 ports detected
usb-uhci.c: $Revision: 1.275 $ time 06:14:26 Jan 11 2009
usb-uhci.c: High bandwidth mode enabled
PCI: Enabling device 01:03.0 (0000 -> 0001)
UHCI: Enabling VIA 6212 workarounds
usb-uhci.c: USB UHCI at I/O 0x200, IRQ 2
usb-uhci.c: Detected 2 ports
usb.c: new USB bus registered, assigned bus number 2
hub.c: USB hub found
hub.c: 2 ports detected
PCI: Enabling device 01:03.1 (0000 -> 0001)
UHCI: Enabling VIA 6212 workarounds
usb-uhci.c: USB UHCI at I/O 0x220, IRQ 2
usb-uhci.c: Detected 2 ports
usb.c: new USB bus registered, assigned bus number 3
hub.c: USB hub found
hub.c: 2 ports detected
usb-uhci.c: v1.275:USB Universal Host Controller Interface driver
PCI: Enabling device 01:03.2 (0000 -> 0002)
ehci_hcd 01:03.2: PCI device 1106:3104
ehci_hcd 01:03.2: irq 2, pci mem c02ae000
usb.c: new USB bus registered, assigned bus number 4
EHCI: Enabling VIA 6212 workarounds
ehci_hcd 01:03.2: USB 2.0 enabled, EHCI 1.00, driver 2003-Dec-29/2.4
hub.c: USB hub found
hub.c: 4 ports detected
No Broadcom devices found.
usb.c: registered new driver usblp
printer.c: v0.13: USB Printer Device Class driver
hub.c: connect-debounce failed, port 1 disabled
Initializing USB Mass Storage driver...
usb.c: registered new driver usb-storage
USB Mass Storage support registered.
reiserfs: found format "3.6" with standard journal
hub.c: port 4 over-current change
hub.c: new USB device 01:03.0-1, assigned address 2
printer.c: usblp0: USB Bidirectional printer dev 2 if 0 alt 0 proto 2 vid 0x04F9
 pid 0x0027
reiserfs: checking transaction log (device ide0(3,2)) ...
for (ide0(3,2))
reiserfs: replayed 2 transactions in 0 seconds
ide0(3,2):Using r5 hash to sort names
BusyBox v1.11.2 (2009-01-06 07:18:07 CET) built-in shell (ash)
Enter 'help' for a list of built-in commands.
  _______                     ________        __
 |       |.-----.-----.-----.|  |  |  |.----.|  |_
 |   -   ||  _  |  -__|     ||  |  |  ||   _||   _|
 |_______||   __|_____|__|__||________||__|  |____|
          |__| W I R E L E S S   F R E E D O M
 KAMIKAZE (8.09, r14127) ----------------------------
  * 10 oz Vodka       Shake well with ice and strain
  * 10 oz Triple sec  mixture into 10 shot glasses.
  * 10 oz lime juice  Salute!
 ---------------------------------------------------}}}
