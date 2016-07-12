== Specifications ==
ADSL modem with ADSL2/2+ support to 24Mbit/s+, it has port 1 LAN port.

PCB: 2110EH V7.20+ 2005.11.30

Flash chip: 2MBytes
KH KH29LV160CBTC-70G

SDRAM: 8Mbytes
Winbound W9864G6GH-6
W9864G6GH 4Mx16 4 Banks CL3 3.3 V TSOP II 54 (400 mil) -6 166 MHz
http://www.winbond-usa.com/mambo/content/view/123/238/

CPU: Texas Instruments AR7 MIPS based
TI TNETD7100GDW 
http://focus.ti.com/general/docs/bcg/bcgprodcontent.tsp?templateId=6116&navigationId=12111&contentId=4001
http://focus.ti.com/pdfs/bcg/ar7_prod_bulletin.pdf

== Original settings ==

The Flash memory is divided into blocks:
||||||||<style="text-align: center;">'''Default memory mappings''' ||
||Name ||Start ||End ||Description ||
||mtd0 ||0x90096000 ||0x90200000 ||Filesystem ||
||mtd1 ||0x90020090 ||0x90096000 ||Kernel ||
||mtd2 ||0x90000000 ||0x90010000 ||Bootloader ||
||mtd3 ||0x90010000 ||0x90020000 ||Configuration ||
||mtd4 ||0x90020000 ||0x90200000 ||Filesystem + Kernel ||

== Dump Original Firmware ==

{{{
# mkdir /var/dump 
# /usr/sbin/thttpd -d /var/dump -u root -p 1080 -g 
# dd if=/dev/mtdblock/2 of=/var/dump/mtd2-pspboot.bin 
http://192.168.1.1:1080/mtd2-pspboot.bin 
reboot 

# mkdir /var/dump 
# /usr/sbin/thttpd -d /var/dump -u root -p 1080 -g 
# dd if=/dev/mtdblock/3 of=/var/dump/mtd3-nvram.bin 
http://192.168.1.1:1080/mtd3-nvram.bin 
reboot 

# mkdir /var/dump 
# /usr/sbin/thttpd -d /var/dump -u root -p 1080 -g 
# dd if=/dev/mtdblock/4 of=/var/dump/mtd4-fs-kern1.bin skip=983040 count=983040 bs=1 
http://192.168.1.1:1080/mtd4-fs-kern1.bin 
reboot 

# mkdir /var/dump 
# /usr/sbin/thttpd -d /var/dump -u root -p 1080 -g 
# dd if=/dev/mtdblock/4 of=/var/dump/mtd4-fs-kern2.bin count=983040 bs=1 
# http://192.168.1.1:1080/mtd4-fs-kern2.bin 
reboot 
}}}

copy /b mtd4-fs-kern1.bin + mtd4-fs-kern2.bin mtd4-fs-kern.bin 

----
 . ["CategoryAR7Device"]
