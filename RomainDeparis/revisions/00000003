##master-page:HomepageTemplate
#format wiki
== Intro ==

I have been using a Linksys WRT54GS-Rev0 with OpenWRT for some time now - since early RC3 if I remember correctly. It used to be my Internet router/firewall/server combo and it always worked fine even with a DNS local authority/cache and a Squid cache for the LAN, but it was a little slowish so I switch back to a laptop for this part. I still use the WRT54GS with OpenWRT - now in RC5 - as my wireless-G AP with WPA2 and MAC filtering. It was pretty much as secure as one can easily get for a long time (MS Win did not even support WPA2 by default, not sure now).

Recently I have been playing with USB toys so I got an Asus WL-500g Premium and a Linksys WRTSL54G. So far I have only been messing aroung with the Asus, the only real difference being it has 2 USB ports while the Linksys has only one. Below are my experiments with the Asus, and since they are mysteriously not completely consistent with what I have seen around the wiki and forums I will not make changes to the official wiki pages until more people try it out.

== Asus WL-500g Premium ==

I only use kamikaze with some basic customization on which packages are installed and some simple patches to support extra USB hardware. Should it ever come to something interesting I will post that here.



=== CPU/Memory/Drivers ===

{{{
root@OpenWrt:~# cat /proc/cpuinfo
system type             : Broadcom BCM47xx
processor               : 0
cpu model               : Broadcom BCM3302 V0.6
BogoMIPS                : 197.12
wait instruction        : no
microsecond timers      : yes
tlb_entries             : 32
extra interrupt vector  : no
hardware watchpoint     : no
ASEs implemented        :
VCED exceptions         : not available
VCEI exceptions         : not available
}}}

{{{
root@OpenWrt:~# cat /proc/meminfo
MemTotal:        30024 kB
MemFree:         19972 kB
Buffers:           788 kB
Cached:           4476 kB
SwapCached:          0 kB
Active:           3900 kB
Inactive:         2016 kB
HighTotal:           0 kB
HighFree:            0 kB
LowTotal:        30024 kB
LowFree:         19972 kB
SwapTotal:           0 kB
SwapFree:            0 kB
Dirty:               0 kB
Writeback:           0 kB
Mapped:           1412 kB
Slab:             2448 kB
CommitLimit:     15012 kB
Committed_AS:     8676 kB
PageTables:        200 kB
VmallocTotal:  1048560 kB
VmallocUsed:      1428 kB
VmallocChunk:  1047028 kB
}}}

{{{
root@OpenWrt:~# lsmod
Module                  Size  Used by    Tainted: P
snd_pcm_oss            38880  0
snd_mixer_oss          14496  1 snd_pcm_oss
snd_usb_audio          54016  0
snd_hwdep               5136  1 snd_usb_audio
snd_usb_lib            11424  1 snd_usb_audio
snd_rawmidi            16352  1 snd_usb_lib
snd_pcm                65440  2 snd_pcm_oss,snd_usb_audio
snd_timer              16496  1 snd_pcm
snd                    36352  8 snd_pcm_oss,snd_mixer_oss,snd_usb_audio,snd_hwdep,snd_usb_lib,snd_rawmidi,snd_pcm,snd_timer
snd_page_alloc          5136  1 snd_pcm
ehci_hcd               25072  0
usbcore               106448  4 snd_usb_audio,snd_usb_lib,ehci_hcd
soundcore               4816  1 snd
wlan_xauth               416  0
wlan_wep                4576  0
wlan_tkip              10752  0
wlan_ccmp               6112  0
wlan_acl                2752  0
ath_pci                88592  0
ath_rate_sample         8768  1 ath_pci
ath_hal               207072  2 ath_pci,ath_rate_sample
wlan_scan_sta           9728  0
wlan_scan_ap            3072  0
wlan                  169696  9 wlan_xauth,wlan_wep,wlan_tkip,wlan_ccmp,wlan_acl,ath_pci,ath_rate_sample,wlan_scan_sta,wlan_scan_ap
switch_robo             3984  0
switch_core             5056  1 switch_robo
}}}

{{{
root@OpenWrt:~# dmesg
Linux version 2.6.16.7 (user@debian) (gcc version 3.4.6 (OpenWrt-2.0)) #1 Sat Jun 24 14:43:51 EDT 2006
CPU revision is: 00029006
Determined physical RAM map:
 memory: 02000000 @ 00000000 (usable)
On node 0 totalpages: 8192
  DMA zone: 8192 pages, LIFO batch:1
  DMA32 zone: 0 pages, LIFO batch:0
  Normal zone: 0 pages, LIFO batch:0
  HighMem zone: 0 pages, LIFO batch:0
Built 1 zonelists
Kernel command line: root=/dev/mtdblock2 rootfstype=squashfs,jffs2 init=/etc/preinit noinitrd console=ttyS0,115200
Primary instruction cache 16kB, physically tagged, 2-way, linesize 16 bytes.
Primary data cache 16kB, 2-way, linesize 16 bytes.
Synthesized TLB refill handler (19 instructions).
Synthesized TLB load handler fastpath (31 instructions).
Synthesized TLB store handler fastpath (31 instructions).
Synthesized TLB modify handler fastpath (30 instructions).
PID hash table entries: 256 (order: 8, 4096 bytes)
Using 100.000 MHz high precision timer.
Dentry cache hash table entries: 8192 (order: 3, 32768 bytes)
Inode-cache hash table entries: 4096 (order: 2, 16384 bytes)
Memory: 29884k/32768k available (1996k kernel code, 2868k reserved, 259k data, 124k init, 0k highmem)
Calibrating delay loop... 197.12 BogoMIPS (lpj=98560)
Mount-cache hash table entries: 512
Checking for 'wait' instruction...  unavailable.
NET: Registered protocol family 16
PCI: fixing up bridge
PCI: Setting latency timer of device 0000:01:00.0 to 64
PCI: Fixing up device 0000:01:00.0
PCI: Failed to allocate I/O resource #4:20@400 for 0000:01:03.0
PCI: Failed to allocate I/O resource #4:20@400 for 0000:01:03.1
squashfs: version 3.0 (2006/03/15) Phillip Lougher
devfs: 2004-01-31 Richard Gooch (rgooch@atnf.csiro.au)
devfs: boot_options: 0x1
JFFS2 version 2.2. (NAND) (C) 2001-2003 Red Hat, Inc.
Initializing Cryptographic API
io scheduler noop registered
io scheduler anticipatory registered (default)
Serial: 8250/16550 driver $Revision: 1.90 $ 2 ports, IRQ sharing disabled
serial8250: ttyS0 at MMIO 0x0 (irq = 3) is a 16550A
serial8250: ttyS1 at MMIO 0x0 (irq = 3) is a 16550A
PCI: Enabling device 0000:00:06.0 (0000 -> 0002)
b44.c:v0.97 (Nov 30, 2005)
PCI: Enabling device 0000:00:01.0 (0000 -> 0002)
PCI: Setting latency timer of device 0000:00:01.0 to 64
eth0: Broadcom 47xx 10/100BaseT Ethernet 00:17:31:97:92:9a
PCI: Enabling device 0000:00:02.0 (0000 -> 0002)
PCI: Setting latency timer of device 0000:00:02.0 to 64
eth1: Broadcom 47xx 10/100BaseT Ethernet 40:10:18:00:00:2d
Physically mapped flash: Found 1 x16 devices at 0x0 in 16-bit bank
 Amd/Fujitsu Extended Query Table at 0x0040
Physically mapped flash: CFI does not contain boot bank location. Assuming top.
number of CFI chips: 1
cfi_cmdset_0002: Disabling erase-suspend-program due to code brokenness.
Flash device: 0x800000 at 0x1c000000
bootloader size flag: 0
Creating 5 MTD partitions on "Physically mapped flash":
0x00000000-0x00040000 : "cfe"
0x00040000-0x007f0000 : "linux"
0x000ea400-0x00213000 : "rootfs"
mtd: partition "rootfs" doesn't start on an erase block boundary -- force read-only
0x007f0000-0x00800000 : "nvram"
0x00220000-0x007f0000 : "OpenWrt"
NET: Registered protocol family 2
IP route cache hash table entries: 512 (order: -1, 2048 bytes)
TCP established hash table entries: 2048 (order: 1, 8192 bytes)
TCP bind hash table entries: 2048 (order: 1, 8192 bytes)
TCP: Hash tables configured (established 2048 bind 2048)
TCP reno registered
ip_conntrack version 2.4 (256 buckets, 2048 max) - 244 bytes per conntrack
ip_tables: (C) 2000-2006 Netfilter Core Team
TCP vegas registered
NET: Registered protocol family 1
NET: Registered protocol family 17
802.1Q VLAN Support v1.8 Ben Greear <greearb@candelatech.com>
All bugs added by David S. Miller <davem@redhat.com>
VFS: Mounted root (squashfs filesystem) readonly.
Mounted devfs on /dev
Freeing unused kernel memory: 124k freed
Algorithmics/MIPS FPU Emulator v1.5
Probing device eth0: found!
b44: eth0: Link is up at 100 Mbps, full duplex.
b44: eth0: Flow control is off for TX and off for RX.
vlan1: add 01:00:5e:00:00:01 mcast address to master interface
vlan0: add 01:00:5e:00:00:01 mcast address to master interface
vlan0: dev_set_promiscuity(master, 1)
device eth0 entered promiscuous mode
device vlan0 entered promiscuous mode
vlan0: dev_set_allmulti(master, 1)
br0: port 1(vlan0) entering learning state
br0: topology change detected, propagating
br0: port 1(vlan0) entering forwarding state
wlan: 0.8.4.2 (svn r1590)
ath_hal: module license 'Proprietary' taints kernel.
ath_hal: 0.9.16.16 (AR5210, AR5211, AR5212, RF5111, RF5112, RF2413, RF5413)
ath_rate_sample: 1.2 (svn r1590)
ath_pci: 0.9.4.5 (svn r1590)
wlan: mac acl policy registered
usbcore: registered new driver usbfs
usbcore: registered new driver hub
PCI: Enabling device 0000:01:03.2 (0000 -> 0002)
PCI: Fixing up device 0000:01:03.2
ehci_hcd 0000:01:03.2: EHCI Host Controller
ehci_hcd 0000:01:03.2: new USB bus registered, assigned bus number 1
ehci_hcd 0000:01:03.2: irq 2, io mem 0x40000000
ehci_hcd 0000:01:03.2: USB 2.0 started, EHCI 1.00, driver 10 Dec 2004
usb usb1: configuration #1 chosen from 1 choice
hub 1-0:1.0: USB hub found
hub 1-0:1.0: 4 ports detected
Linux video capture interface: v1.00
usb 1-1: new high speed USB device using ehci_hcd and address 2
usb 1-1: configuration #1 chosen from 1 choice
usb 1-2: new high speed USB device using ehci_hcd and address 3
usb 1-2: configuration #1 chosen from 1 choice
usbcore: registered new driver snd-usb-audio
}}}



Email: [[MailTo(romain DOT deparis AT SPAMFREE gmail DOT com)]]

...

----
 CategoryHomepage
