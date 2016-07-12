'''Airlink101 ANAS350''' 

Link to Product info page at airlink101.com -> http://www.airlink101.com/products/anas350.html

Also known as the MGB111 from AMIT and others. PATA controller is IT8211F. SATA controller is SPIF213A.

The sources released appear to be the toolchain only. (July 9, 2008)

GPL tarball : http://www.airlink101.com/gpl/anas350/

=== JTAG Port ===

Accessed through serial connector:

DSR = TCK

RTS = TDO

DCD = TDI

CTS = TMS

=== Serial Port ===

||1) RI ||2) Vcc ||
||3) CTS ||4) RTS ||
||5) Rx ||6) DTR ||
||7) DSR ||8) Tx ||
||9) DCD ||10) GND ||

=== 16-pin MII Connector ===

Not yet documented.

=== kernel boot from /proc/kmsg ===

{{{
<4>Linux version 2.4.28 (root@ATC-P4-95) (gcc version 3.3.6) #187 ¤­ 3¤ë 30 10:33:32 CST 2007
<6>BIOS-provided physical RAM map:
<4> BIOS-e801: 0000000000000000 - 000000000009f000 (usable)
<4> BIOS-e801: 0000000000100000 - 0000000002000000 (usable)
<5>32MB LOWMEM available.
<4>On node 0 totalpages: 8192
<4>zone(0): 4096 pages.
<4>zone(1): 4096 pages.
<4>zone(2): 0 pages.
<6>DMI not present.
<4>Kernel command line: rw console=ttyS0,38400 aT
                                                 AÕTÖâ
<6>Initializing CPU#0
<4>Calibrating delay loop... 44.33 BogoMIPS
<6>Memory: 27368k/32768k available (1117k kernel code, 5012k reserved, 720k data, 60k init, 0k highmem)
<4>Checking if this processor honours the WP bit even in supervisor mode... Ok.
<6>Dentry cache hash table entries: 4096 (order: 3, 32768 bytes)
<6>Inode cache hash table entries: 2048 (order: 2, 16384 bytes)
<6>Mount cache hash table entries: 512 (order: 0, 4096 bytes)
<6>Buffer cache hash table entries: 1024 (order: 0, 4096 bytes)
<4>Page-cache hash table entries: 8192 (order: 3, 32768 bytes)
<7>CPU:     After generic, caps: 00000000 00000000 00000000 00000000
<7>CPU:             Common caps: 00000000 00000000 00000000 00000000
<4>CPU: Cyrix Cx486SLC
<6>Checking 'hlt' instruction... OK.
<6>Checking for popad bug... OK.
<4>POSIX conformance testing by UNIFIX
<6>PCI: Using configuration type 1
<6>PCI: Probing PCI hardware
<4>PCI: Probing PCI hardware (bus 00)
<6>Linux NET4.0 for Linux 2.4
<6>Based upon Swansea University Computer Society NET3.039
<4>Initializing RT netlink socket
<4>Starting kswapd
<5>VFS: Disk quotas vdquot_6.5.1
<5>NTFS driver v1.1.22 [Flags: R/O]
<6>Serial driver version 5.05c (2001-07-08) with MANY_PORTS SHARE_IRQ SERIAL_PCI enabled
<6>ttyS00 at 0x03f8 (irq = 4) is a 16550A
<4>RAMDISK driver initialized: 16 RAM disks of 8192K size 1024 blocksize
<6>r6040: RDC R6040 RX NAPI net driver, version 0.15 (26Sep2006)
<6>r6040: RDC R6040 RX NAPI net driver, version 0.15 (26Sep2006)
<7>PCI: Setting latency timer of device 00:08.0 to 64
<6>r6040: RDC R6040 RX NAPI net driver, version 0.15 (26Sep2006)
<7>PCI: Setting latency timer of device 00:09.0 to 64
<6>Uniform Multi-Platform E-IDE driver Revision: 7.00beta4-2.4
<6>ide: Assuming 33MHz system bus speed for PIO modes; override with idebus=xx
<6>IT821x: unknown IDE controller at PCI slot 00:04.0, VID=1283, DID=8211
<6>IT821x: chipset revision 17
<6>IT821x: not 100% native mode: will probe irqs later
<6>it8212: forcing bypass mode.
<6>it821x: controller in pass through mode.
<6>    ide0: BM-DMA at 0xa410-0xa417, BIOS settings: hda:pio, hdb:pio
<6>    ide1: BM-DMA at 0xa418-0xa41f, BIOS settings: hdc:pio, hdd:pio
<4>hdc: ST3320620AS, ATA DISK drive
<4>blk: queue c02fdcd4, I/O limit 4095Mb (mask 0xffffffff)
<4>ide1 at 0x9c10-0x9c17,0xa012 on irq 9
<4>hdc: attached ide-disk driver.
<4>hdc: host protected area => 1
<6>hdc: 625142448 sectors (320073 MB) w/16384KiB Cache, CHS=38913/255/63, UDMA(133)
<6>Partition check:
<6> hdc:hdc1 hdc4
<6>SCSI subsystem driver Revision: 1.00
<3>kmod: failed to exec /sbin/modprobe -s -k scsi_hostadapter, errno = 2
<5>physmap flash device: 400000 at ffc00000
<4>enter cfi_probe_chip
<4>send query command 98 55
<5> Amd/Fujitsu Extended Query Table v1.1 at 0x0040
<4>Physically mapped flash: Swapping erase regions for broken CFI table.
<5>number of CFI chips: 1
<5>cfi_cmdset_0002: Disabling fast programming due to code brokenness.
<6>usb.c: registered new driver usbdevfs
<6>usb.c: registered new driver hub
<6>ehci_hcd 00:0a.1: PCI device 17f3:6061
<6>ehci_hcd 00:0a.1: irq 14, pci mem c2c01000
<6>usb.c: new USB bus registered, assigned bus number 1
<6>ehci_hcd 00:0a.1: USB 2.0 enabled, EHCI 1.00, driver 2003-Dec-29/2.4
<6>hub.c: USB hub found
<6>hub.c: 2 ports detected
<4>kusbd: /sbin/hotplug add 1 0
<6>host/usb-ohci.c: USB OHCI at membase 0xc2c03000, IRQ 15
<6>host/usb-ohci.c: usb-00:0a.0, PCI device 17f3:6060
<6>usb.c: new USB bus registered, assigned bus number 2
<6>hub.c: USB hub found
<6>hub.c: 2 ports detected
<4>kusbd: /sbin/hotplug add 1 0
<6>usb.c: registered new driver usbscanner
<6>scanner.c: 0.4.16:USB Scanner Driver
<6>usb.c: registered new driver usblp
<6>printer.c: v0.13: USB Printer Device Class driver
<6>Initializing USB Mass Storage driver...
<6>usb.c: registered new driver usb-storage
<6>USB Mass Storage support registered.
<6>NET4: Linux TCP/IP 1.0 for NET4.0
<6>IP Protocols: ICMP, UDP, TCP, IGMP
<6>IP: routing cache hash table of 512 buckets, 4Kbytes
<6>TCP: Hash tables configured (established 8192 bind 16384)
<6>NET4: Unix domain sockets 1.0/SMP for Linux NET4.0.
<6>NET4: Ethernet Bridge 008 for NET4.0
<6>NET4: AppleTalk 0.18a for Linux NET4.0
<5>RAMDISK: LZMA image found at block 0
<5>RAMDISK: LZMA lc=3,lp=0,pb=2,dictSize=8388608,origSize=8388608
<5>LZMA initrd by Ming-Ching Tiew <mctiew@yahoo.com>
<4> ..........<6>hub.c: new USB device 00:0a.1-1, assigned address 2
<4>...<6>scsi0 : SCSI emulation for USB Mass Storage devices
<4>.  Vendor: Generic   Model: USB Flash Drive   Rev: 1.00
<4>  Type:   Direct-Access                      ANSI SCSI revision: 02
<4>Attached scsi removable disk sda at scsi0, channel 0, id 0, lun 0
<4>....SCSI device sda: 4194305 512-byte hdwr sectors (2147 MB)
<4>.sda: Write Protect is off
<6> sda:sda1
<7>WARNING: USB Mass Storage data integrity not assured
<7>USB Mass Storage device found at 2
<4>kusbd: /sbin/hotplug add 2 1
<4>.............................................................................................................................................................................................................................................
<4>LZMA initrd loaded successfully
<6>Freeing initrd memory: 2559k freed
<4>EXT2-fs warning: checktime reached, running e2fsck is recommended
<4>VFS: Mounted root (ext2 filesystem).
<6>Freeing unused kernel memory: 60k freed
<6>Adding Swap: 136512k swap-space (priority -1)
<4>EXT2-fs warning: mounting unchecked fs, running e2fsck is recommended
<4>VFS: Can't find ext2 filesystem on dev sd(8,1).
<6>device eth1 entered promiscuous mode
<6>br0: port 1(eth1) entering learning state
<6>br0: port 1(eth1) entering forwarding state
<6>br0: topology change detected, propagating
}}}

Note: The 320GB SATA hard drive and 2GB usb flash drive are not installed by default.

 . CategoryNasDevices
