'''Davolink DV201AMR'''

=== Details ===
{{{
Bootloader     : CFE version 1.0.37-0.6 for BCM96348 (32bit,SP,BE)
System-On-Chip : Broadcom 6348 (CPU type 0x29107)
CPU Speed      : 256MHz, Bus: 128MHz, Ref: 32MHz
Flash size     : 8 MB
RAM            : 16 MB
Wireless       : Broadcom 4320 802.11b/g (mini-pci DV201AMR) (integrated DV2020)
Switch         : BCM5325E
USB            : 1.1 slave
ADSL           : 2/2+
Serial         : yes
JTAG           : yes
}}}

=== Serial console ===

Pinout as follows:
{{{
1 VCC 3.3V
2 GND
3 TX
4 RX
5 GND
6 nc
}}}

=== JTAG ===

Standard 12 pin's, close to the leds.

=== CFE ===

Image for regular cfe the trx is copied to low half of flash. Map is as follows:
{{{
  start          len
  0x00000000:<firmware>                           backup
  <firmware>:-0x00400000                          rootfs_data
  0x00400000:0x00010000                           CFE:RO
  0x00410000:0x003f0000                           linux
  0x00410000+<kernel>:<rootfs_len>                rootfs
  0x00410000+<firmware>:-0x8000000                free1
}}}

Patched CFE, proposed MAP is like:
{{{
  start          len
  0x00000000:0x00010000                           free2
  0x00010000:0x003f0000                           rootfs_data
  0x00400000:0x00010000                           CFE:RO
  0x00410000:0x003f0000                           linux
  0x00410000+<kernel_len>:<rootfs_len>            rootfs
  0x00410000+<kernel_len>+<rootfs_len>:-0x8000000 free1
}}}
attachment:Patched-cfe-for-Davolink.bin

update: mtd write Patched-cfe-for-Davolink.bin /dev/mtd0

attachment:bcm963xx_fs_kernel_dv201amr   Firmware image

'''Working:'''
{{{
CFE
Ethernet  BCM6348
wlan      BCM4320
switch    BCM5325E    
}}}
'''Missing:'''
{{{
adsl dsp
voip dsp
slave usb 
}}}

=== Links ===
For internals and pinouts see (in Dutch):
http://gathering.tweakers.net/forum/list_message/27451094#27451094

Notes on patched CFE:
http://forum.openwrt.org/viewtopic.php?pid=81093#p81093
----
CategoryModel ["CategoryBCM63xx"]
 
