#pragma section-numbers off

||<tablebgcolor="#f1f1ed" tablewidth="40%" tablestyle="FONT-SIZE: 0.9em; FLOAT: right; MARGIN: 0pt 0pt 1em 1em"style="PADDING-RIGHT: 0.5em; PADDING-LEFT: 0.5em; PADDING-BOTTOM: 0.5em; PADDING-TOP: 0.5em"> [[TableOfContents]] ||
= Netgear WNR834B =
The Netgear WNR834B is Netgear's Rangemax Next single-band wireless-N broadband router based on Broadcom's Intensi-Fi MIMO platform.  It shares similar hardware and configuration with the Linksys WRT-150N and WRT-160n routers.  Netgear's 2_1_13_na firmware runs Linux 2.4.20 internally and DD-WRT v24 sp2 firmware runs Linux 2.4.36 internally.

'''NOTE:''' This device supports only 2.4 kernel versions of Kamikaze. At this time the Broadcom wl.o binary driver is only available for 2.4 kernels and the open source b43 driver is not ready yet.  Wireless WILL NOT WORK if you flash an image with a 2.6 kernel. 

== General ==

=== Hardware Versions ===
||'''Model''' ||'''CPU''' ||'''Wireless''' ||'''Flash''' ||'''RAM''' ||'''FCC ID''' ||'''OpenWrt Kamikaze''' ||
||WNR834B v1 || BCM4704 ||BCM4321 (PC-card) ||4MB ||16MB ||PY30XXXXXXXXXXX || ?? ||
||WNR834B v2 || BCM4704 ||BCM4321 (integrated) ||4MB ||16MB ||PY307100061 || ?? ||

 * Link to Product page at netgear.com -> [http://www.netgear.com/Home/Products/RoutersandGateways/RangeMaxWirelessNRoutersandGateways/WNR834B.aspx?detail=Customer+Reviews#reviews Product_Page]
 * Link to general Support page at netgear.com -> [http://kbserver.netgear.com/products/WNR834B.asp WNR834B] 
 * Link to v1 Support page at netgear.com -> [http://kbserver.netgear.com/products/wnr834bv1.asp WNR834B v1] 
 * Link to v2 Support page at netgear.com -> [http://kbserver.netgear.com/products/wnr834bv2.asp WNR834B v2] 

=== Linux command line ===
{{{
root=/dev/mtdblock2 rootfstype=squashfs,jffs2 noinitrd console=ttyS0,115200
}}}

=== Netgear 2_1_13_na kernel signature ===
{{{
Linux version 2.4.20 (root@yoda.wycotransport.com) (gcc version 3.2.3 with Broadcom modifications) #10 Sat Sep 6 14:04:59 EDT 2008
}}}

=== DD-WRT V24 SVN 10991 kernel signature ===
{{{
Linux version 2.4.36 (bin@dd-wrt) (gcc version 3.4.6 (OpenWrt-2.0)) #2384 Wed Nov 5 17:21:15 CET 2008
}}}

== Hardware ==
||<tablebgcolor="#f1f1ed" tablewidth="35%" tablestyle="FONT-SIZE: 0.9em; FLOAT: right; MARGIN: -15px 0pt 0pt 0pt"style="PADDING-RIGHT: 0.5em; PADDING-LEFT: 0.5em; PADDING-BOTTOM: 0.5em; PADDING-TOP: 0.5em"> ||
||'''Architecture''' ||MIPS ||
||'''Vendor''' ||Broadcom ||
||'''Bootloader''' ||CFE 1.0.37 ||
||'''System-On-Chip'''||BCM4704KFBG ||
||'''Processor'''||BCM3302 v0.6 ||
||'''CPU Speed''' ||263 Mhz ||
||'''Flash size''' ||4 MiB ||
||'''RAM size''' ||16 MiB ||
||'''Wireless''' ||BCM4321 b/g/n Wireless (v1:PC-card, v2:integrated) ||
||'''Ethernet''' ||Switch in CPU ||
||'''USB''' ||No ||
||'''Serial'''||Yes ||

=== Integrated circuits ===
 * CPU - BCM4704 [http://www.broadcom.com/collateral/pb/4703_4704-PB00-R.pdf Product_Brief] 
(/proc/cpuinfo describes it as SoC BCM4704 rev 9 with CPU BCM3302 v0.6)
 * Switch - BCM5325 [http://www.broadcom.com/collateral/pb/5325M-PB05-R.pdf Product_Brief]
 * Wireless - BCM4321 [http://www.broadcom.com/collateral/pb/4321_2055-PB02-R.pdf Product_Brief]
 * Wireless - BCM2055 (under the shield) [http://www.broadcom.com/collateral/pb/4321_2055-PB02-R.pdf Product_Brief]
 * Flashchip - Macronix MX29LV320CBTC-90G [http://www.macronix.com/QuickPlace/hq/PageLibrary4825740B00298A3B.nsf/h_Index/7CE3021F57B8EA4848257412002E26CC/$File/MX29LV320CT-B-2.0.pdf Data Sheet]

=== Pads on PCB ===
There are 3 sets of pads on the PCB of the WRN834B v2:
JP1 - Serial console, 3.3v, 115200/8/N
J12 - JTAG
Solder pads - JTAG - near radio shield, top edge of board.


'''JP1'''

3.3v TTL Serial
||'''Pin 1''' || 3.3v ||
||'''Pin 2''' || RXD ||
||'''Pin 3''' || n/c ||
||'''Pin 4''' || n/c ||
||'''Pin 5''' || TXD ||
|| '''Pin 6''' || GND ||


'''J12'''

10-pin JTAG, 2 rows of 5 pins
R374 through R378 and R343 remain un-populated

||'''Pin 10''' || GND ||'''Pin 9''' || TCK ||
||'''Pin 8''' || GND ||'''Pin 7''' || TMS ||
||'''Pin 6''' || GND ||'''Pin 5''' || TDO ||
||'''Pin 4''' || GND ||'''Pin 3''' || TDI ||
||'''Pin 2''' || GND ||'''Pin 1''' || TRST ||


'''Solder pads'''
JTAG
R470 through R473 remain un-populated

||'''R470''' || TCK ||'''R471''' || TMS ||'''R472''' || TDO ||'''R473''' || TDI ||'''n/a''' || TRST ||

=== TJTAG command parameters ===
{{{
-flash:custom /window:1fc00000 /start:1ffe0000 /length:10000
}}}

=== MTD Flash RAM partitions ===
{{{
Flash device: 0x400000 at 0x1c000000
bootloader size: 131072

0x00000000-0x00020000 : "cfe"
0x00020000-0x003e0000 : "linux"
0x00102800-0x003b0000 : "rootfs"
0x003b0000-0x003e0000 : "ddwrt"
0x003f0000-0x00400000 : "nvram"
}}}

=== Serial Port ===

JP1 is a 3.3v serial console port running @ 115200/8/N
Refer to this page:
 * http://wiki.openwrt.org/OpenWrtDocs/Customizing/Hardware/Serial_Console

=== Boot Messages ===

 * Boot messages from CFE and Linux booting DD-WRT v24 SVN 10776
{{{
Decompressing..........done
Decompressing..........done

CFE version 1.0.37 for BCM947XX (32bit,SP,LE)
Build Date: Thu May  3 14:43:11 CST 2007
Copyright (C) 2000,2001,2002,2003 Broadcom Corporation.

Initializing Arena
Initializing Devices.
Boot partition size = 131072(0x20000)
et0: Broadcom BCM47xx 10/100 Mbps Ethernet Controller 4.80.53.0
et1: Broadcom BCM47xx 10/100 Mbps Ethernet Controller 4.80.53.0
CPU type 0x29006: 264MHz
Total memory: 16384 KBytes

Device eth0:  hwaddr 00-1E-2A-06-58-50, ipaddr 192.168.1.1, mask 255.255.255.0
        gateway not set, nameserver not set
Loader:raw Filesys:tftp Dev:eth0 File:192.168.1.2:vmlinuz Options:(null)
Loading: Failed.
Could not load 192.168.1.2:vmlinuz: Timeout occured
Checksum mismatch:
Image chksum: 0xFFFFFFFF
Calc  chksum: 0x00000000
Loader:raw Filesys:raw Dev:flash0.os File: Options:(null)
Loading: .. 3856 bytes read
Entry at 0x80001000
Closing network.
Starting program at 0x80001000

CPU revision is: 00029006
Linux version 2.4.36 (bin@dd-wrt) (gcc version 3.4.6 (OpenWrt-2.0)) #2384 Wed Nov 5 17:21:15 CET 2008
Setting the PFC to its default value
Determined physical RAM map:
 memory: 01000000 @ 00000000 (usable)
On node 0 totalpages: 4096
zone(0): 4096 pages.
zone(1): 0 pages.
zone(2): 0 pages.
Kernel command line: root=/dev/mtdblock2 rootfstype=squashfs,jffs2 noinitrd console=ttyS0,115200
CPU: BCM4704 rev 9 at 264 MHz
Using 132.000 MHz high precision timer.
Calibrating delay loop... 262.96 BogoMIPS
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
Initializing RT netlink socket
Starting kswapd
devfs: v1.12c (20020818) Richard Gooch (rgooch@atnf.csiro.au)
devfs: boot_options: 0x1
squashfs: version 3.0 (2006/03/15) Phillip Lougher
pty: 256 Unix98 ptys configured
Serial driver version 5.05c (2001-07-08) with MANY_PORTS SHARE_IRQ SERIAL_PCI enabled
ttyS00 at 0xb8000300 (irq = 3) is a 16550A
ttyS01 at 0xb8000400 (irq = 3) is a 16550A
PCI: Enabling device 01:01.0 (0004 -> 0006)
Overriding boardvendor: 0x14e4 instead of 0x14e4
Overriding boardtype: 0x46d instead of 0x4321
Universal TUN/TAP device driver 1.5 (C)1999-2002 Maxim Krasnyansky
 Amd/Fujitsu Extended Query Table v1.1 at 0x0040
number of CFI chips: 1
cfi_cmdset_0002: Disabling fast programming due to code brokenness.
Flash device: 0x400000 at 0x1c000000
bootloader size: 131072
Physically mapped flash: Filesystem type: squashfs, size=0x2a1ee9
Creating 5 MTD partitions on "Physically mapped flash":
0x00000000-0x00020000 : "cfe"
0x00020000-0x003e0000 : "linux"
0x00102800-0x003b0000 : "rootfs"
mtd: partition "rootfs" doesn't start on an erase block boundary -- force read-only
0x003f0000-0x00400000 : "nvram"
0x003b0000-0x003e0000 : "ddwrt"
sflash not supported on this router
Initializing Cryptographic API
IP Protocols: ICMP, UDP, TCP, IGMP
IP: routing cache hash table of 512 buckets, 4Kbytes
TCP: Hash tables configured (established 1024 bind 2048)
ip_conntrack version 2.1 (512 buckets, 4096 max) - 336 bytes per conntrack
ip_tables: (C) 2000-2002 Netfilter core team
ipt_random match loaded
netfilter PSD loaded - (c) astaro AG
ipt_osf: Startng OS fingerprint matching module.
ipt_IPV4OPTSSTRIP loaded
NET4: Unix domain sockets 1.0/SMP for Linux NET4.0.
802.1Q VLAN Support v1.8 Ben Greear <greearb@candelatech.com>
All bugs added by David S. Miller <davem@redhat.com>
VFS: Mounted root (squashfs filesystem) readonly.
Mounted devfs on /dev
starting Architecture code for broadcom
Booting device: Netgear WNR834B v2
}}}

== Configuration data ==

=== NVRAM ===

|| '''boardtype''' || 0x0472 ||
|| '''boardrev''' || 0x23 ||
|| '''boardflags''' || 0x10 ||
|| '''pci/1/1/boardvendor''' || 0x14e4 ||
|| '''pci/1/1/boardtype''' || 0x046d ||
|| '''pci/1/1/boardrev''' || 0x4b ||
|| '''pci/1/1/boardnum''' || 01 ||
|| '''pci/1/1/boardflags''' || 0x200 ||
|| '''pci/1/1/boardflags2''' || 0x0013 ||

== Other Categories including this device ==

 . Category80211nDevice
