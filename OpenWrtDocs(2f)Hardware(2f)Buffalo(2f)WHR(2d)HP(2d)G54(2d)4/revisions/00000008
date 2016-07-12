The Buffalo WHR-HP-G54-4 seems to work fine with OpenWRT RC5.

== Flo's user report ==
After uploading the WhiteRussian RC5 file "openwrt-brcm-2.4-jffs2-4MB.trx" the router is reachable via LAN interface with IP 192.168.11.1.

mtd erase nvram (for resetting NVRAM settings) seem to be supported by this device.

For getting the WirelessLAN interface to work it's necessary to manually set the corresponding OpenWRT NVRAM wireless variables:

nvram set wifi_ifname=eth1

nvram set wlan_hardware_present=yes

nvram commit

==> reboot the device

Maybe you would also change the LAN IP-range to OpenWRT defaults:

nvram set lan_ipaddr=192.168.1.1

nvram set lan_netmask=255.255.255.0

nvram commit

==> reboot the device

Hope I did not forget anything ;-)


== JustRob's information ==

dmesg output (changing MAC addr):

{{{
CPU revision is: 00029008
Primary instruction cache 16kB, physically tagged, 2-way, linesize 16 bytes.
Primary data cache 8kB, 2-way, linesize 16 bytes.
Linux version 2.4.30 (mbm@reboot) (gcc version 3.4.4 (OpenWrt-1.0)) #1 Mon Nov 6 17:35:21 PST 2006
Setting the PFC value as 0x15
Determined physical RAM map:
 memory: 01000000 @ 00000000 (usable)
On node 0 totalpages: 4096
zone(0): 4096 pages.
zone(1): 0 pages.
zone(2): 0 pages.
Kernel command line: root=/dev/mtdblock2 rootfstype=squashfs,jffs2 init=/etc/preinit noinitrd console=ttyS0,115200
CPU: BCM5352 rev 0 at 200 MHz
Using 100.000 MHz high precision timer.
Calibrating delay loop... 199.47 BogoMIPS
Memory: 14212k/16384k available (1464k kernel code, 2172k reserved, 104k data, 84k init, 0k highmem)
Dentry cache hash table entries: 2048 (order: 2, 16384 bytes)
Inode cache hash table entries: 1024 (order: 1, 8192 bytes)
Mount cache hash table entries: 512 (order: 0, 4096 bytes)
Buffer cache hash table entries: 1024 (order: 0, 4096 bytes)
Page-cache hash table entries: 4096 (order: 2, 16384 bytes)
Checking for 'wait' instruction...  unavailable.
POSIX conformance testing by UNIFIX
PCI: no core
PCI: Fixing up bus 0
Linux NET4.0 for Linux 2.4
Based upon Swansea University Computer Society NET3.039
Initializing RT netlink socket
Starting kswapd
Registering mini_fo version $Id$
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
eth0: Broadcom 47xx 10/100BaseT Ethernet 00:16:01:aa:gg:hh
Physically mapped flash: Found an alias at 0x400000 for the chip at 0x0
Physically mapped flash: Found an alias at 0x800000 for the chip at 0x0
Physically mapped flash: Found an alias at 0xc00000 for the chip at 0x0
Physically mapped flash: Found an alias at 0x1000000 for the chip at 0x0
Physically mapped flash: Found an alias at 0x1400000 for the chip at 0x0
Physically mapped flash: Found an alias at 0x1800000 for the chip at 0x0
Physically mapped flash: Found an alias at 0x1c00000 for the chip at 0x0
 Amd/Fujitsu Extended Query Table v1.1 at 0x0040
number of CFI chips: 1
cfi_cmdset_0002: Disabling fast programming due to code brokenness.
Flash device: 0x400000 at 0x1c000000
bootloader size: 262144
Physically mapped flash: Filesystem type: squashfs, size=0xda5f3
Updating TRX offsets and length:
old trx = [0x0000001c, 0x000008d8, 0x0007f400], len=0x0015a000 crc32=0x3c540b4c
new trx = [0x0000001c, 0x000008d8, 0x0007f400], len=0x00160000 crc32=0xfdc1bc2e
Done
Creating 5 MTD partitions on "Physically mapped flash":
0x00000000-0x00040000 : "cfe"
0x00040000-0x003f0000 : "linux"
0x000bf400-0x001a0000 : "rootfs"
mtd: partition "rootfs" doesn't start on an erase block boundary -- force read-only
0x003f0000-0x00400000 : "nvram"
0x001a0000-0x003f0000 : "OpenWrt"
Initializing Cryptographic API
NET4: Linux TCP/IP 1.0 for NET4.0
IP Protocols: ICMP, UDP, TCP, IGMP
IP: routing cache hash table of 512 buckets, 4Kbytes
TCP: Hash tables configured (established 1024 bind 2048)
ip_conntrack version 2.1 (5953 buckets, 5953 max) - 332 bytes per conntrack
ip_tables: (C) 2000-2002 Netfilter core team
NET4: Unix domain sockets 1.0/SMP for Linux NET4.0.
NET4: Ethernet Bridge 008 for NET4.0
802.1Q VLAN Support v1.8 Ben Greear <greearb@candelatech.com>
All bugs added by David S. Miller <davem@redhat.com>
VFS: Mounted root (squashfs filesystem) readonly.
Mounted devfs on /dev
Freeing unused kernel memory: 84k freed
Algorithmics/MIPS FPU Emulator v1.5
diag: Detected 'Buffalo WHR-HP-G54'
Probing device eth0: found!
b44: eth0: Link is up at 100 Mbps, full duplex.
b44: eth0: Flow control is off for TX and off for RX.
mini_fo: using base directory: /
mini_fo: using storage directory: /tmp/root
jffs2.bbc: SIZE compression mode activated.
PCI: Setting latency timer of device 00:05.0 to 64
eth1: Broadcom BCM4318 802.11 Wireless Controller 3.90.37.0
BFL_ENETADM not set in boardflags. Use force=1 to ignore.
device eth0 entered promiscuous mode
b44: eth0: Link is up at 100 Mbps, full duplex.
b44: eth0: Flow control is off for TX and off for RX.
vlan0: add 01:00:5e:00:00:01 mcast address to master interface
vlan0: dev_set_promiscuity(master, 1)
vlan0: dev_set_allmulti(master, 1)
device eth1 entered promiscuous mode
br0: port 2(eth1) entering learning state
br0: port 1(vlan0) entering learning state
br0: port 2(eth1) entering forwarding state
br0: topology change detected, propagating
br0: port 1(vlan0) entering forwarding state
br0: topology change detected, propagating
vlan1: add 01:00:5e:00:00:01 mcast address to master interface
mini_fo: using base directory: /
mini_fo: using storage directory: /jffs
}}}


Device info:

 * 48-pin TSOP flash chip on top PCB:  Macronix MX29LV320CBTC-90G 48-pin TSOP 90ns
 . URL: http://www.macronix.com/QuickPlace/hq/PageLibrary48256F5500439ED0.nsf/h_CE4C9490FDF4280B48256F550043C6D8/209CFCBBF4BCCB9148257031002F02E6/$File/MX29LV320CTBver15.pdf
 * 2 sets of open pads on top PCB for other SDRAM memory footprint, each 66-pin TSOP
   . can use Micron 32Mx16 MT46V32M16TG (if same assumptions regarding other routers with similar BCM5352 processor are true for this board)
   . Caveats:
            1. I haven't tried this (yet)
            2. Need VERY GOOD soldering skills, using microscope and Metcal or other SMT soldering iron
            3. Need to install bulk decoupling and small-value high-freq decoupling capacitors on front (footprints are there but they are not installed)
            4. You'll obviously have to remove the bottom PCB SDRAM chips if you want to populate the top PCB with SDRAM chips.
 * 2 DDR SDRAM devices on back-side:  Mira 64Mbit/SDRAM  4M*16 P2V64S40 54-pin
   . more details (copied from Jeremy Collake aka db90h of DD-WRT): http://www.dd-wrt.com/phpBB2/viewtopic.php?t=2542
     . RAM : Mira p2v28s40btp [5409fa03-6]
     . spec: http://www.deutron.com.tw/data_sheets/sdram/p2v28s_0btp11_07024.pdf
       . P2 == Mira DRAM
       . V == LVTTL
       . 28 == density (128mbit)
       . S == synchronous DRAM
       . 4 == x16 organization (4 banks - 16-bit)
       . 0 == random column
       . B == 3rd gen
       . TP == TSOP(II)
 * 2 serial ports detected, the first port (/dev/tts/0) is brought out on a 4 pin header labeled J1, located near a corner of the PCB. Pin 1 is nearest the edge. The signals are low level, and not directly EIA232 compatible. The default baud rate is 115K. When booting, CTRL-C will interrupt the CFE monitor. The pinout is:
       . 1 - 3.3V
       . 2 - Ground
       . 3 - Data out
       . 4 - Data in
 * Noticed that there is an LED missing (LED4), and a series resistor (R4) is also missing.  I wonder if that can be used for GPIO and thus for the SD card slot kernel mod??
 * Need to confirm the JTAG pinout.  It is rumored that J1 can be used for JTAG, but that's only 4 pins; JTAG needs TRST, TMS, TDI, TDO, TCK, GND (but TRST isn't really needed as it just pulls/puts the device out of/in reset)
