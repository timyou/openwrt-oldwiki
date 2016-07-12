= PCi MZK-W04N =

{{{
CPU : Ralink RT1310A
SDRAM : 32MB
Flash : 4MB
Wi-Fi : Ralink RT2860RT
Switch : Realtek RTL8305SC
}}}

== JTAG pinout ==

The pinout is silk screened on the PCB here it is :

{{{
LED

TDI [x]                 SoC
RTCK [x] [x] TCK
TDO [x] [x] NTRST
}}}

== Serial pinout ==

{{{
Switch

[x] TX
[x] GND
[x] RX
[x] VCC
}}}

== Bootlog ==

{{{
U-Boot 1.1.3 (May 18 2007 - 10:07:28)

U-Boot code: 40780000 -> 4079AB24  BSS: -> 407B0000
System Memory Map:
0x00000000-0x01FFFFFF: SDRAM Bank 0
0x19C00000-0x1E7FFFFF: Memory Mapped IO Space-AHB
        0x19C00000-0x19C1FFFF: Static/SDRAM Memory Controller
        0x19C40000-0x19C5FFFF: Interrupt Controller
        0x19C60000-0x19C7FFFF: AHB Arbiter
        0x19C80000-0x19C9FFFF: MAC 0
        0x19CA0000-0x19CBFFFF: MA1 0
        0x1E700000-0x1E71FFFF: HDMA
0x1E800000-0x1EFFFFFF: Memory Mapped IO Space-APB
        0x1E800000-0x1E81FFFF: Timer 0/1/2/3
        0x1E840000-0x1E85FFFF: UART 0
        0x1E880000-0x1E89FFFF: SPI
        0x1E8A0000-0x1E8BFFFF: GPIO 0
        0x1E8C0000-0x1E8DFFFF: WDT
        0x1E8E0000-0x1E8FFFFF: SCU
        0x1E940000-0x1E95FFFF: ACI0(PL040)
        0x1E960000-0x1E97FFFF: ACI1(PL040)
0x1F000000-0x1F7FFFFF: Flash Bank 0
0x40000000-0x41FFFFFF: SDRAM Bank 1
RAM Configuration:
Bank #0: 40000000 16 MB
Board: 5V-ATA REV.A(CPU Speed 297 MHz)
       MXIC-MX29LV320CB = 4MB;   start at 0x1F000000;
Flash:  4 MB
*** Warning - bad CRC, using default environment

In:    serial
Out:   serial
Err:   serial
Hit any key to stop autoboot:  0
****************Kernel CheckSume**************
Checksum ok!

## Booting image at 1f020014 ...
   Image Name:   Linux-2.6.17
   Image Type:   ARM Linux Kernel Image (bzip2 compressed)
   Data Size:    866133 Bytes = 845.8 kB
   Load Address: 40008000
   Entry Point:  40008000
   Verifying Checksum ... OK
   Uncompressing Kernel Image dst len 600000  1f020054 d3755
................................... OK

Starting kernel @40008000...

Linux version 2.6.17 (root@localhost.localdomain) (gcc version 4.1.1) #1682 Tue Dec 4 09:27:04 CST 2007
CPU: ARM926EJ-Sid(wb) [41069265] revision 5 (ARMv5TEJ)
Machine: 5VT13XX
Ignoring unrecognised tag 0x00000000
Memory policy: ECC disabled, Data cache writeback
CPU0: D VIVT write-back cache
CPU0: I cache: 16384 bytes, associativity 4, 32 byte lines, 128 sets
CPU0: D cache: 16384 bytes, associativity 4, 32 byte lines, 128 sets
Built 1 zonelists
Kernel command line: root=/dev/mtdblock3 ro cpufreq=300M rootfstype=squashfs mem=32M console=ttyS0,38400 mtdparts=5VT13XX_mapped_flash:4M@0x0(U-Boot)ro,0x3a0000@0x20000(Upgrade),0x100000@0x20000(Kie
PID hash table entries: 256 (order: 8, 1024 bytes)
Timer1 load register: 743423(0x000B57FF)
Dentry cache hash table entries: 4096 (order: 2, 16384 bytes)
Inode-cache hash table entries: 2048 (order: 1, 8192 bytes)
Memory: 32MB = 32MB total
Memory: 30336KB available (1568K code, 305K data, 76K init)
Mount-cache hash table entries: 512
CPU: Testing write buffer coherency: ok
NET: Registered protocol family 16
PCI: Scanning bus...
PCI: FV Host Bridge - header fixup
PCI: bus0: Fast back to back transfers disabled
NET: Registered protocol family 2
IP route cache hash table entries: 256 (order: -2, 1024 bytes)
TCP established hash table entries: 1024 (order: 0, 4096 bytes)
TCP bind hash table entries: 512 (order: -1, 2048 bytes)
TCP: Hash tables configured (established 1024 bind 512)
TCP reno registered
NetWinder Floating Point Emulator V0.97 (double precision)
squashfs: version 3.0 (2006/03/15) Phillip Lougher
Initializing Cryptographic API
io scheduler noop registered
io scheduler deadline registered (default)
PCI: FV Host Bridge - final fixup
HDLC line discipline: version $Revision: 4.8 $, maxframe=4096
N_HDLC line discipline registered.
LED & GPIO & LAN Status Driver LED_VERSION
Serial: 8250/16550 driver $Revision: 1.90 $ 2 ports, IRQ sharing disabled
serial8250: ttyS0 at MMIO 0x1e840000 (irq = 1) is a 16550A
serial8250: ttyS1 at MMIO 0x1e860000 (irq = 2) is a 16550A
loop: loaded (max 8 devices)
PPP generic driver version 2.4.2
PPP Deflate Compression module registered
PPP BSD Compression module registered
PPP MPPE Compression module registered
NET: Registered protocol family 24
physmap flash device: 800000 at 1f000000
5VT13XX_mapped_flash: Found 1 x16 devices at 0x0 in 8-bit bank
 Amd/Fujitsu Extended Query Table at 0x0040
number of CFI chips: 1
cfi_cmdset_0002: Disabling erase-suspend-program due to code brokenness.
5 cmdlinepart partitions found on MTD device 5VT13XX_mapped_flash
Creating 5 MTD partitions on "5VT13XX_mapped_flash":
0x00000000-0x00400000 : "U-Boot"
0x00020000-0x003c0000 : "Upgrade"
0x00020000-0x00120000 : "Kimage"
0x00120000-0x003c0000 : "Rimage"
0x003c0000-0x00400000 : "Cimage"
u32 classifier
    Perfomance counters on
    input device check on
ip_conntrack version 2.4 (256 buckets, 2048 max) - 244 bytes per conntrack
ip_tables: (C) 2000-2006 Netfilter Core Team
ipt_recent v0.3.1: Stephen Frost <sfrost@snowman.net>.  http://snowman.net/projects/ipt_recent/
ClusterIP Version 0.8 loaded successfully
arp_tables: (C) 2002 David S. Miller
TCP bic registered
NET: Registered protocol family 1
NET: Registered protocol family 17
VFS: Mounted root (squashfs filesystem) readonly.
Freeing init memory: 76K
Sat Jan  1 00:00:00 UTC 2000
Using /lib/modules/2.6.17.3-gcc-4.1-FV13XX.299/fvt13xx/fvmac.ko
fvmac: module license '5VT' taints kernel.
FVMAC version: 1.11, date: 2007/08/07 (compiled at 19:54:06, Nov 12 2007)
FVMAC 0: FVMAC core w/AMBA at 0xf0080000 IRQ 7
FVMAC 0: registered_netdev() as eth1.
FVMAC 1: FVMAC core w/AMBA at 0xf00a0000 IRQ 8
FVMAC 1: registered_netdev() as eth0.
eth0: set media mode 100M/full-duplex
eth1: set media mode 10M/half-duplex
killall: pptp.sh: no process killed
killall: pppoe.sh: no process killed
Initialize WLAN interface
****************Use External RADIUS******************
Using /bin/rt2860ap.ko
PCI: enabling device 0000:00:01.0 (0140 -> 0142)


=== pAd = c3081000, size = 419424 ===

<-- RTMPAllocAdapterBlock, Status=0
PCI: Setting latency timer of device 0000:00:01.0 to 64
RX DESC ffc1a000  size = 2048
<-- RTMPAllocDMAMemory, Status=0
1. Phy Mode = 9
2. Phy Mode = 9
3. Phy Mode = 9
MCS Set = ff ff 00 00 01
Main bssid = 00:90:cc:f5:17:c8
The UUID Hex string is:67dc1d80bfde11d38e7a0090ccf517c8
The UUID ASCII string is:67dc1d80-bfde-11d3-8e7a-0090ccf517c8!
<==== RTMPInitialize, Status=0
0x1300 = 00064330
Setup BRIDGE interface
SIOCGIFFLAGS: No such device
SIOCGIFFLAGS: No such device
SIOCGIFFLAGS: No such device
SIOCGIFFLAGS: No such device
SIOCGIFFLAGS: No such device
bridge br0 doesn't exist; can't delete it
Setup bridge...
device eth0 entered promiscuous mode
eth0: set media mode 100M/full-duplex
SIOCDELRT: No such process
device ra0 entered promiscuous mode
SIOCDELRT: No such process
br0: port 2(ra0) entering learning state
br0: port 1(eth0) entering learning state
br0: topology change detected, propagating
br0: port 2(ra0) entering forwarding state
br0: topology change detected, propagating
br0: port 1(eth0) entering forwarding state
SIOCDELRT: No such process
SIOCDELRT: No such process
------> 802.1x--------->Enter
------> 802.1x------>Exit
Static DHCP Leases disable!
SIOCDELRT: No such process
udhcpd (v0.9.9-pre) started
max_leases value (254) not sane, setting to 31 instead
Setup WAN interface
********** run Diagd **********
********** run GaTest **********
=================Enable WSC_UPNP===================
don't create flash.inc
don't create flash.inc
=================Enable WSC_UPNP===================
killall: snmpd: no process killed
udhcp client (v0.9.9-pre) started
into eth1.deconfig
=================Enable LLTD===================
=================END LLTD===================
gPassiveMsgQ Init success! gPassiveMsgID=0x386d438f!
gActiveMsgQ Init success!
sock=5!(0x0xbe90dd50)
Pthread(wscDevNLHandle)Now waiting for the netlink socket incoming message!
Create netlink socket thread success!
Create ioctl socket(6) success!
UPnP Initialized
         IP-Addr: 192.168.2.1 Port: 49152
         HW-Addr: 00:90:cc:f5:17:c8!



         Please enter your Name and Password



 User Name   :Advertisement Sent

}}}

== GPL sourcecode ==

It seems like the Edimax BR6504N is using the same chip. Sourcecode for it can be found here : http://www.edimax.com/images/Image/OpenSourceCode/Wireless/Router/BR-6504n/BR-6504n_GPL.zip

Here is the list of the sofware inside :

{{{
bridge-utils 0.96
bpalogin-2.0.2
busybox-1.1.0
clockspeed-0.62
dhid-5.1
dnrd-2.10
ez-ipupdate-3.0.10
gmp-4.1.2
iproute2-2.6.16-060323
iptables-1.3.5
iputils-021024
libpcap-0.7.2
ppp-2.4.2
pptp-1.31
rp-l2tp-0.3
rp-pppoe-3.5
udhcp-0.9.9-pre
libupnp-1.21
linuxigd-0.92
wireless_tools.28
uboot-1.13
uclibc-0.9.28
gcc 4.1.1
linux-2.6.17
}}}

The linux directory contains the sources for an ARM 926EJS
