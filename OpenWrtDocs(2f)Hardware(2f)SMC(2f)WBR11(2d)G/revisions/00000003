= SMC WBR11-G =

{{{
CPU : AR2315
RAM : 16MB
Flash : 4MB
Wi-Fi : in SoC
Switch : Infineon ADM6996
}}}

== Serial pinout ==

{{{
RX TX
VCC GND         FLASH
}}}

== Original bootlog ==

{{{
+Ethernet eth0: MAC address 00:12:cf:7d:76:60
IP: 192.168.0.1/255.255.255.0, Gateway: 0.0.0.0
Default server: 169.254.255.254

RedBoot(tm) bootstrap and debug environment [ROMRAM]
Non-certified release, version v1.3.0 - built 14:53:16, Jan  9 2007

Copyright (C) 2000, 2001, 2002, 2003, 2004 Red Hat, Inc.

Board: ap61
RAM: 0x80000000-0x81000000, [0x8003e9a0-0x80fe1000] available
FLASH: 0xa8000000 - 0xa87f0000, 128 blocks of 0x00010000 bytes each.
== Executing boot script in 3.000 seconds - enter ^C to abort
RedBoot> fis load -l vmlinux.bin.l7
Image loaded from 0x80041000-0x801ec000
RedBoot> exec
Now booting linux kernel:
 Base address 0x80030000 Entry 0x80041000
 Cmdline :
CPU revision is: 00019064
Primary instruction cache 16kB, physically tagged, 4-way, linesize 16 bytes.
Primary data cache 16kB, 4-way, linesize 16 bytes.
Linux version 2.4.34 (samul_hwang@samLnxG2) (gcc version 3.4.6 (OpenWrt-2.0)) #2 Tue Jul 3 14:16:21 CST 2007
Determined physical RAM map:
 memory: 01000000 @ 00000000 (usable)
On node 0 totalpages: 4096
zone(0): 4096 pages.
zone(1): 0 pages.
zone(2): 0 pages.
Kernel command line: console=ttyS0,9600 rootfstype=squashfs,jffs2
Using 92.000 MHz high precision timer.
Calibrating delay loop... 183.50 BogoMIPS
Memory: 13984k/16384k available (1520k kernel code, 2400k reserved, 100k data, 68k init, 0k highmem)
Dentry cache hash table entries: 2048 (order: 2, 16384 bytes)
Inode cache hash table entries: 1024 (order: 1, 8192 bytes)
Mount cache hash table entries: 512 (order: 0, 4096 bytes)
Buffer cache hash table entries: 1024 (order: 0, 4096 bytes)
Page-cache hash table entries: 4096 (order: 2, 16384 bytes)
Checking for 'wait' instruction...  available.
POSIX conformance testing by UNIFIX
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
Serial driver version 5.05c (2001-07-08) with no serial options enabled
ttyS00 at 0xb1100003 (irq = 37) is a 16550A

Going to gpio_proc_entry
MTD driver for SPI flash.
spiflash: Probing for Serial flash ...
spiflash: Found SPI serial Flash.
8388608: size
Creating 8 MTD partitions on "spiflash":
0x00000000-0x00030000 : "RedBoot"
0x00030000-0x00720000 : "rootfs"
0x002a0000-0x00720000 : "rootfs1"
0x00720000-0x00730000 : "config"
0x00730000-0x007e0000 : "vmlinux.bin.l7"
0x007e0000-0x007ef000 : "FIS directory"
mtd: partition "FIS directory" doesn't end on an erase block -- force read-only
0x007ef000-0x007f0000 : "RedBoot config"
mtd: partition "RedBoot config" doesn't start on an erase block boundary -- force read-only
0x007f0000-0x00800000 : "board_config"
Initializing Cryptographic API
NET4: Linux TCP/IP 1.0 for NET4.0
IP Protocols: ICMP, UDP, TCP, IGMP
IP: routing cache hash table of 512 buckets, 4Kbytes
TCP: Hash tables configured (established 1024 bind 2048)
ip_conntrack version 2.1 (5953 buckets, 5953 max) - 360 bytes per conntrack
ip_tables: (C) 2000-2002 Netfilter core team
NET4: Unix domain sockets 1.0/SMP for Linux NET4.0.
NET4: Ethernet Bridge 008 for NET4.0
802.1Q VLAN Support v1.8 Ben Greear <greearb@candelatech.com>
All bugs added by David S. Miller <davem@redhat.com>
VFS: Mounted root (squashfs filesystem) readonly.
Mounted devfs on /dev
Freeing unused kernel memory: 68k freed
init started:  BusyBox v1.4.1 (2007-07-03 14:06:28 CST) multi-call binary

Please press Enter to activate this console. Algorithmics/MIPS FPU Emulator v1.5
mini_fo: using base directory: /
mini_fo: using storage directory: /jffs
jffs2.bbc: SIZE compression mode activated.
phyAttach: using admtek phy switch.
CSLIP: code copyright 1989 Regents of the University of California
PPP generic driver version 2.4.2
eth0.1: dev_set_promiscuity(master, 1)
device eth0 entered promiscuous mode
device eth0.1 entered promiscuous mode
br-lan: port 1(eth0.1) entering learning state
br-lan: port 1(eth0.1) entering forwarding state
br-lan: topology change detected, propagating
ipt_recent v0.3.1: Stephen Frost <sfrost@snowman.net>.  http://snowman.net/projects/ipt_recent/
IPP2P v0.8.1_rc1 loading
imq driver loaded.
ipt_time loading
ip_conntrack_rtsp v0.01 loading
ip_nat_rtsp v0.01 loading
ip_conntrack_pptp version 1.9 loaded
ip_nat_pptp version 1.5 loaded
wlan: 0.8.4.2 (Atheros/multi-bss)
ath_hal: 0.9.17.1 (AR5212, AR5312, RF5111, RF5112, RF2413, RF5413, RF2317)
ath_rate_atheros: Version 2.0.1
Copyright (c) 2001-2004 Atheros Communications, Inc, All Rights Reserved
ath_dfs: Version 2.0.0
Copyright (c) 2005-2006 Atheros Communications, Inc. All Rights Reserved
wlan: mac acl policy registered
ath_ahb: 0.9.4.5 (Atheros/multi-bss)
Setting ah_eepromDetach
**** Going to ath_hal_readEepromIntoDataset
wifi0: 11b rates: 1Mbps 2Mbps 5.5Mbps 11Mbps
wifi0: 11g rates: 1Mbps 2Mbps 5.5Mbps 11Mbps 6Mbps 9Mbps 12Mbps 18Mbps 24Mbps 36Mbps 48Mbps 54Mbps
wifi0: mac 11.0 phy 4.8 radio 8.6
wifi0: Use hw queue 1 for WME_AC_BE traffic
wifi0: Use hw queue 0 for WME_AC_BK traffic
wifi0: Use hw queue 2 for WME_AC_VI traffic
wifi0: Use hw queue 3 for WME_AC_VO traffic
wifi0: Use hw queue 8 for CAB traffic
wifi0: Use hw queue 9 for beacons
wifi0: Atheros 2317 WiSoC: mem=0xb0000000, irq=3
device ath0 entered promiscuous mode
br-lan: port 2(ath0) entering learning state
br-lan: port 2(ath0) entering forwarding state
br-lan: topology change detected, propagating
ar531x_wdt: Watchdog timer is now enabled.



BusyBox v1.4.1 (2007-07-03 14:06:28 CST) Built-in shell (ash)
Enter 'help' for a list of built-in commands.


 MR3202A-FLF-17 v1.0 -------------------------------
  * build version: r668
  * build date   : 2007/07/03
 ---------------------------------------------------
wlan[0,0]->

}}}

== OpenWrt bootlog ==

{{{
RedBoot> load -r -b %{FREEMEMLO} openwrt-atheros-2.6-vmlinux.lzma
Using default protocol (TFTP)
Can't load 'openwrt-atheros-2.6-vmlinux.lzma': file not found
RedBoot> load -r -b %{FREEMEMLO} openwrt-atheros-^C -vmlinux.lzma
RedBoot> load -r -b %{FREEMEMLO} openwrt-atheros-vmlinux.lzma
Using default protocol (TFTP)
Raw file loaded 0x8003ec00-0x8022ebff, assumed entry at 0x8003ec00
RedBoot> fis init
About to initialize [format] FLASH image system - continue (y/n)? y
*** Initialize FLASH Image System
... Erase from 0xa87e0000-0xa87f0000: .
... Program from 0x80ff0000-0x81000000 at 0xa87e0000: .
RedBoot> fis create -e 0x80041000 -r 0x80041000 vmlinux.bin.l7
... Erase from 0xa8030000-0xa8220000: ...............................
... Program from 0x8003ec00-0x8022ec00 at 0xa8030000: ...............................
... Erase from 0xa87e0000-0xa87f0000: .
... Program from 0x80ff0000-0x81000000 at 0xa87e0000: .
RedBoot> fis free
  0xA8220000 .. 0xA87E0000
RedBoot> load -r -b %{FREEMEMLO} openwrt-atheros-root.squashfs
Using default protocol (TFTP)
Raw file loaded 0x8003ec00-0x8017ebff, assumed entry at 0x8003ec00
RedBoot> fis create -l 0x5C0000 rootfs
... Erase from 0xa8220000-0xa87e0000: ............................................................................................
... Program from 0x8003ec00-0x8017ec00 at 0xa8220000: ....................
... Erase from 0xa87e0000-0xa87f0000: .
... Program from 0x80ff0000-0x81000000 at 0xa87e0000: .
RedBoot> reset
+Ethernet eth0: MAC address 00:12:cf:7d:76:60
IP: 192.168.0.1/255.255.255.0, Gateway: 0.0.0.0
Default server: 169.254.255.254

RedBoot(tm) bootstrap and debug environment [ROMRAM]
Non-certified release, version v1.3.0 - built 14:53:16, Jan  9 2007

Copyright (C) 2000, 2001, 2002, 2003, 2004 Red Hat, Inc.

Board: ap61
RAM: 0x80000000-0x81000000, [0x8003e9a0-0x80fe1000] available
FLASH: 0xa8000000 - 0xa87f0000, 128 blocks of 0x00010000 bytes each.
== Executing boot script in 3.000 seconds - enter ^C to abort
RedBoot> fis load -l vmlinux.bin.l7
Image loaded from 0x80041000-0x803c91a7
RedBoot> exec
Now booting linux kernel:
 Base address 0x80030000 Entry 0x80041000
 Cmdline :
Linux version 2.6.23.16 (fainelli@anaconda.int-evry.fr) (gcc version 4.1.2) #1 Tue Apr 22 13:42:10 CEST 2008
CPU revision is: 00019064
Determined physical RAM map:
 memory: 01000000 @ 00000000 (usable)
Initrd not found or empty - disabling initrd
Built 1 zonelists in Zone order.  Total pages: 4064
Kernel command line: console=ttyS0,9600 rootfstype=squashfs,jffs2 init=/etc/preinit
Primary instruction cache 16kB, physically tagged, 4-way, linesize 16 bytes.
Primary data cache 16kB, 4-way, linesize 16 bytes.
Synthesized TLB refill handler (20 instructions).
Synthesized TLB load handler fastpath (32 instructions).
Synthesized TLB store handler fastpath (32 instructions).
Synthesized TLB modify handler fastpath (31 instructions).
PID hash table entries: 64 (order: 6, 256 bytes)
Using 92.000 MHz high precision timer.
console [ttyS0] enabled
Dentry cache hash table entries: 2048 (order: 1, 8192 bytes)
Inode-cache hash table entries: 1024 (order: 0, 4096 bytes)
Memory: 12252k/16384k available (1948k kernel code, 4132k reserved, 287k data, 1380k init, 0k highmem)
Mount-cache hash table entries: 512
NET: Registered protocol family 16
Radio config found at offset 0xf8(0x1f8)
Generic PHY: Registered new driver
Time: MIPS clocksource has been installed.
NET: Registered protocol family 2
IP route cache hash table entries: 1024 (order: 0, 4096 bytes)
TCP established hash table entries: 512 (order: 0, 4096 bytes)
TCP bind hash table entries: 512 (order: -1, 2048 bytes)
TCP: Hash tables configured (established 512 bind 512)
TCP reno registered
ar531x: Registering GPIODEV device
squashfs: version 3.0 (2006/03/15) Phillip Lougher
Registering mini_fo version $Id$
JFFS2 version 2.2. (NAND) (SUMMARY)  þþ 2001-2006 Red Hat, Inc.
io scheduler noop registered
io scheduler deadline registered (default)
Serial: 8250/16550 driver $Revision: 1.90 $ 1 ports, IRQ sharing disabled
serial8250: ttyS0 at MMIO 0xb1100003 (irq = 37) is a 16550A
ICPlus IP175C: Registered new driver
Infineon ADM6996: Registered new driver
Marvell 88E6060: Registered new driver
eth0: Atheros AR231x: 00:12:cf:7d:76:60, irq 4
ar2313_eth_mii: probed
eth0: ADM6996 PHY driver attached.
eth0: attached PHY driver [Infineon ADM6996] (mii_bus:phy_addr=0:00)
cmdlinepart partition parsing not available
Searching for RedBoot partition table in spiflash at offset 0x7d0000
Searching for RedBoot partition table in spiflash at offset 0x7e0000
5 RedBoot partitions found on MTD device spiflash
Creating 5 MTD partitions on "spiflash":
0x00000000-0x00030000 : "RedBoot"
0x00030000-0x00220000 : "vmlinux.bin.l7"
0x00220000-0x007e0000 : "rootfs"
mtd: partition "rootfs" set to be root filesystem
mtd: partition "rootfs_data" created automatically, ofs=330000, len=4B0000
0x00330000-0x007e0000 : "rootfs_data"
0x007e0000-0x007ef000 : "FIS directory"
0x007ef000-0x007f0000 : "RedBoot config"
Registered led device: wlan
gpiodev: gpio device registered with major 254
gpiodev: gpio platform device registered with access mask FFFFFFFF
nf_conntrack version 0.5.0 (1024 buckets, 4096 max)
ip_tables: (C) 2000-2006 Netfilter Core Team
TCP vegas registered
NET: Registered protocol family 1
NET: Registered protocol family 17
802.1Q VLAN Support v1.8 Ben Greear <greearb@candelatech.com>
All bugs added by David S. Miller <davem@redhat.com>
eth0: Configuring MAC for half duplex
Freeing unused kernel memory: 1380k freed
Algorithmics/MIPS FPU Emulator v1.5
[sighandler]: No more events to be processed, quitting.
[cleanup]: Waiting for children.
[cleanup]: All children terminated.
- preinit -

Please press Enter to activate this console. PPP generic driver version 2.4.2
device eth0.0 entered promiscuous mode
device eth0 entered promiscuous mode
br-lan: port 1(eth0.0) entering learning state
br-lan: topology change detected, propagating
br-lan: port 1(eth0.0) entering forwarding state
wlan: trunk
ath_hal: module license 'Proprietary' taints kernel.
ath_hal: 0.9.30.13 (AR5212, AR5312, RF2316, TX_DESC_SWAP)
ath_rate_minstrel: Minstrel automatic rate control algorithm 1.2 (trunk)
ath_rate_minstrel: look around rate set to 10%
ath_rate_minstrel: EWMA rolloff level set to 75%
ath_rate_minstrel: max segment size in the mrr set to 6000 us
wlan: mac acl policy registered
ath_ahb: trunk
MadWifi: unable to attach hardware: 'No hardware present or device not yet supported' (HAL status 1)



BusyBox v1.8.2 (2008-04-10 18:29:44 CEST) built-in shell (ash)
Enter 'help' for a list of built-in commands.

  _______                     ________        __
 |       |.-----.-----.-----.|  |  |  |.----.|  |_
 |   -   ||  _  |  -__|     ||  |  |  ||   _||   _|
 |_______||   __|_____|__|__||________||__|  |____|
          |__| W I R E L E S S   F R E E D O M
 KAMIKAZE (bleeding edge, r10910) -------------------
  * 10 oz Vodka       Shake well with ice and strain
  * 10 oz Triple sec  mixture into 10 shot glasses.
  * 10 oz lime juice  Salute!
 ---------------------------------------------------
root@OpenWrt:/#
}}}
