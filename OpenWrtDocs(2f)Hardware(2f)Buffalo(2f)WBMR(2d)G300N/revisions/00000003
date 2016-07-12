Hi, I'm (GalaxyMaster).  I have purchased Buffalo WBMR-G300N and discovered that it's not yet supported by OpenWRT.  A quick examination showed that it's quite a decent device (802.11n, ADSL2+, and 4 port switch) which is likely running Linux.  During my further examination I discovered that port 1 of the switch has suspicious 4 cooper tracks on the board and I guessed that it might be a serial console.  I have disassembled the device (the tough part is to remove the front cover -- I used a knife to unlock 4 small clips, but it was scary since every clip produced a sound that might look like the clip was just broken).

What I found inside were 3 big Boadcom's chips BCM6358 (SoC), BCM5325 (Switch), and BCM4321 (WiFi).  At the corner of the PCB I found 14 holes -- looks like a MIPS standard JTAG interface.

Then I powered the device up to check it out with a multimeter.  The results were promising -- 4 cooper leads under UTP port 1 were Vcc (this one is closer to the ADSL port), Tx, Rx, GND (this one is closer to the rest of UTP ports).  Hence, I went ahead, purchased soldering iron (never soldered anything before :) ), read some soldering tutorials, and soldered 4 wires just behind UTP port 1 (I accidentally broke one of the resistors there, but I found out that they are 0-ohm, i.e. they could be just removed).

My next step was to purchase Nokia CA-42 USB cable from eBay, and once I received it I connected it to the wires soldered to the PCB.  Then I attached the device to my notebook, loaded pl2303 (a module needed to work with Serial-to-USB converter builtin into the CA-42 USB jack).  Executed minicom, configured it to 115200 8N1 with no flow control, powered the device up and got the following:

{{{
Welcome to minicom 2.3

OPTIONS: I18n
Compiled on Sep 10 2008, 20:37:46.
Port /dev/ttyUSB4

                 Press CTRL-A Z for help on special keys



CFE version 1.0.37-6.5 for BCM96358 (32bit,SP,BE)
CyberTAN rev: 1.00
Build Date: ╓@  6╓К  4 19:30:27 CST 2007 (sparq@localhost)
Copyright (C) 2000-2005 Broadcom Corporation.

Boot Address 0xbfc00000

Initializing Arena.
Initializing Devices.
Parallel flash device: name AM29LV320T, id 0x22f6, size 4096KB
CPU type 0x2A010: 300MHz, Bus: 133MHz, Ref: 64MHz
Total memory: 16777216 bytes (16MB)

Total memory used by CFE:  0x80401000 - 0x8052C6E0 (1226464)
Initialized Data:          0x8041EBA0 - 0x804211D0 (9776)
BSS Area:                  0x804211D0 - 0x8042A6E0 (38160)
Local Heap:                0x8042A6E0 - 0x8052A6E0 (1048576)
Stack Area:                0x8052A6E0 - 0x8052C6E0 (8192)
Text (code) segment:       0x80401000 - 0x8041EB94 (121748)
Boot area (physical):      0x0052D000 - 0x0056D000
Relocation Factor:         I:00000000 - D:00000000

Update mac from [02:10:18:01:00:01] to [00:16:01:a2:14:12]
Board IP address                  : 192.168.1.1
Host IP address                   : 192.168.1.100
Gateway IP address                :
Run from flash/host (f/h)         : f
Default host run file name        : vmlinux
Default host flash file name      : bcm963xx_fs_kernel
Boot delay (0-9 seconds)          : 1
Board Id Name                     : DWN814C
Psi size in KB                    : 24
Number of MAC Addresses (1-32)    : 11
Base MAC Address                  : 00:16:01:a2:14:12
Ethernet PHY Type                 : Internal
Memory size in MB                 : 16
CMT Thread Number                 : 1

*** Press any key to stop auto run (1 seconds) ***
Auto run second count down: 0
Code Address: 0x80010000, Entry Address: 0x801e5018
Decompression OK!
Entry at 0x801e5018
Closing network.
Starting program at 0x801e5018
Linux version 2.6.8.1 (sparq@localhost) (gcc version 3.4.2) #1 Fri Jun 1 13:17:20 CST 2007
Parallel flash device: name AM29LV320T, id 0x22f6, size 4096KB
Total Flash size: 4096K with 71 sectors
DWN814C prom init
CPU revision is: 0002a010
Determined physical RAM map:
 memory: 00fa0000 @ 00000000 (usable)
On node 0 totalpages: 4000
  DMA zone: 4000 pages, LIFO batch:1
  Normal zone: 0 pages, LIFO batch:1
  HighMem zone: 0 pages, LIFO batch:1
Built 1 zonelists
Kernel command line: root=31:1 ro noinitrd
brcm mips: enabling icache and dcache...
Primary instruction cache 16kB, physically tagged, 2-way, linesize 16 bytes.
Primary data cache 16kB 2-way, linesize 16 bytes.
PID hash table entries: 64 (order 6: 512 bytes)
Using 150.000 MHz high precision timer.
Dentry cache hash table entries: 4096 (order: 2, 16384 bytes)
Inode-cache hash table entries: 2048 (order: 1, 8192 bytes)
Memory: 13528k/16000k available (1636k kernel code, 2452k reserved, 235k data, 84k init, 0k highmem)
Calibrating delay loop... 299.00 BogoMIPS
Mount-cache hash table entries: 512 (order: 0, 4096 bytes)
Checking for 'wait' instruction...  unavailable.
NET: Registered protocol family 16
MPI: No Card is in the PCMCIA slot
Can't analyze prologue code at 801a79d4
devfs: 2004-01-31 Richard Gooch (rgooch@atnf.csiro.au)
devfs: devfs_debug: 0x0
devfs: boot_options: 0x1
Initializing Cryptographic API
smtp_dev reg succeed ,major_num = 253 , start make /dev/smtp_server_dev
PPP generic driver version 2.4.2
NET: Registered protocol family 24
Using noop io scheduler
bcm963xx_mtd driver v1.0
Physically mapped flash: Found 1 x16 devices at 0x0 in 16-bit bank
 Amd/Fujitsu Extended Query Table at 0x0040
Physically mapped flash: Swapping erase regions for broken CFI table.
number of CFI chips: 1
cfi_cmdset_0002: Disabling erase-suspend-program due to code brokenness.
boot_size = 131072, nvram_size= 65536
partition[0].offset=0 size=131072
partition[1].offset=20100 size=3997440
partition[2].offset=20000 size=3997696
partition[3].offset=3f0000 size=65536
Creating 4 MTD partitions on "Physically mapped flash":
0x00000000-0x00020000 : "cfe"
0x00020100-0x003f0000 : "rootfs"
mtd: partition "rootfs" doesn't start on an erase block boundary -- force read-only
0x00020000-0x003f0000 : "kernel"
0x003f0000-0x00400000 : "nvram"
brcmboard: brcm_board_init entry
bcm963xx_serial driver v2.0
u32 classifier
    OLD policer on
NET: Registered protocol family 2
IP: routing cache hash table of 512 buckets, 4Kbytes
TCP: Hash tables configured (established 512 bind 1024)
ip_conntrack version 2.1 (125 buckets, 0 max) - 368 bytes per conntrack
ip_conntrack_h323: init
ip_conntrack_pptp version 2.1 loaded
ip_nat_h323: initialize the module!
ip_nat_pptp version 2.0 loaded
ip_tables: (C) 2000-2002 Netfilter core team
Initializing IPsec netlink socket
NET: Registered protocol family 1
NET: Registered protocol family 17
NET: Registered protocol family 15
NET: Registered protocol family 8
NET: Registered protocol family 20
802.1Q VLAN Support v1.8 Ben Greear <greearb@candelatech.com>
All bugs added by David S. Miller <davem@redhat.com>
VFS: Mounted root (squashfs filesystem) readonly.
Mounted devfs on /dev
Freeing unused kernel memory: 84k freed
Firmware Version: 1.00
Hit enter to continue...killall: httpd: no process killed
Using /lib/modules/2.6.8.1/extra/bootnv.ko
Write srom_map[98] = 93
Write srom_map[99] = 91
Using /lib/modules/2.6.8.1/extra/bcm_enet.ko
Using /lib/modules/2.6.8.1/extra/atmapi.ko
Using /lib/modules/2.6.8.1/extra/blaa_dd.ko
Using /lib/modules/2.6.8.1/extra/adsldd.ko
Using /lib/modules/2.6.8.1/extra/wl.ko
name=[eth0] lan_ifname=[br0]
=====> set br0 hwaddr to eth0
Lan Ipaddr: 255.255.255.0 Netmask: 255.255.255.0................
10.0.0.254 10.0.0.254
=====> set wl0 hwaddr to br0
bcmGetPid: NAS pid = 0
bcmGetPid: NAS pid = 0
Setting SSID "testssid"
Setting SSID "Guest"
Setting country code using abbreviation: "GB"
Chanspec set to 0x2b06
wl0: current chanspec 0x2b06
[wlWep = disabled]
.............list  ..............
The boot is UNKNOWN
tftp server started
tftpd: standalone socket
HTTPD start,  port 80
dhcpd:auto_search_ip=0,firstsetlanip=1
error to open /proc/Cybertan/half_bridge_enableerror to open /proc/Cybertan/wan_ip_addr.............list  ..............
info, udhcp server (v0.9.8) started
log_ipaddr=255
Now Start syslog.........................!!zebra disabled
killall: adslpolling: no process killed
IDLE
Hit enter to continue...wan def hwaddr 00:16:01:A2:14:13
polling now .......



BusyBox v1.00 (2007.06.01-05:21+0000) Built-in shell (ash)
Enter 'help' for a list of built-in commands.

/ # ps
  PID  Uid     VmSize Stat Command
    1 0           608 S   /sbin/init noinitrd
    2 0               SW< [ksoftirqd/0]
    3 0               SW< [events/0]
    4 0               SW< [khelper]
    5 0               SW< [kblockd/0]
   17 0               SW  [pdflush]
   18 0               SW  [pdflush]
   19 0               SW  [kswapd0]
   20 0               SW< [aio/0]
   26 0               SW  [mtdblockd]
   48 0           348 S   resetbutton
   50 0           316 S   aossbutton
  220 0           396 S   nas -P /var/nas.lan0.pid -H 34954 -l br0 -i wl0 -A -m
  223 0           284 S   ap_serv -i br0
  224 0           284 S   ap_serv -i br0
  227 0           340 S   cron
  230 0           392 S   tftpd -a 10.0.0.254 -s /tmp -c -l
  232 0           368 S   httpd
  239 0           416 S   dnsmasq -i br0 -r /tmp/resolv.conf -h
  242 0           364 S   udhcpd /tmp/udhcpd.conf
  245 0           360 S   syslogd
  248 0           316 S   klogd
  250 0           392 S   /tmp/adslpolling
  361 0           440 S   /bin/sh
  402 0           328 R   ps
/ # cat /proc/cpuinfo
system type             : DWN814C
processor               : 0
cpu model               : BCM6358 V1.0
BogoMIPS                : 299.00
wait instruction        : no
microsecond timers      : yes
tlb_entries             : 32
extra interrupt vector  : no
hardware watchpoint     : no
VCED exceptions         : not available
VCEI exceptions         : not available
/ # free
              total         used         free       shared      buffers
  Mem:        13632        11976         1656            0         1332
 Swap:            0            0            0
Total:        13632        11976         1656
/ # Cann't find upnpd-igd
Maybe upnpd-igd had died, we need to re-exec it
killall: upnpd-igd: no process killed
}}}

That's all for now since I'm working on the JTAG cable (my notebook has no LPT so I need to solder an USB JTAG cable to start playing with the device).

Well, I've soldered my USB JTAG cable based on FT2232 IC and below is what I'm getting using UrJTAG:
{{{
[root@galaxy bin]# ./jtag

UrJTAG 0.9 #1417
Copyright (C) 2002, 2003 ETC s.r.o.
Copyright (C) 2007, 2008 Kolja Waschk and the respective authors

jtag> cable OOCDLink-s
Connected to libftd2xx driver.
jtag> frequency 300000
Setting TCK frequency to 300000 Hz
jtag> detect
IR length: 5
Chain length: 1
Device Id: 00000110001101011000000101111111 (0x000000000635817F)
  Manufacturer: Broadcom
  Part(0):         BCM6358
  Stepping:     V1
  Filename:     /home/galaxy/urjtag/share/urjtag/broadcom/bcm6358/bcm6358
tap_capture_ir: Invalid state:  5
tap_shift_register: Invalid state:  8
tap_capture_dr: Invalid state: 16
tap_shift_register: Invalid state: 42
ImpCode=00000110001101011000000101111111
EJTAG version: <= 2.0
EJTAG Implementation flags: R4k ASID_6 MIPS16 DMA MIPS64
Clear memory protection bit in DCR
Clear Watchdog
Potential flash base address: [0x643000], [0x1fc0000c]
Processor successfully switched in debug mode.
tap_shift_register: Invalid state:  8
Error: Unable to detect JTAG chain end!
tap_shift_register: Invalid state:  8
tap_capture_ir: Invalid state: 16
tap_shift_register: Invalid state:  8
tap_capture_dr: Invalid state: 16
tap_shift_register: Invalid state: 42
ImpCode=00000000100000011000100100000100
EJTAG version: <= 2.0
EJTAG Implementation flags: R4k MIPS16 DMA MIPS32
Clear memory protection bit in DCR
Clear Watchdog
Potential flash base address: [0x643000], [0x1fc0000c]
Processor successfully switched in debug mode.
jtag>
}}}

Unfortunately, I still hasn't figured out what do all these "Invalid state" error mean -- I'm new to JTAG and the ways it's working.
However, I've got a full flash dump with the following commands:
{{{
jtag> initbus ejtag_dma
ImpCode=00000000100000011000100100000100
EJTAG version: <= 2.0
EJTAG Implementation flags: R4k MIPS16 DMA MIPS32
Clear memory protection bit in DCR
Clear Watchdog
Potential flash base address: [0x643000], [0x1fc0000c]
Processor successfully switched in debug mode.
jtag> print
 No. Manufacturer              Part                 Stepping Instruction          Register
-------------------------------------------------------------------------------------------------------------------
   0 Broadcom                  BCM6358              V1       EJTAG_CONTROL        EJCONTROL

Active bus:
*0: EJTAG compatible bus driver via DMA (JTAG part No. 0)
        start: 0x00000000, length: 0x1E000000, data width: 32 bit, (USEG : User addresses)
        start: 0x1E000000, length: 0x02000000, data width: 16 bit, (FLASH : Addresses in flash (boot=0x1FC000000))
        start: 0x20000000, length: 0x60000000, data width: 32 bit, (USEG : User addresses)
        start: 0x80000000, length: 0x20000000, data width: 32 bit, (KSEG0: Kernel Unmapped Cached)
        start: 0xA0000000, length: 0x20000000, data width: 32 bit, (KSEG1: Kernel Unmapped Uncached)
        start: 0xC0000000, length: 0x20000000, data width: 32 bit, (SSEG : Supervisor Mapped)
        start: 0xE0000000, length: 0x20000000, data width: 32 bit, (KSEG3: Kernel Mapped)
jtag> detectflash 0x1e000000
Query identification string:
        Primary Algorithm Command Set and Control Interface ID Code: 0x0002 (AMD/Fujitsu Standard Command Set)
        Alternate Algorithm Command Set and Control Interface ID Code: 0x0000 (null)
Query system interface information:
        Vcc Logic Supply Minimum Write/Erase or Write voltage: 2700 mV
        Vcc Logic Supply Maximum Write/Erase or Write voltage: 3600 mV
        Vpp [Programming] Supply Minimum Write/Erase voltage: 0 mV
        Vpp [Programming] Supply Maximum Write/Erase voltage: 0 mV
        Typical timeout per single byte/word program: 16 us
        Typical timeout for maximum-size multi-byte program: 0 us
        Typical timeout per individual block erase: 1024 ms
        Typical timeout for full chip erase: 0 ms
        Maximum timeout for byte/word program: 512 us
        Maximum timeout for multi-byte program: 0 us
        Maximum timeout per individual block erase: 16384 ms
        Maximum timeout for chip erase: 0 ms
Device geometry definition:
        Device Size: 4194304 B (4096 KiB, 4 MiB)
        Flash Device Interface Code description: 0x0002 (x8/x16)
        Maximum number of bytes in multi-byte program: 1
        Number of Erase Block Regions within device: 2
        Erase Block Region Information:
                Region 0:
                        Erase Block Size: 65536 B (64 KiB)
                        Number of Erase Blocks: 63
                Region 1:
                        Erase Block Size: 8192 B (8 KiB)
                        Number of Erase Blocks: 8
Primary Vendor-Specific Extended Query:
        Major version number: 1
        Minor version number: 1
        Address Sensitive Unlock: Required
        Erase Suspend: Read/write
        Sector Protect: 1 sectors per group
        Sector Temporary Unprotect: Not supported
        Sector Protect/Unprotect Scheme: 29BDS640 mode (Software Command Locking)
        Simultaneous Operation: Not supported
        Burst Mode Type: Supported
        Page Mode Type: Not supported
        ACC (Acceleration) Supply Minimum: 11500 mV
        ACC (Acceleration) Supply Maximum: 12500 mV
        Top/Bottom Sector Flag: Top boot device
jtag> readmem 0x1E000000 0x02000000 flash.dump
address: 0x1E000000
length:  0x02000000
reading:
[it has taken awhile at 300kHz clock -- will update this output once another run completes]
}}}

If you have some questions or want to collaborate on preparing this device to be OpenWRT supported -- you can contact me at <gm.outside+openwrt AT gmail.com> (replace AT with the '@' sign).
----
["CategoryBCM63xx"]
