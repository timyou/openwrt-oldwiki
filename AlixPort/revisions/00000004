== Building firmware for the alix 2c2: ==

http://www.netgate.com/product_info.php?cPath=60&products_id=509

 * config buildroot with the following options:
  * Target System: x86
  * Subtarget: Generic
  * Target Profile: PCEngines Alix
  * Target Options: 
   * jffs2, squashfs, ext2
   * serial baud rate: 38400
   * Kernel partition size: 12 (my preference)
   * root partition: /dev/hda2
   * Filsystem part size: 96MB (my preference)
   * Maximum number of inodes: 1500

This patch would be interesting, perhaps I will have time for it later:
http://www.docunext.com/wiki/My_Notes_on_Patching_2.6.22_with_OCF


On a linux box with a cf reader:
 * Make sure the card isn't mounted, often its mounted by default
 * use dd to write the image to the disk:
{{{
 dd if=openwrt-x86-squashfs.image of=/dev/sda
}}}
 * After booting linux, it took a long time for the jffs partition to init.
 * After jffs init, run firstboot manually (causes oops?)


To upgrade from within openwrt:
 * use dd to write the image to the disk:
{{{
 dd if=openwrt-x86-squashfs.image of=/dev/hda
}}}
 * reboot
 * make sure the root_data partition was regenerated automatically


Using the LEDs on the alix: 
{{{
You should get three LED devices under /sys/class/leds/ 
- alix:1, alix:2 and alix:3

This should turn on one led:
  echo 1 > /sys/class/leds/alix:1/brightness

And off:
  echo 0 > /sys/class/leds/alix:1/brightness

And this should make it blink:
  echo timer > /sys/class/leds/alix:1/trigger
  echo 1000 > /sys/class/leds/alix:1/delay_off
  echo 100 > /sys/class/leds/alix:1/delay_on
}}}

After rebooting, you will have to add the wan interface to /etc/config/network


Entering failsafe:
 * The button does not seem to work
 * Attach serial cable, speed is 38400
 * Press Esc during the memory check
 * Choose 'safe mode' in the grub menu

== More Info ==

/proc/cpuinfo
{{{
processor       : 0
vendor_id       : AuthenticAMD
cpu family      : 5
model           : 10
model name      : Geode(TM) Integrated Processor by AMD PCS
stepping        : 2
cpu MHz         : 498.049
cache size      : 128 KB
fdiv_bug        : no
hlt_bug         : no
f00f_bug        : no
coma_bug        : no
fpu             : yes
fpu_exception   : yes
cpuid level     : 1
wp              : yes
flags           : fpu de pse tsc msr cx8 sep pge cmov clflush mmx mmxext 3dnowext 3dnow up
bogomips        : 997.37
clflush size    : 32
}}}

/proc/meminfo
{{{
MemTotal:       257144 kB
MemFree:        227688 kB
Buffers:         15004 kB
Cached:           4136 kB
SwapCached:          0 kB
Active:           4800 kB
Inactive:        15712 kB
SwapTotal:           0 kB
SwapFree:            0 kB
Dirty:               0 kB
Writeback:           0 kB
AnonPages:        1372 kB
Mapped:            812 kB
Slab:             7140 kB
SReclaimable:     4388 kB
SUnreclaim:       2752 kB
PageTables:        192 kB
NFS_Unstable:        0 kB
Bounce:              0 kB
CommitLimit:    128572 kB
Committed_AS:     4496 kB
VmallocTotal:   777948 kB
VmallocUsed:       820 kB
VmallocChunk:   777092 kB
}}}

dmesg
{{{
Linux version 2.6.23.16 (bpfountz@bens-computer) (gcc version 4.1.2) #1 SMP Tue Feb 19 16:53:48 EST 2008
BIOS-provided physical RAM map:
 BIOS-e820: 0000000000000000 - 00000000000a0000 (usable)
 BIOS-e820: 00000000000f0000 - 0000000000100000 (reserved)
 BIOS-e820: 0000000000100000 - 0000000010000000 (usable)
 BIOS-e820: 00000000fff00000 - 0000000100000000 (reserved)
256MB LOWMEM available.
Entering add_active_range(0, 0, 65536) 0 entries of 256 used
Zone PFN ranges:
  DMA             0 ->     4096
  Normal       4096 ->    65536
Movable zone start PFN for each node
early_node_map[1] active PFN ranges
    0:        0 ->    65536
On node 0 totalpages: 65536
  DMA zone: 32 pages used for memmap
  DMA zone: 0 pages reserved
  DMA zone: 4064 pages, LIFO batch:0
  Normal zone: 480 pages used for memmap
  Normal zone: 60960 pages, LIFO batch:15
  Movable zone: 0 pages used for memmap
DMI not present or invalid.
Allocating PCI resources starting at 20000000 (gap: 10000000:eff00000)
Built 1 zonelists in Zone order.  Total pages: 65024
Kernel command line: block2mtd.block2mtd=/dev/hda2,65536,rootfs root=/dev/mtdblock0 rootfstype=squashfs init=/etc/preinit  noinitrd console=tty0 console=ttyS0,38400n8 reboot=bios
No local APIC present or hardware disabled
mapped APIC to ffffb000 (0120a000)
Initializing CPU#0
PID hash table entries: 1024 (order: 10, 4096 bytes)
Detected 498.049 MHz processor.
Console: colour dummy device 80x25
console [tty0] enabled
console [ttyS0] enabled
Dentry cache hash table entries: 32768 (order: 5, 131072 bytes)
Inode-cache hash table entries: 16384 (order: 4, 65536 bytes)
Memory: 256940k/262144k available (1529k kernel code, 4812k reserved, 595k data, 184k init, 0k highmem)
virtual kernel memory layout:
    fixmap  : 0xfffb9000 - 0xfffff000   ( 280 kB)
    vmalloc : 0xd0800000 - 0xfffb7000   ( 759 MB)
    lowmem  : 0xc0000000 - 0xd0000000   ( 256 MB)
      .init : 0xc0319000 - 0xc0347000   ( 184 kB)
      .data : 0xc027e576 - 0xc031325c   ( 595 kB)
      .text : 0xc0100000 - 0xc027e576   (1529 kB)
Checking if this processor honours the WP bit even in supervisor mode... Ok.
Calibrating delay using timer specific routine.. 997.37 BogoMIPS (lpj=4986878)
Mount-cache hash table entries: 512
CPU: After generic identify, caps: 0088a93d c0c0a13d 00000000 00000000 00000000 00000000 00000000 00000000
CPU: L1 I Cache: 64K (32 bytes/line), D cache 64K (32 bytes/line)
CPU: L2 Cache: 128K (32 bytes/line)
CPU: After all inits, caps: 0088a93d c0c0a13d 00000000 00000000 00000000 00000000 00000000 00000000
Compat vDSO mapped to ffffe000.
Checking 'hlt' instruction... OK.
Checking for popad bug... OK.
SMP alternatives: switching to UP code
Freeing SMP alternatives: 11k freed
CPU0: AMD Geode(TM) Integrated Processor by AMD PCS stepping 02
SMP motherboard not detected.
Local APIC not detected. Using dummy APIC emulation.
Brought up 1 CPUs
NET: Registered protocol family 16
PCI: PCI BIOS revision 2.10 entry at 0xfcc2b, last bus=0
PCI: Using configuration type 1
Setting up standard PCI resources
Linux Plug and Play Support v0.97 (c) Adam Belay
PCI: Probing PCI hardware
PCI: Probing PCI hardware (bus 00)
NET: Registered protocol family 2
Time: tsc clocksource has been installed.
IP route cache hash table entries: 2048 (order: 1, 8192 bytes)
TCP established hash table entries: 8192 (order: 4, 98304 bytes)
TCP bind hash table entries: 8192 (order: 4, 65536 bytes)
TCP: Hash tables configured (established 8192 bind 8192)
TCP reno registered
microcode: CPU0 not a capable Intel processor
IA-32 Microcode Update Driver: v1.14a <tigran@aivazian.fsnet.co.uk>
scx200: NatSemi SCx200 Driver
squashfs: version 3.0 (2006/03/15) Phillip Lougher
Registering mini_fo version $Id$
JFFS2 version 2.2. (NAND) (SUMMARY)  Â© 2001-2006 Red Hat, Inc.
io scheduler noop registered
io scheduler deadline registered (default)
isapnp: Scanning for PnP cards...
isapnp: No Plug & Play device found
Real Time Clock Driver v1.12ac
Non-volatile memory driver v1.2
AMD Geode RNG detected
Serial: 8250/16550 driver $Revision: 1.90 $ 2 ports, IRQ sharing disabled
serial8250: ttyS0 at I/O 0x3f8 (irq = 4) is a 16550A
Uniform Multi-Platform E-IDE driver Revision: 7.00alpha2
ide: Assuming 33MHz system bus speed for PIO modes; override with idebus=xx
Probing IDE interface ide0...
hda: SanDisk SDCFB-512, CFA DISK drive
Probing IDE interface ide1...
ide0 at 0x1f0-0x1f7,0x3f6 on irq 14
hda: max request size: 128KiB
hda: 1000944 sectors (512 MB) w/1KiB Cache, CHS=993/16/63
 hda: hda1 hda2
block2mtd: version $Revision: 1.30 $
Creating 1 MTD partitions on "rootfs":
0x00000000-0x06070000 : "rootfs"
mtd: partition "rootfs_data" created automatically, ofs=2E0000, len=5D90000
0x002e0000-0x06070000 : "rootfs_data"
block2mtd: mtd0: [rootfs] erase_size = 64KiB [65536]
PNP: No PS/2 controller found. Probing ports directly.
i8042.c: No controller found.
mice: PS/2 mouse device common for all mice
nf_conntrack version 0.5.0 (4096 buckets, 16384 max)
ip_tables: (C) 2000-2006 Netfilter Core Team
TCP vegas registered
NET: Registered protocol family 1
NET: Registered protocol family 17
802.1Q VLAN Support v1.8 Ben Greear <greearb@candelatech.com>
All bugs added by David S. Miller <davem@redhat.com>
Using IPI Shortcut mode
VFS: Mounted root (squashfs filesystem) readonly.
Freeing unused kernel memory: 184k freed
Please be patient, while OpenWrt loads ...
mini_fo: using base directory: /
mini_fo: using storage directory: /jffs
natsemi dp8381x driver, version 2.1, Sept 11, 2006
  originally by Donald Becker <becker@scyld.com>
  2.4.x kernel port by Jeff Garzik, Tjeerd Mulder
Registered led device: alix:1
Registered led device: alix:2
Registered led device: alix:3
ne2k-pci.c:v1.03 9/22/2003 D. Becker/P. Gortmaker
via-rhine.c:v1.10-LK1.4.3 2007-03-06 Written by Donald Becker
PCI: Setting latency timer of device 0000:00:09.0 to 64
eth0: VIA Rhine III (Management Adapter) at 0xe0000000, 00:0d:b9:13:b0:60, IRQ 10.
eth0: MII PHY found at address 1, status 0x7849 advertising 05e1 Link 0000.
PCI: Setting latency timer of device 0000:00:0b.0 to 64
eth1: VIA Rhine III (Management Adapter) at 0xe0040000, 00:0d:b9:13:b0:61, IRQ 12.
eth1: MII PHY found at address 1, status 0x786d advertising 05e1 Link cde1.
eth0: link down
eth1: link up, 100Mbps, full-duplex, lpa 0xCDE1
IMQ starting with 1 devices...
IMQ driver loaded successfully.
        Hooking IMQ before NAT on PREROUTING.
        Hooking IMQ after NAT on POSTROUTING.
IPP2P v0.8.1_rc1 loading
arc4: Unknown symbol crypto_unregister_alg
arc4: Unknown symbol crypto_register_alg
sha1: Unknown symbol crypto_unregister_alg
sha1: Unknown symbol crypto_register_alg
PPP generic driver version 2.4.2
}}}
