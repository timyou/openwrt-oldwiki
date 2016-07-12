= Netgear DG834GT =
The Netgear DG834GT is not as similar to the ["OpenWrtDocs/Hardware/Netgear/DG834G"] as the name may imply.  Unlike the DG834G which is [:AR7Port:AR7]-based, this device is based on the BCM6348, which is of opposite endianess (this device is big-endian).  Thus this device is not currently supported by OpenWrt. MIPS CPU is 256MHz, Atheros MiniPCI WLAN, BCM5325 switch. 4MiB flash, 16MiB RAM. More about this device might be found by searching the forum.

''' Cpu Info '''

{{{
# cat /proc/cpuinfo
system type             : 96348GW-10
processor               : 0
cpu model               : BCM6348 V0.7
BogoMIPS                : 255.59
wait instruction        : no
microsecond timers      : yes
tlb_entries             : 32
extra interrupt vector  : yes
hardware watchpoint     : no
VCED exceptions         : not available
VCEI exceptions         : not available
}}}
''' Partition MTD '''

{{{
# cat /proc/mtd
dev:    size   erasesize  name
mtd0: 0022a000 00010000 "fs"
mtd1: 003e0000 00010000 "tag+fs+kernel"
mtd2: 00010000 00002000 "bootloader"
mtd3: 00010000 00010000 "nvram"
mtd4: 00010000 00002000 "bootloader"
}}}
''' Boot Log '''

{{{
Code Address: 0x80010000, Entry Address: 0x8021c018
Decompression OK!
Entry at 0x8021c018
Closing network.
Starting program at 0x8021c018
Linux version 2.6.8.1 (root@localhost.localdomain) (gcc version 3.4.2) #9 Wed Apr 4 22:14:23 CST 2007
Total Flash size: 4096K with 71 sectors
Scratch pad is not used for this flash part.
96348GW-10 prom init
CPU revision is: 00029107
mpi: No Card is in the PCMCIA slot
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
Using 128.000 MHz high precision timer.
Dentry cache hash table entries: 4096 (order: 2, 16384 bytes)
Inode-cache hash table entries: 2048 (order: 1, 8192 bytes)
Memory: 13248k/16000k available (1856k kernel code, 2732k reserved, 235k data, 96k init, 0k highmem)
Calibrating delay loop... 255.59 BogoMIPS
Mount-cache hash table entries: 512 (order: 0, 4096 bytes)
Checking for 'wait' instruction...  unavailable.
NET: Registered protocol family 16
Can't analyze prologue code at 801de8dc
devfs: 2004-01-31 Richard Gooch (rgooch@atnf.csiro.au)
devfs: boot_options: 0x1
Initializing Cryptographic API
PPP generic driver version 2.4.2
NET: Registered protocol family 24
Using noop io scheduler
Physically mapped flash: Found 1 x16 devices at 0x0 in 16-bit bank
 Amd/Fujitsu Extended Query Table at 0x0040
number of CFI chips: 1
cfi_cmdset_0002: Disabling erase-suspend-program due to code brokenness.
Creating 5 MTD partitions on "Physically mapped flash":
0x00010100-0x0023a100 : "fs"
mtd: partition "fs" doesn't start on an erase block boundary -- force read-only
0x00010000-0x003f0000 : "tag+fs+kernel"
0x00000000-0x00010000 : "bootloader"
0x003f0000-0x00400000 : "nvram"
0x00000000-0x00010000 : "bootloader"
brcmboard: brcm_board_init entry
bcm963xx_serial driver v2.0
blaadd: blaa_detect entry
adsl: adsl_init entry
Broadcom BCM6348A2 Ethernet Network Device v0.3 Apr  4 2007 19:32:39
Config Ethernet Switch Through SPI Slave Select 1
eth0: MAC Address: 00:1B:2F:32:AB:31
NET: Registered protocol family 2
IP: routing cache hash table of 512 buckets, 4Kbytes
TCP: Hash tables configured (established 512 bind 1024)
IPv4 over IPv4 tunneling driver
ip_conntrack version 2.1 (125 buckets, 1000 max) - 368 bytes per conntrack
ip_conntrack_h323: init
ip_nat_h323: initialize the module!
ip_tables: (C) 2000-2002 Netfilter core team
NET: Registered protocol family 1
NET: Registered protocol family 17
NET: Registered protocol family 8
NET: Registered protocol family 20
802.1Q VLAN Support v1.8 Ben Greear <greearb@candelatech.com>
All bugs added by David S. Miller <davem@redhat.com>
VFS: Mounted root (cramfs filesystem) readonly.
Mounted devfs on /dev
Freeing unused kernel memory: 96k freed
init started:  BusyBox v1.00 (2007.01.29-08:12+0000) multi-call binary
init started:  BusyBox v1.00 (2007.01.29-08:12+0000) multi-call binary
Starting pid 40, console /dev/tts/0: '/usr/etc/rcS'
ipt_string: module license 'unspecified' taints kernel.
netfilter PSD loaded - (c) astaro AG
ipt_random match loaded
insmod: cannot insert `/lib/modules/ipt_mark.ko': Success (22): Success
BcmAdsl_Initialize=0x8011D968, g_pFnNotifyCallback=0x80212274
AnnexCParam=0x7FFF7E88 AnnexAParam=0x00000980 adsl2=0x00000000
pSdramPHY=0xA0FFFFF8, 0x4004000 0xFFFFFFFF
AdslCoreHwReset: AdslOemDataAddr = 0xA0FFD274
AnnexCParam=0x7FFF7E88 AnnexAParam=0x00000980 adsl2=0x00000000
dgasp: kerSysRegisterDyingGaspHandler: dsl0 registered
device eth0 entered promiscuous mode
ap_name=(null) action=start
br0: port 1(eth0) entering learning state
br0: topology change detected, propagating
br0: port 1(eth0) entering forwarding state
killall: upnpd: no process killed
killall: upnpd: no process killed
UPnP Initialized
Intialized UPnP
        with fullurl=http://192.168.0.1:49152/gateway.xml
                     ipaddress=192.168.0.1 port=49152
             web_dir_path=/usr/upnp/
             desc_doc_url=http://192.168.0.1:49152
Specifying the webserver root directory -- /usr/upnp/
Registering the RootDevice
RootDevice Registered
Initializing State Table
fullurl http://192.168.0.1:49152/gateway.xml
route: SIOC[ADD|DEL]RT: File exists
Please press Enter to activate this console.
}}}
''' CFE Menu '''

{{{
CFE version 1.0.37-5.11 for BCM96348 (32bit,SP,BE)
Build Date: Fri Sep 17 15:59:48 CST 2004 (root@Run-P4)
Copyright (C) 2000,2001,2002,2003 Broadcom Corporation.
Initializing Arena.
Initializing Devices.
internal_open
bcm6348enet: init_emac
CPU type 0x29107: 256MHz, Bus: 128MHz, Ref: 32MHz
Total memory used by CFE:  0x80401000 - 0x8051C910 (1161488)
Initialized Data:          0x80418630 - 0x804192D0 (3232)
BSS Area:                  0x804192D0 - 0x8041A910 (5696)
Local Heap:                0x8041A910 - 0x8051A910 (1048576)
Stack Area:                0x8051A910 - 0x8051C910 (8192)
Text (code) segment:       0x80401000 - 0x80418624 (95780)
Boot area (physical):      0x0051D000 - 0x0055D000
Relocation Factor:         I:00000000 - D:00000000
Board IP address                : 192.168.1.1:ffffff00
Host IP address                 : 192.168.1.100
Gateway IP address              :
Run from flash/host (f/h)       : f
Default host run file name      : vmlinux
Default host flash file name    : bcm963xx_fs_kernel
Boot delay (0-9 seconds)        : 1
Board Id Name                   : 96348GW-10
Psi size in KB                  : 16
Number of MAC Addresses (1-32)  : 2
Base MAC Address                : 00:1b:2f:32:ab:31
Ethernet PHY Type               : Internal
Memory size in MB               : 16
*** Press any key to stop auto run (1 seconds) ***
Auto run second count down: 1
CFE>
*** command status = -1
CFE> help
Available commands:
d                   Download
a                   Asmod
w                   Write the whole image start from beginning of the flash
e                   Erase [n]vram or [a]ll flash except bootrom
r                   Run program from flash image or from host depend on [f/h] flag
p                   Print boot line and board parameter info
c                   Change booline parameters
f                   Write image to the flash
i                   Erase persistent storage data
b                   Change board parameters
reset               Reset the board
flashimage          Flashes a compressed image after the bootloader.
help                Obtain help for CFE commands
}}}
''' Serial Console 
'''

Serial console is J503.
||'''pin''' ||'''signal''' ||
||1 ||GND ||
||2 ||TX ||
||3 ||VCC ||
||4 ||RX ||

'''
'''

''' JTAG Port '''

Jtag Port is J201 this port is verified.

Disposition on the board:

||2 ||4 ||6 ||8 ||10 ||12 ||
||1 ||3 ||5 ||7 || 9 ||11 ||

 

||nTRST || 1 || 2 || GND ||
||TDI || 3 || 4 || GND ||
||TDO || 5 || 6 || GND ||
||TMS || 7 || 8 || GND ||
||TCK || 9 ||10 || GND ||
||nSRST ||11 ||12 || GND ||


For programm the firmware with JTAG Port read this [:OpenWrtDocs/Customizing/Hardware/JTAG Cable]



----
CategoryModel ["CategoryBCM63xx"]
