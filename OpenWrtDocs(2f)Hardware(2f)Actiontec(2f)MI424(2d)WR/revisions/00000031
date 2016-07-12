#pragma section-numbers off
[[TableOfContents]]

= Actiontec MI424-WR Overview =
The [http://www.actiontec.com Actiontec] MI424-WR router is based on a 533MHz IXP425. It has 32MB RAM and 8MB of FLASH. It has 4 external LAN ports connected to a switch and 1 WAN port. It has a coax interface and IEEE 802.11g support. Some pictures of the unit and the various revisions can be found here: http://en.wikipedia.org/wiki/MI424WR.

== Hardware ==
 * NPEB - WAN interface with separate Micrel KS8721 PHY; PHY address: 17.
 * NPEC - LAN interface connected to Micrel KSZ8995MA switch via SPI; PHY addresses: 1, 2, 3, 4.
 * 3 PCI slots - 2 used for coax interface.
 * Wireless MiniPCI based on RA2560.
There are also two [http://www.entropic.com/products/homenetworking.htm Entropic] [http://www.mocalliance.org MoCA] controllers for the coax interface. Because of the proprietary nature of these devices, they are not supported.

=== GPIO ===
||'''Pin''' ||'''I/O''' ||'''Description''' ||
||<style="text-align: right;">0 ||<style="text-align: center;">O ||HW Reset ||
||<style="text-align: right;">2 ||<style="text-align: center;">O ||SPI CLK ||
||<style="text-align: right;">3 ||<style="text-align: center;">I ||SPI RxD ||
||<style="text-align: right;">4 ||<style="text-align: center;">O ||SPI TxD ||
||<style="text-align: right;">6 ||<style="text-align: center;">I ||PCI INTA (MoCA WAN) ||
||<style="text-align: right;">7 ||<style="text-align: center;">I ||PCI INTB (Mini-PCI) ||
||<style="text-align: right;">8 ||<style="text-align: center;">I ||PCI INTC (MoCA LAN) ||
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
There's an internal serial port available on the J20 pins. It's found on the side. It's possible to connect a TTL 3.3V serial converter (e.g. [http://www.sparkfun.com/commerce/product_info.php?products_id=8772 this]) and have access to the console for both redboot and linux.
||'''Pin''' ||'''Function''' ||
||<style="text-align: right;">1 ||Gnd ||
||<style="text-align: right;">2 ||Tx ||
||<style="text-align: right;">3 ||Rx ||
||<style="text-align: right;">4 ||? ||
||<style="text-align: right;">5 ||? ||
||<style="text-align: right;">6 ||? ||


== Software ==
=== Redboot ===
A custom version of redboot has been built and can be found here: attachment:redboot.bin . The redboot prompt is accessible via {{{telnet 192.168.1.1 9000}}} on the Wan port. The Wan port is configured to obtain an address via DHCP; if this fails it defaults to 192.168.1.1. Note that there's a feature that allows skipping the redboot boot script by pressing the "Reset" button after power on for about 10 seconds. When redboot is ready to accept commands, it sets the Internet LED red.

Installation of redboot can be accomplished with the attachment:jungo-image.py script. It requires that a tftp server that can serve the {{{redboot.bin}}}. The script uses the telnet interface into the router to accomplish it's task. Depending on the version of the firmware, it may have to be manually enabled in the advanced tab under local adminstration. The script will first make a backup of the current flash image; this procedure takes about 4 minutes. The actual writing of redboot requires the {{{-w}}} flag. Use {{{-h}}} to get help on all the options. If there's some failure, the only recourse is to install a JTAG header and restore the firmware via JTAG.

After establishing a telnet session to redboot, the flash must be initialized and configured:

 1. Initialize flash -- {{{fis init}}}
 1. Configure MAC addresses -- {{{fconfig npe_eth0_esa 0x00:0x01:0x02:0x03:0x04:0x05}}}. Use MAC address at the bottom of the unit!
 1. Write attachment:openwrt-mi424wr-zImage image to flash {{{load -r -b %{FREEMEMLO} -h <hostip> openwrt-mi424wr-zImage}}} followed by {{{fis create linux}}}
 1. Write attachment:openwrt-mi424wr-squashfs.img to flash {{{load -r -b %{FREEMEMLO} -h <hostip> openwrt-mi424wr-squashfs.img}}} followed by {{{fis create rootfs}}}
The original image can be restored using the following procedure:

 1. Get a copy of attachment:redram.img .
 1. {{{load -h <ipaddress> redram.img}}}
 1. {{{go}}}
 1. Close telnet session and start another one. Verify that RAM version is running with {{{version}}} command.
 1. {{{load -h <ipaddress> -r -b %{FREEMEMLO} mi424wr-xxxxxxxxxxxx.bin}}}
 1. {{{fis unlock -f 0x50000000 -l 0x800000}}}
 1. {{{fis write -b %{FREEMEMLO} -l 0x800000 -f 0x50000000}}}
 1. Close telnet session and power cycle.
==== Building RedBoot ====
Redboot can be built from the Intel Redboot sources found in the [http://www.intel.com/design/network/products/npfamily/download_ixp400.htm Intel IXP400 Software] site. You'll need the RedBoot source code as well as the RedBoot NPE microcode. This attachment:mi424wr.epk adds support for the MI424-WR. The procedure for building redboot is as follows:

1. {{{export ECOS_REPOSTIORY=/path/to/ecos/packages}}} 2. {{{cd ${ECOS_REPOSITORY}; ./ecosadmin.tcl add mi424wr.epk}}} 3. {{{cd <build_dir>; ecosconfig new mi424wr_npe redboot}}} 4. {{{ecosconfig add memalloc io fileio error linux_compat kernel crc zlib}}} 5. {{{ecosconfig import ${ECOS_REPOSITORY}/hal/arm/xscale/mi424wr/current/misc/redboot_ROM.ecm}}} 6. {{{ecosconfig tree}}} 7. {{{make}}}

The {{{redboot.bin}}} image can be fond in the {{{install/bin}}} direcoctory.

=== Linux ===
Board id 1778 has been registered for this device. The attached MI424-WR images have been built from the OpenWrt trunk with various patches and tweaks.Patches supporting the MI424-WR have been submitted to the OpenWrt development [http://lists.openwrt.org/cgi-bin/mailman/listinfo/openwrt-devel list]; hopefully, they will be merged into the trunk soon. It should be noted that the wifi rt2500pci drivers are built from the kernel sources and not the mac80211 (compat-wireless) package. The mac80211 is old and doesn't work at all with the rt2500pci device. The kernel version works well in client mode but master mode is buggy and causes duplicate packets to be sent.

Here's a boot log generated by dmesg:

{{{
BusyBox v1.11.2 (2008-11-01 10:30:08 EDT) built-in shell (ash)
Enter 'help' for a list of built-in commands.
  _______                     ________        __
 |       |.-----.-----.-----.|  |  |  |.----.|  |_
 |   -   ||  _  |  -__|     ||  |  |  ||   _||   _|
 |_______||   __|_____|__|__||________||__|  |____|
          |__| W I R E L E S S   F R E E D O M
 KAMIKAZE (bleeding edge, r13088) -------------------
  * 10 oz Vodka       Shake well with ice and strain
  * 10 oz Triple sec  mixture into 10 shot glasses.
  * 10 oz lime juice  Salute!
 ---------------------------------------------------
root@OpenWrt:/# cd
root@OpenWrt:~# dmesg
Linux version 2.6.26.7 (jose@chessmaster) (gcc version 4.2.4) #9 Sat Nov 1 11:27:34 EDT 2008
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
Memory: 30548KB available (1672K code, 145K data, 76K init)
SLUB: Genslabs=12, HWalign=32, Order=0-3, MinObjects=0, CPUs=1, Nodes=1
Calibrating delay loop... 532.48 BogoMIPS (lpj=2662400)
Mount-cache hash table entries: 512
CPU: Testing write buffer coherency: ok
net_namespace: 480 bytes
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
0x00000000-0x00060000 : "RedBoot"
0x00060000-0x00180000 : "linux"
0x00180000-0x007e0000 : "rootfs"
mtd: partition "rootfs" set to be root filesystem
mtd: partition "rootfs_data" created automatically, ofs=420000, len=3C0000
0x00420000-0x007e0000 : "rootfs_data"
0x007e0000-0x007ff000 : "FIS directory"
mtd: partition "FIS directory" doesn't end on an erase block -- force read-only
0x007ff000-0x00800000 : "RedBoot config"
mtd: partition "RedBoot config" doesn't start on an erase block boundary -- force read-only
IXP4xx Watchdog Timer: heartbeat 60 sec
Registered led device: moca-wan
Registered led device: power-alarm
Registered led device: power-ok
Registered led device: wireless
Registered led device: inet-down
Registered led device: inet-up
Registered led device: moca-lan
Registered led device: wan-alarm
TCP westwood registered
NET: Registered protocol family 17
802.1Q VLAN Support v1.8 Ben Greear <greearb@candelatech.com>
All bugs added by David S. Miller <davem@redhat.com>
XScale DSP coprocessor detected.
VFS: Mounted root (squashfs filesystem) readonly.
Freeing init memory: 76K
Please be patient, while OpenWrt loads ...
mini_fo: using base directory: /
mini_fo: using storage directory: /tmp/root
firmware: requesting NPE-C
NPE-C: firmware's license can be found in /usr/share/doc/LICENSE.IPL
NPE-C: firmware functionality 0x5, revision 0x2:1
eth0: link down
firmware: requesting NPE-B
NPE-B: firmware's license can be found in /usr/share/doc/LICENSE.IPL
NPE-B: firmware functionality 0x2, revision 0x2:1
eth1: link down
PCI: enabling device 0000:00:0e.0 (0140 -> 0142)
phy0: Selected rate control algorithm 'pid'
Registered led device: rt2500pci-phy0:radio
PPP generic driver version 2.4.2
tun: Universal TUN/TAP device driver, 1.6
tun: (C) 1999-2004 Max Krasnyansky <maxk@qualcomm.com>
ip_tables: (C) 2000-2006 Netfilter Core Team
eth0: link up
nf_conntrack version 0.5.0 (1024 buckets, 4096 max)
Micrel/Kendin KS8995 Ethernet switch SPI driver version 0.1.1
spi-ks8995 spi32766.0: KS8995 device found, Chip ID:0, Revision:3
jffs2_scan_eraseblock(): End of filesystem marker found at 0x0
jffs2_build_filesystem(): unlocking the mtd device... done.
jffs2_build_filesystem(): erasing all blocks after the end marker... done.
mini_fo: using base directory: /
mini_fo: using storage directory: /jffs
root@OpenWrt:~# ifconfig
eth0      Link encap:Ethernet  HWaddr 00:0F:B3:E5:26:E6
          inet addr:192.168.2.1  Bcast:192.168.2.255  Mask:255.255.255.0
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:1483 errors:0 dropped:0 overruns:0 frame:0
          TX packets:1470 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:100
          RX bytes:134732 (131.5 KiB)  TX bytes:1296736 (1.2 MiB)
eth1      Link encap:Ethernet  HWaddr 00:0F:B3:E5:26:E7
          inet addr:192.168.1.1  Bcast:192.168.1.255  Mask:255.255.255.0
          UP BROADCAST MULTICAST  MTU:1500  Metric:1
          RX packets:2 errors:0 dropped:0 overruns:0 frame:0
          TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:100
          RX bytes:100 (100.0 B)  TX bytes:0 (0.0 B)
lo        Link encap:Local Loopback
          inet addr:127.0.0.1  Mask:255.0.0.0
          UP LOOPBACK RUNNING  MTU:16436  Metric:1
          RX packets:2 errors:0 dropped:0 overruns:0 frame:0
          TX packets:2 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0
          RX bytes:136 (136.0 B)  TX bytes:136 (136.0 B)
mon.wlan0 Link encap:UNSPEC  HWaddr 00-15-05-EE-67-08-00-00-00-00-00-00-00-00-00-00
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)
wlan0     Link encap:Ethernet  HWaddr 00:15:05:EE:67:08
          inet addr:192.168.3.1  Bcast:192.168.3.255  Mask:255.255.255.0
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)
wmaster0  Link encap:UNSPEC  HWaddr 00-15-05-EE-67-08-00-00-00-00-00-00-00-00-00-00
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)
root@OpenWrt:~# iwconfig wlan0
wlan0     IEEE 802.11  ESSID:"OpenWrt"
          Mode:Master  Frequency:2.432 GHz  Tx-Power=26 dBm
          Retry min limit:7   RTS thr:off   Fragment thr=2352 B
          Encryption key:off
          Link Quality:0  Signal level:0  Noise level:0
          Rx invalid nwid:0  Rx invalid crypt:0  Rx invalid frag:0
          Tx excessive retries:0  Invalid misc:0   Missed beacon:0
root@OpenWrt:~#
}}}
=== TODO ===
 * Debug ap (master) mode for rt2500 driver.
----
 . CategoryModel ["CategoryIXP4xxDevice"]
