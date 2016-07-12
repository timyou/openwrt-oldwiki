= Cellvision CAS-771W =

The Cellvision CAS-771 IP camera is a Linux based IP camera. It comes in two flavours: wired and wired/wireless. This page describes the Wireless one.

== Technical specifications ==

{{{
CPU : Infineon ADM5120 CPU
Wi-Fi : Ralink RT2500
Video : CPIA2
USB : audio / slave /host
RAM : 32Mb
Flash : 4Mb NOR
}}}

== Known models ==

Cellvision does not directly sell to customers, but acts purely as an ODM company.
Known models are:
  * Airlink101 [http://www.airlink101.com/products/aicap650w.html AICAP650W]
  * GSF [http://www.gsf.com.my/ipcam/index.htm CAS-771W]
  * IODATA [http://www.iodata.jp/prod/network/videoserver/2005/ts-mcam/index.htm TS-MCAM-G]
  * Planet [http://www.planet.com.tw/product/product_dm.php?product_id=457&menu_id=24 ICA-210W]
  * Simicom technologies CAS-771W
  * SparkLAN [http://www.sparklan.com/product_details.php?prod_id=150 CAS-771W]
  * V-Gear [http://vgear.com/products/list.asp?ProdID=AMVG1-010-074-G LiveCam]

== Serial pinout ==

{{{
GND RX TX VCC
 x  x   x  x


USB Rst btn Ethernet Power
}}}

=== Bootlog ===

{{{
ADM5120 Boot v3.0.2:
LINUX/5120 started...
CPU revision is: 0001800b
Primary instruction cache 8kb, linesize 16 bytes (2 ways)
Primary data cache 8kb, linesize 16 bytes (2 ways)
Linux version 2.4.18-5120-05 (root@localhost.localdomain) v1.00 #2439 Wed May 24 15:23:37 CST 2006
am5120_setup() starts.
System has PCI BIOS
Determined physical RAM map:
 memory: 01c15000 @ 003eb000 (usable)
Initial ramdisk at: 0x80217000 (1750879 bytes)
On node 0 totalpages: 8192
zone(0): 8192 pages.
zone(1): 0 pages.
zone(2): 0 pages.
Kernel command line: root=/dev/ram0 console=ttyS0
CPU clock: 175MHz
Calibrating delay loop... 174.48 BogoMIPS
Memory: 28232k/28756k available (1944k kernel code, 524k reserved, 1820k data, 60k init, 0k highmem)
Dentry-cache hash table entries: 4096 (order: 3, 32768 bytes)
Inode-cache hash table entries: 2048 (order: 2, 16384 bytes)
Mount-cache hash table entries: 512 (order: 0, 4096 bytes)
Buffer-cache hash table entries: 1024 (order: 0, 4096 bytes)
Page-cache hash table entries: 8192 (order: 3, 32768 bytes)
Checking for 'wait' instruction...  available.
POSIX conformance testing by UNIFIX
Autoconfig PCI channel 0x802167d8
Scanning bus 00, I/O 0x11500000:0x115ffff0, Mem 0x11400000:0x11500000
00:00.0 Class 0600: 1317:5120
        Mem unavailable -- skipping
        I/O unavailable -- skipping
00:03.0 Class 0c03: 1033:0035 (rev 43)
        Mem at 0x11400000 [size=0x1000]
00:03.1 Class 0c03: 1033:0035 (rev 43)
        Mem at 0x11401000 [size=0x1000]
00:03.2 Class 0c03: 1033:00e0 (rev 04)
        Mem at 0x11402000 [size=0x100]
fixup resource
fixup host controller
am5120 fix up
fixup resource
fixup resource
fixup resource
pcibios_fixup
fixup IRQ
slot=0 pin=0
PCI Interrupt Line = 0x0
PCI Interrupt Pin = 0x0
slot=3 pin=1
PCI Interrupt Line = 0x7
PCI Interrupt Pin = 0x1
slot=3 pin=2
PCI Interrupt Line = 0x0
PCI Interrupt Pin = 0x2
slot=3 pin=3
PCI Interrupt Line = 0x8
PCI Interrupt Pin = 0x3
Linux NET4.0 for Linux 2.4
Based upon Swansea University Computer Society NET3.039
Initializing RT netlink socket
Starting kswapd
JFFS2 version 2.2. (C) 2001-2003 Red Hat, Inc.
pty: 256 Unix98 ptys configured
HDLC line discipline: version $Revision: 1.1.1.1 $, maxframe=4096
N_HDLC line discipline registered.
block: 64 slots per queue, batch=16
RAMDISK driver initialized: 16 RAM disks of 6144K size 1024 blocksize
loop: loaded (max 8 devices)
ADM5120 Switch Module Init
PPP generic driver version 2.4.1
PPP Deflate Compression module registered
PPP BSD Compression module registered
bond0 registered with MII link monitoring set to 100 ms, in active-backup mode.
Linux video capture interface: v1.00
SCSI subsystem driver Revision: 1.00
request_module[scsi_hostadapter]: Root fs not mounted
request_module[scsi_hostadapter]: Root fs not mounted
AM5120 NOR flash device: 400000 at 1fc00000
AM5120 NOR flash device: Found 1 x16 devices at 0x0 in 16-bit mode
 Amd/Fujitsu Extended Query Table at 0x0040
number of CFI chips: 1
cfi_cmdset_0002: Disabling fast programming due to code brokenness.
Creating 3 MTD partitions on "AM5120 NOR flash device":
0x00008000-0x00010000 : "BoardCfg"
0x00010000-0x00030000 : "Linux NVFS"
0x00030000-0x00400000 : "Kernel Image"
AM5120 NOR flash device initialized
usb.c: registered new driver usbdevfs
usb.c: registered new driver hub
usb.c: registered new driver audio
audio.c: v1.0.0:USB Audio Class driver
Initializing USB Mass Storage driver...
usb.c: registered new driver usb-storage
USB Mass Storage support registered.
NET4: Linux TCP/IP 1.0 for NET4.0
IP Protocols: ICMP, UDP, TCP
IP: routing cache hash table of 512 buckets, 4Kbytes
TCP: Hash tables configured (established 2048 bind 2048)
NET4: Unix domain sockets 1.0/SMP for Linux NET4.0.
RAMDISK: Compressed image found at block 0
Freeing initrd memory: 1709k freed
EXT2-fs warning: maximal mount count reached, running e2fsck is recommended
VFS: Mounted root (ext2 filesystem).
Freeing prom memory: 0kb freed
Freeing unused kernel memory: 60k freed
init started:  BusyBox v1.00-pre1 (2004.05.31-03:09+0000) multi-call binary
check save config busying...
fsck.minix, 1.2 - 11/11/96
Forcing filesystem check on /dev/mtdblock1.
restore config files from flash to host...Done
Using /lib/modules/usb-ohci.o
usb-ohci.c: USB OHCI at membase 0xb1400000, IRQ 7
usb-ohci.c: usb-00:03.0, PCI device 1033:0035
usb.c: new USB bus registered, assigned bus number 1
hub.c: USB hub found
hub.c: 3 ports detected
usb-ohci.c: found OHCI device with no IRQ assigned. check BIOS settings!
Using /lib/modules/ehci-hcd.o
ehci_hcd 00:03.2: PCI device 1033:00e0
ehci_hcd 00:03.2: irq 8, pci mem b1402000
usb.c: new USB bus registered, assigned bus number 2
ehci_hcd 00:03.2: USB 2.0 enabled, EHCI 1.00, driver 2003-Dec-29/2.4
hub.c: USB hub found
hub.c: 5 ports detected
Using /lib/modules/ptc.o
pt: ver1.0.2
Using /lib/modules/cpia2.o
cpia2: V4L-Driver for Vision CPiA2 based cameras v1.21.1
usb.c: registered new driver cpia2
Using /lib/modules/msgeng.o
Warning: loading msgeng will taint the kernel: no license
  See http://www.tux.org/lkml/#export-tainted for information about tainted modules
MSGENG: message engine initialized
Using /lib/modules/imon.o
Warning: loading imon will taint the kernel: no license
  See http://www.tux.org/lkml/#export-tainted for information about tainted modules
SOC MONITOR: Soc monitor initialized.
 access_led control
access led timer terminated--
 status_led control
dispatch msg=83 val=0
=== This is IODATA ===
ptcmd: Open /dev/pt fail
time zone=(GMT) Greenwich Mean Time : Dublin, Edinburgh, Lisbon, London
tzfix: time zone adjust 2352 minutes
Sat Jan  1 00:00:00 GMT 2005
Formatting log file for the 1st use...done, 100 records
hub.c: new USB device 00:03.0-2, assigned address 2
cpia2_usb_probe...
cpia2: USB CPiA2 camera found
USB CPiA2 camera found
USB set configuration
USB set alternate
Device registered on minor 0
Reset default parameters
  CPiA Version: 2.164 (103.96)
  CPiA PnP-ID: 0553:0140:0103
  SensorID: 16.(version 15)
Setting fixed WAN IP Address ....
hub.c: new USB device 00:03.0-1, assigned address 3
usbaudio: device 3 audiocontrol interface 0 has 1 input and 1 output AudioStreaming interfaces
usbaudio: device 3 interface 2 altsetting 1 channels 1 framesize 2 configured
usbaudio: valid input sample rate 48000
usbaudio: valid input sample rate 44100
usbaudio: device 3 interface 2 altsetting 1: format 0x00000010 sratelo 44100 sratehi 48000 attributes 0x01
usbaudio: device 3 interface 1 altsetting 0 does not have an endpoint
usbaudio: device 3 interface 1 altsetting 1 channels 2 framesize 2 configured
usbaudio: valid output sample rate 48000
usbaudio: valid output sample rate 44100
usbaudio: device 3 interface 1 altsetting 1: format 0x01000010 sratelo 44100 sratehi 48000 attributes 0x01
usbaudio: registered dsp 14,3
usbaudio: warning: found 1 of 2 logical channels.
usbaudio: assuming that a stereo channel connected directly to a mixer is missing in search (got Labtec headset?). Should be fine.
Setting Hostname: CAS-771
usbaudio: registered mixer 14,0
usbaudio: registered mixer 14,16
dispatch msg=78 val=1
dispatch msg=78 val=2
dispatch msg=91 val=0
Starting DNS Proxy ....
Can't find log entry with id 102
Warning: Using hosts from /etc/hosts. Use master instead
Warning: SIGHUP will not work as expected
Can't find log entry with id 103
Starting UPNP ....
Starting ddns:disabled
buffer created
buffer created
Starting HTTP Server ....
starting udp_broadcast_server
Current Time: Sat Jan  1 00:00:02 GMT 2005
    mode:         16384
-o  offset:       0
-f  frequency:    0
    maxerror:     16384000
    esterror:     16384000
    status:       64 ( UNSYNC )
-p  timeconstant: 2
    precision:    1
    tolerance:    33554432
-t  tick:         10011
    time.tv_sec:  1104537602
    time.tv_usec: 914894
    return value: 5 (clock not synchronized)
[ws] websAdminSecurity Off
set user priv = 1
[ws] C760 UPLOAD Fix  initialized
[ws] C760 CGI module initialized
[ws] C771 CGI module initialized
[ws] C760 ASP module initialized
[ws] C771 ASP module initialized
[ws] C7XX CGI module initialed
[ws] C7XX WEB module initialized
default  user exist!
default admin exist!
group user alredy exist!!
group power alredy exist!!

+-------------------------------------+
| Wecome to CAS-771 Video/Audio System |
+-------------------------------------+
ptcmd: BTone = 2
[vs] Error: get_exposure() fail

Please press Enter to activate this console. reset cam width=640, height=480
input triggered
Sensor flag = 0x10, user mode = 0x20, frame rate = 0x20 width=640, height=480
Cpia2: Set Flicker Never
user effect=10
set mic boost: val=0x1
set mic gain: val=0x10
mic in volume: 0x1680
user effect=10
Cpia2: SetImageParam: Res:2, Framerate:4, Compress:0
set default jpeg compression rate
Cpia2: Set CompressIdx: mode: 0, framerate: 0x20, idx: 0, compress: 40
Requested params: bright 0x40, sat 0xAC, contrast 0x98, Hue 0xE
set trigger in state=0
Algorithmics/MIPS FPU Emulator v1.5



BusyBox v1.00-pre1 (2004.05.31-03:09+0000) Built-in shell (ash)
Enter 'help' for a list of built-in commands.

# lsmod
Module                  Size  Used by    Tainted: P

imon                    6992   1
msgeng                  3440   2
cpia2                  39392   1
ptc                     3552   0
ehci-hcd               24000   0 (unused)
usb-ohci               22424   0 (unused)
# cat /proc/cpuinfo
system type             : ADM5120 Demo Board
processor               : 0
cpu model               : MIPS 4Kc V0.11
BogoMIPS                : 174.48
wait instruction        : yes
microsecond timers      : yes
tlb_entries             : 16
extra interrupt vector  : yes
hardware watchpoint     : yes
VCED exceptions         : not available
VCEI exceptions         : not available
}}}

== Installing OpenWrt ==

Grab latest trunk revision. Choose the "ADM5120 2.6 (Little Endian)" target, then in "Target images", choose "ramdisk".

Once the build is complete, copy the file "openwrt-adm5120-2.6-vmlinux-lzma-cas-771.gz" to a safe location.

{{{
ADM Bootloader (v0.04.01 20040216)
===================================
(a) Download vmlinuz to flash ...
(b) Download vmlinuz to sdram (for debug) ...
(c) Update bootloader ...
(e) Exit

Please enter your key : b
}}}

Now send the file mentionned before via Xmodem. This should take some time since the lzma decompressor + kernel + ramdisk is approximately 2Mb.

Once the transfer is done, ADMBOOT will jump to the LZMA decompressor which will uncompress and boot the kernel :

{{{
ADM Bootloader (v0.04.01 20040216)
===================================
(a) Download vmlinuz to flash ...
(b) Download vmlinuz to sdram (for debug) ...
(c) Update bootloader ...
(e) Exit

Please enter your key : b
Downloading......... PASS

decompress kernel image ...
boot linux ...

LZMA loader for ADM5120, Copyright (C) 2007 OpenWrt.org

decompressing kernel... done!
launching kernel...

Linux version 2.6.21.1 (florian@dorelei) (gcc version 4.1.2) #2 Mon Jun 11 22:11:15 CEST 2007
ADM5120 revision 8, running at 175MHz
Boot loader is: Unknown
Booted from   : NOR flash
Board is      : Unknown ADM5120 board
GETENV: envname is memsize
GETENV: returning 0x001000000
CPU revision is: 0001800b
ADM5120 board setup
Determined physical RAM map:
 memory: 00bf8000 @ 00408000 (usable)
Wasting 33024 bytes for tracking 1032 unused pages
Initrd not found or empty - disabling initrd
Built 1 zonelists.  Total pages: 4064
Kernel command line: console=ttyS0,115200 rootfs=jffs2,squashfs,yaffs2 init=/etc/preinit
Primary instruction cache 8kB, physically tagged, 2-way, linesize 16 bytes.
Primary data cache 8kB, 2-way, linesize 16 bytes.
Synthesized TLB refill handler (20 instructions).
Synthesized TLB load handler fastpath (32 instructions).
Synthesized TLB store handler fastpath (32 instructions).
Synthesized TLB modify handler fastpath (31 instructions).
PID hash table entries: 64 (order: 6, 256 bytes)
Using 87.500 MHz high precision timer.
Dentry cache hash table entries: 2048 (order: 1, 8192 bytes)
Inode-cache hash table entries: 1024 (order: 0, 4096 bytes)
Memory: 12108k/12256k available (2286k kernel code, 148k reserved, 354k data, 1372k init, 0k highmem)
Mount-cache hash table entries: 512
NET: Registered protocol family 16
adm5120: system has PCI BIOS
registering PCI controller with io_map_base unset
usbcore: registered new interface driver usbfs
usbcore: registered new interface driver hub
usbcore: registered new device driver usb
PCI: mapping irq for device 0000:00:02.0, slot:2, pin:1, irq:15
PCI: mapping irq for device 0000:00:03.0, slot:3, pin:1, irq:16
PCI: mapping irq for device 0000:00:03.1, slot:3, pin:2, irq:16
PCI: mapping irq for device 0000:00:03.2, slot:3, pin:3, irq:16
Time: MIPS clocksource has been installed.
NET: Registered protocol family 2
IP route cache hash table entries: 1024 (order: 0, 4096 bytes)
TCP established hash table entries: 512 (order: 0, 4096 bytes)
TCP bind hash table entries: 512 (order: -1, 2048 bytes)
TCP: Hash tables configured (established 512 bind 512)
TCP reno registered
squashfs: version 3.0 (2006/03/15) Phillip Lougher
Registering mini_fo version $Id$
JFFS2 version 2.2. (NAND) (SUMMARY)  (C) 2001-2006 Red Hat, Inc.
yaffs Jun 11 2007 20:28:06 Installing.
io scheduler noop registered
io scheduler deadline registered (default)
Registered led device: adm5120:led
ttyS0 at I/O 0x12600000 (irq = 9) is a ADM5120
ttyS1 at I/O 0x12800000 (irq = 10) is a ADM5120
eth0: ADM5120 switch port0
eth1: ADM5120 switch port1
eth2: ADM5120 switch port2
eth3: ADM5120 switch port3
eth4: ADM5120 switch port4
adm5120 : flash init : 0x1fc00000 0x00000000
Failed to ioremap
block2mtd: version $Revision: 1.30 $
RB1xx nand
No NAND device found!!!
No NAND device found!!!
No NAND device found!!!
No NAND device found!!!
RB1xxx nand device not found
nf_conntrack version 0.5.0 (95 buckets, 760 max)
ip_tables: (C) 2000-2006 Netfilter Core Team
TCP vegas registered
NET: Registered protocol family 1
NET: Registered protocol family 17
NET: Registered protocol family 15
Bridge firewalling registered
802.1Q VLAN Support v1.8 Ben Greear <greearb@candelatech.com>
All bugs added by David S. Miller <davem@redhat.com>
Freeing unused kernel memory: 1372k freed
Warning: unable to open an initial console.
Algorithmics/MIPS FPU Emulator v1.5
device eth0 entered promiscuous mode
br-lan: port 1(eth0) entering learning state
br-lan: topology change detected, propagating
br-lan: port 1(eth0) entering forwarding state
PPP generic driver version 2.4.2
wlan: 0.8.4.2 (svn r2420)
ath_hal: module license 'Proprietary' taints kernel.
ath_hal: 0.9.30.13 (AR5210, AR5211, AR5212, AR5416, RF5111, RF5112, RF2413, RF5413, RF2133, REGOPS_FUNC)
ath_rate_minstrel: 1.2 (svn r2420)

Minstrel automatic rate control algorithm.

Look around rate set to 10%
EWMA rolloff level set to 75%
Max Segment size in the mrr set to 6000 us

wlan: mac acl policy registered
ath_pci: 0.9.4.5 (svn r2420)
init started:  BusyBox v1.4.2 (2007-06-11 10:55:54 CEST) multi-call binary

Please press Enter to activate this console.


BusyBox v1.4.2 (2007-06-11 10:55:54 CEST) Built-in shell (ash)
Enter 'help' for a list of built-in commands.

  _______                     ________        __
 |       |.-----.-----.-----.|  |  |  |.----.|  |_
 |   -   ||  _  |  -__|     ||  |  |  ||   _||   _|
 |_______||   __|_____|__|__||________||__|  |____|
          |__| W I R E L E S S   F R E E D O M
 KAMIKAZE (bleeding edge, r7559) -------------------
  * 10 oz Vodka       Shake well with ice and strain
  * 10 oz Triple sec  mixture into 10 shot glasses.
  * 10 oz lime juice  Salute!
 ---------------------------------------------------
root@OpenWrt:/#
}}}
}}}

CategoryModel ["CategoryADM5120Device"]
