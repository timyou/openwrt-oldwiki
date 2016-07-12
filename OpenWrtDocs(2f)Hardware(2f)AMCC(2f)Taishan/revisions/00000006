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

Press a key on bootup to enter the u-boot bootloader's console.

Set up the IP addresses:

{{{
setenv ipaddr 192.168.1.1
setenv serverip 192.168.1.254
}}}

Create an easy way for us to reflash the box in u-boot:
{{{
setenv flash_openwrt erase \${kernel_addr} ffdfffff\;tftp 100000 openwrt-ppc44x-squashfs.img\;cp.b \${fileaddr} \${kernel_addr} \${filesize}
}}}

Create the needed bootargs for !OpenWrt:

{{{
setenv bootargs console=ttyS1,115200 root=/dev/mtdblock1 rootfstype=squashfs,jffs2 noinitrd init=/etc/preinit
setenv bootcmd bootm \$(kernel_addr)
saveenv
reset
}}}

Flash !OpenWrt and reset:
{{{
run flash_openwrt
reset
}}}

----
CategoryModel
