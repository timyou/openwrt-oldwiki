'''IO-DATA USL-5P'''


This is a NAS with 5 USB ports and 1 ethernet interface.

 * Bootloader: SH IPL+g with modifications from IO-DATA
 * CPU: SH7751R @ 240MHz (SH4)
 * Flash size: 512Kbyte
 * RAM: 64MByte
 * Ethernet: Realtek RTL8139C+
 * Serial: yes, pinouts follow
 * CF slot: yes, the bootloader boots from a CF card
 * USB: Yes, NEC USB 2.0 controller with 5 ports
 * Other: Buzzer, RTC


=== Serial pinout ===


{{{
   o   o   o   o     [battery]
  GND RxD TxD 3.3V
}}}

Serial settings are 9600, 8n1.

=== Boot ===

The original firmware boots immediately after the bootloader initialization is complete, there is no way to abort it. Also there is no known way to login to it, so the only way to install OpenWrt on this device is to change the contents of the CF card.

Some hacking will have to be done, currently the bootloader invokes LILO, which invokes its hacked bootblock, which boots the kernel...


'''OpenWrt dmesg'''

This is based on the 2.6.22-rc4 patchset made by Kaloz, so don't let the revision number cheat you. Patches will be done after a major cleanup, since the toolchain, the kernel, the kenel modules and the userland is a bit messy right now. Anyway, we've got a lift-off, Houston.

{{{
Uncompressing Linux... Ok, booting the kernel.                                  
m�   0.000000] Linux version 2.6.22-rc4 (root@bprov02) (gcc version 3.4.6 (Open7
[    0.000000] Node 0: start_pfn = 0xc000, low = 0x10000                        
[    0.000000] Zone PFN ranges:                                                 
[    0.000000]   Normal      49152 ->    65536                                  
[    0.000000] early_node_map[1] active PFN ranges                              
[    0.000000]     0:    49152 ->    65536                                      
[    0.000000] Node 0: mem_map starts at 8c1e8000                               
[    0.000000] I-O DATA DEVICE, INC. "LANDISK Series" support.                  
[    0.000000] Built 1 zonelists.  Total pages: 16256                           
[    0.000000] Kernel command line: console=ttySC1,9600 mem=64M init=/etc/prein1
[    0.000000] Setting GDB trap vector to 0x80000100                            
[    0.000000] PID hash table entries: 256 (order: 8, 1024 bytes)               
[    0.000000] Using tmu for system timer                                       
[    0.000049] Using 8.333 MHz high precision timer.                            
[    0.000324] Dentry cache hash table entries: 8192 (order: 3, 32768 bytes)    
[    0.000837] Inode-cache hash table entries: 4096 (order: 2, 16384 bytes)     
[    0.009770] Memory: 62976k/63024k available (1423k kernel code, 2512k reserv)
[    0.009824] PVR=04050005 CVR=20480000 PRR=00000113                           
[    0.009855] I-cache : n_ways=2 n_sets=256 way_incr=8192                      
[    0.009890] I-cache : entry_mask=0x00001fe0 alias_mask=0x00001000 n_aliases=2
[    0.009930] D-cache : n_ways=2 n_sets=512 way_incr=16384                     
[    0.009964] D-cache : entry_mask=0x00003fe0 alias_mask=0x00003000 n_aliases=4
[    0.249983] Mount-cache hash table entries: 512                              
[    0.250710] CPU: SH7751R                                                     
[    0.251931] NET: Registered protocol family 16                               
[    0.256531] SCSI subsystem initialized                                       
[    0.256814] DMA: Registering DMA API.                                        
[    0.256869] DMA: Registering sh_dmac handler (8 channels).                   
[    0.259466] Autoconfig PCI channel 0x8c1b36a4                                
[    0.259515] Scanning bus 00, I/O 0xfe240000:0xfe280000, Mem 0xfd000000:0xfe00
[    0.259573] 00:00.0 Class 0200: 10ec:8139 (rev 20)                           
[    0.259618]         I/O at 0xfe240000 [size=0x100]                           
[    0.259659]         Mem at 0xfd000000 [size=0x100]                           
[    0.259785] 00:02.0 Class 0c03: 1033:0035 (rev 43)                           
[    0.259826]         Mem at 0xfd001000 [size=0x1000]                          
[    0.259905] 00:02.1 Class 0c03: 1033:0035 (rev 43)                           
[    0.259945]         Mem at 0xfd002000 [size=0x1000]                          
[    0.260025] 00:02.2 Class 0c03: 1033:00e0 (rev 04)                           
[    0.260064]         Mem at 0xfd003000 [size=0x100]                           
[    0.264048] PCI: Using configuration type 1                                  
[    0.267571] NET: Registered protocol family 2                                
[    0.269686] Time: SuperH clocksource has been installed.                     
[    0.359772] IP route cache hash table entries: 1024 (order: 0, 4096 bytes)   
[    0.360097] TCP established hash table entries: 2048 (order: 2, 16384 bytes) 
[    0.360313] TCP bind hash table entries: 2048 (order: 1, 8192 bytes)         
[    0.360450] TCP: Hash tables configured (established 2048 bind 2048)         
[    0.360483] TCP reno registered                                              
[    0.393286] gio: driver initialized                                          
[    0.395055] squashfs: version 3.0 (2006/03/15) Phillip Lougher               
[    0.395103] Registering mini_fo version $Id$                                 
[    0.395209] io scheduler noop registered                                     
[    0.395237] io scheduler deadline registered (default)                       
[    0.396483] Serial: 8250/16550 driver $Revision: 1.90 $ 2 ports, IRQ sharingd
[    0.397730] SuperH SCI(F) driver initialized                                 
[    0.398123] sh-sci: ttySC0 at MMIO 0xffe00000 (irq = 25) is a sci            
[    0.398554] sh-sci: ttySC1 at MMIO 0xffe80000 (irq = 43) is a scif           
[    3.946739] 8139cp: 10/100 PCI Ethernet driver v1.3 (Mar 22, 2004)           
[    4.020874] eth0: RTL-8139C+ at 0xfd000000, 00:a0:b0:6c:e0:69, IRQ 5         
[    4.097549] scsi0 : pata_platform                                            
[    4.136456] ata1: PATA max PIO0 cmd 0xc0100040 ctl 0xc010002c bmdma 0x0000000
[    4.424392] ata1.00: CFA: Hitachi XX.V.4.1.0.0, Rev 0.00, max PIO4           
[    4.488451] ata1.00: 62592 sectors, multi 0: LBA                             
[    4.544962] ata1.00: configured for PIO                                      
[    4.591566] scsi 0:0:0:0: Direct-Access     ATA      Hitachi XX.V.4.1 Rev  P5
[    4.689223] sd 0:0:0:0: [sda] 62592 512-byte hardware sectors (32 MB)        
[    4.765879] sd 0:0:0:0: [sda] Write Protect is off                           
[    4.823552] sd 0:0:0:0: [sda] Write cache: disabled, read cache: enabled, doA
[    4.933766] sd 0:0:0:0: [sda] 62592 512-byte hardware sectors (32 MB)        
[    5.010726] sd 0:0:0:0: [sda] Write Protect is off                           
[    5.068404] sd 0:0:0:0: [sda] Write cache: disabled, read cache: enabled, doA
[    5.178027]  sda: sda1                                                       
[    5.207007] sd 0:0:0:0: [sda] Attached SCSI removable disk                   
[    5.272647] push-switch: version 0.1.1 loaded                                
[    5.325003] heartbeat: version 0.1.0 loaded                                  
[    5.375252] nf_conntrack version 0.5.0 (512 buckets, 4096 max)               
[    5.445815] ip_tables: (C) 2000-2006 Netfilter Core Team                     
[    5.508924] TCP vegas registered                                             
[    5.547445] NET: Registered protocol family 1                                
[    5.599733] NET: Registered protocol family 17                               
[    5.653187] Bridge firewalling registered                                    
[    5.701237] 802.1Q VLAN Support v1.8 Ben Greear <greearb@candelatech.com>    
[    5.782834] All bugs added by David S. Miller <davem@redhat.com>             
[    5.858019] EXT3-fs: INFO: recovery required on readonly filesystem.         
[    5.931442] EXT3-fs: write access will be enabled during recovery.           
[    6.215307] kjournald starting.  Commit interval 5 seconds                   
[    6.271051] EXT3-fs: recovery complete.                                      
[    6.354947] EXT3-fs: mounted filesystem with ordered data mode.              
[    6.415921] VFS: Mounted root (ext3 filesystem) readonly.                    
[    6.480955] Freeing unused kernel memory: 68k freed                          
[    6.541674] Warning: unable to open an initial console.                      
�[    7.142014] EXT3-fs warning: maximal mount count reached, running e2fsck isd
[    7.243859] EXT3 FS on sda1, internal journal                                
�5init started:  BusyBox v1.4.2 (2007-06-10 18:24:16 CEST) multi-ca             
Please press Enter to activate this console. [    8.286636] eth0: link up, 100M1
: udhcpc (v1.4.2) started                                                       
                                                                                
: Sending discover...                                                           
                                                                                
: Sending select for 10.1.2.17...                                               
                                                                                
: Lease of 10.1.2.17 obtained, lease time 7200                                  
                                                                                
: adding router 10.1.2.254                                                      
                                                                                
: deleting old routes                                                           
                                                                                
[    9.826578] eth0: link up, 100Mbps, full-duplex, lpa 0x41E1                  
: adding dns 195.184.181.228                                                    
                                                                                
[   10.679971] PPP generic driver version 2.4.2                                 
                                                                                
                                                                                
                                                                                
BusyBox v1.4.2 (2007-06-10 18:24:16 CEST) Built-in shell (ash)                  
Enter 'help' for a list of built-in commands.                                   
                                                                                
  _______                     ________        __                                
 |       |.-----.-----.-----.|  |  |  |.----.|  |_                              
 |   -   ||  _  |  -__|     ||  |  |  ||   _||   _|                             
 |_______||   __|_____|__|__||________||__|  |____|                             
          |__| W I R E L E S S   F R E E D O M                                  
 KAMIKAZE (bleeding edge, r7257) -------------------                            
  * 10 oz Vodka       Shake well with ice and strain                            
  * 10 oz Triple sec  mixture into 10 shot glasses.                             
  * 10 oz lime juice  Salute!                                                   
 ---------------------------------------------------                            
root@OpenWrt:/# 
}}}






'''Original dmesg'''

This is out-of-date, but you can still reach it at http://trash.uid0.hu/openwrt/usl-5p_original-dmesg.txt


NOTE: This wiki entry will be changing quickly as I'm playing around with OpenWrt to support this board.
, which boots the kernel 
