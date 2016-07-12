##master-page:HomepageTemplate
#format wiki
== Introduction ==

''This is a WorkInProgress, please bare with me until it is fully fool-proofed and spell-checked.''

I have been using a Linksys WRT54GS-v1.0 with OpenWRT for some time now - since early RC3 if I remember correctly. It used to be my Internet router / firewall / server combo and it always worked fine even with a DNS local authority / cache and a Squid cache for the LAN, but it was a little slowish so I switched back to a laptop for this part. I still use the WRT54GS with OpenWRT - now in RC5 - as my wireless-G AP with WPA2 and MAC filtering. It was pretty much as secure as one can easily get for a long time (MS Win did not even support WPA2 by default).

Recently I have been playing with USB toys so I got an Asus WL-500g Premium and a Linksys WRTSL54G. So far I have only been messing aroung with the Asus, the only real difference being it has 2 USB ports while the Linksys has only one. Below are my experiments with the Asus, and since they are with kamikaze rather than WhiteRussian RC5 I will not make changes to the official wiki pages.

If you already know everything about running kamikaze on your latest router and have your own OpenWRT firmware optimized to the latest byte, you may want to jump to the real added value of this page, '''support for the GO7007 chipset based devices like the Plextor ConvertX PX-TV402U'''.

[[TableOfContents]]

Email: [[MailTo(romain DOT deparis AT SPAMFREE gmail DOT com)]]

Or leave me a message at the end of this page with the following syntax:
{{{
----
Just saying Hi! -- JohnDoe
}}}

[[Anchor(Asus)]]
== Asus WL-500g Premium ==

'''I use only kamikaze brcm-2.6 on SquashFS'''. I also add some basic customization on which packages are installed and some simple patches to support extra USB hardware.

As mentionned on the ["OpenWrtDocs/Hardware/Asus/WL500GP"] page, I only use tftp to upload the firmware. Router does not reboot automatically after the upload.

=== CPU / Memory / Modules ===

 * CPU

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

I saw someone somewhere commenting on this and complaining about his WL-500gP not running at 266MHz. Those are measured BogoMIPS.

 * Memory

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

As we can see we do have 32MB, but I had to use the trick from the Hardware page:
{{{
nvram set sdram_init=0x0009
nvram set sdram_ncdl=0 
}}}

 * Modules

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

 * And the summary

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
usb 1-1: new high speed USB device using ehci_hcd and address 2
usb 1-1: configuration #1 chosen from 1 choice
usb 1-2: new high speed USB device using ehci_hcd and address 3
usb 1-2: configuration #1 chosen from 1 choice
usbcore: registered new driver snd-usb-audio
}}}

Note that eth1 was disabled on this trace, see below.

Please let me know if you want any additional information posted here.

=== Network ===

Here is where things get a little more confusing. The switch part is fairly clear but the router has one more interface than expected.

Basically the switch setup appears to be exactly the same as the WRT54G v2/v3 & WRT54GS v1/v2 (see ["OpenWrtDocs/Configuration#NetworkInterfaceNames"]). I would say switchports 1 to 4 are the four LAN ports, switchport 0 is the separate WAN port and switchport 5 is the uplink to the eth0 interface of the router. So here is what I have setup:

 * VLANs

{{{
root@OpenWrt:~# cat /proc/switch/eth0/vlan/0/ports
1       2       3       4       5t*
root@OpenWrt:~# cat /proc/switch/eth0/vlan/1/ports
0       5t
}}}

VLAN 0 is native on LAN switchports 1,2,3 and 4 and tagged on switchport 5.

VLAN 1 is native on WAN swithport 0 and tagged on switchport 5.

On the router you get the trunking VLANs from switchport 5 on virtual interfaces vlan0 and vlan1 from eth0.

 * Interfaces

{{{
root@OpenWrt:~# ifconfig
br0       Link encap:Ethernet  HWaddr 00:17:31:97:92:9A
          inet addr:192.168.1.1  Bcast:192.168.1.255  Mask:255.255.255.0
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0
          RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)

eth0      Link encap:Ethernet  HWaddr 00:17:31:97:92:9A
          UP BROADCAST RUNNING PROMISC MULTICAST  MTU:1500  Metric:1
          RX packets:22 errors:0 dropped:0 overruns:0 frame:0
          TX packets:27 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:4049 (3.9 KiB)  TX bytes:4115 (4.0 KiB)
          Interrupt:4

eth1      Link encap:Ethernet  HWaddr 40:10:18:00:00:2D
          UP BROADCAST RUNNING ALLMULTI MULTICAST  MTU:1500  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)
          Interrupt:5

lo        Link encap:Local Loopback
          inet addr:127.0.0.1  Mask:255.0.0.0
          UP LOOPBACK RUNNING  MTU:16436  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0
          RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)

vlan0     Link encap:Ethernet  HWaddr 00:17:31:97:92:9A
          UP BROADCAST RUNNING ALLMULTI MULTICAST  MTU:1500  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0
          RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)

vlan1     Link encap:Ethernet  HWaddr 00:17:31:97:92:9A
          inet addr:192.168.15.50  Bcast:192.168.15.255  Mask:255.255.255.0
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:32 errors:0 dropped:0 overruns:0 frame:0
          TX packets:32 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0
          RX bytes:4363 (4.2 KiB)  TX bytes:4535 (4.4 KiB)

}}}

Note that network 192.168.15.0/24 is my actual LAN network connected to the WAN port while 192.168.1.0/24 is the development network connected to LAN port 1 for firmware upload from my linux box. They both work fine this way.
As expected we get the WAN port on interface vlan1 and the LAN ports uplink is bridged with br0 over vlan0:

{{{
root@OpenWrt:~# brctl show
bridge name     bridge id               STP enabled     interfaces
br0             8000.00173197929a       no              vlan0
}}}

Note that I removed eth1 from br0 (and from hotplug altogether) as I have no clue what it is and where it leads and I had the b44 timeout flood messages with it anyway:

{{{
b44: eth1: BUG!  Timeout waiting for bit 80000000 of register 428 to clear.
}}}

So I added extra checks in /etc/hotplug.d/net/* to forget all about eth1 for now :)

I have not bothered at all with wifi yet, so I cannot confirm anything about wifi. As far as I can see from the forums it seems pretty messy with the bcm43xx-d80211 driver. Following kernel numbering the wifi interface is expected to be on eth2 so if you get wifi to work you want to add eth2 to br0 and consider it your wlan interface.

/!\ Todo: bother with wifi...

=== PCI / USB ===

Now that the basics are ok, let us play with the juicy parts, the add-ons. Here is what we can see on the buses.

 * PCI

{{{
root@OpenWrt:~# lspci -v
00:00.0 FLASH memory: Broadcom Corporation Sentry5 Chipcommon I/O Controller (rev 08)
        Flags: fast devsel, IRQ 3
        Memory at 18000000 (32-bit, non-prefetchable) [disabled] [size=4K]
        [virtual] Expansion ROM at 18009000 [disabled] [size=2K]

00:01.0 Ethernet controller: Broadcom Corporation Sentry5 Ethernet Controller (rev 08)
        Flags: bus master, fast devsel, latency 64, IRQ 4
        Memory at 18001000 (32-bit, non-prefetchable) [size=4K]
        [virtual] Expansion ROM at 18009800 [disabled] [size=2K]

00:02.0 Ethernet controller: Broadcom Corporation Sentry5 Ethernet Controller (rev 08)
        Flags: bus master, fast devsel, latency 64, IRQ 5
        Memory at 18002000 (32-bit, non-prefetchable) [size=4K]
        [virtual] Expansion ROM at 1800a000 [disabled] [size=2K]

00:03.0 USB Controller: Broadcom Corporation Sentry5 USB Controller (rev 08) (prog-if 10 [OHCI])
        Flags: fast devsel, IRQ 6
        Memory at 18003000 (32-bit, non-prefetchable) [disabled] [size=4K]
        [virtual] Expansion ROM at 1800a800 [disabled] [size=2K]

00:04.0 MIPS: Broadcom Corporation Sentry5 PCI Bridge (rev 08)
        Flags: fast devsel, IRQ 2
        Memory at 18004000 (32-bit, non-prefetchable) [disabled] [size=4K]
        [virtual] Expansion ROM at 1800b000 [disabled] [size=2K]

00:05.0 MIPS: Broadcom Corporation BCM3302 Sentry5 MIPS32 CPU (rev 08)
        Flags: fast devsel, IRQ 2
        Memory at 18005000 (32-bit, non-prefetchable) [disabled] [size=4K]
        [virtual] Expansion ROM at 1800b800 [disabled] [size=2K]

00:06.0 Modem: Broadcom Corporation BCM47xx V.92 56k modem (rev 08) (prog-if 00 [Generic])
        Flags: fast devsel, IRQ 2
        Memory at 18006000 (32-bit, non-prefetchable) [size=4K]
        [virtual] Expansion ROM at 1800c000 [disabled] [size=2K]

00:07.0 Network and computing encryption device: Broadcom Corporation Sentry5 Crypto Accelerator (rev 08)
        Flags: fast devsel, IRQ 2
        Memory at 18007000 (32-bit, non-prefetchable) [disabled] [size=4K]
        [virtual] Expansion ROM at 1800c800 [disabled] [size=2K]

00:08.0 RAM memory: Broadcom Corporation Sentry5 DDR/SDR RAM Controller (rev 08)
        Flags: fast devsel, IRQ 3
        Memory at 18008000 (32-bit, non-prefetchable) [disabled] [size=4K]
        [virtual] Expansion ROM at 1800d000 [disabled] [size=2K]

01:00.0 Host bridge: Broadcom Corporation BCM4704 PCI to SB Bridge
        Subsystem: Broadcom Corporation BCM4704 PCI to SB Bridge
        Flags: bus master, fast devsel, latency 64, IRQ 2
        Memory at <unassigned> (32-bit, prefetchable)

01:02.0 Network controller: Broadcom Corporation BCM4318 [AirForce One 54g] 802.11g Wireless LAN Controller (rev 02)
        Subsystem: ASUSTeK Computer Inc. Unknown device 120f
        Flags: fast devsel, IRQ 2
        Memory at 40000000 (32-bit, non-prefetchable) [disabled] [size=8K]

01:03.0 USB Controller: VIA Technologies, Inc. VT82xxxxx UHCI USB 1.1 Controller (rev 61) (prog-if 00 [UHCI])
        Subsystem: VIA Technologies, Inc. VT82xxxxx UHCI USB 1.1 Controller
        Flags: medium devsel, IRQ 2
        I/O ports at <ignored> [disabled]
        Capabilities: [80] Power Management version 2

01:03.1 USB Controller: VIA Technologies, Inc. VT82xxxxx UHCI USB 1.1 Controller (rev 61) (prog-if 00 [UHCI])
        Subsystem: VIA Technologies, Inc. VT82xxxxx UHCI USB 1.1 Controller
        Flags: medium devsel, IRQ 2
        I/O ports at <ignored> [disabled]
        Capabilities: [80] Power Management version 2

01:03.2 USB Controller: VIA Technologies, Inc. USB 2.0 (rev 63) (prog-if 20 [EHCI])
        Subsystem: VIA Technologies, Inc. USB 2.0
        Flags: bus master, medium devsel, latency 22, IRQ 2
        Memory at 40000000 (32-bit, non-prefetchable) [size=256]
        Capabilities: [80] Power Management version 2
}}}

If we look at the network devices, we do see 2 wired ethernet controllers:

{{{
root@OpenWrt:~# ls -la /sys/devices/pci0000\:00/0000\:00\:01.0/ | grep net
lrwxrwxrwx    1 root     root            0 Jan  1 00:11 net:eth0 -> ../../../class/net/eth0
root@OpenWrt:~# ls -la /sys/devices/pci0000\:00/0000\:00\:02.0/ | grep net
lrwxrwxrwx    1 root     root            0 Jan  1 00:11 net:eth1 -> ../../../class/net/eth1
}}}

They are the two mapped to eth0 and eth1.

Notice the "Broadcom Corporation Sentry5 Crypto Accelerator". Is it some hardware encryption module for IPSEC VPN terminations? Or is it just for vendor internal function support? I am sure we can do something fun with this. Also there appears to be a V.92 56k modem inside too. I really need to open that box :)

 * USB 2.0

{{{
root@OpenWrt:~# lsusb
Bus 001 Device 002: ID 0457:0151 Silicon Integrated Systems Corp.
Bus 001 Device 001: ID 0000:0000
}}}

Device 002 is a 1GB USB2 key.

If you want a more interesting USB device support example, check below.

[[Anchor(Linksys)]]
== Linksys WRTSL54GS ==

=== Todo ===

/!\ Untested so far

[[Anchor(wis-go7007)]]
== GO7007 devices support ==

The idea here is to add support to OpenWRT for hardware accelerated encoding device like the Plextor ConvertX PX-TV402U that I have.

http://oss.wischip.com/tv402u.jpg

For more info on the Plextor:
http://www.plextor.com/english/products/TV402U.htm

Fortunately the driver for the GO7007 chipset it is based on is Open Source Software. For more info on this driver:
http://oss.wischip.com/

The GO7007 video part uses Video4Linux2 API and the audio part uses ALSA OSS emulation.

In the next sections I assume that you know how to tweak kamikaze and that you have a working copy of the SVN trunk. For more info check the wiki documentation BuildingPackagesHowTo and the development documentation
 https://dev.openwrt.org/browser/trunk/openwrt/docs/buildroot-documentation.html?format=raw

=== Requirements ===

From the README file distributed with the GO7007 driver archive, we can summarize the requirements as following:

 * Linux kernel 2.6.10 or later
 * USB 2.0 support
 * Kernel options:
  * CONFIG_HOTPLUG           - Support for hot-pluggable devices
  * CONFIG_MODULES           - Enable loadable module support
  * CONFIG_KMOD              - Automatic kernel module loading
  * CONFIG_FW_LOADER         - Hotplug firmware loading support
  * CONFIG_I2C               - I2C support
  * CONFIG_VIDEO_DEV         - Video For Linux
  * CONFIG_SOUND             - Sound card support
  * CONFIG_SND               - Advanced Linux Sound Architecture
  * CONFIG_USB               - Support for Host-side USB
  * CONFIG_USB_DEVICEFS      - USB device filesystem
  * CONFIG_USB_EHCI_HCD      - EHCI HCD (USB 2.0) support
  * CONFIG_SND_MIXER_OSS     - OSS Mixer API
  * CONFIG_SND_PCM_OSS       - OSS PCM (digital audio) API
 * Hotplug scripts
 * The FXload utility

As of today kamikaze comes with Linux kernel 2.6.16 and with built-in USB 2.0 support, so the first two requirements are met. Kernel options setup is documented and we will configure them later. 

OpenWRT also includes a minimalist Hotplug emulation that works just fine and that we will use for firmware auto-loading. The only unmet requirement is the FXload utility used to upload the firmware to the EZ-USB device.

=== FXload utility ===

FXload is available from the SourceForge website for Linux-hotplug:
http://prdownloads.sourceforge.net/linux-hotplug/

Below is the set of files to create under package/fxload/:

{{{
package/fxload/:
total 12
-rw-r--r--  1 user users  374 Jun 24 12:50 Config.in
-rw-r--r--  1 user users 1030 Jun 24 12:50 Makefile
drwxr-xr-x  2 user users 4096 Jun 24 12:50 ipkg

package/fxload/ipkg:
total 4
-rw-r--r--  1 user users 117 Jun 24 12:50 fxload.control
}}}

And their content:

 * Config.in

{{{
config BR2_PACKAGE_FXLOAD
        prompt "fxload............................ firmware loader for EZ-USB devices"
        tristate
        default y
        help
          This program is conveniently able to download firmware into FX and FX2
          EZ-USB devices, as well as the original AnchorChips EZ-USB.  It is
          intended to be invoked by hotplug scripts when the unprogrammed device
          appears on the bus.
}}}

 * Makefile

{{{
# $Id: Makefile 3112 2006-06-18 23:33:19Z rdeparis $

include $(TOPDIR)/rules.mk

PKG_NAME:=fxload
PKG_VERSION:=2002_04_11
PKG_RELEASE:=1
PKG_MD5SUM:=cafd71a5bff0c57bcd248273b2541c05

PKG_SOURCE_URL:=@SF/linux-hotplug
PKG_SOURCE:=$(PKG_NAME)-$(PKG_VERSION).tar.gz
PKG_CAT:=zcat

PKG_BUILD_DIR:=$(BUILD_DIR)/$(PKG_NAME)-$(PKG_VERSION)
PKG_INSTALL_DIR:=$(PKG_BUILD_DIR)/ipkg-install

include $(TOPDIR)/package/rules.mk

$(eval $(call PKG_template,FXLOAD,fxload,$(PKG_VERSION)-$(PKG_RELEASE),$(ARCH)))

$(PKG_BUILD_DIR)/.configured: $(PKG_BUILD_DIR)/.prepared
        (cd $(PKG_BUILD_DIR); \
                \
        );
        touch $@

$(PKG_BUILD_DIR)/.built: $(PKG_BUILD_DIR)/.configured
        rm -rf $(PKG_INSTALL_DIR)
        mkdir -p $(PKG_INSTALL_DIR)
        $(MAKE) -C $(PKG_BUILD_DIR) \
                CC="$(TARGET_CC)" \
                CFLAGS="$(TARGET_CFLAGS)" \
                DESTDIR="$(PKG_INSTALL_DIR)" \
                all
        touch $@

$(IPKG_FXLOAD):
        install -d -m0755 $(IDIR_FXLOAD)/usr/sbin
        $(CP) $(PKG_BUILD_DIR)/fxload $(IDIR_FXLOAD)/usr/sbin/
        $(RSTRIP) $(IDIR_FXLOAD)
        $(IPKG_BUILD) $(IDIR_FXLOAD) $(PACKAGE_DIR)
}}}

 * fxload.control

{{{
Package: fxload
Priority: optional
Section: sys
Maintainer: rdeparis
Description: firmware loader for EZ-USB devices
}}}

Now all you have to do is to integrate this package to the kamikaze build system. Add the following lines to the corresponding files directly under package/:

 * Config.in (somewhere under the menu "Utilities" for instance)

{{{
source "package/fxload/Config.in"
}}}

 * Makefile

{{{
package-$(BR2_PACKAGE_FXLOAD) += fxload
}}}

All this should produce the following package under bin/packages when you ''make'':
{{{
fxload_2002_04_11-1_mipsel.ipk
}}}

Copy it to your router (I make intense use of public key authentication and SCP) and install with ipkg. Try to launch FXload to make sure the compilation worked okay:

{{{
root@OpenWrt:~# fxload
no device specified!
usage: fxload [-vV] [-t type] [-D devpath]
                [-I firmware_hexfile] [-s loader] [-c config_byte]
                [-L link] [-m mode]
... [-D devpath] overrides DEVICE= in env
... device types:  one of an21, fx, fx2
... at least one of -I, -L, -m is required
}}}

We now have FXload.

=== Kernel and system setup ===

Before we get to the actual driver compilation we need to enable a couple of kernel options. Almost all the required options are present in kamikaze except CONFIG_KMOD and CONFIG_I2C. Unfortunately I2C core support triggers some more options that needs to be disabled.

Here is the diff against the stock bcrm-2.6 config:

{{{
diff -NurbB -x .svn kamikaze.orig/trunk/openwrt/target/linux/brcm-2.6/config kamikaze.devel/trunk/openwrt/target/linux/brcm-2.
6/config
--- kamikaze.orig/trunk/openwrt/target/linux/brcm-2.6/config    2006-06-17 14:13:12.000000000 -0400
+++ kamikaze.devel/trunk/openwrt/target/linux/brcm-2.6/config   2006-06-24 11:37:40.000000000 -0400
@@ -183,7 +183,7 @@
 CONFIG_OBSOLETE_MODPARM=y
 # CONFIG_MODVERSIONS is not set
 # CONFIG_MODULE_SRCVERSION_ALL is not set
-# CONFIG_KMOD is not set
+CONFIG_KMOD=y

 #
 # Block layer
@@ -1118,7 +1118,45 @@
 #
 # I2C support
 #
-# CONFIG_I2C is not set
+CONFIG_I2C=y
+CONFIG_I2C_CHARDEV=n
+CONFIG_I2C_ALGOBIT=n
+CONFIG_I2C_ALGOPCF=n
+CONFIG_I2C_ALGOPCA=n
+CONFIG_I2C_ALI1535=n
+CONFIG_I2C_ALI1563=n
+CONFIG_I2C_ALI15X3=n
+CONFIG_I2C_AMD756=n
+CONFIG_I2C_AMD8111=n
+CONFIG_I2C_I801=n
+CONFIG_I2C_I810=n
+CONFIG_I2C_PIIX4=n
+CONFIG_I2C_NFORCE2=n
+CONFIG_I2C_PARPORT_LIGHT=n
+CONFIG_I2C_PROSAVAGE=n
+CONFIG_I2C_SAVAGE4=n
+CONFIG_SCx200_ACB=n
+CONFIG_I2C_SIS5595=n
+CONFIG_I2C_SIS630=n
+CONFIG_I2C_SIS96X=n
+CONFIG_I2C_STUB=n
+CONFIG_I2C_VIA=n
+CONFIG_I2C_VIAPRO=n
+CONFIG_I2C_VOODOO3=n
+CONFIG_I2C_PCA_ISA=n
+CONFIG_SENSORS_DS1337=n
+CONFIG_SENSORS_DS1374=n
+CONFIG_SENSORS_EEPROM=n
+CONFIG_SENSORS_PCF8574=n
+CONFIG_SENSORS_PCA9539=n
+CONFIG_SENSORS_PCF8591=n
+CONFIG_SENSORS_RTC8564=n
+CONFIG_SENSORS_MAX6875=n
+CONFIG_RTC_X1205_I2C=n
+CONFIG_I2C_DEBUG_CORE=n
+CONFIG_I2C_DEBUG_ALGO=n
+CONFIG_I2C_DEBUG_BUS=n
+CONFIG_I2C_DEBUG_CHIP=n

 #
 # SPI support
@@ -1153,6 +1191,16 @@
 #
 # Video For Linux
 #
+CONFIG_VIDEO_BT848=n
+CONFIG_VIDEO_SAA5246A=n
+CONFIG_VIDEO_SAA5249=n
+CONFIG_TUNER_3036=n
+CONFIG_VIDEO_SAA7134=n
+CONFIG_VIDEO_CX88=n
+CONFIG_VIDEO_EM28XX=n
+CONFIG_VIDEO_OVCAMCHIP=n
+CONFIG_VIDEO_AUDIO_DECODER=n
+CONFIG_VIDEO_DECODER=n

 #
 # Video Adapters
}}}

You need to ''make menuconfig'' and enable at least modprobe under busybox configuration. This is necessary for modules and their dependencies to automagically load with CONFIG_KMOD. That is usually when I tweak the image to remove most of the packages I will not use and add others usefull (lspci, lsusb, lsmod...).

Do not forget to ''make'' and upload the new firmware to your router.

=== Kernel module wis-go7007 ===

Create the wis-go7007 package under target/linux/package:

{{{
target/linux/package/wis-go7007/:
total 16
-rw-r--r--  1 user users  599 Jun 24 12:49 Config.in
-rw-r--r--  1 user users 1868 Jun 24 15:05 Makefile
drwxr-xr-x  2 user users 4096 Jun 24 12:49 files
drwxr-xr-x  2 user users 4096 Jun 24 12:49 ipkg

target/linux/package/wis-go7007/files:
total 8
-rw-r--r--  1 user users   80 Jun 24 12:49 go7007.modules
-rw-r--r--  1 user users 1286 Jun 24 12:49 modules.dep

target/linux/package/wis-go7007/ipkg:
total 4
-rw-r--r--  1 user users 151 Jun 24 12:49 kmod-go7007.control
}}}

With the folowing files content:

 * Config.in

{{{
config BR2_PACKAGE_KMOD_GO7007
        prompt "kmod-go7007....................... GO7007 chipset support (Plextor ConvertX...)"
        tristate
        default y
        depends BR2_LINUX_2_6_X86 || BR2_LINUX_2_6_BRCM
        select BR2_PACKAGE_KMOD_USB2
        select BR2_PACKAGE_KMOD_VIDEODEV
        select BR2_PACKAGE_KMOD_ALSA
        help
          Linux kernel module for the GO7007 which delivers compressed video via
          the Video4Linux2 API and uncompressed audio via the ALSA API.

          http://oss.wischip.com/

          DEPENDS: BR2_PACKAGE_KMOD_USB2
                   BR2_PACKAGE_KMOD_VIDEODEV
                   BR2_PACKAGE_KMOD_ALSA
}}}

 * Makefile

{{{
# $Id: Makefile 3526 2006-06-24 21:29:01 rdeparis $

include $(TOPDIR)/rules.mk
include ../../rules.mk

PKG_NAME:=wis-go7007-linux
PKG_VERSION:=0.9.8
PKG_RELEASE:=1
PKG_MD5SUM:=dbeaceae423972140d6a5107a1f586ec

PKG_SOURCE_URL:=http://oss.wischip.com
PKG_SOURCE:=$(PKG_NAME)-$(PKG_VERSION).tar.bz2
PKG_CAT:=bzcat

PKG_BUILD_DIR:=$(BUILD_DIR)/$(PKG_NAME)-$(PKG_VERSION)

include $(TOPDIR)/package/rules.mk

$(eval $(call PKG_template,KMOD_GO7007,kmod-go7007,\
         $(LINUX_VERSION)+$(PKG_VERSION)-$(BOARD)-$(PKG_RELEASE),\
         $(ARCH),kernel ($(LINUX_VERSION)-$(BOARD)-$(LINUX_RELEASE))))

$(PKG_BUILD_DIR)/.configured:
        (cd $(PKG_BUILD_DIR); \
                touch kernel/.configured \
        );
        touch $@

$(PKG_BUILD_DIR)/.built:
        $(MAKE) -C $(LINUX_DIR)/ \
                ARCH="$(LINUX_KARCH)" \
                CROSS_COMPILE="$(TARGET_CROSS)" \
                SUBDIRS="$(PKG_BUILD_DIR)/kernel" \
                modules
        sed -e s/@FIRMWARE_DIR@/\\/lib\\/firmware/ \
                -e s/@FXLOAD@/\\/usr\\/sbin\\/fxload/ \
                <$(PKG_BUILD_DIR)/hotplug/wis-ezusb.in \
                >$(PKG_BUILD_DIR)/hotplug/wis-ezusb
        touch $@

$(IPKG_KMOD_GO7007):
        install -m0644 $(PKG_BUILD_DIR)/include/*.h \
                $(LINUX_DIR)/include/linux
        install -d -m0755 $(IDIR_KMOD_GO7007)/lib/firmware/ezusb
        install -m0644 $(PKG_BUILD_DIR)/firmware/*.bin \
                $(IDIR_KMOD_GO7007)/lib/firmware
        install -m0644 $(PKG_BUILD_DIR)/firmware/ezusb/*.hex \
                $(IDIR_KMOD_GO7007)/lib/firmware/ezusb
        install -d -m0755 $(IDIR_KMOD_GO7007)/etc/hotplug.d/usb
        install -m0755 $(PKG_BUILD_DIR)/hotplug/wis-ezusb \
                $(IDIR_KMOD_GO7007)/etc/hotplug.d/usb/90-ezusb
        install -d -m0755 $(IDIR_KMOD_GO7007)/lib/modules/$(LINUX_VERSION)
        install -m0644 ./files/modules.dep \
                $(IDIR_KMOD_GO7007)/lib/modules/$(LINUX_VERSION)/
        install -m0644 $(PKG_BUILD_DIR)/kernel/*.$(LINUX_KMOD_SUFFIX) \
                $(IDIR_KMOD_GO7007)/lib/modules/$(LINUX_VERSION)/
        $(IPKG_BUILD) $(IDIR_KMOD_GO7007) $(PACKAGE_DIR)
}}}

 * go7007.modules

{{{
v4l2-common
snd-go7007
go7007
go7007-usb
wis-saa7115
wis-uda1342
wis-sony-tuner
}}}

Note that this file was used before I start using modprobe so it is unused for now.

 * modules.dep

{{{
/lib/modules/2.6.16.7/wis-sony-tuner.ko: /lib/modules/2.6.16.7/go7007.ko /lib/modules/2.6.16.7/v4l2-common.ko
/lib/modules/2.6.16.7/wis-uda1342.ko: /lib/modules/2.6.16.7/go7007.ko
/lib/modules/2.6.16.7/wis-saa7115.ko: /lib/modules/2.6.16.7/go7007.ko
/lib/modules/2.6.16.7/go7007-usb.ko: /lib/modules/2.6.16.7/go7007.ko /lib/modules/2.6.16.7/usbcore.ko
/lib/modules/2.6.16.7/go7007.ko: /lib/modules/2.6.16.7/snd-go7007.ko /lib/modules/2.6.16.7/v4l2-common.ko /lib/modules/2.6.16.7/videodev.ko
/lib/modules/2.6.16.7/snd-go7007.ko:
/lib/modules/2.6.16.7/v4l2-common.ko:
/lib/modules/2.6.16.7/videodev.ko:
/lib/modules/2.6.16.7/ehci-hcd.ko:
/lib/modules/2.6.16.7/usbcore.ko:
}}}

Note that not all actual dependencies are listed as most modules are loaded at boot time and would only generate insmod "Success error". This is the module.dep file you want it you leave the /etc/modules.d/* files alone.

 * kmod-go7007.control

{{{
Package: kmod-go7007
Priority: optional
Section: sys
Maintener: rdeparis
Depends: kmod-usb2, kmod-videodev, kmod-alsa
Description: GO7007 Linux driver
}}}

As far as the integration to the kamikaze build system is concerned, there nothing to do for Config.in as all subdirectories under target/linux/packages are automatically scanned. You do need to edit the corresponding Makefile adding the following line:

{{{
package-$(BR2_PACKAGE_KMOD_GO7007) += wis-go7007
}}}

After you ''make'' you should have among other packages the followings under bin/packages:

{{{
kmod-alsa_2.6.16.7+1.0.11rc4-brcm-1_mipsel.ipk
kmod-go7007_2.6.16.7+0.9.8-brcm-1_mipsel.ipk
kmod-usb-core_2.6.16.7-brcm-1_mipsel.ipk
kmod-usb2_2.6.16.7-brcm-1_mipsel.ipk 
kmod-videodev_2.6.16.7-brcm-1_mipsel.ipk
}}}

Copy them to your router, install them with ipkg and reboot.

/!\ Note on GO7007 modules loading: only ALSA, videodev and USB should load automatically at boot time, not GO7007. We could use the same principle with GO7007 but it is not that simple. The GO7007 device configuration is a two steps firmware loading process. First we load the EZ-USB firmware to the box, the box reboots, and then we have a limited time to upload the actual GO7007 code to the driver. With the way hotplug and the boot scripts are design we end up having a race condition between the USB devices configuration and the modules loading. So you may either miss the second firmware upload or have the box reboot before the modules are loaded. This could be resolved with checks within the scripts but this could also introduce deadlocks at boot time. So in order to keep things easy and simple we use modprobe, which is a lot cleaner anyway.

Now it is time to test the hardware:

{{{
root@OpenWrt:~# modprobe go7007-usb
root@OpenWrt:~#
}}}

You should not have any error message :) Check dmesg:

{{{
go7007-usb: probing new GO7007 USB board
go7007: registering new Plextor PX-TV402U-NA
wis-saa7115: initializing SAA7115 at address 32 on WIS GO7007SB EZ-USB
wis-uda1342: initializing UDA1342 at address 26 on WIS GO7007SB EZ-USB
wis-sony-tuner: initializing tuner at address 96 on WIS GO7007SB EZ-USB
wis-sony-tuner: type set to 202 (Sony NTSC (BTF-PB463Z))
usbcore: registered new driver go7007
}}}

Here is the complete list of relevant modules now loaded:

{{{
wis_sony_tuner          5904  0
wis_uda1342             1568  0
wis_saa7115             3936  0
go7007_usb             10288  0
go7007                 53728  4 wis_sony_tuner,wis_uda1342,wis_saa7115,go7007_usb
snd_go7007              2448  1 go7007
v4l2_common             5312  2 wis_sony_tuner,go7007
snd_pcm_oss            38880  0
snd_mixer_oss          14496  1 snd_pcm_oss
snd_usb_audio          54016  0
snd_hwdep               5136  1 snd_usb_audio
snd_usb_lib            11424  1 snd_usb_audio
snd_rawmidi            16352  1 snd_usb_lib
snd_pcm                65440  3 snd_go7007,snd_pcm_oss,snd_usb_audio
snd_timer              16496  1 snd_pcm
snd                    36352  9 snd_go7007,snd_pcm_oss,snd_mixer_oss,snd_usb_audio,snd_hwdep,snd_usb_lib,snd_rawmidi,snd_pcm,snd_timer
snd_page_alloc          5136  1 snd_pcm
videodev                5472  1 go7007
ehci_hcd               25072  0
usbcore               106448  5 go7007_usb,snd_usb_audio,snd_usb_lib,ehci_hcd
soundcore               4816  1 snd
}}}

Check the USB bus:

{{{
root@OpenWrt:~# lsusb
Bus 001 Device 004: ID 093b:a104 Plextor Corp.
Bus 001 Device 002: ID 0457:0151 Silicon Integrated Systems Corp.
Bus 001 Device 001: ID 0000:0000
}}}

Device 002 is still my USB2 1GB key. Device 004 is our Plextor ConvertX.

Check the ALSA and video4linux integration:

{{{
root@OpenWrt:~# cat /sys/class/video4linux/video0/name
go7007
root@OpenWrt:~# cat /proc/asound/oss/devices
  0: [0- 0]: mixer
  3: [0- 0]: digital audio
  4: [0- 0]: digital audio
}}}

Finally check the device files automagically created by kamikaze udev:
{{{
root@OpenWrt:~# ls -la /dev/v4l/
drwxr-xr-x    1 root     root            0 Jan  1  1970 .
drwxr-xr-x    1 root     root            0 Jan  1  1970 ..
crw-------    1 root     root      81,   0 Jan  1  1970 video0
root@OpenWrt:~# ls -la /dev/sound/
drwxr-xr-x    1 root     root            0 Jan  1  1970 .
drwxr-xr-x    1 root     root            0 Jan  1  1970 ..
crw-------    1 root     root      14,   4 Jan  1  1970 audio
crw-------    1 root     root      14,   3 Jan  1  1970 dsp
crw-------    1 root     root      14,   0 Jan  1  1970 mixer
}}}

All set!

=== User application wis-streamer ===

----
 CategoryHomepage
