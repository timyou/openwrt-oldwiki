'''Buffalo WHR-G54S'''

The device is supported in OpenWrt White Russian. You need to install the openwrt-brcm-2.4-<type>.trx firmware images.

If you have a newer hardware revision (this being written on 8/21/2006), you should use the current SVN, as there are some bricking issues on older builds of OpenWrt.

{{{
System-On-Chip:  Broadcom 5352
CPU Speed: 200 Mhz
Flash size: 4 MB
RAM: 16 MB
Wireless: Broadcom (integrated)
Switch: in CPU
Serial: yes
JTAG: yes
USB: no
}}}

The boot_wait NVRAM variable is '''on''' by default. 

You need to use TFTP installation, as the web interface expects an encrypted file (with the .enc extension), and it will not work.

'''TFTP installation notes'''

This device is based on the Broadcom chipset so the openwrt-brcm-<t<pe>.trx image is required. Pull the power plug, press and hold the reset ("INIT") button, start the TFTP, plug the power back in, and let go of the button. The power light does *not* flash on this unit, but the diag does. This unit keeps the IP address that it was set to while in this mode. Factory setting is 192.168.11.1.

TFTP commands:

{{{
tftp 192.168.11.1
tftp> binary
tftp> trace
tftp> rexmt 1
tftp> timeout 60
tftp> put openwrt-xxx-x.x-xxx.trx
}}}

After this, wait for the device to reboot and you should be set. You should be able to telnet to 192.168.11.1 or whatever the unit was set to prior to the installation.

----
CategoryModel CategoryModel
