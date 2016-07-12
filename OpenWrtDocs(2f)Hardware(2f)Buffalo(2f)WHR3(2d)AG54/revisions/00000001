 * LAN: br0 = eth0 eth2
 * WAN: eth1

dmesg:
{{{
CPU revision is: 00029006
Primary instruction cache 16kB, physically tagged, 2-way, linesize 16 bytes.
Primary data cache 16kB, 2-way, linesize 16 bytes.
Linux version 2.4.30 (nbd@ux-2y02) (gcc version 3.4.4 (OpenWrt-1.0)) #1 Sun Mar 26 19:02:04 CEST 2006
Setting the PFC value as 0x15
Determined physical RAM map:
 memory: 04000000 @ 00000000 (usable)
On node 0 totalpages: 16384
zone(0): 16384 pages.
zone(1): 0 pages.
zone(2): 0 pages.
Kernel command line: root=/dev/mtdblock2 rootfstype=squashfs,jffs2 init=/etc/preinit noinitrd console=ttyS0,115200
CPU: BCM4704 rev 8 at 264 MHz
Using 132.000 MHz high precision timer.
Calibrating delay loop... 263.78 BogoMIPS
Memory: 62892k/65536k available (1412k kernel code, 2644k reserved, 100k data, 80k init, 0k highmem)
Dentry cache hash table entries: 8192 (order: 4, 65536 bytes)
Inode cache hash table entries: 4096 (order: 3, 32768 bytes)
Mount cache hash table entries: 512 (order: 0, 4096 bytes)
Buffer cache hash table entries: 4096 (order: 2, 16384 bytes)
Page-cache hash table entries: 16384 (order: 4, 65536 bytes)
Checking for 'wait' instruction...  unavailable.
POSIX conformance testing by UNIFIX
PCI: Fixing up bus 0
PCI: Fixing up bridge
PCI: Setting latency timer of device 01:00.0 to 64
PCI: Fixing up bus 1
Linux NET4.0 for Linux 2.4
Based upon Swansea University Computer Society NET3.039
Initializing RT netlink socket
Starting kswapd
devfs: v1.12c (20020818) Richard Gooch (rgooch@atnf.csiro.au)
devfs: boot_options: 0x1
JFFS2 version 2.1. (C) 2001 Red Hat, Inc., designed by Axis Communications AB.
Squashfs 2.1-r2 (released 2004/12/15) (C) 2002-2004 Phillip Lougher
pty: 256 Unix98 ptys configured
Serial driver version 5.05c (2001-07-08) with MANY_PORTS SHARE_IRQ SERIAL_PCI enabled
ttyS00 at 0xb8000300 (irq = 3) is a 16550A
ttyS01 at 0xb8000400 (irq = 0) is a 16550A
b44.c:v0.93 (Mar, 2004)
PCI: Setting latency timer of device 00:01.0 to 64
eth0: Broadcom 47xx 10/100BaseT Ethernet 00:0d:0b:65:02:f4
PCI: Setting latency timer of device 00:02.0 to 64
eth1: Broadcom 47xx 10/100BaseT Ethernet 00:0d:0b:65:02:f5
Physically mapped flash: Found an alias at 0x400000 for the chip at 0x0
Physically mapped flash: Found an alias at 0x800000 for the chip at 0x0
Physically mapped flash: Found an alias at 0xc00000 for the chip at 0x0
Physically mapped flash: Found an alias at 0x1000000 for the chip at 0x0
Physically mapped flash: Found an alias at 0x1400000 for the chip at 0x0
Physically mapped flash: Found an alias at 0x1800000 for the chip at 0x0
Physically mapped flash: Found an alias at 0x1c00000 for the chip at 0x0
 Amd/Fujitsu Extended Query Table v1.0 at 0x0040
number of CFI chips: 1
cfi_cmdset_0002: Disabling fast programming due to code brokenness.
Flash device: 0x400000 at 0x1c000000
Creating 5 MTD partitions on "Physically mapped flash":
0x00000000-0x00040000 : "pmon"
0x00040000-0x003f0000 : "linux"
0x000bc400-0x001b6000 : "rootfs"
mtd: partition "rootfs" doesn't start on an erase block boundary -- force read-only
0x003f0000-0x00400000 : "nvram"
0x001c0000-0x003f0000 : "OpenWrt"
Initializing Cryptographic API
NET4: Linux TCP/IP 1.0 for NET4.0
IP Protocols: ICMP, UDP, TCP, IGMP
IP: routing cache hash table of 512 buckets, 4Kbytes
TCP: Hash tables configured (established 4096 bind 8192)
ip_conntrack version 2.1 (5953 buckets, 5953 max) - 328 bytes per conntrack
ip_tables: (C) 2000-2002 Netfilter core team
NET4: Unix domain sockets 1.0/SMP for Linux NET4.0.
NET4: Ethernet Bridge 008 for NET4.0
802.1Q VLAN Support v1.8 Ben Greear <greearb@candelatech.com>
All bugs added by David S. Miller <davem@redhat.com>
VFS: Mounted root (squashfs filesystem) readonly.
Mounted devfs on /dev
Freeing unused kernel memory: 80k freed
Algorithmics/MIPS FPU Emulator v1.5
diag boardtype: 0000042f
Probing device eth0: No Robo switch in managed mode found
Probing device eth1: No Robo switch in managed mode found
Probing device eth2: No such device
Probing device eth3: No such device
BFL_ENETADM not set in boardflags. Use force=1 to ignore.
b44: eth0: Link is up at 100 Mbps, full duplex.
b44: eth0: Flow control is off for TX and off for RX.
jffs2.bbc: SIZE compression mode activated.
PCI: Setting latency timer of device 01:01.0 to 64
PCI: Enabling device 01:01.0 (0004 -> 0006)
eth2: Broadcom BCM4324 802.11 Wireless Controller 3.90.37.0
Probing device eth0: No Robo switch in managed mode found
Probing device eth1: No Robo switch in managed mode found
Probing device eth2: [switch-robo.c:90] SIOCGETCPHYRD failed!
[switch-robo.c:90] SIOCGETCPHYRD failed!
No Robo switch in managed mode found
Probing device eth3: No such device
BFL_ENETADM not set in boardflags. Use force=1 to ignore.
device eth0 entered promiscuous mode
device eth2 entered promiscuous mode
br0: port 2(eth2) entering learning state
br0: port 1(eth0) entering learning state
br0: port 2(eth2) entering forwarding state
br0: topology change detected, propagating
br0: port 1(eth0) entering forwarding state
br0: topology change detected, propagating
b44: eth1: Link is up at 100 Mbps, full duplex.
b44: eth1: Flow control is off for TX and off for RX.
CSLIP: code copyright 1989 Regents of the University of California
PPP generic driver version 2.4.2
b44: eth1: Link is up at 100 Mbps, full duplex.
b44: eth1: Flow control is off for TX and off for RX.
}}}
