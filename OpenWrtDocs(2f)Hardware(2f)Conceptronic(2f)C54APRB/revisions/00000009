= Conceptronic C54APRB =

The Conceptronic C54APRB is a router with built-in ADSL modem for Annex B (ISDN) connections. It is based on the AR7 chipset.

Seems a clone of the D-Link DSL-G604T

== Picture ==

attachment:c54aprb.jpg

== Serial ==

== Conceptronic C54APRB serial pinout ==
{{{
_______________________________________
|                                      \
|                                       led
|                                       led
| Pin 5: TX      ----> ()               led
| Pin 4: GND     ----> ()               led
| Pin 3: + 3.3 v ----> ()               |
| Pin 2: GND     ----> ()               |
| Pin 1: RX      ----> []               led     Front of C54APRB
|                     JP5               |
|                                       led
|                                       |
|                                       led
|                                       led
|______________________________________/
}}}

The console is located aproximately in center of a board, it's JP5, the only 5-pin 2,54mm-step connector. Usualy it is already soldered-in. Voltage reference is 3.3 volts and it is set by default at 38400,8,N,1.

== Flashing ==

OpenWrt ar7-2.6 works very well on this device. Grab the latest SVN revision. Compile an ar7-2.6 target. Once finished :

Set up a virtual interface with the IP 10.8.8.7 so that you will be able to reach 10.8.8.8 which is the default IP address for the C54APRB.

Now run the adam2 flash script :

{{{
./scripts/adam2flash.pl 10.8.8.8 bin/openwrt-ar7-2.6-squashfs.bin
}}}

and it will flash your device with an OpenWrt firmware. Wait a few seconds, the device then reboots and you are in :

{{{
Adam2_AR7RD >
Press any key to abort OS load, or wait 5 seconds for OS to boot...
Linux version 2.6.21.1 (florian@dorelei) (gcc version 4.1.2) #1 Tue Jun 5 16:25:45 CEST 2007
CPU revision is: 00018448
Determined physical RAM map:
 memory: 01000000 @ 14000000 (usable)
Built 1 zonelists.  Total pages: 4064
Kernel command line: init=/etc/preinit rootfstype=squashfs,jffs2, console=ttyS0,38400n8r
Primary instruction cache 16kB, physically tagged, 4-way, linesize 16 bytes.
Primary data cache 16kB, 4-way, linesize 16 bytes.
Synthesized TLB refill handler (20 instructions).
Synthesized TLB load handler fastpath (32 instructions).
Synthesized TLB store handler fastpath (32 instructions).
Synthesized TLB modify handler fastpath (31 instructions).
PID hash table entries: 64 (order: 6, 256 bytes)
Using 75.000 MHz high precision timer.
Linux version 2.6.21.1 (florian@dorelei) (gcc version 4.1.2) #1 Tue Jun 5 16:25:45 CEST 2007
CPU revision is: 00018448
Determined physical RAM map:
 memory: 01000000 @ 14000000 (usable)
Built 1 zonelists.  Total pages: 4064
Kernel command line: init=/etc/preinit rootfstype=squashfs,jffs2, console=ttyS0,38400n8r
Primary instruction cache 16kB, physically tagged, 4-way, linesize 16 bytes.
Primary data cache 16kB, 4-way, linesize 16 bytes.
Synthesized TLB refill handler (20 instructions).
Synthesized TLB load handler fastpath (32 instructions).
Synthesized TLB store handler fastpath (32 instructions).
Synthesized TLB modify handler fastpath (31 instructions).
PID hash table entries: 64 (order: 6, 256 bytes)
Using 75.000 MHz high precision timer.
Dentry cache hash table entries: 2048 (order: 1, 8192 bytes)
Inode-cache hash table entries: 1024 (order: 0, 4096 bytes)
Memory: 13468k/16388k available (2076k kernel code, 180k reserved, 435k data, 112k init)
Mount-cache hash table entries: 512
NET: Registered protocol family 16
vlynq0: regs 0x08611800, irq 29, mem 0x04000000
vlynq1: regs 0x08611c00, irq 33, mem 0x0c000000
vlynq0: linked
vlynq-pci: attaching device TI ACX111 at vlynq0
registering PCI controller with io_map_base unset
Generic PHY: Registered new driver
Time: MIPS clocksource has been installed.
NET: Registered protocol family 2
IP route cache hash table entries: 1024 (order: 0, 4096 bytes)
TCP established hash table entries: 512 (order: 0, 4096 bytes)
TCP bind hash table entries: 512 (order: -1, 2048 bytes)
TCP: Hash tables configured (established 512 bind 512)
TCP reno registered
squashfs: version 3.0 (2006/03/15) Phillip Lougher
Registering mini_fo version $Id$
JFFS2 version 2.2. (NAND) (C) 2001-2006 Red Hat, Inc.
io scheduler noop registered
io scheduler deadline registered (default)
ar7_wdt: timer margin 59 seconds (prescale 65535, change 57180, freq 62500000)
Serial: 8250/16550 driver $Revision: 1.90 $ 2 ports, IRQ sharing disabled
serial8250: ttyS0 at MMIO 0x8610e00 (irq = 15) is a TI-AR7
serial8250: ttyS1 at MMIO 0x8610f00 (irq = 16) is a TI-AR7
Fixed PHY: Registered new driver
Device 'fixed@100:1' does not have a release() function, it is broken and must be fixed.
BUG: at drivers/base/core.c:106 device_release()
Call Trace:
[<94109818>] dump_stack+0x8/0x34
[<94202ac4>] kobject_cleanup+0x68/0x98
[<94203c6c>] kref_put+0x10c/0x124
[<94388254>] fixed_init+0x1fc/0x24c
[<94375684>] init+0xbc/0x1f4
[<94105494>] kernel_thread_helper+0x10/0x18

cpmac-mii: probed
cpmac: device eth0 (regs: 08612800, irq: 41, phy: fixed@100:1, mac: 00:80:5a:31:ba:c0)
cpmac: device eth1 (regs: 08610000, irq: 27, phy: 0:1f, mac: 00:80:5a:31:ba:c0)
physmap platform flash device: 00400000 at 10000000
physmap-flash.0: Found 1 x16 devices at 0x0 in 16-bit bank
 Amd/Fujitsu Extended Query Table at 0x0040
number of CFI chips: 1
cfi_cmdset_0002: Disabling erase-suspend-program due to code brokenness.
cmdlinepart partition parsing not available
RedBoot partition parsing not available
Parsing AR7 partition map...
4 ar7part partitions found on MTD device physmap-flash.0
Creating 4 MTD partitions on "physmap-flash.0":
0x00000000-0x00010000 : "loader"
0x003f0000-0x00400000 : "config"
0x00010000-0x003f0000 : "linux"
0x000da06f-0x003f0000 : "rootfs"
mtd: partition "rootfs" doesn't start on an erase block boundary -- force read-only
0x001b0000-0x003f0000 : "rootfs_data"
Registered led device: ar7:status
nf_conntrack version 0.5.0 (128 buckets, 1024 max)
ip_tables: (C) 2000-2006 Netfilter Core Team
TCP vegas registered
NET: Registered protocol family 1
NET: Registered protocol family 17
Bridge firewalling registered
802.1Q VLAN Support v1.8 Ben Greear <greearb@candelatech.com>
All bugs added by David S. Miller <davem@redhat.com>
VFS: Mounted root (squashfs filesystem) readonly.
Freeing unused kernel memory: 112k freed
Warning: unable to open an initial console.
Algorithmics/MIPS FPU Emulator v1.5
mini_fo: using base directory: /
mini_fo: using storage directory: /tmp/root
init started:  BusyBox v1.4.2 (2007-06-04 16:49:37 CEST) multi-call binary
Please press Enter to activate this console. fixed@100:1 not found
eth0: Could not attach to PHY
fixed@100:1 not found
eth0: Could not attach to PHY
fixed@100:1 not found
eth0: Could not attach to PHY
fixed@100:1 not found
eth0: Could not attach to PHY
PPP generic driver version 2.4.2
acx: this driver is still EXPERIMENTAL
acx: reading README file and/or Craig's HOWTO is recommended, visit http://acx100.sf.net in case of further questions/discussion
acx: compiled to use 32bit I/O access. I/O timing issues might occur, such as non-working firmware upload. Report them
acx: running on a little-endian CPU
acx: PCI module v0.3.36 initialized, waiting for cards to probe...
PCI: Enabling device 0000:00:00.0 (0000 -> 0002)
acx: found ACX111-based wireless network card at 0000:00:00.0, irq:0, phymem1:0x4000000, phymem2:0x4022000, mem1:0xa4000000, mem1_siz2
initial debug setting is 0x000A
acx: can't use IRQ 0
pci_set_power_state(): 0000:00:00.0: state=3, current state=5
acx_pci: probe of 0000:00:00.0 failed with error -5
jffs2_scan_eraseblock(): End of filesystem marker found at 0x0
jffs2_build_filesystem(): unlocking the mtd device... done.
jffs2_build_filesystem(): erasing all blocks after the end marker... done.
mini_fo: using base directory: /
mini_fo: using storage directory: /jffs



BusyBox v1.4.2 (2007-06-04 16:49:37 CEST) Built-in shell (ash)
Enter 'help' for a list of built-in commands.

  _______                     ________        __
 |       |.-----.-----.-----.|  |  |  |.----.|  |_
 |   -   ||  _  |  -__|     ||  |  |  ||   _||   _|
 |_______||   __|_____|__|__||________||__|  |____|
          |__| W I R E L E S S   F R E E D O M
 KAMIKAZE (bleeding edge, r7505) -------------------
  * 10 oz Vodka       Shake well with ice and strain
  * 10 oz Triple sec  mixture into 10 shot glasses.
  * 10 oz lime juice  Salute!
 ---------------------------------------------------
root@OpenWrt:/#
}}}

== JTAG ==

["CategoryAR7Device"] CategoryModel
