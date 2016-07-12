## Please add only OpenWrt and WRT350N related things to this page! Thanks.
'''Linksys WRT350N'''

'''Identification by S/N'''

Useful for identifying shrinkwrapped units. The '''S/N''' can be found on the box, below the UPC barcode.
||||<style="text-align: center;"> (!) '''Please contribute to this list.''' (!) ||
||||<style="text-align: center;">'''Model''' ||<style="text-align: center;"> '''S/N''' ||
||||<style="text-align: center;">WRT350N v1.0 -- Not available in Europe? ||<style="text-align: center;"> CNQ01 ||
||||<style="text-align: center;">WRT350N v2.0 -- Only available in Europe? ||<style="text-align: center;"> SNQ00 ||


'''WRT350N v1.0'''

The WRT350N v1.0 is based on the Broadcom 4785 r2 running at 300MHz cpu. It has 8 MB flash and 32 MB SDRAM. The wireless NIC is a Broadcom Cardbus card with maybe a BCM5397 Chipset on the switch.  The WRT350N runs 802.11 B, G, and Draft N wireless protocols. It provides 4 gigabit LAN ports, 1 WAN port and a USB 'storage link' port.

--(OpenWRT runs on the v1.0, but currently the switch is unsupported.  This means you must have a serial console installed to access the device.  Work is being done to support the switch in kamikaze 2.4, which will hopefully be added soon.)--

Support for the wrt350n v1.0 was added to SVN with changesets 11466-11471 (broadcom 2.4 build).  In order to use the device, make sure the bcm57xx package is included in your image (selected as * in menuconfig).  Without this package installed, the switch will not come up and you'll have to use a serial console to recover.

Wireless works as long as kmod-brcm-wl-mimo is installed.  USB also works with kmod-usb-ohci, I have tested it as a print server with p9100d.

A note about NVRAM

The switch in the wrt350n v1 is a little different from the older switch chips.  By default, it will forward packets between the LAN and WAN, much like a normal switch.  This is a problem during bootup because boot_wait will activate the switch to wait for an image.  The only way I could find to make the switch not forward packets on bootup was to set the following NVRAM variables:

''Disabling boot_wait is a bad idea, so make sure you really need it off before doing so.''
{{{
nvram set boot_wait=off
nvram set manual_boot_nv=1
nvram unset disabled_57xx
nvram commit
}}}


'''WRT350N v2.0'''

The WRT350N v2.0 is based on the Marvell 88F5181 running at 500MHz cpu. It has 8MB flash and --(16MB)-- 32MB SDRAM. The wireless NIC is an Atheros AR5416 (AR5008 family) Mini-PCI card. The WRT350N runs 802.11 B, G, and Draft N wireless protocols. It provides 4 gigabit LAN ports, 1 WAN port and a USB 'storage link' port.

--(There seems to be another version of WRT350N v2 based on ARM926EJ running at 333MHz and with  32MB SDRAM.)-- Not so, when looking at /proc/cpuinfo 333 BogoMIPS are reported. This does not, however, mean that it runs at 333MHz. All WRT350N V2's seem to run at 500 MHz.

OpenWRT support for the WRT350N V2 is coming along well, for the latest information see this thread: http://forum.openwrt.org/viewtopic.php?id=12358

'''''Information'''''

serial is on  JP5  with 115200 8N1

 . | ground | TX | RX | 3.3V |
{{{
~ # cat /proc/version
Linux version 2.6.12-arm1 (root@davidnb-gentoo) (gcc version 3.4.4 (release) (CodeSourcery ARM 2005q3-2)) #1 Fri Jan 25 21:35:35 CET 2008
}}}
{{{
~ # cat /proc/cpuinfo
Processor       : ARM926EJ-Sid(wb) rev 0 (v5l)
BogoMIPS        : 331.77
Features        : swp half thumb fastmult edsp java
CPU implementer : 0x41
CPU architecture: 5TEJ
CPU variant     : 0x0
CPU part        : 0x926
CPU revision    : 0
Cache type      : write-back
Cache clean     : cp15 c7 ops
Cache lockdown  : format C
Cache format    : Harvard
I size          : 32768
I assoc         : 1
I line length   : 32
I sets          : 1024
D size          : 32768
D assoc         : 1
D line length   : 32
D sets          : 1024
Hardware        : MV-88fxx81
Revision        : 0000
Serial          : 0000000000000000
}}}
{{{
~ # cat /proc/mtd
dev:    size   erasesize  name
mtd0: 00760000 00010000 "kernel"
mtd1: 005c0000 00010000 "rootfs"
mtd2: 00040000 00010000 "lang"
mtd3: 00020000 00010000 "nvram"
mtd4: 00040000 00010000 "u-boot"
}}}
{{{
~ # cat /proc/modules
wsc_daemon 2208 0 - Live 0xbf0ef000
wlan_wep 5888 1 - Live 0xbf0ec000
ath_pci 138064 0 - Live 0xbf0c9000
ath_dfs 25772 1 ath_pci, Live 0xbf0c1000
ath_rate_atheros 28612 1 ath_pci, Live 0xbf0b9000
wlan 207016 4 wlan_wep,ath_pci,ath_rate_atheros, Live 0xbf085000
ath_hal 183152 3 ath_pci,ath_rate_atheros, Live 0xbf057000
kwsc_mod 24456 2 wsc_daemon,wlan, Live 0xbf050000
ufsd 292976 0 - Live 0xbf007000
ipt_webstr 3712 0 - Live 0xbf005000
pb 3876 2 - Live 0xbf003000
led 5044 0 - Live 0xbf000000
}}}
{{{
~ # cat /proc/devices
Character devices:
  1 mem
  2 pty
  3 ttyp
  4 /dev/vc/0
  4 tty
  4 ttyS
  5 /dev/tty
  5 /dev/console
  5 /dev/ptmx
  7 vcs
 10 misc
 13 input
 90 mtd
108 ppp
128 ptm
136 pts
180 usb
254 pcmcia
Block devices:
  7 loop
  8 sd
 31 mtdblock
 65 sd
 66 sd
 67 sd
 68 sd
 69 sd
 70 sd
 71 sd
128 sd
129 sd
130 sd
131 sd
132 sd
133 sd
134 sd
135 sd
}}}
{{{
~ # free
              total         used         free       shared      buffers
  Mem:        29036        19068         9968            0         1628
 Swap:            0            0            0
Total:        29036        19068         9968
}}}
{{{
~ # cat /proc/meminfo
MemTotal:        29036 kB
MemFree:          9956 kB
Buffers:          1628 kB
Cached:           7876 kB
SwapCached:          0 kB
Active:           5212 kB
Inactive:         6052 kB
HighTotal:           0 kB
HighFree:            0 kB
LowTotal:        29036 kB
LowFree:          9956 kB
SwapTotal:           0 kB
SwapFree:            0 kB
Dirty:               0 kB
Writeback:           0 kB
Mapped:           2944 kB
Slab:             5116 kB
CommitLimit:     14516 kB
Committed_AS:     4576 kB
PageTables:        304 kB
VmallocTotal:   483328 kB
VmallocUsed:      8644 kB
VmallocChunk:   474620 kB
}}}
{{{
~ # cat /proc/iomem
00000000-01ffffff : System RAM
  00021000-002911df : Kernel text
  00292000-0036d41b : Kernel data
e0000000-e7ffffff : PCI Memory Primary
e8000000-efffffff : PCI Memory Primary
  e8000000-e800ffff : 0000:01:07.0
    e8000000-e800ffff : ath
f4000000-f47fffff : flashMap
}}}
{{{
~ # ps
  PID  Uid     VmSize Stat Command
    1 root        308 S   init
    2 root            SWN [ksoftirqd/0]
    3 root            SW< [events/0]
    4 root            SW< [khelper]
    5 root            SW< [kthread]
   11 root            SW< [kblockd/0]
   14 root            SW  [khubd]
   60 root            SW  [pdflush]
   61 root            SW  [pdflush]
   63 root            SW< [aio/0]
  185 root            SW  [mtdblockd]
   62 root            SW  [kswapd0]
  233 root        200 S   /usr/sbin/pb_ap
  249 root        276 S   /sbin/klogd
  322 root        300 S   /sbin/syslogd -f /tmp/syslog.conf -R 192.168.1.100:51
  334 root        220 S   /usr/sbin/ntp -z GMT+1 2 -s 1
  339 root        192 S   /usr/sbin/scfgmgr
  342 root        212 S   /usr/sbin/wps_ap
  345 root        432 S   /usr/sbin/mini_httpd -d /tmp/www -r Linksys WRT350N -
  373 root        772 S   /usr/sbin/hostapd -B /tmp/madwifi.conf
  385 root        244 S   /usr/sbin/udhcpc -i eth1 -s /etc/udhcpc.script
  387 root        232 S   /usr/sbin/cmd_agent
  390 root        184 S   /usr/sbin/cmd_agent1
  392 root        208 S   /usr/sbin/download
  393 root        212 S   /usr/sbin/wizard
  409 root        324 S   /usr/sbin/lld2 br0 ath0
  420 root        220 S   /usr/sbin/usbdect
  437 root        600 S   /usr/sbin/wscupnpd br0 ath0 30 4
  439 root        600 S   /usr/sbin/wscupnpd br0 ath0 30 4
  440 root        600 S   /usr/sbin/wscupnpd br0 ath0 30 4
  442 root        600 S   /usr/sbin/wscupnpd br0 ath0 30 4
  444 root        600 S   /usr/sbin/wscupnpd br0 ath0 30 4
  445 root        600 S   /usr/sbin/wscupnpd br0 ath0 30 4
  454 root        600 R   /usr/sbin/wscupnpd br0 ath0 30 4
  463 root        668 S   /usr/sbin/upnpd eth1 br0 30 4
  465 root        668 S   /usr/sbin/upnpd eth1 br0 30 4
  466 root        668 S   /usr/sbin/upnpd eth1 br0 30 4
  468 root        668 S   /usr/sbin/upnpd eth1 br0 30 4
  470 root        668 S   /usr/sbin/upnpd eth1 br0 30 4
  471 root        668 S   /usr/sbin/upnpd eth1 br0 30 4
  486 root        668 S   /usr/sbin/upnpd eth1 br0 30 4
  491 root        296 R   /usr/sbin/telnetd -p 33
  492 root        308 S   init
  550 root        464 S   /bin/sh
  555 root        348 R   ps
}}}
{{{
~ # ifconfig
ath0      Link encap:Ethernet  HWaddr 00:1A:70:A1:C3:8C
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:3891045 errors:0 dropped:0 overruns:0 frame:0
          TX packets:4318909 errors:0 dropped:128 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:467565175 (445.9 MiB)  TX bytes:717290129 (684.0 MiB)
br0       Link encap:Ethernet  HWaddr 00:1A:70:A1:C3:8C
          inet addr:192.168.0.90  Bcast:192.168.0.255  Mask:255.255.255.0
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:47383 errors:0 dropped:0 overruns:0 frame:0
          TX packets:20253 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0
          RX bytes:9866347 (9.4 MiB)  TX bytes:4722786 (4.5 MiB)
eth0      Link encap:Ethernet  HWaddr 00:1A:70:A1:C3:8C
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:4315667 errors:0 dropped:0 overruns:0 frame:0
          TX packets:3907574 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:759378372 (724.1 MiB)  TX bytes:472106949 (450.2 MiB)
          Interrupt:21
eth1      Link encap:Ethernet  HWaddr 00:1A:70:A1:C3:8D
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:17196 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:512
          RX bytes:0 (0.0 B)  TX bytes:10145640 (9.6 MiB)
          Interrupt:21
lo        Link encap:Local Loopback
          inet addr:127.0.0.1  Mask:255.0.0.0
          UP LOOPBACK RUNNING  MTU:16436  Metric:1
          RX packets:72 errors:0 dropped:0 overruns:0 frame:0
          TX packets:72 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0
          RX bytes:17792 (17.3 KiB)  TX bytes:17792 (17.3 KiB)
wifi0     Link encap:Ethernet  HWaddr 00:1A:70:A1:C3:8C
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:4263539 errors:0 dropped:0 overruns:0 frame:40765
          TX packets:4639042 errors:129 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:605802378 (577.7 MiB)  TX bytes:881407527 (840.5 MiB)
          Interrupt:36 Memory:c2860000-c2870000
}}}
{{{
~ # dmesg -s 65535
Linux version 2.6.12-arm1 (root@davidnb-gentoo) (gcc version 3.4.4 (release) (CodeSourcery ARM 2005q3-2)) #1 Thu Jan 31 00:13:20 CET 2008
CPU: ARM926EJ-Sid(wb) [41069260] revision 0 (ARMv5TEJ)
CPU0: D VIVT write-back cache
CPU0: I cache: 32768 bytes, associativity 1, 32 byte lines, 1024 sets
CPU0: D cache: 32768 bytes, associativity 1, 32 byte lines, 1024 sets
Machine: MV-88fxx81
Using UBoot passing parameters structure
Sys Clk = 166000000, Tclk = 166000000
Memory policy: ECC disabled, Data cache writeback
On node 0 totalpages: 8192
  DMA zone: 8192 pages, LIFO batch:3
  Normal zone: 0 pages, LIFO batch:1
  HighMem zone: 0 pages, LIFO batch:1
Built 1 zonelists
Kernel command line: console=ttyS0,115200 root=/dev/mtdblock1 rw
PID hash table entries: 256 (order: 8, 4096 bytes)
Console: colour dummy device 80x30
Dentry cache hash table entries: 8192 (order: 3, 32768 bytes)
Inode-cache hash table entries: 4096 (order: 2, 16384 bytes)
Memory: 32MB 0MB 0MB 0MB = 32MB total
Memory: 28928KB available (2496K code, 877K data, 100K init)
Calibrating delay loop... 331.77 BogoMIPS (lpj=1658880)
Mount-cache hash table entries: 512
CPU: Testing write buffer coherency: ok
NET: Registered protocol family 16
Flash bankwidth 1, base f4000000, size 800000
  Marvell Development Board (LSP Version 1.8.5)-- RD-88F5181L-VOIP-GE
 Detected Tclk 166000000 and SysClk 166000000
Marvell USB EHCI Host controller #0: c03fbb00
pexBarOverlapDetect: winNum 2 overlap current 0
mvPexInit:Warning :Bar 2 size is illigal
it will be disabled
please check Pex and CPU windows configuration
PCI: bus0: Fast back to back transfers enabled
PCI: bus1: Fast back to back transfers enabled
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
pci access ctrl reg 0x31e00's value = 0x00000a01
pci access ctrl size reg 0x31e08's value = 0x07fff000
SCSI subsystem initialized
Linux Kernel Card Services
  options:  [pci]
usbcore: registered new driver usbfs
usbcore: registered new driver hub
TWSI: twsiAddr7BitSet ERROR - Addr (7 Bit) int TimeOut.
TWSI: mvTwsiStopBitSet ERROR - Stop bit TimeOut .
TWSI: mvTwsiStartBitSet ERROR - Start Clear bit TimeOut .
TWSI: twsiAddr7BitSet ERROR - Addr (7 Bit) int TimeOut.
TWSI: mvTwsiStopBitSet ERROR - Stop bit TimeOut .
TWSI: mvTwsiStartBitSet ERROR - Start Clear bit TimeOut .
TWSI: twsiAddr7BitSet ERROR - Addr (7 Bit) int TimeOut.
TWSI: mvTwsiStopBitSet ERROR - Stop bit TimeOut .
TWSI: mvTwsiStartBitSet ERROR - Start Clear bit TimeOut .
TWSI: twsiAddr7BitSet ERROR - Addr (7 Bit) int TimeOut.
TWSI: mvTwsiStopBitSet ERROR - Stop bit TimeOut .
use IDMA acceleration in copy to/from user buffers. used channels 2 and 3
Done.
Fast Floating Point Emulator V0.9 (c) Peter Teichmann.
squashfs: version 3.0 (2006/03/15) Phillip Lougher
JFFS2 version 2.2. (C) 2001-2003 Red Hat, Inc.
Initializing Cryptographic API
HDLC line discipline: version $Revision: 1.1.1.1 $, maxframe=4096
N_HDLC line discipline registered.
Serial: 8250/16550 driver $Revision: 1.1.1.1 $ 4 ports, IRQ sharing disabled
ttyS0 at MMIO 0x0 (irq = 3) is a 16550A
io scheduler noop registered
io scheduler anticipatory registered
io scheduler deadline registered
io scheduler cfq registered
loop: loaded (max 8 devices)
Loading Marvell Gatway Driver:
multi queue enabled
prioritizing ToS 0xA0
eth0: 00:00:00:00:51:81, group-id 0x100, group-members are port-CPU port-1 port-2 port-3 port-4
eth1: 00:00:00:00:51:82, group-id 0x200, group-members are port-CPU port-0
init switch layer... gcosSetPortDefaultTc failed (port 8)
gcosSetPortDefaultTc failed (port 8)
gcosSetPortDefaultTc failed (port 8)
gcosSetPortDefaultTc failed (port 8)
gcosSetPortDefaultTc failed (port 8)
gcosSetPortDefaultTc failed (port 8)
gcosSetPortDefaultTc failed (port 8)
gcosSetPortDefaultTc failed (port 8)
done
init gigabit layer... done
loading network interfaces: eth0 eth1
PPP generic driver version 2.4.2
PPP Deflate Compression module registered
PPP BSD Compression module registered
NET: Registered protocol family 24
SLIP: version 0.8.4-NET3.019-NEWTTY (dynamic channels, max=256).
STRIP: Version 1.3A-STUART.CHESHIRE (unlimited channels)
physmap flash device: 800000 at f4000000
phys_mapped_flash: Found 1 x16 devices at 0x0 in 8-bit bank
 Amd/Fujitsu Extended Query Table at 0x0040
phys_mapped_flash: Swapping erase regions for broken CFI table.
number of CFI chips: 1
cfi_cmdset_0002: Disabling erase-suspend-program due to code brokenness.
Using physmap partition definition
Creating 5 MTD partitions on "phys_mapped_flash":
0x00000000-0x00760000 : "kernel"
0x001a0000-0x00760000 : "rootfs"
0x00760000-0x007a0000 : "lang"
0x007a0000-0x007c0000 : "nvram"
0x007c0000-0x00800000 : "u-boot"
ehci_platform ehci_platform.4523: EHCI Host Controller
ehci_platform ehci_platform.4523: new USB bus registered, assigned bus number 1
ehci_platform ehci_platform.4523: irq 17, io mem 0x00000000
ehci_platform ehci_platform.4523: park 0
ehci_platform ehci_platform.4523: USB 0.0 initialized, EHCI 1.00, driver 10 Dec 2004
hub 1-0:1.0: USB hub found
hub 1-0:1.0: 1 port detected
ohci_hcd: 2004 Nov 08 USB 1.1 'Open' Host Controller (OHCI) Driver (PCI)
USB Universal Host Controller Interface driver v2.2
Initializing USB Mass Storage driver...
usbcore: registered new driver usb-storage
USB Mass Storage support registered.
mice: PS/2 mouse device common for all mice
u32 classifier
    OLD policer on
NET: Registered protocol family 2
IP: routing cache hash table of 512 buckets, 4Kbytes
/proc/eth1_tm created
TCP established hash table entries: 2048 (order: 2, 16384 bytes)
TCP bind hash table entries: 2048 (order: 1, 8192 bytes)
TCP: Hash tables configured (established 2048 bind 2048)
ip_conntrack version 2.1 (256 buckets, 2048 max) - 268 bytes per conntrack
ip_conntrack_rtsp v0.6.21 loading
ip_nat_rtsp v0.6.21 loading
ip_tables: (C) 2000-2002 Netfilter core team
netfilter PSD loaded - (c) astaro AG
ipt_random match loaded
ip_conntrack_pptp version 3.0 loaded
ip_nat_pptp version 3.0 loaded
NET: Registered protocol family 1
NET: Registered protocol family 17
802.1Q VLAN Support v1.8 Ben Greear <greearb@candelatech.com>
All bugs added by David S. Miller <davem@redhat.com>
VFS: Mounted root (squashfs filesystem) readonly.
Freeing init memory: 100K
ipt_webstr: module license 'unspecified' taints kernel.
ufsd: driver loaded
UFSD version 5.28 (Nov  8 2006, 21:54:59)
NTFS read/write support included
ufsd: address 0xbf030538
mv_gateway: starting eth0
mv_gateway: starting eth1
device eth0 entered promiscuous mode
br0: port 1(eth0) entering learning state
br0: topology change detected, propagating
br0: port 1(eth0) entering forwarding state
lock init
create wsc_cfb entry
create wsc_cfb entry
create wsc_iechange entry
create wsc_userset entry
ath_hal: 0.9.14.25 (AR5416, DEBUG)
wlan: 0.8.4.2 (Atheros/multi-bss)
ath_rate_atheros: Version 2.0.1
Copyright (c) 2001-2004 Atheros Communications, Inc, All Rights Reserved
ath_dfs: Version 2.0.0
Copyright (c) 2005-2006 Atheros Communications, Inc. All Rights Reserved
ath_pci: 0.9.4.5 (Atheros/multi-bss)
Chan  Freq  RegPwr  HT   CTL CTL_U CTL_L DFS
   1  2412n     20  HT20  1    0    1     N
   1  2412n     20  HT40  1    0    1     N
   2  2417n     20  HT40  1    0    1     N
   3  2422n     20  HT40  1    1    1     N
   4  2427n     20  HT40  1    1    1     N
   5  2432n     20  HT40  1    1    1     N
   6  2437n     20  HT40  1    1    1     N
   7  2442n     20  HT40  1    1    1     N
   8  2447n     20  HT40  1    1    1     N
   9  2452n     20  HT40  1    1    1     N
  10  2457n     20  HT40  1    1    1     N
  11  2462n     20  HT40  1    1    1     N
  12  2467n     20  HT40  1    1    0     N
  13  2472n     20  HT40  1    1    0     N
register_simple_config_callback called
wifi0: 11ng rates: 1Mbps 2Mbps 5.5Mbps 11Mbps 6Mbps 9Mbps 12Mbps 18Mbps 24Mbps 36Mbps 48Mbps 54Mbps
wifi0: 11ng MCS:  0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15
wifi0: mac 13.2 phy 8.1 radio 13.0
wifi0: Use hw queue 1 for WME_AC_BE traffic
wifi0: Use hw queue 0 for WME_AC_BK traffic
wifi0: Use hw queue 2 for WME_AC_VI traffic
wifi0: Use hw queue 3 for WME_AC_VO traffic
wifi0: Use hw queue 8 for CAB traffic
wifi0: Use hw queue 9 for beacons
wifi0: Atheros 5416 PCI: mem=0xe8000000, irq=36 hw_base=0xc2860000
ar5416SetPowerPerRateTable() syn 2412 ctl 2412 ext 2412 is40 0
  6mb OFDM  13.0 dBm |  9mb OFDM  13.0 dBm | 12mb OFDM  13.0 dBm | 18mb OFDM  13.0 dBm
 24mb OFDM  13.0 dBm | 36mb OFDM  13.0 dBm | 48mb OFDM  13.0 dBm | 54mb OFDM  13.0 dBm
 1L   CCK   13.0 dBm | 2L   CCK   13.0 dBm | 2S   CCK   13.0 dBm | 5.5L CCK   13.0 dBm
 5.5S CCK   13.0 dBm | 11L  CCK   13.0 dBm | 11S  CCK   13.0 dBm | XR         13.0 dBm
 HT20mcs 0  13.0 dBm | HT20mcs 1  13.0 dBm | HT20mcs 2  13.0 dBm | HT20mcs 3  13.0 dBm
 HT20mcs 4  13.0 dBm | HT20mcs 5  13.0 dBm | HT20mcs 6  12.0 dBm | HT20mcs 7   6.0 dBm
 HT40mcs 0   0.0 dBm | HT40mcs 1   0.0 dBm | HT40mcs 2   0.0 dBm | HT40mcs 3   0.0 dBm
 HT40mcs 4   0.0 dBm | HT40mcs 5   0.0 dBm | HT40mcs 6   0.0 dBm | HT40mcs 7   0.0 dBm
 Dup CCK     0.0 dBm | Dup OFDM    0.0 dBm | Ext CCK     0.0 dBm | Ext OFDM    0.0 dBm
2xAntennaReduction: 0, 2xMaxRegulatory: 40, 2xPowerLimit: 60
2xMaxPowerLevel: 26 (HT20)
TPC Enabled 1 1 0
ar5416SetPowerPerRateTable() syn 2412 ctl 2412 ext 2412 is40 0
  6mb OFDM  13.0 dBm |  9mb OFDM  13.0 dBm | 12mb OFDM  13.0 dBm | 18mb OFDM  13.0 dBm
 24mb OFDM  13.0 dBm | 36mb OFDM  13.0 dBm | 48mb OFDM  13.0 dBm | 54mb OFDM  13.0 dBm
 1L   CCK   13.0 dBm | 2L   CCK   13.0 dBm | 2S   CCK   13.0 dBm | 5.5L CCK   13.0 dBm
 5.5S CCK   13.0 dBm | 11L  CCK   13.0 dBm | 11S  CCK   13.0 dBm | XR         13.0 dBm
 HT20mcs 0  13.0 dBm | HT20mcs 1  13.0 dBm | HT20mcs 2  13.0 dBm | HT20mcs 3  13.0 dBm
 HT20mcs 4  13.0 dBm | HT20mcs 5  13.0 dBm | HT20mcs 6  12.0 dBm | HT20mcs 7   6.0 dBm
 HT40mcs 0   0.0 dBm | HT40mcs 1   0.0 dBm | HT40mcs 2   0.0 dBm | HT40mcs 3   0.0 dBm
 HT40mcs 4   0.0 dBm | HT40mcs 5   0.0 dBm | HT40mcs 6   0.0 dBm | HT40mcs 7   0.0 dBm
 Dup CCK     0.0 dBm | Dup OFDM    0.0 dBm | Ext CCK     0.0 dBm | Ext OFDM    0.0 dBm
2xAntennaReduction: 0, 2xMaxRegulatory: 40, 2xPowerLimit: 60
2xMaxPowerLevel: 26 (LEG)
device ath0 entered promiscuous mode
lock_write_proc: count = 260 sizeof(wsc_cfb)=260
 wsc_enable=1
 wsc_context=1
 wsc_version=0x10
 wsc_devcfstat=0
 wsc_admin.role=0
 wsc_admin.pwdMode=1
 wsc_admin.wsc_pin=00000000
 wsc_admin.seesionTimeout=120
 wsc_admin.retransmitTimeout=15
 wsc_admin.retryLimit=300
 wsc_admin.messageTimeout=0
 wsc_admin.configured=0
 wsc_admin.pbcIsRunning=0
 wsc_admin.selectedReg=0
 wsc_admin.selectedRegTime=0
 wsc_admin.selectRegConfigMethod=0
 wsc_admin.selectRegDevPwdId=0
 wsc_admin.selfPbcPressed=0
 wsc_admin.selfPbcPressedTime=0
 wsc_mac=00:1a:70:a1:c3:8c
 wsc_manfa=LINKSYS
 wsc_ssid=WirelessDANwepCrackTest
 wsc_modelname=WRT350Nv2
 wsc_modelnumber=WSC0001
 wsc_serialnumber=0001000004E044
 wsc_devicename=LINKSYS-WRT350Nv2
 wsc_encrytype=2
lock_write_proc: count = 28 sizeof(wsc_cfb)=28
 role=0
 pwdMode=0
 wsc_context=1
 wsc_iechanged=0
 configured=0
 selectedReg=0
 selectRegConfigMethod=0x00
 selectRegDevPwdId=0x00
 wsc_admin.wsc_pin=00000000
 wsc_daemon_init
create wsc_pushbutton entry
ar5416SetPowerPerRateTable() syn 2412 ctl 2412 ext 2412 is40 0
  6mb OFDM  13.0 dBm |  9mb OFDM  13.0 dBm | 12mb OFDM  13.0 dBm | 18mb OFDM  13.0 dBm
 24mb OFDM  13.0 dBm | 36mb OFDM  13.0 dBm | 48mb OFDM  13.0 dBm | 54mb OFDM  13.0 dBm
 1L   CCK   13.0 dBm | 2L   CCK   13.0 dBm | 2S   CCK   13.0 dBm | 5.5L CCK   13.0 dBm
 5.5S CCK   13.0 dBm | 11L  CCK   13.0 dBm | 11S  CCK   13.0 dBm | XR         13.0 dBm
 HT20mcs 0  13.0 dBm | HT20mcs 1  13.0 dBm | HT20mcs 2  13.0 dBm | HT20mcs 3  13.0 dBm
 HT20mcs 4  13.0 dBm | HT20mcs 5  13.0 dBm | HT20mcs 6  12.0 dBm | HT20mcs 7   6.0 dBm
 HT40mcs 0   0.0 dBm | HT40mcs 1   0.0 dBm | HT40mcs 2   0.0 dBm | HT40mcs 3   0.0 dBm
 HT40mcs 4   0.0 dBm | HT40mcs 5   0.0 dBm | HT40mcs 6   0.0 dBm | HT40mcs 7   0.0 dBm
 Dup CCK     0.0 dBm | Dup OFDM    0.0 dBm | Ext CCK     0.0 dBm | Ext OFDM    0.0 dBm
2xAntennaReduction: 0, 2xMaxRegulatory: 40, 2xPowerLimit: 60
2xMaxPowerLevel: 26 (HT20)
TPC Enabled 1 1 0
Force rf_pwd_icsyndiv to 1 on 2412 (1 2)
ath_newstate: Resetting VAP dfswait_run
ath_newstate: Resetting VAP dfswait_run
Force rf_pwd_icsyndiv to 2 on 2427 (1 2)
ar5416SetPowerPerRateTable() syn 2427 ctl 2427 ext 2427 is40 0
  6mb OFDM  13.0 dBm |  9mb OFDM  13.0 dBm | 12mb OFDM  13.0 dBm | 18mb OFDM  13.0 dBm
 24mb OFDM  13.0 dBm | 36mb OFDM  13.0 dBm | 48mb OFDM  13.0 dBm | 54mb OFDM  13.0 dBm
 1L   CCK   13.0 dBm | 2L   CCK   13.0 dBm | 2S   CCK   13.0 dBm | 5.5L CCK   13.0 dBm
 5.5S CCK   13.0 dBm | 11L  CCK   13.0 dBm | 11S  CCK   13.0 dBm | XR         13.0 dBm
 HT20mcs 0  13.0 dBm | HT20mcs 1  13.0 dBm | HT20mcs 2  13.0 dBm | HT20mcs 3  13.0 dBm
 HT20mcs 4  13.0 dBm | HT20mcs 5  13.0 dBm | HT20mcs 6  12.0 dBm | HT20mcs 7   6.0 dBm
 HT40mcs 0   0.0 dBm | HT40mcs 1   0.0 dBm | HT40mcs 2   0.0 dBm | HT40mcs 3   0.0 dBm
 HT40mcs 4   0.0 dBm | HT40mcs 5   0.0 dBm | HT40mcs 6   0.0 dBm | HT40mcs 7   0.0 dBm
 Dup CCK     0.0 dBm | Dup OFDM    0.0 dBm | Ext CCK     0.0 dBm | Ext OFDM    0.0 dBm
2xAntennaReduction: 0, 2xMaxRegulatory: 40, 2xPowerLimit: 60
2xMaxPowerLevel: 26 (HT20)
ath_chan_set: Changing to channel 2427, Flags 30080, PF 0
 make a wpa2 ie :
30      <1>1c   <1>01   <1>00   <1>00   <1>0f   <1>ac   <1>02   <1>02   <1>00   <1>00   <1>0f   <1>ac   <1>04   <1>00   <1>0f
ac      <1>02   <1>02   <1>00   <1>00   <1>0f   <1>ac   <1>01   <1>00   <1>0f   <1>ac   <1>02   <1>00   <1>00   <1>make a wpa ie :
dd      <1>1e   <1>00   <1>50   <1>f2   <1>01   <1>01   <1>00   <1>00   <1>50   <1>f2   <1>02   <1>02   <1>00   <1>00   <1>50
f2      <1>04   <1>00   <1>50   <1>f2   <1>02   <1>02   <1>00   <1>00   <1>50   <1>f2   <1>01   <1>00   <1>50   <1>f2   <1>02   <6>br0: port 2(ath0) entering learning state
br0: topology change detected, propagating
br0: port 2(ath0) entering forwarding state
download uses obsolete (PF_INET,SOCK_PACKET)
}}}
----
 . CategoryModel
 . Category80211nDevice
 . CategoryGigabitDevices
