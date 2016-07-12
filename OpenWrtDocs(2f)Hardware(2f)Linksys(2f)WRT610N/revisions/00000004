## Please add only OpenWrt and WRT610N related things to this page! Thanks.
'''Linksys WRT610N'''

'''Identification by S/N'''

Useful for identifying shrinkwrapped units. The '''S/N''' can be found on the box, left of the UPC and EAN barcodes.
||||<style="text-align: center;"> (!) '''Please contribute to this list.''' (!) ||
||||<style="text-align: center;">'''Model''' ||<style="text-align: center;"> '''S/N''' ||
||||<style="text-align: center;">WRT610N v1.0 ||<style="text-align: center;"> CTG01 ||


'''WRT610N v1.0'''

The WRT610N v1.0 is based on the Broadcom 4705 cpu running at 300MHz. It has 8 MB flash and 64 MB SDRAM (2x HY5DU561622FTP). The wireless NICs are a dual BCM4322 Chipset, one for 5GHz A and N and one for 2.4GHz B,G and N.  The switch is a BCM53115 chip. The WRT610N runs 802.11 A, B, G, and Draft N wireless protocols. It provides 4 gigabit LAN ports, 1 WAN port and a USB 2.0 'storage link' port.

Linksys source code is available at ftp://ftp.linksys.com/opensourcecode/wrt610n/

'''Original Firmware Boot Log'''

{{{
CFE version 1.0.37 for BCM947XX (32bit,SP,LE)
Build Date: Mon May 12 15:37:48 CST 2008 (ljh@team2-complier)
Copyright (C) 2000,2001,2002,2003 Broadcom Corporation.

Initializing Arena
Initializing PCI. [normal]
PCI bus 0 slot 0/0: vendor 0x14e4 product 0x0800 (flash memory, rev 0x02)
PCI bus 0 slot 1/0: vendor 0x14e4 product 0x471f (ethernet network, rev 0x02)
PCI bus 0 slot 2/0: vendor 0x14e4 product 0x471a (USB serial bus, interface 0x10, rev 0x02)
PCI bus 0 slot 2/1: vendor 0x14e4 product 0x471a (USB serial bus, interface 0x20, rev 0x02)
PCI bus 0 slot 3/0: vendor 0x14e4 product 0x471b (USB serial bus, rev 0x02)
PCI bus 0 slot 4/0: vendor 0x14e4 product 0x0804 (PCI bridge, rev 0x02)
PCI bus 0 slot 5/0: vendor 0x14e4 product 0x0816 (MIPS processor, rev 0x02)
PCI bus 0 slot 6/0: vendor 0x14e4 product 0x471d (IDE mass storage, rev 0x02)
PCI bus 0 slot 7/0: vendor 0x14e4 product 0x4718 (network/computing crypto, rev 0x02)
PCI bus 0 slot 8/0: vendor 0x14e4 product 0x080f (RAM memory, rev 0x02)
PCI bus 0 slot 9/0: vendor 0x14e4 product 0x471e (class 0xfe, subclass 0x00, rev 0x02)
Initializing Devices.

No DPN
This is a Parallel Flash
Boot partition size = 262144(0x40000)
Partition information:
boot    #00   00000000 -> 0003FFFF  (262144)
trx     #01   00040000 -> 0004001B  (28)
os      #02   0004001C -> 007F7FFF  (8093668)
nvram   #03   007F8000 -> 007FFFFF  (32768)
Partition information:
boot    #00   00000000 -> 0003FFFF  (262144)
trx     #01   00040000 -> 007F7FFF  (8093696)
nvram   #02   007F8000 -> 007FFFFF  (32768)
PCI bus 0 slot 1/0: pci_map_mem: attempt to map 64-bit region tag=0x800 @ addr=18010004
PCI bus 0 slot 1/0: pci_map_mem: addr=0x18010004 pa=0x18010000
ge0: BCM5750 Ethernet at 0x18010000
CPU type 0x2901A: 300MHz
Total memory: 65536 KBytes

Total memory used by CFE:  0x80700000 - 0x807A60B0 (680112)
Initialized Data:          0x8073A2B0 - 0x8073E540 (17040)
BSS Area:                  0x8073E540 - 0x807400B0 (7024)
Local Heap:                0x807400B0 - 0x807A40B0 (409600)
Stack Area:                0x807A40B0 - 0x807A60B0 (8192)
Text (code) segment:       0x80700000 - 0x8073A2B0 (238256)
Boot area (physical):      0x007A7000 - 0x007E7000
Relocation Factor:         I:00000000 - D:00000000

Boot version: v4.2
The boot is CFE

mac_init(): Find mac [00:21:29:C6:61:00] in location 0
Nothing...
country_init(): Find country code in location 0
The country is same
CMD: [ifconfig eth0 -addr=192.168.1.1 -mask=255.255.255.0]
eth0: Link speed: 1000BaseT FDX
Device eth0:  hwaddr 00-21-29-C6-61-00, ipaddr 192.168.1.1, mask 255.255.255.0
        gateway not set, nameserver not set
CMD: [go;]
Check CRC of image1
  Len:     0x717000     (7434240)       (0xBC040000)
  Offset0: 0x1C         (28)            (0xBC04001C)
  Offset1: 0x1016DC     (1054428)       (0xBC1416DC)
  Offset2: 0x0  (0)     (0xBC040000)
  Header CRC:    0x9E47184F
  Calculate CRC: 0x9E47184F
Image 1 is OK
Try to load image 1.
CMD: [load -raw -addr=0x807a60b0 -max=0x3a0000 :]
Loader:raw Filesys:tftp Dev:eth0 File:: Options:(null)
Loading: Failed.
Could not load :: Timeout occured
CMD: [boot -raw -z -addr=0x80001000 -max=0x3a0000 flash0.os:]
Loader:raw Filesys:raw Dev:flash0.os File: Options:(null)
Loading: .. 2416640 bytes read
Entry at 0x80001000
Closing network.
eth0: cannot clear 1400/00000002
Starting program at 0x80001000
CPU revision is: 0002901a
Primary instruction cache 32kb, linesize 16 bytes (4 ways)
Primary data cache 32kb, linesize 16 bytes (2 ways)
 2008
Setting the PFC to its default value
Determined physical RAM map:
 memory: 04000000 @ 00000000 (usable)
On node 0 totalpages: 16384
zone(0): 16384 pages.
zone(1): 0 pages.
zone(2): 0 pages.
Kernel command line: root=/dev/mtdblock2 noinitrd console=ttyS0,115200
CPU: BCM4785 rev 2 at 300 MHz
Calibrating delay loop... 299.82 BogoMIPS
Memory: 62208k/65536k available (2119k kernel code, 3328k reserved, 144k data, 76k init, 0k highmem)
Dentry cache hash table entries: 8192 (order: 4, 65536 bytes)
Inode cache hash table entries: 4096 (order: 3, 32768 bytes)
Mount-cache hash table entries: 1024 (order: 1, 8192 bytes)
Buffer-cache hash table entries: 4096 (order: 2, 16384 bytes)
Page-cache hash table entries: 16384 (order: 4, 65536 bytes)
Checking for 'wait' instruction...  unavailable.
POSIX conformance testing by UNIFIX
PCI: Initializing host
PCI: Fixing up bus 0
PCI: Fixing up bridge
PCI: Fixing up bus 1
Linux NET4.0 for Linux 2.4
Based upon Swansea University Computer Society NET3.039
Initializing RT netlink socket
Starting kswapd
devfs: v1.12c (20020818) Richard Gooch (rgooch@atnf.csiro.au)
devfs: boot_options: 0x1
NTFS driver v1.1.22 [Flags: R/O]
squashfs: version 3.0 (2006/03/15) Phillip Lougher
pty: 256 Unix98 ptys configured
Serial driver version 5.05c (2001-07-08) with MANY_PORTS SHARE_IRQ SERIAL_PCI enabled
ttyS00 at 0xb8000300 (irq = 8) is a 16550A
ttyS01 at 0xb8000400 (irq = 0) is a 16550A
HDLC line discipline: version $Revision$, maxframe=4096
N_HDLC line discipline registered.
PPP generic driver version 2.4.2
Broadcom Gigabit Ethernet Driver bcm5700 with Broadcom NIC Extension (NICE) ver. 8.3.14 (11/2/05)
PHY ID unknown, assume it is a copper PHY.
eth0: Broadcom BCM4785 10/100/1000 Integrated Controller found at mem 18010000, IRQ 5, node addr 002129c66100
eth0: Unknown transceiver found
eth0: Scatter-gather ON, 64-bit DMA ON, Tx Checksum ON, Rx Checksum ON, 802.1Q VLAN ON, NAPI ON
SCSI subsystem driver Revision: 1.00
 Amd/Fujitsu Extended Query Table v1.1 at 0x0040
number of CFI chips: 1
Flash device: 0x800000 at 0x1c000000
Physically mapped flash: squashfs filesystem found at block 1285
(Not Found Lang Block)off=0x1416dc off1=0x7e0000 size=0x800000
Creating 5 MTD partitions on "Physically mapped flash":
0x00000000-0x00040000 : "pmon"
0x00040000-0x007e0000 : "linux"
0x001416dc-0x007e0000 : "rootfs"
mtd: partition "rootfs" doesn't start on an erase block boundary -- force read-only
0x007e0000-0x007f0000 : "lang"
0x007f0000-0x00800000 : "nvram"
sflash: found no supported devices
usb.c: registered new driver usbdevfs
usb.c: registered new driver hub
ehci_hcd 00:02.1: PCI device 14e4:471a
ehci_hcd 00:02.1: irq 3, pci mem b8002800
usb.c: new USB bus registered, assigned bus number 1
ehci_hcd 00:02.1: illegal capability!
ECHI PCI device 471a14e4 found.
PCI: 00:02.1 PCI cache line size set incorrectly (0 bytes) by BIOS/FW, correcting to 32
ehci_hcd 00:02.1: USB 0.0 enabled, EHCI 1.00, driver 2003-Dec-29/2.4
hub.c: USB hub found
hub.c: 2 ports detected
host/usb-uhci.c: $Revision: 1.2 $ time 21:04:02 Jun  2 2008
host/usb-uhci.c: High bandwidth mode enabled
ECHI PCI device 471b14e4 found.
host/usb-uhci.c: v1.275:USB Universal Host Controller Interface driver
host/usb-ohci.c: USB OHCI at membase 0xb8002000, IRQ 3
host/usb-ohci.c: usb-00:02.0, PCI device 14e4:471a
usb.c: new USB bus registered, assigned bus number 2
hub.c: USB hub found
hub.c: 2 ports detected
usb.c: registered new driver usblp
printer.c: v0.13: USB Printer Device Class driver
Initializing USB Mass Storage driver...
usb.c: registered new driver usb-storage
USB Mass Storage support registered.
NET4: Linux TCP/IP 1.0 for NET4.0
IP Protocols: ICMP, UDP, TCP, IGMP
IP: routing cache hash table of 512 buckets, 4Kbytes
TCP: Hash tables configured (established 4096 bind 8192)
Linux IP multicast router 0.06 plus PIM-SM
ip_conntrack version 2.1 (512 buckets, 4096 max) - 368 bytes per conntrack
IPSEC isakmp Support Max Pass-through [50].
ip_conntrack_rtsp v0.01 loading
ip_nat_rtsp v0.01 loading
ip_tables: (C) 2000-2002 Netfilter core team
ipt_time loading
NET4: Unix domain sockets 1.0/SMP for Linux NET4.0.
IPv6 v0.8 for NET4.0
IPv6 over IPv4 tunneling driver
NET4: Ethernet Bridge 008 for NET4.0
802.1Q VLAN Support v1.7 Ben Greear <greearb@candelatech.com>
All bugs added by David S. Miller <davem@redhat.com>
cramfs: wrong magic
FAT: bogus logical sector size 19232
NTFS: Unable to set blocksize 512.
VFS: Mounted root (squashfs filesystem) readonly.
Mounted devfs on /dev
Freeing unused kernel memory: 76k freed
Algorithmics/MIPS FPU Emulator v1.5
cmd=[insmod ctmisc ]
Using /lib/modules/2.4.20/kernel/drivers/net/ctmisc/ctmisc.o
Register /dev/ctmisc device, major:250 minor:0
The boot is CFE
/dev/: cannot create
cmd=[misc -t get_wsc_pin -w 3 ]
type = [get_wsc_pin]
get_data(): cmd=ctmisc_ioctl: cmd=0x26, buffer size=196
0x26 count=8 lendata_init(): base = 0xbc03fcdc
=8
data_init(): location = [1], mydatas index = 1
ctmisc_ioctl: index=1
tallest:=====(ctmisc ioctl done...)=====
get_data(): Get WSC count is [1]
get_data(): WSC 0: [86328432]
get_data(): done
cmd=[misc -t get_mac -w 3 ]
type = [get_mac]
get_data(): cmd=ctmisc_ioctl: cmd=0x11, buffer size=196
0x11 count=8 lendata_init(): base = 0xbc001e00
=18
data_init(): location = [1], mydatas index = 1
ctmisc_ioctl: index=1
tallest:=====(ctmisc ioctl done...)=====
get_data(): Get MAC count is [1]
get_data(): MAC 0: [00:21:29:C6:61:00]
get_data(): done
cmd=[misc -t get_sn -w 3 ]
type = [get_sn]
get_data(): cmd=ctmisc_ioctl: cmd=0x15, buffer size=196
0x15 count=8 lendata_init(): base = 0xbc03fe30
=20
data_init(): location = [1], mydatas index = 1
ctmisc_ioctl: index=1
tallest:=====(ctmisc ioctl done...)=====
get_data(): Get SN count is [1]
get_data(): SN 0: [CTG01H700321<FF><FF><FF><FF><FF><FF><FF><FF>]
get_data(): done
cmd=[misc -t get_country -w 3 ]
type = [get_country]
get_data(): cmd=ctmisc_ioctl: cmd=0x2c, buffer size=196
0x2c count=1 lendata_init(): base = 0xbc03fe2c
=4
data_init(): location = [1], mydatas index = 1
ctmisc_ioctl: index=1
tallest:=====(ctmisc ioctl done...)=====
get_data(): Get COUNTRY count is [1]
get_data(): COUNTRY 0: [EU<FF><FF>]
get_data(): done
cmd=[misc -t get_flash_type -w 1 ]
type = [get_flash_type]
ctmisc_ioctl: cmd=0x17, buffer size=196
get_flash_type()Try 4: vendor id = 0x007F, device id = 0x22CB
: cmd=0x17 countEon EN29LV640B 4Mx16 BotB=0 len=0
Flash Type: Eon EN29LV640B 4Mx16 BotB
tallest:=====(ctmisc ioctl done...)=====
Get FLASH TYPE is [Eon EN29LV640B 4Mx16 BotB]
------ CT HW version is NULL ------
cmd=[misc -t get_pa2ga0idxval -w 3 ]
type = [get_pa2ga0idxval]
ctmisc_ioctl: cmd=0x28, buffer size=196
get_data(): cmd=data_init(): base = 0xbc03f6c0
0x28 count=8 lendata_init(): location = [1], mydatas index = 1
=24
ctmisc_ioctl: index=1
tallest:=====(ctmisc ioctl done...)=====
get_data(): Get PA2GA0IDXVAL count is [1]
get_data(): PA2GA0IDXVAL 0: [4 0xfeca 0x14a4 0xfb21<FF><FF>]
get_data(): done
cmd=[misc -t get_pa2ga1idxval -w 3 ]
type = [get_pa2ga1idxval]
ctmisc_ioctl: cmd=0x2a, buffer size=196
get_data(): cmd=data_init(): base = 0xbc03f600
0x2a count=8 lendata_init(): location = [0], mydatas index = 0
=24
ctmisc_ioctl: index=0
tallest:=====(ctmisc ioctl done...)=====
get_data(): Get PA2GA1IDXVAL count is [0]
get_data(): done
2G idx[4] w0a0[0xfeca] w1a0[0x14a4] w2a0[0xfb21<FF><FF>]
Update [0xfeca] to [0xfeca]
Update [0x14a4] to [0x14a4]
Update [0xfb21<FF><FF>] to [0xfb21]
Using default 2G PA1 value
cmd=[misc -t get_pa5gha0idxval -w 3 ]
type = [get_pa5gha0idxval]
ctmisc_ioctl: cmd=0x38, buffer size=196
get_data(): cmd=data_init(): base = 0xbc03f4c0
0x38 count=8 lendata_init(): location = [1], mydatas index = 1
=24
ctmisc_ioctl: index=1
tallest:=====(ctmisc ioctl done...)=====
get_data(): Get PA5GHA0IDXVAL count is [1]
get_data(): PA5GHA0IDXVAL 0: [6 0xfea6 0x134c 0xfb34<FF><FF>]
get_data(): done
cmd=[misc -t get_pa5gha1idxval -w 3 ]
type = [get_pa5gha1idxval]
ctmisc_ioctl: cmd=0x3a, buffer size=196
get_data(): cmd=data_init(): base = 0xbc03f400
0x3a count=8 lendata_init(): location = [1], mydatas index = 1
=24
ctmisc_ioctl: index=1
tallest:=====(ctmisc ioctl done...)=====
get_data(): Get PA5GHA1IDXVAL count is [1]
get_data(): PA5GHA1IDXVAL 0: [6 0xfeac 0x12da 0xfb54<FF><FF>]
get_data(): done
5G high idx[6] w0a0[0xfea6] w1a0[0x134c] w2a0[0xfb34<FF><FF>]
Update [0xfea6] to [0xfea6]
Update [0x134c] to [0x134c]
Update [0xfb34<FF><FF>] to [0xfb34]
5G high idx[6] w0a1[0xfeac] w1a1[0x12da] w2a1[0xfb54<FF><FF>]
Update [0xfeac] to [0xfeac]
Update [0x12da] to [0x12da]
Update [0xfb54<FF><FF>] to [0xfb54]
cmd=[misc -t get_pa5gla0idxval -w 3 ]
type = [get_pa5gla0idxval]
ctmisc_ioctl: cmd=0x48, buffer size=196
get_data(): cmd=data_init(): base = 0xbc03f2c0
0x48 count=8 lendata_init(): location = [0], mydatas index = 0
=24
ctmisc_ioctl: index=0
tallest:=====(ctmisc ioctl done...)=====
get_data(): Get PA5GLA0IDXVAL count is [0]
get_data(): done
cmd=[misc -t get_pa5gla1idxval -w 3 ]
type = [get_pa5gla1idxval]
ctmisc_ioctl: cmd=0x4a, buffer size=196
get_data(): cmd=data_init(): base = 0xbc03f200
0x4a count=8 lendata_init(): location = [0], mydatas index = 0
=24
ctmisc_ioctl: index=0
tallest:=====(ctmisc ioctl done...)=====
get_data(): Get PA5GLA1IDXVAL count is [0]
get_data(): done
Using default 5G low PA0 value
Using default 5G low PA1 value
cmd=[misc -t get_pa5ga0idxval -w 3 ]
type = [get_pa5ga0idxval]
ctmisc_ioctl: cmd=0x58, buffer size=196
get_data(): cmd=data_init(): base = 0xbc03f0c0
0x58 count=8 lendata_init(): location = [1], mydatas index = 1
=24
ctmisc_ioctl: index=1
tallest:=====(ctmisc ioctl done...)=====
tallest:=====(ctmisc ioctl done...)=====
get_data(): Get PA5GA0IDXVAL count is [1]
get_data(): PA5GA0IDXVAL 0: [4 0xfead 0x134f 0xfb43<FF><FF>]
get_data(): done
cmd=[misc -t get_pa5ga1idxval -w 3 ]
type = [get_pa5ga1idxval]
ctmisc_ioctl: cmd=0x5a, buffer size=196
get_data(): cmd=data_init(): base = 0xbc03f000
0x5a count=8 lendata_init(): location = [0], mydatas index = 0
=24
ctmisc_ioctl: index=0
tallest:=====(ctmisc ioctl done...)=====
get_data(): Get PA5GA1IDXVAL count is [0]
get_data(): done
5G middle idx[4] w0a0[0xfead] w1a0[0x134f] w2a0[0xfb43<FF><FF>]
Update [0xfead] to [0xfead]
Update [0x134f] to [0x134f]
Update [0xfb43<FF><FF>] to [0xfb43]
Using default 5G middle PA1 value
Restoring Storage Nvram Defaults
enter main_loop()..
find "lang" in MSQUASHFS error: Can't find a SQUASHFS superblock on mtdblock(31,3)
TD 3 (/dev/mtdblock/3)
ret = -1
www -> /www
mount: No such file or directory
cmd=[touch /tmp/var/lib/nfs/xtab ]
cmd=[chmod 644 /tmp/var/lib/nfs/xtab ]
cmd=[touch /tmp/var/lib/nfs/etab ]
cmd=[chmod 644 /tmp/var/lib/nfs/etab ]
cmd=[touch /tmp/var/lib/nfs/rmtab ]
cmd=[chmod 644 /tmp/var/lib/nfs/rmtab ]
cmd=[touch /tmp/var/lib/nfs/state ]
cmd=[chmod go-rwx /tmp/var/lib/nfs/state ]
cmd=[touch /tmp/disk_updating_lock ]
cmd=[chmod 644 /tmp/disk_updating_lock ]
cmd=[touch /tmp/file_variable_updating_lock ]
cmd=[chmod 644 /tmp/file_variable_updating_lock ]
cmd=[insmod /lib/ufsd_cbtn.o ]
Using /lib/ufsd_cbtn.o
modules[0]=bcm57xx buf=[bcm57xx ]
modules[1]=wl buf=[bcm57xx wl ]
Needed modules: bcm57xx wl
cmd=[insmod bcm57xx ]
insmod: bcm57xx.o: no module by that name found
cmd=[insmod wl ]
Using /lib/modules/2.4.20/kernel/drivers/net/wl/wl.o
Error reading /proc/partitions: invalid header.
Failed trying to open `/proc/mdstat': No such file or directory
Failed trying to open `/proc/sestat': No such file or directory
Error reading /proc/partitions: invalid header.
Failed trying to open `/proc/mdstat': No such file or directory
Failed trying to open `/proc/sestat': No such file or directory
Hit enter to continue...The chipset is BCM4705 + BCM5397 for EWC

Make date==>Year:8,Month:6,Day:2
Firmware version =>v1.00.00
sum3=7435264 garbage=992 n=1024
MD5=[461cebecdf6b0d453ed225d2030de824]
cmd=[killall httpd ]
killall: httpd: no process killed
cmd=[killall httpd ]
killall: httpd: no process killed
cmd=[resetbutton ]
WARNING: console log level set to 1
cmd=[vconfig set_name_type VLAN_PLUS_VID_NO_PAD ]
cmd=[vconfig add eth0 1 ]
cmd=[vconfig set_ingress_map vlan1 0 0 ]
cmd=[vconfig set_ingress_map vlan1 1 1 ]
cmd=[vconfig set_ingress_map vlan1 2 2 ]
cmd=[vconfig set_ingress_map vlan1 3 3 ]
cmd=[vconfig set_ingress_map vlan1 4 4 ]
cmd=[vconfig set_ingress_map vlan1 5 5 ]
cmd=[vconfig set_ingress_map vlan1 6 6 ]
cmd=[vconfig set_ingress_map vlan1 7 7 ]
cmd=[vconfig add eth0 2 ]
cmd=[vconfig set_ingress_map vlan2 0 0 ]
cmd=[vconfig set_ingress_map vlan2 1 1 ]
cmd=[vconfig set_ingress_map vlan2 2 2 ]
cmd=[vconfig set_ingress_map vlan2 3 3 ]
cmd=[vconfig set_ingress_map vlan2 4 4 ]
cmd=[vconfig set_ingress_map vlan2 5 5 ]
cmd=[vconfig set_ingress_map vlan2 6 6 ]
cmd=[vconfig set_ingress_map vlan2 7 7 ]
cmd=[brctl addbr br0 ]
cmd=[brctl setfd br0 0 ]
cmd=[brctl stp br0 dis ]
name=[vlan1] lan_ifname=[br0]
cmd=[brctl addif br0 vlan1 ]
br0: No such file or directory
cmd=[wlconf vlan1 up ]
vlan1: Operation not supported
name=[eth1] lan_ifname=[br0]
Write wireless mac successfully
cmd=[brctl addif br0 eth1 ]
br0: No such file or directory
cmd=[wlconf eth1 up ]
eth1: Numerical result out of range
eth1: Operation not supported
eth1: Invalid argument
eth1: Invalid argument
eth1: Operation not supported
eth1: Operation not supported
eth1: Invalid argument
eth1: Invalid argument
eth1: Invalid argument
eth1: Invalid argument
eth1: Invalid argument
eth1: Invalid argument
eth1: Invalid argument
eth1: Invalid argument
eth1: Invalid argument
eth1: Invalid argument
eth1: Invalid argument
eth1: Invalid argument
eth1: Invalid argument
eth1: Invalid argument
eth1: Invalid argument
eth1: Invalid argument
eth1: Invalid argument
eth1: Invalid argument
eth1: Invalid argument
eth1: Invalid argument
eth1: Invalid argument
cmd=[brctl addif br0 eth1 ]
device eth1 is already a member of a bridge; can't enslave it to bridge br0.
name=[eth2] lan_ifname=[br0]
Write wireless mac successfully
cmd=[brctl addif br0 eth2 ]
br0: No such file or directory
cmd=[wlconf eth2 up ]
eth2: Numerical result out of range
eth2: Operation not supported
eth2: Operation not supported
eth2: Operation not supported
cmd=[brctl addif br0 eth2 ]
device eth2 is already a member of a bridge; can't enslave it to bridge br0.
name=[eth3] lan_ifname=[br0]
cmd=[brctl addif br0 eth3 ]
interface eth3 does not exist!
eth3: No such device
module:  wl                  c0068000  1172704   2
cmd=[wl gpiotimerval 0x640000 ]
wl: No such file or directory
cmd=[wl vlan_mode 0 ]
wl: No such file or directory
lo: File exists
Set 66560 to /proc/sys/net/core/rmem_max ...
cmd=[tftpd -s /tmp -c -l -P 610N ]
cmd=[cron ]
The boot is CFE
tftp server started
tftpd: standalone socket
cron: No such file or directory
cron: created
[HTTPD Starting on /www]
cmd=[httpd ]
cmd=[dnsmasq -h -i br0 -r /tmp/resolv.conf ]
br0 192.168.1.100  86400
cmd=[udhcpd /tmp/udhcpd.conf ]
info, udhcp server (v0.9.8) started
cmd=[/bin/wsccmd ]
cmd=[nas /tmp/nas.lan.conf /tmp/nas.lan.pid lan ]
zebra disabled.
No disk, do not start samba.
cmd=[killall twonkymedia ]
killall: twonkymedia: no process killed
cmd=[killall twonkymediaserv ]
killall: twonkymediaserv: no process killed
cmd=[killall twonkymediaserver ]
eth1: ignore i/f due to error(s)
eth2: ignore i/f due to error(s)
killall: twonkymediaserver: no process killed
cmd=[upnp -D -L br0 -W  -S 0 -I 60 -A 180 ]
*********************************************
Wi-Fi Simple Config Application - Intel Corp.
Version: Build 1.0.5, November 19 2006
*********************************************
calling upnp_main
lltd:echo WRT610N > /proc/sys/kernel/hostname
Initializing stack...button monitor start...!
 OK
Now starting stack
LLTD: wireless interface argument is eth1.
get mac = 00 21 29 C6 61 02
Using /bin/eghn_kernel_module.o
IP is 101a8c0
mask is ffffff
cmd=[tc qdisc del dev vlan1 root ]
RTNETLINK answers: No such file or directory
cmd=[tc qdisc del dev eth1 root ]
RTNETLINK answers: No such file or directory
Initializing UPnP Sdk with
         ipaddress = (null) port = 0
UPnP Initialized
         ipaddress= 192.168.1.1 port = 49152
Specifying the webserver root directory -- /var/EGHN_QPH
Registering the RootDevice
         with desc_doc_url: http://192.168.1.1:49152/qphdevicedesc.xml
RootDevice Registered
Initializing State Table
Found service: urn:schemas-upnp-org:service:QosPolicyHolder:2
serviceId: urn:upnp-org:serviceId:QosPolicyHolder-1
State Table Initialized
cmd=[tc qdisc del dev eth2 root ]
RTNETLINK answers: No such file or directory
cmd=[sh /tmp/cmdfile134 ]
Advertisements Sent
cmd=[dhcp6s -c /tmp/dhcp6s.conf br0 ]
Dispay orig configurations
cmd=[cat /tmp/cmdfile134 ]
tc qdisc add dev vlan1 root handle 1: prio bands 8 priomap 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7
tc qdisc add dev vlan1 parent 1:1 handle 10: pfifo limit 20
tc qdisc add dev vlan1 parent 1:2 handle 20: pfifo limit 20
tc qdisc add dev vlan1 parent 1:3 handle 30: pfifo limit 20
tc qdisc add dev vlan1 parent 1:4 handle 40: pfifo limit 20
tc qdisc add dev vlan1 parent 1:5 handle 50: pfifo limit 20
tc qdisc add dev vlan1 parent 1:6 handle 60: pfifo limit 20
tc qdisc add dev vlan1 parent 1:7 handle 70: pfifo limit 20
tc qdisc add dev vlan1 parent 1:8 handle 80: pfifo limit 20
tc filter add dev vlan1 parent 1:0 prio 5 protocol all tcindex mask 0xff shift 0 pass_on
tc filter add dev vlan1 parent 1:0 prio 5 handle 0 tcindex classid 1:6
tc filter add dev vlan1 parent 1:0 prio 5 handle 1 tcindex classid 1:8
tc filter add dev vlan1 parent 1:0 prio 5 handle 2 tcindex classid 1:7
tc filter add dev vlan1 parent 1:0 prio 5 handle 3 tcindex classid 1:5
tc filter add dev vlan1 parent 1:0 prio 5 handle 4 tcindex classid 1:4
tc filter add dev vlan1 parent 1:0 prio 5 handle 5 tcindex classid 1:3
tc filter add dev vlan1 parent 1:0 prio 5 handle 6 tcindex classid 1:2
tc filter add dev vlan1 parent 1:0 prio 5 handle 7 tcindex classid 1:1
cmd=[sh /tmp/cmdfile134 ]
cmd=[killall -1 radvd ]
DEVICE PIN: 86328432
UdpLib: Entered udp_open
UdpLib: Socket open successful, sd: 9
UdpLib: Entered udp_bind
UdpLib: Binding successful for socket [9]
UdpLib: Entered udp_read

******* MODE: Access Point *******

DEVICE PIN:86328432
WSC: In unconfiged AP mode, wait for start command....
tlvPtrChar* : func CMasterControl_InitiateRegistration  line 658 allocating memory 0x10003700 for 0x100036e8
UdpLib: Entered udp_open
UdpLib: Socket open successful, sd: 10
UdpLib: Entered udp_bind
UdpLib: Binding successful for socket [10]
UdpLib: Entered udp_read
UdpLib: Entered udp_read
killall: radvd: no process killed
Waiting for Registrar to connect...
tallest:=====( wan_or_lan=wan )=====
tallest:=====( wan_or_lan=wan is wan !!)=====
cmd=[udhcpc -i vlan2 -l br0 -p /var/run/wan_udhcpc.pid -s /tmp/udhcpc ]
info, udhcp client (v0.9.8) started
cmd=[nas /tmp/nas.wan.conf /tmp/nas.wan.pid wan ]
cmd=[dhcp6s -c /tmp/dhcp6s.conf br0 ]
Hit enter to continue...No interface specified. Quitting...
Hit enter to continue...Hit enter to continue...cmd=[sh /tmp/cmdfile134 ]
Hit enter to continue...
}}}

{{{
root@OpenWrt:/# cat /proc/version
Linux version 2.6.25.16 (andy@devsandbox.padded-cell.net) (gcc version 4.1.2) #1 Sun Sep 21 19:55:53 PDT 2008
}}}

{{{
root@OpenWrt:/# cat /proc/cpuinfo
system type             : Broadcom BCM47XX
processor               : 0
cpu model               : Broadcom BCM3302 V1.10
BogoMIPS                : 299.00
wait instruction        : yes
microsecond timers      : yes
tlb_entries             : 32
extra interrupt vector  : yes
hardware watchpoint     : no
ASEs implemented        : mips16
shadow register sets    : 1
core                    : 0
VCED exceptions         : not available
VCEI exceptions         : not available
}}}

{{{
root@OpenWrt:/# cat /proc/mtd
dev:    size   erasesize  name
mtd0: 00040000 00010000 "cfe"
mtd1: 007b0000 00010000 "linux"
mtd2: 006eb400 00010000 "rootfs"
mtd3: 005c0000 00010000 "rootfs_data"
mtd4: 00010000 00010000 "nvram"
}}}

{{{
root@OpenWrt:/# cat /proc/modules
nf_nat_tftp 448 0 - Live 0xc011c000
nf_conntrack_tftp 2448 1 nf_nat_tftp, Live 0xc011a000
nf_nat_irc 928 0 - Live 0xc0118000
nf_conntrack_irc 2768 1 nf_nat_irc, Live 0xc0116000
nf_nat_ftp 1440 0 - Live 0xc0114000
nf_conntrack_ftp 5120 1 nf_nat_ftp, Live 0xc0102000
ipt_TTL 864 0 - Live 0xc010f000
xt_MARK 1184 0 - Live 0xc010d000
ipt_ECN 1440 0 - Live 0xc010b000
xt_CLASSIFY 608 0 - Live 0xc0109000
ipt_ttl 672 0 - Live 0xc0107000
xt_time 1824 0 - Live 0xc0105000
ipt_time 1536 0 - Live 0xc00f4000
xt_tcpmss 1056 0 - Live 0xc0100000
xt_statistic 800 0 - Live 0xc00fe000
xt_mark 832 0 - Live 0xc00fc000
xt_mac 704 0 - Live 0xc00fa000
xt_length 736 0 - Live 0xc00f8000
ipt_ecn 992 0 - Live 0xc00f6000
xt_DSCP 2048 0 - Live 0xc00bb000
xt_dscp 1216 0 - Live 0xc00bd000
ipt_LOG 4960 1 - Live 0xc00f1000
xt_CHAOS 1792 0 - Live 0xc00ef000
xt_DELUDE 2368 1 - Live 0xc00ed000
xt_TARPIT 2752 1 - Live 0xc00b7000
xt_quota 768 0 - Live 0xc00b9000
xt_portscan 1920 0 - Live 0xc007e000
xt_pkttype 704 0 - Live 0xc00b5000
xt_physdev 1456 0 - Live 0xc0080000
iptable_raw 800 0 - Live 0xc006b000
ppp_async 9728 0 - Live 0xc0077000
ppp_generic 20096 1 ppp_async, Live 0xc00bf000
slhc 5248 1 ppp_generic, Live 0xc007b000
crc_ccitt 992 1 ppp_async, Live 0xc006d000
b43 169232 0 - Live 0xc008a000
switch_core 5248 0 - Live 0xc004f000
mac80211 158480 1 b43, Live 0xc00c5000
cfg80211 24624 1 mac80211, Live 0xc0082000
arc4 832 0 - Live 0xc0069000
aes_generic 28432 0 - Live 0xc006f000
deflate 1568 0 - Live 0xc0067000
ecb 1408 0 - Live 0xc0065000
cbc 2176 0 - Live 0xc0063000
crypto_blkcipher 12272 2 ecb,cbc, Live 0xc005b000
crypto_hash 992 0 - Live 0xc0059000
cryptomgr 1696 0 - Live 0xc0052000
crypto_algapi 8576 7 arc4,aes_generic,deflate,ecb,cbc,crypto_blkcipher,cryptomgr, Live 0xc0055000
diag 7728 0 - Live 0xc0060000
}}}

{{{
root@OpenWrt:/# cat /proc/devices
Character devices:
  1 mem
  4 ttyS
  5 /dev/tty
  5 /dev/console
  5 /dev/ptmx
 10 misc
 13 input
 90 mtd
108 ppp
128 ptm
136 pts

Block devices:
 31 mtdblock
}}}

{{{
root@OpenWrt:/# free
              total         used         free       shared      buffers
  Mem:        62336         8220        54116            0          944
 Swap:            0            0            0
Total:        62336         8220        54116
}}}

{{{
root@OpenWrt:/# cat /proc/meminfo
MemTotal:        62336 kB
MemFree:         54104 kB
Buffers:           944 kB
Cached:           3304 kB
SwapCached:          0 kB
Active:           2580 kB
Inactive:         2364 kB
SwapTotal:           0 kB
SwapFree:            0 kB
Dirty:               0 kB
Writeback:           0 kB
AnonPages:         712 kB
Mapped:            736 kB
Slab:             1960 kB
SReclaimable:      416 kB
SUnreclaim:       1544 kB
PageTables:        168 kB
NFS_Unstable:        0 kB
Bounce:              0 kB
CommitLimit:     31168 kB
Committed_AS:     2356 kB
VmallocTotal:  1048404 kB
VmallocUsed:      1208 kB
VmallocChunk:  1047160 kB
}}}

{{{
root@OpenWrt:/# cat /proc/iomem
00000000-03ffffff : System RAM
  00001000-0021c323 : Kernel code
  0021c324-0026e6bf : Kernel data
18010000-1801ffff : SSB Broadcom 47xx GigE memory
  18010000-1801ffff : 0000:01:00.0
40000000-7fffffff : SSB PCIcore external memory
  40000000-40003fff : 0000:00:01.0
  40004000-40007fff : 0000:00:02.0
}}}

{{{
root@OpenWrt:/# ps
  PID USER       VSZ STAT COMMAND
    1 root      1956 S    init
    2 root         0 SW<  [kthreadd]
    3 root         0 SW<  [ksoftirqd/0]
    4 root         0 SW<  [events/0]
    5 root         0 SW<  [khelper]
   22 root         0 SW<  [kblockd/0]
   64 root         0 SW   [pdflush]
   65 root         0 SW   [pdflush]
   66 root         0 SW<  [kswapd0]
   67 root         0 SW<  [aio/0]
   78 root         0 SW<  [mtdblockd]
  268 root      1956 S    logger -s -p 6 -t
  269 root      1960 S    /bin/ash --login
  286 root      1968 S    syslogd -C16
  288 root      1948 S    klogd
  300 root      1128 S    /sbin/hotplug2 --override --persistent --max-children
  577 root      1952 S    /usr/sbin/httpd -p 80 -h /www -r OpenWrt
  581 root      1952 S    telnetd -l /bin/login
  597 nobody    1272 S    /usr/sbin/dnsmasq -K -D -y -Z -b -E -s lan -S /lan/ -
  616 root         0 SWN  [jffs2_gcd_mtd3]
  647 root      1932 S    /usr/sbin/dropbear -p 22
  658 root      1956 R    ps
}}}

{{{
root@OpenWrt:/# ifconfig
lo        Link encap:Local Loopback··
          inet addr:127.0.0.1  Mask:255.0.0.0
          UP LOOPBACK RUNNING  MTU:16436  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0·
          RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)
}}}

{{{
root@OpenWrt:/# dmesg
Linux version 2.6.25.16 (andy@devsandbox.padded-cell.net) (gcc version 4.1.2) #1 Sun Sep 21 19:55:53 PDT 2008
console [early0] enabled
CPU revision is: 0002901a (Broadcom BCM3302)
ssb: Core 0 found: ChipCommon (cc 0x800, rev 0x0F, vendor 0x4243)
ssb: Core 1 found: GBit Ethernet (cc 0x81F, rev 0x00, vendor 0x4243)
ssb: Core 2 found: USB 2.0 Host (cc 0x819, rev 0x00, vendor 0x4243)
ssb: Core 3 found: USB 2.0 Device (cc 0x81A, rev 0x02, vendor 0x4243)
ssb: Core 4 found: PCI (cc 0x804, rev 0x0B, vendor 0x4243)
ssb: Core 5 found: MIPS 3302 (cc 0x816, rev 0x07, vendor 0x4243)
ssb: Core 6 found: PATA (cc 0x81D, rev 0x00, vendor 0x4243)
ssb: Core 7 found: IPSEC (cc 0x80B, rev 0x03, vendor 0x4243)
ssb: Core 8 found: MEMC SDRAM (cc 0x80F, rev 0x03, vendor 0x4243)
ssb: Core 9 found: SATA XOR-DMA (cc 0x81E, rev 0x00, vendor 0x4243)
ssb: Initializing MIPS core...
ssb: set_irq: core 0x081f, irq 3 => 2
ssb: set_irq: core 0x0819, irq 1 => 3
ssb: set_irq: core 0x0804, irq 4 => 4
ssb: Sonics Silicon Backplane found at address 0x18000000
Serial init done.
Determined physical RAM map:
 memory: 04000000 @ 00000000 (usable)
Entering add_active_range(0, 0, 16384) 0 entries of 256 used
Initrd not found or empty - disabling initrd
Zone PFN ranges:
  Normal          0 ->    16384
Movable zone start PFN for each node
early_node_map[1] active PFN ranges
    0:        0 ->    16384
On node 0 totalpages: 16384
  Normal zone: 128 pages used for memmap
  Normal zone: 0 pages reserved
  Normal zone: 16256 pages, LIFO batch:3
  Movable zone: 0 pages used for memmap
Built 1 zonelists in Zone order, mobility grouping on.  Total pages: 16256
Kernel command line: root=/dev/mtdblock2 rootfstype=squashfs,jffs2 init=/etc/preinit noinitrd console=ttyS0,115200
Primary instruction cache 32kB, VIPT, 4-way, linesize 16 bytes.
Primary data cache 32kB, 2-way, VIPT, cache aliases, linesize 16 bytes
Synthesized clear page handler (26 instructions).
Synthesized copy page handler (46 instructions).
PID hash table entries: 256 (order: 8, 1024 bytes)
console handover: boot [early0] -> real [ttyS0]
Dentry cache hash table entries: 8192 (order: 3, 32768 bytes)
Inode-cache hash table entries: 4096 (order: 2, 16384 bytes)
Memory: 62128k/65536k available (2156k kernel code, 3336k reserved, 328k data, 136k init, 0k highmem)
Calibrating delay loop... 299.00 BogoMIPS (lpj=598016)
Mount-cache hash table entries: 512
net_namespace: 540 bytes
NET: Registered protocol family 16
Switched to high resolution mode on CPU 0
ssb: PCIcore in host mode found
Registering a PCI bus after boot
PCI: Fixing up bridge 0000:00:00.0
PCI: Setting latency timer of device 0000:00:00.0 to 64
PCI: Fixing up device 0000:00:00.0
PCI: Fixing latency timer of device 0000:00:00.0 to 168
Registering a PCI bus after boot
NET: Registered protocol family 2
IP route cache hash table entries: 1024 (order: 0, 4096 bytes)
TCP established hash table entries: 2048 (order: 2, 16384 bytes)
TCP bind hash table entries: 2048 (order: 1, 8192 bytes)
TCP: Hash tables configured (established 2048 bind 2048)
TCP reno registered
detected lzma initramfs
initramfs: LZMA lc=1,lp=2,pb=2,origSize=512
squashfs: version 3.0 (2006/03/15) Phillip Lougher
Registering mini_fo version $Id$
JFFS2 version 2.2. (NAND) (SUMMARY)  © 2001-2006 Red Hat, Inc.
io scheduler noop registered
io scheduler deadline registered (default)
Serial: 8250/16550 driver $Revision: 1.90 $ 2 ports, IRQ sharing enabled
serial8250: ttyS0 at MMIO 0x0 (irq = 2) is a 16550A
serial8250: ttyS1 at MMIO 0x0 (irq = 2) is a 16550A
serial8250 serial8250.0: unable to register port at index 0 (IO0 MEMb8000300 IRQ2): -28
serial8250 serial8250.0: unable to register port at index 1 (IO0 MEMb8000400 IRQ2): -28
flash init: 0x1c000000 0x02000000
Physically mapped flash: Found 1 x16 devices at 0x0 in 16-bit bank
Physically mapped flash: Found an alias at 0x800000 for the chip at 0x0
Physically mapped flash: Found an alias at 0x1000000 for the chip at 0x0
Physically mapped flash: Found an alias at 0x1800000 for the chip at 0x0
 Amd/Fujitsu Extended Query Table at 0x0040
number of CFI chips: 1
cfi_cmdset_0002: Disabling erase-suspend-program due to code brokenness.
Flash device: 0x800000 at 0x1fc00000
bootloader size: 262144
Updating TRX offsets and length:
old trx = [0x0000001c, 0x0000090c, 0x000c4c00], len=0x00201000 crc32=0xc99586f5
new trx = [0x0000001c, 0x0000090c, 0x000c4c00], len=0x000c4c00 crc32=0x2097e743
Done
Creating 4 MTD partitions on "Physically mapped flash":
0x00000000-0x00040000 : "cfe"
0x00040000-0x007f0000 : "linux"
0x00104c00-0x007f0000 : "rootfs"
mtd: partition "rootfs" doesn't start on an erase block boundary -- force read-only
mtd: partition "rootfs" set to be root filesystem
mtd: partition "rootfs_data" created automatically, ofs=230000, len=5C0000·
0x00230000-0x007f0000 : "rootfs_data"
0x007f0000-0x00800000 : "nvram"
nf_conntrack version 0.5.0 (1024 buckets, 4096 max)
ip_tables: (C) 2000-2006 Netfilter Core Team
TCP vegas registered
NET: Registered protocol family 1
NET: Registered protocol family 17
Bridge firewalling registered
802.1Q VLAN Support v1.8 Ben Greear <greearb@candelatech.com>
All bugs added by David S. Miller <davem@redhat.com>
VFS: Mounted root (squashfs filesystem) readonly.
Freeing unused kernel memory: 136k freed
Please be patient, while OpenWrt loads ...
Algorithmics/MIPS FPU Emulator v1.5
diag: Detected 'Linksys WRT54G/GS/GL'
roboswitch: Probing device eth0: No such device
roboswitch: Probing device eth1: No such device
roboswitch: Probing device eth2: No such device
roboswitch: Probing device eth3: No such device
BFL_ENETADM not set in boardflags. Use force=1 to ignore.
mini_fo: using base directory: /
mini_fo: using storage directory: /tmp/root
roboswitch: Probing device eth0: No such device
roboswitch: Probing device eth1: No such device
roboswitch: Probing device eth2: No such device
roboswitch: Probing device eth3: No such device
BFL_ENETADM not set in boardflags. Use force=1 to ignore.
Broadcom 43xx driver loaded [ Features: NLR, Firmware-ID: FW13 ]
PPP generic driver version 2.4.2
ipt_time loading
jffs2_scan_eraseblock(): End of filesystem marker found at 0x0
jffs2_build_filesystem(): unlocking the mtd device... done.
jffs2_build_filesystem(): erasing all blocks after the end marker... done.
mini_fo: using base directory: /
mini_fo: using storage directory: /jffs
}}}
