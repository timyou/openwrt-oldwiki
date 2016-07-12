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

Set up a tftp server and use these commands over serial console:

{{{
erase 0xffc00000 fffbffff
setenv ipaddr [ip for the magicbox]
setenv serverip [tftp server ip]
tftp 100000 openwrt-magicbox-2.6-squashfs.img
cp.b 0x100000 0xffc00000 [size of the image in hex, the bootloader prints it after the tftp]
setenv openwrt setenv bootargs console=ttyS1,115200 root=/dev/mtdblock1 rootfstype=squashfs,jffs2 noinitrd init=/etc/preinit\;bootm \$(kernel_addr)
setenv bootcmd run openwrt
saveenv
reset
}}}


----
CategoryModel
