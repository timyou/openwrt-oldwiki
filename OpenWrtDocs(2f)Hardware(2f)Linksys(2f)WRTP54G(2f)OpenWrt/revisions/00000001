Running OpenWRT onto WRTP54g

= Boot =

{{{
Booting...
Linux version 2.6.26.5 (xinzhen@avxhome) (gcc version 4.1.2) #18 Fri Nov 7 16:47:51 CST 2008
console [early0] enabled
CPU revision is: 00018448 (MIPS 4KEc)
TI AR7 (TNETV1050), ID: 0x0007, Revision: 0x02
RESET REG: 0x1c420041
Determined physical RAM map:
 memory: 01000000 @ 14000000 (usable)
Initrd not found or empty - disabling initrd
Zone PFN ranges:
  Normal      81920 ->    86016
Movable zone start PFN for each node
early_node_map[1] active PFN ranges
    0:    81920 ->    86016
Built 1 zonelists in Zone order, mobility grouping off.  Total pages: 4064
Kernel command line: init=/etc/preinit rootfstype=squashfs,jffs2, console=ttyS0,115200n8
Primary instruction cache 16kB, VIPT, 4-way, linesize 16 bytes.
Primary data cache 16kB, 4-way, VIPT, no aliases, linesize 16 bytes
PID hash table entries: 64 (order: 6, 256 bytes)
Dentry cache hash table entries: 2048 (order: 1, 8192 bytes)
Inode-cache hash table entries: 1024 (order: 0, 4096 bytes)
Memory: 12660k/16384k available (1922k kernel code, 3724k reserved, 404k data, 120k init, 0k highmem)
SLUB: Genslabs=6, HWalign=32, Order=0-3, MinObjects=0, CPUs=1, Nodes=1
Mount-cache hash table entries: 512
net_namespace: 484 bytes
NET: Registered protocol family 16
registering cpmac_high
registering cpmac_low
NET: Registered protocol family 2
IP route cache hash table entries: 1024 (order: 0, 4096 bytes)
TCP established hash table entries: 512 (order: 0, 4096 bytes)
TCP bind hash table entries: 512 (order: -1, 2048 bytes)
TCP: Hash tables configured (established 512 bind 512)
TCP reno registered
NET: Registered protocol family 1
squashfs: version 3.0 (2006/03/15) Phillip Lougher
Registering mini_fo version $Id$
JFFS2 version 2.2. (NAND) (SUMMARY)  漏 2001-2006 Red Hat, Inc.
msgmni has been set to 24
io scheduler noop registered
io scheduler deadline registered (default)
Serial: 8250/16550 driver $Revision: 1.90 $ 2 ports, IRQ sharing disabled
serial8250: ttyS0 at MMIO 0x8610e00 (irq = 15) is a TI-AR7
console handover: boot [early0] -> real [ttyS0]
serial8250: ttyS1 at MMIO 0x8610f00 (irq = 16) is a TI-AR7
Fixed MDIO Bus: probed
RESET REG: 0x1c620041
phy_mask: 0x3fffffff
register phy 30
register phy 31
cpmac-mii: probed
cpmac: device eth0 (regs: 08640800, irq: 41, phy: , mac: 00:13:10:a3:54:10)
cpmac: device eth1 (regs: 08640000, irq: 27, phy: , mac: 00:13:10:a3:54:11)
physmap platform flash device: 00800000 at 10000000
physmap-flash.0: Found 1 x16 devices at 0x0 in 16-bit bank
 Amd/Fujitsu Extended Query Table at 0x0040
number of CFI chips: 1
cfi_cmdset_0002: Disabling erase-suspend-program due to code brokenness.
cmdlinepart partition parsing not available
RedBoot partition parsing not available
4 ar7part partitions found on MTD device physmap-flash.0
Creating 4 MTD partitions on "physmap-flash.0":
0x00000000-0x00010000 : "loader"
0x00010000-0x00020000 : "config"
0x00030000-0x00800000 : "linux"
0x000f0fa3-0x00800000 : "rootfs"
mtd: partition "rootfs" doesn't start on an erase block boundary -- force read-only
mtd: partition "rootfs" set to be root filesystem
mtd: partition "rootfs_data" created automatically, ofs=1E0000, len=620000 
0x001e0000-0x00800000 : "rootfs_data"
ar7_wdt: timer margin 59 seconds (prescale 65535, change 57180, freq 62500000)
Registered led device: status
vlynq0: regs 0x08611300, irq 34, mem 0x40000000
vlynq1: regs 0x08611c00, irq 33, mem 0x0c000000
Found a VLYNQ device: 00000009
TCP vegas registered
NET: Registered protocol family 17
802.1Q VLAN Support v1.8 Ben Greear <greearb@candelatech.com>
All bugs added by David S. Miller <davem@redhat.com>
VFS: Mounted root (squashfs filesystem) readonly.
Freeing unused kernel memory: 120k freed
Please be patient, while OpenWrt loads ...
Algorithmics/MIPS FPU Emulator v1.5
- preinit -
Press CTRL-C for failsafe
jffs2 not ready yet; using ramdisk
mini_fo: using base directory: /
mini_fo: using storage directory: /tmp/root
- init -

Please press Enter to activate this console. br-lan: Dropping NETIF_F_UFO since no NETIF_F_HW_CSUM feature.
device eth0 entered promiscuous mode
ENBL_SET 0x81
br-lan: port 1(eth0) entering learning state
br-lan: topology change detected, propagating
br-lan: port 1(eth0) entering forwarding state
PHY: 0:1f - Link is Down


BusyBox v1.11.1 (2008-11-07 16:40:08 CST) built-in shell (ash)
Enter 'help' for a list of built-in commands.

  _______                     ________        __
 |       |.-----.-----.-----.|  |  |  |.----.|  |_
 |   -   ||  _  |  -__|     ||  |  |  ||   _||   _|
 |_______||   __|_____|__|__||________||__|  |____|
          |__| W I R E L E S S   F R E E D O M
 KAMIKAZE (bleeding edge, r12486) -------------------
  * 10 oz Vodka       Shake well with ice and strain
  * 10 oz Triple sec  mixture into 10 shot glasses.
  * 10 oz lime juice  Salute!
 ---------------------------------------------------
root@OpenWrt:/# 
}}}

= Infomation =

== cpuinfo ==

{{{root@OpenWrt:/# cat /proc/cpuinfo 
system type             : TI AR7 (TNETV1050)
processor               : 0
cpu model               : MIPS 4KEc V4.8
BogoMIPS                : 149.91
wait instruction        : yes
microsecond timers      : yes
tlb_entries             : 16
extra interrupt vector  : yes
hardware watchpoint     : yes
ASEs implemented        :
shadow register sets    : 1
core                    : 0
VCED exceptions         : not available
VCEI exceptions         : not available}}}

== interrupts ==

{{{root@OpenWrt:/# cat /proc/interrupts 
           CPU0       
  2:          0            MIPS  AR7 cascade interrupt
  7:     130911            MIPS  timer
  8:          0             AR7  AR7 cascade interrupt
 15:      16648             AR7  serial
 27:       4626             AR7  eth1
 41:        992             AR7  eth0

ERR:          0}}}

== iomem ==

{{{root@OpenWrt:/# cat /proc/iomem 
03400000-34001fff : mem
  08610b00-08610b1f : TI AR7 Watchdog Timer
  08611200-086112ff : regs
  08611300-086113ff : regs
    08611300-086113fe : vlynq0
  08611c00-08611cff : regs
    08611c00-08611cfe : vlynq1
  08640000-086407ff : regs
    08640000-086407fe : eth1
  08640800-08640fff : regs
    08640800-08640ffe : eth0
  0c000000-0cffffff : mem
  10000000-107fffff : mem
    10000000-107fffff : physmap-flash.0
  14000000-14ffffff : System RAM
    14100000-142e0887 : Kernel code
    142e0888-14345bbf : Kernel data
40000000-43ffffff : mem}}}

= Network =

== ifconfig ==

{{{root@OpenWrt:/# ifconfig 
br-lan    Link encap:Ethernet  HWaddr 00:13:10:A3:54:10  
          inet addr:192.168.1.1  Bcast:192.168.1.255  Mask:255.255.255.0
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:123 errors:0 dropped:0 overruns:0 frame:0
          TX packets:956 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0 
          RX bytes:14104 (13.7 KiB)  TX bytes:41244 (40.2 KiB)

eth0      Link encap:Ethernet  HWaddr 00:13:10:A3:54:10  
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:133 errors:0 dropped:0 overruns:0 frame:0
          TX packets:956 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:17585 (17.1 KiB)  TX bytes:41244 (40.2 KiB)
          Interrupt:41 

eth1      Link encap:Ethernet  HWaddr 00:13:10:A3:54:11  
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:5140 errors:0 dropped:0 overruns:0 frame:0
          TX packets:2 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:557154 (544.0 KiB)  TX bytes:84 (84.0 B)
          Interrupt:27 

lo        Link encap:Local Loopback  
          inet addr:127.0.0.1  Mask:255.0.0.0
          UP LOOPBACK RUNNING  MTU:16436  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0 
          RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)}}}

== route ==

{{{root@OpenWrt:/# route -n
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
192.168.1.0     0.0.0.0         255.255.255.0   U     0      0        0 br-lan}}}

== ping ==

{{{root@OpenWrt:/# ping 192.168.1.8 -c 4
PING 192.168.1.8 (192.168.1.8): 56 data bytes
64 bytes from 192.168.1.8: seq=0 ttl=128 time=9.855 ms
64 bytes from 192.168.1.8: seq=1 ttl=128 time=0.603 ms
64 bytes from 192.168.1.8: seq=2 ttl=128 time=0.592 ms
64 bytes from 192.168.1.8: seq=3 ttl=128 time=0.589 ms

--- 192.168.1.8 ping statistics ---
4 packets transmitted, 4 packets received, 0% packet loss
round-trip min/avg/max = 0.589/2.909/9.855 ms}}}

== PHY ==

{{{root@OpenWrt:/# mii-tool 
eth0: 10 Mbit, half duplex, no link
eth1: 10 Mbit, half duplex, no link}}}
