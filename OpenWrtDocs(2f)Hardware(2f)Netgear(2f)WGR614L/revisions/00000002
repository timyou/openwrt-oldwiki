CPU is MIPS BCM5354v2 @ 240Mhz, 16 MB of RAM. Looking at the bootlog. The WGR615L identifies itself as WGR614v8.

Serial console pins I used are: 
2 RX

5 TX

6 GND



Boot log from serial console
{{{
Decompressing..........done


WGR614v8 - 1.5 (Fri Jun  6 15:53:24 CST 2008)
et0: Broadcom BCM47xx 10/100 Mbps Ethernet Controller 4.130.30.0
Device eth0:  hwaddr 00-22-3F-13-D0-D6, ipaddr 192.168.1.1, mask 255.255.255.0
        gateway not set, nameserver not set
Loading .........................................
CPU revision is: 00029029
Primary instruction cache 16kb, linesize 16 bytes (4 ways)
Primary data cache 16kb, linesize 16 bytes (2 ways)
Linux version 2.4.20 (lewis@dev) (gcc version 3.2.3 with Broadcom modifications) #390 Fri May 23 18:19:07 CST 2008
Setting the PFC to its default value
Determined physical RAM map:
 memory: 01000000 @ 00000000 (usable)
On node 0 totalpages: 4096
zone(0): 4096 pages.
zone(1): 0 pages.
zone(2): 0 pages.
Kernel command line: root=/dev/mtdblock2 noinitrd console=ttyS0,115200
CPU: BCM5354 rev 2 at 240 MHz
Calibrating delay loop... 237.56 BogoMIPS
Memory: 14468k/16384k available (1363k kernel code, 1916k reserved, 108k data, 60k init, 0k highmem)
Dentry cache hash table entries: 2048 (order: 2, 16384 bytes)
Inode cache hash table entries: 1024 (order: 1, 8192 bytes)
Mount-cache hash table entries: 512 (order: 0, 4096 bytes)
Buffer-cache hash table entries: 1024 (order: 0, 4096 bytes)
Page-cache hash table entries: 4096 (order: 2, 16384 bytes)
Checking for 'wait' instruction...  unavailable.
POSIX conformance testing by UNIFIX
PCI: no core
PCI: Fixing up bus 0
Linux NET4.0 for Linux 2.4
Based upon Swansea University Computer Society NET3.039
Initializing RT netlink socket
Starting kswapd
devfs: v1.12c (20020818) Richard Gooch (rgooch@atnf.csiro.au)
devfs: boot_options: 0x1
Squashfs 2.2-r2 (released 2005/09/08) (C) 2002-2005 Phillip Lougher
Serial driver version 5.05c (2001-07-08) with MANY_PORTS SHARE_IRQ SERIAL_PCI enabled
ttyS00 at 0xb8000300 (irq = 3) is a 16550A
ttyS01 at 0xb8000400 (irq = 0) is a 16550A
PPP generic driver version 2.4.2
pflash: found no supported devices
sflash: squashfs filesystem found at block 621
Creating 8 MTD partitions on "sflash":
0x00000000-0x00020000 : "boot"
0x00020000-0x003b0000 : "linux"
0x0009b7ec-0x003b0000 : "rootfs"
0x003b0000-0x003c0000 : "T_Meter1"
0x003c0000-0x003d0000 : "T_Meter2"
0x003d0000-0x003e0000 : "POT"
0x003e0000-0x003f0000 : "board_data"
0x003f0000-0x00400000 : "nvram"
NET4: Linux TCP/IP 1.0 for NET4.0
IP Protocols: ICMP, UDP, TCP, IGMP
IP: routing cache hash table of 512 buckets, 4Kbytes
TCP: Hash tables configured (established 1024 bind 2048)
Linux IP multicast router 0.06 plus PIM-SM
NET4: Unix domain sockets 1.0/SMP for Linux NET4.0.
NET4: Ethernet Bridge 008 for NET4.0
802.1Q VLAN Support v1.7 Ben Greear <greearb@candelatech.com>
All bugs added by David S. Miller <davem@redhat.com>
VFS: Mounted root (squashfs filesystem) readonly.
Mounted devfs on /dev
Freeing unused kernel memory: 60k freed
Algorithmics/MIPS FPU Emulator v1.5
Reading board data...
WSC UUID: 0x34351d57c7238c42332f05f7d9f32ffa
pa0maxpwr - 82
pa0b0 - 0x164B
pa0b1 - 0xFA66
pa0b2 - 0xFE86
opo - 8
configure RF parameters OK
Using /lib/modules/2.4.20/kernel/drivers/net/et/et.o
insmod: bcm57xx.o: no module by that name found
Using /lib/modules/2.4.20/kernel/drivers/net/wl/wl.o
Hit enter to continue...WARNING: console log level set to 1
eth1: ignore i/f due to error(s)
*********************************************
Wi-Fi Simple Config Application - Intel Corp.
Version: Build 1.0.5, November 19 2006
*********************************************
Initializing stack...button monitor start...!
apLockDownLog_init, counttion = 300, duration = 300!
 OK
Now starting stack
get mac = 00 22 3F 13 D0 D6 
Reading board data...
WSC UUID: 0x34351d57c7238c42332f05f7d9f32ffa
Using /lib/modules/2.4.20/kernel/net/ipv4/acos_nat/acos_nat.o
info, udhcp server (v0.9.8) started
error, unable to parse 'option wins '
error, unable to parse 'option domain '
Info: No FWPT default policies.
POT integrity check OK.
wl: Unsupported
Start DHCP client daemon
info, udhcp client (v0.9.8) started
DEVICE PIN: *hidden*
Hit enter to continue...
******* MODE: Access Point *******

DEVICE PIN: *hidden*
WSC: In unconfiged AP mode, wait for start command....
tlvPtrChar* : func CMasterControl_InitiateRegistration  line 658 allocating memory 0x10003750 for 0x10003738
eth0: No such process

}}}
