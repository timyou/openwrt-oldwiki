'''AMCC Kilauea Evaluation board'''

{{{
Bootloader: u-boot
CPU: AMCC PPC405EX
CPU Speed: 600 Mhz
Flash size: 64 MB NOR + 64MB NAND
RAM: 256 MB
Wireless: none, 2x PCIe 1x slots
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
setenv flash_openwrt erase \${kernel_addr} fc2fffff\;tftp 100000 openwrt-ppc40x-squashfs.img\;cp.b \${fileaddr} \${kernel_addr} \${filesize}
}}}

Create the needed variables for !OpenWrt:

{{{
openwrt cp.b 0xfc1e0000 \${fdt_addr} 20000\; bootm \${kernel_addr} - \${fdt_addr}
setenv bootcmd run openwrt
saveenv
}}}

Flash !OpenWrt and reset:
{{{
run flash_openwrt
reset
}}}

----
CategoryModel
