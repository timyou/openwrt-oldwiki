[[TableOfContents]]

== Specifications ==
ADSL modem with ADSL2/2+ support to 24Mbit/s+, it has port 1 LAN port.

STAR-NET ADSL 2110EHR V7.0+

PCB: 2110EH V7.0 2005.1.28

PCB Photo:
[[ImageLink(2110EH_V700_2005_1_28.jpg,2110EH_V700_2005_1_28.jpg,width=400)]]

serial console 9600,n,8,1,hw jp1:

1 VCC 2 TX 3 RX 4 -- 5-- 6 GND 7 GND

Flash chip: 2MBytes Macronix MX29LV160CBTC-70 29LV160CBTC 29LV160 http://www.datasheet.org.uk/pdf/29lv160cbtc-70-datasheet/29lv160cbtc-70-datasheet.html

SDRAM: 8Mbytes Samsung K4S641632H-UC75 4M x 4Bit x 4 / 2M x 8Bit x 4 / 1M x 16Bit x 4 Banks Synchronous DRAM http://www.alldatasheet.com/datasheet-pdf/pdf/118300/SAMSUNG/K4S641632H-UC75.html

CPU: Texas Instruments AR7 MIPS based TI TNETD7300AGDW TNETD7300

http://focus.ti.com/general/docs/bcg/bcgprodcontent.tsp?templateId=6116&navigationId=12111&contentId=4001

http://focus.ti.com/pdfs/bcg/ar7_prod_bulletin.pdf

== Add USB BUS ==
Add type B female USB connector & 2N7002 Transistor

Photo connector&Transistor installed :
[[ImageLink(Add_Usb.jpg,Add_Usb.jpg,width=400)]]

== Jtag CPU pin-out ==
TNETD7300A TCK A20 TMS A21 TDO A22 TDI B20

== Information ==
{{{
# cat /proc/iomem
00000000-13ffffff : reserved
14000000-1401ffff : System RAM
14020000-147fffff : System RAM
  14020000-1418c07f : Kernel code
  1419d300-141bafff : Kernel data
a8610000-a86107ff : eth0
# cat /proc/mounts
/dev/mtdblock/0 / squashfs ro 0 0
none /dev devfs rw 0 0
proc /proc proc rw 0 0
ramfs /var ramfs rw 0 0
# cat /proc/tty/driver/serial
serinfo:1.0 driver:5.05c revision:2001-07-08
0: uart:16550A port:A8610E00 irq:15 baud:2258 tx:10869 rx:0 RTS|DTR
1: uart:16550A port:A8610F00 irq:16 tx:0 rx:0 RTS|DTR
# cat /proc/cpuinfo
processor               : 0
cpu model               : MIPS 4KEc V4.8
BogoMIPS                : 149.91
wait instruction        : no
microsecond timers      : yes
extra interrupt vector  : yes
hardware watchpoint     : yes
VCED exceptions         : not available
VCEI exceptions         : not available
# cat /proc/mtd
dev:    size   erasesize  name
mtd0: 00160000 00010000 "mtd0"
mtd1: 00080000 00010000 "mtd1"
mtd2: 00010000 00008000 "mtd2"
mtd3: 00010000 00010000 "mtd3"
mtd4: 001e0000 00010000 "mtd4"
# cat /proc/version
Linux version 2.4.17_mvl21-malta-mips_fp_le (root@localhost.localdomain) (gcc version 2.95.3 2001031
5 (release/MontaVista)) #1 &#9562;¤ 3&#9560;&#9516; 9 15:28:39 CST 2005
# cat /proc/avalanche/avsar_ver
ATM Driver version:[4.03.03.00]
DSL HAL version: [3.02.00.03]
DSP Datapump version: [3.02.06.00] Annex A
SAR HAL version: [01.07.02]
PDSP Firmware version:[0.49]
# cat /proc/avalanche/cpmac_ver
Texas Instruments CPMAC driver version: 1.5
Texas Instruments CPMAC HAL version: CPMAC 01.07.08 Mar  9 2005 15:29:27
# cat /proc/avalanche/psp_version
Linux OS DSL-PSP version 4.3.0.5 on BasePSP Version 5.7.6.12  Mar  9 2005 15:33:28
Avalanche SOC Version: 0x250005 operating in cached, write back, write allocate mode
Cpu Frequency:150 MHZ
System Bus frequency: 125 MHZ
# cat /proc/avalanche/usb0_ver
Texas Instruments USB CDC/RNDIS Driver Version 1.1.0
Built for RNDIS protocol(s).
}}}
== ACORP LAN120 firmware ==
Dont Flash ACORP firmware. Yet do not replace boot loader on pspboot.

http://mcmcc.bat.ru/acorp/psp_boot/psp_boot_LAN120_2M_8M-1.4.rar

Change boot loader to PSPboot

{{{
# cd /var/var
# tftp -g -l psp_boot_LAN120_2M_8M-1.4.bin 192.168.0.90
# cat psp_boot_LAN120_2M_8M-1.4.bin > /dev/mtdblock/2
}}}
http://mcmcc.bat.ru/acorp/LAN120/Acorp_nsp_LAN120_V.1.1.00.RU.23102007_AnnexA_DSP74.zip

Web login/password: Admin Admin Telnet login/password: root Admin

Add mtd5 and change mtd0 & mtd4

{{{
# echo "mtd5 0x901F0000,0x90200000" > /proc/ticfg/env
# echo "mtd4 0x90020000,0x901F0000" > /proc/ticfg/env
# echo "mtd0 0x90094000,0x901F0000" > /proc/ticfg/env
}}}
tftpd32 for Windows

{{{
http://tftpd32.jounin.net/
}}}
TX & RX led fix:

{{{
# cd /var/var
# tftp -g -l mycfg.tar.gz_blink_on_lan 192.168.0.90
# cat mycfg.tar.gz_blink_on_lan > /dev/mtdblock/5
}}}
attachment:mycfg.tar.gz_blink_on_lan file size 759

http://mcmcc.bat.ru/acorp/env_db/env_lan120.txt

{{{
mtd0 0x90094000,0x901F0000
mtd1 0x90020090,0x90094000
mtd2 0x90000000,0x90010000
mtd3 0x90010000,0x90020000
mtd4 0x90020000,0x901F0000
mtd5 0x901F0000,0x90200000
}}}
== WatchDog Enable ==
{{{

CPU revision is: 00018448 (MIPS 4KEc)
bootcr 7300 is 0x2514281
TI AR7 (TNETD7300), ID: 0x0005, Revision: 0x27
0x2514281 100101000101000010100-0-0001 disable
R59 connected between pin17 flash and Vcc(+3,3v)
After change R59 place
0x2514291 100101000101000010100-1-0001 enable!
R59 connected between pin17 flash and GND

}}}
attachment:enable_watchdog.jpg

----

 . CategoryModel ["CategoryAR7Device"]
 . CategoryDslModems
