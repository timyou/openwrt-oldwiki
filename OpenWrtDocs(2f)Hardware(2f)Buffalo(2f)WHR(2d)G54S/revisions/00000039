'''Buffalo WHR-G54S'''

----
The device is supported in OpenWrt 0.9 (White Russian) and later.  You need to install the openwrt-brcm-2.4-<type>.trx firmware images using the TFTP method only! This is because the installed Buffalo Firmware loader may require or perform some kind of decryption and expects a filename with a .ENC extension instead of the standard .bin or .trx.
If you have a newer hardware revision (this being written on 8/21/2006), you should use the current SVN, as there are some bricking issues on older builds of OpenWrt. (Note: RC6 seems OK). There is also different hardware versions with almost same serial. (Also on old one) So DO NOT copy nvram from router to another or you can get brick because of memory settings.

This device is based on the Broadcom chipset so the openwrt-brcm-<type>.trx image is required.

 * connect ethernet to a LAN port
 * pull the power plug
 * press and hold the reset ("INIT") button
 * start the TFTP (as below)
 * plug the power back in
 * let go of the button.
The power light does *not* flash on this unit, but the diag does. This unit keeps the IP address that it was set to while in this mode. Factory setting is 192.168.11.1.  If using a recent Kamikaze, try 192.168.1.1 instead.

TFTP commands:

{{{
tftp 192.168.11.1
tftp> binary
tftp> trace
tftp> rexmt 1
tftp> timeout 60
tftp> put openwrt-xxx-x.x-xxx.trx
}}}
If you get something like

 . {{{
 sent WRQ <file=openwrt-brcm-2.4-squashfs.trx, mode=octet>
 sent WRQ <file=openwrt-brcm-2.4-squashfs.trx, mode=octet>
 sent WRQ <file=openwrt-brcm-2.4-squashfs.trx, mode=octet>
 sent WRQ <file=openwrt-brcm-2.4-squashfs.trx, mode=octet>
 sent WRQ <file=openwrt-brcm-2.4-squashfs.trx, mode=octet>
 sent WRQ <file=openwrt-brcm-2.4-squashfs.trx, mode=octet>
 ...
 Transfer timed out.
 }}}
then just try again.

After this, wait for the device to reboot and you should be set.

----
[[BR]]
'''Disassembly'''[[BR]]
I've written a little tutorial on how to take apart the WHR-G54S without breaking anything. You can find it
here:
http://www.k9spud.com/whr-g54s/disassembly.php

----

[[BR]]

'''GPIO Information for Buffalo WHR-G54S'''[[BR]]
These information are very useful for SD hack described below and for your own custom hacking on special I/O

{{{
PIN     Usage   Original Use
----------------------------------------------------------------
GPIO 0  Input   AOSS Button
GPIO 1  Output  Bridge led
GPIO 2  Output  Wlan Led
GPIO 3  Output  Extra Led (unknown use) between wlan and bridge
GPIO 4  Input   Reset Button
GPIO 5  Input   Bridge/Auto switch
GPIO 6  Output  AOSS Led
GPIO 7  Output  Diag Led
GPIO 8  N/A     don't know, i didn't find it
GPIO 9  Output  Power Led
}}}
Please note it's very important to understand original buffalo usage doesn't affect the way you use IOs, all ports are basically structured to work in Input as well as Output.[[BR]]
'''NOTE''': Using GPIO 4 is NOT a good idea :)

''(Ben)''

[[BR]]

----
'''[:OpenWrtDocs/Hardware/Buffalo/WHR-G54S/SD-MMC.hack:SD/MMC Hack]'''[[BR]]
This hack is very popular with other APs (eg.Linksys) and can be applied to Buffalo WHR-G54S as well, things are slightly different because of different usage of GPIO but there's a binary kernel module mmc.o optimized and fully working for Linksys as well as Buffalo

For this hack i've used these I/O (please see table described above)

{{{
Signal     GPIO
----------------
Data IN    5
Data OUT   6
Clock      3
CS         7
}}}
I've [:OpenWrtDocs/Hardware/Buffalo/WHR-G54S/SD-MMC.hack:created a new wiki page] with some photos of my hack, Hope it helps, send me some notes if you need more information on my job''' NOTE''': Using GPIO 4 (like linksys WRT models) is NOT a good idea here (reset button... :) )

''(Andrea Ben Benini)''

''.''

''.''

----
'''Built in Serial port on the WHR-G54S'''[[BR]] As with most of these AP devices the printed circuit board has one serial interface presented. The WHR-G54S however does not have a header block soldered on the board. The following details will allow you to connect to the serial interface using 3.3V TTL signals typically derived from a RS-232 to 3.3V TTL converter such as an ST232CN IC as used on a neat little PCB which can be obtained at a very reasonable price from http://www.robomicro.co.uk/

Or you can make your own from the schematic available here: http://www.k9spud.com/whr-g54s/

On the WHR-G54S locate the un-populated header block RJP1. This is in the top left of the board next to a large electrolytic capacitor. To the right of this block you will find several SM components and also un-populated pads. I used the following soldered connections onto the un-populated pads:

{{{
Left hand pad of  R48  >>  RX.    Receive data into the WHR-G54S.
Right hand pad of R50  >>  TX.    Transmit data from the WHR-G54S.}}}
|| pin 10 (missing) || pin  9 (unconnected) ||
|| pin  8 (ground) || pin  7 (RX) ||
|| pin  6 (ground) || pin  5 (unused) ||
|| pin  4 (+3.3VDC) || pin  3 (ground) ||
|| pin  2 (+3.3VDC) || pin  1 (TX) ||
||||<style="text-align: center;"> RJP1 ||
By default the serial port runs at 115200 8N1 using ANSI terminal emulation.

NB: This was a device with board revision WRTB-133G_V00 190-c02-9200 (This can be seen in the top left hand corner of the PCB. All my units have started with this code and therefore I can not be sure if the board layout is different on older units.

NB2: The table previously showed pins 4 and 2 as GND. As someone else already suspected they are 3.3 VDC when the device is powered up.

'''Using the second serial port on the WHR-G54S'''[[BR]]
I found out how to access the second serial interface. With dmesg you can see ttyS00 and ttyS01 present. On my hardware the second interface is present on the two unpopulated resistors R48 and R46. The right-hand solder-pad is directly connected to the processors 2nd tty. In the default openwrt configuration this interface runs at 9600 8N1 and there is no terminal. 
In the original hardware both pin 9 and pin 5 were not connected to anything. The unused pin 5 is connected to the left-hand solder pad of the unpopulated resistor R50. 


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
this is for devices with serials starting 7407 (you can ONLY run a current SVN version on these devices. See notes above. But RC6 seems OK):

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
I have a unit starting 7407 which is labelled "AirStation Turbo G" and "model WHR-G54S-1" on the packaging. It has a slide switch marked "BRI. / AUTO" on the side, and an "AOSS" button.

Running RC6:

{{{
root@OpenWrt:/# ls -1 /proc/diag/led
diag         # controls green "bridge" LED
internal     # seems to do nothing
ses          # controls orange LED next to AOSS button
}}}
The red "diag" LED comes up during power-up, but does not seem to be software controllable by !OpenWrt.

----
 CategoryModel CategoryModel
