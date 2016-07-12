= Linksys WRV54G =
The linksys WRV54G is no Wrt, it does not use a broadcom chip, and runs on arm instead of mips.

For now, i recommend the openixp project if you have a wrv.

= Hardware =
== CPU ==
Intel XScale 425
Part number: FWIXP425AB

{{{
Processor       : XScale-IXP42x Family rev 1 (v5b)
BogoMIPS        : 266.24
Features        : swp half fastmult edsp
CPU implementer : 0x69
CPU architecture: 5TE
CPU variant     : 0x0
CPU part        : 0x41f
CPU revision    : 1
Cache type      : undefined 5
Cache clean     : undefined 5
Cache lockdown  : undefined 5
Cache format    : Harvard
I size          : 32768
I assoc         : 32
I line length   : 32
I sets          : 32
D size          : 32768
D assoc         : 32
D line length   : 32
D sets          : 32
Hardware        : Gemtek GTWX5715 (Linksys WRV54G)
Revision        : 0000
Serial          : 0000000000000000
}}}
== RAM ==
32MB

== Flash ==
Intel Strataflash 8MB
Part Number: E28F640J3A120

== WLAN ==
Intersil Prism54


== Serial Pinout (J11) ==
 .
 || 1: || Txd ||
 || 7: || Rxd  2,4: +3.3V ||
 || 6,8: || GND ||
== JTAG Pinout (J2) to EA253 parallel cable ('''100Ohm except GND''') ==
 .
 || JTAG ||       DB-25 ||
 || 3 (TRST-) ||           6 ||
 || 5 (TDI) ||           2 ||
 || 7 (TMS) ||           4 ||
 || 9 (TCK) ||           3 ||
 || 11 (GND) ||          25 ||

more detail pinout
{{{
               c[] LED5
       +3.3V -- 1o o2 -- nc
       nTRST -- 3o o4 -- GND
         TDI -- 5o o6 -- GND
         TMS -- 7o o8 -- GND
         TCK -- 9o o10 - GND
         GND - 11o o12 - GND
         TDO - 13o o14 - GND
      nRESET - 15o o16 - GND
          nc - 17o o18 - GND
          nc - 19o o20 - GND
}}}
== booting openixp ==
{{{
 Uncompressing Linux......................................... done, booting the kernel.
RGLoader Version: 2.4.4 Internal Version: 1.2
Press ESC to enter BOOT MENU mode.
Booting an active image in 0 seconds
Uncompressing Linux......................................... done, booting the kernel.
Linux version 2.6.13 (root@linux) (gcc version 3.4.4) #164
Fri Oct 28 14:00:15 CEST 2005
CPU: XScale-IXP42x Family [690541f1] revision 1 (ARMv5TE)
Machine: Gemtek GTWX5715 (Linksys WRV54G)
Memory policy: ECC disabled, Data cache writeback
On node 0 totalpages: 8192
   DMA zone: 8192 pages, LIFO batch:3
  Normal zone: 0 pages, LIFO batch:1
  HighMem zone: 0 pages, LIFO batch:1
CPU0: D VIVT undefined 5 cache
CPU0: I cache: 32768 bytes, associativity 32, 32 byte lines, 32 sets
CPU0: D cache: 32768 bytes, associativity 32, 32 byte lines, 32 sets
Built 1 zonelists
Kernel command line: mtdparts=IXP4XX:1280k(boot)ro,1024k@1280k(linux)ro,4608k@2304k(root) console=ttyS0,115200 root=/dev/mtdblock2 rootfstype=jffs2 init=/sbin/init
PID hash table entries: 256 (order: 8, 4096 bytes)
Console: colour dummy device 80x30
Dentry cache hash table entries: 8192 (order: 3, 32768 bytes)
Inode-cache hash table entries: 4096 (order: 2, 16384 bytes)
Memory: 32MB = 32MB total Memory: 30464KB available (1538K code, 329K data, 76K init)
Calibrating delay loop... 266.24 BogoMIPS (lpj=1331200)
Mount-cache hash table entries: 512
CPU: Testing write buffer coherency: ok
NET: Registered protocol family 16
PCI: IXP4xx is host
PCI: IXP4xx Using direct access for memory space
PCI: bus0: Fast back to back transfers enabled
dmabounce: registered device 0000:00:01.0 on pci bus
dmabounce: registered device 0000:00:02.0 on pci bus
gtwx5715_map_irq: Mapped slot 1 pin 1 to IRQ 28
gtwx5715_map_irq: Mapped slot 2 pin 1 to IRQ 27
NetWinder Floating Point Emulator V0.97 (double precision)
JFFS2 version 2.2. (NAND) (C) 2001-2003 Red Hat, Inc.
Initializing Cryptographic API
creating /dev/console
IXP4xx Watchdog Timer: heartbeat 60 sec
Serial: 8250/16550 driver $Revision: 1.90 $ 2 ports, IRQ sharing disabled
platform: Matched Device serial8250.0 with Driver serial8250(irq = 13) is a XScale
io scheduler noop registered
RAMDISK driver initialized: 16 RAM disks of 8192K size 1024 blocksize
loop: loaded (max 8 devices)
nbd: registered device at major 43
platform: Matched Device IXP4XX-LED.0 with Driver IXP4XX-LED
platform: Bound Device IXP4XX-LED.0 to Driver IXP4XX-LED
tun: Universal TUN/TAP device driver, 1.6 tun: (C) 1999-2004 Max Krasnyansky
platform: Matched Device IXP4XX-Flash.0 with Driver IXP4XX-Flash
IXP4XX-Flash.0: Found 1 x16 devices at 0x0 in 16-bit bank
Intel/Sharp Extended Query Table at 0x0031
Using buffer write method cfi_cmdset_0001: Erase suspend on write enabled 0: offset=0x0,size=0x20000,blocks=64
MTD device IXP4XX-Flash.0
Creating 3 MTD partitions on "IXP4XX-Flash.
0x00000000-0x00140000 : "boot"
0x00140000-0x00240000 : "linux"
0x00240000-0x006c0000 : "root"
platform: Bound Device IXP4XX-Flash.0 to Driver IXP4XX-Flash
i2c /dev entries driver
platform: Matched Device IXP4XX-SPI.0 with Driver IXP4XX-SPI
platform: Bound Device IXP4XX-SPI.0 to Driver IXP4XX-SPI
KS8995M: Family ID: 95, Chip ID: 00, Revision ID: 01
NET: Registered protocol family 2
IP route cache hash table entries: 512 (order: -1, 2048 bytes)
TCP established hash table entries: 2048 (order: 2, 16384 bytes)
TCP bind hash table entries: 2048 (order: 1, 8192 bytes)
TCP: Hash tables configured (established 2048 bind 2048)
TCP reno registered TCP bic registered
NET: Registered protocol family 1
NET: Registered protocol family 17
VFS: Mounted root (jffs2 filesystem) readonly.
Freeing init memory: 76K
802.1Q VLAN Support v1.8 Ben Greear All bugs added by David S. Miller
Loaded prism54 driver, version 1.2
pci: Matched Device 0000:00:01.0 with Driver prism54
pci: Bound Device 0000:00:01.0 to Driver prism54
eth0: resetting device... eth0: uploading firmware... eth0: firmware version: eth0: firmware upload complete eth0: interface reset complete
ixp400: module license 'IPL' taints kernel.
ixp400: Module init.
ixp400_eth: Initializing IXP400 NPE Ethernet driver software v. 1.4
ixp400_eth: CPU clock speed (approx) = 266 MHz
ixp400_eth: ixp0 is using NPEB and the PHY at address 4
ixp400_eth: ixp1 is using NPEC and the PHY at address 5
ixp400_eth: Use default MAC address 00:02:b3:01:01:01 for port 0
ixp400_eth: Use default MAC address 00:02:b3:02:02:02 for port 1
ixp0.1: add 01:00:5e:00:00:01 mcast address to master interface
ixp0.2: add 01:00:5e:00:00:01 mcast address to master interface
ixp400_eth: ixp1,PHY:5 link up->down
ath_hal: 0.9.15.1 (AR5210, AR5211, AR5212, RF5111, RF5112, RF2413, RF5413, REGOPS_FUNC)
wlan: 0.8.4.2 (Atheros/multi-bss) ath_rate_onoe: 1.0 ath_pci: 0.9.4.5 (Atheros/multi-bss)
pci: Matched Device 0000:00:02.0 with Driver
ath_pci PCI: enabling device 0000:00:02.0 (0340 -> 0342)
wifi0: 11a rates: 6Mbps 9Mbps 12Mbps 18Mbps 24Mbps 36Mbps 48Mbps 54Mbps
wifi0: 11b rates: 1Mbps 2Mbps 5.5Mbps 11Mbps
wifi0: 11g rates: 1Mbps 2Mbps 5.5Mbps 11Mbps 6Mbps 9Mbps 12Mbps 18Mbps 24Mbps 36Mbps 48Mbps 54Mbps
wifi0: turboG rates: 6Mbps 12Mbps 18Mbps 24Mbps 36Mbps 48Mbps 54Mbps
SVN $Revision: 1200 $
wifi0: mac 5.9 phy 724.14 radio 3.6
wifi0: Use hw queue 1 for WME_AC_BE traffic
wifi0: Use hw queue 0 for WME_AC_BK traffic
wifi0: Use hw queue 2 for WME_AC_VI traffic
wifi0: Use hw queue 3 for WME_AC_VO traffic
wifi0: Use hw queue 8 for CAB traffic
wifi0: Use hw queue 9 for beacons
wifi0: Atheros 5212: mem=0x48000000, irq=27
pci: Bound Device 0000:00:02.0 to Driver
ath_pci wlan: mac acl policy registered
}}}
== lspci ==
{{{
 lspci:
00:01.0 Class 0280: 1260:3890 (rev 01)
   Subsystem: 1260:0000
   Flags: bus master, fast Back2Back, medium devsel, latency 128, IRQ 28
   Memory at 48010000 (32-bit, non-prefetchable) [size=8K]
   Capabilities: [dc] Power Management version 1
00:02.0 Class 0200: 168c:0013 (rev 01)
  Subsystem: 168c:2042
  Flags: bus master, fast Back2Back, medium devsel, latency 168, IRQ 27
  Memory at 48000000 (32-bit, non-prefetchable) [size=64K]
  Capabilities: [44] Power Management version 2
}}}
== /proc/diag ==
|| Bit ||         0 ||   1 ||
|| 0 ||         power LED constant yellow ||    power LED blinking green ||
|| 1 ||         wireless LED yellow, more light when working ||         wireless LED dark, green when working ||
|| 2 ||         wireless2 LED yellow, more light when working ||        wireless2 LED dark, green when working ||
|| 3 ||         Internet LED yellow, more light when working ||         Internet LED green, dark when working ||
|| 4 ||         DMZ LED green ||        DMZ LED dark ||
== random text ==
{{{
 The Linksys WRT54GS was a really good choice, but there are some problems with it, mainly that the speed of the processor not enough for driving the radio/ethernet at full speed and unfortunatelly the radio and the ethernet driver not in GPL, so no any modification possibility,etc.
The high-end AP's now contains Intel ARM processors,  Linksys have a VPN router that also have a GPL code, relatively cheap, so no any problem, let's modify it........
The hardware mods was relatively simple task. Using an SVHS 4 pole connector and a mobile phone serial cable, there is a serial console. Soldering some pins to the JTAG connector and building the EA232-compatible parallel cable also isn't hard. But the unit has an empty miniPCI slot which we must use - desoldering from a damaged Dlink AP and soldering to the PCB don't easy but possible. The case has an empty RPSMA connector place - an UFL-RPSMA pigtail solve the connection between the second Atheros a/b/g miniPCI card and the outside.The mainboard has full support for this slot, there are even an unsoldered (but working) LED on the front panel to showing card activity. The picture of the unit (click to enlarge):
  WRV54G
First of all, the GPL code are uncomplete and unuseable, there was no any piece of code that we can use. It use an old 2.4 kernel and initrd like most of the commercial AP device. There are some good information at seattlewireless about the hardware,the bootloader,etc. Two monts ago Barnabas Kalman and I started the "OpenWRV" project to yield an open-source , powerfull router/AP device based on the Intel IXP425 processor. Because the lack of the useable implementations, we choose the latest 2.6.13 kernel version and the buildroot2 environment. The unit based on the IXP425 processor - the first step register and download the  Intel Access Software Library from Intel. It is necessary because the processor has the two Network Processing Engine ( co-processors making the Ethernet ports) bult-in. Patching the kernel with the Intel code was a hard work, but this was just the beginning of the nightmare...
After the first (semi)successfull compilation we have a kernel image, but how can we use it? First of all it is necessary to build the serial interface to reach the bootloader console. The original bootloader can load images from the tftp server and start it automatically ( it seems that the bootloader have just one eth port, the internet - address 192.168.2.1). Disassembling the original code shows that the kernel image loaded and executed with the small piece of code before and after the kernel code, so we do the same. After downloading - happened nothing, no serial console. Searching for the problem ( we are at the assembly code now ) and voila: the printascii doesn't work because it has hard coded address for the serial0 and we must use the serial1. From now we can debugging, but the normal console doesn't work. Tracking the code until the kernel real start show that the code is working.Patching printk to use the assembly code output routine help to mimic the console and find the real error: changing the serial port parameters (baudrate,etc) kill the serial port. But because this is just a console instead of find the error, we just skip the port setting and everything is working - at least the kernel started.
The next step was to produce a jffs2 filesystem. Patching into he buildroot environment, we have a uClibc based linux root image. Placing it to the flash we choose that the first Mbyte occupyed by the kernel, after that there is a jffs2 image. Ok, but the bootloader make a checksum of the image in the second partition  and if changed  - because of the jffs2 write - invalidate it. Therefore first must load the kernel to the partition 2 and after that load the jfffs2 image to the same partion but with direct write to 0x240000. In this case the bootloader seems just the kernel on the partition. If you -like I am - issue a wrong number in the line  "load -u tftp://192.168.2.10/xxx.img.jffs2 -r 0x240000" there is no warning, the bootloader overwrited, the unit doesn't boot. Keep in mind that you must build the JTAG connector and first make a complete flash backup - it took hours....
Now the system starting, find the root filesystem, mounting it. The ethernet port1 (ixp1) after finding the right settings (mainly from the coyote board) and the right microcode image the internet ethernet port working. The original Prism54 card supported by the 2.6.13 kernel except the microcode - after find it we doesn't use the complicated hotpug firmware method,instead simly pass the microcode to the kernel driver. In the second minipci slot we use an Atheros 5213 a/b/g card. Because the new features the driverset downloaded from the new madwifi-ng, after some patching it is also working. The only thing remain was the first ethernet port (ixp0). This is connected to the Kendin 8995M switch controller - but with an SPI bus, so using the GPIO lines must implement the protocoll. In the implemented SPI driver the bus is reacheable over the /proc for userspace programs. After programmining the switch controller the LAN ports on the switch are reacheable, but the goal was an independent usage of the ports - therefore we must use the switch VLAN functionality. One side is OK, with vconfig is possible to create on the ixp0 interface as many VLANs as we need, but no the switch documentation nor the application notes content not working as expected - the switch can assign VLANS to the ports and working accordingly, but in this case on port 5, the port connected to the micropocessor there are no any traffic?.... The solution is to set the "special tag" mode on - in this case the switch in the VLAN header insert the port number also ( 0x810p instead of 0x8100). That way the ixp0 receive the packets but with "wrong" VLAN header, so as a quick and dirty solution in OSAL we simply masked out this byte... Making a /proc/sys/diag interface to driving the LED's after that was an easy task.
Now we have the latest 2.6.13 kernel based linux on a writeable jffs2 filesystem on a powerful machine. The netperf result for the ixp1  94 Mbps on a switched ethernet network, ixp0 (with vlan) 86.5 Mbps , the atheros card (no turbo, gmode)  24.5-25 Mbps and the average processor load in this case 15-20%!
To do:
- replace the bootloader with RedBoot
- setting kernel and jffs2 unpadded at the same image
- serialize the image - hardcoded ethernet MAC addresses
- identify and solve the serial port issues
- use the built-in hardware for the crypto devices
- decide to publish or not the code - there are several reason to be careful, the Intel code cannot be GPL'ed , patch into maybe illegal,etc.....
}}}

== related link ==
[http://www.seattlewireless.net/index.cgi/LinksysWrv54g]
----
["CategoryIXP4xxDevice"]
