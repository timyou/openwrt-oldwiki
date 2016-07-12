== Pirelli Alice Gate 2 plus Wi-Fi ==
This router is rent to his users by Telecom Italia. It's basically a [javascript:void(0);/*1213754106989*/ BCM63xx] device with a smart card reader for IPTV and VoIP.

=== Serial ===
There are six pins (3x2) in the middle of the board. The serial layout is:

{{{
Antennas
+---+---+
|TX | - |
| - | - |
|RX |GND|
+---+---+
LEDs }}}
=== Bootloader ===
The bootloader is CFE, but it seems that when the boot process is interrupted by a keypress, a web server on port 80 is open,

and the main page says:

{{{
Update Software
Step 1: Obtain an updated software image file from your ISP.
Step 2: Enter the path to the image file location in the box below or click the "Browse" button to locate the image file.
Step 3: Click the "Update Software" button once to upload the new image file.
NOTE: The update process takes about 2 minutes to complete, and your DSL Router will reboot.
Software File Name:  [BROWSE]
           [     UPDATE     ]
}}}
Here is a full bootlog from the serial console:
{{{
CFE version 1.0.37-3.1 P12 for BCM96348 (32bit,SP,BE)
Build Date: mar set 26 15:13:11 CEST 2006 (root@RanmaLinux)
Copyright (C) 2000-2005 Broadcom Corporation.

Boot Address 0xbf000000

Initializing Arena.
Initializing Devices.
cfi_flash_get_device_id
Parallel flash device: name AM29LV640MT, id 0x2201, size 8192KB
CPU type 0x29107: 256MHz, Bus: 128MHz, Ref: 32MHz
Total memory: 16777216 bytes (16MB)

Total memory used by CFE:  0x80401000 - 0x80525DD0 (1199568)
Initialized Data:          0x8041D5E0 - 0x8041F560 (8064)
BSS Area:                  0x8041F560 - 0x80423DD0 (18544)
Local Heap:                0x80423DD0 - 0x80523DD0 (1048576)
Stack Area:                0x80523DD0 - 0x80525DD0 (8192)
Text (code) segment:       0x80401000 - 0x8041D5D8 (116184)
Boot area (physical):      0x00526000 - 0x00566000
Relocation Factor:         I:00000000 - D:00000000

Board IP address                  : 192.168.1.1:ffffff00  
Host IP address                   : 192.168.1.100  
Gateway IP address                :   
Run from flash/host (f/h)         : f  
Default host run file name        : vmlinux  
Default host flash file name      : bcm963xx_fs_kernel  
Boot delay (0-9 seconds)          : 1  
Boot image (0=latest, 1=previous) : 0  
Board Id Name                     : AliceAGW2+  
Psi size in KB                    : 24
Number of MAC Addresses (1-32)    : 13  
Base MAC Address                  : 00:1c:a2:12:0e:05  
Ethernet PHY Type                 : Internal
Memory size in MB                 : 16

*** Press any key to stop auto run (1 seconds) ***
Auto run second count down: 110
Booting from latest image (0xbf400000) ...
Code Address: 0x80010000, Entry Address: 0x80223018
8192 size flash memory detected
starting image at [BF400100] image length 370dae 

CRC from tag a25aec22 - CRC image calculated a25aec22
Decompression OK!
Entry at 0x80223018
Closing network.
Starting program at 0x80223018
Linux version 2.6.8.1 (fulvio@buildserver) (gcc version 3.4.2) #1 Tue Apr 3 18:09:37 CEST 2007
cfi_flash_get_device_id
Parallel flash device: name AM29LV640MT, id 0x2201, size 8192KB
Total Flash size: 8192K with 135 sectors
AliceAGW2+ prom init
CPU revision is: 00029107
mpi: No Card is in the PCMCIA slot

mpi_DetectPcCard:  mpi->pcmcia_cntl1 = 0x400f
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
Memory: 13456k/16000k available (1816k kernel code, 2524k reserved, 304k data, 76k init, 0k highmem)
Calibrating delay loop... 255.59 BogoMIPS
Mount-cache hash table entries: 512 (order: 0, 4096 bytes)
Checking for 'wait' instruction...  unavailable.
NET: Registered protocol family 16
Can't analyze prologue code at 801d46f4
SCSI subsystem initialized
usbcore: registered new driver usbfs
usbcore: registered new driver hub
NTFS driver 2.1.15 [Flags: R/W].
Initializing Cryptographic API
PPP generic driver version 2.4.2
NET: Registered protocol family 24
Using noop io scheduler
bcm963xx_mtd driver v1.0
PCI: Enabling device 0000:00:02.2 (0000 -> 0002)
ehci_hcd 0000:00:02.2: EHCI Host Controller
PCI: Setting latency timer of device 0000:00:02.2 to 64
ehci_hcd 0000:00:02.2: irq 32, pci mem b0020000
ehci_hcd 0000:00:02.2: new USB bus registered, assigned bus number 1
ehci_hcd 0000:00:02.2: USB 2.0 enabled, EHCI 0.95, driver 2004-May-10
hub 1-0:1.0: USB hub found
hub 1-0:1.0: 2 ports detected
ehci_hcd 0000:00:02.2: SCAN SetPortFeature wIndex=1 ports=2
ehci_hcd 0000:00:02.2: SCAN wValue =8
ehci_hcd 0000:00:02.2: SCAN SetPortFeature wIndex=2 ports=2
ehci_hcd 0000:00:02.2: SCAN wValue =8
ohci_hcd: 2004 Feb 02 USB 1.1 'Open' Host Controller (OHCI) Driver (PCI)
ohci_hcd: block sizes: ed 64 td 64
PCI: Enabling device 0000:00:02.0 (0000 -> 0002)
ohci_hcd 0000:00:02.0: OHCI Host Controller
PCI: Setting latency timer of device 0000:00:02.0 to 64
ohci_hcd 0000:00:02.0: irq 32, pci mem b0010000
ohci_hcd 0000:00:02.0: new USB bus registered, assigned bus number 2
hub 2-0:1.0: USB hub found
hub 2-0:1.0: 2 ports detected
PCI: Enabling device 0000:00:09.0 (0000 -> 0002)
ohci_hcd 0000:00:09.0: OHCI Host Controller
PCI: Setting latency timer of device 0000:00:09.0 to 64
ohci_hcd 0000:00:09.0: irq 20, pci mem c0000b00
ohci_hcd 0000:00:09.0: new USB bus registered, assigned bus number 3
ohci_hcd 0000:00:09.0: init err
ohci_hcd 0000:00:09.0: can't start
ohci_hcd 0000:00:09.0: init error -16
ohci_hcd 0000:00:09.0: remove, state 0
iounmap: bad address c0000b00
ohci_hcd 0000:00:09.0: USB bus 3 deregistered
ohci_hcd: probe of 0000:00:09.0 failed with error -16
usbcore: registered new driver usblp
drivers/usb/class/usblp.c: v0.13: USB Printer Device Class driver
Initializing USB Mass Storage driver...
usbcore: registered new driver usb-storage
USB Mass Storage support registered.
usbcore: registered new driver usbnet
brcmboard: brcm_board_init entry
SES: Button GPIO 0x8023 is enabled
SES: Button Interrupt 0x3 is enabled
SES: LED GPIO 0x8023 is enabled
plab_sem_init -- NOW create Sem_SPI_SmartCard SEMAPHORE 
bcm963xx_serial driver v2.0
********* Init NCN6001 Smart Card Driver *********
PLAB: reset_input()
PLAB: NCN-6001 Initialized
ext irq cfg register: 0x10040340


 IRQinit Register CTRL 18060340


u32 classifier
NET: Registered protocol family 2
IP: routing cache hash table of 512 buckets, 4Kbytes
TCP: Hash tables configured (established 512 bind 1024)
Initializing IPsec netlink socket
NET: Registered protocol family 1
NET: Registered protocol family 17
NET: Registered protocol family 15
Ebtables v2.0 registered
NET: Registered protocol family 8
NET: Registered protocol family 20
VFS: Mounted root (squashfs filesystem) readonly.
Freeing unused kernel memory: 76k freed
^@init started:  BusyBox v1.00 (2006.05.11-15:07+0000) multi-call binary
Algorithmics/MIPS FPU Emulator v1.5


BusyBox v1.00 (2006.05.11-15:07+0000) Built-in shell (msh)
Enter 'help' for a list of built-in commands.


Loading drivers and kernel modules... 

atmapi: module license 'Proprietary' taints kernel.
blaadd: blaa_detect entry
adsl: adsl_init entry
Broadcom BCMPROCFS v1.0 initialized
bcm63xxenet: bcmenet_module_init
bcm63xxenet: bcm63xx_enet_probe
Broadcom BCM6348B0 Ethernet Network Device v0.3 Apr  3 2007 18:06:51
bcm63xxenet: bcm63xx_init_dev
bcm63xxenet: init_dma
bcm63xxenet: init_buffers
bcm63xxenet: init_emac
init_emac EMAC_DISABLE
Config Internal PHY Through MDIO
mii_soft_reset--->mii_write
mii_write
mii_autoconfigure
mii_autoconfigure--->mii_write
mii_write
mii_getconfig
BCM63xx_ENET: Auto-negotiation timed-out
BCM63xx_ENET: 10 MB Half-Duplex (assumed)
eth0: MAC Address: 00:1C:A2:12:0E:05
mii_enablephyinterrupt--->mii_write
mii_write
Broadcom BCM6348B0 Ethernet Network Device v0.3 Apr  3 2007 18:06:51
bcm63xxenet: bcm63xx_init_dev
bcm63xxenet: init_dma
bcm63xxenet: init_buffers
bcm63xxenet: init_emac
init_emac EMAC_DISABLE
Config Ethernet Switch Through SPI Slave Select 0
dgasp: kerSysRegisterDyingGaspHandler: eth1 registered 
eth1: MAC Address: 00:1C:A2:12:0E:06
Broadcom BCM6348B0 USB Network Device v0.4 Apr  3 2007 18:06:53
usb0: MAC Address: 00 1C A2 12 0E 07
usb0: Host MAC Address: 00 1C A2 12 0E 08
PCI: Setting latency timer of device 0000:00:01.0 to 64
PCI: Enabling device 0000:00:01.0 (0004 -> 0006)
wl: srom not detected, using main memory mapped srom info (wombo board)
wl0: wlc_attach: using main board MAC address base in NVRAM (wombo board)
wl0 MAC Address: 00:1C:A2:12:0E:09
wl0: Broadcom BCM4318 802.11 Wireless Controller 3.131.35.0.cpe2.1ap1
dgasp: kerSysRegisterDyingGaspHandler: wl0 registered 
bcmIsEnetUp check internal PHY mii_linkstatus dev eth0
90
Running varlogger
<INFO> 00:00:11 xmlParse: syntax is OK
<INFO> 00:00:11 xmlParse: bad applications num is: 0
bcm63xx_enet_poll_timer EXTERNAL_SWITCH
bcm63xx_enet_poll_timer disabilito DMA ed EMAC
bcm63xx_enet_poll_timer riabilito EMAC e DMA
eth1 Link UP.
Pirelli_check_gateway: Start check default gateway 
Pirelli_check_gateway: Default gateway is set to ppp_8_35_1
Pirelli_UpgradeCheck: Previous version AGA_3.2.4
Pirelli_check_napt
Pirelli_check_napt: can' get user connection Name
BcmAdsl_Initialize=0xC005E238, g_pFnNotifyCallback=0xC0074C44
pSdramPHY=0xA0FFFFF8, 0x10180 0x82A10226
AdslCoreHwReset: AdslOemDataAddr = 0xA0FFA664
dgasp: kerSysRegisterDyingGaspHandler: dsl0 registered 
kLedAdsl: TRUE init led!
ip_tables: (C) 2000-2002 Netfilter core team
ip_conntrack version 2.1 (125 buckets, 0 max) - 368 bytes per conntrack
ip_conntrack_h323: init 
ip_conntrack_pptp version 2.1 loaded
ip_conntrack_rtsp v0.01 loading
ip_nat_h323: initialize the module!
ip_nat_pptp version 2.0 loaded
ip_nat_rtsp v0.01 loading
insmod: cannot open module `/lib/modules/2.6.8.1/kernel/net/ipv4/netfilter/ip_conntrack_ipsec.ko': No such file or directory
insmod: cannot open module `/lib/modules/2.6.8.1/kernel/net/ipv4/netfilter/ip_conntrack_wm.ko': No such file or directory
insmod: cannot open module `/lib/modules/2.6.8.1/kernel/net/ipv4/netfilter/ip_nat_ipsec.ko': No such file or directory
insmod: cannot open module `/lib/modules/2.6.8.1/kernel/net/ipv4/netfilter/ip_nat_wm.ko': No such file or directory
device usb0 entered promiscuous mode
eth0: bcm63xx_enet_open
eth0: bcm_set_multicast_list: 00001003
eth0: bcm_set_multicast_list: 00001003
br0: port 1(usb0) entering learning state
br0: topology change detected, propagating
br0: port 1(usb0) entering forwarding state
eth0: bcm_set_multicast_list: 00001103
device eth0 entered promiscuous mode
br0: port 2(eth0) entering learning state
br0: topology change detected, propagating
br0: port 2(eth0) entering forwarding state
eth0: bcm_set_multicast_list: 00001103
eth0: bcm_set_multicast_list: 00001103
eth1: bcm63xx_enet_open
eth1: bcm_set_multicast_list: 00001003
eth1: bcm_set_multicast_list: 00001003
eth1: bcm_set_multicast_list: 00001103
device eth1 entered promiscuous mode
br0: port 3(eth1) entering learning state
br0: topology change detected, propagating
br0: port 3(eth1) entering forwarding state
BcmNtwk_initLan: starting igmp lo
igmp started!
[AC] wait_for_interfaces: interface_name[0] = lo 
[AC] wait_for_interfaces: val length = 2 
[AC] wait_for_interfaces: iface.ifr_name = lo 
[AC] wait_for_interfaces: After parser interface_name[0] = lo 
igmp_main: ifc->igmpi_name == br0
PLAB: BcmPppoe_init --- wanInfo.ConnType:1
PLAB: BcmPppoe_init --- Lancio la BcmRfc2684_init(pWanId)
pvc2684d: Interface "nas_8_35" created sucessfully

pvc2684d: Communicating over ATM 0.8.35, encapsulation: LLC

DHCP DNS Servers:192.168.1.1
udhcp server (v0.9.6-pirelli) started
read_config init 
read_vlst: elementi trovati 0
read_vlst: elementi trovati 1
Clearing Reservations
Reloading Leases
Reloading Reservations
CreateHosts: il file non esiste..lo creo
CA: dhcpd domain_name= homenet.telecomitalia.it
[CA] bad_chaddr mac ff:ff:ff:ff:ff:ff
PLAB: BcmPppoe_init --- wanInfo.ConnType:3
PLAB: G.S. BcmPppoe_init --- Questo e' il PPPOE_BRIDGED quindi Aggiungo l'interfaccia al Bridge
br0: port 3(eth1) entering disabled state
br0: port 2(eth0) entering disabled state
br0: port 1(usb0) entering disabled state
device usb0 left promiscuous mode
br0: port 1(usb0) entering disabled state
eth0: bcm_set_multicast_list: 00001003
device eth0 left promiscuous mode
br0: port 2(eth0) entering disabled state
eth1: bcm_set_multicast_list: 00001003
device eth1 left promiscuous mode
br0: port 3(eth1) entering disabled state
eth0: bcm_set_multicast_list: 00001103
device eth0 entered promiscuous mode
br0: port 1(eth0) entering learning state
br0: topology change detected, propagating
br0: port 1(eth0) entering forwarding state
device nas_8_35 entered promiscuous mode
eth1: bcm_set_multicast_list: 00001103
device eth1 entered promiscuous mode
br0: port 3(eth1) entering learning state
br0: topology change detected, propagating
br0: port 3(eth1) entering forwarding state
device usb0 entered promiscuous mode
br0: port 4(usb0) entering learning state
br0: topology change detected, propagating
br0: port 4(usb0) entering forwarding state
device wl0 entered promiscuous mode
******   BcmL2BrCfg_init IS FLUSHING PSI...   ******
******   BcmL2BrCfg_init HAS FLUSHED PSI.   ******
device usb0 is already a member of a bridge; can't enslave it to bridge br0.
eth0: bcm_set_multicast_list: 00001103
device eth0 is already a member of a bridge; can't enslave it to bridge br0.
eth0: bcm_set_multicast_list: 00001103
eth1: bcm_set_multicast_list: 00001103
device eth1 is already a member of a bridge; can't enslave it to bridge br0.
BcmNtwk_initLan*** killing igmp lo pid = 319
BcmNtwk_initLan: starting igmp lo
igmp started!
[AC] wait_for_interfaces: interface_name[0] = lo 
[AC] wait_for_interfaces: val length = 2 
[AC] wait_for_interfaces: iface.ifr_name = lo 
[AC] wait_for_interfaces: After parser interface_name[0] = lo 
igmp_main: ifc->igmpi_name == br0
Setting SSID "Alice-31478062"
Setting SSID "Alice2-36957393"
Setting country code using abbreviation: "IT"
BUFRATE =  1b 2b 5.5b 6 9 11b 12 18 24 36 48 54 
[SL] MNTR_WIFI_SECURITY_WPA
Setting SSID ""
wl0 current channel 6
Setting SSID "Alice-31478062"
br0: port 5(wl0) entering learning state
br0: topology change detected, propagating
br0: port 5(wl0) entering forwarding state
sntp: host not found
[CA - ClientListMngr] ClientList_sem_init
[CA] - ARP_poll_task_init
[CA - ARP_ClientList_task_init] init  correctly completed
>> initVccCfg - vcc inst id=1, vcc=8/35
BcmCfmWlan_initSecMacFilterCfg
sysScratchPadSet: write scratch pad
Tr069DeviceMgr Interface is ppp_8_35_1
invalid index for interface 0
DNSMASQ reload_clients: Created a new client list for interface ppp_8_35_1
dnsmasq: NO DHCP server features
Init L2Filter CFM object queue for 2 objects
Init L2Filter CFM EXIT 2 objects
<INFO> 00:00:39 start: Starting HTB Configuration for QOS purposes


Creating UDHCPD.RES file.

Clearing Reservations
Reloading Leases
Reloading Reservations
WiFi List Initialization correctly completed
age_app.c:616 Started Smart Card engine version 2.11.1
PLAB: SmCardDrv_open () 
PLAB:SESSIONE di I/O su Smart Card -- TERMINALE NON DISPONIBILE !!!
}}}
