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

'''Installation'''

Set up a tftp server and use these commands over serial console:

{{{
protect off 0x20000 0x7EFFFF
erase 0x20000 0x7EFFFF
setenv ipaddr [ip for the ngw]
setenv serverip [tftp server ip]
setenv tftpip
tftp 0x90000000 openwrt-avr32-2.6-squashfs.img
cp.b 0x90000000 0x20000 [size of the image in hex, the bootloader prints it after the tftp]
setenv bootargs console=ttyS0,115200 root=/dev/mtdblock2 rootfstype=squashfs,jffs2 noinitrd init=/etc/preinit
setenv bootcmd bootm 0x20000
saveenv
reset
}}}


----
CategoryModel
