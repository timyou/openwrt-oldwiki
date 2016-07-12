#pragma section-numbers off
[[TableOfContents]]

= Actiontec MI424-WR Overview =
The [http://www.actiontec.com Actiontec] MI424-WR router is based on a 533MHz IXP425. It has 32MB RAM and 8MB of FLASH. It has 4 external LAN ports and 1 WAN port. It has a coax interface and IEEE 802.11g support. Some pictures of the unit and the various revisions can be found here: [http://en.wikipedia.org/wiki/MI424WR].

== Hardware ==
 * NPEB - WAN interface with separate Micrel KS8721 PHY; PHY address: 17.
 * NPEC - LAN interface connected to Micrel KSZ8995MA switch via SPI; PHY addresses: 1, 2, 3, 4.
 * 3 PCI slots - 2 used for coax interface.
 * Wireless MiniPCI based on RA2560.
=== GPIO ===
||'''Pin''' ||'''I/O''' ||'''Description''' ||
||<)>0 ||<:>O ||Reset? ||
||<)>2 ||<:>O ||SPI CLK ||
||<)>3 ||<:>I ||SPI RxD ||
||<)>4 ||<:>O ||SPI TxD ||
||<)>6 ||<:>I ||PCI INTA (MoCA WAN) ||
||<)>7 ||<:>I ||PCI INTB (MoCA LAN) ||
||<)>8 ||<:>I ||PCI INTC (Mini-PCI) ||
||<)>9 ||<:>O ||SPI CS ||
||<)>10 ||<:>I ||Button ||
||<)>11 ||<:>O ||MoCA WAN LED ||
||<)>14 ||<:>O ||PCI CLK Pin ||
=== Latch ===
There's a latch accessible via CS1 that is 16-bits wide.
||'''Bit''' ||'''Function''' ||
||<)>0 ||Power alarm (red) ||
||<)>1 ||Power ||
||<)>2 ||Wireless ||
||<)>3 ||Internet alarm (red) ||
||<)>4 ||Internet active ||
||<)>5 ||MoCA LAN ||
||<)>7 ||PCI reset ||

== Software ==

=== Redboot ===

A custom version has been built. After installation (using JTAG), the redboot prompt is accessible via "telnet 192.168.1.1 9000".

=== Linux ===

Board id 1778 has been registered for this device.
Here's a boot log:
{{{
<5>Linux version 2.6.26 (jose@chessmaster) (gcc version 4.2.4) #13 Thu Jul 24 18:52:37 EDT 2008
<4>CPU: XScale-IXP42x Family [690541c1] revision 1 (ARMv5TE), cr=000039ff
<4>Machine: Actiontec MI424WR
<4>Memory policy: ECC disabled, Data cache writeback
<7>On node 0 totalpages: 8192
<7>  DMA zone: 64 pages used for memmap
<7>  DMA zone: 0 pages reserved
<7>  DMA zone: 8128 pages, LIFO batch:0
<7>  Normal zone: 0 pages used for memmap
<7>  Movable zone: 0 pages used for memmap
<4>CPU0: D VIVT undefined 5 cache
<4>CPU0: I cache: 32768 bytes, associativity 32, 32 byte lines, 32 sets
<4>CPU0: D cache: 32768 bytes, associativity 32, 32 byte lines, 32 sets
<4>Built 1 zonelists in Zone order, mobility grouping on.  Total pages: 8128
<5>Kernel command line: root=/dev/mtdblock2 rootfstype=squashfs,jffs2 noinitrd console=ttyS0,115200 init=/etc/preinit
<4>PID hash table entries: 128 (order: 7, 512 bytes)
<6>Dentry cache hash table entries: 4096 (order: 2, 16384 bytes)
<6>Inode-cache hash table entries: 2048 (order: 1, 8192 bytes)
<6>Memory: 32MB = 32MB total
<5>Memory: 30324KB available (1844K code, 179K data, 100K init)
<7>Calibrating delay loop... 532.48 BogoMIPS (lpj=2662400)
<4>Mount-cache hash table entries: 512
<6>CPU: Testing write buffer coherency: ok
<6>net_namespace: 480 bytes
<6>NET: Registered protocol family 16
<4>IXP4xx: Using 16MiB expansion bus window size
<4>PCI: IXP4xx is host
<4>PCI: IXP4xx Using direct access for memory space
<6>PCI: bus0: Fast back to back transfers enabled
<7>Switched to high resolution mode on CPU 0
<6>NET: Registered protocol family 2
<6>IP route cache hash table entries: 1024 (order: 0, 4096 bytes)
<6>TCP established hash table entries: 1024 (order: 1, 8192 bytes)
<6>TCP bind hash table entries: 1024 (order: 0, 4096 bytes)
<6>TCP: Hash tables configured (established 1024 bind 1024)
<6>TCP reno registered
<6>NET: Registered protocol family 1
<6>IXP4xx Queue Manager initialized.
<6>squashfs: version 3.0 (2006/03/15) Phillip Lougher
<4>Registering mini_fo version $Id$
<6>JFFS2 version 2.2. (NAND) (SUMMARY)  Â© 2001-2006 Red Hat, Inc.
<6>msgmni has been set to 59
<6>io scheduler noop registered
<6>io scheduler deadline registered (default)
<6>Serial: 8250/16550 driver $Revision: 1.90 $ 4 ports, IRQ sharing disabled
<6>serial8250.0: ttyS0 at MMIO 0xc8000000 (irq = 15) is a XScale
<6>console [ttyS0] enabled
<6>serial8250.0: ttyS1 at MMIO 0xc8001000 (irq = 13) is a XScale
<6>eth0: MII PHY 17 on NPE-B
<6>eth1: MII PHY 1 on NPE-C
<6>eth1: MII PHY 2 on NPE-C
<6>eth1: MII PHY 3 on NPE-C
<6>eth1: MII PHY 4 on NPE-C
<6>IXP4XX-Flash.0: Found 1 x16 devices at 0x0 in 16-bit bank
<4> Intel/Sharp Extended Query Table at 0x0031
<6>Using buffer write method
<5>cfi_cmdset_0001: Erase suspend on write enabled
<7>erase region 0: offset=0x0,size=0x20000,blocks=64
<5>Searching for RedBoot partition table in IXP4XX-Flash.0 at offset 0x7e0000
<5>5 RedBoot partitions found on MTD device IXP4XX-Flash.0
<5>Creating 5 MTD partitions on "IXP4XX-Flash.0":
<5>0x00000000-0x00080000 : "RedBoot"
<5>0x00080000-0x001c0000 : "linux"
<5>0x001c0000-0x007e0000 : "root"
<5>0x007e0000-0x007ff000 : "FIS directory"
<5>0x007ff000-0x00800000 : "RedBoot config"
<6>i2c /dev entries driver
<3>i2c-gpio: probe failed: -19
<4>IXP4xx Watchdog Timer: heartbeat 60 sec
<6>Registered led device: moca-wan
<6>Registered led device: power-alarm
<6>Registered led device: power-ok
<6>Registered led device: wireless
<6>Registered led device: inet-down
<6>Registered led device: inet-up
<6>Registered led device: moca-lan
<6>Registered led device: wan-alarm
<4>nf_conntrack version 0.5.0 (1024 buckets, 4096 max)
<6>ip_tables: (C) 2000-2006 Netfilter Core Team
<6>TCP westwood registered
<6>NET: Registered protocol family 17
<6>802.1Q VLAN Support v1.8 Ben Greear <greearb@candelatech.com>
<6>All bugs added by David S. Miller <davem@redhat.com>
<6>XScale DSP coprocessor detected.
<4>drivers/rtc/hctosys.c: unable to open rtc device (rtc0)
<4>VFS: Mounted root (jffs2 filesystem).
<6>Freeing init memory: 100K
<4>Please be patient, while OpenWrt loads ...
<0>Kernel panic - not syncing: Attempted to kill init!
}}}

----
 CategoryModel ["CategoryIXP4xxDevice"]
