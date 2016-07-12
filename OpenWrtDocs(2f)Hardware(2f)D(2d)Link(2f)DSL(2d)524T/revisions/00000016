= D-LINK DSL-524T =

edited by [http://guidoserra.it Guido Serra]

this webpage was created to add more details about that ["OpenWrtDocs/Hardware/D-Link/DSL-502T"]

= differences =

== Specifications ==
ADSL modem with ADSL2/2+ support to 24Mbit/s+, it has port 4 LAN ports

Flash chip: 32MBytes - [http://www.spansion.com/products/S29AL032D.html Spansion S29AL032D90TFI04]

SDRAM: 128Mb syncronous DRAM - 2M x 4Bank x16 I/O - HYNIX HY57V281620ETP-H

CPU: TNETD7300AZDW (6BZHT99) Texas Instruments AR7 MIPS based

== bootloader ==

ip address for adam2 bootloader is 5.8.8.8 (instead of 10.8.8.8 like it was for DSL-502T)

the dump of the adam2 env:
{{{
fork:~ zeph$ telnet 192.168.1.1
Trying 192.168.1.1...
Connected to mygateway1.ar7.
Escape character is '^]'.
BusyBox on (none) login: admin
Password:
BusyBox v0.61.pre (2006.02.09-03:06+0000) Built-in shell (ash)
Enter 'help' for a list of built-in commands.
# cat /proc/ticfg/env
memsize 0x01000000
flashsize       0x00400000
modetty0        38400,n,8,1,hw
modetty1        38400,n,8,1,hw
bootserport     tty0
cpufrequency    150000000
sysfrequency    125000000
bootloaderVersion       0.22.02
Adam2_Release   0.22.02_b04_Mar 10 2005
ProductID       AR7RD
HWRevision      Unknown
SerialNumber    N/A
my_ipaddress    5.8.8.8
prompt  Adam2_AR7RD
firstfreeaddress        0x9401d888
req_fullrate_freq       125000000
maca    00:19:5B:79:16:E8
mtd0    0x90091000,0x903f0000
mtd1    0x90010090,0x90090000
mtd2    0x90000000,0x90010000
mtd3    0x903f0000,0x90400000
mtd4    0x90010000,0x903f0000
autoload        1
autoload_timeout        7
StaticBuffer    120
SW_FEATURES     0X8000
vcc_encaps0     0.0
vcc_encaps1     0.0
vcc_encaps2     0.0
vcc_encaps3     0.0
vcc_encaps4     0.0
vcc_encaps5     0.0
vcc_encaps6     0.0
vcc_encaps7     0.0
modulation      0xffff
usb_vid 0x0
usb_pid 0x0
usb_man N/A
usb_prod        N/A
eoc_vendor_id   DLink
enable_margin_retrain   1
eoc_vendor_serialnum    N/A
eoc_vendor_revision     20060209
# Connection closed by foreign host.
fork:~ zeph$
}}}

== Flashing the new firmware ==

as for DSL-502T check the memory mapping

openwrt-ar7-2.4-squashfs.bin goes to mtd4

and it has... 0x00076B80 as result of searching hsqs with the hexeditor 

(THIS IS VALID JUST FOR my binary compiled ad described in the page for the DSL-502T)

||||||||<style="text-align: center;">'''Custom memory map for OpenWRT''' ||
||Name ||Start ||End ||Description ||
||mtd0 ||{{{0x90086B80}}} ||{{{0x903f0000}}} ||Filesystem ||
||mtd1 ||{{{0x90010000}}} ||{{{0x90086B80}}} ||Kernel ||
||mtd2 ||{{{0x90000000}}} ||{{{0x90010000}}} ||bootloader ||
||mtd3 ||{{{0x903f0000}}} ||{{{0x90400000}}} ||config ||
||mtd4 ||{{{0x90010000}}} ||{{{0x903f0000}}} ||Kernel + FS ||

so... edit adam2

{{{
USER adam2
PASS adam2
quote "SETENV mtd0,0x90086B80,0x903f0000" (fs)
quote "SETENV mtd1,0x90010000,0x90086B80" (kernel)
quote "SETENV mtd4,0x90010000,0x903f0000" (fs+kernel)
}}}

and flash it!

{{{
quote "MEDIA FLSH"
binary
debug
hash
put "openwrt-ar7-2.4-squashfs.bin" "c mtd4"
quote REBOOT
quit
}}}

{{{
fork:~ zeph$ telnet 192.168.1.1
Trying 192.168.1.1...
Connected to 192.168.1.1.
Escape character is '^]'.
 === IMPORTANT ============================
  Use 'passwd' to set your login password
  this will disable telnet and enable SSH
 ------------------------------------------


BusyBox v1.4.0 (2007-10-16 18:03:36 CEST) Built-in shell (ash)
Enter 'help' for a list of built-in commands.

  _______                     ________        __
 |       |.-----.-----.-----.|  |  |  |.----.|  |_
 |   -   ||  _  |  -__|     ||  |  |  ||   _||   _|
 |_______||   __|_____|__|__||________||__|  |____|
          |__| W I R E L E S S   F R E E D O M
 KAMIKAZE (bleeding edge, r6250) -------------------
  * 10 oz Vodka       Shake well with ice and strain
  * 10 oz Triple sec  mixture into 10 shot glasses.
  * 10 oz lime juice  Salute!
 ---------------------------------------------------
root@OpenWrt:/# 
}}}
