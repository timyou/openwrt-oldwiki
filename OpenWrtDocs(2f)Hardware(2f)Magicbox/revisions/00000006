'''Magicbox'''

The Magicbox have two different hardware versions currently.

=== Magicbox v1.1 ===

{{{
Bootloader: u-boot
CPU: AMCC PPC405EP
CPU Speed: 200 Mhz
Flash size: 4 MB
RAM: 32 MB
Wireless: 1x mini-PCI slot
Ethernet: 1 port connected to the CPU
USB: no
Serial: yes, external (you need a straight cable)
JTAG: yes
Power over Ethernet: 18-24V
}}}

=== Magicbox v2.0 ===

{{{
Bootloader: u-boot
CPU: AMCC PPC405EP
CPU Speed: 200 Mhz
Flash size: 4 MB + CF slot
RAM: 32 MB
Wireless: 3x mini-PCI slot
Ethernet: 2 ports connected to the CPU
USB: no
Serial: yes, external (you need a null-modem cable)
JTAG: yes
Power over Ethernet: 18-24V
}}}

'''Installation'''

Press a key on bootup to enter the u-boot bootloader's console.

Set up the IP addresses:

{{{
setenv ipaddr 192.168.1.1
setenv serverip 192.168.1.254
}}}

Create script to flash !OpenWrt:
{{{
setenv flash_openwrt tftp 100000 openwrt-magicbox-squashfs.img\;erase \${kernel_addr} +\${filesize}\;cp.b \${fileaddr} \${kernel_addr} \${filesize}
}}}

Create the needed bootargs for !OpenWrt:

Magicbox 1.1:
{{{
setenv bootargs console=ttyS0,115200 root=/dev/mtdblock1 rootfstype=squashfs,jffs2 noinitrd init=/etc/preinit
}}}

Magicbox 2.0:
{{{
setenv bootargs console=ttyS0,115200 root=/dev/mtdblock1 rootfstype=squashfs,jffs2 noinitrd init=/etc/preinit
}}}

Set/clear the needed variables and save:

{{{
setenv ramdisk_addr
setenv flash_mem
setenv bootcmd bootm \${kernel_addr}
saveenv
}}}

Flash !OpenWrt and reset:
{{{
run flash_openwrt
reset
}}}

----
CategoryModel
