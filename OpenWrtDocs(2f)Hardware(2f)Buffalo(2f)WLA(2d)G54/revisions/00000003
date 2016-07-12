'''Buffalo WLA-G54'''

The router is supported in OpenWrt 1.0 (White Russian) and later. You need to install the openwrt-brcm-2.4-<type>.trx firmware images.

{{{
Bootloader: unknown
System-On-Chip:  Broadcom 4710
CPU Speed: 125 Mhz
Flash size: 4 MB
RAM: 16 MB
Wireless: Mini-PCI
Ethernet: Robo switch BCM5325e
Serial: no
JTAG: no
}}}

The boot_wait NVRAM variable is on by default. Resetting to factory defaults via reset button or mtd erase nvram is '''not save''' on this unit.

'''TFTP installation notes'''

This device is based on the Broadcom chipset so the openwrt-brcm-<t<pe>.trx image is required. The web interface will not allow you to install the openwrt firmware so you will need to use tftp. Pull the power plug, press and hold the reset button, plug the device and wait until the PWR LED starts flashing slowly (almost immediately). Now release the reset button and upload the firmware. This unit keeps the IP address that it was set to whilst in this mode. Factory setting is 192.168.11.2.

TFTP commands:

{{{
tftp 192.168.11.2
tftp> binary
tftp> trace
tftp> rexmt 1
tftp> timeout 60
tftp> put openwrt-xxx-x.x-xxx.trx
}}}

After this, wait until the PWR LED stops flashing and the device to reboot and you should be set. You should be able to telnet to 192.168.11.2 or whatever the unit was set to prior to the installation.

----
CategoryModel
