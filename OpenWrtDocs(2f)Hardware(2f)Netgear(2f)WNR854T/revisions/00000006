'''Netgear WNR854'''

The hardware in this router is very similar to the [:OpenWrtDocs/Hardware/Buffalo/WZR-AG300:Buffalo WZR-AG300], although that has two N cards and the user space differs.  However, the Airlink 101 AR625W is a carbon of this router, and is identical in almost every detail.

=== Serial Port ===

This is a Marvell board, and its serial pins are identical to the [:OpenWrtDocs/Hardware/Airlink101/AR525W:AR525W]. 

Serial connection parameters are : 115200,8N1

=== Linux ===

This runs the ubiquitous Linux 2.4.27-vrs1 version, using Uboot as a bootloader. 

Boot log:

{{{
Linux version 2.4.27-vrs1 (joshua@localhost.localdomain) (gcc version 3.4.4 (release) (CodeSourcery ARM 2005q3-1)) #152 Thu Sep 28 17:39:36 CST 2006
CPU: ARM926EJ-Sid(wb) revision 0
Machine: MV-88fxx81
Using UBoot passing parameters structure
Sys Clk = 166000000, Tclk = 166000000


- Warning - This LSP release was tested only with U-Boot release 1.7.3 

On node 0 totalpages: 8192
zone(0): 8192 pages.
zone(1): 0 pages.
zone(2): 0 pages.
Kernel command line: console=ttyS0,115200 root=/dev/mtdblock1 rw ip=192.168.1.1:192.168.1.101:::DB88FXX81:eth0:none
Relocating machine vectors to 0xffff0000
gppMask = [0x130]
Calibrating delay loop... 331.77 BogoMIPS
Memory: 32MB 0MB 0MB 0MB = 32MB total
Memory: 30292KB available (1681K code, 326K data, 72K init)
Dentry cache hash table entries: 4096 (order: 3, 32768 bytes)
Inode cache hash table entries: 2048 (order: 2, 16384 bytes)
Mount cache hash table entries: 512 (order: 0, 4096 bytes)
Buffer cache hash table entries: 1024 (order: 0, 4096 bytes)
Page-cache hash table entries: 8192 (order: 3, 32768 bytes)
CPU: Testing write buffer: pass
POSIX conformance testing by UNIFIX
init hw started.

CPU Interface
-------------
SDRAM_CS0 ....base 00000000, size  32MB 
SDRAM_CS1 ....disable
SDRAM_CS2 ....disable
SDRAM_CS3 ....disable
PEX0_MEM ....base e0000000, size 128MB 
PEX0_IO ....base f2000000, size   1MB 
PCI0_MEM ....base e8000000, size 128MB 
PCI0_IO ....base f2100000, size   1MB 
INTER_REGS ....base f1000000, size   1MB 
DEVICE_CS0 ....no such
DEVICE_CS1 ....no such
DEVICE_CS2 ....no such
DEV_BOOCS ....base f4000000, size  16MB 
PCI: bus0: Fast back to back transfers enabled
HW already initialized.
PCI: bus1: Fast back to back transfers enabled
Linux NET4.0 for Linux 2.4
Based upon Swansea University Computer Society NET3.039
Initializing RT netlink socket
 bankwidth 2, base f4000000, size 1000000

  Marvell Development Board (LSP Version 1.0.4)-- RD-88F5181L-VOIP-GE 

 Detected Tclk 166000000 and SysClk 166000000 
Starting kswapd
devfs: v1.12c (20020818) Richard Gooch (rgooch@atnf.csiro.au)
devfs: boot_options: 0x1
JFFS2 version 2.1. (C) 2001 Red Hat, Inc., designed by Axis Communications AB.
pty: 256 Unix98 ptys configured
Serial driver version 5.05c (2001-07-08) with MANY_PORTS SHARE_IRQ SERIAL_PCI enabled
ttyS00 at 0xf1012000 (irq = 3) is a 16550A
Marvell Gigabit Ethernet Driver 'egiga':
  o Ethernet descriptors in DRAM
  o DRAM SW cache-coherency
  o Loading network interface 
  o Using switch header mode
qdInit 
BoardID = eqdStart: CPU port 0x3 
----set PPU En
Switch driver initialized
Can't get netConfig: Use default
UNM is not initialized yet
2 VLANs created: CpuPortMask = 0xa7
vid=0:  DISABLED(0), portMask=0x750, portNum=5
vid=1:       VLAN_1, portMask=0x04, portNum=1
vid=2:       VLAN_2, portMask=0xa3, portNum=4
vid=12: ISOLATED(12), portMask=0x00, portNum=0
Port - Vlan
 0  - VLAN_2
 1  - VLAN_2
 2  - VLAN_1
 3  - VLAN_ALL
 4  - DISABLED(0)
 5  - VLAN_2
 6  - DISABLED(0)
 7  - VLAN_2
load virtual interface vid = 1
 register if with name  
Init the hal
: Ilegal MTU value 1500,  rounding MTU to: 1506 
 if eth0 registered
load virtual interface vid = 2
 register if with name  
 if eth1 registered
PPP generic driver version 2.4.2
physmap flash device: 1000000 at f4000000
phys_mapped_flash: Found an alias at 0x800000 for the chip at 0x0
cfi_cmdset_0001: Erase suspend on write enabled
0: offset=0x0,size=0x20000,blocks=64
Using buffer write method
Using physmap partition definition
Creating 6 MTD partitions on "phys_mapped_flash":
0x00000000-0x00600000 : "root"
0x00600000-0x00620000 : "nvram"
0x00620000-0x00640000 : "nvram default"
0x00640000-0x00660000 : "POT"
0x00660000-0x00680000 : "Traffic Meter"
0x00700000-0x00800000 : "uboot"
Initializing Cryptographic API
NET4: Linux TCP/IP 1.0 for NET4.0
IP Protocols: ICMP, UDP, TCP, IGMP
IP: routing cache hash table of 512 buckets, 4Kbytes
TCP: Hash tables configured (established 2048 bind 4096)
IPv4 over IPv4 tunneling driver
GRE over IPv4 tunneling driver
Linux IP multicast router 0.06 plus PIM-SM
ip_conntrack version 2.1 (8192 buckets, 65536 max) - 348 bytes per conntrack
ip_tables: (C) 2000-2002 Netfilter core team
ipt_time loading
NET4: Unix domain sockets 1.0/SMP for Linux NET4.0.
NET4: Ethernet Bridge 008 for NET4.0
Fast Floating Point Emulator V0.94M by Peter Teichmann.
cramfs: wrong magic
VFS: Mounted root (jffs2 filesystem).
Mounted devfs on /dev
Freeing init memory: 72K
ap0: Marvell AP-8x 802.11n adapter: mem=0xe8000000, irq=36

}}}

== Building Netgear firmware ==

Netgear are pretty good about providing sources and being open about the GPL.  Sources for this router are [http://kbserver.netgear.com/kb_web_files/open_src.asp provided on their site].  You need a very precise toolchain setup in order to be able to rebuild this, or you will have trouble linking the binary only components in the archive.  I used Crosstool to create a toolchain with:

 * arm-softfloat (OABI little endian)
 * GCC 3.4.4
 * glibc 2.3.5 

You will need to change some hard-coded paths in the Makefiles and config files.  You should also modify the top level makefile so that mkfs.jffs2 makes the ownership of all the files root (using -U).  Finally, the mkimage tool is missing, which generates suitable uboot kernels.  I modified linux/scripts/mkuboot.sh in the archive to point at the one built in openwrt (openwrt/tool_build/mkimage/mkimage).
