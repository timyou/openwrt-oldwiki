= Linksys WAG54GS =

{{{
Bootloader     : CFE version 1.0.37-5.11 for BCM96348 (32bit,SP,BE)
System-On-Chip : Broadcom 6348 (CPU type 0x29107)
CPU Speed      : 240MHz, Bus: 133MHz, Ref: 26MHz
Flash size     : 4 MB
RAM            : 16 MB
Wireless       : Integrated Broadcom 4318 802.11b/g
Switch         : BCM5325
USB            : None
ADSL           : 2/2+
Serial         : yes (J503)
JTAG           : assumed on J201
}}}

= Serial console =

Pinout as follows:

{{{
Ethernet ports

  o  o  o  o
GND TX VCC RX

     Leds
}}}

= Shell access =

Serial console, or http://192.168.1.1/setup.cgi?todo=debug (turn on telnet server)

= Bootlog =

Note: Yeah, those bears are really there :)

{{{
CFE version 1.0.37-5.11 for BCM96348 (32bit,SP,BE)
Build Date: ä¸  5ć 25 10:03:03 CST 2005 (root@localhost.localdomain)
Copyright (C) 2000,2001,2002,2003 Broadcom Corporation.

Initializing Arena.
Initializing Devices.
internal_open
bcm6348enet: init_emac
CPU type 0x29107: 240MHz, Bus: 133MHz, Ref: 26MHz

Total memory used by CFE:  0x80401000 - 0x8051CD00 (1162496)
Initialized Data:          0x804189C0 - 0x80419670 (3248)
BSS Area:                  0x80419670 - 0x8041AD00 (5776)
Local Heap:                0x8041AD00 - 0x8051AD00 (1048576)
Stack Area:                0x8051AD00 - 0x8051CD00 (8192)
Text (code) segment:       0x80401000 - 0x804189BC (96700)
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
Number of MAC Addresses (1-32)  : 10  
Base MAC Address                : 00:14:bf:62:0b:78  
Ethernet PHY Type               : Internal
Memory size in MB               : 16

*** Press any key to stop auto run (1 seconds) ***
Auto run second count down: 110
Code Address: 0x80010000, Entry Address: 0x801cc018
Decompression OK!
Entry at 0x801cc018
Closing network.
Starting program at 0x801cc018
Linux version 2.6.8.1 (solomon@localhost.localdomain) (gcc version 3.4.2) #6 Tue Jun 28 15:40:58 CST 2005
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
Kernel command line: root=/dev/mtdblock0 ro
brcm mips: enabling icache and dcache...
Primary instruction cache 16kB, physically tagged, 2-way, linesize 16 bytes.
Primary data cache 8kB 2-way, linesize 16 bytes.
PID hash table entries: 64 (order 6: 512 bytes)
Using 120.000 MHz high precision timer.
Dentry cache hash table entries: 4096 (order: 2, 16384 bytes)
Inode-cache hash table entries: 2048 (order: 1, 8192 bytes)
Memory: 13544k/16000k available (1539k kernel code, 2436k reserved, 233k data, 88k init, 0k highmem)
Calibrating delay loop... 237.56 BogoMIPS
Mount-cache hash table entries: 512 (order: 0, 4096 bytes)
Checking for 'wait' instruction...  unavailable.
 populate root fs
 do basic setup
NET: Registered protocol family 16
Can't analyze prologue code at 8018f33c
PPP generic driver version 2.4.2
NET: Registered protocol family 24
Using noop io scheduler
cfi_amdstd_init: Register CFI amdstd
bcm963xx_mtd driver v1.0
rootfs_addr bfc10100, kernel_addr bfe48100
do_map_probe: drv name cfi_probe
do_map_probe: drv  name cfi_probe
Call cfi_prob map 801bfe00
genprobe_ident_chips: memset
genprobe_new_chip:min 1, max 2
cfi_probe_chip:interleave 1, device_type 1
cfi_probe_chip:check QRY
cfi_probe_chip:interleave 1, device_type 2
cfi_probe_chip:check QRY
cfi_probe_chip:Check QRY OK
Physically mapped flash: Found 1 x16 devices at 0x0 in 16-bit bank
genprobe_ident_chips: like it
gen_probe: pass genprobe_ident_chips
 Amd/Fujitsu Extended Query Table at 0x0040
number of CFI chips: 1
0: offset=0x0,size=0x2000,blocks=8
1: offset=0x10000,size=0x10000,blocks=63
cfi_cmdset_0002: Disabling erase-suspend-program due to code brokenness.
mymtd = 80f95c00
Creating 5 MTD partitions on "Physically mapped flash":
0x00010100-0x00248100 : "fs"
mtd: partition "fs" doesn't start on an erase block boundary -- force read-only
0x00010000-0x003b0000 : "tag+fs+kernel"
0x00000000-0x00010000 : "bootloader"
0x003f0000-0x00400000 : "nvram"
0x003b0000-0x003f0000 : "lang"
bcm963xx_serial driver v2.0
blaadd: blaa_detect entry
adsl: adsl_init entry
Broadcom BCMPROCFS v1.0 initialized
Broadcom BCM6348B0 Ethernet Network Device v0.3 May 16 2005 15:35:15
Config Ethernet Switch Through SPI Slave Select 1
eth0: MAC Address: 00:14:BF:62:0B:78
NET: Registered protocol family 2
IP: routing cache hash table of 512 buckets, 4Kbytes
TCP: Hash tables configured (established 512 bind 1024)
ip_conntrack version 2.1 (125 buckets, 0 max) - 368 bytes per conntrack
ip_conntrack_rtsp v0.01 loading
ip_nat_rtsp v0.01 loading
ip_tables: (C) 2000-2002 Netfilter core team
netfilter PSD loaded - (c) astaro AG
ipt_random match loaded
NET: Registered protocol family 1
NET: Registered protocol family 17
Ebtables v2.0 registered
NET: Registered protocol family 8
NET: Registered protocol family 20
802.1Q VLAN Support v1.8 Ben Greear <greearb@candelatech.com>
All bugs added by David S. Miller <davem@redhat.com>
VFS: Mounted root (cramfs filesystem) readonly.
Freeing unused kernel memory: 88k freed
Call /sbin/init

init started:  BusyBox v1.00 (2005.04.04-05:49+0000) multi-call binary
init started:  BusyBox v1.00 (2005.04.04-05:49+0000) multi-call binary
Starting pid 38, console /dev/ttyS0: '/usr/etc/rcS'
Algorithmics/MIPS FPU Emulator v1.5
download uses obsolete (PF_INET,SOCK_PACKET)
wl: module license 'Proprietary' taints kernel.
PCI: Setting latency timer of device 0000:00:01.0 to 64
PCI: Enabling device 0000:00:01.0 (0004 -> 0006)
wl: srom not detected, using main memory mapped srom info (wombo board)
wl0: wlc_attach: using main broad MAC address base in NVRAM (wombo board)
wl0 MAC Address: 00:14:BF:62:0B:79
wl0: Broadcom BCM4318 802.11 Wireless Controller 3.91.23.0
BcmAdsl_Initialize=0x800F33B8, g_pFnNotifyCallback=0x801C0C04
AdslCoreHwReset: AdslOemDataAddr = 0xA0FED880
device eth0 entered promiscuous mode

     *           *  
  *      *   *      *
  *     {~._.~}      *
  *      ( Y )       *
   *    ()~*~()    *
     *  (_)-(_)  *
       *       *
         *   *
           *
ap_name=printk action=start
/bin/cp /proc/uptime /tmp//var/run/rc.printk.run
     *           *  
  *      *   *      *
  *     {~._.~}      *
  *      ( Y )       *
   *    ()~*~()    *
     *  (_)-(_)  *
       *       *
         *   *
           *
ap_name=lan action=start
/bin/cp /proc/uptime /tmp//var/run/rc.lan.run
/sbin/ifconfig br0 192.168.1.1 netmask 255.255.255.0 broadcast 192.168.1.255
     *           *  
  *      *   *      *
  *     {~._.~}      *
  *      ( Y )       *
   *    ()~*~()    *
     *  (_)-(_)  *
       *       *
         *   *
           *
ap_name=wlan action=create
/bin/cp /proc/uptime /tmp//var/run/rc.wlan.run
     *           *  
  *      *   *      *
  *     {~._.~}      *
  *      ( Y )       *
   *    ()~*~()    *
     *  (_)-(_)  *
       *       *
         *   *
           *
ap_name=wlan action=start
/bin/cp /proc/uptime /tmp//var/run/rc.wlan.run
/sbin/ifconfig wl0 up
wlctl essid ''
/sbin/ifconfig wl0 down
wlctl ap 1
wlctl close 0
wlctl country GB
Setting country code "GB"
wlctl band b
wlctl channel 6
wlctl rate 0
wlctl rts 2346
wlctl frag 2346
wlctl dtim 1
wlctl beacon 100
wlctl frameburst 0
wlctl afterburner_override -1
/sbin/ifconfig wl0 up
wlctl gmode Auto
/sbin/ifconfig wl0 down
wlctl gmode_protection_control 2
wlctl gmode_protection_override -1
wlctl plcphdr auto
wlctl mac none
wlctl macmode 0
/sbin/ifconfig wl0 up
wlctl essid 'l''i''n''k''s''y''s'
/usr/sbin/brctl addif br0 wl0
wlctl wsec 0
wlctl wsec_restrict 0
wlctl wpa_auth 0
wlctl eap 0
wlctl rmwep 0
wlctl rmwep 1
wlctl rmwep 2
wlctl rmwep 3
wlctl auth 0
wlctl essid 'l''i''n''k''s''y''s'
echo W1>/proc/led
/usr/sbin/ses -f
SES: SES_EVTO_UNCONFIGURED: status=0
     *           *  
  *      *   *      *
  *     {~._.~}      *
  *      ( Y )       *
   *    ()~*~()    *
     *  (_)-(_)  *
       *       *
         *   *
           *
ap_name=syslogd action=start
/bin/cp /proc/uptime /tmp//var/run/rc.syslogd.run
/usr/bin/killall -SIGUSR2 syslogd
killall: syslogd: no process killed
     *           *  
  *      *   *      *
  *     {~._.~}      *
  *      ( Y )       *
   *    ()~*~()    *
     *  (_)-(_)  *
       *       *
         *   *
           *
ap_name=httpd action=start
/bin/cp /proc/uptime /tmp//var/run/rc.httpd.run
tar: Short read
/bin/ln -sf /www.eng /tmp/www
/usr/sbin/mini_httpd -d /www -r "Linksys WAG54GS
B" -c '*.cgi' -t 300&
     *           *  
  *      *   *      *
  *     {~._.~}      *
  *      ( Y )       *
   *    ()~*~()    *
     *  (_)-(_)  *
       *       *
         *   *
           *
ap_name=dhcpd action=start
/bin/cp /proc/uptime /tmp//var/run/rc.dhcpd.run
/usr/sbin/udhcpd /etc/udhcpd.conf&
     *           *  
  *      *   *      *
  *     {~._.~}      *
  *      ( Y )       *
   *    ()~*~()    *
     *  (_)-(_)  *
       *       *
         *   *
           *
ap_name=ntp action=start
/bin/cp /proc/uptime /tmp//var/run/rc.ntp.run
/usr/sbin/ntp -z GMT-8& 
     *           *  
  *      *   *      *
  *     {~._.~}      *
  *      ( Y )       *
   *    ()~*~()    *
     *  (_)-(_)  *
       *       *
         *   *
           *
ap_name=route action=start
/bin/cp /proc/uptime /tmp//var/run/rc.route.run
     *           *  
  *      *   *      *
  *     {~._.~}      *
  *      ( Y )       *
   *    ()~*~()    *
     *  (_)-(_)  *
       *       *
         *   *
           *
ap_name=ripd action=start
/bin/cp /proc/uptime /tmp//var/run/rc.ripd.run
     *           *  
  *      *   *      *
  *     {~._.~}      *
  *      ( Y )       *
   *    ()~*~()    *
     *  (_)-(_)  *
       *       *
         *   *
           *
ap_name=snmp action=start
/bin/cp /proc/uptime /tmp//var/run/rc.snmp.run
/usr/bin/killall snmp
killall: snmp: no process killed
     *           *  
  *      *   *      *
  *     {~._.~}      *
  *      ( Y )       *
   *    ()~*~()    *
     *  (_)-(_)  *
       *       *
         *   *
           *
ap_name=upnp action=start
/bin/cp /proc/uptime /tmp//var/run/rc.upnp.run
/usr/bin/killall -9 upnpd
killall: upnpd: no process killed
route add -net 239.0.0.0 netmask 255.0.0.0 br0
/usr/sbin/upnpd nas0 br0 30 4&

Please press Enter to activate this console. 
}}}

----
CategoryModel
