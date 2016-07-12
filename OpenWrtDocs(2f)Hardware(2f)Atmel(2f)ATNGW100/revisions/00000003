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
