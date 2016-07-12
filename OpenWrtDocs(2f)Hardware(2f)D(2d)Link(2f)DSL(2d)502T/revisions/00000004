= Work in Progress =
Porting OpenWrt to the DSL-502T is a work in progress. This page is to assist those working in that direction.

Thanks Strider for starting the page off & thank you nbd + all the openwrt guys for making this work - Z3r0
Kamikaze build 5174 works on the DSL-502T AU & AT

== Specifications ==
ADSL modem with ADSL2 support to 8Mbit/s, it has port 1 LAN port

Flash chip: 4MBytes - Samsung K8D3216UBC a 32Mbit NOR-type Flash Memory organized as 4M x 8

SDRAM: 16Mbytes - Nanya NT5SV8M16DS-6K

CPU: TNETD7300GDU Texas Instruments AR7 MIPS based
'''
'''
== How to get OpenWRT onto the router: ==
== How to Debrick: ==
See the forum for how to debrick the DSL-502T[[BR]]http://forum.openwrt.org/viewtopic.php?id=7742[[BR]]
== OpenWRT logs and so on... ==
'''Telnet/SSH Login screen'''
BusyBox v1.2.1 (2006.10.17-01:23+0000) Built-in shell (ash)
Enter 'help' for a list of built-in commands.
_______                     ________        __
|       |.-----.-----.-----.|  |  |  |.----.|  |_
|   -   ||  _  |  -__|     ||  |  |  ||   _||   _|
|_______||   __|_____|__|__||________||__|  |____|
|__| W I R E L E S S   F R E E D O M
KAMIKAZE (bleeding edge, r5174) -------------------
* 10 oz Vodka       Shake well with ice and strain
* 10 oz Triple sec  mixture into 10 shot glasses.
* 10 oz lime juice  Salute!
---------------------------------------------------
'''DMESG'''
<4>CPU revision is: 00018448
<4>Primary instruction cache 16kB, physically tagged, 4-way, linesize 16 bytes.
<4>Primary data cache 16kB, 4-way, linesize 16 bytes.
<4>Linux version 2.4.32 (root@ZPC) (gcc version 3.4.6 (OpenWrt-2.0)) #2 Tue Oct                               17 11:29:52 EST 2006
<4>Determined physical RAM map:
<4> memory: 00020000 @ 14000000 (ROM data)
<4> memory: 00fe0000 @ 14020000 (usable)
<4>On node 0 totalpages: 4096
<4>zone(0): 4096 pages.
<4>zone(1): 0 pages.
<4>zone(2): 0 pages.
<4>Kernel command line: root=/dev/mtdblock2 rootfstype=squashfs,jffs2 init=/etc/                              preinit noinitrd console=ttyS0,38400
<7>set_except_vector: using long jump via k0 to reach 94025200
<4>the pacing pre-scalar has been set as 600.
<7>set_except_vector: using long jump via k0 to reach 94151f40
<4>Using 75.000 MHz high precision timer.
<4>Calibrating delay loop... 149.91 BogoMIPS
<6>Memory: 14292k/16384k available (1346k kernel code, 2092k reserved, 92k data,                               72k init, 0k highmem)
<6>Dentry cache hash table entries: 2048 (order: 2, 16384 bytes)
<6>Inode cache hash table entries: 1024 (order: 1, 8192 bytes)
<6>Mount cache hash table entries: 512 (order: 0, 4096 bytes)
<6>Buffer cache hash table entries: 1024 (order: 0, 4096 bytes)
<4>Page-cache hash table entries: 4096 (order: 2, 16384 bytes)
<4>Checking for 'wait' instruction...  available.
<4>POSIX conformance testing by UNIFIX
<6>Linux NET4.0 for Linux 2.4
<6>Based upon Swansea University Computer Society NET3.039
<4>Initializing RT netlink socket
<4>Starting kswapd
<6>devfs: v1.12c (20020818) Richard Gooch (rgooch@atnf.csiro.au)
<6>devfs: boot_options: 0x1
<5>JFFS2 version 2.1. (C) 2001 Red Hat, Inc., designed by Axis Communications AB                              .
<6>squashfs: version 3.0 (2006/03/15) Phillip Lougher
<4>pty: 256 Unix98 ptys configured
<6>Serial driver version 5.05c (2001-07-08) with no serial options enabled
<6>ttyS00 at 0xa8610e00 (irq = 15) is a 16550A
<6>ttyS01 at 0xa8610f00 (irq = 16) is a 16550A
<4>VLYNQ INIT FAILED: Please try cold reboot.
<4>Vlynq CONFIG_AR7_VLYNQ_PORTS=2
<4>Vlynq Device vlynq0 registered with minor no 63 as misc device. Result=0
<4>VLYNQ 0 : init failed
<4>Vlynq Device vlynq1 registered with minor no 62 as misc device. Result=0
<4>VLYNQ 1 : init failed
<6>ar7_wdt: last system reset initiated by hardware reset
<7>ar7_wdt: disabling watchdog timer
<6>ar7_wdt: timer margin 59 seconds (prescale 65535, change 57180, freq 62500000                              )
<5>ar7 flash device: 0x400000 at 0x10000000.
<5> Amd/Fujitsu Extended Query Table v3.3 at 0x0040
<5>number of CFI chips: 1
<5>cfi_cmdset_0002: Disabling fast programming due to code brokenness.
<4>Parsing ADAM2 partition map...
<4>Looking for mtd device :mtd0:
<4>Found a mtd0 image (0x850e0), with size (0x36af20).
<4>Assuming default rootfs offset of 0x850e0
<4>Looking for mtd device :mtd1:
<4>Found a mtd1 image (0x10000), with size (0x750e0).
<4>Looking for mtd device :mtd2:
<4>Found a mtd2 image (0x0), with size (0x10000).
<4>Assuming adam2 size of 0x10000
<4>Looking for mtd device :mtd3:
<4>Found a mtd3 image (0x3f0000), with size (0x10000).
<4>Looking for mtd device :mtd4:
<4>Found a mtd4 image (0x10000), with size (0x3e0000).
<4>Setting new rootfs offset to 000850e0
<4>Squashfs detected (size = 0xb0085154)
<5>Creating 5 MTD partitions on "Physically mapped flash":
<5>0x00000000-0x00010000 : "adam2"
<5>0x00010000-0x003f0000 : "linux"
<5>0x000850e0-0x00180000 : "rootfs"
<4>mtd: partition "rootfs" doesn't start on an erase block boundary -- force rea                              d-only
<5>0x003f0000-0x00400000 : "config"
<5>0x00180000-0x003f0000 : "OpenWrt"
<6>Initializing Cryptographic API
<6>NET4: Linux TCP/IP 1.0 for NET4.0
<6>IP Protocols: ICMP, UDP, TCP, IGMP
<6>IP: routing cache hash table of 512 buckets, 4Kbytes
<6>TCP: Hash tables configured (established 1024 bind 2048)
<4>ip_conntrack version 2.1 (5953 buckets, 5953 max) - 360 bytes per conntrack
<4>ip_tables: (C) 2000-2002 Netfilter core team
<6>NET4: Unix domain sockets 1.0/SMP for Linux NET4.0.
<6>NET4: Ethernet Bridge 008 for NET4.0
<6>802.1Q VLAN Support v1.8 Ben Greear <greearb@candelatech.com>
<6>All bugs added by David S. Miller <davem@redhat.com>
<4>VFS: Mounted root (squashfs filesystem) readonly.
<6>Mounted devfs on /dev
<4>Preserving ADAM2 memory.
<6>Freeing unused kernel memory: 72k freed
<4>Algorithmics/MIPS FPU Emulator v1.5
<4>jffs2.bbc: SIZE compression mode activated.
<4>Using the MAC with internal PHY
<4>Cpmac driver is allocating buffer memory at init time.
<4>Using the MAC with internal PHY
<4>Cpmac driver Disable TX complete interrupt setting threshold to 20.
<4>registered device TI Avalanche SAR
<4>Initializing DSL interface
<4>size=27008
<4>size=26144
<4>size=26624
<4>size=24704
<4>size=21152
<4>dsl modulation = GLITE
<4>Texas Instruments ATM driver: version:[4.02.04.00]
'''Cat /proc/meminfo'''
total:    used:    free:  shared: buffers:  cached:
Mem:  14708736  7778304  6930432        0   872448  2486272
Swap:        0        0        0
MemTotal:        14364 kB
MemFree:          6768 kB
MemShared:           0 kB
Buffers:           852 kB
Cached:           2428 kB
SwapCached:          0 kB
Active:           1988 kB
Inactive:         1304 kB
HighTotal:           0 kB
HighFree:            0 kB
LowTotal:        14364 kB
LowFree:          6768 kB
SwapTotal:           0 kB
SwapFree:            0 kB
'''cat /proc/cpuinfo'''
system type             : Texas Instruments AR7
processor               : 0
cpu model               : MIPS 4KEc V4.8
BogoMIPS                : 149.91
wait instruction        : yes
microsecond timers      : yes
tlb_entries             : 16
extra interrupt vector  : yes
hardware watchpoint     : yes
VCED exceptions         : not available
VCEI exceptions         : not available
'''cat /proc/modules'''
tiatm                 113524   0 (unused)
atm                    35928   0 [tiatm]
avalanche_cpmac        67768   1
