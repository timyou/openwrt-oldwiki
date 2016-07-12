= Work in Progress =
Porting OpenWrt to the [http://www.a-link.com/RR24AP.html RoadRunner 24AP] is a work in progress.

== Specifications ==
A-Link RoadRunner 24AP(i+) is an external 4-port ADSL2+-router with 54Mb WLAN Access point (also supports standard ADSL,RE ADSL and ANNEX M).

=== Hardware ===
||'''CPU''' || AR7 @ 211 MHz || Texas Instruments AR7 MIPS-based, [http://focus.ti.com/general/docs/bcg/bcggencontent.tsp?templateId=6116&navigationId=11917&path=templatedata/cm/general/data/bcgmiddl/ar7_cpe TNETD73000AZDW] ||
||'''RAM''' || Unknown || Unknown ||
||'''FLASH''' || Unknown || Unknown ||
||'''SWITCH''' || Unknown || Unknown ||
||'''Wi-Fi''' || Unknown || Unknown ||

=== Loader ===
{{{
PSPBoot1.4 rev: 1.4.0.4
}}}

=== Memory ===
||'''dev''' ||'''start''' ||'''end''' ||'''desc''' ||
||mtd0 || 0x9009f000 || 0x90400000 || Filesystem ||
||mtd1 || 0x90020090 || 0x9009f000 || Kernel ||
||mtd2 || 0x90000000 || 0x90010000 || PSPBoot ||
||mtd3 || 0x90020000 || 0x90400000 || variabiles ||
||mtd4 || 0x90010000 || 0x90400000 || Kernel + Filesystem ||

== How to get OpenWRT onto the router ==

WiP

== Informations from the D-Link firmware ==
=== Backup original firmware ===
'''Strongly recommend'''

Use serial console or telnet access to backup original firmware. Original firmware have no dd so i used cat

{{{
# cat /dev/mtdblock/0 > /var/tmp/mtd0.bin
# cat /dev/mtdblock/1 > /var/tmp/mtd1.bin
# cat /dev/mtdblock/2 > /var/tmp/mtd2.bin
# cat /dev/mtdblock/3 > /var/tmp/mtd3.bin
# cat /dev/mtdblock/4 > /var/tmp/mtd4.bin
# ps
  PID  Uid     VmSize Stat Command
    1 root       1564 S    init
    2 root            S    [keventd]
    3 root            S    [ksoftirqd_CPU0]
    4 root            S    [kswapd]
    5 root            S    [bdflush]
    6 root            S    [kupdated]
    7 root            S    [mtdblockd]
   41 root       2176 S    /usr/bin/cm_pc
   43 root        620 S    /sbin/ch_iptables
   44 root       1564 S    init
   45 root       4152 S    /usr/sbin/mini_httpd -d /usr/www -u root -p 80 -c /c
   46 root       5180 S    /usr/bin/cm_logic -m /dev/ticfg -c /etc/config.xml
   68 root        612 S    /usr/bin/cm_klogd /dev/klog
   70 root        644 S    /sbin/dproxy -c /etc/resolv.conf -d
  333 root        632 S    /sbin/utelnetd
  334 root       1284 S    -cmcli
  336 root       1568 S    sh -c /bin/sh
  337 root       1568 S    /bin/sh
  347 root       1564 R    ps
# kill 45
# /usr/sbin/mini_httpd -d /var/tmp -u root -p 80
}}}
Then using internet browser download backup files


Firmware: [http://support.a-link.com/rr24ap/upd.htm 7.2.3]

{{{
# cat /proc/cpuinfo
processor               : 0
cpu model               : MIPS 4KEc V4.8
BogoMIPS                : 211.35
wait instruction        : no
microsecond timers      : yes
extra interrupt vector  : yes
hardware watchpoint     : yes
VCED exceptions         : not available
VCEI exceptions         : not available}}}
{{{
# cat /proc/meminfo
        total:    used:    free:  shared: buffers:  cached:
Mem:  14659584  6062080  8597504        0   200704   983040
Swap:        0        0        0
MemTotal:        14316 kB
MemFree:          8396 kB
MemShared:           0 kB
Buffers:           196 kB
Cached:            960 kB
SwapCached:          0 kB
Active:           1512 kB
Inactive:         1436 kB
HighTotal:           0 kB
HighFree:            0 kB
LowTotal:        14316 kB
LowFree:          8396 kB
SwapTotal:           0 kB
SwapFree:            0 kB}}}
{{{
# cat /proc/mounts
/dev/mtdblock/0 / squashfs ro 0 0
none /dev devfs rw 0 0
proc /proc proc rw 0 0
ramfs /var ramfs rw 0 0}}}
{{{
# cat /proc/mtd
dev:    size   erasesize  name
mtd0: 00361000 00010000 "mtd0"
mtd1: 0007ef70 00010000 "mtd1"
mtd2: 00010000 00002000 "mtd2"
mtd3: 00010000 00010000 "mtd3"
mtd4: 003e0000 00010000 "mtd4"}}}
{{{
# cat /proc/version
Linux version 2.4.17_mvl21-malta-mips_fp_le (root@localhost.localdomain) (gcc ve
rsion 2.95.3 20010315 (release/MontaVista)) #1 Fri Jun 22 10:21:11 CST 2007}}}
{{{
# cat /proc/tty/driver/serial
serinfo:1.0 driver:5.05c revision:2001-07-08
0: uart:16550A port:A8610E00 irq:15 baud:667 tx:8370 rx:0 RTS|DTR
1: uart:unknown port:A8610F00 irq:16}}}
{{{
# cat /proc/ticfg/env
mtd4    0x90020000,0x90400000
mtd3    0x90010000,0x90020000
vlynq_polarity  low
BUILD_OPS       0x301
bootloaderVersion       1.4.0.4
mtd2    0x90000000,0x90010000
MAC_PORT        0
MEMSZ   0x01000000
FLASHSZ 0x00400000
MODETTY0        9600,n,8,1,hw
MODETTY1        9600,n,8,1,hw
CPUFREQ 211968000
MIPSFREQ        211968000
SYSFREQ 105984000
PROMPT  (psbl)
DSL_BIT_TMODE   1
DSL_UPG_DONE    1
sar_ipacemax    6
vcc_encaps0     0.0
vcc_encaps1     0.0
vcc_encaps2     0.0
vcc_encaps3     0.0
vcc_encaps4     0.0
vcc_encaps5     0.0
vcc_encaps6     0.0
vcc_encaps7     0.0
IPA_SVR 10.0.0.100
IPA     10.0.0.2
BOOTCFG m:f:"mtd1"
WLAN_EEPROM0    021156041B06001200000601095612000000010D56A9000000026D5453845A0E
WLAN_EEPROM1    12000000013984000100000101854C1068900105850600100001298507000000
WLAN_EEPROM2    01C1850000300001C585000000000111850000FFFF0115850000F0FF01A58500
WLAN_EEPROM3    8000000109850000800201010C03000000012184000000800181851D00030001
WLAN_EEPROM4    55090100000001E5580200000001F1580800000001D5581000000001B1580400
WLAN_EEPROM5    0000000000000000000C00C300FE0008011401260144014D014F0165019F01AF
WLAN_EEPROM6    01B70101390000110004010101000501060002010201021E000A000205020411
WLAN_EEPROM7    2244030610203031324004095449204143583130300507544920546573740108
WLAN_EEPROM8    1B17CE9AB95801190502000037007000A600E200040444101D0045102600185A
WLAN_EEPROM9    4000145A0D00020E0801CA000A0193025000BC0185095000EE000A0128035000
WLAN_EEPROM10   AC0185090107100000400000010000050400010100000000FFFFFFFFFDFDFDFD
WLAN_EEPROM11   FBF4F4F4F40E0409090909090909090909090909090909090909090909090909
WLAN_EEPROM12   090909090909090909090909090909090909090909090909090909090909090E
WLAN_EEPROM13   0100000000000000000000000000000302A318A3180700012000000000000000
WLAN_EEPROM14   00000000000000000000000000000000000000000000000000
NVS_TFTP_LOAD   0
HWA_0   00:13:64:35:81:AE
HWA_3   00:13:64:35:81:AF
HWA_2   00:13:64:35:81:AF
HWA_WAN0        00:13:64:35:81:B0
HWA_WAN1        00:13:64:35:81:B1
HWA_WAN2        00:13:64:35:81:B2
HWA_WAN3        00:13:64:35:81:B3
HWA_WAN4        00:13:64:35:81:B4
HWA_WAN5        00:13:64:35:81:B5
HWA_WAN6        00:13:64:35:81:B6
HWA_WAN7        00:13:64:35:81:B7
WLAN_HWADDR0    00:13:64:35:81:B8
WLAN_HWADDR1    00:13:64:35:81:B9
WLAN_HWADDR2    00:13:64:35:81:BA
WLAN_HWADDR3    00:13:64:35:81:BB
ProductID       Wireless ADSL2/2+ Router
HWRevision      9415AG
SerialNumber    20061130
autopvc_enable  0
DSL_PHY_CTRL_0  0x200
mtd1    0x90020090,0x9009f000
mtd0    0x9009f000,0x90400000
DSL_PHY_CNTL_0  0x200
enable_margin_retrain   1
margin_threshold        -1
usb_vid 0x0451
usb_pid 0x6060
HWA_RNDIS       00:E0:A6:66:41:EB
HWA_HRNDIS      00:E0:A6:66:41:E1
modulation      0x0}}}
{{{
# cat /proc/iomem
00000000-13ffffff : reserved
14000000-1401ffff : System RAM
14020000-14ffffff : System RAM
  14020000-141b1197 : Kernel code
  141c2380-141dbfff : Kernel data
a8610000-a86107ff : eth0}}}
{{{
# cat /proc/avalanche/cpmac_ver
Texas Instruments : CPMAC Linux DDA version 1.9
Texas Instruments : CPMAC DDC version 0.3}}}
{{{
# cat /proc/modules
tiatm                 134272 c0031060 96    0
avalanche_usb          65208 c0020060 96    1}}}

== External Links ==
[http://librium08200.tripod.com/rr24ap.htm Details for A-link RR24AP firmware GPL licensed components]

----
["CategoryAR7Device"]
