'''Meraki Mini'''

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

'''Serial to USB adaptor'''

Meraki sell a small adaptor board (18mm x 32mm) for $29 which plugs into JP1 and has a serial to USB adaptor chip and a mini USB connector; it comes with a mini USB to normal USB cable. It appears to be powered by the host side, not the Meraki side. Plugging it into a Linux system shows:

{{{
usb 2-1: new full speed USB device using address 3
ftdi_sio 2-1:1.0: FTDI FT232BM Compatible converter detected
usb 2-1: FTDI FT232BM Compatible converter now attached to ttyUSB0
usbcore: registered new driver ftdi_sio
drivers/usb/serial/ftdi_sio.c: v1.4.1:USB FTDI Serial Converters Driver
}}}

It is not polarised, but the correct way round is so that it overhangs the RF module, and doesn't hang out of the side of the case. Minicom set to /dev/ttyUSB0 and 115200 8N1 works.

(Using CentOS 4, with its 2.6.9 kernel, the USB adaptor was somewhat unreliable; power-cycling the Meraki made it freeze, so I had to unplug and reconnect the USB connection to the host as well. Maybe later kernels don't have this problem)

'''Opening the case'''

Peel off the bottom left and top right corners of the silver label on the back of the unit, to reveal two crosspoint screws. Remove them, then prise apart the case with a screwdriver.

'''Startup messages (standard firmware)'''

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

Plugging in the ethernet port to another host and running tcpdump there shows the following:

{{{
11:23:12.830678 arp who-has 192.168.84.1 tell 192.168.84.1
  0000: 0001 0800 0604 0001 0018 0aXX XXXX c0a8  .............???
  0010: 5401 0000 0000 0000 c0a8 5401 0000 0000  T.......??T.....
  0020: 0000 0000 0000 0000 0000 0000 0000       ..............

(8 times)

11:23:19.002236 arp who-has 192.168.84.9 tell 192.168.84.1
  0000: 0001 0800 0604 0001 0018 0aXX XXXX c0a8  .............???
  0010: 5401 0000 0000 0000 c0a8 5409 0000 0000  T.......??T.....
  0020: 0000 0000 0000 0000 0000 0000 0000       ..............

(16 times)

...Pick up IP address via DHCP
...Send UDP packet to 64.62.142.12.7351
...DNS lookups for config.meraki.net. and db.meraki.net.
}}}

If I set the connected host to have IP address 192.168.84.9 then I see:

{{{
11:34:36.005386 arp who-has 192.168.84.1 tell 192.168.84.1
  0000: 0001 0800 0604 0001 0018 0aXX XXXX c0a8  .............???
  0010: 5401 0000 0000 0000 c0a8 5401 0000 0000  T.......??T.....
  0020: 0000 0000 0000 0000 0000 0000 0000       ..............

(8 times)

11:34:42.176947 arp who-has 192.168.84.9 tell 192.168.84.1
  0000: 0001 0800 0604 0001 0018 0aXX XXXX c0a8  .............???
  0010: 5401 0000 0000 0000 c0a8 5409 0000 0000  T.......??T.....
  0020: 0000 0000 0000 0000 0000 0000 0000       ..............

11:34:42.176953 arp reply 192.168.84.9 is-at 0:2:e3:xx:xx:xx
  0000: 0001 0800 0604 0002 0002 e3XX XXXX c0a8  ..........?...??
  0010: 5409 0018 0aXX XXXX c0a8 5401 0000 0000  T......???T.....
  0020: 0000 0000 0000 0000 0000 0000 0000       ..............

11:34:42.177481 192.168.84.1.7700 > 192.168.84.9.tftp: 21 RRQ "art_ap51.elf"
  0000: 4500 0031 0000 0000 4011 5161 c0a8 5401  E..1....@.Qa??T.
  0010: c0a8 5409 1e14 0045 001d 27c8 0001 6172  ??T....E..'?..ar
  0020: 745f 6170 3531 2e65 6c66 004f 4354 4554  t_ap51.elf.OCTET
  0030: 00                                       .

11:34:42.181932 192.168.84.9.43846 > 192.168.84.1.7700: udp 19
  0000: 4500 002f cb68 0000 4011 85fa c0a8 5409  E../?h..@..???T.
  0010: c0a8 5401 ab46 1e14 001b cc0a 0005 0001  ??T.?F....?.....
  0020: 4669 6c65 206e 6f74 2066 6f75 6e64 00    File not found.

11:34:42.195173 192.168.84.1.7800 > 192.168.84.9.www: S 511237751:511237751(0) win 1472 <mss 1472>
  0000: 4500 002c 0001 0000 4006 5170 c0a8 5401  E..,....@.Qp??T.
  0010: c0a8 5409 1e78 0050 1e78 de77 0000 0000  ??T..x.P.x?w....
  0020: 6002 05c0 4d47 0000 0204 05c0 0000       `..?MG.....?..

11:34:42.195206 192.168.84.9.www > 192.168.84.1.7800: S 1199264634:1199264634(0) ack 511237752 win 16384 <mss 1460> (DF)
  0000: 4500 002c b63f 4000 4006 5b31 c0a8 5409  E..,??@.@.[1??T.
  0010: c0a8 5401 0050 1e78 477b 537a 1e78 de78  ??T..P.xG{Sz.x?x
  0020: 6012 4000 780c 0000 0204 05b4            `.@.x......?

11:34:42.198048 192.168.84.1.7800 > 192.168.84.9.www: . ack 1 win 1472
  0000: 4500 0028 0002 0000 4006 5173 c0a8 5401  E..(....@.Qs??T.
  0010: c0a8 5409 1e78 0050 1e78 de78 477b 537b  ??T..x.P.x?xG{S{
  0020: 5010 05c0 ca09 0000 0000 0000 0000       P..??.........

11:34:42.198122 192.168.84.1.7800 > 192.168.84.9.www: P 1:36(35) ack 1 win 1472
  0000: 4500 004b 0003 0000 4006 514f c0a8 5401  E..K....@.QO??T.
  0010: c0a8 5409 1e78 0050 1e78 de78 477b 537b  ??T..x.P.x?xG{S{
  0020: 5018 05c0 ef15 0000 4745 5420 2f6d 6572  P..??...GET /mer
  0030: 616b 692f 6d69 6e69 2e31 2e69 6d67 2048  aki/mini.1.img H
  0040: 5454 502f 312e 300d 0a0d 0a              TTP/1.0....

11:34:42.199144 192.168.84.9.www > 192.168.84.1.7800: P 1:487(486) ack 36 win 17520 (DF)
  0000: 4500 020e b09f 4000 4006 5eef c0a8 5409  E...?.@.@.^???T.
  0010: c0a8 5401 0050 1e78 477b 537b 1e78 de9b  ??T..P.xG{S{.x?.
  0020: 5018 4470 6055 0000 4854 5450 2f31 2e31  P.Dp`U..HTTP/1.1
  0030: 2034 3034 204e 6f74 2046 6f75 6e64 0d0a   404 Not Found..
  0040: 4461 7465 3a20 5468 752c 2031 3420 4465  Date: Thu, 14 De
  0050: 6320 3230 3036 2031 313a 3334 3a34 3220  c 2006 11:34:42
  0060: 474d 540d 0a53 6572 7665 723a 2041 7061  GMT..Server: Apa
  0070: 6368 652f 312e 332e 3239 2028 556e 6978  che/1.3.29 (Unix
  0080: 2920 6d6f 645f 7373 6c2f 322e 382e 3136  ) mod_ssl/2.8.16
  0090: 204f 7065 6e53 534c 2f30 2e39 2e37 6a0d   OpenSSL/0.9.7j.
  00a0: 0a43 6f6e 6e65 6374 696f 6e3a 2063 6c6f  .Connection: clo
  00b0: 7365 0d0a 436f 6e74 656e 742d 5479 7065  se..Content-Type
  00c0: 3a20 7465 7874 2f68 746d 6c3b 2063 6861  : text/html; cha
  00d0: 7273 6574 3d69 736f 2d38 3835 392d 310d  rset=iso-8859-1.
<<SNIP>>

11:34:42.199213 192.168.84.9.www > 192.168.84.1.7800: F 487:487(0) ack 36 win 17520 (DF)
  0000: 4500 0028 8ab5 4000 4006 86bf c0a8 5409  E..(.?@.@..???T.
  0010: c0a8 5401 0050 1e78 477b 5561 1e78 de9b  ??T..P.xG{Ua.x?.
  0020: 5011 4470 894f 0000                      P.Dp.O..

11:34:42.200839 192.168.84.1.7800 > 192.168.84.9.www: . ack 487 win 1472
  0000: 4500 0028 0004 0000 4006 5171 c0a8 5401  E..(....@.Qq??T.
  0010: c0a8 5409 1e78 0050 1e78 de9b 477b 5561  ??T..x.P.x?.G{Ua
  0020: 5010 05c0 c800 0000 0000 0000 0000       P..??.........

11:34:42.200865 192.168.84.1.7800 > 192.168.84.9.www: . ack 488 win 1472
  0000: 4500 0028 0005 0000 4006 5170 c0a8 5401  E..(....@.Qp??T.
  0010: c0a8 5409 1e78 0050 1e78 de9b 477b 5562  ??T..x.P.x?.G{Ub
  0020: 5010 05c0 c7ff 0000 0000 0000 0000       P..???........
}}}

So it looks like there are at least two different ways to download new firmware at power-up.

'''ssh access'''

Once the unit has picked up an IP address via DHCP, you can ssh in. The username is 'meraki' and the password is the SN displayed on the bottom of the unit, in the form XXX-XXX-XXX (including the dashes)

{{{
# ssh meraki@192.168.1.105
meraki@192.168.1.105's password:


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

'''!OpenWrt support'''

!OpenWrt support is not currently in the main SVN repository. Meraki distribute their own tarball at http://www.meraki.net/linux/openwrt-meraki.tar.gz

Follow the instructions in Meraki.README. Note that you will need to install the 'flex', 'sharutils' and 'gawk' packages first (Ubuntu: "apt-get install flex sharutils gawk")

Sit back and expect to wait an hour or more for the build to complete.

'''Install and restore procedure'''

The standard approach is to copy build_ar531x/upgrade.sh to the Meraki (e.g. with scp) and then run it. This overwrites the "stage2", "redboot config", "part1" and "part2" partitions.

So logically you should be able to restore the device to its original state by backing these up:

{{{
ssh meraki@x.x.x.x 'dd if=/dev/mtd1 bs=64k' >stage2.bak
ssh meraki@x.x.x.x 'dd if=/dev/mtd3 bs=64k' >part1.bak
ssh meraki@x.x.x.x 'dd if=/dev/mtd4 bs=64k' >part2.bak
ssh meraki@x.x.x.x 'dd if=/dev/mtd5 bs=64k' >redboot-config.bak
}}}

In practice you'll probably find that part1.bak and part2.bak are identical. If you dd /dev/mtd7, you'll get an 8MB file which is the same as the first 7 partitions concatenated together.

Note: the "board config" partition contains the unit's MAC address and SN (secret password); you should probably never overwrite this partition.

FIXME: Instructions say "A raw ELF binary is provided for those using serial adapters". Explain how to use this.

FIXME: The Meraki makes TFTP and HTTP requests, can these be used?
