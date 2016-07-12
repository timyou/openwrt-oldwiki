'''SHmin'''

This board is also known as TAC Inc. SH7706LAN or T-SH7706LAN. It is is a very minimal board only enough to experiment with the SH3 platform, however, there are rumours about hacking an LCD onto the expansion pins and playing Doom on it.

 * Bootloader: MES 2.3 Rev12 (Micro Embedded System)
 * CPU: SH7706 @ 133MHz (SH3)
 * Flash size: 512KByte
 * RAM: 8 - 32 MByte
 * Ethernet: RTL8019AS
 * Serial: Yes, via a DB9 connector
 * JTAG: yes, 14-pin U-HDI
 * Other: MMC slot
 * Expansion pins: Yes, check [http://trash.uid0.hu/openwrt/sh/T-SH7706LAN3.pdf here]

Different versions of this board exists, most of them are equipped with 8 MByte memory, only rev. 3.0 is equipped with 32 MByte.

Serial console settings are 115200 baud, 8n1, but the terminal software has to be configured to add a linefeed after a carriage return. Hyperterminal is known to be working with these, minicom does not yet correctly.

The flash contains a minimal number of files, namely config.sys, boot.exe and shell.exe. The first contains a few init parameters, the second will boot our vmlinux file from the MMC card, the third is the shell You are currently in.

NOTE: MES supports only FAT12 partitions on the MMC, so if you try to take a card from a phone or a digital camera, it has to be repartitioned and reformatted first, otherwise mounting it will result in an 'ERROR[Disk I/O error.]'

The MMC card has to be mounted first, with 'mount mmc0'. After successful mounting, You can try to run 'boot.exe', which loads the vmlinux file from the mmc, and if the kernel is correct, it will begin booting.


NOTE: This wiki entry will be changing quickly as I'm playing around with OpenWrt to support this board.
