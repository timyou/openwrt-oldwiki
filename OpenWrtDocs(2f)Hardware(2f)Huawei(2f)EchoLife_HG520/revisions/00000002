= Huawei EchoLife HG520 =
The device is NOT supported in OpenWrt. The internals are very similar to the [:OpenWrtDocs/Hardware/Linksys/WAG54GX2:Linksys WAG54GX2].

{{{
Bootloader     : CFE version cfe.d010.2103 for BCM96348 (32bit,SP,BE)
System-On-Chip : Broadcom 6348 (CPU type 0x29107)
CPU Speed      : 240MHz, Bus: 133MHz, Ref: 26MHz
Flash size     : 4 MB
RAM            : 16 MB
Wireless       : On-board BCM4328 802.11b/g Wireless LAN Controller
Ethernet       : Unknown, switch BCM5325
USB            : Yes, 2.0 full-speed (12Mbit/s)
ADSL           : 2/2+
Serial         : yes J303
JTAG           : assumed on J201 (need no de-solder C186 to soler J201)
}}}

The {{{boot_wait}}} NVRAM variable is not defined.

== Firmware notes ==
We can build custom firmwares that will upload via the regular web interface. original firmware is linux-2.6-based

== Boot log ==
{{{
CFE version cfe.d010.2103 for BCM96348 (32bit,SP,BE)
Build Date: Tue Oct 25 20:59:43 CST 2005 (z47214@server)
Copyright (C) 2000,2001,2002,2003 Broadcom Corporation.

Initializing Arena.
Initializing Devices.
Ethernet Network Device: External PHY
CPU type 0x29107: 240MHz, Bus: 133MHz, Ref: 26MHz

Total memory used by CFE:  0x80401000 - 0x80523020 (1187872)
Initialized Data:          0x8041AFB0 - 0x8041C990 (6624)
BSS Area:                  0x8041C990 - 0x80421020 (18064)
Local Heap:                0x80421020 - 0x80521020 (1048576)
Stack Area:                0x80521020 - 0x80523020 (8192)
Text (code) segment:       0x80401000 - 0x8041AFA4 (106404)
Boot area (physical):      0x00524000 - 0x00564000
Relocation Factor:         I:00000000 - D:00000000

Board IP address                : 192.168.1.1:ffffff00
Host IP address                 : 192.168.1.100
Gateway IP address              :
Run from flash/host (f/h)       : f
Default host run file name      : vmlinux
Default host flash file name    : bcm963xx_fs_kernel
Boot delay (0-9 seconds)        : 1
Board Id Name                   : 96348GW-HG520-1
Psi size in KB                  : 64
Number of MAC Addresses (1-32)  : 11
Base MAC Address                : 00:11:f5:e6:9c:ff
Serial Number                   : 21500802198K61001749
Ethernet PHY Type               : Internal
Memory size in MB               : 16

*** Press any key to stop auto run (1 seconds) ***
Auto run second count down: 0
Code Address: 0x80010000, Entry Address: 0x80195018
Decompression OK!
Entry at 0x80195018
Closing network.
Starting program at 0x80195018
Linux version 2.6.8.1 (root@debian) (gcc version 3.4.2) #1 Wed Jan 4 19:40:50 HKT 2006
Total Flash size: 4096K with 71 sectors
96348GW-HG520-1 prom init
CPU revision is: 00029107
mpi: No Card is in the PCMCIA slot
Determined physical RAM map:
 memory: 00fa0000 @ 00000000 (usable)
On node 0 totalpages: 4000
  DMA zone: 4000 pages, LIFO batch:1
  Normal zone: 0 pages, LIFO batch:1
  HighMem zone: 0 pages, LIFO batch:1
Built 1 zonelists
Kernel command line: root=31:0 ro noinitrd
brcm mips: enabling icache and dcache...
Primary instruction cache 16kB, physically tagged, 2-way, linesize 16 bytes.
Primary data cache 8kB 2-way, linesize 16 bytes.
PID hash table entries: 64 (order 6: 512 bytes)
Using 120.000 MHz high precision timer.
Dentry cache hash table entries: 4096 (order: 2, 16384 bytes)
Inode-cache hash table entries: 2048 (order: 1, 8192 bytes)
Memory: 14060k/16000k available (1346k kernel code, 1920k reserved, 205k data, 72k init, 0k highmem)
Calibrating delay loop... 239.20 BogoMIPS
Mount-cache hash table entries: 512 (order: 0, 4096 bytes)
Checking for 'wait' instruction...  unavailable.
NET: Registered protocol family 16
Can't analyze prologue code at 8015f258
Software Watchdog Timer: 0.07 initialized. soft_noboot=0 soft_margin=1 sec (nowayout= 0)
PPP generic driver version 2.4.2
NET: Registered protocol family 24
Using noop io scheduler
bcm963xx_mtd driver v1.0
brcmboard: brcm_board_init entry
bcm963xx_serial driver v2.0
NET: Registered protocol family 2
IP: routing cache hash table of 512 buckets, 4Kbytes
TCP: Hash tables configured (established 512 bind 1024)
NET: Registered protocol family 1
NET: Registered protocol family 17
Ebtables v2.0 registered
NET: Registered protocol family 8
NET: Registered protocol family 20
802.1Q VLAN Support v1.8 Ben Greear <greearb@candelatech.com>
All bugs added by David S. Miller <davem@redhat.com>
VFS: Mounted root (squashfs filesystem) readonly.
Freeing unused kernel memory: 72k freed
init started:  BusyBox v1.00 (2006.01.04-11:43+0000) multi-call binary
Algorithmics/MIPS FPU Emulator v1.5


BusyBox v1.00 (2006.01.04-11:43+0000) Built-in shell (msh)
Enter 'help' for a list of built-in commands.


Loading drivers and kernel modules...

atmapi: module license 'Proprietary' taints kernel.
blaadd: blaa_detect entry
adsl: adsl_init entry
Broadcom BCMPROCFS v1.0 initialized
Broadcom BCM6348B0 Ethernet Network Device v0.3 Jan  4 2006 19:39:16
Config Ethernet Switch Through SPI Slave Select 0
eth0: MAC Address: 00:11:F5:E6:9C:FF
Broadcom BCM6348B0 USB Network Device v0.4 Jan  4 2006 19:39:17
usb0: MAC Address: 00 11 F5 E6 9D 00
usb0: Host MAC Address: 00 11 F5 E6 9D 01
PCI: Setting latency timer of device 0000:00:01.0 to 64
PCI: Enabling device 0000:00:01.0 (0004 -> 0006)
wl: srom not detected, using main memory mapped srom info (wombo board)
eth0 Link UP.
wl0: wlc_attach: using main board MAC address base in NVRAM (wombo board)
wl0 MAC Address: 00:11:F5:E6:9D:02
wl0: Broadcom BCM4318 802.11 Wireless Controller 3.91.41.0
Match Succeed!
BcmAdsl_Initialize=0xC0054280, g_pFnNotifyCallback=0xC00675C4
AdslCoreHwReset: AdslOemDataAddr = 0xA0FF73B0
dgasp: kerSysRegisterDyingGaspHandler: dsl0 registered

==>   Bcm963xx Software Version: EchoLife HG520V300R001B01D081.A2pB018b.d16f   <==

device usb0 entered promiscuous mode
br0: port 1(usb0) entering learning state
br0: topology change detected, propagating
br0: port 1(usb0) entering forwarding state
device eth0 entered promiscuous mode
br0: port 2(eth0) entering learning state
br0: topology change detected, propagating
br0: port 2(eth0) entering forwarding state
Setting country code "RU"
channel selected 11
channel selected 11
device wl0 entered promiscuous mode
br0: port 3(wl0) entering learning state
br0: topology change detected, propagating
br0: port 3(wl0) entering forwarding state
SIOCGIFFLAGS: No such device
pvc2684d: Interface "nas_255_65535" created sucessfully

blaadd: open error -125
pvc2684d: Communicating over ATM 0.255.65535, encapsulation: LLC

pvc2684d: Interface "nas_1_50" created sucessfully

pvc2684d: Communicating over ATM 0.1.50, encapsulation: LLC

pvc2684d: Interface "nas_1_91" created sucessfully

pvc2684d: Communicating over ATM 0.1.91, encapsulation: LLC

pvc2684d: Interface "nas_1_92" created sucessfully

pvc2684d: Communicating over ATM 0.1.92, encapsulation: LLC

device eth0 left promiscuous mode
br0: port 2(eth0) entering disabled state
device usb0 left promiscuous mode
br0: port 1(usb0) entering disabled state
device usb0 entered promiscuous mode
br0: port 1(usb0) entering learning state
br0: topology change detected, propagating
br0: port 1(usb0) entering forwarding state
device eth0.3 entered promiscuous mode
device eth0.4 entered promiscuous mode
device eth0.5 entered promiscuous mode
device nas_1_50 is not a slave of br0
device nas_1_50 entered promiscuous mode
br0: port 6(nas_1_50) entering learning state
br0: topology change detected, propagating
br0: port 6(nas_1_50) entering forwarding state
device wl0 left promiscuous mode
br0: port 3(wl0) entering disabled state
device wl0 entered promiscuous mode
br0: port 3(wl0) entering learning state
br0: topology change detected, propagating
br0: port 3(wl0) entering forwarding state
device eth0.2 entered promiscuous mode
device nas_1_91 is not a slave of br0
device nas_1_91 entered promiscuous mode
br1: port 2(nas_1_91) entering learning state
br1: topology change detected, propagating
br1: port 2(nas_1_91) entering forwarding state
device nas_1_92 is not a slave of br0
device nas_1_92 entered promiscuous mode
br1: port 3(nas_1_92) entering learning state
br1: topology change detected, propagating
br1: port 3(nas_1_92) entering forwarding state
eth0.2: dev_set_promiscuity(master, 1)
device eth0 entered promiscuous mode
br1: port 1(eth0.2) entering learning state
br1: topology change detected, propagating
br1: port 1(eth0.2) entering forwarding state
eth0.3: dev_set_promiscuity(master, 1)
br0: port 2(eth0.3) entering learning state
br0: topology change detected, propagating
br0: port 2(eth0.3) entering forwarding state
eth0.4: dev_set_promiscuity(master, 1)
br0: port 4(eth0.4) entering learning state
br0: topology change detected, propagating
br0: port 4(eth0.4) entering forwarding state
eth0.5: dev_set_promiscuity(master, 1)
br0: port 5(eth0.5) entering learning state
br0: topology change detected, propagating
br0: port 5(eth0.5) entering forwarding state
Initing TR069 Stack...
No servers specified.
}}}
