= Motorola PowerLine MU Gateway =

The [http://www.motorola.com/Business/US-EN/Product+Lines/MOTOwi4/Powerline+MU+Gateway_US-EN Powerline MU gateway] is a 5-LAN ports, Coax, 3-phase PLC gateway.

{{{
SoC: ADM5120 @175Mhz
RAM: 32MB
Flash: 8MB
PLC PHY : Intellon INT5500
Serial : yes
USB : no
JTAG : maybe
Wi-Fi: no
}}}

== Serial pinout ==

Serial console is available on header JP1 which is a 2x7 pin header :

{{{
CPU

(x) (x) (x) (x) (x) (x) (x) (x)
(x) (x) (x) (x) (x) (x) (x) (x)
VCC TX  RX  GND

LEDs
}}}

== Bootlog ==

Stock firmware is a Linux-2.4 based kernel :

{{{
ADM5120 Boot:


Copyright 2004-2006  Motorola, Inc.
CPU: ADM5120-175MHz
SDRAM: 32MB
Flash: NOR-8M
Boot System: Linux-5120
Loader Version: V1.06
Creation Date: 2006.10.12
0
Booting Linux...
Kernel decompress ... PASS
LINUX/5120 started...
CPU revision is: 0001800b
Primary instruction cache 8kB, physically tagged, 2-way, linesize 16 bytes.
Primary data cache 8kB 2-way, linesize 16 bytes.
Linux version 2.4.20_mvl31-ADM5120 (root@Linux-Server) (gcc version 2.96 20000731 (Red Hat Linux 7.3 2.96-110.1)) #843 Fri Mar 9 11:04:46 HKT 2007
Can't analyze prologue code at 800214c0
am5120_setup() starts.
System no PCI BIOS
Determined physical RAM map:
 memory: 00d42000 @ 002be000 (usable)
Initial ramdisk at: 0x80161000 (1286144 bytes)
On node 0 totalpages: 4096
zone(0): 4096 pages.
zone(1): 0 pages.
zone(2): 0 pages.
Kernel command line: root=/dev/ram0 console=ttyS0
CPU clock: 175MHz
Calibrating delay loop... 174.48 BogoMIPS
MIPS CPU counter frequency is fixed at 87500000 Hz
Memory: 13388k/13576k available (1247k kernel code, 188k reserved, 1340k data, 52k init, 0k highmem)
Dentry cache hash table entries: 2048 (order: 2, 16384 bytes)
Inode cache hash table entries: 1024 (order: 1, 8192 bytes)
Mount-cache hash table entries: 512 (order: 0, 4096 bytes)
Buffer-cache hash table entries: 1024 (order: 0, 4096 bytes)
Page-cache hash table entries: 4096 (order: 2, 16384 bytes)
Checking for 'wait' instruction...  available.
POSIX conformance testing by UNIFIX
Linux NET4.0 for Linux 2.4
Based upon Swansea University Computer Society NET3.039
Initializing RT netlink socket
LSP Revision 1
Starting kswapd
Disabling the Out Of Memory Killer
pty: 256 Unix98 ptys configured
RAMDISK driver initialized: 16 RAM disks of 8024K size 1024 blocksize
loop: loaded (max 8 devices)
PPP generic driver version 2.4.2
PPP Deflate Compression module registered
PPP BSD Compression module registered
NET4: Linux TCP/IP 1.0 for NET4.0
IP Protocols: ICMP, UDP, TCP
IP: routing cache hash table of 512 buckets, 4Kbytes
TCP: Hash tables configured (established 1024 bind 2048)
NET4: Unix domain sockets 1.0/SMP for Linux NET4.0.
NET4: Ethernet Bridge 008 for NET4.0
802.1Q VLAN Support v1.7 Ben Greear <greearb@candelatech.com>
All bugs added by David S. Miller <davem@redhat.com>
AM5120 NOR flash device: 400000 at 1fc00000
 Amd/Fujitsu Extended Query Table v1.3 at 0x0040
number of CFI chips: 1
cfi_cmdset_0002: Disabling fast programming due to code brokenness.
Creating 2 MTD partitions on "AM5120 NOR flash device":
0x00010000-0x00020000 : "BoardCfg"
0x00020000-0x00200000 : "Kernel Image"
AM5120 NOR flash device initialized
RAMDISK: Compressed image found at block 0
Freeing initrd memory: 1256k freed
EXT2-fs warning: maximal mount count reached, running e2fsck is recommended
VFS: Mounted root (ext2 filesystem).
Freeing prom memory: 0kb freed
Freeing unused kernel memory: 52k freed
Algorithmics/MIPS FPU Emulator v1.5
Starting RAWACCESS device driver...
Using /lib/modules/ifx_raw_acs
(raw_acs)Init raw_acs successfully!
buf size is 4 and block is 10000.
rawdev opened!
Read 8110 bytes from flash
6654 bytes...Uncompressed to...18612 bytes
Write 129 bytes to /nv/chap-secrets
Write 4604 bytes to /nv/pppoe.conf
Write 3173 bytes to /nv/rc.conf
Write 260 bytes to /nv/options.pptp
Write 446 bytes to /nv/pptp
Write 1882 bytes to /nv/rc.firewall
Write 4120 bytes to /nv/rc.iptables
Write 106 bytes to /nv/pap-secrets
Write 429 bytes to /nv/ripd.conf
Write 3463 bytes to /nv/udhcpd.conf
Read data completely!
Thu Jan  1 00:00:02 1970 <3> ulogd.c:300 registering interpreter `raw'
Thu Jan  1 00:00:02 1970 <3> ulogd.c:300 registering interpreter `oob'
Thu Jan  1 00:00:02 1970 <3> ulogd.c:300 registering interpreter `ip'
Thu Jan  1 00:00:02 1970 <3> ulogd.c:300 registering interpreter `tcp'
Thu Jan  1 00:00:02 1970 <3> ulogd.c:300 registering interpreter `icmp'
Thu Jan  1 00:00:02 1970 <3> ulogd.c:300 registering interpreter `udp'
Thu Jan  1 00:00:02 1970 <3> ulogd.c:300 registering interpreter `ahesp'
Thu Jan  1 00:00:02 1970 <5> ulogd.c:355 registering output `syslogemu'
Using /lib/modules/rtcdriver.o
Warning: loading rtcdriver will taint the kernel: no license
  See http://www.tux.org/lkml/#export-tainted for information about tainted modules
init is ok!
get the value 0x7e06
Value is equal to 0x7e06
cmd 4000 ,result=0x7e06.
get the value 0x3f3f00
Value is equal to 0x3f3f00
cmd 4000 ,result=0x3f3f00.
reset swith configuration
Starting config VLAN.....
<6>adm0.0: dev_set_promiscuity(master, 1)
device adm0 entered promiscuous mode
device adm0.0 entered promiscuous mode
device adm1 entered promiscuous mode
device adm2 entered promiscuous mode
br0: port 3(adm2) entering learning state
br0: port 2(adm1) entering learning state
br0: port 1(adm0.0) entering learning state
get the value 0x7e06
Value is equal to 0x7e06
cmd 4000 ,result=0x7e06.
get the value 0x3f3f00
Value is equal to 0x3f3f00
cmd 4000 ,result=0x3f3f00.
reset swith configuration
Setting Hostname: Gateway.Motorola
Starting HTTP Server ....
--Starting system in switch mode (rc.network_switch)....
Initialize device table successfully!
Start PLC Server
Start Reset Deamon
start FTP server
Starting SNMP Agent ....
+----------------------------------------------------+
| Welcome to Motorola MU Gateway Command Line System |
+----------------------------------------------------+
Gateway.Motorola login: Tue Nov 30 00:00:00 UTC 1999
cat: null: No such file or directory
Get Spectral from device UNCW-JUOY-KWXV-QLSA with interface adm0
Get response for Spectral

80 80 80 80 00 00 80 80 80 80 80 80 80 00 00 80
80 80 80 80 80 80 80 80 80 80 80 80 80 00 80 80
80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80
80 00 00 00 80 80 80 80 80 80 80 80 80 80 80 80
80 80 80 80 80 00 00 80 80 80 80 80 80 80 80 80
80 80 80 80

Gateway.Motorola login:
}}}


== Firmware analysis ==

The device firmware can be found on Motorola's website under the format of Java serialized objects, which should be loaded as packages using Canopy Network Updater Tool.

The bootloader looks like a modified ADMBoot loader, and includes a configurable tftp client to load images. It accepts gzip'd images, similarly to what ADMBoot accepts.
