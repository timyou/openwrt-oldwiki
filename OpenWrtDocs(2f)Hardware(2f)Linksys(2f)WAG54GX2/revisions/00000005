= Linksys WAG54GX2 =

The device is NOT supported in OpenWrt. The internals are strikingly similar to the [:OpenWrtDocs/Hardware/Netgear/DG834GT: DG834GT].

{{{
Bootloader     : CFE version 1.0.37-5.11 for BCM96348 (32bit,SP,BE)
System-On-Chip : Broadcom 6348 (CPU type 0x29107)
CPU Speed      : 240MHz, Bus: 133MHz, Ref: 26MHz
Flash size     : 8 MB
RAM            : 32 MB
Wireless       : Mini-PCI Airgo MIMO 802.11b/g Wireless LAN Controller
Ethernet       : Unknown switch
USB            : None
ADSL           : 2/2+
Serial         : yes J503
JTAG           : assumed on J201
}}}

The {{{boot_wait}}} NVRAM variable is not defined.

== Firmware notes ==

We can build custom firmwares that will upload via the regular web interface.

{{{
Analysis of WAG54GX2_A_V1.00.01.img
-----------------------------------
00010100:0035d100:gzip cramfs on /tmp/fs1
00400000:-       :CFE bootloader 0
00404a84:00404a84:CFE bootloader 1 (lzma compressed)
00410000:00410100:Firmware header
   FW_BCM.vendor = Broadcom Corporatio
   FW_BCM.version = ver. 2.0
   FW_BCM.chipid = 6348
   FW_BCM.model = 96348GW-10
   FW_BCM.image_size = 0x2431d9
   FW_BCM.loader_addr = 0x0
   FW_BCM.loader_size = 0x0
   FW_BCM.root_fs_addr = 0xbfc10100
   FW_BCM.root_fs_size = 0x1a6000
   FW_BCM.kernel_addr = 0xbfdb6100
   FW_BCM.kernel_size = 0x9d1d9
   FW_BCM.payload_checksum = 0x0
   FW_BCM.data_crc = 0x67b71da5
   FW_BCM.header_crc = 0xf8ebdca2
00410100:005b6100:gzip cramfs on /
005b610c:-       :lzma compressed kernel
}}}


== Serial Console ==
Serial console confirmed on J503.
||'''pin'''||'''signal'''||
||1||GND||
||2||TX||
||3||VCC||
||4||RX||


== JTAG ==
The device has an internal 12-pins connector on J201 although not confirmed this should be for JTAG.


== Appendix ==

=== dmesg ===

{{{
flash device_id = (0x22c9)
Total Flash size: 8192K with 135 sectors
Scratch pad is not used for this flash part.
96348GW-10 prom init
CPU revision is: 00029107
Primary instruction cache 16kb, linesize 16 bytes (2 ways)
Primary data cache 8kb, linesize 16 bytes (2 ways)
Linux version 2.4.17 (kenneth@localhost.localdomain) (gcc version 3.1) #5 ËÄ 9ÔÂ 1 15:46:17 CST 2005
Determined physical RAM map:
 memory: 01fa0000 @ 00000000 (usable)
On node 0 totalpages: 8096
zone(0): 8096 pages.
zone(1): 0 pages.
zone(2): 0 pages.
Kernel command line: root=/dev/mtdblock0 ro
bcm_console_setup
Calibrating delay loop... 239.20 BogoMIPS
Memory: 29536k/32384k available (1870k kernel code, 2848k reserved, 108k data, 64k init, 0k highmem)
Dentry-cache hash table entries: 4096 (order: 3, 32768 bytes)
Inode-cache hash table entries: 2048 (order: 2, 16384 bytes)
Mount-cache hash table entries: 512 (order: 0, 4096 bytes)
Buffer-cache hash table entries: 1024 (order: 0, 4096 bytes)
Page-cache hash table entries: 8192 (order: 3, 32768 bytes)
Checking for 'wait' instruction...  unavailable.
POSIX conformance testing by UNIFIX
mpi: No Card is in the PCMCIA slot
PCI: Fixing up bus 0
Linux NET4.0 for Linux 2.4
Based upon Swansea University Computer Society NET3.039
Initializing RT netlink socket
Starting kswapd
devfs: v1.7 (20011216) Richard Gooch (rgooch@atnf.csiro.au)
devfs: boot_options: 0x1
brcmboard: brcm_board_init entry
Module bcm63xx_cons.c v1.1 Jul 29 2005 17:16:30
block: 64 slots per queue, batch=16
loop: loaded (max 8 devices)
PPP generic driver version 2.4.1
blaadd: blaa_detect entry
adsl: adsl_init entry
Broadcom BCM6348B0 Ethernet Network Device v0.1 Jul 29 2005 17:23:10 External Switch Reverse MII (SPI Device 1)
eth0: MAC Address: 00:14:xx:xx:xx:xx
 Amd/Fujitsu Extended Query Table v1.1 at 0x0040
Physically mapped flash: Swapping erase regions for broken CFI table.
number of CFI chips: 1
mymtd = 802686a0
Creating 7 MTD partitions on "Physically mapped flash":
0x00410100-0x005b6100 : "fs"
mtd: partition "fs" doesn't start on an erase block boundary -- force read-only
0x00410000-0x007b0000 : "tag+fs+kernel"
0x00400000-0x00410000 : "bootloader"
0x007f0000-0x00800000 : "nvram"
0x00010000-0x003b0000 : "tag1+fs1"
0x00010100-0x0035d100 : "fs1"
mtd: partition "fs1" doesn't start on an erase block boundary -- force read-only
0x007b0000-0x007f0000 : "lang"
NET4: Linux TCP/IP 1.0 for NET4.0
IP Protocols: ICMP, UDP, TCP, IGMP
IP: routing cache hash table of 512 buckets, 4Kbytes
TCP: Hash tables configured (established 2048 bind 4096)
Linux IP multicast router 0.06 plus PIM-SM
klips_info:ipsec_init: KLIPS startup, Openswan KLIPS IPsec stack version: cvs2005Mar03_10:54:11
klips_info:ipsec_alg_init: KLIPS alg v=0.8.1-0 (EALG_MAX=255, AALG_MAX=251)
klips_info:ipsec_alg_init: calling ipsec_alg_static_init()
ipsec_aes_init(alg_type=15 alg_id=12 name=aes): ret=0
ipsec_aes_init(alg_type=14 alg_id=9 name=aes_mac): ret=0
ip_conntrack_rtsp v0.01 loading
ip_nat_rtsp v0.01 loading
netfilter PSD loaded - (c) astaro AG
ipt_random match loaded
NET4: Unix domain sockets 1.0/SMP for Linux NET4.0.
Ebtables v2.0 registered<6>NET4: Ethernet Bridge 008 for NET4.0
802.1Q VLAN Support v1.6  Ben Greear <greearb@candelatech.com>
vlan Initialization complete.
VFS: Mounted root (cramfs filesystem) readonly.
Mounted devfs on /dev
Freeing unused kernel memory: 64k freed
Algorithmics/MIPS FPU Emulator v1.5
download uses obsolete (PF_INET,SOCK_PACKET)
BcmAdsl_Initialize=0x800B2BD8, g_pFnNotifyCallback=0x80208EEC
AdslCoreHwReset: AdslOemDataAddr = 0xA1FF7504
device eth0 entered promiscuous mode
br0: port 1(eth0) entering listening state
eth0 Link UP.
br0: port 1(eth0) entering learning state
plm probe (plm_dump_buf @ C004E060)
PCI: Enabling device 00:01.0 (0000 -> 0002)
np->hif_regs->bus_slave.hif_ctrl.val 00000000
np->hif_regs->bus_slave.hif_ctrl.val 000000C0
wlan0: PCI Revision = 3, Slot Name[00:01.0], Slot#[1]
wlan0: at BAR0 = 0xa9000000, BAR1 = 0xa9080000, IRQ 32.
wlan0: request_irq, err = 0
wlan0: plm_reg_init Succeeded
wlan0: MAC:00:14:xx:xx:xx:xx
wlan0: plm_get_radio_eeprominfo(), err = 0
wlan0: OFFSET of dev->priv[0x64]
wlan0: OFFSET of np->hif_regs[0x105C]
wlan0: OFFSET of np->stats_mac_td_ring_flush_cnt[0xD3C]
wlan0: OFFSET of np->stats_mac_td_cnt[0xD28]
Register shadow 18
ccd_msg_handler_shadow 18 2 C004F378
br0: port 1(eth0) entering forwarding state
br0: topology change detected, propagating
Starting MAC FW module...radioID = 0 NUM_RADIO 1 - param_addr = 0x8164d0a4 start at C005DDA0
[0][1a][3][1538] bg = 1, nTx = 1, nRx = 1, cb=0, ap=1, mpci=0
[0][11][3][1] Sending CFG_DNLD_REQ
[0][11][3][1] CFG size 3252 bytes MAGIC dword is 0xdeaddead
[0][11][3][1] CFG hdr totParams 187 intParams 144 strBufSize 756/1596
[0][10][3][1] CFG RDET MIN PULSE WIDTH = 100
[0][10][3][1] CFG RDET MAX PULSE WIDTH = 100
[0][10][3][1] CFG RDET PULSE WIDTH MARGIN = 4
[0][10][3][1] CFG RDET PULSE TR CNT1 = 3
[0][10][3][1] CFG RDET PULSE TR CNT2 = 3
[0][10][3][1] CFG RDET PULSE TR CNT3 = 5
[0][10][3][1] CFG RDET RSSI TH = 60
[0][10][3][1] CFG RDET MIN IAT = 5000
[0][10][3][1] CFG RDET MAX IAT = 65535
[0][10][3][1] CFG RDET MEAS DEL  = 77
device wlan0 entered promiscuous mode
br0: port 2(wlan0) entering listening state
[0][14][2][10] Cfg param 177 indication not handled
[0][14][2][10] Cfg param 178 indication not handled
[0][10][3][10] CFG RDET FLAG  = 0
br0: port 2(wlan0) entering learning state
[0][12][3][311] Going to parse numSSID  in the START_BSS_REQ, len=8
wns msg rcvd: type = 0x1300     length = 32
wns msg rcvd: type = 0x1304     length = 48
br0: port 2(wlan0) entering forwarding state
br0: topology change detected, propagating
}}}


----
CategoryModel
