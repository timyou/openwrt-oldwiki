'''Buffalo WHR-G54S'''

----
 . The device is supported in OpenWrt 1.0 (White Russian) and later.  You need to install the openwrt-brcm-2.4-<type>.trx firmware images using the TFTP method only! This is because the installed Buffalo Firmware loader may require or perform some kind of decryption and expects a filename with a .ENC extension instead of the standard .bin or .trx. 

If you have a newer hardware revision (this being written on 8/21/2006), you should use the current SVN, as there are some bricking issues on older builds of OpenWrt.
There is also different hardware versions with almost same serial.(Also on old one) So DO NOT copy nvram from router to another or you can get brick because of memory settings. 

This device is based on the Broadcom chipset so the openwrt-brcm-<type>.trx image is required. Pull the power plug, press and hold the reset ("INIT") button, start the TFTP, plug the power back in, and let go of the button. The power light does *not* flash on this unit, but the diag does. This unit keeps the IP address that it was set to while in this mode. Factory setting is 192.168.11.1.

TFTP commands:

{{{
tftp 192.168.11.1
tftp> binary
tftp> trace
tftp> rexmt 1
tftp> timeout 60
tftp> put openwrt-xxx-x.x-xxx.trx
}}}

 <!> Note:

 You have to enter the 'put' command fairly quickly after plugging the power back in. Just after most of the network indicator LEDs have gone off (i.e. only the ports with cables connected should have LEDs on) would be perfect. If you get something like

 {{{
 sent WRQ <file=openwrt-brcm-2.4-squashfs.trx, mode=octet>
 sent WRQ <file=openwrt-brcm-2.4-squashfs.trx, mode=octet>
 sent WRQ <file=openwrt-brcm-2.4-squashfs.trx, mode=octet>
 sent WRQ <file=openwrt-brcm-2.4-squashfs.trx, mode=octet>
 sent WRQ <file=openwrt-brcm-2.4-squashfs.trx, mode=octet>
 sent WRQ <file=openwrt-brcm-2.4-squashfs.trx, mode=octet>
 ...
 Transfer timed out.
 }}}

 you were probably not quick enough. In that case, just try again.

After this, wait for the device to reboot and you should be set. You should be able to telnet to 192.168.11.1 or whatever the unit was set to prior to the installation.

----

this is for devices starting with serial 3407:

----
{{{
Bootloader: CFE 
System-On-Chip:  Broadcom 5352
CPU Speed: 200 Mhz
Flash size: 4 MB
RAM: 16 MB
Wireless: integrated Broadcom BCM4306 802.11b/g Wireless LAN Controller
Ethernet: ?
Serial: yes
JTAG: yes

--------------> output from dmesg <---------------

Setting the PFC value as 0x15
Determined physical RAM map:
 memory: 01000000 @ 00000000 (usable)
On node 0 totalpages: 4096
zone(0): 4096 pages.
zone(1): 0 pages.
zone(2): 0 pages.
Kernel command line: root=/dev/mtdblock2 rootfstype=squashfs,jffs2 init=/etc/pre
init noinitrd console=ttyS0,115200
CPU: BCM5352 rev 0 at 200 MHz
Using 100.000 MHz high precision timer.
Calibrating delay loop... 199.47 BogoMIPS
Memory: 14268k/16384k available (1412k kernel code, 2116k reserved, 100k data, 8
0k init, 0k highmem)
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
devfs: v1.12c (20020818) Richard Gooch (rgooch@atnf.csiro.au)
devfs: boot_options: 0x1
JFFS2 version 2.1. (C) 2001 Red Hat, Inc., designed by Axis Communications AB.
Squashfs 2.1-r2 (released 2004/12/15) (C) 2002-2004 Phillip Lougher
pty: 256 Unix98 ptys configured
Serial driver version 5.05c (2001-07-08) with MANY_PORTS SHARE_IRQ SERIAL_PCI en
abled
ttyS00 at 0xb8000300 (irq = 3) is a 16550A
ttyS01 at 0xb8000400 (irq = 0) is a 16550A
b44.c:v0.93 (Mar, 2004)
PCI: Setting latency timer of device 00:01.0 to 64
eth0: Broadcom 47xx 10/100BaseT Ethernet 00:0d:0b:e8:a9:1e
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
Creating 4 MTD partitions on "Physically mapped flash":
0x00000000-0x00040000 : "pmon"
0x00040000-0x003f0000 : "linux"
0x000c0000-0x003f0000 : "rootfs"
0x003f0000-0x00400000 : "nvram"
Initializing Cryptographic API
NET4: Linux TCP/IP 1.0 for NET4.0
IP Protocols: ICMP, UDP, TCP, IGMP
IP: routing cache hash table of 512 buckets, 4Kbytes
TCP: Hash tables configured (established 1024 bind 2048)
ip_conntrack version 2.1 (5953 buckets, 5953 max) - 328 bytes per conntrack
ip_tables: (C) 2000-2002 Netfilter core team
NET4: Unix domain sockets 1.0/SMP for Linux NET4.0.
NET4: Ethernet Bridge 008 for NET4.0
802.1Q VLAN Support v1.8 Ben Greear <greearb@candelatech.com>
All bugs added by David S. Miller <davem@redhat.com>
VFS: Mounted root (jffs2 filesystem) readonly.
Mounted devfs on /dev
Freeing unused kernel memory: 80k freed
Algorithmics/MIPS FPU Emulator v1.5
diag boardtype: 00000467
Probing device eth0: found!
b44: eth0: Link is up at 100 Mbps, full duplex.
b44: eth0: Flow control is off for TX and off for RX.
jffs2.bbc: SIZE compression mode activated.
PCI: Setting latency timer of device 00:05.0 to 64
eth1: Broadcom BCM4318 802.11 Wireless Controller 3.90.37.0
Universal TUN/TAP device driver 1.5 (C)1999-2002 Maxim Krasnyansky
BFL_ENETADM not set in boardflags. Use force=1 to ignore.
device eth0 entered promiscuous mode
vlan0: add 01:00:5e:00:00:01 mcast address to master interface
vlan0: dev_set_promiscuity(master, 1)
vlan0: dev_set_allmulti(master, 1)

}}}

The {{{boot_wait}}} NVRAM variable is '''on''' by default. Resetting to factory defaults via reset button or {{{mtd erase nvram}}} is '''not safe''' on this unit.

-----

this is for devices with serials starting 7407 (you can ONLY run a current SVN version on these devices. See notes above.):

----
{{{
CFE version 1.0.37-1.07 for BCM947XX (32bit,SP,LE)
Build Date: 2005\uffff\uffff 10\uffff\uffff 17\uffff\uffff \uffff\uffff\uffff\uffff\uffff\uffff 04:38:11 JST (root@ifedora)
Copyright (C) 2000,2001,2002,2003 Broadcom Corporation.

Initializing Arena
Initializing Devices.
* cmdset: AMD Standard
* Insaner_1 = (0xa8)
* flashutl_cmd: type (0004), read_id (0090)
 -> vendid (00C2), devid (22A8), devid2 (0000)
* flashutl_cmd: type (0003), read_id (0090)
 -> vendid (00C2), devid (22A8), devid2 (0000)
* flashutl_cmd: type (0002), read_id (0090)
 -> vendid (00C2), devid (22A8), devid2 (0000)
* Flash Info. -> manufacturer (00), device (FF)
* Flash Info. -> manufacturer2 (0000), device2 (0000)
* Insaner_2 = (0xa8)
* cmdset: AMD Standard
* Insaner_1 = (0xa8)
* flashutl_cmd: type (0004), read_id (0090)
 -> vendid (00C2), devid (22A8), devid2 (0000)
* flashutl_cmd: type (0003), read_id (0090)
 -> vendid (00C2), devid (22A8), devid2 (0000)
* flashutl_cmd: type (0002), read_id (0090)
 -> vendid (00C2), devid (22A8), devid2 (0000)
* Flash Info. -> manufacturer (00), device (FF)
* Flash Info. -> manufacturer2 (0000), device2 (0000)
* Insaner_2 = (0xa8)
* cmdset: AMD Standard
* Insaner_1 = (0xa8)
* flashutl_cmd: type (0004), read_id (0090)
 -> vendid (00C2), devid (22A8), devid2 (0000)
* flashutl_cmd: type (0003), read_id (0090)
 -> vendid (00C2), devid (22A8), devid2 (0000)
* flashutl_cmd: type (0002), read_id (0090)
 -> vendid (00C2), devid (22A8), devid2 (0000)
* Flash Info. -> manufacturer (00), device (FF)
* Flash Info. -> manufacturer2 (0000), device2 (0000)
* Insaner_2 = (0xa8)
et0: Broadcom BCM47xx 10/100 Mbps Ethernet Controller 3.90.39.0
* memc_config: (00048000)
CPU type 0x29008: 200MHz
Total memory: 16384 KBytes

Total memory used by CFE:  0x80400000 - 0x804A29A0 (666016)
Initialized Data:          0x80438650 - 0x8043B1F0 (11168)
BSS Area:                  0x8043B1F0 - 0x8043C9A0 (6064)
Local Heap:                0x8043C9A0 - 0x804A09A0 (409600)
Stack Area:                0x804A09A0 - 0x804A29A0 (8192)
Text (code) segment:       0x80400000 - 0x80438650 (230992)
Boot area (physical):      0x004A3000 - 0x004E3000
Relocation Factor:         I:00000000 - D:00000000

Device eth0:  hwaddr 00-16-01-11-45-00, ipaddr 192.168.11.1, mask 255.255.255.0
        gateway not set, nameserver not set
Wait a few seconds for an image
Reading :: Failed.: Timeout occured
>>> boot -raw -z -addr=0x80001000 -max=0x3a0000 flash0.os:
Loader:raw Filesys:raw Dev:flash0.os File: Options:(null)
Loading: ...... 1732608 bytes read
Entry at 0x80001000
Closing network.
Starting program at 0x80001000
CPU revision is: 00029008
Primary instruction cache 16kb, linesize 16 bytes (2 ways)
Primary data cache 8kb, linesize 16 bytes (2 ways)
Linux version 2.4.20 (root@localhost.localdomain) (gcc version 3.3.3) #4 2005\uffff\uffff\uffff 8\uffff\uffff\uffff 11\uffff\uffff\uffff \uffff\uffff\uffff\uffff\uffff\uffff\uffff\uffff\uffff 21:50:46 JST
Setting the PFC to its default value
Determined physical RAM map:
 memory: 01000000 @ 00000000 (usable)
On node 0 totalpages: 4096
zone(0): 4096 pages.
zone(1): 0 pages.
zone(2): 0 pages.
Kernel command line: root=/dev/mtdblock2 noinitrd console=ttyS0,115200
CPU: BCM5352 rev 0 at 200 MHz
Calibrating delay loop... 199.47 BogoMIPS
Memory: 14148k/16384k available (1507k kernel code, 2236k reserved, 104k data, 64k init, 0k highmem)
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
mel_initsw: GPIO initialize done..
BUFFALO SWICH&LED DRIVER ver 1.00
Serial driver version 5.05c (2001-07-08) with MANY_PORTS SHARE_IRQ SERIAL_PCI enabled
ttyS00 at 0xb8000300 (irq = 3) is a 16550A
ttyS01 at 0xb8000400 (irq = 0) is a 16550A
HDLC line discipline: version $Revision$, maxframe=4096
N_HDLC line discipline registered.
PPP generic driver version 2.4.2
PPP Deflate Compression module registered
PPP BSD Compression module registered
 Amd/Fujitsu Extended Query Table v1.1 at 0x0040
number of CFI chips: 1
Flash device: 0x400000 at 0x1c000000
Physically mapped flash: cramfs filesystem found at block 1024
Creating 4 MTD partitions on "Physically mapped flash":
0x00000000-0x00040000 : "boot"
0x00040000-0x003e0000 : "linux"
0x00100000-0x003e0000 : "rootfs"
0x003e0000-0x00400000 : "nvram"
sflash: found no supported devices
NET4: Linux TCP/IP 1.0 for NET4.0
IP Protocols: ICMP, UDP, TCP
IP: routing cache hash table of 512 buckets, 4Kbytes
TCP: Hash tables configured (established 1024 bind 2048)
ip_conntrack version 2.1 (128 buckets, 1024 max) - 344 bytes per conntrack
ip_tables: (C) 2000-2002 Netfilter core team
*** #define HZ is (100).
ipt_time loading
NET4: Unix domain sockets 1.0/SMP for Linux NET4.0.
NET4: Ethernet Bridge 008 for NET4.0
802.1Q VLAN Support v1.7 Ben Greear <greearb@candelatech.com>
All bugs added by David S. Miller <davem@redhat.com>
VFS: Mounted root (cramfs filesystem) readonly.
Mounted devfs on /dev
Freeing unused kernel memory: 64k freed
init started:  BusyBox v1.00 (2005.08.11-13:00+0000) multi-call binary
Algorithmics/MIPS FPU Emulator v1.5
mount: Mounting none on / failed: Permission denied
MidLayer.c(1878) ML_Initialize :***** Please push init button if you want to init_reboot ******
insmod: /lib/modules/2.4.20: No such file or directory
Using /lib/modules/kernel/drivers/net/et/et.o
Warning: loading et will taint the kernel: no license
  See http://www.tux.org/lkml/#export-tainted for information about tainted modules
eth0: Broadcom BCM47xx 10/100 Mbps Ethernet Controller 3.130.1.10

Please press Enter to activate this console. create procpoint for station information eth%d
eth1: Broadcom BCM4318 802.11 Wireless Controller 3.130.1.10
et0: link up (interface up)
register_vlan_device: ALREADY had VLAN registered
register_vlan_device: ALREADY had VLAN registered
Performing WLC_COMMIT
wlc_set_rate_override:35629: band 11a
wl0: Channel Select: 10



BusyBox v1.00 (2005.08.11-13:00+0000) Built-in shell (msh)
Enter 'help' for a list of built-in commands.

# ls
bin   dev   etc   lib   mnt   proc  tmp   usr   var   www
# * VPN Masqurade -- IPsec Support
reg isakmp:done
reg ESP protocol:
reg ESP conntrack:done
ip_nat_ipsec : isakmp : done.
ip_nat_ipsec : esp    : done.
}}}
----
CategoryModel CategoryModel
