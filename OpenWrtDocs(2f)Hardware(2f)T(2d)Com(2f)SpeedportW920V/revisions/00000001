#pragma section-numbers off
[[TableOfContents]]

= T-Com Speedport W920V =

Users known to have this device:  abraXxl (still in avm mode)

== Hardware Info ==

Uses a TI AR7 CPU, UR8 chipset with Infineon VINAX DSL Chipset and Atheros 5416 onboard wireless.
It has 16MB flash and 64MB RAM (!), USB2.

The Speedport W920V also features as ISDN socket and two telephone sockets for VoIP use.

CPU: UR8@366Mhz

It also has a single 3.3v serial port, the original T-Com firmware allows you shell access with no password to the device though the serial port.

=== Photos ===

None yet

=== Serial Port ===
It has a 3.3v serial port to the lower right of the CPU, near the two RAM ICs.

The general location of the port and it's pin-out is as follows:

{{{
        Top right of PCB
____________________________
               Antenna      |
F                           |
L        WIFI    WIFI  Ant  |
A  CPU   CHIP    CHIP       |
S        BIG     small      |
H  R R                 Ant  |
   A A   o GND              |
   M M   o RX               |
   R R   o TX               |
   A A   o VCC              |
   M M                      |
                            |
VINAX                       |
____________________________|
}}}

Serial port settings: 38400 8N1


=== Boot log from original firmware ===
With some useful output of some commands at the end.

{{{

(AVM) EVA Revision: 1.458 Version: 1458
(C) Copyright 2005 AVM Date: Apr 11 2008 Time: 10:36:56 (0) 2 0x0-0x41D

[FLASH:] ST Uniform-MirrorBit-Flash 16MB 64 Bytes WriteBuffer
[FLASH:](Eraseregion [0] 128 sectors a 128kB) 
[SYSTEM:] UR8 on 360MHz/120MHz syncron

Eva_AVM >AVM decompress Kernel:
.................executeProgram on 0x942A7000
[prom_init] 0
[prom_init] argv[0]=gocommand
[prom_init] fw_arg3 0x94643b70

LINUX started...
flashsize=16 MByte
&_end=0x9432000c PFN_ALIGN(&_end)=0x94321000 CPHYSADDR(PFN_ALIGN(&_end))=0x14321000 memsize=0x4000000
[c55] membase = 0x14000000 memtop = 0x18000000 memsize = 0x4000000
[c55] memsegment1(size) = 0x40000 memsegment2(size) = 0x0
[c55] mdesc[0]: base = 0x14000000 size = 0x3fc0000
[c55] mdesc[1]: base = 0x17fc0000 size = 0x40000
[c55] mdesc[2]: base = 0x18000000 size = 0x0
[c55] mdesc[3]: base = 0x0 size = 0x0
Config serial console: console=ttyS0,38400n8r
[ur8_pre_init] System Clk = 60000000 Hz               

(ur8_gpio_init)
ur8_clk_get_pll_factor: 300000000
ur8_get_pci_clock 33333333
(mips_reboot_setup)
plat_timer_setup TIMER IRQ: 7
Linux version 2.6.19.2 (2113) (gcc version 3.4.6) #2 Fri Dec 19 10:34:20 CET 2008
cpu-probe: Manufacturer MIPS
mips-config1: JTAG pressent
mips-config1: TLB size 16
mips-config3: Vectored interrupts implmented
CPU revision is: 00019068
[mips_clock] default 360000000 MHz
[ur8_clk_set_emif] SDRAM Refresh 0x3a8 Timing 0x2214717 Bank 0x21 Async 0xc42c301
[ur8_pci_init]
[pci] default: 33 MHz
[setup_pci_master]
[setup_pci_slave]
Exposing 67108864 memory over PCI
Setup Complete, Enabling PCI Interface
PCI Interface Running
PCI controller initialized
[ur8_vbus_set_prio] instance vbus_nwss_dma level 2 escalator disabled (count 255, floor 7)
[ur8_vbus_set_prio] instance vbus_sar_pdsp level 2 escalator disabled (count 255, floor 7)
[ur8_vbus_set_prio] instance vbus_buffer_manager level 2 escalator disabled (count 255, floor 7)
[ur8_vbus_set_prio] instance vbus_usb level 5 escalator disabled (count 255, floor 7)
[ur8_vbus_set_prio] instance vbus_vlynq level 7 escalator disabled (count 255, floor 7)
[ur8_vbus_set_prio] instance vbus_pci level 5 escalator disabled (count 255, floor 7)
[ur8_vbus_set_prio] instance vbus_c55 level 3 escalator disabled (count 255, floor 7)
[ur8_vbus_set_prio] instance vbus_tdm level 0 escalator disabled (count 255, floor 7)
[ur8_vbus_set_prio] instance vbus_mips level 3 escalator disabled (count 255, floor 7)
Determined physical RAM map:
 memory: 03fc0000 @ 14000000 (usable)
 memory: 00040000 @ 17fc0000 (reserved)
[init_bootmem]
[free_bootmem]
[reserve_bootmem]
[mem_map-hack]: reduce size from 3145728 524288 Bytes
[mem_map-hack]: move map base from 0x94324000 to 0x940a4000
[request_resource] Kernel code: start 0x14000000 < root->start 0x17fc0000
[request_resource] Kernel data: start 0x14205de0 < root->start 0x17fc0000
Built 1 zonelists.  Total pages: 97473
Kernel command line:  console=ttyS0,38400n8r
Primary instruction cache 16kB, physically tagged, 4-way, linesize 16 bytes.
Primary data cache 16kB, 4-way, linesize 16 bytes.
Synthesized TLB refill handler (20 instructions).
Synthesized TLB load handler fastpath (32 instructions).
Synthesized TLB store handler fastpath (32 instructions).
Synthesized TLB modify handler fastpath (31 instructions).
PID hash table entries: 2048 (order: 11, 8192 bytes)
CPU frequency 360.00 MHz
Using 180.000 MHz high precision timer.
Dentry cache hash table entries: 65536 (order: 6, 262144 bytes)
Inode-cache hash table entries: 32768 (order: 5, 131072 bytes)
[free_all_bootmem]
Memory: 61056k/65280k available (2071k kernel code, 4120k reserved, 640k data, 140k init, 0k highmem)
Mount-cache hash table entries: 512
Checking for 'wait' instruction...  available.
NET: Registered protocol family 16
[ur8_mtd_init]
[ur8_mtd_init] flashsize = 0x01000000 Byte 16 MBytes
[ur8_mtd_init] mtd[0] = 0x90000000,0x90000000
[ur8_mtd_init] mtd[1] = 0x90020000,0x90F80000
[ur8_mtd_init] mtd[2] = 0x90000000,0x90020000
[ur8_mtd_init] mtd[3] = 0x90F80000,0x90FC0000
[ur8_mtd_init] mtd[4] = 0x90FC0000,0x91000000
[ur8_mtd_init] mtd[5] = 0x90000000,0x90000000
pcibios_read_config: accessing present PCI slot : 14, where 0, size 4
Master and Slave Enabled
pktsched: using high resolution timer
NET: Registered protocol family 2
IP route cache hash table entries: 4096 (order: 2, 16384 bytes)
TCP established hash table entries: 16384 (order: 4, 65536 bytes)
TCP bind hash table entries: 8192 (order: 3, 32768 bytes)
TCP: Hash tables configured (established 16384 bind 8192)
TCP reno registered
squashfs: version 3.2 (2007/01/02) Phillip Lougher
Installing knfsd (copyright (C) 1996 okir@monad.swb.de).
fuse init (API version 7.8)
io scheduler noop registered (default)
avm_net_trace: Up and running.
[avm] configured: watchdog event debug enable direct gpio 

AVM_WATCHDOG: Watchdog Driver for AR7 Hardware (Version 1.0, build: Dec 19 2008 10:33:54)
Serial: 8250/16550 driver $Revision: 1.3 $ 1 ports, IRQ sharing disabled
serial8250: ttyS0 at MMIO 0x0 (irq = 15) is a UR8_UART
[cpmac] Version: URL: svn://EmbeddedVM/home/SVN/drivers/cpmac/tags/1.102-r740-trunk-PPPoA_und_Tantos13  -  Revision 538:741  -  Fr 19. Dez 10:34:07 CET 2008 
[cpmac] [cpmac_if_register] dev cpmac0 (phy_id 0) registered
tun: Universal TUN/TAP device driver, 1.6
tun: (C) 1999-2004 Max Krasnyansky <maxk@qualcomm.com>
physmap platform flash device: 01000001 at 10000000
physmap-flash.1: Found 1 x16 devices at 0x0 in 16-bit bank
 Amd/Fujitsu Extended Query Table at 0x0040
physmap-flash.1: CFI does not contain boot bank location. Assuming top.
number of CFI chips: 1
cfi_cmdset_0002: Disabling erase-suspend-program due to code brokenness.
RedBoot partition parsing not available
[ur8_jffs2_parser_function] mtd_info->name physmap-flash.1 mtd_info->index 0 param=0 p_mtd_pat=0x97f5e43c
[ur8_jffs2_parser_function] try partition kernel (offset 0x20000 len 16121856)
[ur8_jffs2_parser_function] magic 20031985 found @pos 0x740000, size 8650752
[ur8_squashfs_parser_function] mtd_info->name physmap-flash.1 mtd_info->index 0 param=0 p_mtd_pat=0x97f5e43c
[ur8_squashfs_parser_function] *p_mtd_pat->name filesystem
[ur8_squashfs_parser_function] try partition kernel (offset 0x20000 len 16121856 blocksize=20000)
[ur8_squashfs_parser_function] magic found @pos 0x102e00
6 find_squashfs partitions found on MTD device physmap-flash.1
Creating 6 MTD partitions on "physmap-flash.1":
0x00102e00-0x00f80000 : "rootfs"
mtd: partition "rootfs" doesn't start on an erase block boundary -- force read-only
[ur8_mtd_add_notifier] name rootfs
[ur8_mtd_add_notifier] use rootfs
[ur8_mtd_add_notifier] root device: /dev/mtdblock0 (rootfs)
0x00020000-0x00102e00 : "kernel"
mtd: partition "kernel" doesn't end on an erase block -- force read-only
[ur8_mtd_add_notifier] name kernel
[ur8_mtd_add_notifier] skip kernel
0x00000000-0x00020000 : "urlader"
[ur8_mtd_add_notifier] name urlader
[ur8_mtd_add_notifier] skip urlader
0x00f80000-0x00fc0000 : "tffs (1)"
[ur8_mtd_add_notifier] name tffs (1)
[ur8_mtd_add_notifier] skip tffs (1)
0x00fc0000-0x01000000 : "tffs (2)"
[ur8_mtd_add_notifier] name tffs (2)
[ur8_mtd_add_notifier] skip tffs (2)
0x00740000-0x00f80000 : "jffs2"
[ur8_mtd_add_notifier] name jffs2
[ur8_mtd_add_notifier] skip jffs2
Generic platform RAM MTD, (c) 2004 Simtec Electronics
mtd-ram mtd-ram.2: no memory resource specified
[ur8_ram_mtd_set_rw] PLATRAM_RO
mtd-ram: probe of mtd-ram.2 failed with error -2
CAPI Subsystem Rev 1.1.2.8
TCP cubic registered
mcfw: IGMPv3 fast forwarding
NET: Registered protocol family 1
NET: Registered protocol family 17
NET: Registered protocol family 8
NET: Registered protocol family 20
MUSB UR8 pdev active!
PCI_STATUS_SET: 40000
PCI_STATUS_CLR: 40000
PCI_HOST_INT_EN: 0
PCI_HOST_INT_CLR: 0
PCI_BE_INT_En: 0
PCI_BE_INT_CLR: 0
[pci_int_init] done
TFFS: tiny flash file system driver. GPL (c) AVM Berlin (Version 2.0)
Time: MIPS clocksource has been installed.
      mount on mtd3 and mtd4 (double buffering)
Adam2 environment variables API installed.
[avm_new] push_button_gpio=25 value=0 enabled
VFS: Mounted root (squashfs filesystem) readonly.
Freeing prom memory: 0kb freed
Freeing unused kernel memory: 140k freed
init started: BusyBox v1.8.2 (2008-11-19 12:13:49 CET)
starting pid 107, tty '/dev/console': '/etc/init.d/rc.S'
AVM_WATCHDOG: System Init UEberwachung 240 Sekunden
TFFS Name Table F
HWRevision	135.1.0.6
ProductID	Fritz_Box_DECT_W920V
SerialNumber	0000000000000000
annex	B
autoload	yes
bootloaderVersion	1.458
bootserport	tty0
cpufrequency	360000000
firstfreeaddress	0x946BD81C
firmware_version	tcom
firmware_info	65.04.70
flashsize	0x01000000
jffs2_size	132
maca	00:1F:3F:xxx
macb	00:1F:3F:xxx
macwlan	00:1F:3F:xxx
macdsl	00:1F:3F:xxx
memsize	0x04000000
modetty0	38400,n,8,1,hw
modetty1	38400,n,8,1,hw
mtd0	0x90000000,0x90000000
mtd1	0x90020000,0x90F80000
mtd2	0x90000000,0x90020000
mtd3	0x90F80000,0x90FC0000
mtd4	0x90FC0000,0x91000000
my_ipaddress	192.168.178.1
prompt	Eva_AVM
ptest	
req_fullrate_freq	120000000
sysfrequency	120000000
urlader-version	1458
usb_board_mac	00:1F:3F:xxxxxxxx
usb_rndis_mac	00:1F:3F:xxxxxxxx
usb_device_id	0x0000
usb_revision_id	0x0000
usb_device_name	USB DSL Device
usb_manufacturer_name	AVM
webgui_pass	xxxxxxxxxxxxx
wlan_key	xxxxxxxxxxxxxx
starting AVM_LED_EVENTS
led_modul_Fritz_Box_DECT_W920V: module license '
(C) Copyright 2008 by AVM
' taintskernel.
[led_gpio_bit_driver_init] gpio 1 name power
[led_gpio_bit_driver_init] gpio 36 name update
[led_gpio_bit_driver_init] gpio 32 name dsl
[led_gpio_bit_driver_init] gpio 17 name pppoe
[led_gpio_bit_driver_init] gpio 9 name voip_con
[led_gpio_bit_driver_init] gpio 27 name festnetz
[led_gpio_bit_driver_init] gpio 21 name dual1
[led_gpio_bit_driver_init] gpio 22 name dual2
[led_gpio_bit_driver_init] gpio 28 name wlan
mknod: /var/flash/ar7.cfg: File exists
patch_dectfw: patch_adress: 6718 max_len: 22 with Version 2 Len: 16
patch_dectfw: c0061000, datalen = 30535, 
dect_loader(first): unknown 0 in state dect_wait_for_ack received

***********************************************************
dect_file_process: upload of '/lib/modules/dectfw_secondlevel.hex' successfull
[avm_new]push_button_ctrl: gpio=30 value=0 enabled
[avm_new]push_button_ctrl:'Werkseinstellungs-Taster': enable=2 gpio=30 regaddr=00000000 button_type=1
[avm_new]push_button_ctrl: gpio=31 value=0 enabled
[avm_new]push_button_ctrl:'Taster_4': enable=2 gpio=31 regaddr=00000000 button_type=0
[piglet]bitfile '/lib/modules/microvoip_isdn_top.bit'
[piglet] Read 169297 bytes total from file
[piglet]TDM: FS: 8000 Hz CLK:2047820 Hz
[jffs2] xx=mtd5: 00840000 00020000 "jffs2"
[jffs2] i=mtd5:
[jffs2] jffs2_pat=5
[jffs2] i=00840000
[jffs2] jffs2_size=132
[jffs2] i=00020000
[jffs2] i="jffs2"
[jffs2] load jffs2 module
JFFS2 version 2.2. (NAND) (C) 2001-2006 Red Hat, Inc.
[jffs2] mount jffs 
[jffs2] write env variable jffs2_size to 132
TAM: create JFFS2 directory /data/tam

[avm_debug]redirect kernel-messages (/dev/debug)
[4294938233][DECTSTUB] {DspInit}
[4294938233][DECTSTUB] {dsp_router_connect} 0 <- 12
[4294938233][DECTSTUB] {dsp_router_connect} 1 <- 12
[4294938233][DECTSTUB] {dsp_router_connect} 2 <- 12
[4294938234][DECTSTUB] {dsp_router_connect} 3 <- 12
[4294938234][DECTSTUB] {dsp_router_connect} 4 <- 15
[4294938234][DECTSTUB] {dsp_router_connect} 5 <- 15
[4294938234][DECTSTUB] {dsp_router_connect} 6 <- 15
VINAX Driver, Version 0.1.5.99
(c) Copyright 2005, Infineon Technologies AG
<VINAX COMPATIBILITY CHECK> interface version is 1
VINAX_DRV: VINAX_InitModuleRegCharDev: Registering device vinax, vinax (PROC_FS)
T >> init dev: base address = 0x1C000000
T >> parse: opt value = 9
T >> open device: /dev/vinax/0.
T >> ioct(FIO_VINAX_DEV_INIT): baseaddr = 0x1C000000, IRQ = 9
usedIrq: 9
VINAX: GOT INTERRUPT: startup
locking interrupts
+++++++++++++++++++++++++++++++++++++++init ATM OAM!!
T >> Line = 00 Return = 0
T >> open device: /dev/vinax/0.
T >> Start Download </lib/modules/vinax_fw_adsl.bin>, size: 540916
device already started--> execute FW Download
VINAX_DRV[00]: Start Download - DMA transfere
VINAX_DRV[00]: BM-7 CS: EMPTY <data> page[53] found - skipped
VINAX_DRV[00]: BM-7 CS: EMPTY <data> page[54] found - skipped
VINAX_DRV[00]: BM-7 CS: EMPTY <data> page[55] found - skipped
VINAX_DRV[00]: BM-7 CS: EMPTY <code> page[61] found - skipped
VINAX_DRV[00]: BM-7 CS: EMPTY <data> page[62] found - skipped
checked download state machine (= 4)
VINAX_DRV[00]: DL/CS - Wait for 1. Response
VINAX_DRV[00]: BM-7 CS: EMPTY <data> page[40] found - skipped
T >> Line = 00 Return = 0
state has changed
VINAX_DRV[00]: DL/CS 1. response received - done

==================
Configuring Vinax
==================
DSL Mode=VB
Profile=17A
Trellis=on
VDSL: US_max_datenrate = 150000000
VDSL: DS_max_datenrate = 150000000
ADSL: US_max_datenrate = 32768000
ADSL: DS_max_datenrate = 32768000


DSL: start DSL daemon (pid 237).
DSL: using firmware file - /lib/modules/vinax_fw_adsl.bin
DSL: using dynamic FW script - /nv/get_fw.sh
DSL: DSL daemon running in background now! (pid=239)
DSL: Device granularity is 1
DSL: No firmware pointer
DSL: No 2nd firmware pointer
DSL: Given warmstart memory will be analyzed...
DSL: using external memory
DSL: No mapping information (line -> device channel) provided. Taking internal default settings.
DSL[00]: VINAX driver : 0.1.5.99
unlocking interrupts
DSL[00]: VINAXX[0] reset done -         mask [0]0x00000001 [1]0x00000000 [2]0x00000000 [3]0x00000000
polling for dsl_daemon (attempt 1).
dsl_daemon not ready yet. Try again in 2 seconds
 ===================================================
 AVM: no response from Modem! Workaround...now!
 ===================================================
1) SW reset
unlocking interrupts
polling for dsl_daemon (attempt 2).
dsl_daemon not ready yet. Try again in 2 seconds
reset done. wait for first modem response.
no response! Try again?
2) SW reset
unlocking interrupts
reset done. wait for first modem response.
no response! Try again?
3) SW reset
unlocking interrupts
polling for dsl_daemon (attempt 3).
VINAX: GOT INTERRUPT: user reset
locking interrupts
dsl_daemon not ready yet. Try again in 2 seconds
reset done. wait for first modem response.
Done. Modem state= 0
 =======================================
 workaround worked! (after 3 attempt(s))
 exiting workaround.
 =======================================
 na bitte geht doch 
 =======================================
VINAX_DRV[00]: Start Download - DMA transfere
VINAX_DRV[00]: BM-7 CS: EMPTY <data> page[53] found - skipped
VINAX_DRV[00]: BM-7 CS: EMPTY <data> page[54] found - skipped
VINAX_DRV[00]: BM-7 CS: EMPTY <data> page[55] found - skipped
VINAX_DRV[00]: BM-7 CS: EMPTY <code> page[61] found - skipped
VINAX_DRV[00]: BM-7 CS: EMPTY <data> page[62] found - skipped
checked download state machine (= 4)
VINAX_DRV[00]: DL/CS - Wait for 1. Response
polling for dsl_daemon (attempt 4).
dsl_daemon not ready yet. Try again in 2 seconds
VINAX_DRV[00]: BM-7 CS: EMPTY <data> page[40] found - skipped
state has changed
VINAX_DRV[00]: DL/CS 1. response received - done
DSL: 
DSL: *****************************************************
DSL: DSL library version: 2.1.2
DSL: *****************************************************
DSL: Number of devices       :   1
DSL: Number of lines         :   1
DSL: Number of lines/device  :   1
DSL: Number of channels/line :   1
DSL: 
DSL: Memory usage of warm start resistent data base
DSL:   magic key data base          :       4 bytes
DSL:   instance config data base    :      28 bytes
DSL:   device config data base      :       4 bytes
DSL:   global array config data base:       0 bytes
DSL:   line config data base        :     276 bytes
DSL:   channel config data base     :     136 bytes
DSL:   line array config data base  :    1216 bytes
DSL:                                 --------------
DSL:   Total                        :    1664 bytes
DSL: 
DSL: Memory usage of status data base
DSL:   device status data base      :       8 bytes
DSL:   line status data base        :     356 bytes
DSL:   channel status data base     :     312 bytes
DSL:                                 --------------
DSL:   Total                        :     676 bytes
DSL: 
DSL: Context memory usage
DSL:   context structure            :    1904 bytes
DSL:   Timeout event lists          :      96 bytes
DSL:                                 --------------
DSL:   Total                        :    2000 bytes
DSL: *****************************************************
DSL: 
DSL: DSL_Init finished with device mask 0x00000001
DSL: Thread ID for thread VinaxCtrl is 1026 (PID 258)
DSL: Thread ID for thread tPM_Tick is 2051 (PID 259)
DSL: Thread ID for thread DmsAlive is 3076 (PID 260)
DSL: Thread ID for thread tAgentX is 4101 (PID 261)
DSL: Thread tAgentX, ID 4101 (PID 261) exited
DSL: Thread ID for thread tPipe_0 is 5126 (PID 262)
DSL: Thread ID for thread tPipe_1 is 6151 (PID 263)
DSL: Thread ID for thread tPipe_2 is 7176 (PID 264)
polling for dsl_daemon (attempt 5).
DSL[00]: line 0 on device 0 not accessible!
dsl_daemon not ready yet. Try again in 2 seconds
DSL[00]: Device Start EVT - UsrRst, DrvState 1 --> 1
DSL[00]: Line in reset - block!
polling for dsl_daemon (attempt 6).
Wait for dsl_daemon: success after 6 attempts. Keep booting now.

[dsl_pipe] dsl serial number successfully set to "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
nReturn=0 
nReturn=0 nLine=0

nReturn=0 nLine=0 nChannel=0 nDirection=0

nReturn=0 nLine=0 nChannel=0 nDirection=1

nReturn=0 nLine=0 nChannel=0

nReturn=0 nLine=0 nChannel=0

nReturn=0 nLine=0

enabling ADSL AnnexB and VDSL2
nReturn=0 nLine=0

nReturn=0 nLine=0

automode enabled
nReturn=0 nLine=0 nDirection=0

nReturn=0 nLine=0 nDirection=1

nReturn=0 nLine=0 nDirection=0

nReturn=0 nLine=0 nDirection=1

nReturn=1002 nLine=0

nReturn=0 nData="0049 0000 0001 "

++++++++++++++++++++++++++++ OAM activate ++++++++++++++++++++++++
++++++++++++++++++++++++++++ OAM activated!!!! ++++++++++++++++++++++++
================== Short Packet Filter deactivated =============
================== ethernet OAM control =============
================== ADSL Detected ==================
================== packet filter configured  =============
================== filter offset 1 configured  =============
================== filter offset 2 configured  =============
================== packet filter activated =============
================== avm_vinax_configure_single_cell_extraction configured 1 =============
================== avm_vinax_configure_single_cell_extraction configured 2  =============
================== avm_vinax_configure_single_cell_extraction configured 3  =============
================== avm_vinax_configure_single_cell_extraction configured 4  =============
================== avm_vinax_configure_single_cell_extraction configured 5  =============
================== avm_vinax_configure_single_cell_extraction configured 6  =============
================== avm_vinax_configure_single_cell_extraction configured 7  =============
VINAX_DRV[00]: BM-7 CS: EMPTY <data> page[41] found - skipped
VINAX_DRV[00]: BM-7 CS: EMPTY <data> page[12] found - skipped
VINAX_DRV[00]: BM-7 CS: EMPTY <data> page[13] found - skipped
nReturn=0 nData="0041 0000 0001 "

sCommand=DSL_CBS_LINE_STATE nLine=00 nLineState=00000200 
dsl_daemon: new modem state 512 
nReturn=0 

[pcmlink] driver init
[4294941099][isdn]svn:2458
driver params overwritten io_addr=0x0 irq_num=0
[4294941198]PCMLINK: Version 4.672 Slots=13 BChan=11(Analog=3) DChan=2 Fifo=128 
avm_dect driver init
[DECTDRV] [avm_dect]:(success)
[DECTDRV] [avm_dect]avm_dect_thread: start
[DECTDRV] dect_os_init
[DECTDRV] dect_os_init: InitFunc called for TaskId 0x03
[DECTDRV] dect_os_init: InitFunc called for TaskId 0x04
[DECTDRV] dect_os_init: InitFunc called for TaskId 0x05
[DECTDRV] dect_os_init: InitFunc called for TaskId 0x01
[DECTDRV] dect_os_init: InitFunc called for TaskId 0x10
[DECTDRV] dect_os_init: InitFunc called for TaskId 0x14
[DECTDRV] dect_os_init: InitFunc called for TaskId 0x06
[DECTDRV] dect_os_init: InitFunc called for TaskId 0x0D
[DECTDRV] dect_os_init: InitFunc called for TaskId 0x21
[DECTDRV] pcm_TaskInit
[DECTDRV] dect_os_init: InitFunc called for TaskId 0x22
[dect_uicp_file_init] init()
[4294941457][DCTDRV] (RFPI_REQ) UI_TASK->FP_CCF_TASK  
[4294941462][DCTDRV] (RFPI_CFM) FP_CCF_TASK->UI_TASK  
[4294941462][DCTDRV] (STUB_FP_CAP_IND) FP_CCF_TASK->UI_TASK  
[4294941462][DECTDRV] CAP_IND, RFPI is:  01 2A 6D 1F 90
usbcore: registered new interface driver usbfs
usbcore: registered new interface driver hub
usbcore: registered new device driver usb
musb_hdrc: version 2.2a/db-0.5.1, cppi-dma, host, debug=0
musb_hdrc: ConfigData=0x06 (UTMI-8, dyn FIFOs, SoftConn)
musb_hdrc: MHDRC RTL version 1.500 
musb_hdrc: setup fifo_mode 2
musb_hdrc: 7/9 max ep, 2624/4096 memory
musb_hdrc: hw_ep 0shared, max 64
musb_hdrc: hw_ep 1tx, max 512
musb_hdrc: hw_ep 1rx, max 512
musb_hdrc: hw_ep 2tx, max 512
musb_hdrc: hw_ep 2rx, max 512
musb_hdrc: hw_ep 3shared, max 256
musb_hdrc: hw_ep 4shared, max 256
musb_hdrc: USB Host mode controller at A3400000 using DMA, IRQ 39
musb_hdrc musb_hdrc: MUSB HDRC host driver
musb_hdrc musb_hdrc: new USB bus registered, assigned bus number 1
usb usb1: configuration #1 chosen from 1 choice
hub 1-0:1.0: USB hub found
hub 1-0:1.0: 1 port detected
TI USB 2.0 Host started
/etc/init.d/rc.S: line 1355: cannot create /dev/new_led: No such device or address
/etc/init.d/rc.S: line 1355: cannot create /dev/new_led: No such device or address
/etc/init.d/rc.S: line 1355: cannot create /dev/new_led: No such device or address
kdsldmod: init start (Dec 19 2008 15:18:06) sizeof(struct sk_buff)=168
<6>kdsld: ttychannel: ldisc 8 registered
kdsldmod: init done
Jan  1 01:00:46 ctlmgr[388]: process priority is 19
Jan  1 01:00:46 ctlmgr[390]: [main.c:1317] **** cwd -> {/}
Jan  1 01:00:46 ctlmgr[390]: FactoryDefault=/etc/default/tcom/user.cfg (user)
Jan  1 01:00:46 ctlmgr[390]: load_config(user): factory default loaded
Jan  1 01:00:46 ctlmgr[390]: FactoryDefault=/etc/default/tcom/voip.cfg (voip)
Jan  1 01:00:47 ctlmgr[390]: load_config(voip): factory default loaded
[avm_vinax] state request received.

[avm_vinax] event.  < Size: 20 | Status: 1 | DS: 0 | US: 0 | dsl mode: ADSL>

Jan  1 01:00:47 ctlmgr[390]: internal vcc:
Jan  1 01:00:47 ctlmgr[390]:   name=mstv vpi=1 vci=32 encap=4 sep_config=1 vcc=0x2aab5880
Jan  1 01:00:47 ctlmgr[390]:   name=internet vpi=1 vci=32 encap=1 sep_config=0 vcc=0x2aab5880
[avm_power] : ethernet port 0 status 2
[avm_power] : ethernet port 1 status 1
[avm_power] : ethernet port 2 status 1
[avm_power] : ethernet port 3 status 1
Jan  1 01:00:47 ctlmgr[390]: mapping to info-LED already exist
Jan  1 01:00:47 ctlmgr[390]: box init ok
Jan  1 01:00:47 ctlmgr[390]: ipmasqfwruleex_parse ret=0 'tcp 0.0.0.0:7547 0.0.0.0:7547'
Jan  1 01:00:48 ctlmgr[390]: forwardrules: internal rule
Jan  1 01:00:48 ctlmgr[390]: ipmasqfwruleex_parse ret=0 'udp 0.0.0.0:5060 0.0.0.0:5060'
Jan  1 01:00:48 ctlmgr[390]: forwardrules: internal rule
Jan  1 01:00:48 ctlmgr[390]: ipmasqfwruleex_parse ret=0 'tcp 0.0.0.0:5060 0.0.0.0:5060'
Jan  1 01:00:48 ctlmgr[390]: forwardrules: internal rule
Jan  1 01:00:48 ctlmgr[390]: ipmasqfwruleex_parse ret=0 'udp 0.0.0.0:7078+32 0.0.0.0:7078'
Jan  1 01:00:48 ctlmgr[390]: forwardrules: internal rule
Jan  1 01:00:48 ctlmgr[390]: sipextra my_init
/etc/init.d/rc.wlan: line 1231: cannot create /dev/new_led: No such device or address
/etc/init.d/rc.wlan: line 1308: cannot create /dev/new_led: No such device or address
ath_hal: 0.9.14.25 (AR5416, DEBUG, REGOPS_FUNC)
ath_dfs: Version 2.0.0
Copyright (c) 2005-2006 Atheros Communications, Inc. All Rights Reserved
wlan: 0.8.4.2 (Atheros/multi-bss)
Registered for AVM event source.
ath_rate_atheros: Version 2.0.1
Copyright (c) 2001-2004 Atheros Communications, Inc, All Rights Reserved
Jan  1 01:00:49 ctlmgr[390]: /dev/avm_power <-- MODE=vdsl
Jan  1 01:00:49 ctlmgr[390]: TR-069 is activated in tr069.cfg
ath_pci: 0.9.4.5 (Atheros/multi-bss)
ath_pci: CR-LSDK-1.3.1.52
cache line size: 16
ar5416AttachHwPlatform: AR_EMU is set
in ar5416HwAttach
in ar5416ChipTest
avmEEPROM: Reading calibration data
avmEEPROM: Got calibration data version: 2
avmEEPROM: Using MAC address: 00:1F:3F:xxxxxxx
avmEEPROM: offset=0x200, length=0xCB8(65C), setting checksum to: 7F02
avmEEPROM: Using patched eeprom for OWL at offset 256.
avmEEPROM: EEPROM content copied to driver
avmEEPROM: antCtrlCommon, 2 GHz: 0x1120, 5 GHz: 0x1120
No MBSSID aggregation supportChan  Freq  RegPwr  HT   CTL CTL_U CTL_L DFS
   1  2412n     20  HT20  1    0    1     N
   1  2412n     20  HT40  1    0    1     N
   2  2417n     20  HT40  1    0    1     N
   3  2422n     20  HT40  1    1    1     N
   4  2427n     20  HT40  1    1    1     N
   5  2432n     20  HT40  1    1    1     N
   6  2437n     20  HT40  1    1    1     N
   7  2442n     20  HT40  1    1    1     N
   8  2447n     20  HT40  1    1    1     N
   9  2452n     20  HT40  1    1    1     N
  10  2457n     20  HT40  1    1    1     N
  11  2462n     20  HT40  1    1    1     N
  12  2467n     20  HT40  1    1    0     N
  13  2472n     20  HT40  1    1    0     N
  36  5180n     30  HT20  1    0    1     N
  38  5190n     20  HT40  1    0    0     N
  40  5200n     30  HT20  1    1    0     N
  44  5220n     30  HT20  1    0    1     N
  46  5230n     20  HT40  1    0    0     N
  48  5240n     30  HT20  1    1    0     N
  52  5260n     20  HT20  1    0    1     Y
  54  5270n     20  HT40  1    0    0     Y
  56  5280n     20  HT20  1    1    0     Y
  60  5300n     20  HT20  1    0    1     Y
  62  5310n     20  HT40  1    0    0     Y
  64  5320n     20  HT20  1    1    0     Y
 100  5500n     27  HT20  1    0    1     Y
 102  5510n     27  HT40  1    0    0     Y
 104  5520n     27  HT20  1    1    0     Y
 108  5540n     27  HT20  1    0    1     Y
 110  5550n     27  HT40  1    0    0     Y
 112  5560n     27  HT20  1    1    0     Y
 116  5580n     27  HT20  1    0    1     Y
 118  5590n     27  HT40  1    0    0     Y
 120  5600n     27  HT20  1    1    0     Y
 124  5620n     27  HT20  1    0    1     Y
 126  5630n     27  HT40  1    0    0     Y
 128  5640n     27  HT20  1    1    0     Y
 132  5660n     27  HT20  1    0    1     Y
 134  5670n     27  HT40  1    0    0     Y
 136  5680n     27  HT20  1    1    0     Y
 140  5700n     27  HT20  1    0    0     Y
dfs_init_radar_filters: dfs->dfs_rinfo.rn_numradars: 0
DFS min filter rssiThresh = 21
DFS max pulse dur = 131 ticks
wifi0: 11na rates: 6Mbps 9Mbps 12Mbps 18Mbps 24Mbps 36Mbps 48Mbps 54Mbps
wifi0: 11na MCS:  0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15
wifi0: 11ng rates: 1Mbps 2Mbps 5.5Mbps 11Mbps 6Mbps 9Mbps 12Mbps 18Mbps 24Mbps 36Mbps 48Mbps 54Mbps
wifi0: 11ng MCS:  0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15
wifi0: mac 13.2 phy 8.1 radio 12.0
wifi0: Use hw queue 1 for WME_AC_BE traffic
wifi0: Use hw queue 0 for WME_AC_BK traffic
wifi0: Use hw queue 2 for WME_AC_VI traffic
wifi0: Use hw queue 3 for WME_AC_VO traffic
wifi0: Use hw queue 8 for CAB traffic
wifi0: Use hw queue 9 for beacons
wifi0: Use hw queue 7 for UAPSD
wifi0: Atheros 9280: mem=0x40000000, irq=80 hw_base=0xC03E0000
wlan: mac acl policy registered
Jan  1 01:00:50 ctlmgr[390]: TR069_Full_Init
Jan  1 01:00:50 ctlmgr[390]: TR069_Init returned 0
Jan  1 01:00:50 ctlmgr[390]: TR069_Init(full) returned 0
Jan  1 01:00:50 ctlmgr[390]: TR064 RegisterServices (InternetGatewayDevice) OK
Jan  1 01:00:50 ctlmgr[390]: TR064 RegisterServices (DeviceInfo) OK
Jan  1 01:00:50 ctlmgr[390]: TR064 RegisterServices (Layer3Forwarding) OK
Jan  1 01:00:50 ctlmgr[390]: TR064 RegisterServices (LANConfigSecurity) OK
Jan  1 01:00:50 ctlmgr[390]: TR064 RegisterServices (Time) OK
Jan  1 01:00:50 ctlmgr[390]: TR064 RegisterServices (ManagementServer) OK
Jan  1 01:00:50 ctlmgr[390]: TR064 RegisterServices (UserInterface) OK
Jan  1 01:00:50 ctlmgr[390]: TR064 RegisterServices (LANHostConfigManagement) OK
Jan  1 01:00:50 ctlmgr[390]: TR064 RegisterServices (WANCommonInterfaceConfig) OK
Jan  1 01:00:50 ctlmgr[390]: TR064 RegisterServices (WANDSLInterfaceConfig) OK
Jan  1 01:00:50 ctlmgr[390]: TR064 RegisterServices (WANDSLLinkConfig) OK
Jan  1 01:00:50 ctlmgr[390]: TR064 RegisterServices (WANPPPConnection) OK
Jan  1 01:00:50 ctlmgr[390]: TR064 RegisterServices (PortMapping) OK
Jan  1 01:00:50 ctlmgr[390]: TR064 RegisterServices (WLANConfiguration) OK
Jan  1 01:00:50 ctlmgr[390]: TR064 RegisterServices (X_VoIP) OK
Jan  1 01:00:50 ctlmgr[390]: TR064 RegisterServices (X_AVM-DE_Storage) OK
Jan  1 01:00:50 ctlmgr[390]: TR064_Init 0
Jan  1 01:00:50 ctlmgr[390]: [../webserver/webserver.c:624] Initialisation of webserver configuration
Jan  1 01:00:50 ctlmgr[390]: https access enabled
libwlanparam: config ok(1)
Invalid command : fmini_sns_on
Invalid command : fmini_mac
Reading topology file /var/tmp/hostapd_topology.conf ...
Reading radio configuration file /var/tmp/hostapd_ap.conf ...
Reading bss configuration file /var/tmp/hostapd_bss.conf ...
libwlanparam: config ok(1)
Using WPA/WPA2 passphrase from flash.
/etc/init.d/rc.wlan: line 1308: cannot create /dev/new_led: No such device or address
/etc/init.d/rc.wlan: line 1310: cannot create /dev/new_led: No such device or address
/etc/init.d/rc.net: line 385: websrv: not found
 key_alloc_2pair XX: sc_splitmic SET to 1
ar5416AttachHwPlatform: AR_EMU is set
ar5416SetPowerPerRateTable() syn 2412 ctl 2412 ext 2412 is40 0
  6mb OFDM  11.5 dBm |  9mb OFDM  11.5 dBm | 12mb OFDM  11.5 dBm | 18mb OFDM  11.5 dBm
 24mb OFDM  11.5 dBm | 36mb OFDM  11.5 dBm | 48mb OFDM  11.5 dBm | 54mb OFDM  11.5 dBm
 1L   CCK   11.5 dBm | 2L   CCK   11.5 dBm | 2S   CCK   11.5 dBm | 5.5L CCK   11.5 dBm
 5.5S CCK   11.5 dBm | 11L  CCK   11.5 dBm | 11S  CCK   11.5 dBm | XR         11.5 dBm
 HT20mcs 0  11.5 dBm | HT20mcs 1  11.5 dBm | HT20mcs 2  11.5 dBm | HT20mcs 3  11.5 dBm
 HT20mcs 4  11.5 dBm | HT20mcs 5  11.5 dBm | HT20mcs 6  11.0 dBm | HT20mcs 7  11.0 dBm
 HT40mcs 0   0.0 dBm | HT40mcs 1   0.0 dBm | HT40mcs 2   0.0 dBm | HT40mcs 3   0.0 dBm
 HT40mcs 4   0.0 dBm | HT40mcs 5   0.0 dBm | HT40mcs 6   0.0 dBm | HT40mcs 7   0.0 dBm
 Dup CCK     0.0 dBm | Dup OFDM    0.0 dBm | Ext CCK     0.0 dBm | Ext OFDM    0.0 dBm
2xAntennaReduction: 0, 2xMaxRegulatory: 40, 2xPowerLimit: 63
2xMaxPowerLevel: 23 (HT20)
Force rf_pwd_icsyndiv to 1 on 2412 (1 0)
ar5416SetDma: AR_AHB_MODE=1f
;ar5416SetPowerPerRateTable() syn 2412 ctl 2412 ext 2412 is40 0
  6mb OFDM  10.0 dBm |  9mb OFDM  10.0 dBm | 12mb OFDM  10.0 dBm | 18mb OFDM  10.0 dBm
 24mb OFDM  10.0 dBm | 36mb OFDM  10.0 dBm | 48mb OFDM  10.0 dBm | 54mb OFDM  10.0 dBm
 1L   CCK   10.0 dBm | 2L   CCK   10.0 dBm | 2S   CCK   10.0 dBm | 5.5L CCK   10.0 dBm
 5.5S CCK   10.0 dBm | 11L  CCK   10.0 dBm | 11S  CCK   10.0 dBm | XR         10.0 dBm
 HT20mcs 0  10.0 dBm | HT20mcs 1  10.0 dBm | HT20mcs 2  10.0 dBm | HT20mcs 3  10.0 dBm
 HT20mcs 4  10.0 dBm | HT20mcs 5  10.0 dBm | HT20mcs 6  10.0 dBm | HT20mcs 7  10.0 dBm
 HT40mcs 0   0.0 dBm | HT40mcs 1   0.0 dBm | HT40mcs 2   0.0 dBm | HT40mcs 3   0.0 dBm
 HT40mcs 4   0.0 dBm | HT40mcs 5   0.0 dBm | HT40mcs 6   0.0 dBm | HT40mcs 7   0.0 dBm
 Dup CCK     0.0 dBm | Dup OFDM    0.0 dBm | Ext CCK     0.0 dBm | Ext OFDM    0.0 dBm
2xAntennaReduction: 0, 2xMaxRegulatory: 40, 2xPowerLimit: 63
2xMaxPowerLevel: 20 (HT20)
ath_newstate: Resetting VAP dfswait_run
ar5416AttachHwPlatform: AR_EMU is set
ar5416SetPowerPerRateTable() syn 2412 ctl 2412 ext 2412 is40 0
  6mb OFDM  11.5 dBm |  9mb OFDM  11.5 dBm | 12mb OFDM  11.5 dBm | 18mb OFDM  11.5 dBm
 24mb OFDM  11.5 dBm | 36mb OFDM  11.5 dBm | 48mb OFDM  11.5 dBm | 54mb OFDM  11.5 dBm
 1L   CCK   11.5 dBm | 2L   CCK   11.5 dBm | 2S   CCK   11.5 dBm | 5.5L CCK   11.5 dBm
 5.5S CCK   11.5 dBm | 11L  CCK   11.5 dBm | 11S  CCK   11.5 dBm | XR         11.5 dBm
 HT20mcs 0  11.5 dBm | HT20mcs 1  11.5 dBm | HT20mcs 2  11.5 dBm | HT20mcs 3  11.5 dBm
 HT20mcs 4  11.5 dBm | HT20mcs 5  11.5 dBm | HT20mcs 6  11.0 dBm | HT20mcs 7  11.0 dBm
 HT40mcs 0   0.0 dBm | HT40mcs 1   0.0 dBm | HT40mcs 2   0.0 dBm | HT40mcs 3   0.0 dBm
 HT40mcs 4   0.0 dBm | HT40mcs 5   0.0 dBm | HT40mcs 6   0.0 dBm | HT40mcs 7   0.0 dBm
 Dup CCK     0.0 dBm | Dup OFDM    0.0 dBm | Ext CCK     0.0 dBm | Ext OFDM    0.0 dBm
2xAntennaReduction: 0, 2xMaxRegulatory: 40, 2xPowerLimit: 63
2xMaxPowerLevel: 23 (HT20)
Force rf_pwd_icsyndiv to 1 on 2412 (1 0)
ar5416SetDma: AR_AHB_MODE=1f
;ath_chan_set: Changing to channel 2412, Flags 30080, PF 0
Jan  1 01:00:52 ctlmgr[390]: symbol TI_Interpreter_LookupDBField not found
Jan  1 01:00:52 ctlmgr[390]: startup (Dec 19 2008 15:18:48)
Jan  1 01:00:52 ctlmgr[390]: [main.c:1673] *** WEBSERVER started successfully
Jan  1 01:00:52 ctlmgr[390]: verbose: DISABLED
Jan  1 01:00:52 ctlmgr[390]: dlsym(/usr/share/ctlmgr/libvdsl.so,vdsl_poll) failed
Jan  1 01:00:53 multid[636]: startup ($Revision: 1.170 $$CompileDate: Dec 19 2008 15:17:10 $)
Jan  1 01:00:53 multid[638]: new cpmac driver detected
Jan  1 01:00:53 multid[638]: VDSL detected
Jan  1 01:00:53 multid[638]: voip: disabled, not in first vcc
Jan  1 01:00:53 multid[638]: enabling VDSL-Mode
Jan  1 01:00:53 multid[638]: normal 7,8
[cpmac] [set_map_in] Port 0 already set to device 1 instead of 0.
[cpmac] [set_map_in] Port 1 already set to device 1 instead of 0.
[cpmac] [set_map_in] Port 2 already set to device 1 instead of 0.
[cpmac] [set_map_in] Port 3 already set to device 1 instead of 0.
[cpmac] cpmac_main_ioctl, unknown ioctl 35142
device cpmac0 entered promiscuous mode
device eth0 entered promiscuous mode
device ath0 entered promiscuous mode
Jan  1 01:00:53 multid[638]: mrouter: using IGMPv3 for upstream interface dsl
Jan  1 01:00:53 multid[638]: mrouter: using IGMPv3 for other interfaces
[cpmac] cpmac_main_ioctl, unknown ioctl 35142
lan: port 1(eth0) entering learning state
lan: port 2(ath0) entering learning state
Jan  1 01:00:53 dsld[640]: startup (Dec 19 2008 15:17:21)
Jan  1 01:00:53 dsld[640]: voip: disabled, not in vccs
lan: topology change detected, propagating
lan: port 1(eth0) entering forwarding state
lan: topology change detected, propagating
lan: port 2(ath0) entering forwarding state
Jan  1 01:00:53 dsld[640]: new cpmac driver detected
Jan  1 01:00:53 dsld[640]: VDSL detected
device wan entered promiscuous mode
Jan  1 01:00:53 multid[638]: DHCPD on lan
Jan  1 01:00:53 multid[638]: dhcpd: can't open /var/flash/multid.leases - No such file or directory (2)
Jan  1 01:00:53 multid[638]: DDNS: no valid accounts
Jan  1 01:00:53 multid[638]: interface wan new.
Jan  1 01:00:53 multid[638]: interface eth0 new.
Jan  1 01:00:53 multid[638]: interface lan new.
Jan  1 01:00:53 multid[638]: DHCPD on lan
Jan  1 01:00:53 multid[638]: interface cpmac0 new.
Jan  1 01:00:53 multid[638]: interface cpmac0 up.
Jan  1 01:00:53 multid[638]: interface lo new.
Jan  1 01:00:53 multid[638]: interface lo up.
Jan  1 01:00:53 multid[638]: mrouter: lo: no multicast interface, ignored.
Jan  1 01:00:53 multid[638]: interface wifi0 new.
Jan  1 01:00:53 multid[638]: interface wifi0 up.
Jan  1 01:00:53 dsld[648]: DSL Mac 00:1f:3f:xxxxxxx
Jan  1 01:00:53 dsld[648]: VOIP Mac 00:1f:3f:xxxxxxx
Jan  1 01:00:53 dsld[648]: VCC2 Mac 00:1f:3f:xxxxxxx
Jan  1 01:00:53 dsld[648]: VCC3 Mac 00:1f:3f:xxxxxxx
Jan  1 01:00:53 dsld[648]: kdsld_qos_add_devport_vlanid: port=1, vlanid=772
Jan  1 01:00:53 dsld[648]: kdsld_qos_add_devport_vlanid: port=2, vlanid=1284
Jan  1 01:00:53 dsld[648]: kdsld_qos_add_devport_vlanid: port=3, vlanid=1796
Jan  1 01:00:53 dsld[648]: kdsld_qos_add_devport_vlanid: port=4, vlanid=2308
Jan  1 01:00:53 dsld[648]: get_queueindex: none: not found
Jan  1 01:00:53 dsld[648]: get_queueindex: none: not found
Jan  1 01:00:53 dsld[648]: classifer: lan "ip.proto == tcp ip.len <= 64" disabled
Jan  1 01:00:53 dsld[648]: classifer: lan "tcp.dest 80,3128,8080 ip.len <= 800" disabled
Jan  1 01:00:53 dsld[648]: queue 0: prio 0 weight 0 shrate 0 shburst 0 wan
Jan  1 01:00:53 dsld[648]: queue 1: prio 10 weight 0 shrate 0 shburst 0 wan
Jan  1 01:00:53 dsld[648]: queue 2: prio 20 weight 0 shrate 0 shburst 0 wan
Jan  1 01:00:53 dsld[648]: queue 3: prio 30 weight 0 shrate 0 shburst 0 wan
Jan  1 01:00:53 dsld[648]: queue 4: prio 100 weight 90 shrate 0 shburst 0 wan
Jan  1 01:00:53 dsld[648]: queue 5: prio 100 weight 10 shrate 0 shburst 0 wan
Jan  1 01:00:53 dsld[648]: queue 6: prio 200 weight 0 shrate 0 shburst 0 wan
Jan  1 01:00:53 dsld[648]: appl 0: sip-appl result 1
Jan  1 01:00:53 dsld[648]: classifer: local "localmark none ip.proto == igmp" result 2
Jan  1 01:00:53 dsld[648]: classifer: local "localmark sipdns,ntpdns,tr069dns,tr069" result 3
Jan  1 01:00:53 dsld[648]: classifer: lan "udp.dport 43962" result 4
Jan  1 01:00:53 dsld[648]: classifer: lan "udp.dport 47806" result 4
Jan  1 01:00:53 dsld[648]: classifer: lan "ip.proto icmp" result 3
Jan  1 01:00:53 dsld[648]: classifer: lan "udp.dport 53" result 3
Jan  1 01:00:53 dsld[648]: classifer: local "localmark sip" result 1
Jan  1 01:00:53 dsld[648]: classifer: local "localmark rtp" result 1
Jan  1 01:00:53 dsld[648]: classifer: lan "udp.dport 5060" result 5
Jan  1 01:00:53 dsld[648]: result 0: tos 0 vprio 65535 queue 5 appl 65535 bridge 65535 forward 65535
Jan  1 01:00:53 dsld[648]: result 1: tos 192 vprio 65535 queue 2 appl 65535 bridge 65535 forward 65535
Jan  1 01:00:53 dsld[648]: result 2: tos 128 vprio 65535 queue 0 appl 65535 bridge 65535 forward 65535
Jan  1 01:00:53 dsld[648]: result 3: tos 65535 vprio 65535 queue 1 appl 65535 bridge 65535 forward 65535
Jan  1 01:00:53 dsld[648]: result 4: tos 96 vprio 65535 queue 1 appl 65535 bridge 65535 forward 65535
Jan  1 01:00:53 dsld[648]: result 5: tos 192 vprio 65535 queue 2 appl 0 bridge 65535 forward 65535
<6>kdsld: mac whitelist disabled
<6>kdsld: lan-cfg:
<6>kdsld:  0: eth.proto 0x0800 ip.proto 17 udp.dport 43962 (ri 4)
<6>kdsld:  0: eth.proto 0x0800 ip.proto 17 udp.dport 47806 (ri 4)
<6>kdsld:  0: eth.proto 0x0800 ip.proto 1 (ri 3)
<6>kdsld:  0: eth.proto 0x0800 ip.proto 17 udp.dport 53 (ri 3)
<6>kdsld:  0: eth.proto 0x0800 ip.proto 17 udp.dport 5060 (ri 5)
<6>kdsld: lan:
<6>kdsld:  0: eth.proto 0x0800 (ri 4)
<6>kdsld:  1:    ip.proto 17 (ri 4)
<6>kdsld:  2:       udp.dport 43962 (ri 4)
<6>kdsld:  2:       udp.dport 47806 (ri 4)
<6>kdsld:  1:    ip.proto 1 (ri 3)
<6>kdsld:  1:    ip.proto 17 (ri 3)
<6>kdsld:  2:       udp.dport 53 (ri 3)
<6>kdsld:  2:       udp.dport 5060 (ri 5)
<6>kdsld: local-cfg:
<6>kdsld:  0: localmark none ip.proto 2 (ri 2)
<6>kdsld:  0: localmark sipdns,ntpdns,tr069dns,tr069 (ri 3)
<6>kdsld:  0: localmark sip (ri 1)
<6>kdsld:  0: localmark rtp (ri 1)
<6>kdsld: local:
<6>kdsld:  0: localmark none ip.proto 2 (ri 2)
<6>kdsld:  0: localmark sipdns,ntpdns,tr069dns,tr069 (ri 3)
<6>kdsld:  0: localmark sip (ri 1)
<6>kdsld:  0: localmark rtp (ri 1)
<6>kdsld: wan-cfg:
<6>kdsld: wan:
<6>kdsld: early-cfg:
<6>kdsld: early:
Force rf_pwd_icsyndiv to 1 on 2417 (1 0)
ar5416SetPowerPerRateTable() syn 2417 ctl 2417 ext 2417 is40 0
  6mb OFDM  11.5 dBm |  9mb OFDM  11.5 dBm | 12mb OFDM  11.5 dBm | 18mb OFDM  11.5 dBm
 24mb OFDM  11.5 dBm | 36mb OFDM  11.5 dBm | 48mb OFDM  11.5 dBm | 54mb OFDM  11.5 dBm
 1L   CCK   11.5 dBm | 2L   CCK   11.5 dBm | 2S   CCK   11.5 dBm | 5.5L CCK   11.5 dBm
 5.5S CCK   11.5 dBm | 11L  CCK   11.5 dBm | 11S  CCK   11.5 dBm | XR         11.5 dBm
 HT20mcs 0  11.5 dBm | HT20mcs 1  11.5 dBm | HT20mcs 2  11.5 dBm | HT20mcs 3  11.5 dBm
 HT20mcs 4  11.5 dBm | HT20mcs 5  11.5 dBm | HT20mcs 6  11.0 dBm | HT20mcs 7  11.0 dBm
 HT40mcs 0   0.0 dBm | HT40mcs 1   0.0 dBm | HT40mcs 2   0.0 dBm | HT40mcs 3   0.0 dBm
 HT40mcs 4   0.0 dBm | HT40mcs 5   0.0 dBm | HT40mcs 6   0.0 dBm | HT40mcs 7   0.0 dBm
 Dup CCK     0.0 dBm | Dup OFDM    0.0 dBm | Ext CCK     0.0 dBm | Ext OFDM    0.0 dBm
2xAntennaReduction: 0, 2xMaxRegulatory: 40, 2xPowerLimit: 63
2xMaxPowerLevel: 23 (HT20)
ath_chan_set: Changing to channel 2417, Flags 30082, PF 0
Jan  1 01:00:53 dsld[648]: PPP led: off (value=0)
[avm_vinax] state request received.
Jan  1 01:00:53 multid[638]: interface ath0 new.
Jan  1 01:00:54 multid[638]: interface ath0 up.
Jan  1 01:00:54 multid[638]: interface wan new.
Jan  1 01:00:54 multid[638]: interface eth0 new.
Jan  1 01:00:54 multid[638]: interface lan new.
Jan  1 01:00:54 multid[638]: DHCPD on lan
Jan  1 01:00:54 multid[638]: CONFIG_LOGD disabled: No UPnP-Device for avmlogd
Jan  1 01:00:54 multid[638]: verbose: DISABLED
mcfw: group 0.0.0.0: query cpmac:0,1,2,3 10sec

[avm_vinax] event.  < Size: 20 | Status: 1 | DS: 0 | US: 0 | dsl mode: ADSL>

[avm_vinax] state request received.
Jan  1 01:00:54 telefon[650]: use clock_gettime(CLOCK_MONOTONIC)!

[avm_vinax] event.  < Size: 20 | Status: 1 | DS: 0 | US: 0 | dsl mode: ADSL>

Jan  1 01:00:55 dsld[648]: verbose: DISABLED
<6>kdsld: sync lost
Jan  1 01:00:55 telefon[650]: SIGCHLD received!
Jan  1 01:00:55 telefon[650]: WARNING No config file '/var/flash/fx_def' !
Jan  1 01:00:55 telefon[650]: WARNING No CG file '/var/flash/fx_cg' !
Jan  1 01:00:55 voipd[658]: FactoryDefault=/etc/default/tcom/voip.cfg (voip)
Jan  1 01:00:55 voipd[658]: load_config(voip): factory default loaded
Jan  1 01:00:55 voipd[658]: startup (AVM Speedport W 920V 65.04.70 AVM SIP v9.04.323 Dec 19 2008 15:18:09)
Jan  1 01:00:55 voipd[658]: using capi controller 5
Jan  1 01:00:55 voipd[658]: using b1 protocol 10 for 8kHz
Jan  1 01:00:55 voipd[658]: using b1 protocol 11 for 16kHz
Jan  1 01:00:55 voipd[658]: tel: NOT supported
Jan  1 01:00:55 voipd[658]: ENUM NOT supported
Jan  1 01:00:55 voipd[658]: VoIP led value = 0
Jan  1 01:00:55 voipd[658]: no useragent configured
Jan  1 01:00:55 voipd[658]: INFO led: off (value=0)
Jan  1 01:00:55 voipd[658]: VoIP SRTP led value = 0
Jan  1 01:00:55 voipd[658]: priority is -20
Jan  1 01:00:55 voipd[658]: encaplen 32
Jan  1 01:00:55 voipd[658]: brutto speed unknown
Jan  1 01:00:55 voipd[658]: connstatus 0 -> 1
Jan  1 01:00:55 voipd[658]: PCMA/8000/1: 98933 bits/second (encaplen=32,30ms)
Jan  1 01:00:55 voipd[658]: PCMU/8000/1: 98933 bits/second (encaplen=32,30ms)
Jan  1 01:00:55 voipd[658]: G726-32/8000/1: 70666 bits/second (encaplen=32,30ms)
Jan  1 01:00:55 voipd[658]: G726-40/8000/1: 70666 bits/second (encaplen=32,30ms)
Jan  1 01:00:55 voipd[658]: G726-24/8000/1: 56533 bits/second (encaplen=32,30ms)
Jan  1 01:00:55 voipd[658]: PCMA/16000/1: 197866 bits/second (encaplen=32,30ms)
Jan  1 01:00:55 voipd[658]: PCMU/16000/1: 197866 bits/second (encaplen=32,30ms)
Jan  1 01:00:55 voipd[658]: CLEARMODE/8000/1: 98933 bits/second (encaplen=32,30ms)
Jan  1 01:00:55 voipd[658]: G722/8000/1: 98933 bits/second (encaplen=32,30ms)
Jan  1 01:00:55 voipd[658]: PCMA/8000/1: 106000 bits/second (encaplen=32,20ms)
Jan  1 01:00:55 voipd[658]: PCMU/8000/1: 106000 bits/second (encaplen=32,20ms)
Jan  1 01:00:55 voipd[658]: G726-32/8000/1: 84800 bits/second (encaplen=32,20ms)
Jan  1 01:00:55 voipd[658]: G726-40/8000/1: 84800 bits/second (encaplen=32,20ms)
Jan  1 01:00:55 voipd[658]: G726-24/8000/1: 63600 bits/second (encaplen=32,20ms)
Jan  1 01:00:55 voipd[658]: PCMA/16000/1: 212000 bits/second (encaplen=32,20ms)
Jan  1 01:00:55 voipd[658]: PCMU/16000/1: 212000 bits/second (encaplen=32,20ms)
Jan  1 01:00:55 voipd[658]: CLEARMODE/8000/1: 106000 bits/second (encaplen=32,20ms)
Jan  1 01:00:55 voipd[658]: G722/8000/1: 106000 bits/second (encaplen=32,20ms)
Jan  1 01:00:55 voipd[658]: verbose: DISABLED
create sema UPNPAPI_DATA_phonebook
Jan  1 01:00:56 telefon[654]: SIGCHLD received!
Force rf_pwd_icsyndiv to 2 on 2422 (1 0)
ar5416SetPowerPerRateTable() syn 2422 ctl 2422 ext 2422 is40 0
  6mb OFDM  11.5 dBm |  9mb OFDM  11.5 dBm | 12mb OFDM  11.5 dBm | 18mb OFDM  11.5 dBm
 24mb OFDM  11.5 dBm | 36mb OFDM  11.5 dBm | 48mb OFDM  11.5 dBm | 54mb OFDM  11.5 dBm
 1L   CCK   11.5 dBm | 2L   CCK   11.5 dBm | 2S   CCK   11.5 dBm | 5.5L CCK   11.5 dBm
 5.5S CCK   11.5 dBm | 11L  CCK   11.5 dBm | 11S  CCK   11.5 dBm | XR         11.5 dBm
 HT20mcs 0  11.5 dBm | HT20mcs 1  11.5 dBm | HT20mcs 2  11.5 dBm | HT20mcs 3  11.5 dBm
 HT20mcs 4  11.5 dBm | HT20mcs 5  11.5 dBm | HT20mcs 6  11.0 dBm | HT20mcs 7  11.0 dBm
 HT40mcs 0   0.0 dBm | HT40mcs 1   0.0 dBm | HT40mcs 2   0.0 dBm | HT40mcs 3   0.0 dBm
 HT40mcs 4   0.0 dBm | HT40mcs 5   0.0 dBm | HT40mcs 6   0.0 dBm | HT40mcs 7   0.0 dBm
 Dup CCK     0.0 dBm | Dup OFDM    0.0 dBm | Ext CCK     0.0 dBm | Ext OFDM    0.0 dBm
2xAntennaReduction: 0, 2xMaxRegulatory: 40, 2xPowerLimit: 63
2xMaxPowerLevel: 23 (HT20)
ath_chan_set: Changing to channel 2422, Flags 30082, PF 0
run_clock demon started

AVM_WATCHDOG: System Init UEberwachung abgeschlossen (186270 ms noch verfuegbar)
[avm_power] pm_ressourceinfo_scriptparse: powerdevice_cpuclock: norm_power_rate=100 act_rate=100 mul=0 div=1 offset=0 NormP=0 mW -> SumNormP=0 mW
[avm_power] pm_ressourceinfo_scriptparse: powerdevice_dspclock: norm_power_rate=100 act_rate=100 mul=0 div=1 offs
Please press Enter to activate this console. [4294942966][DCTDRV] (FP_MAC_START_STOP_REQ) UI_TASK->FP_CCF_TASK  
cat: read error: Broken pipe
Jan  1 01:01:02 igdd[617]: OemStringData.MAC:001F3Fxxxxxxx
Jan  1 01:01:02 igdd[617]: get_wlan_ssid=WLAN-001F3Fxxxxxxx
Jan  1 01:01:02 igdd[617]: OemStringData.BOXID='WLAN-001F3Fxxxxxx', _boxenv_name_and_version='AVM Speedport W 920V 65.04.70'
Jan  1 01:01:02 igdd[617]: desc=WLAN-001F3Fxxxxxxx UPnP/1.0 AVM Speedport W 920V 65.04.70
Jan  1 01:01:02 igdd[617]: startup (Dec 19 2008 15:17:08)
Jan  1 01:01:02 igdd[617]: verbose: DISABLED
DSL: ++++++++++++++++ loading ADSL FW ++++++++++++++++++++
DSL: ++++++++++++++++ loading ADSL FW ++++++++++++++++++++
file path is /lib/modules/vinax_fw_adsl.bin
fw   size is 0
DSL: loading firmware binary /lib/modules/vinax_fw_adsl.bin
DSL: firmware binary size 540916 bytes
DSL[00]: Device Start EVT - UsrRst, DrvState 1 --> 1
DSL[00]: Line in reset - block!
DSL[00]: VINAX line recovered.
sCommand=DSL_CBS_LINE_STATE nLine=00 nLineState=00000100 
dsl_daemon: new modem state 256 
sCommand=DSL_CBS_LINE_STATE nLine=00 nLineState=00000200 
dsl_daemon: new modem state 512 
DSL: ++++++++++++++++ loading ADSL FW ++++++++++++++++++++
DSL: ++++++++++++++++ loading ADSL FW ++++++++++++++++++++
file path is /lib/modules/vinax_fw_adsl.bin
fw   size is 0
DSL: loading firmware binary /lib/modules/vinax_fw_adsl.bin
DSL: firmware binary size 540916 bytes
DSL[00]: Device Start EVT - UsrRst, DrvState 1 --> 1
DSL[00]: Line in reset - block!
DSL[00]: VINAX line recovered.
sCommand=DSL_CBS_LINE_STATE nLine=00 nLineState=00000100 
dsl_daemon: new modem state 256 
sCommand=DSL_CBS_LINE_STATE nLine=00 nLineState=00000200 
dsl_daemon: new modem state 512 

starting pid 684, tty '/dev/console': '/bin/sh'


BusyBox v1.8.2 (2008-11-19 12:13:49 CET) built-in shell (ash)
Enter 'help' for a list of built-in commands.

ermittle die aktuelle TTY
tty is "/dev/console"
Serielles Terminal


# free
              total         used         free       shared      buffers
  Mem:        61300        39264        22036            0         4620
 Swap:            0            0            0
Total:        61300        39264        22036
 

# busybox 
BusyBox v1.8.2 (2008-11-19 12:13:49 CET) multi-call binary
Copyright (C) 1998-2006 Erik Andersen, Rob Landley, and others.
Licensed under GPLv2. See source distribution for full notice.

Usage: busybox [function] [arguments]...
   or: [function] [arguments]...

	BusyBox is a multi-call binary that combines many common Unix
	utilities into a single executable.  Most people will create a
	link to busybox for each function they wish to use and BusyBox
	will act like whatever it was invoked as!

Currently defined functions:
	[, [[, ash, basename, cat, chmod, clear, cp, date, dd,
	dmesg, echo, egrep, env, false, fgrep, find, free, grep,
	halt, head, hostname, ifconfig, ifdown, ifup, inetd, init,
	insmod, kill, killall, ln, login, ls, lsmod, md5sum, mkdir,
	mknod, modprobe, more, mount, mv, nc, netstat, nohup,
	pidof, ping, poweroff, ps, pwd, realpath, reboot, rm,
	rmdir, rmmod, route, sed, setconsole, sh, sleep, stty,
	tail, tar, tee, test, tftp, time, touch, tr, traceroute,
	true, tty, umount, uname, uniq, uptime, vconfig, vi, wget


# cat /proc/cpuinfo 
system type		: MIPS UR8
processor		: 0
cpu model		: MIPS 4KEc V6.8
BogoMIPS		: 359.62
wait instruction	: yes
unaligned_instructions 	: 135
microsecond timers	: yes
tlb_entries		: 16
extra interrupt vector	: yes
hardware watchpoint	: no
ASEs implemented	:
VCED exceptions		: not available
VCEI exceptions		: not available


# cat /proc/version 
Linux version 2.6.19.2 (2113) (gcc version 3.4.6) #2 Fri Dec 19 10:34:20 CET 2008


# # cat /proc/interrupts 
           CPU0       
  1:      87262          <NULL>  system timer
  6:     249420          <NULL>  UR8 primary
  7:      87262          <NULL>  timer
  9:       1052          <NULL>  vinax
 15:      81613          <NULL>  serial
 16:         40          <NULL>  UARTB_IRQ
 17:     104314          <NULL>  MCDMA_IRQ
 23:          3          <NULL>  Cpmac Driver Tx
 33:      62397          <NULL>  UR8 Unified PCI
 38:          0          <NULL>  musb_hdrc
 39:          1          <NULL>  musb_hdrc
 40:          0          <NULL>  Cpmac Driver Rx
 80:      62397          <NULL>  wifi0

ERR:          0


# cat /proc/de# cat /proc/devices 
Character devices:
255 avm_net_trace
  1 mem
  2 pty
  3 ttyp
  4 ttyS
  5 /dev/tty
  5 /dev/console
  5 /dev/ptmx
 10 misc
 68 capi_oslib
 90 mtd
128 ptm
136 pts
180 usb
189 usb_device
226 kdsld_traffic
227 dect_io
229 kdsld_user
239 avmEEPROM
240 tffs
241 avm_event
242 watchdog
243 kdsld
244 kdsldptrace
246 debug
247 led
252 avm_power
253 vinax

Block devices:
 31 mtdblock
# # cat /proc/ioports 
10000000-11000000 : physmap-flash.1
  10000000-107fffff : mtd-ram.2
7fff0000-7fffffff : PCI I/O
# # cat /proc/iomem 
10000000-11000000 : physmap-flash.1
14000000-17fbffff : System RAM
  14000000-14205ddf : Kernel code
  14205de0-142a60bf : Kernel data
17fc0000-17ffffff : reserved
1c000000-1c00003f : vinax
40000000-50000000 : PCI Memory
  40000000-4000ffff : 0000:00:0e.0
    40000000-4000ffff : ath
a3400000-a34005ff : musb_hdrc
a8604000-a86040c8 : pcmlink_tdm
a8610f00-a8610f1c : piglet_dectuart(func)


# cat /proc/sys/urlader/e# cat /proc/sys/urlader/environment 
HWRevision	135.1.0.6
ProductID	Fritz_Box_DECT_W920V
SerialNumber	0000000000000000
annex	B
autoload	yes
bootloaderVersion	1.458
bootserport	tty0
cpufrequency	360000000
firstfreeaddress	0x946BD81C
firmware_version	tcom
firmware_info	65.04.70
flashsize	0x01000000
jffs2_size	132
maca	00:1F:3F:xxxxxxxx
macb	00:1F:3F:xxxxxxxx
macwlan	00:1F:3F:xxxxxxxx
macdsl	00:1F:3F:xxxxxxxx
memsize	0x04000000
modetty0	38400,n,8,1,hw
modetty1	38400,n,8,1,hw
mtd0	0x90000000,0x90000000
mtd1	0x90020000,0x90F80000
mtd2	0x90000000,0x90020000
mtd3	0x90F80000,0x90FC0000
mtd4	0x90FC0000,0x91000000
my_ipaddress	192.168.178.1
prompt	Eva_AVM
ptest	
req_fullrate_freq	120000000
sysfrequency	120000000
urlader-version	1458
usb_board_mac	00:xxxxxxxxxxxxxx
usb_rndis_mac	00:xxxxxxxxxxxxxx
usb_device_id	0x0000
usb_revision_id	0x0000
usb_device_name	USB DSL Device
usb_manufacturer_name	AVM
webgui_pass	xxxxxxxx
wlan_key	xxxxxxxxxxxxxxxx


# cat /etc/initt# cat /etc/inittab 
/dev/console::sysinit:/etc/init.d/rc.S
## Start an "askfirst" shell on the console (whatever that may be)
/dev/console::askfirst:-/bin/sh
## Stuff to do before rebooting
/dev/console::shutdown:/bin/sh -c /var/post_install
# 
}}}

CategoryModel ["CategoryAR7Device"]
