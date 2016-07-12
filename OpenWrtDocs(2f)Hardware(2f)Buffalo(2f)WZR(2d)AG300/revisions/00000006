'''Buffalo Wireless-N Nfiniti Dual Band'''

=== Serial Port ===

This is a Marvell board, and its serial pins are identical to the [:OpenWrtDocs/Hardware/Airlink101/AR525W:AR525W]. 

Serial connection parameters are : 112500,8N1

=== CPU ===

The "ARM926EJ-Sid(wb)" is a Jazelle-enabled CPU which means it can interpret (a subset of) Java bytecodes directly.  This is a CPU now being used in a number of WinCE phones, and is likely to appear in more routers in the future.

=== Source availability ===

At this time, Buffalo do not provide a download of the sources for this router - this is typical of their attitude towards open source.  The manual contains instructions on how to contact Buffalo with a CD and request the source for $20.  It has been suggested that Buffalo require this for every module in the system.

Having said that, the kernel for the [:OpenWrtDocs/Hardware/Netgear/WNR854:Netgear WNR854] will boot on this board with trivial changes to the flash layout, and using that, an OpenWRT port should be straight forward.

=== Linux ===

This runs the ubiquitous Linux 2.4.27-vrs1 version, using Uboot as a bootloader. 

Boot log:

{{{
Linux version 2.4.27-vrs1 (vc03021@mkitec_vc03021) (gcc version 3.4.4 (release) (CodeSourcery ARM 2005q3-1)) #1 2007å¹´ 1æœˆ 10æ—¥ æ°´æ›œæ—¥ 11:26:49 JST
CPU: ARM926EJ-Sid(wb) revision 0
Machine: MV-88fxx81
Using UBoot passing parameters structure
Sys Clk = 166666667, Tclk = 166666667


- Warning - This LSP release was tested only with U-Boot release 1.7.3 

On node 0 totalpages: 8192
zone(0): 8192 pages.
zone(1): 0 pages.
zone(2): 0 pages.
Kernel command line: console=ttyS0,115200 mtdparts=phys_mapped_flash:7m(root),1m@7m(uboot)ro root=/dev/mtdblock1 rw ip=192.168.11.1:192.168.11.108:::DB88FXX81:eth0:none
Relocating machine vectors to 0xffff0000
Calibrating delay loop... 332.59 BogoMIPS
Memory: 32MB 0MB 0MB 0MB = 32MB total
Memory: 30040KB available (1914K code, 341K data, 76K init)
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

  Marvell Development Board (LSP Version 1.1.1)-- RD-88F5181L-VOIP-GE 

 Detected Tclk 166666667 and SysClk 166666667 
Starting kswapd
Journalled Block Device driver loaded
devfs: v1.12c (20020818) Richard Gooch (rgooch@atnf.csiro.au)
devfs: boot_options: 0x1
JFFS2 version 2.1. (C) 2001 Red Hat, Inc., designed by Axis Communications AB.
mel_initsw: GPIO initialize done..
BUFFALO SWICH & LED DRIVER ver 1.00
Serial driver version 5.05c (2001-07-08) with MANY_PORTS SHARE_IRQ SERIAL_PCI enabled
ttyS00 at 0xf1012000 (irq = 3) is a 16550A
HDLC line discipline: version $Revision: 3.7 $, maxframe=4096
N_HDLC line discipline registered.
Marvell Gateway Driver:
Detected RD_88F5181L_VOIP_GE
Multi queue support ( rxq0=128 rxq1=64 rxq2=64 rxq3=64 txq0=2000 )
Routing QoS support (ToS 0x11;0x22)
L2 IGMP support
Using boot network interface configuration
eth0: mac_addr 00:16:01:6f:0c:11, VID 0x100, port list: port-4 
eth1: mac_addr 00:16:01:6f:0c:11, VID 0x200, port list: port-0 port-1 port-2 port-3 
init switch layer... my_gateway: SetPhyReg(port=0,pd_port=2)=1111
my_gateway: SetPhyReg(port=1,pd_port=1)=1111
my_gateway: SetPhyReg(port=2,pd_port=0)=1111
my_gateway: SetPhyReg(port=3,pd_port=7)=1111
my_gateway: SetPhyReg(port=4,pd_port=5)=1111
done
init MAC layer... done
loading network interfaces: eth0 eth1 
PPP generic driver version 2.4.2
PPP Deflate Compression module registered
PPP BSD Compression module registered
physmap flash device: 1000000 at f4000000
Physically mapped flash: Found an alias at 0x800000 for the chip at 0x0
 Amd/Fujitsu Extended Query Table v0.0 at 0x0040
number of CFI chips: 1
cfi_cmdset_0002: Disabling fast programming due to code brokenness.
Using physmap partition definition
Creating 4 MTD partitions on "Physically mapped flash":
0x00000000-0x00780000 : "rootfs"
0x00780000-0x007a0000 : "user_property"
0x007a0000-0x007c0000 : "uboot_environ"
0x007c0000-0x00800000 : "uboot"
Initializing Cryptographic API
IPv6 v0.8 (usagi-cvs) for NET4.0
IPv6 over IPv4 tunneling driver
NET4: Linux TCP/IP 1.0 for NET4.0
IP Protocols: ICMP, UDP, TCP
IP: routing cache hash table of 512 buckets, 4Kbytes
TCP: Hash tables configured (established 2048 bind 4096)
ip_conntrack version 2.1 (256 buckets, 2048 max) - 316 bytes per conntrack
ip_tables: (C) 2000-2002 Netfilter core team
ipt_time loading
NET4: Unix domain sockets 1.0/SMP for Linux NET4.0.
ip6_tables: (C) 2000-2002 Netfilter core team
registering ipv6 mark target
NET4: Ethernet Bridge 008 for NET4.0
Fast Floating Point Emulator V0.94M by Peter Teichmann.
VFS: Mounted root (cramfs filesystem).
Mounted devfs on /dev
Freeing init memory: 76K
ap0: Marvell AP-8x 802.11n adapter: mem=0xe8000000, irq=38
ap1: Marvell AP-8x 802.11n adapter: mem=0xe8020000, irq=36
}}}

----
Category80211nDevice CategoryGigabitDevices
