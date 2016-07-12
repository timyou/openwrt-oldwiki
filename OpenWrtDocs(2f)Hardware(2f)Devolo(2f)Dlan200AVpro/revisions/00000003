= Devolo dLAN 200 AVpro host =

This board is a HomePlug AV- Ethernet bridge based on an Intel IXP420.

{{{
SoC : Intel IXP420ABB
RAM : 32MB
Flash : 8MB
Ethernet switch : IC+ 175C
Serial : yes
JTAG : yes
Mini-PCI slot : yes
HomeplugAV frontend : Intellon INT6000
}}}

== Serial port ==

Serial console is located on header ST9, pinout as follows :

{{{
Ethernet

GND (x) (x)
    (x) (x)
    (x) (x) RX
TX  (x) (x)
    (x) [x] VCC

Capacitor C24
}}}

== Bootlog ==

{{{
RedBoot(tm) bootstrap and debug environment [ROM]
Red Hat certified release, version 2.01 - built 15:50:05, Mar 31 2008

Platform: devolo dLAN Host Platform (XScale) BE
Copyright (C) 2000, 2001, 2002, 2003, 2004 Red Hat, Inc.

RAM: 0x00000000-0x02000000, [0x00015848-0x01fe1000] available
FLASH: 0x50000000 - 0x50800000, 128 blocks of 0x00010000 bytes each.
== Executing boot script in 1.000 seconds - enter ^C to abort
RedBoot> start -n
Starting 'IMAGE 0x1' ...
Using base address 0x00030000 and length 0x0033af6c
Linux version 2.6.21.2 (timo@TRtux) (gcc version 3.4.2) #1 Wed Jun 11 16:00:47 CEST 2008
CPU: XScale-IXP42x Family [690541f2] revision 2 (ARMv5TE), cr=000039ff
Machine: devolo dLAN Host
Memory policy: ECC disabled, Data cache writeback
CPU0: D VIVT undefined 5 cache
CPU0: I cache: 32768 bytes, associativity 32, 32 byte lines, 32 sets
CPU0: D cache: 32768 bytes, associativity 32, 32 byte lines, 32 sets
Built 1 zonelists.  Total pages: 8128
Kernel command line: console=ttyS1,115200 rootfstype=squashfs mtdparts=IXP4XX-Flash.0:0x50000@0x0(RedBoot),0x1000@0x7ff000(RedBootconfig),0xf000@0x7f0000(FISdirectory),0x10000@0x7f0000(FCblock),0x10000@0x7d0000(Data),0x10000@0x7e0000(SysMgrconfig),0x790000@0x50000(Flash),0x3c0000@0x50000(Update),0x3c0000@0x410000(Firmware),0xd0
000@0x410000(kernel),0x26b000@0x4e0000(root) root=/dev/mtdblock10
PID hash table entries: 128 (order: 7, 512 bytes)
Dentry cache hash table entries: 4096 (order: 2, 16384 bytes)
Inode-cache hash table entries: 2048 (order: 1, 8192 bytes)
Memory: 32MB = 32MB total
Memory: 30696KB available (1544K code, 119K data, 88K init)
Mount-cache hash table entries: 512
CPU: Testing write buffer coherency: ok
NET: Registered protocol family 16
IXP4xx: Using 16MiB expansion bus window size
PCI: IXP4xx is host
PCI: IXP4xx Using indirect access for memory space
PCI: bus0: Fast back to back transfers enabled
NET: Registered protocol family 2
Time: OSTS clocksource has been installed.
IP route cache hash table entries: 1024 (order: 0, 4096 bytes)
TCP established hash table entries: 1024 (order: 1, 8192 bytes)
TCP bind hash table entries: 1024 (order: 0, 4096 bytes)
TCP: Hash tables configured (established 1024 bind 1024)
TCP reno registered
NetWinder Floating Point Emulator V0.97 (double precision)
squashfs: version 3.3 (2007/10/31) Phillip Lougher
io scheduler noop registered
io scheduler deadline registered (default)
IXP4xx Watchdog Timer: heartbeat 60 sec
Serial: 8250/16550 driver $Revision: 1.90 $ 2 ports, IRQ sharing disabled
serial8250.0: ttyS0 at MMIO 0xc8000000 (irq = 15) is a XScale
serial8250.0: ttyS1 at MMIO 0xc8001000 (irq = 13) is a XScale
RAMDISK driver initialized: 4 RAM disks of 10240K size 1024 blocksize
IXP4XX-Flash.0: Found 1 x16 devices at 0x0 in 16-bit bank
 Amd/Fujitsu Extended Query Table at 0x0040
number of CFI chips: 1
cfi_cmdset_0002: Disabling erase-suspend-program due to code brokenness.
RedBoot partition parsing not available
11 cmdlinepart partitions found on MTD device IXP4XX-Flash.0
Creating 11 MTD partitions on "IXP4XX-Flash.0":
0x00000000-0x00050000 : "RedBoot"
0x007ff000-0x00800000 : "RedBootconfig"
mtd: partition "RedBootconfig" doesn't start on an erase block boundary -- force read-only
0x007f0000-0x007ff000 : "FISdirectory"
mtd: partition "FISdirectory" doesn't end on an erase block -- force read-only
0x007f0000-0x00800000 : "FCblock"
0x007d0000-0x007e0000 : "Data"
0x007e0000-0x007f0000 : "SysMgrconfig"
0x00050000-0x007e0000 : "Flash"
0x00050000-0x00410000 : "Update"
0x00410000-0x007d0000 : "Firmware"
0x00410000-0x004e0000 : "kernel"
0x004e0000-0x0074b000 : "root"
mtd: partition "root" doesn't end on an erase block -- force read-only
Registered led device: L2
Registered led device: L3
Registered led device: L4
Registered led device: L5
Registered led device: L6
Registered led device: L7
Registered led device: L8
Registered led device: L9
u32 classifier
nf_conntrack version 0.5.0 (256 buckets, 2048 max)
ip_tables: (C) 2000-2006 Netfilter Core Team
TCP cubic registered
NET: Registered protocol family 1
XScale DSP coprocessor detected.
VFS: Mounted root (squashfs filesystem) readonly.
Freeing init memory: 88K
init started: BusyBox v1.7.3 (2008-06-11 16:04:04 CEST)
starting pid 106, tty '': '/etc/init.d/rcS'
Checking console ...!
Module dvlheartbeat initialized
Module dvlbutton initialized
Module dlanhw initialized
Checking flash mtd sections ...
ixp400: module license 'unspecified' taints kernel.
ixp400_eth: Initializing IXP400 NPE Ethernet driver software v. 1.7
ixp400_eth: CPU clock speed (approx) = 266 MHz
[warning] ixNpeDlNpeMgrInit - Warning:NPEA is not present.
ixp400_eth: eth0 is using NPEB and the PHY at address 24
ixp400_eth: eth1 is using NPEC and the PHY at address 0
ixp400_eth: Use default MAC address 00:0b:3b:ff:ee:dd for port 0
ixp400_eth: Use default MAC address 00:0b:3b:ff:ee:de for port 1

Please press Enter to activate this console. |Ebtables v2.0 registered
Bridge firewalling registered
device eth0 entered promiscuous mode
device eth1 entered promiscuous mode

process '-/tmp/bin/sh' (pid 172) exited. Scheduling it for restart.

Please press Enter to activate this console.
process '-/tmp/bin/sh' (pid 261) exited. Scheduling it for restart.

Please press Enter to activate this console. br0: port 2(eth1) entering learning state
br0: port 1(eth0) entering learning state
NET: Registered protocol family 17
ixp400_eth: Error reading MII reg 0 on phy 24
ixp400_eth: Error reading MII reg 1 on phy 24
ixp400_eth: Error reading MII reg 2 on phy 24
ixp400_eth: Error reading MII reg 3 on phy 24
ixp400_eth: Error reading MII reg 4 on phy 24
ixp400_eth: Error reading MII reg 5 on phy 24
ixp400_eth: Error reading MII reg 6 on phy 24
ixp400_eth: Error reading MII reg 7 on phy 24
br0: topology change detected, propagating
br0: port 2(eth1) entering forwarding state
br0: topology change detected, propagating
br0: port 1(eth0) entering forwarding state

process '-/tmp/bin/sh' (pid 262) exited. Scheduling it for restart.

Please press Enter to activate this console.
}}}

== Getting shell access ==

Redboot can be interrupted. It has a limited number of stock Redboot commands, but you can still choose to pass a custom kernel command line to Linux, to get shell access and networking, issue the following command in redboot :

{{{
start -c "console=ttyS1,115200 rootfstype=squashfs mtdparts=IXP4XX-Flash.0:0x3c0000@0x410000(Firmware),0x26b000@0x4e0000(root) root=/dev/mtdblock1 init=/bin/sh"
}}}

You then get shell access and allow network interfaces to be loaded with the NPE microcode.

 . CategoryModel ["CategoryIXP4xxDevice"]
