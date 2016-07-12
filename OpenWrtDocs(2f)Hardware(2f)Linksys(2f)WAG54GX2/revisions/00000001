'''Linksys WAG54GX2'''

The device is NOT supported in OpenWrt.

{{{
Bootloader: CFE
System-On-Chip:  Broadcom 6348
CPU Speed: 200 Mhz (assumed: BogoMIPS=239.20 XTAL=66Mhz)
Flash size: 8 MB
RAM: 32 MB
Wireless: integrated Airgo MIMO 802.11b/g Wireless LAN Controller
Ethernet: Unknown switch
USB: None
ADSL: 2/2+
Serial: tbd
JTAG: tbd
}}}

The {{{boot_wait}}} NVRAM variable is not defined.

'''Firmware notes'''

We can build custom firmwares that will upload via the regular web interface.

{{{
Analysis of WAG54GX2_A_V1.00.01.img
-----------------------------------
00010100:0035d100:gzip cramfs on /tmp/fs1
00400000:-        :CFE bootloader 0
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


'''Serial console/JTAG'''

The device has an internal 12-pins connector and a 4 pins connector. At least a serial console would be supported I think.

----
CategoryModel
