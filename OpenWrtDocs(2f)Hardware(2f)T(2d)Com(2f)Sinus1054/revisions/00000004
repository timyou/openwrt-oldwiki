= Chipset =
The Sinus 1054 is based on the Broadcom BCM 6345 KPB chip. It is OEM Product produced by Hitachi for Deutsche Telekom.

== Hardware Parts used ==
attachment:sin1054.jpg

Devices on top of the board are:
||<tablewidth="410px">Amount ||Type ||
||1 ||BCM4306KFB ||
||1 ||MX29LV320ATTC-70 ||
||1 ||BCM6345KPB ||
||1 ||Samsung K4S641632H-TC75 ||


= Serial =
Serial connector is marked with J502 name. Location is following

 . WLAN Slot
VCC TX GND RX

 . LEDS
= Boot Loader =
The bootload used is Broadcom CFE:

----
{{{
CFE> help
Available commands:
w                   Write the whole image start from beginning of the flash
e                   Erase [n]vram or [a]ll flash except bootrom
r                   Run program from flash image or from host depend on [f/h] flag
p                   Print boot line and board parameter info
c                   Change booline parameters
f                   Write image to the flash
i                   Erase persistent storage data
b                   Change board parameters
reset               Reset the board
flashimage          Flashes a compressed image after the bootloader.
help                Obtain help for CFE commands
For more information about a command, enter 'help command-name'
*** command status = 0
CFE>
}}}
----
= Sinus 1054 Bootlog =
The only thing changed in the bootlog is the mac address. Other parts are as is from the original Sinus 1054 Firmware:

----
{{{
CFE version 1.0.37-5.6 for BCM96345 (32bit,SP,BE)
Build Date: Tue Nov 16 20:48:23 CST 2004 (root@weiyu.tecom.com.tw)
Copyright (C) 2000,2001,2002,2003 Broadcom Corporation.
Initializing Arena.
Initializing Devices.
Auto-negotiation timed-out
CPU type 0x28000: 140MHz
Total memory used by CFE:  0x80401000 - 0x805210D0 (1179856)
Initialized Data:          0x8041BA80 - 0x8041D4E0 (6752)
BSS Area:                  0x8041D4E0 - 0x8041F0D0 (7152)
Local Heap:                0x8041F0D0 - 0x8051F0D0 (1048576)
Stack Area:                0x8051F0D0 - 0x805210D0 (8192)
Text (code) segment:       0x80401000 - 0x8041BA80 (109184)
Boot area (physical):      0x00522000 - 0x00562000
Relocation Factor:         I:00000000 - D:00000000
Board IP address                : 192.168.1.1:ffffff00
Host IP address                 : 192.168.1.100
Gateway IP address              : 192.168.1.100
Run from flash/host (f/h)       : f
Default host run file name      : vmlinux
Default host flash file name    : bcm963xx_fs_kernel
Boot delay (0-9 seconds)        : 9
Board Id Name                   : 96345GW2
Psi size in KB                  : 16
Number of MAC Addresses (1-32)  : 11
Base MAC Address                : XX:XX:XX:XX:XX:XX
Ethernet PHY Type               : Internal
Memory size in MB               : 8
*** Press any key to stop auto run (9 seconds) ***
Auto run second count down: 0
Code Address: 0x80010000, Entry Address: 0x8001046c
Decompression OK!
Entry at 0x8001046c
Closing network.
Starting program at 0x8001046c
Total Flash size: 4096K with 71 sectors
96345GW2 prom init
CPU revision is: 00028000
Primary instruction cache 8kb, linesize 16 bytes (2 ways)
Primary data cache 4kb, linesize 16 bytes (2 ways)
Linux version 2.4.17 (root@linux) (gcc version 3.1) #377 Sun Nov 13 06:38:30 CET 2005
Determined physical RAM map:
 memory: 007a0000 @ 00000000 (usable)
On node 0 totalpages: 1952
zone(0): 1952 pages.
zone(1): 0 pages.
zone(2): 0 pages.
Kernel command line: root=/dev/mtdblock0 rw
bcm_console_setup
Calibrating delay loop... 92.97 BogoMIPS
Memory: 6268k/7808k available (1067k kernel code, 1540k reserved, 76k data, 40k init, 0k highmem)
Dentry-cache hash table entries: 1024 (order: 1, 8192 bytes)
Inode-cache hash table entries: 512 (order: 0, 4096 bytes)
Mount-cache hash table entries: 512 (order: 0, 4096 bytes)
Buffer-cache hash table entries: 1024 (order: 0, 4096 bytes)
Page-cache hash table entries: 2048 (order: 1, 8192 bytes)
Checking for 'wait' instruction...  unavailable.
POSIX conformance testing by UNIFIX
Linux NET4.0 for Linux 2.4
Based upon Swansea University Computer Society NET3.039
Initializing RT netlink socket
Starting kswapd
brcmboard: brcm_board_init entry
Module bcm63xx_cons.c v1.1 Apr 30 2005 17:39:52
block: 64 slots per queue, batch=16
PPP generic driver version 2.4.1
NET4: Linux TCP/IP 1.0 for NET4.0
IP Protocols: ICMP, UDP, TCP
IP: routing cache hash table of 512 buckets, 4Kbytes
TCP: Hash tables configured (established 512 bind 1024)
NET4: Unix domain sockets 1.0/SMP for Linux NET4.0.
NET4: Ethernet Bridge 008 for NET4.0
VFS: Mounted root (cramfs filesystem).
Freeing unused kernel memory: 40k freed
init started:  BusyBox v0.60.4 (2005.11.12-18:12+0000) multi-call binary
Algorithmics/MIPS FPU Emulator v1.5
mount: Mounting devpts on /dev/pts failed: No such device
Terminated
BusyBox v0.60.4 (2005.11.12-20:53+0000) Built-in shell (ash)
Enter 'help' for a list of built-in commands.
sh: can't access tty; job control turned off
Loading drivers and kernel modules...
[28] Jan 01 00:00:06 Running in background
atmapi: init_module entry 0xc0002060
blaadd: blaa_detect entry
adsl: adsl_init entry
var 1.0 initialised
Broadcom BCM6345A0 Ethernet Network Device v0.1 Dec  7 2004 16:50:17 Internal PHY
BCM6345_ENET: Auto-negotiation timed-out
BCM6345_ENET: 10 MB Half-Duplex (assumed)
eth0: MAC Address: 00:03:C9:6D:FD:E9
[: S: unknown operand
kille
killall: inetd: no process killed
Device
WLAN hardware configuration BE_PCMCIA EBI_DMA
wl0: Broadcom BCM4320 802.11 Wireless Controller 3.61.13.0
nein
SPI ist nicht da
BcmAdsl_Initialize=0xC00144A8, g_pFnNotifyCallback=0xC0025290
AdslCoreHwReset: AdslOemDataAddr = 0xA07DCC04
atmctl: ATM driver return code, memory allocation error
atmctl: ATM driver return code, state error
atmctl: ATM driver return code, state error
atmctl: invalid vcc address '0.1.32'
S
/bin/inetd
Device
nein
SPI ist nicht da
==>   Bcm963xx Software Version: 2.14L.02DT1650_120704.BA09b6e   <==
S
/bin/inetd
Device
nein
SPI ist nicht da
device wl0 entered promiscuous mode
br0: port 1(wl0) entering listening state
br0: port 1(wl0) entering learning state
br0: port 1(wl0) entering forwarding state
br0: topology change detected, propagating
device eth0 entered promiscuous mode
br0: port 2(eth0) entering listening state
br0: port 2(eth0) entering learning state
br0: port 2(eth0) entering forwarding state
br0: topology change detected, propagating
pvc2684d: Interface "nas33" created sucessfully
atm_connect (TX: cl 1,bw 0-0,sdu 1524; RX: cl 1,bw 0-0,sdu 1524,AAL 5)
blaadd: open error -125
pvc2684d: Communicating over ATM 0.1.32, encapsulation: LLC
device nas33 entered promiscuous mode
br0: port 3(nas33) entering listening state
br0: port 3(nas33) entering learning state
br0: port 3(nas33) entering forwarding state
br0: topology change detected, propagating
}}}
----
 . CategoryModel ["CategoryBCM63xx"]
