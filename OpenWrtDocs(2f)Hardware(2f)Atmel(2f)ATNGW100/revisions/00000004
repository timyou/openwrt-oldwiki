'''Atmel ATNGW100 Network Gateway Kit'''

{{{
Bootloader: u-boot
CPU: Atmel AT32AP7000
CPU Speed: 130 Mhz
Flash size: 2x8 MB + SD/MMC slot
RAM: 32 MB
Wireless: none
Ethernet: 2 ethernet ports connected to the CPU
USB: yes
Serial: yes
JTAG: yes
}}}
'''Bootloader'''

First of all ensure you have a recent u-boot (1.3.0 or higher). If not, you can safely upgrade u-boot downloading the flash-upgrade image image from here: http://www.atmel.no/buildroot/buildroot-u-boot.html and loading it:

{{{
tftp 0x10400000 flash-upgrade-atngw100-to-v1.3.3.uimg
bootm}}}
Confirm the upgrade procedure when asked:

{{{
AVR32 Flash upgrade utility version 0.2
HSMC configuration: 0x00030001 0x06030504 0x00080008 0x00001103
Atmel AT49BV642D found at address 0x00000000
cfi: using AMD/Fujitsu command set
cfi: 2 erase regions (total size: 8388608 bytes)
  0 8 sectors, 8192 bytes each
  1 127 sectors, 65536 bytes each
Going to copy 104816 bytes to offset 0x00000000 in flash
Press `y' to continue, or any other key to abort}}}
'''Installation'''

Set up the IP addresses:

{{{
setenv ipaddr 192.168.1.1
setenv serverip 192.168.1.254
}}}
Create an easy way for us to reflash the box in u-boot:

{{{
setenv flash_openwrt tftp 0x90000000 openwrt-avr32-squashfs.img\;erase 0x20000 +\${filesize}\;cp.b \${fileaddr} 0x20000 \${filesize}
}}}
Create the needed variables for !OpenWrt:

{{{
setenv bootargs console=ttyS0,115200 root=/dev/mtdblock2 rootfstype=squashfs,jffs2 noinitrd init=/etc/preinit
setenv bootcmd bootm 0x20000
setenv tftpip
saveenv
}}}
Flash !OpenWrt and reset:

{{{
run flash_openwrt
reset
}}}
----
 CategoryModel
