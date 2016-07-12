'''LiteStation 2'''

{{{
Bootloader: RedBoot
CPU: Atheros AR2316
CPU Speed: 184 Mhz
Flash size: 4 MB
RAM: 16 MB
Wireless: Atheros 802.11b/g (in CPU)
Ethernet: 2 port connected to the CPU
USB: none
Serial: yes, external
JTAG: ?
}}}

=== Problems ===

The factory bootloader is crap. It only enables 8MB of the 16MB of memory, doesn't understand LZMA compression, and it's buggy.
For the above reasons, it's recommended to change the bootloader (and for now this is the only supported/usable mode).

=== Updating the bootloader ===

You can download the new bootloader from [http://downloads.openwrt.org/people/kaloz/ls2.rom here]. Put it on a TFTP server (RedBoot tries to download from the IP address of 192.168.1.254, so if your server is on a different address, pass "-h $ip_address" to the load command).

{{{
+Ethernet eth0: MAC address 00:15:6d:e0:03:19
IP: 192.168.1.20/255.255.255.0, Gateway: 0.0.0.0
Default server: 192.168.1.254

RedBoot(tm) bootstrap and debug environment [ROMRAM]
Non-certified release, version UNKNOWN - built 17:31:09, Feb  6 2006

Copyright (C) 2000, 2001, 2002, 2003, 2004 Red Hat, Inc.

Board: ap51 
RAM: 0x80000000-0x80800000, [0x8003d830-0x807e1000] available
FLASH: 0xbfc00000 - 0xbfff0000, 64 blocks of 0x00010000 bytes each.
== Executing boot script in 1.000 seconds - enter ^C to abort
^C
RedBoot> load -r -b %{FREEMEMLO} ls2.rom
Using default protocol (TFTP)
Raw file loaded 0x8003dc00-0x800664ef, assumed entry at 0x8003dc00 
RedBoot> fis create RedBoot
An image named 'RedBoot' exists - continue (y/n)? y
... Erase from 0xbfc00000-0xbfc30000: ...
... Program from 0x8003dc00-0x800664f0 at 0xbfc00000: ...
... Erase from 0xbffe0000-0xbfff0000: .
... Program from 0x807f0000-0x80800000 at 0xbffe0000: .
RedBoot> reset
... Resetting.
}}}

If everything went well, you will see the following:

{{{
+Ethernet eth0: MAC address 00:15:6d:e0:03:19
IP: 192.168.1.20/255.255.255.0, Gateway: 0.0.0.0
Default server: 192.168.1.254
 
RedBoot(tm) bootstrap and debug environment [ROMRAM]
OpenWrt certified release, version 1.0 - built 01:18:43, Jan 21 2007
 
Copyright (C) 2000, 2001, 2002, 2003, 2004 Red Hat, Inc.
 
Board: Ubiquiti LiteStation2
RAM: 0x80000000-0x81000000, [0x80040770-0x80fe1000] available
FLASH: 0xbfc00000 - 0xbfff0000, 64 blocks of 0x00010000 bytes each.
== Executing boot script in 1.000 seconds - enter ^C to abort
^C
RedBoot>
}}}

=== Installing OpenWrt ===

After we've changed the bootloader, it's time to install OpenWrt.
First we have to delete the factory partitions:

{{{
RedBoot> fis delete cfg
Delete image 'cfg' - continue (y/n)? y
... Erase from 0xbffc0000-0xbffe0000: ..
... Erase from 0xbffe0000-0xbfff0000: .
... Program from 0x80ff0000-0x81000000 at 0xbffe0000: .
RedBoot> fis delete cramfs
Delete image 'cramfs' - continue (y/n)? y
... Erase from 0xbfd00000-0xbffc0000: ..........................................
..
... Erase from 0xbffe0000-0xbfff0000: .
... Program from 0x80ff0000-0x81000000 at 0xbffe0000: .
RedBoot> fis delete kernel
Delete image 'kernel' - continue (y/n)? y
... Erase from 0xbfc30000-0xbfd00000: .............
... Erase from 0xbffe0000-0xbfff0000: .
... Program from 0x80ff0000-0x81000000 at 0xbffe0000: .
RedBoot>
}}}

Then create the new ones:

{{{
RedBoot> load -r -b %{FREEMEMLO} openwrt-atheros-2.6-vmlinux.lzma
Using default protocol (TFTP)
Raw file loaded 0x80040800-0x800f07ff, assumed entry at 0x80040800
RedBoot> fis create -r 0x80041000 -e 0x80041000 kernel
... Erase from 0xbfc30000-0xbfce0000: ...........
... Program from 0x80040800-0x800f0800 at 0xbfc30000: ...........
... Erase from 0xbffe0000-0xbfff0000: .
... Program from 0x80ff0000-0x81000000 at 0xbffe0000: .
RedBoot> load -r -b %{FREEMEMLO} openwrt-atheros-2.6-root.jffs2-64k
Using default protocol (TFTP)
Raw file loaded 0x80040800-0x802007ff, assumed entry at 0x80040800
RedBoot> fis create -l 0x300000 rootfs
... Erase from 0xbfce0000-0xbffe0000: ................................................
... Program from 0x80040800-0x80200800 at 0xbfce0000: ............................
... Erase from 0xbffe0000-0xbfff0000: .
... Program from 0x80ff0000-0x81000000 at 0xbffe0000: .
RedBoot>
}}}

We have to modify the bootscript via the "fconfig" command:

{{{
RedBoot> fconfig
Run script at boot: true
Boot script: 
.. cache off
.. fis load kernel -d -e
.. go
Enter script, terminate with empty line
>> fis load -l kernel
>> exec
>> 
Boot script timeout (1000ms resolution): 1
Use BOOTP for network configuration: false
Gateway IP address: 
Local IP address: 192.168.1.20
Local IP address mask: 255.255.255.0
Default server IP address: 192.168.1.254
Console baud rate: 9600
GDB connection port: 9000
Force console for special debug messages: false
Network debug at boot time: false
Update RedBoot non-volatile configuration - continue (y/n)? y
... Erase from 0xbffe0000-0xbfff0000: .
... Program from 0x80ff0000-0x81000000 at 0xbffe0000: .
RedBoot>
}}}

Now we only have to reboot into OpenWrt :) Enjoy!

{{{
RedBoot> reset
... Resetting.+Ethernet eth0: MAC address 00:15:6d:e0:03:19
IP: 192.168.1.20/255.255.255.0, Gateway: 0.0.0.0
Default server: 192.168.1.254

RedBoot(tm) bootstrap and debug environment [ROMRAM]
OpenWrt certified release, version 1.0 - built 01:18:43, Jan 21 2007

Copyright (C) 2000, 2001, 2002, 2003, 2004 Red Hat, Inc.

Board: Ubiquiti LiteStation2 
RAM: 0x80000000-0x81000000, [0x80040770-0x80fe1000] available
FLASH: 0xbfc00000 - 0xbfff0000, 64 blocks of 0x00010000 bytes each.
== Executing boot script in 1.000 seconds - enter ^C to abort
RedBoot> fis load -l kernel
Image loaded from 0x80041000-0x8028c086
RedBoot> exec
Now booting linux kernel:
 Base address 0x80030000 Entry 0x80041000
 Cmdline : 

Linux version 2.6.19.2 (kaloz@ecaz) (gcc version 3.4.6 (OpenWrt-2.0)) #1 Sat Jan 20 23:07:13 CET 2007
CPU revision is: 00019064
Determined physical RAM map:
 memory: 01000000 @ 00000000 (usable)
Initrd not found or empty - disabling initrd
On node 0 totalpages: 4096
  DMA zone: 32 pages used for memmap
  DMA zone: 0 pages reserved
  DMA zone: 4064 pages, LIFO batch:0
  Normal zone: 0 pages used for memmap
Built 1 zonelists.  Total pages: 4064
Kernel command line: console=ttyS0,9600 rootfstype=squashfs,jffs2
Primary instruction cache 16kB, physically tagged, 4-way, linesize 16 bytes.
Primary data cache 16kB, 4-way, linesize 16 bytes.
Synthesized TLB refill handler (20 instructions).
Synthesized TLB load handler fastpath (32 instructions).
Synthesized TLB store handler fastpath (32 instructions).
Synthesized TLB modify handler fastpath (31 instructions).
PID hash table entries: 64 (order: 6, 256 bytes)
Using 92.000 MHz high precision timer.
Dentry cache hash table entries: 2048 (order: 1, 8192 bytes)
Inode-cache hash table entries: 1024 (order: 0, 4096 bytes)
Memory: 13516k/16384k available (1966k kernel code, 2868k reserved, 273k data, 116k init, 0k highmem)
Calibrating delay loop... 183.50 BogoMIPS (lpj=917504)
Mount-cache hash table entries: 512
Checking for 'wait' instruction...  available.
NET: Registered protocol family 16
Radio config found at offset 0xf8
NET: Registered protocol family 2
IP route cache hash table entries: 128 (order: -3, 512 bytes)
TCP established hash table entries: 512 (order: -1, 2048 bytes)
TCP bind hash table entries: 256 (order: -2, 1024 bytes)
TCP: Hash tables configured (established 512 bind 256)
TCP reno registered
squashfs: version 3.0 (2006/03/15) Phillip Lougher
devfs: 2004-01-31 Richard Gooch (rgooch@atnf.csiro.au)
devfs: boot_options: 0x1
JFFS2 version 2.2. (NAND) (C) 2001-2006 Red Hat, Inc.
io scheduler noop registered
io scheduler deadline registered (default)
Serial: 8250/16550 driver $Revision: 1.90 $ 1 ports, IRQ sharing disabled
serial8250: ttyS0 at MMIO 0xb1100003 (irq = 37) is a 16550A
eth0: Dropping NETIF_F_SG since no checksum feature.
eth0: Atheros AR2313: 00:15:6d:e0:03:08, irq 4
MTD driver for SPI flash.
spiflash: Probing for Serial flash ...
spiflash: Found SPI serial Flash.
cmdlinepart partition parsing not available
Searching for RedBoot partition table in spiflash at offset 0x3d0000
Searching for RedBoot partition table in spiflash at offset 0x3e0000
5 RedBoot partitions found on MTD device spiflash
Creating 6 MTD partitions on "spiflash":
0x00000000-0x00030000 : "RedBoot"
0x00030000-0x000e0000 : "kernel"
0x000e0000-0x003d0000 : "rootfs"
0x003e0000-0x003ef000 : "FIS directory"
0x003ef000-0x003f0000 : "RedBoot config"
0x003f0000-0x00400000 : "board_config"
ip_conntrack version 2.4 (128 buckets, 1024 max) - 240 bytes per conntrack
ip_tables: (C) 2000-2006 Netfilter Core Team
TCP vegas registered
NET: Registered protocol family 1
NET: Registered protocol family 17
Bridge firewalling registered
802.1Q VLAN Support v1.8 Ben Greear <greearb@candelatech.com>
All bugs added by David S. Miller <davem@redhat.com>
Time: MIPS clocksource has been installed.
jffs2_scan_eraseblock(): End of filesystem marker found at 0x150000
jffs2_build_filesystem(): unlocking the mtd device... done.
jffs2_build_filesystem(): erasing all blocks after the end marker... done.
VFS: Mounted root (jffs2 filesystem) readonly.
Mounted devfs on /dev
Freeing firmware memory: 25k freed
Freeing unused kernel memory: 116k freed
Algorithmics/MIPS FPU Emulator v1.5
wlan: 0.8.4.2 (0.9.2.1)
ath_hal: module license 'Proprietary' taints kernel.
ath_hal: 0.9.17.2 (AR5212, AR5312, RF2316, TX_DESC_SWAP)
ath_rate_sample: 1.2 (0.9.2.1)
wlan: mac acl policy registered
ath_ahb: 0.9.4.5 (0.9.2.1)
ath_pci: switching rfkill capability off
wifi0: 11b rates: 1Mbps 2Mbps 5.5Mbps 11Mbps
wifi0: 11g rates: 1Mbps 2Mbps 5.5Mbps 11Mbps 6Mbps 9Mbps 12Mbps 18Mbps 24Mbps 36Mbps 48Mbps 54Mbps
wifi0: turboG rates: 6Mbps 12Mbps 18Mbps 24Mbps 36Mbps 48Mbps 54Mbps
wifi0: H/W encryption support: WEP AES AES_CCM TKIP
wifi0: mac 11.0 phy 4.8 radio 7.0
wifi0: Use hw queue 1 for WME_AC_BE traffic
wifi0: Use hw queue 0 for WME_AC_BK traffic
wifi0: Use hw queue 2 for WME_AC_VI traffic
wifi0: Use hw queue 3 for WME_AC_VO traffic
wifi0: Use hw queue 8 for CAB traffic
wifi0: Use hw queue 9 for beacons
wifi0: Atheros 2315 WiSoC: mem=0xb0000000, irq=3
Please press Enter to activate this console.

BusyBox v1.3.1 (2007-01-20 22:28:20 CET) Built-in shell (ash)
Enter 'help' for a list of built-in commands.

  _______                     ________        __
 |       |.-----.-----.-----.|  |  |  |.----.|  |_
 |   -   ||  _  |  -__|     ||  |  |  ||   _||   _|
 |_______||   __|_____|__|__||________||__|  |____|
          |__| W I R E L E S S   F R E E D O M
 KAMIKAZE (bleeding edge, r6148) -------------------
  * 10 oz Vodka       Shake well with ice and strain
  * 10 oz Triple sec  mixture into 10 shot glasses.
  * 10 oz lime juice  Salute!
 ---------------------------------------------------
root@OpenWrt:/#
}}}
