attachment:small-2091.png [BR]

[http://www.voyager.bt.com/wireless_devices/voyager_2091/product_info.htm BT Voyager 2091] uses a [:BroadcomBCM63xxPort:BCM6348] chipset. 

More information on this device can be found on [http://corz.org/comms/hardware/router/other.bt.voyager.routers.php corz.org]

{{{
cat /proc/cpuinfo
system type             : V2091_BB
processor               : 0
cpu model               : BCM6348 V0.7
BogoMIPS                : 239.20
wait instruction        : no
microsecond timers      : yes
tlb_entries             : 32
extra interrupt vector  : yes
hardware watchpoint     : no
VCED exceptions         : not available
VCEI exceptions         : not available
}}}

{{{
# dmesg
Linux version 2.6.8.1 (compiled by michaelc) (gcc version 3.4.2) #1 Tue May 2 16:37:07 CST 2006
01/2200 System PLL( MPI clock 0x10)
Flash Config: CS0(1f80000a,17),Base(bf800000),Size(8MB)
FLASH_BASE bfc00000,blk 47
Total Flash size: 8192K with 135 sectors NVRAM @71 block
Scratch pad is not used for this flash part.
V2091_BB prom init
CPU revision is: 00029107
Determined physical RAM map:
 memory: 00fa0000 @ 00000000 (usable)
On node 0 totalpages: 4000
  DMA zone: 4000 pages, LIFO batch:1
  Normal zone: 0 pages, LIFO batch:1
  HighMem zone: 0 pages, LIFO batch:1
Built 1 zonelists
Kernel command line: root=31:0 ro noinitrd
brcm mips: enabling icache and dcache...
Primary instruction cache 16kB, physically tagged, 2-way, linesize 16 bytes.
Primary data cache 8kB 2-way, linesize 16 bytes.
PID hash table entries: 64 (order 6: 512 bytes)
Using 120.000 MHz high precision timer.
Dentry cache hash table entries: 4096 (order: 2, 16384 bytes)
Inode-cache hash table entries: 2048 (order: 1, 8192 bytes)
Memory: 14052k/16000k available (1355k kernel code, 1928k reserved, 204k data, 72k init, 0k highmem)
Calibrating delay loop... 239.20 BogoMIPS
Mount-cache hash table entries: 512 (order: 0, 4096 bytes)
Checking for 'wait' instruction...  unavailable.
NET: Registered protocol family 16
Can't analyze prologue code at 801617bc
1.parse options inodes 1759 block 1759
PPP generic driver version 2.4.2
NET: Registered protocol family 24
Using noop io scheduler
bcm963xx_mtd driver v1.0
brcmboard: brcm_board_init entry
bcm963xx_serial driver v2.0
u32 classifier
    OLD policer on 
NET: Registered protocol family 2
IP: routing cache hash table of 512 buckets, 4Kbytes
TCP: Hash tables configured (established 512 bind 1024)
NET: Registered protocol family 1
NET: Registered protocol family 17
Ebtables v2.0 registered
NET: Registered protocol family 8
NET: Registered protocol family 20
802.1Q VLAN Support v1.8 Ben Greear <greearb@candelatech.com>
All bugs added by David S. Miller <davem@redhat.com>
VFS: Mounted root (squashfs filesystem) readonly.
Freeing unused kernel memory: 72k freed
Algorithmics/MIPS FPU Emulator v1.5
tmpfs size 262144
1.parse options inodes 1768 block 64
atmapi: module license 'Proprietary' taints kernel.
blaadd: blaa_detect entry
adsl: adsl_init entry
Broadcom BCMPROCFS v1.0 initialized
Internal PHY
Broadcom BCM6348B0 Ethernet Network Device v0.3 May  2 2006 16:35:19
Config Internal PHY Through MDIO
BCM63xx_ENET: 100 MB Full-Duplex (auto-neg)
eth0: MAC Address: 00:11:F5:D3:D7:1B
Broadcom BCM6348B0 USB Network Device v0.4 May  2 2006 16:35:21
usb0: MAC Address: 00 11 F5 D3 D7 1C
usb0: Host MAC Address: 00 11 F5 D3 D7 1D
USB Vendor id=069a, USB Product id=0311 
PCI: Setting latency timer of device 0000:00:01.0 to 64
PCI: Enabling device 0000:00:01.0 (0004 -> 0006)
wl: srom not detected, using main memory mapped srom info (wombo board)
eth0 Link UP.
wl0: Broadcom BCM4318 802.11 Wireless Controller 3.91.41.0
pSdramPHY=0xA0FFFFF8, 0xE7FBFDFF 0xFBFFEFFE
AdslCoreHwReset: AdslOemDataAddr = 0xA0FFA664
SharedMemAlloc: ptr=0xA0FFFC38 size=936
disable vlan
ip_tables: (C) 2000-2002 Netfilter core team
ip_conntrack version 2.1 (125 buckets, 0 max) - 368 bytes per conntrack
ip_conntrack_pptp version 2.1 loaded
ip_nat_pptp version 2.0 loaded
ip_conntrack_h323: init 
ip_nat_h323: initialize the module!
ip_conntrack_rtsp v0.01 loading
ip_nat_rtsp v0.01 loading
board_ioctl: boot complete!
eth0 Link DOWN.
eth0 Link UP.
AdslCoreEcUpdTmr: timeMs=1800040 ecUpdMask=0x40000
}}}

{{{
> cat /proc/meminfo
MemTotal:        14144 kB
MemFree:           608 kB
Buffers:           796 kB
Cached:           7116 kB
SwapCached:          0 kB
Active:           3548 kB
Inactive:         5508 kB
HighTotal:           0 kB
HighFree:            0 kB
LowTotal:        14144 kB
LowFree:           608 kB
SwapTotal:           0 kB
SwapFree:            0 kB
Dirty:               0 kB
Writeback:           0 kB
Mapped:           2608 kB
Slab:             2508 kB
Committed_AS:     3788 kB
PageTables:        272 kB
VmallocTotal:  1048560 kB
VmallocUsed:      1316 kB
VmallocChunk:  1047200 kB
}}}

{{{
ifconfig
br0             Link encap:Ethernet  HWaddr 00:11:F5:D3:D7:1B  
                inet addr:192.168.1.1  Bcast:192.168.1.255  Mask:255.255.255.0
                UP BROADCAST RUNNING ALLMULTI MULTICAST  MTU:1500  Metric:1
                RX packets:13481 errors:0 dropped:0 overruns:0 frame:0
                TX packets:6092 errors:0 dropped:0 overruns:0 carrier:0
                collisions:0 txqueuelen:0 
                RX bytes:1149143 (1.0 MiB)  TX bytes:2965636 (2.8 MiB)

eth0            Link encap:Ethernet  HWaddr 00:11:F5:D3:D7:1B  
                UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
                RX packets:13485 errors:0 dropped:0 overruns:0 frame:0
                TX packets:6086 errors:0 dropped:0 overruns:0 carrier:0
                collisions:0 txqueuelen:1000 
                RX bytes:1392185 (1.3 MiB)  TX bytes:2990334 (2.8 MiB)
                Interrupt:28 Base address:0x6000 

lo              Link encap:Local Loopback  
                inet addr:127.0.0.1  Mask:255.0.0.0
                UP LOOPBACK RUNNING  MTU:16436  Metric:1
                RX packets:0 errors:0 dropped:0 overruns:0 frame:0
                TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
                collisions:0 txqueuelen:0 
                RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)

wl0             Link encap:Ethernet  HWaddr 00:11:F5:D3:D7:1E  
                UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
                RX packets:0 errors:0 dropped:0 overruns:0 frame:22095
                TX packets:361 errors:682 dropped:0 overruns:0 carrier:0
                collisions:0 txqueuelen:1000 
                RX bytes:0 (0.0 B)  TX bytes:73744 (72.0 KiB)
                Interrupt:32 
}}}
