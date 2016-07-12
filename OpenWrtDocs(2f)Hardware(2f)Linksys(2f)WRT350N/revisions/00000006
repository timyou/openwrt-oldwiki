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

'''WRT350N v2.0'''

The WRT350N v2.0 is based on the Marvell 88F5181 running at 500MHz cpu. It has 8MB flash and 16MB SDRAM. The wireless NIC is an Atheros AR5008 card. The WRT350N runs 802.11 B, G, and Draft N wireless protocols. It provides 4 gigabit LAN ports, 1 WAN port and a USB 'storage link' port.

There seems to be another version of WRT350N v2 based on ARM926EJ running at 333MHz and with  32MB SDRAM.

'''''Information'''''

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

----
 . CategoryModel
