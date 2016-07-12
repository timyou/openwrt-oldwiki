'''AMCC Taishan Evaluation board'''

{{{
Bootloader: u-boot
CPU: AMCC PPC440GX
CPU Speed: 800 Mhz
Flash size: 64 MB
RAM: 256 MB
Wireless: none, 2x PCI-X slots
Ethernet: 2 gigabit ports connected to the CPU
USB: none
Serial: yes
JTAG: yes
}}}

'''Installation'''

Set up a tftp server and use these commands over serial console:

{{{
erase 0xfc000000 ffdfffff
setenv ipaddr [ip for the taishan]
setenv serverip [tftp server ip]
tftp 100000 openwrt-amcc-2.6-squashfs.img
cp.b 0x100000 0xfc000000 [size of the image in hex, the bootloader prints it after the tftp]
setenv ramdisk_addr
setenv openwrt setenv bootargs console=ttyS1,115200 root=/dev/mtdblock1 rootfstype=squashfs,jffs2\;bootm \$(kernel_addr)
setenv bootcmd run openwrt
saveenv
reset
}}}


----
CategoryModel
