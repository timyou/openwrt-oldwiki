#pragma section-numbers off
[[TableOfContents]]

= Actiontec MI424-WR Overview =
The [http://www.actiontec.com Actiontec] MI424-WR router is based on a 533MHz IXP425. It has 32MB RAM and 8MB of FLASH. It has 4 external LAN ports and 1 WAN port. It has a coax interface and IEEE 802.11g support. Some pictures of the unit and the various revisions can be found here: http://en.wikipedia.org/wiki/MI424WR.

== Hardware ==
 * NPEB - WAN interface with separate Micrel KS8721 PHY; PHY address: 17.
 * NPEC - LAN interface connected to Micrel KSZ8995MA switch via SPI; PHY addresses: 1, 2, 3, 4.
 * 3 PCI slots - 2 used for coax interface.
 * Wireless MiniPCI based on RA2560.

There are also two [http://www.entropic.com/products/homenetworking.htm Entropic] [http://www.mocalliance.org MoCA] controllers for the coax interface. Because of the proprietary nature of these devices, they are not supported.
=== GPIO ===
||'''Pin''' ||'''I/O''' ||'''Description''' ||
||<style="text-align: right;">0 ||<style="text-align: center;">O ||Reset? ||
||<style="text-align: right;">2 ||<style="text-align: center;">O ||SPI CLK ||
||<style="text-align: right;">3 ||<style="text-align: center;">I ||SPI RxD ||
||<style="text-align: right;">4 ||<style="text-align: center;">O ||SPI TxD ||
||<style="text-align: right;">6 ||<style="text-align: center;">I ||PCI INTA (MoCA WAN) ||
||<style="text-align: right;">7 ||<style="text-align: center;">I ||PCI INTB (MoCA LAN) ||
||<style="text-align: right;">8 ||<style="text-align: center;">I ||PCI INTC (Mini-PCI) ||
||<style="text-align: right;">9 ||<style="text-align: center;">O ||SPI CS ||
||<style="text-align: right;">10 ||<style="text-align: center;">I ||Button ||
||<style="text-align: right;">11 ||<style="text-align: center;">O ||MoCA WAN LED ||
||<style="text-align: right;">14 ||<style="text-align: center;">O ||PCI CLK Pin ||
=== Latch ===
There's a latch accessible via CS1 that is 16-bits wide.
||'''Bit''' ||'''Function''' ||
||<style="text-align: right;">0 ||Power alarm (red) ||
||<style="text-align: right;">1 ||Power ||
||<style="text-align: right;">2 ||Wireless ||
||<style="text-align: right;">3 ||Internet alarm (red) ||
||<style="text-align: right;">4 ||Internet active ||
||<style="text-align: right;">5 ||MoCA LAN ||
||<style="text-align: right;">6 ||MoCA WAN alarm (red) ||
||<style="text-align: right;">7 ||PCI reset ||

=== Serial Port ===
There's an internal serial port available on the J20 pins. It's found on the side.
It's possible to connect a TTL 3.3V serial converter
(e.g. [http://www.sparkfun.com/commerce/product_info.php?products_id=8772 this])
and have access to the console for both redboot and linux.
||'''Pin''' ||'''Function''' ||
||<style="text-align: right;">1 ||Gnd ||
||<style="text-align: right;">2 ||Tx ||
||<style="text-align: right;">3 ||Rx ||
||<style="text-align: right;">4 ||? ||
||<style="text-align: right;">5 ||? ||
||<style="text-align: right;">6 ||? ||

== Software ==
=== Redboot ===
A custom version of redboot has been built and can be found [http://mysite.verizon.net/jvasco/mi424wr/redboot.bin here]. The redboot prompt is accessible via {{{telnet 192.168.1.1 9000}}} on the Wan port. The Wan port is configured to obtain an address via DHCP; if this fails it defaults to 192.168.1.1. Note that there's a feature that allows skipping the redboot boot script by pressing the "Reset" button after power on for about 10 seconds. When redboot is ready to accept commands, it sets the Internet LED red.

Installation of redboot can be accomplished with the [http://mysite.verizon.net/jvasco/mi424wr/mi424wr-image.py mi424wr-image.py] script. It requires that a tftp server that can serve the {{{redboot.bin}}}. The script uses the telnet interface into the router to accomplish it's task. Depending on the version of the firmware, it may have to be manually enabled in the advanced tab under local adminstration. The script will first make a backup of the current flash image; this procedure takes about 4 minutes.
The actual writing of redboot requires the {{{-w}}} flag. Use {{{-h}}} to get help on all the options.
If there's some failure, the only recourse is to install a JTAG header and restore the firmware via JTAG.

After establishing a telnet session to redboot, the flash must be initialized and configured:

 1. Initialize flash -- {{{fis init}}}
 2. Configure MAC addresses -- {{{fconfig npe_eth0_esa 0x00:0x01:0x02:0x03:0x04:0x05}}}. Use MAC address at the bottom of the unit!
 3. Write [http://mysite.verizon.net/jvasco/mi424wr/openwrt-ixp4xx-zImage linux] image to flash -- {{{load -r -b %{FREEMEMLO} -h <hostip> openwrt-ixp4xx-zImage}}} followed by {{{fis create linux}}}
 4. Write [http://mysite.verizon.net/jvasco/mi424wr/openwrt-ixp4xx-squashfs.img rootfs] to flash -- {{{load -r -b %{FREEMEMLO} -h <hostip> openwrt-ixp4xx-squashfs.img}}} followed by {{{fis create rootfs}}}

The original image can be restored using the following procedure:

 1. Get a copy of [http://mysite.verizon.net/jvasco/mi424wr/redram.img redram.img].
 2. {{{load -h <ipaddress> redram.img}}}
 3. {{{go}}}
 4. Close telnet session and start another one.
 5. {{{load -h <ipaddress> -r -b %{FREEMEMLO} mi424wr-xxxxxxxxxxxx.bin}}}
 6. {{{fis unlock -f 0x50000000 -l 0x800000}}}
 7. {{{fis write -b %{FREEMEMLO} -l 0x800000 -f 0x50000000}}}
 8. Close telnet session and power cycle.

=== Linux ===
Board id 1778 has been registered for this device. When building OpenWrt from source, you'll need the MI424-WR patch that can be found [http://mysite.verizon.net/jvasco/mi424wr/333-mi424wr_support.patch here] and should be copied to the {{{target/linux/ixp4xx/patches/2.6.26}}} directory. Also, make sure to add the spi-ks8995 kernel module to enable the switch.

Here's a boot log generated by dmesg:

{{{
 === IMPORTANT ============================
  Use 'passwd' to set your login password
  this will disable telnet and enable SSH
 ------------------------------------------


BusyBox v1.11.1 (2008-09-05 17:39:41 EDT) built-in shell (ash)
Enter 'help' for a list of built-in commands.

  _______                     ________        __
 |       |.-----.-----.-----.|  |  |  |.----.|  |_
 |   -   ||  _  |  -__|     ||  |  |  ||   _||   _|
 |_______||   __|_____|__|__||________||__|  |____|
          |__| W I R E L E S S   F R E E D O M
 KAMIKAZE (bleeding edge, r12561) -------------------
  * 10 oz Vodka       Shake well with ice and strain
  * 10 oz Triple sec  mixture into 10 shot glasses.
  * 10 oz lime juice  Salute!
 ---------------------------------------------------
root@OpenWrt:/# dmesg
Linux version 2.6.26.3 (jose@chessmaster) (gcc version 4.2.4) #10 Tue Sep 9 21:11:42 EDT 2008
CPU: XScale-IXP42x Family [690541c1] revision 1 (ARMv5TE), cr=000039ff
Machine: Actiontec MI424WR
Memory policy: ECC disabled, Data cache writeback
On node 0 totalpages: 8192
  DMA zone: 64 pages used for memmap
  DMA zone: 0 pages reserved
  DMA zone: 8128 pages, LIFO batch:0
  Normal zone: 0 pages used for memmap
  Movable zone: 0 pages used for memmap
CPU0: D VIVT undefined 5 cache
CPU0: I cache: 32768 bytes, associativity 32, 32 byte lines, 32 sets
CPU0: D cache: 32768 bytes, associativity 32, 32 byte lines, 32 sets
Built 1 zonelists in Zone order, mobility grouping on.  Total pages: 8128
Kernel command line: root=/dev/mtdblock2 rootfstype=squashfs,jffs2 noinitrd console=ttyS0,115200 init=/etc/preinit
PID hash table entries: 128 (order: 7, 512 bytes)
Dentry cache hash table entries: 4096 (order: 2, 16384 bytes)
Inode-cache hash table entries: 2048 (order: 1, 8192 bytes)
Memory: 32MB = 32MB total
Memory: 30348KB available (1848K code, 163K data, 88K init)
SLUB: Genslabs=12, HWalign=32, Order=0-3, MinObjects=0, CPUs=1, Nodes=1
Calibrating delay loop... 532.48 BogoMIPS (lpj=2662400)
Mount-cache hash table entries: 512
CPU: Testing write buffer coherency: ok
net_namespace: 640 bytes
NET: Registered protocol family 16
IXP4xx: Using 16MiB expansion bus window size
PCI: IXP4xx is host
PCI: IXP4xx Using direct access for memory space
PCI: bus0: Fast back to back transfers disabled
dmabounce: registered device 0000:00:0d.0 on pci bus
dmabounce: registered device 0000:00:0d.1 on pci bus
dmabounce: registered device 0000:00:0e.0 on pci bus
dmabounce: registered device 0000:00:0f.0 on pci bus
dmabounce: registered device 0000:00:0f.1 on pci bus
mi424wr_map_irq: Mapped slot 13 pin 1 to IRQ -1
mi424wr_map_irq: Mapped slot 13 pin 2 to IRQ -1
mi424wr_map_irq: Mapped slot 14 pin 1 to IRQ 25
mi424wr_map_irq: Mapped slot 15 pin 1 to IRQ -1
mi424wr_map_irq: Mapped slot 15 pin 2 to IRQ -1
NET: Registered protocol family 2
Switched to high resolution mode on CPU 0
IP route cache hash table entries: 1024 (order: 0, 4096 bytes)
TCP established hash table entries: 1024 (order: 1, 8192 bytes)
TCP bind hash table entries: 1024 (order: 0, 4096 bytes)
TCP: Hash tables configured (established 1024 bind 1024)
TCP reno registered
NET: Registered protocol family 1
IXP4xx Queue Manager initialized.
squashfs: version 3.0 (2006/03/15) Phillip Lougher
Registering mini_fo version $Id$
JFFS2 version 2.2. (NAND) (SUMMARY)  © 2001-2006 Red Hat, Inc.
msgmni has been set to 59
io scheduler noop registered
io scheduler deadline registered (default)
Serial: 8250/16550 driver $Revision: 1.90 $ 2 ports, IRQ sharing disabled
serial8250.0: ttyS0 at MMIO 0xc8000000 (irq = 15) is a XScale
console [ttyS0] enabled
serial8250.0: ttyS1 at MMIO 0xc8001000 (irq = 13) is a XScale
eth0: MII PHY 1 on NPE-C
eth0: MII PHY 2 on NPE-C
eth0: MII PHY 3 on NPE-C
eth0: MII PHY 4 on NPE-C
eth1: MII PHY 17 on NPE-B
IXP4XX-Flash.0: Found 1 x16 devices at 0x0 in 16-bit bank
 Intel/Sharp Extended Query Table at 0x0031
Using buffer write method
cfi_cmdset_0001: Erase suspend on write enabled
erase region 0: offset=0x0,size=0x20000,blocks=64
Searching for RedBoot partition table in IXP4XX-Flash.0 at offset 0x7e0000
5 RedBoot partitions found on MTD device IXP4XX-Flash.0
Creating 5 MTD partitions on "IXP4XX-Flash.0":
0x00000000-0x00080000 : "RedBoot"
0x00080000-0x00180000 : "linux"
0x00180000-0x007e0000 : "rootfs"
mtd: partition "rootfs" set to be root filesystem
mtd: partition "rootfs_data" created automatically, ofs=3E0000, len=400000
0x003e0000-0x007e0000 : "rootfs_data"
0x007e0000-0x007ff000 : "FIS directory"
0x007ff000-0x00800000 : "RedBoot config"
IXP4xx Watchdog Timer: heartbeat 60 sec
Registered led device: moca-wan
firmware: requesting NPE-C
nf_conntrack version 0.5.0 (1024 buckets, 4096 max)
ip_tables: (C) 2000-2006 Netfilter Core Team
TCP westwood registered
NET: Registered protocol family 17
802.1Q VLAN Support v1.8 Ben Greear <greearb@candelatech.com>
All bugs added by David S. Miller <davem@redhat.com>
XScale DSP coprocessor detected.
VFS: Mounted root (squashfs filesystem) readonly.
Freeing init memory: 88K
Please be patient, while OpenWrt loads ...
mini_fo: using base directory: /
mini_fo: using storage directory: /jffs
firmware: requesting NPE-C
NPE-C: firmware's license can be found in /usr/share/doc/LICENSE.IPL
NPE-C: firmware functionality 0x5, revision 0x2:1
eth0: link down
firmware: requesting NPE-B
NPE-B: firmware's license can be found in /usr/share/doc/LICENSE.IPL
NPE-B: firmware functionality 0x2, revision 0x2:1
eth1: link down
NET: Registered protocol family 10
lo: Disabled Privacy Extensions
ADDRCONF(NETDEV_UP): eth0: link is not ready
ADDRCONF(NETDEV_UP): eth1: link is not ready
PPP generic driver version 2.4.2
tun: Universal TUN/TAP device driver, 1.6
tun: (C) 1999-2004 Max Krasnyansky <maxk@qualcomm.com>
ipt_time loading
Micrel/Kendin KS8995 Ethernet switch SPI driver version 0.1.1
spi-ks8995 spi32766.0: KS8995 device found, Chip ID:0, Revision:3
eth0: link up
ADDRCONF(NETDEV_CHANGE): eth0: link becomes ready
eth1: link up, 100Mbps, full-duplex, lpa 0x45E1
ADDRCONF(NETDEV_CHANGE): eth1: link becomes ready
eth0: no IPv6 routers present
eth1: no IPv6 routers present
root@OpenWrt:/#
}}}
=== TODO ===
 * Add latched led driver.
 * Debug RA2500 driver.
----
 . CategoryModel ["CategoryIXP4xxDevice"]
