#format wiki
#language en
= Asus AAM6020VI ADSL modem 4Port eth and Wireless =
== Major Chips ==
 * TNET7300GDU             AR7WRD SoC
 * 88E6060                Marvel 6 port ethernet swicth
 * K4S281632F             Samsung 16Mb SDRAM
 * TNETW1130GVF           Single-Chip MAC and Baseband Processor for IEE 802.11 a/b/g.
On AAM6020VI-T4 the WLAN card is in a mini-pci slot. The -T? bit is still confusing, while on the box it's is -T4 on the pcb -T2 is written. That also says revision 1.0 .

Device has 16Mb Ram and 4Mb Ram which should make it a reasonably flexible unit

It uses PSPBoot with a default address of 192.168.1.1

== Debug HW ==
There is a 2x4 (male pins) EJTAG ["OpenWrtDocs/Customizing/Hardware/JTAG Cable"] connector and another 2x3 female one without a specific label (only says J1).

== Similar Openwrt dev list devices ==
These all have the same base processor and similar RAM size.

Netgear [:OpenWrtDocs/Hardware/Netgear/DG834G:DG834G]        -

DLink [:OpenWrtDocs/Hardware/D-Link/DSL-502T:DSL-502T] - Uses Adam2

Sphairon [:OpenWrtDocs/Hardware/Sphairon/TurbolinkJDR454WB:TurbolinkJDR454WB]
== Manufacturer Product link ==
http://www.asus.com.tw/products.aspx?l1=13&l2=96&l3=0&model=46&modelmenu=1

Firmware ver MSTAR_3.6.0C_1F00_AAM6020VI-T4

Linux version 2.4.17_mvl21-malta-mips_fp_le (root@adslrick) (gcc version 2.95.3 20010315 (release/MontaVista)) #1 Mon Apr 11 15:05:10 CST 2005

== cpuinfo ==
processor               : 0

cpu model               : MIPS 4KEc V4.8

BogoMIPS                : 149.91

wait instruction        : no

microsecond timers      : yes

extra interrupt vector  : yes

hardware watchpoint     : yes

VCED exceptions         : not available

VCEI exceptions         : not available

== iomem -- 00000000-13ffffff : reserved

14000000-1401ffff : System RAM

14020000-14ffffff : System RAM

 . 14020000-14194f37 : Kernel code 141a5300-141befff : Kernel data
a8612800-a8612fff : eth0

== Special Libraries ==
tiatm.o

tiap.o

=== and utilities ===
/usr/sbin/

br2684ctl

=== Startup script ===
/etc/init.d/rcS

# cat /etc/init.d/rcS

#! /bin/sh

#

# rcS           Call all S??* scripts in /etc/rcS.d in

#               numerical/alphabetical order.

#

# Version:      @(#)/etc/init.d/rcS  2.76  19-Apr-1999  miquels@cistron.nl

#

trap "" SIGHUP

PATH=/sbin:/bin:/usr/sbin:/usr/bin

runlevel=S

prevlevel=N

umask 022

export PATH runlevel prevlevel

#

#       Trap CTRL-C &c only in this shell so we can interrupt subprocesses.

#

trap ":" INT QUIT TSTP

mount -n /proc

#mount -n -o remount,rw /

mount /var

# unreserve for unp systems

echo "0 0" > /proc/sys/vm/pagetable_cache

# router

echo 1 > /proc/sys/net/ipv4/ip_forward

# pppox

echo 1 > /proc/sys/net/ipv4/ip_dynaddr

# ignore_all not yet used: this should be satisfactory

echo 1 > /proc/sys/net/ipv4/icmp_echo_ignore_broadcasts

# drop spoofed addr: turn this off on non-loop-free networks

# echo 1 > /proc/sys/net/ipv4/conf/default/rp_filter

# echo 1 > /proc/sys/net/ipv4/conf/all/rp_filter

# do not honor source route flags

echo 0 > /proc/sys/net/ipv4/conf/default/accept_source_route

echo 0 > /proc/sys/net/ipv4/conf/all/accept_source_route

# protect against syn flood attacks

echo 1 >/proc/sys/net/ipv4/tcp_syncookies

# this needs proper sampling on av_blog to determine optimal value

# for now just observe softnet_stats to see # time was throttled

# historical value was 300

echo 100 > /proc/sys/net/core/netdev_max_backlog

echo 50 > /proc/sys/net/core/mod_cong

echo 30 > /proc/sys/net/core/lo_cong

echo 10 > /proc/sys/net/core/no_cong

(cd /; tar xf var.tar)

/sbin/ledcfg

sleep 1

#/sbin/insmod avalanche_usb

#sleep 1

/sbin/insmod tiatm

sleep 1

# UPnP requires loopback

ifconfig lo 127.0.0.1

/usr/sbin/thttpd -d /usr/www -u root -p 80 -c '/cgi-bin/*' -l /dev/null

/usr/bin/cm_pc > /dev/tts/0 &

= Further info from software commands =
== cat proc/tty/driver/serial ==
serinfo:1.0 driver:5.05c revision:2001-07-08

0: uart:16550A port:A8610E00 irq:15 baud:2258 tx:2204 rx:0 RTS|CTS|DTR

1: uart:16550A port:A8610F00 irq:16 tx:0 rx:0 RTS|DTR

== cat proc/ticfg/env ==
bootloaderVersion       1.2.5.9

ProductID       AR7WRD

HWRevision      Unknown

SerialNumber    none

IPA     192.168.1.1

BOOTCFG m:f:"mtd1"

mtd2    0x90000000,0x90010000

mtd3    0x90010000,0x90020000

mtd4    0x90020000,0x90400000

usb_vid 0x0451

usb_pid 0x6060

usb_prod        USB MODEM

MAC_PORT        1

ReleaseVersion  pspboot-1259-0104-AR7WRD-FLSH4-RAM16-EX

MEMSZ   0x01000000

FLASHSZ 0x00400000

MODETTY0        38400,n,8,1,hw

MODETTY1        38400,n,8,1,hw

CPUFREQ 150000000

SYSFREQ 125000000

PROMPT  (psbl)

mtd0    0x90099000,0x90400000

mtd1    0x90020090,0x90099000

StaticBuffer    120

vcc_encaps0     0.0

vcc_encaps1     0.0

vcc_encaps2     0.0

vcc_encaps3     0.0

vcc_encaps4     0.0

vcc_encaps5     0.0

vcc_encaps6     0.0

vcc_encaps7     0.0

HWA_0   00:13:D4:31:86:89

mac_ap  00:60:B3:D0:E2:A2

== cat proc/mounts ==
/dev/mtdblock/0 / squashfs ro 0 0

none /dev devfs rw 0 0

proc /proc proc rw 0 0

ramfs /var ramfs rw 0 0

== /proc/mtd ==
dev:    size   erasesize  name

mtd0: 00367000 00010000 "mtd0"

mtd1: 00078f70 00010000 "mtd1"

mtd2: 00010000 00002000 "mtd2"

mtd3: 00010000 00010000 "mtd3"

mtd4: 003e0000 00010000 "mtd4"

= PSPBoot log =
= PARTITION INFO =
= Board Layout =
I don't have an image of the underside and I can't find the flash chip on the top surface. The JTAG is obvious but I have no idea where the serial port is. attachment:AAM6020VI.jpg

----
 . CategoryModel ["CategoryAR7Device"]
