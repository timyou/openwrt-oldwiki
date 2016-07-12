[[TableOfContents(3)]]

= Hardware Overview =

{{{
Bootloader: RedBoot
CPU: Atheros AR2315
CPU Speed: 180 Mhz
Flash size: 8 MB
RAM: 32 MB
Wireless: integrated Atheros 802.11b/g
Ethernet: 1xLAN
USB: none
Serial: yes
JTAG: yes
}}}

Serial port (labeled JP1, @115200bps):

{{{
      VCC o
LAN   RX  o   Antenna
      TX  o
      GND o
}}}

== Opening the case ==

Peel off the bottom left and top right corners of the silver label on the back of the unit, to reveal two crosspoint screws. Remove them, then prise apart the case with a screwdriver.

== Serial to USB adaptor ==

Meraki sell a small adaptor board (18mm x 32mm) for $29 which plugs into JP1 and has a serial to USB adaptor chip and a mini USB connector; it comes with a mini USB to normal USB cable. It appears to be powered by the host side, not the Meraki side. Plugging it into a Linux system shows:

{{{
usb 2-1: new full speed USB device using address 3
ftdi_sio 2-1:1.0: FTDI FT232BM Compatible converter detected
usb 2-1: FTDI FT232BM Compatible converter now attached to ttyUSB0
usbcore: registered new driver ftdi_sio
drivers/usb/serial/ftdi_sio.c: v1.4.1:USB FTDI Serial Converters Driver
}}}

It is not polarised, but the correct way round is so that it overhangs the RF module, and doesn't hang out of the side of the case. Minicom set to /dev/ttyUSB0 and 115200 8N1 works.  Also make sure that you turn off flow-control.

I found the USB adaptor was somewhat unreliable under Linux; power-cycling the Meraki made it freeze, so I had to unplug and reconnect the USB connection to the host as well. This was both with CentOS 4.3 (2.6.9) and Ubuntu 6.06 (2.6.15). A more reliable sequence was:
 * Unplug JP1
 * Remove power from Meraki
 * Re-apply power to Meraki
 * Reconnect JP1

on ubuntu efty kernel 2.6.19.1 same behavior with pl2303 from siemens datacabel and la_fonera FON2100 (nearly identical hw,but 8/16 MB Flash)

= Standard Meraki firmware =

== Startup messages ==

[captured from serial port, with ethernet port not connected]

{{{
Ethernet eth0: MAC address 00:18:0a:XX:XX:XX
IP: 192.168.84.1/255.255.255.0, Gateway: 0.0.0.0
Default server: 192.168.84.9

RedBoot(tm) bootstrap and debug environment [ROMRAM]
Release, version V1.04 - built 12:24:00, Apr 17 2006

Copyright (C) 2000, 2001, 2002, 2003, 2004 Red Hat, Inc.

Board: Meraki Mini
RAM: 0x80000000-0x82000000, [0x8003d110-0x80fe1000] available
FLASH: 0xa8000000 - 0xa87e0000, 128 blocks of 0x00010000 bytes each.
== Executing boot script in 2.000 seconds - enter ^C to abort
RedBoot> check_mac
Lan Mac address is  : 00:18:0a:XX:XX:XX
Wlan Mac address is : 00:18:0a:XX:XX:XX
Serial Number is    : XXX-XXX-XXX
RedBoot> load art_ap51.elf
Using default protocol (TFTP)
__udp_sendto: Can't find address of server
Can't load 'art_ap51.elf': some sort of network error
RedBoot> go
No entry point known - aborted
RedBoot> load -h 192.168.84.9 -p 80 -m http /meraki/mini.1.img
Unable to reach host 192.168.84.9 (192.168.84.9)
RedBoot> exec
Can't execute Linux - invalid entry address
RedBoot> fis load stage2
RedBoot> exec
Now booting linux kernel:
 Base address 0x80030000 Entry 0x80100000
 Cmdline :
starting stage2
reading flash at 0xa8150000 - 0xa8452927... done
Calculating CRC... 0x727b3da7 - matches
decompressing... done
starting linux
Linux version 2.6.16.16-meraki-mini (jbicket@high.meraki.net) (gcc version 3.4.6 (OpenWrt-2.0)) #8 Fri Nov 3 11:36:22 PST 2006
CPU revision is: 00019064
Determined physical RAM map:
 memory: 02000000 @ 00000000 (usable)
Built 1 zonelists
Kernel command line:
Primary instruction cache 16kB, physically tagged, 4-way, linesize 16 bytes.
Primary data cache 16kB, 4-way, linesize 16 bytes.
Synthesized TLB refill handler (20 instructions).
Synthesized TLB load handler fastpath (32 instructions).
Synthesized TLB store handler fastpath (32 instructions).
Synthesized TLB modify handler fastpath (31 instructions).
PID hash table entries: 256 (order: 8, 4096 bytes)
Using 92.000 MHz high precision timer.
Dentry cache hash table entries: 8192 (order: 3, 32768 bytes)
Inode-cache hash table entries: 4096 (order: 2, 16384 bytes)
Memory: 19940k/32768k available (2121k kernel code, 12812k reserved, 394k data, 9592k init, 0k highmem)
Mount-cache hash table entries: 512
Checking for 'wait' instruction...  available.
unpacking initramfs....done
NET: Registered protocol family 16
Algorithmics/MIPS FPU Emulator v1.5
JFFS2 version 2.2. (NAND) (C) 2001-2003 Red Hat, Inc.
Initializing Cryptographic API
io scheduler noop registered
io scheduler anticipatory registered (default)
io scheduler deadline registered
io scheduler cfq registered
faulty_init
watchdog hb: 90  ISR: 0x21  IMR: 0x8  WD : 0x86b43edd  WDC: 0x0
ar2315_wdt_init using heartbeat 90 s cycles 3600000000
watchdog hb: 90  ISR: 0x21  IMR: 0x88  WD : 0xd68e68bd  WDC: 0x0
Serial: 8250/16550 driver $Revision: 1.90 $ 1 ports, IRQ sharing disabled
serial8250: ttyS0 at MMIO 0xb1100003 (irq = 37) is a 16550A
tun: Universal TUN/TAP device driver, 1.6
tun: (C) 1999-2004 Max Krasnyansky <maxk@qualcomm.com>
setting one ethernet device to null...
MTD driver for SPI flash.
spiflash: Probing for Serial flash ...
spiflash: Found SPI serial Flash.
8388608: size
RedBoot partition parsing not available
Creating 7 MTD partitions on "spiflash":
0x00000000-0x00030000 : "RedBoot"
0x00030000-0x00050000 : "stage2"
0x00050000-0x00150000 : "/storage"
0x00150000-0x00490000 : "part1"
0x00490000-0x007d0000 : "part2"
0x007d0000-0x007e0000 : "redboot config"
0x007e0000-0x00800000 : "board config"
oprofile: using timer interrupt.
NET: Registered protocol family 2
IP route cache hash table entries: 512 (order: -1, 2048 bytes)
TCP established hash table entries: 2048 (order: 2, 16384 bytes)
TCP bind hash table entries: 2048 (order: 2, 16384 bytes)
TCP: Hash tables configured (established 2048 bind 2048)
TCP reno registered
ip_conntrack version 2.4 (256 buckets, 2048 max) - 232 bytes per conntrack
ip_conntrack_pptp version 3.1 loaded
ip_nat_pptp version 3.0 loaded
ip_tables: (C) 2000-2006 Netfilter Core Team
ClusterIP Version 0.8 loaded successfully
TCP bic registered
NET: Registered protocol family 1
NET: Registered protocol family 17
Freeing unused kernel memory: 9592k freed
init started:  BusyBox v1.1.0 (2006.09.29-21:24+0000) multi-call binary

Please press Enter to activate this console. ar2315_wdt: starting watchdog w/timeout 90 seconds
watchdog hb: 90  ISR: 0x20  IMR: 0x89  WD : 0xd6918293  WDC: 0x0
ath_hal: module license 'Proprietary' taints kernel.
ath_hal: 0.9.17.2 (AR5212, AR5312, RF2316, TX_DESC_SWAP)
wlan: 0.8.4.2 (svn 2943)
ath_rate_sample: 1.2 (svn 2943)
ath_ahb: 0.9.4.5 (svn 2943)
wifi0: 11b rates: 1Mbps 2Mbps 5.5Mbps 11Mbps
wifi0: 11g rates: 1Mbps 2Mbps 5.5Mbps 11Mbps 6Mbps 9Mbps 12Mbps 18Mbps 24Mbps 36Mbps 48Mbps 54Mbps
wifi0: H/W encryption support: WEP AES AES_CCM TKIP
wifi0: mac 11.0 phy 4.8 radio 7.0
wifi0: Use hw queue 1 for WME_AC_BE traffic
wifi0: Use hw queue 0 for WME_AC_BK traffic
wifi0: Use hw queue 2 for WME_AC_VI traffic
wifi0: Use hw queue 3 for WME_AC_VO traffic
wifi0: Use hw queue 8 for CAB traffic
wifi0: Use hw queue 9 for beacons
couldn't load module 'wlan_scan_sta' (-89)
unable to load wlan_scan_sta
wifi0: Atheros 2315 WiSoC: mem=0xb0000000, irq=3
click: starting router thread pid 394 (802ecb00)
wlan: mac acl policy registered
realtek setup
couldn't load module 'wlan_scan_monitor' (-89)
unable to load wlan_scan_monitor
ath0: start running
ath0: __ieee80211_newstate: INIT -> RUN
ath0: __ieee80211_newstate: RUN -> RUN
ath0: stop running
ath0: __ieee80211_newstate: RUN -> INIT
ath0: __ieee80211_newstate: INIT -> RUN
ath0: __ieee80211_newstate: RUN -> RUN
ath0: start running
ath0: __ieee80211_newstate: RUN -> INIT
ath0: __ieee80211_newstate: INIT -> RUN
ath0: __ieee80211_newstate: RUN -> RUN
ath0: stop running
ath0: __ieee80211_newstate: RUN -> INIT
ath0: __ieee80211_newstate: INIT -> RUN
ath0: __ieee80211_newstate: RUN -> RUN
...etc
}}}

== Network activity ==

Plugging in the ethernet port to another host and running tcpdump there while the unit is booting up shows:

 1. Unit ARPs for 192.168.84.1 eight times (checking its address is not in use by anyone else)
 1. Unit ARPs for 192.168.84.9. If successful:
  1. Unit attempts to make TFTP (UDP) request to 192.168.84.9 to get '''art_ap51.elf'''
  1. Unit attempts to make HTTP request to 192.168.84.9 to '''GET /meraki/mini.1.img'''
 1. Picks up new IP address via DHCP
 1. Sends UDP packet to 64.62.142.12:7351
 1. Makes DNS lookups for config.meraki.net. and db.meraki.net.

So it looks like there are at least two different ways to download new firmware at power-up.

== ssh access ==

Once the unit has picked up an IP address via DHCP, and you've found it (e.g. using nmap or looking at the upstream router's ARP cache), you can ssh in. The username is 'meraki' and the password is the SN displayed on the bottom of the unit, in the form XXX-XXX-XXX (including the dashes)

{{{
# ssh meraki@x.x.x.x
meraki@x.x.x.x's password:


BusyBox v1.1.0 (2006.09.29-21:24+0000) Built-in shell (ash)
Enter 'help' for a list of built-in commands.

http://meraki.net

Welcome to your meraki mini.  Please look for developer information at
http://meraki.net.  We would like to encourage you to play with this
platform and add your own features to it.  However, our lawyers
require us to tell you that much of the software on this device is
protected by copyrights, and may not be redistributed or sold.

Happy Hacking!
root@meraki-node:~# id
uid=0(root) gid=0(root)
root@meraki-node:~# mount
none on /proc type proc (rw)
/dev/mtdblock2 on /storage type jffs2 (rw)
none on /tmp type tmpfs (rw,nosuid,nodev)
none on /dev/pts type devpts (rw)
none on /sys type sysfs (rw)
none on /click type click (rw)
root@meraki-node:~# df -k
Filesystem           1k-blocks      Used Available Use% Mounted on
/dev/mtdblock2            1024       232       792  23% /storage
none                     14772        76     14696   1% /tmp
df: /click: Function not implemented
root@meraki-node:~# cat /proc/mtd
dev:    size   erasesize  name
mtd0: 00030000 00010000 "RedBoot"
mtd1: 00020000 00010000 "stage2"
mtd2: 00100000 00010000 "/storage"
mtd3: 00340000 00010000 "part1"
mtd4: 00340000 00010000 "part2"
mtd5: 00010000 00010000 "redboot config"
mtd6: 00020000 00010000 "board config"
mtd7: 00800000 00010000 "spiflash"
}}}

The root filesystem is not listed as a mount. It's writeable, but changes are lost on reboot, so presumably it's a ramdisk.

The installed software is quite comprehensive, even including a ruby intepreter. Given that you have root access to the box, and can install your own programs and data in the /storage partition, you might not feel the need to install OpenWrt. But if you do, here's how to.

== Backing up existing firmware ==

If you rebuild Meraki's own released firmware (see below), it produces a script build_ar531x/upgrade.sh which you copy to the Meraki (e.g. with scp) and then run. This script simply overwrites the "stage2", "redboot config", "part1" and "part2" partitions using dd.

So logically you should be able to restore the device to its original state by backing these up:

{{{
ssh meraki@x.x.x.x 'dd if=/dev/mtd1 bs=64k' >stage2.bak
ssh meraki@x.x.x.x 'dd if=/dev/mtd3 bs=64k' >part1.bak
ssh meraki@x.x.x.x 'dd if=/dev/mtd4 bs=64k' >part2.bak
ssh meraki@x.x.x.x 'dd if=/dev/mtd5 bs=64k' >redboot-config.bak
}}}

In practice you'll probably find that part1.bak and part2.bak are identical. If you dd /dev/mtd7, you'll get an 8MB file which is the same as the first 7 partitions concatenated together.

Note1: the "board config" partition contains the unit's MAC address and SN (secret password); you should probably never overwrite this partition.

Note2: when comparing two different Meraki Minis, the stage2, part1 and redboot-config partitions are identical between them.

== Restoring flash using serial console ==

About 13 seconds after applying power, there is a two-second window when you can press ctrl-C to get into the boot loader.

{{{
== Executing boot script in 2.000 seconds - enter ^C to abort
^C
RedBoot>
}}}

The [http://ecos.sourceware.org/docs-latest/redboot/redboot-guide.html RedBoot User's Guide] gives some guidance as to what you can do here, although the version used by Meraki appears to be customised.

Now, looking at the partition info above gives the following partition offsets and sizes:

{{{
                   start    size
mtd0 RedBoot       000000   030000
mtd1 stage2        030000   020000
mtd2 /storage      050000   100000
mtd3 part1         150000   340000
mtd4 part2         490000   340000
mtd5 redboot conf  7d0000   010000
mtd6 board conf    7e0000   020000
}}}

Unfortunately, the Meraki's !RedBoot is missing the load -f (load to flash) command, so you first have to load to RAM and then write to flash.

{{{
RedBoot> version

RedBoot(tm) bootstrap and debug environment [ROMRAM]
Release, version V1.04 - built 12:24:00, Apr 17 2006

Copyright (C) 2000, 2001, 2002, 2003, 2004 Red Hat, Inc.

Board: Meraki Mini
RAM: 0x80000000-0x82000000, [0x8003d110-0x80fe1000] available
FLASH: 0xa8000000 - 0xa87e0000, 128 blocks of 0x00010000 bytes each.
RedBoot> load -r -b 0x80150000 -m tftp -h 192.168.84.9 part1.bak
Raw file loaded 0x80150000-0x8048ffff, assumed entry at 0x80150000
RedBoot> fis write -b 0x80150000 -l 0x340000 -f 0xa8150000
* CAUTION * about to program FLASH
            at 0xa8150000..0xa848ffff from 0x80150000 - continue (y/n)? y
... Erase from 0xa8150000-0xa8490000: ..........................................
... Program from 0x80150000-0x80490000 at 0xa8150000: ..........................
RedBoot> reset
... Resetting.
}}}

You can repeat this for the other partitions backed up. (However, after I broke my Meraki by installing firmware built from Meraki's source - see below - the new stage2 and reboot config partitions were fine, and I only needed to restore part1 to get my Meraki back to how it was)

== RedBoot configuration ==

The default !RedBoot config does the following:

{{{
RedBoot> fconfig -l
Run script at boot: true
Boot script:
.. check_mac
.. load art_ap51.elf
.. go
.. load -h 192.168.84.9 -p 80 -m http /meraki/mini.1.img
.. exec
.. fis load stage2
.. exec

Boot script timeout (1000ms resolution): 2
Use BOOTP for network configuration: false
Gateway IP address: 0.0.0.0
Local IP address: 192.168.84.1
Local IP address mask: 255.255.255.0
Default server IP address: 192.168.84.9
Console baud rate: 115200
GDB connection port: 9000
Force console for special debug messages: false
Network debug at boot time: false
RedBoot>
}}}

If you want to change this, you can use 'fconfig' at the serial port command prompt, which prompts interactively for each item.

This information is stored in the 'redboot conf' partition.

== Stage 2 boot loader ==

Meraki's firmware includes a stage 2 boot loader, run by "fis load stage2" and "exec". The source for this is in the Meraki tarball (see below) in openwrt-meraki/base/stage2. The entry point is entry() in openwrt-meraki/base/stage2/decompress.c

It reads "part1", checking for a valid CRC. If not valid it boots from "part2" instead. It also includes an LZMA decompressor. These partition locations are hard-coded into the stage2 loader itself:

{{{
#define PART1_ADDR                              0xa8150000
#define PART2_ADDR                              0xa8490000
}}}

This means that if you want to use Meraki's stage2 loader with !OpenWrt, then:
 1. You must use the same partitioning arrangement as Meraki
 1. The kernel must be LZMA compressed
 1. The kernel must be prepended with an 8-byte header (4 bytes length, 4 bytes bastardised CRC32 - see below)

It would be useful to retain Meraki's stage2 loader, if only because Meraki's RedBoot doesn't have an LZMA decompressor (fis load -l) which apparently Fonera does. It also avoids having to mess with RedBoot configuration, making it easier to install !OpenWrt without a serial port.

= Building OpenWrt =

Support for the Atheros System-on-Chip used by the Meraki Mini was [https://dev.openwrt.org/changeset/5898 recently added] to Kamikaze SVN trunk. Hence there is currently no released code you can run; you must build it yourself from scratch.

Check out SVN trunk, use 'make menuconfig', select Atheros 2.6 as the target, and then 'make'. When this is complete, you will have the following files in the bin/ subdirectory:

{{{
openwrt-atheros-2.6-root.jffs2-128k
openwrt-atheros-2.6-root.jffs2-64k
openwrt-atheros-2.6-vmlinux.elf
openwrt-atheros-2.6-vmlinux.gz
openwrt-atheros-2.6-vmlinux.lzma
}}}

== Kernel parameters ==

Even though RedBoot can pass a command line to the kernel, currently any user-provided value is overridden by a hardcoded string - see 
target/linux/atheros-2.6/patches/100-board.patch
{{{
+    strcpy(arcs_cmdline, "console=ttyS0,9600 rootfstype=squashfs,jffs2");
}}}

If you wish, you can change the console speed to 115200 here to match the value used by RedBoot. Alternatively you can reconfigure !RedBoot to use 9600bps (see below). Apparently it's also possible to comment this line out to allow the kernel command line provided by !RedBoot to be used.

Also hardcoded is the FIS partition name of the root filesystem which is "rootfs" - see target/linux/atheros-2.6/patches/110-spiflash.patch
{{{
+#define ROOTFS_NAME    "rootfs"
}}}

== Using a ramdisk root ==

If you select "target images" and change to "ramdisk" you'll get the following:

{{{
openwrt-atheros-2.6-vmlinux.elf
openwrt-atheros-2.6-vmlinux.gz
openwrt-atheros-2.6-vmlinux.lzma
}}}

This gives a single image which contains both the kernel and the root filesystem which runs from ramdisk. This is useful when trying to install on a machine where you don't have a serial console (see later)

== Using a squashfs root ==

TBD (it would be very nice if a single flash partition could contain a kernel + fixed squashfs filesystem, with the remaining space as a writable jffs2 filesystem, as you get on Broadcom devices)

= Installing OpenWrt using serial console =

Connect a serial port (115200 8N1, no flow control) to the Meraki and power up. Keep hitting ctrl-C until you get to the RedBoot> prompt; this takes about 13 seconds.

{{{
Board: Meraki Mini
RAM: 0x80000000-0x82000000, [0x8003d110-0x80fe1000] available
FLASH: 0xa8000000 - 0xa87e0000, 128 blocks of 0x00010000 bytes each.
== Executing boot script in 2.000 seconds - enter ^C to abort
^C
RedBoot>
}}}

At this point, it's a good idea to change the serial port speed to 9600 bps, since this is the speed at which the kernel will use (unless you've modified the source)

{{{
RedBoot> baudrate -b 9600
Baud rate will be changed to 9600 - update your settings
}}}

Change your terminal's serial port speed to 9600 (Minicom: Ctrl-A P E) and hit Enter to check it's working.

Configure your PC as 192.168.84.9 and configure it with either a tftp server or http server containing the files from the bin/ directory.

== Testing kernel via tftp or http ==

This lets you test your new kernel without touching the flash at all, by loading the kernel directly over the network:

{{{
RedBoot> load -r -d -b 0x80041000 -m tftp -h 192.168.84.9 openwrt-atheros-2.6-vmlinux.gz
Raw file loaded 0x80041000-0x8028e085, assumed entry at 0x80041000
RedBoot> exec
Now booting linux kernel:
 Base address 0x80030000 Entry 0x80041000
 Cmdline :
Linux version 2.6.19.1 (candlerb@candlerb-desktop) (gcc version 3.4.6 (OpenWrt-7CPU revision is: 00019064
... etc
Please append a correct "root=" boot option
Kernel panic - not syncing: VFS: Unable to mount root fs on unknown-block(1,0)
}}}

This problem will go away when you have a FIS partition called "rootfs". (Or you could use a ramdisk kernel)

== Create flash partitions ==

Now, the first thing to notice is that the Meraki's flash partition map doesn't include 'part1' and 'part2' entries. This is because the Meraki stage2 bootloader has these addresses hard-coded within it instead of reading the flash map (naughty).

{{{
RedBoot> fis load -d part1
No image 'part1' found
RedBoot> fis list
Name              FLASH addr  Mem addr    Length      Entry point
RedBoot           0xA8000000  0xA8000000  0x00030000  0x00000000
stage2            0xA8030000  0x80100000  0x00020000  0x80100000
FIS directory     0xA87D0000  0xA87D0000  0x0000F000  0x00000000
RedBoot config    0xA87DF000  0xA87DF000  0x00001000  0x00000000
RedBoot>
}}}

So let's create them. The name of the kernel partition doesn't matter (let's call it "linux"). However the rootfs partition must be called "rootfs" otherwise the kernel won't be able to find it.

{{{
RedBoot> fis create -b 0x80041000 -l 0x340000 -f 0xa8150000 -e 0x80041000 -r 0x80041000 -n linux
... Erase from 0xa87d0000-0xa87e0000: .
... Program from 0x80ff0000-0x81000000 at 0xa87d0000: .
RedBoot> fis create -b 0x80041000 -l 0x340000 -f 0xa8490000 -e 0x80041000 -r 0x80041000 -n rootfs
... Erase from 0xa87d0000-0xa87e0000: .
... Program from 0x80ff0000-0x81000000 at 0xa87d0000: .
RedBoot> fis list
Name              FLASH addr  Mem addr    Length      Entry point
RedBoot           0xA8000000  0xA8000000  0x00030000  0x00000000
stage2            0xA8030000  0x80100000  0x00020000  0x80100000
linux             0xA8150000  0x80041000  0x00340000  0x80041000
rootfs            0xA8490000  0x80041000  0x00340000  0x80041000
FIS directory     0xA87D0000  0xA87D0000  0x0000F000  0x00000000
RedBoot config    0xA87DF000  0xA87DF000  0x00001000  0x00000000
RedBoot>
}}}

== Booting directly from RedBoot ==

In this configuration, we will bypass Meraki's stage2 boot loader; RedBoot will load, decompress and run the kernel directly.

Here we assume you've built a kernel plus jffs2 root filesystem (the default). We'll put these in Meraki's 'part1' and 'part2' respectively, keeping the Meraki's existing partitioning scheme. Both partitions are 3.25MB.

=== Flash the kernel and root filesystem ===

Now we fetch the files and write them to flash (it seems 0x80041000 is the magic kernel entry point for Linux; the jffs2 partition doesn't need this but it doesn't do any harm to have it)

{{{
RedBoot> load -r -b 0x80041000 -m tftp -h 192.168.84.9 openwrt-atheros-2.6-vmlinux.gz
Raw file loaded 0x80041000-0x80140fff, assumed entry at 0x80041000
RedBoot> fis create -r 0x80041000 -e 0x80041000 linux
An image named 'linux' exists - continue (y/n)? y
... Erase from 0xa8150000-0xa8490000: ....................................................
... Program from 0x80041000-0x80141000 at 0xa8150000: ................
... Erase from 0xa87d0000-0xa87e0000: .
... Program from 0x80ff0000-0x81000000 at 0xa87d0000: .
RedBoot> load -r -b 0x80041000 -m tftp -h 192.168.84.9 openwrt-atheros-2.6-root.jffs2-64k
Raw file loaded 0x80041000-0x801c0fff, assumed entry at 0x80041000
RedBoot> fis create -r 0x80041000 -e 0x80041000 rootfs
An image named 'rootfs' exists - continue (y/n)? y
... Erase from 0xa8490000-0xa87d0000: ....................................................
... Program from 0x80041000-0x801c1000 at 0xa8490000: ................
... Erase from 0xa87d0000-0xa87e0000: .
... Program from 0x80ff0000-0x81000000 at 0xa87d0000: .
RedBoot>
}}}

You can now try to boot directly from the !RedBoot command line:

{{{
RedBoot> fis load -d linux
[This takes about 40 seconds; RedBoot is slow to decompress!]
Image loaded from 0x80041000-0x8028e086
RedBoot> exec
Now booting linux kernel:
 Base address 0x80030000 Entry 0x80041000
 Cmdline :
Linux version 2.6.19.1 (candlerb@candlerb-desktop) (gcc version 3.4.6 (OpenWrt-2.0)) #1 Tue Jan 2 14:07:20 GMT 2007
...
Jan  1 00:00:43 (none) user.info kernel: Time: MIPS clocksource has been installed.
Jan  1 00:00:43 (none) user.warn kernel: jffs2_scan_eraseblock(): End of filesystem marker found at 0x170000
Jan  1 00:00:43 (none) user.warn kernel: jffs2_build_filesystem(): unlocking the mtd device... done.
Jan  1 00:00:43 (none) user.warn kernel: jffs2_build_filesystem(): erasing all blocks after the end marker... done.
Jan  1 00:00:43 (none) user.warn kernel: VFS: Mounted root (jffs2 filesystem) readonly.
...

}}}

Now hit Enter for a shell:

{{{
Jan  1 00:01:28 (none) daemon.info init: Starting pid 67, console /dev/tts/0: '/bin/ash'


BusyBox v1.3.1 (2007-01-02 13:55:25 GMT) Built-in shell (ash)
Enter 'help' for a list of built-in commands.

  _______                     ________        __
 |       |.-----.-----.-----.|  |  |  |.----.|  |_
 |   -   ||  _  |  -__|     ||  |  |  ||   _||   _|
 |_______||   __|_____|__|__||________||__|  |____|
          |__| W I R E L E S S   F R E E D O M
 KAMIKAZE (bleeding edge, r5968) -------------------
  * 10 oz Vodka       Shake well with ice and strain
  * 10 oz Triple sec  mixture into 10 shot glasses.
  * 10 oz lime juice  Salute!
 ---------------------------------------------------
root@OpenWrt:/# mount
/dev/root on / type jffs2 (rw)
none on /dev type devfs (rw)
none on /proc type proc (rw)
none on /tmp type tmpfs (rw,nosuid,nodev)
none on /dev/pts type devpts (rw)
none on /sys type sysfs (rw)
root@OpenWrt:/# df -k
Filesystem           1k-blocks      Used Available Use% Mounted on
/dev/root                 3264      1732      1532  53% /
root@OpenWrt:/#
}}}

=== Use fconfig to change bootup parameters ===

Now you will need to change the boot script so that your new kernel is booted automatically at power-up. You can also use this as an opportunity to change the default !RedBoot serial port speed from 115200 to 9600 bps.

{{{
RedBoot> fconfig
Run script at boot: true
Boot script:
.. check_mac
.. load art_ap51.elf
.. go
.. load -h 192.168.84.9 -p 80 -m http /meraki/mini.1.img
.. exec
.. fis load stage2
.. exec
Enter script, terminate with empty line
>> fis load -d kernel
>> exec
>>
Boot script timeout (1000ms resolution): 2
Use BOOTP for network configuration: false
Gateway IP address:
Local IP address: 192.168.84.1
Local IP address mask: 255.255.255.0
Default server IP address: 192.168.84.9
Console baud rate: 9600
GDB connection port: 9000
Force console for special debug messages: false
Network debug at boot time: false
Update RedBoot non-volatile configuration - continue (y/n)? y
... Erase from 0xa87d0000-0xa87e0000: .
... Program from 0x80ff0000-0x81000000 at 0xa87d0000: .
RedBoot>
}}}

== Booting using Meraki stage2 loader ==

Alternatively, it's possible to continue to use Meraki's stage 2 loader. This has the following advantages:
 * It does LZMA decompression, which is faster and the kernel image is smaller
 * It doesn't require changing the RedBoot configuration, and so is easier to do without a serial console
 * Potentially it allows you to have two images, and boot the second if the first is corrupt (i.e. making it harder to brick the unit)

To do this, you need to prepend an 8-byte header to the kernel image, containing a length and bastardised CRC. The following Perl program does this. (Meraki's own software bundle compiles a C program to calculate the CRC)

{{{
#!/usr/bin/perl -w
# This script takes an LZMA kernel image, prepends the header expected
# by the Meraki stage2 bootloader, and pads to 64K
# Typical usage:
#    ./merakipart.pl ../build_mips/linux-2.6-atheros/vmlinux.bin.l7 >../bin/part

use Digest::CRC;
open(F, $ARGV[0]) or die "$ARGV[0]: $!";
$size = -s F;
# Meraki's non-standard interpretation of the CRC32 algorithm
$ctx = Digest::CRC->new(width=>32, init=>0, xorout=>0,
                         poly=>0x04c11db7, refin=>0, refout=>0);
$ctx->addfile(*F);
print pack 'NN', ($size, $ctx->digest);
seek(F,0,0);
print <F>;
close(F);
$size += 8;
print "\000" while ($size++ & 0xffff);
}}}

Now you have a kernel which stage2 will happily decompress and run:

{{{
RedBoot> load -r -b 0x80041000 -m tftp -h 192.168.84.9 part
Raw file loaded 0x80041000-0x800f0fff, assumed entry at 0x80041000
RedBoot> fis create linux
An image named 'linux' exists - continue (y/n)? y
... Erase from 0xa8150000-0xa8490000: ....................................................
... Program from 0x80041000-0x800f1000 at 0xa8150000: ...........
... Erase from 0xa87d0000-0xa87e0000: .
... Program from 0x80ff0000-0x81000000 at 0xa87d0000: .
RedBoot> load -r -b 0x80041000 -m tftp -h 192.168.84.9 openwrt-atheros-2.6-root.jffs2-64k
Raw file loaded 0x80041000-0x801c0fff, assumed entry at 0x80041000
RedBoot> fis create -r 0x80041000 -e 0x80041000 rootfs
An image named 'rootfs' exists - continue (y/n)? y
... Erase from 0xa8490000-0xa87d0000: ....................................................
... Program from 0x80041000-0x801c1000 at 0xa8490000: ................
... Erase from 0xa87d0000-0xa87e0000: .
... Program from 0x80ff0000-0x81000000 at 0xa87d0000: .
RedBoot> fis load stage2
RedBoot> exec
Now booting linux kernel:
 Base address 0x80030000 Entry 0x80100000
 Cmdline :
starting stage2
reading flash at 0xa8150000 - 0xa81fdc8e... done
Calculating CRC... 0xf87cb83e - matches
decompressing... done
starting linux
Linux version 2.6.19.1 (candlerb@candlerb-desktop) (gcc version 3.4.6 (OpenWrt-2.0)) #1 Tue Jan 2 14:07:20 GMT 2007
...
}}}

The flash load and decompress now takes only about 7 seconds, and you can reboot without changing the !RedBoot config.

= Options for installing without a serial console =

/!\ '''WARNING:''' These procedures can brick your Meraki Mini. If you do, you may need a serial console to fix it. Kamikaze is experimental code and you should NOT install !OpenWrt unless you have got a working serial console cable.

== RedBoot over telnet ==

It's possible to get a !RedBoot> command line over the network. There is a two-second window (!) in which you can do so. Configure your PC as 192.168.84.9 and repeatedly try to connect to port 9000 on 192.168.84.1 (just keep hitting ctrl-C, up-arrow, enter) and you should be able to manage it. If your PC is running Linux you might want to rm /etc/resolv.conf first to stop it doing reverse DNS lookups on the address.

{{{
# arp -d 192.168.84.1; telnet 192.168.84.1 9000
192.168.84.1 (192.168.84.1) deleted
Trying 192.168.84.1...
^C
# arp -d 192.168.84.1; telnet 192.168.84.1 9000
192.168.84.1 (192.168.84.1) deleted
Trying 192.168.84.1...
^C
# arp -d 192.168.84.1; telnet 192.168.84.1 9000
192.168.84.1 (192.168.84.1) deleted
Trying 192.168.84.1...
Connected to 192.168.84.1.
Escape character is '^]'.
== Executing boot script in 1.980 seconds - enter ^C to abort
^C^C
RedBoot>
}}}

Once you've done this, you can use fconfig to set a longer timeout (say 10 seconds) to make this easier in future - ignore any "AHB ERROR" messages you may see.

{{{
RedBoot> fconfig
Run script at boot: true
Boot script:
.. check_mac
.. load art_ap51.elf
.. go
.. load -h 192.168.84.9 -p 80 -m http /meraki/mini.1.img
.. exec
.. fis load stage2
.. exec
Enter script, terminate with empty line
>> check_mac
>> load art_ap51.elf
>> go
>> load -h 192.168.84.9 -p 80 -m http /meraki/mini.1.img
>> exec
>> fis load stage2
>> exec
>>
Boot script timeout (1000ms resolution): 2^H10
Use BOOTP for network configuration: false
Gateway IP address:
Local IP address: 192.168.84.1
Local IP address mask: 255.255.255.0
Default server IP address: 192.168.84.9
Console baud rate: 115200^H^H^H^H^H^H9600
GDB connection port: 9000
Force console for special debug messages: false
Network debug at boot time: false
Update RedBoot non-volatile configuration - continue (y/n)? y
... Erase from 0xa87d0000-0xa87e0000: .
... Program from 0x80ff0000-0x81000000 at 0xa87d0000: .
RedBoot>
}}}

You can then continue as above; in particular you should create the "linux", "rootfs" and "/storage" partitions so that they are accessible when OpenWrt is running.

{{{
RedBoot> fis create -b 0x80041000 -l 0x100000 -f 0xa8050000 -e 0x80041000 -r 0x80041000 -n /storage
RedBoot> fis create -b 0x80041000 -l 0x340000 -f 0xa8150000 -e 0x80041000 -r 0x80041000 -n linux
RedBoot> fis create -b 0x80041000 -l 0x340000 -f 0xa8490000 -e 0x80041000 -r 0x80041000 -n rootfs
}}}

== Installing over ssh from existing firmware ==

In theory it should be possible to overwrite just two partitions if your kernel is stage2-compatible:

 * /dev/mtd/3 with the CRC-prefixed kernel
 * /dev/mtd/4 with the rootfs

Or three partitions with a standard kernel
 * /dev/mtd/3 with the kernel
 * /dev/mtd/4 with the rootfs
 * /dev/mtd/6 with a new !RedBoot config (fis load -d linux; exec)

Unfortunately, neither of these will work with a vanilla Meraki because you'd also need to update the FIS directory to label the "rootfs" partition. (Is there a tool which runs under Linux which can do this? If not you will have to use !RedBoot> as above)

However, instead you can use a kernel with a ramdisk root.

'make menuconfig', select 'target images', select 'ramdisk'. Then 'make'.

=== Risk-free test using tftp ===

Configure a PC as 192.168.84.9 with a tftp server.

Copy bin/openwrt-atheros-2.6-vmlinux.elf to the tftp server with name "art_ap51.elf".

Plug in your Meraki. Run tcpdump on the tftp server if you want to see what's happening.

The Meraki should fetch your kernel+ramdisk and run it. After a minute or two you should be able to telnet to 192.168.1.1. If it fails, then you just power-cycle the unit and no harm is done.

=== Install stage2 image ===

If you're happy with this and want to make it permanent, first you'll want to make a stage2-compatible kernel image using the Perl script given above:

{{{
$ scripts/merakipart.pl build_mips/linux-2.6-atheros/vmlinux.bin.l7 >bin/part-rd
$ ls -l bin/part-rd
-rw-r--r-- 1 candlerb candlerb 1966080 2007-01-04 10:35 bin/part-rd
}}}

(Make sure this is smaller than 3.25MB)

Now you'll need to overwrite the 'part1' flash partition with this file. Unfortunately you can't do this from the !OpenWrt image you've just booted over tftp, because the flash partition isn't known to it, unless you used !RedBoot> to create the entry:

{{{
root@OpenWrt:~# cat /proc/mtd
dev:    size   erasesize  name
mtd0: 00030000 00010000 "RedBoot"
mtd1: 00020000 00010000 "stage2"
mtd2: 0000f000 00010000 "FIS directory"
mtd3: 00001000 00010000 "RedBoot config"
mtd4: 00010000 00010000 "board_config"
}}}

So you need to:
 * set up a DHCP server
 * make sure the art_ap51.elf file is no longer on your tftp server (or the tftp server is no longer on 192.168.84.9)
 * power-cycle the Meraki
 * watch DHCP to see what IP address it picks up

Now you're running the old Meraki firmware, which has the flash partitions hard-coded into it. Now you can copy the new image file, login, and write it to flash:

{{{
$ scp part-rd meraki@x.x.x.x:           # password is SN printed on bottom of box
$ ssh meraki@x.x.x.x                    # ditto
...
root@meraki-node:~# cat /proc/mtd | grep part1
mtd3: 00340000 00010000 "part1"
root@meraki-node:~# mtd erase /dev/mtd3
Unlocking mtd3 ...
Erasing mtd3 ...
root@meraki-node:~# dd if=part-rd of=/dev/mtd3 bs=1k
1920+0 records in
1920+0 records out
root@meraki-node:~# reboot
}}}

Now cross your fingers and hope that the unit comes back up on 192.168.1.1. (However, if you uploaded a broken image with a bad CRC, the Meraki stage2 bootloader should revert to the firmware in part2)

'''NOTE:''' Once you're running OpenWrt, there's no way to upgrade the firmware again!! This is because !OpenWrt still is missing the necessary partition info. So you'll still have to get to the !RedBoot> prompt to create the partition table. For this reason, I recommend using !RedBoot> to perform the installation in the first place.

'''FIXME:''' Running from a ramdisk root is very limited. For example, if you use 'passwd' to set a root password, and then reboot, this is lost. It would be better if we could have a single flash partition containing kernel + squashfs + jffs2 (unioned over the squashfs)

= OpenWrt configuration =

== IP ==

By default, eth0 is configured as 192.168.1.1. Change in /etc/config/network

== Storage ==

Note that there's 1MB of additional flash available which the Meraki original firmware mounted on /storage. You should probably back this up before using it if you want to be able to return to the original Meraki firmware.

It's not accessible until you create a FIS partition entry for it:

{{{
RedBoot> fis create -b 0x80041000 -l 0x100000 -f 0xa8050000 -e 0x80041000 -r 0x80041000 -n /storage
... Erase from 0xa87d0000-0xa87e0000: .
... Program from 0x80ff0000-0x81000000 at 0xa87d0000: .
RedBoot>
}}}

After this:
{{{
root@OpenWrt:/# cat /proc/mtd
dev:    size   erasesize  name
mtd0: 00030000 00010000 "RedBoot"
mtd1: 00020000 00010000 "stage2"
mtd2: 00100000 00010000 "/storage"
mtd3: 00340000 00010000 "linux"
mtd4: 00330000 00010000 "rootfs"
mtd5: 0000f000 00010000 "FIS directory"
mtd6: 00001000 00010000 "RedBoot config"
mtd7: 00010000 00010000 "board_config"
root@OpenWrt:/# mkdir /storage
root@OpenWrt:/# mount -t jffs2 /dev/mtdblock/2 /storage
root@OpenWrt:/# ls /storage
BOOT_COUNT              config.old              random_seed
config                  dropbear
config.local            meraki-watchdog.status
}}}

= Meraki-released source =

/!\ Now that Atheros SoC support is in the main !OpenWrt tree, the rest of this page is probably not of interest to most people. However it does include the source code to build the stage 2 loader, and to build the !RedBoot config partition. It also serves as documentation of some of the changes Meraki had to make.

Meraki distribute their own tarball at http://www.meraki.net/linux/openwrt-meraki.tar.gz which at the time of writing is:

{{{
openwrt-meraki.tar.gz   30-Nov-2006 12:11
size: 63072791
md5sum: da71bbdd97b33bbf7dbb17c819a6c636
}}}

This contains:
 * openwrt kamikaze forked from SVN r3586 (2006-04-02)
 * madwifi-ng forked from SVN r1486 (2006-03-28)
 * an entire linux kernel forked from 2.6.16.16
 * Meraki's own 'base' directory (includes tools for building their stage2 loader and main flash image for booting with !RedBoot)
 * Meraki's own 'base-files' directory (completely replacing the openwrt base files)

Some of the changes made by Meraki are described at http://forum.openwrt.org/viewtopic.php?id=7189

To build this software, follow the instructions in Meraki.README. Note that you will need to install the 'flex', 'sharutils' and 'gawk' packages first (Ubuntu: "apt-get install flex sharutils gawk")

Sit back and expect to wait an hour or more for the build to complete.

== Risk-free test ==

Set up a host system on 192.168.84.9, with either a webserver or a TFTP server.

copy build_ar531x/stage2-embedded.elf to /meraki/mini.1.img under the webserver's document root, or as art_ap51.elf under the tftp server.

Boot the Meraki. It should pick up this firmware and run it, without changing what's in the flash.

(The webserver approach doesn't always work well, at least with OpenBSD as the server; the Meraki always connects from the same source port, which means the socket gets stuck in a FIN_WAIT_2 state and subsequent connections are believed to be part of the same connection. TFTP runs over UDP and doesn't suffer this problem.)

== Install procedure ==

{{{
$ scp build_ar531x/upgrade.sh meraki@x.x.x.x:
$ ssh meraki@x.x.x.x
...
root@meraki-node:~# sh upgrade.sh
upgrading stage2
Unlocking /dev/mtd1 ...
Erasing /dev/mtd1 ...
7+1 records in
7+1 records out
checksumming part1
upgrade.sh: upgrade.sh: 80: /usr/bin/checkpart.pl: not found
part1 was invalid!, upgrading it first
Unlocking /dev/mtd3 ...
Erasing /dev/mtd3 ...
writing part1..
2568+1 records in
2568+1 records out
upgrading part2
Unlocking /dev/mtd4 ...
Erasing /dev/mtd4 ...
writing part2..
2568+1 records in
2568+1 records out
done
root@meraki-node:~# Connection to x.x.x.x closed by remote host.
}}}

[note the bug in the upgrade script! It should say /usr/bin/checkpart not /usr/bin/checkpart.pl. /usr/bin/checkpart is actually written in ruby]

Unfortunately, this upgrade process overwrites both image partitions, so it doesn't retain a fallback image in case the one you've uploaded is broken.

== On first boot ==

I found the machine got as far as picking up an IP address via DHCP but shortly afterwards crashed, going into a reboot loop. On the serial port:

{{{
...
wifi0: Use hw queue 8 for CAB traffic
wifi0: Use hw queue 9 for beacons
couldn't load module 'wlan_scan_sta' (-89)
unable to load wlan_scan_sta
wifi0: Atheros 2315 WiSoC: mem=0xb0000000, irq=3
wlan: mac acl policy registered
realtek setup

ethmac0 link up
eth0: up
bss channel not setupBreak instruction in kernel code[#1]:
Cpu 0
$ 0   : 00000000 10009c00 00000018 80289e6c
$ 4   : 80289e6c 81ef9ee4 00000001 80973bac
$ 8   : 81ede518 00001103 80970000 80980000
$12   : 80970000 00000591 00000002 2ab3be34
$16   : 81902000 0000ffff 81800280 81e26280
$20   : 81800280 803c3076 803c3020 81839ab0
$24   : 00000003 c005d310
$28   : 81838000 81839a20 81800280 c00f5898
Hi    : 00000240
Lo    : 000001f8
epc   : c00f5898 ieee80211_dup_bss+0xa4/0x2b8 [wlan]     Tainted: P
ra    : c00f5898 ieee80211_dup_bss+0xa4/0x2b8 [wlan]
Status: 10009c03    KERNEL EXL IE
Cause : 10800024
PrId  : 00019064
Modules linked in: wlan_xauth wlan_wep wlan_tkip wlan_scan_sta wlan_scan_ap wlalProcess ruby (pid: 529, threadinfo=81838000, task=81836a08)
Stack : 00050006 81e96180 00000000 81902000 803c3076 81e26280 81839ab0 803c3020
        c00f5d0c 002a002f 803c3076 81e26280 00000050 80938640 803c3076 81e26280
        00000050 80938640 81e96000 c00ef798 81839af0 803872a8 803c3020 00000050
        0000000f 00003f1d 0000000a 80980000 2aaae000 8006d080 2aaae000 803872a8
        000c000d 000f0011 00130014 00160018 00220000 0b0b0000 64000000 00000000
        ...
Call Trace:
 [<c00f5d0c>] ieee80211_add_neighbor+0x38/0x198 [wlan]
 [<c00ef798>] ieee80211_recv_mgmt+0xec0/0x4330 [wlan]
 [<8006d080>] __do_softirq+0x70/0x104
 [<c0065dc0>] init_module+0xddc0/0x11838 [ath_ahb]
 [<c00f4510>] ieee80211_input+0x1908/0x1d84 [wlan]
 [<80048c18>] do_gettimeofday+0x30/0x138
 [<8009f9e4>] __handle_mm_fault+0xab0/0xb04
 [<8006cca4>] getnstimeofday+0x18/0x4c
 [<80048c18>] do_gettimeofday+0x30/0x138
 [<80092f2c>] __alloc_pages+0x60/0x2f0
 [<8006cca4>] getnstimeofday+0x18/0x4c
 [<80048c18>] do_gettimeofday+0x30/0x138
 [<c00f4aa8>] ieee80211_input_all+0x11c/0x224 [wlan]
 [<8008312c>] ktime_get+0x20/0x4c
 [<c006f6a0>] ath_suspend+0x38ec/0x6324 [ath_ahb]
 [<801c178c>] dev_watchdog+0xc0/0x1dc
 [<8006d620>] tasklet_action+0x114/0x16c
 [<8008b120>] handle_IRQ_event+0x68/0xe4
 [<8006d080>] __do_softirq+0x70/0x104
 [<8006d170>] do_softirq+0x5c/0x90
 [<80044314>] do_IRQ+0x24/0x34
 [<80042618>] ar531x_interrupt_receive+0xf8/0x100
 [<80042618>] ar531x_interrupt_receive+0xf8/0x100
 [<80052448>] r4k_flush_icache_page+0x2a8/0x2c4
 [<8009e820>] do_wp_page+0x520/0x5ac
 [<8004f38c>] blast_icache16+0x48/0xe8
 [<8009f440>] __handle_mm_fault+0x50c/0xb04
 [<8009f2fc>] __handle_mm_fault+0x3c8/0xb04
 [<80074e34>] __group_send_sig_info+0x28/0xc0
 [<8009d668>] unmap_vmas+0x410/0x5fc
 [<800b4f24>] __fput+0x1f4/0x238
 [<800b4d74>] __fput+0x44/0x238
 [<8004dc14>] do_page_fault+0x104/0x350
 [<800b3308>] filp_close+0x6c/0x90
 [<800a3248>] exit_mmap+0x70/0x164
 [<8006a004>] do_exit+0x9b0/0x9bc
 [<80068a54>] put_files_struct+0x19c/0x214
 [<8006a004>] do_exit+0x9b0/0x9bc
 [<8004e394>] tlb_do_page_fault_0+0x104/0x10c
 [<80042bb0>] syscall_exit+0x0/0x38


Code: 244272a0  0040f809  00000000 <0200000d> 8e020000  ae1101c8  8c420238  304
Kernel panic - not syncing: Aiee, killing interrupt handler!
 <0>Rebooting in 3 seconds..<2>watchdog expired!
watchdog hb: 20  ISR: 0xa1  IMR: 0x9  WD : 0x0  WDC: 0x0
}}}

Unfortunately, I had installed using the flash method rather than the failsafe method. Fortunately I had backed up the partitions and was able to restore using a serial console.
