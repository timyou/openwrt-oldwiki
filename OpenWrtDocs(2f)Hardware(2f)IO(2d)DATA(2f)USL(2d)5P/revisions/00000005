'''IO-DATA USL-5P'''


This is a NAS with 5 USB ports and 1 ethernet interface.

 * Bootloader: SH IPL+g with modifications from IO-DATA
 * CPU: SH7751R @ 240MHz (SH4)
 * Flash size:
 * RAM: 64MByte
 * Ethernet: Realtek RTL8139C+
 * Serial: yes, pinouts follow
 * CF slot: yes, the bootloader boots from a CF card
 * Other: Buzzer, RTC


=== Serial pinout ===


{{{
   o   o   o   o     [battery]
  GND RxD TxD 3.3V
}}}

Serial settings are 9600, 8n1.

=== Boot ===

The original firmware boots immediately after the bootloader initialization is complete, there is no way to abort it. Also there is no known way to login to it, so the only way to install OpenWrt on this device is to change the contents of the CF card.

'''Original dmesg'''
{{{
SH IPL+g version 0.9, Copyright (C) 2000 Free Software Foundation, Inc.

This software comes with ABSOLUTELY NO WARRANTY; for details type `w'.
This is free software, and you are welcome to redistribute it under
certain conditions; type `l' for details.

2002/09/09 Making.  2004/09/08 I-O DATA NSU Update.
266:133:33 on base clock 22.22MHz and SDRAM 4 burst. CF boot.

PCIC initialization done.
MASTER:48bit LBA mode non support
Disk drive detected:  20051220 CF CARD     FFF022BC 
LBA: 0003D860
DiskSize: 129024000Byte
PIO MODE1
Set Transfer Mode result: 50 
> b
Set Transfer Mode result: 50 
Initialize Device Parameters result: 50 
IDLE result: 50 
LILO boot: first-image
Loading linux....................done.
64M console=ttySC1,9600
Kernel Start
version 2.4.21 (ulinux@ELITEPC) (gcc version 3.2.3) #50 2005
On node 0 totalpages: 16384
zone(0): 16384 pages.
zone(1): 0 pages.
zone(2): 0 pages.
Kernel command line: mem=64M console=ttySC1,9600
CPU clock: 266.68MHz
Bus clock: 133.34MHz
Module clock: 33.33MHz
Interval = 5207
Calibrating delay loop... 266.24 BogoMIPS
Memory: 62668k/65536k available (1659k kernel code, 2868k reserved, 271k data, )
Dentry cache hash table entries: 8192 (order: 4, 65536 bytes)
Inode cache hash table entries: 4096 (order: 3, 32768 bytes)
Mount cache hash table entries: 512 (order: 0, 4096 bytes)
Buffer-cache hash table entries: 4096 (order: 2, 16384 bytes)
Page-cache hash table entries: 16384 (order: 4, 65536 bytes)
CPU: SH7751R
POSIX conformance testing by UNIFIX
PCI: Using configuration type 1
SH7751R PCI: Finished initialization of the PCI controller
Linux NET4.0 for Linux 2.4
Based upon Swansea University Computer Society NET3.039
Initializing RT netlink socket
Allocate Area5/6 success.
Julian Shutdown button driver initialized
Starting kswapd
Journalled Block Device driver loaded
Installing knfsd (copyright (C) 1996 okir@monad.swb.de).
NTFS driver 2.1.6b [Flags: R/O].
pty: 256 Unix98 ptys configured
SuperH SCI(F) driver initialized
ttySC0 at 0xffe00000 is a SCI
ttySC1 at 0xffe80000 is a SCIF
Real Time Clock Driver v1.10e
Uniform Multi-Platform E-IDE driver Revision: 7.00beta4-2.4
ide: Assuming 33MHz system bus speed for PIO modes; override with idebus=xx
hda: , CFA DISK drive
ide0 at 0x1f0-0x1f7,0x3f6 on irq 10
hda: attached ide-disk driver.
hda: task_no_data_intr: status=0x51 { DriveReady SeekComplete Error }
hda: task_no_data_intr: error=0x04 { DriveStatusError }
hda: 252000 sectors (129 MB) w/1KiB Cache, CHS=250/16/63
ide-floppy driver 0.99.newide
Partition check:
 hda: hda1
ide-floppy driver 0.99.newide
SCSI subsystem driver Revision: 1.00
scsi0 : SCSI host adapter emulation for IDE ATAPI devices
NET4: Linux TCP/IP 1.0 for NET4.0
IP Protocols: ICMP, UDP, TCP
IP: routing cache hash table of 512 buckets, 4Kbytes
TCP: Hash tables configured (established 4096 bind 8192)
NET4: Unix domain sockets 1.0/SMP for Linux NET4.0.
NET4: AppleTalk 0.18a for Linux NET4.0
 hda: hda1
 hda: hda1
 hda: hda1
 hda: hda1
VFS: Mounted root (ext2 filesystem) readonly.
Freeing unused kernel memory: 52k freed
init started:  BusyBox v0.60.5 (2004.07.22-09:20+0000) multi-call binary
Mounting proc filesystem:  [  OK  ]
Configuring kernel parameters:  [  OK  ]
Timed out waiting for time change.
Setting clock  (localtime): Wed Mar 14 15:03:02 JST 2007 [  OK  ]
Setting hostname usl-5p:  [  OK  ]
Mounting USB filesystem:  [  OK  ]
Remounting root filesystem in read-write mode:  [  OK  ]
Finding module dependencies:  [  OK  ]
Checking filesystems
Checking all file systems.
[  OK  ]
Mounting local filesystems:  [  OK  ]
Setting network parameters:  [  OK  ]
Bringing up loopback interface:  [  OK  ]
Bringing up interface eth0:  
Determining IP information for eth0... failed.
[FAILED]
Starting portmapper: [  OK  ]
Starting httpd: [  OK  ]
Starting SMB services: [  OK  ]
Starting NMB services: [  OK  ]
Starting crond: [  OK  ]
Starting button_daemon:  [  OK  ]
Start Shutdown button surveillance
Done
Starting usbhdmng:  [  OK  ]
getty: ioctl()
Lineo Linux
Kernel 2.4.21 on an sh4
usl-5p login: 
}}}


NOTE: This wiki entry will be changing quickly as I'm playing around with OpenWrt to support this board.
