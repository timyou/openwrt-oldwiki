OpenWrtDocs/Hardware/SMC/SMV2804WBR

LAN - Ports up J2 (pin 1 on right top)
||<tablewidth="294px" tableheight="97px">GND || ? ||TX ||RX ||? ||
||<style="vertical-align: top;">3,3 V + ||<style="vertical-align: top;">? ||<style="vertical-align: top;">? ||<style="vertical-align: top;">? ||<style="vertical-align: top;">? ||


 . LED's down
Startup-log:
{{{ 


===========================================================
  LAN Router BRN Loader V1.3B build Mar 13 2003 18:23:41
                 Broad Net Technology, INC.
===========================================================

read(0)= 28 read(2)=59904
AMD Am29LV160DB bottom boot 16-bit mode found

Copying boot params.....DONE

Press any key to enter command mode ...

}}}

Menu at Command mode: 
{{{
======================
 [U] Upload to Flash  
 [E] Erase Flash      
 [G] Run Runtime Code 
 [A] Set MAC Address 
 [#] Set Serial Number 
 [V] Set Board Version 
 [S] Serial Test 
 [I] Parallel Test 
 [P] Print Boot Params 
======================
}}}

hidden tools:
c
{{{
print the following infos:

===============================================================
    [SYSTEM CONFIGURATION SPECIAL]                   
===============================================================
  * System Configuration Register     [SYSCFG] : [0x00000100] 
  * Product Code and Rev No.          [PDCODE] : [0x251000A0] 
  * Peri Cloclk Disable  Register    [PCLKDIS] : [0x00000000] 
  * Clock Status  Register             [CLKST] : [0xC0133166] 
  * AHB Bus Master Fixed Priority  Reg [HPRIF] : [0x76543210] 
  * AHB Bus Master Round-Robin Pri.Reg [HPRIR] : [0x00000000] 
  * Core PLL Configuration   Register   [CPLL] : [0x0001015C] 
  * System PLL Configuration Register   [SPLL] : [0x00010148] 
  * USB PLL Configuration    Register   [UPLL] : [0x000203B8] 
  * PHY PLL Configuration    Register   [PPLL] : [0x00030248] 
===============================================================
    [CP15 Register Map ]                   
===============================================================
  * CP15 : C0 ID Code                          : [0x41029402] 
  * CP15 : C0 Cache Type                       : [0x0F0F10F1] 
  * CP15 : C1 Control Register                 : [0xC0000079] 
  * CP15 : C2 Data Cacheable Register          : [0x00000022] 
  * CP15 : C2 Inst Cacheable Register          : [0x00000022] 
  * CP15 : C3 Data Bufferable  Register        : [0x000000FE] 
  * CP15 : C5 Data Access Permission  Register : [0x00000FFF] 
  * CP15 : C5 Inst Access Permission  Register : [0x00000FFF] 
===============================================================
  * CP15 : C6 Data Region0 Base/Size  Register : [0x0000003F] 
  * CP15 : C6 Data Region1 Base/Size  Register : [0x00000031] 
  * CP15 : C6 Data Region2 Base/Size  Register : [0x0040002B] 
  * CP15 : C6 Data Region3 Base/Size  Register : [0x80000025] 
  * CP15 : C6 Data Region4 Base/Size  Register : [0x81000029] 
  * CP15 : C6 Data Region5 Base/Size  Register : [0x84000027] 
  * CP15 : C6 Data Region6 Base/Size  Register : [0x00000008] 
  * CP15 : C6 Data Region7 Base/Size  Register : [0x00000008] 
===============================================================
  * CP15 : C6 Inst Region0 Base/Size  Register : [0x0000003F] 
  * CP15 : C6 Inst Region1 Base/Size  Register : [0x00000031] 
  * CP15 : C6 Inst Region2 Base/Size  Register : [0x0040002B] 
  * CP15 : C6 Inst Region3 Base/Size  Register : [0x80000025] 
  * CP15 : C6 Inst Region4 Base/Size  Register : [0x81000029] 
  * CP15 : C6 Inst Region5 Base/Size  Register : [0x84000027] 
  * CP15 : C6 Inst Region6 Base/Size  Register : [0x00000008] 
  * CP15 : C6 Inst Region7 Base/Size  Register : [0x00000008] 
===============================================================
}}}
z
Unzapping 
{{{
Unzipping program from bank 2...done
Unzipping program from bank 3...done


}}}

{{{  
Flash
--------------------------------------
      Area         Address     Length 
--------------------------------------
[0] Boot          0x00000000     128K
[1] Configuration 0x00020000      64K
[2] Web Image     0x00030000     192K
[3] Code Image    0x00060000     576K
[4] Params Area   0x000F0000      64K
--------------------------------------
}}}

Bootlog Original Firmware
{{{ 
Copying boot params.....DONE


Press any key to enter command mode ...

Flash Checking .. Passed.

Unzipping program from bank 2...done
Try to find image for running...
Unzipping program from bank 3...doneFlush I and D cache

GLOBAL_CTOR_BODY in gbl-ctors.h
nptrs : 0
__CTOR_LIST__[0]: 137f38, 0,     - ../../gcc/libgcc2.c 2874
__CTOR_LIST__[1]: 137f3c, 0,     - ../../gcc/libgcc2.c 2874
__CTOR_LIST__[2]: 137f40, 0,     - ../../gcc/libgcc2.c 2874
__CTOR_LIST__[3]: 137f44, 0,     - ../../gcc/libgcc2.c 2874
ATEXIT : e645c
[GPIO FLOW] SetGpio() Begin ..
System Hardware startup ...

[GPIO INIT] Initialize Chip Select Pin Setting ..
[GPIO] (_S3C2510) GPIO_init(): Set GPIO for Wireless LED and reset button !!
=== PCI BUS begin ....
[PCI FLOW] PCI_2510_Init() Begin ..
[PCI IRQ] PCI_2510_Init() Set nPCI_PCCARD=15 , ISR_PCI()
[ISR INIT] PCI_2510_Init() Set nPCI_PCCARD=15 , ISR_PCI()
[SSMAC] init handler table, handler= 73EF4H
[SSMAC] SysSetInterrupt: vector 15 handler 78E18H
[ISR INIT] PCI_2510_Initialize():  &INTMASK = F0140008H , INTMASK = 3FFFFFFFH
[ISR INIT] PCI_2510_Initialize(): Enable PCCARD_INT=9 ..
[ISR INIT] PCI_2510_Initialize():  &INTMASK = F0140008H , INTMASK = 3FFFFFFFH
[ISR INIT] PCI_2510_Initialize(): init handler ISR_PCI_Timer5_NormalOn()
[ISR INIT] nTIMER5 = 34 
[SSMAC] SysSetInterrupt: vector 34 handler 78DE8H
[ISR INIT] GLOBAL_INT = 31 
[ISR INIT] PCI_2510_Initialize():  &EXTMASK = F014000CH , EXTMASK = 8000003FH

---PCI_PCICON_View-------------------------------------    
[0]Host Mode,  
[1]Internal Arbitor,   
[4]ATS,    
[5]Split Response, 
[7]Mem Cycle Prefetchable, 
[8]Config. Done,   
[9]System Read Ready,  
[31]Internal Interrupt Signaled,   
---------------------------------------------------- 
[PCI] device(slot)= 0 memory virtual 00000000H , physical 02000000H 
[PCI]                PCI 02000008H 
[PCI] device(slot)= 0 memory virtual 00000000H , physical 01FFDE00H 
[PCI]                PCI 01FFDE08H 
[PCI] device(slot)= 0 I/O virtual DC0FFF00H , physical 000FFF00H 
[PCI]                PCI 000FFF01H 
[PCI] device(slot)= 4 memory virtual C1FFE000H , physical 01FFE000H 
[PCI]                PCI 01FFE000H 
_pci_map_io: bad request 
[GPIO FLOW] SetGpio() End.


Firmware occupies 0x00010050 ~ 0x003E8B80
DATA area is 15887 bytes from 0x0012925C to 0x00138A94
BSS area is 2818280 bytes from 0x00138A98 to 0x003E8B7C
Web SDRAM area is from 0X00760000H
in usrclk_init() 
usrclk_init() end 144b50 
usrclk_init() 2 end 144b50 
System startup...
soho initialize COLOR1 : 450000

read(0)= 28 read(2)=59904
AMD Am29LV160DB bottom boot 16-bit mode found
Set flash memory layout to Boot Parameters found !!!
Bootcode version: V1.3B
Serial number: A31800 
Hardware version: 01
sizeof(struct III_Config_t) is 60668
read(0)= 28 read(2)=59904
AMD Am29LV160DB bottom boot 16-bit mode found
default route: 0.0.0.0
BufferInit:
BUF_HDR_SZ=48 BUF_ALIGN_SZ=12 BUFFER_OFFSET=112
BUF_BUFSZ0=384 BUF_BUFSZ1=1632
NUM_OF_B0=0 NUM_OF_B1=1320
BUF_POOL0_SZ=0 BUF_POOL1_SZ=2217600
sizeof(BUFFER0)=432,sizeof(BUFFER1)=1680
*BUF0=0x00400000 *BUF1=0x00400010
Altgn *BUF0=0x00400000 *BUF1=0x00400010
End at BUF0:0x00400000, BUF1:0x0061d690

buffer0 pointer init OK!
buffer1 pointer init OK!
Interface 0 ip = 127.0.0.1

ssmac_init is called, ifno=1 descritpors tx 256 rx 256 
TX_NOCOPY is defined 
NO_TX_ISR is defined 
RX_NOCOPY is defined 

Lan channel 0 initialize Function
Mac channel 0 initialize Function[SSMAC] BDMA and MAC interrupt vector setup..
[SSMAC] SysSetInterrupt: vector 19 handler 74DD4H
[SSMAC] SysSetInterrupt: vector 18 handler 74D9CH
[SSMAC] SysSetInterrupt: vector 21 handler 74DF0H
[SSMAC] SysSetInterrupt: vector 20 handler 74DB8H
[SSMAC] Set the Initial condition of BDMA, MAC..
[SSMAC] Set the CAM Control register and the MAC address value
[SSMAC] Configure the BDMA and MAC control registers ..
[SSMAC] Enable interrupt Ethernet interrupt ..
[SSMAC] MacInitialize() End.
ssmac_init ends 
 Mac addr: 0004e27

MACifno: 1
Interface 1 ip = 192.168.2.1

ssmac_init is called, ifno=2 descritpors tx 256 rx 256 
TX_NOCOPY is defined 
NO_TX_ISR is defined 
RX_NOCOPY is defined 
Lan channel 1 initialize Function
Mac channel 1 initialize Function[SSMAC] BDMA and MAC interrupt vector setup..
[SSMAC] SysSetInterrupt: vector 19 handler 74DD4H
[SSMAC] SysSetInterrupt: vector 18 handler 74D9CH
[SSMAC] SysSetInterrupt: vector 21 handler 74DF0H
[SSMAC] SysSetInterrupt: vector 20 handler 74DB8H
[SSMAC] Set the Initial condition of BDMA, MAC..
[SSMAC] Set the CAM Control register and the MAC address value
[SSMAC] Configure the BDMA and MAC control registers ..
[SSMAC] Enable interrupt Ethernet interrupt ..
[SSMAC] MacInitialize() End.
ssmac_init ends 
 Mac addr: 0004e2
MACifno: 2
RUNTASK id=1 rdcemac_intserv_task...
iput_IpLinkUp(ifno=2)> ifp->add_default_route:1
Re-Init NAT data structure
Init NAT data structure
del_virtual_server_by_range> index=0, peer_addr=00000000

Interface 2 ip = 0.0.0.0

[PCI IS FLOW] hwlanPCI_init() Begin ..
[PCI 11G] islpci_probe : verdor id 38901260H 
[PCI 11G] islpci_probe : device id 38901260H 
[PCI 11G] islpci_probe : revision 2800001H 
[PCI 11G] islpci_probe : Master Timer 0000H 
io 01ffe000 irq 00000001 dev_id 00001260 
ISL3890 PCI Memory remapped to 0xC1FFE000 
PSM Buffer at 0x0261FAA0 size 98304
Queue memory base at 0x00637AA0 
Queue memory end at 0x00649AA0 

Unzipping from 800DBC00 to 00686000 ... done

Uncompressed size = 91484
firmware download : from 00686000 to c1fff000 len 1000 bcount 0
firmware download : from 00687000 to c1fff000 len 1000 bcount 1000
firmware download : from 00688000 to c1fff000 len 1000 bcount 2000
firmware download : from 00689000 to c1fff000 len 1000 bcount 3000
firmware download : from 0068a000 to c1fff000 len 1000 bcount 4000
firmware download : from 0068b000 to c1fff000 len 1000 bcount 5000
firmware download : from 0068c000 to c1fff000 len 1000 bcount 6000
firmware download : from 0068d000 to c1fff000 len 1000 bcount 7000
firmware download : from 0068e000 to c1fff000 len 1000 bcount 8000
firmware download : from 0068f000 to c1fff000 len 1000 bcount 9000
firmware download : from 00690000 to c1fff000 len 1000 bcount a000
firmware download : from 00691000 to c1fff000 len 1000 bcount b000
firmware download : from 00692000 to c1fff000 len 1000 bcount c000
firmware download : from 00693000 to c1fff000 len 1000 bcount d000
firmware download : from 00694000 to c1fff000 len 1000 bcount e000
firmware download : from 00695000 to c1fff000 len 1000 bcount f000
firmware download : from 00696000 to c1fff000 len 1000 bcount 10000
firmware download : from 00697000 to c1fff000 len 1000 bcount 11000
firmware download : from 00698000 to c1fff000 len 1000 bcount 12000
firmware download : from 00699000 to c1fff000 len 1000 bcount 13000
firmware download : from 0069a000 to c1fff000 len 1000 bcount 14000
firmware download : from 0069b000 to c1fff000 len 1000 bcount 15000
firmware download : from 0069c000 to c1fff000 len 1000 bcount 16000
firmware download : from 0069d000 to c1fff000 len 318 bcount 17000

Firmware write complete ...total len = 17318

isl38xx_upload_firmware() return ...
[ISR INIT] HwEnable_nGLOBAL_INT() : GLOBAL_INT = 31 
[ISR INIT] HwEnableAllInt() :  &EXTMASK = F014000CH , EXTMASK = 0000003FH
[ISR INIT] HwEnableAllInt(): Enable PCCARD_INT=9 ..
[ISR INIT]  HwEnableAllInt():  &INTMASK = F0140008H , INTMASK = 3EFFFFFFH
[ISR INIT]  HwEnableAllInt():  &INTMOD = F0140000H , INTMOD = 00000000H
[ISR INIT]  HwEnableAllInt():  &INTMASK = F0140008H , INTMASK = 3EFFFDFFH
[ISR INIT]  HwEnableAllInt():  &EXTTMOD = F0140004H , EXTMOD = 00000000H
[ISR INIT] HwEnableAllInt() :  &EXTMASK = F014000CH , EXTMASK = 0000003FH
[HWLAN 11G] ifno=4 Card=0 : hwlan_init()
[PCI 11G] hwlanPCI_init() set ifp flag .. 
[HWLAN INIT] hwlan_ioctl() start.. 
Interface 4 ip = 192.168.2.1

[HWLAN INIT] hwlan_ioctl() start.. 
ruleCheck()> Group: 0,  Error: Useless rule index will be truncated
ruleCheck()> Group: 1,  Error: Useless rule index will be truncated
ruleCheck()> Group: 2,  Error: Useless rule index will be truncated
CBAC rule format check succeed !!
reqCBACBuf()> init match pool, Have: 1000
Memory Address: 0x003c51d0 ~ 0x003cbf4c
reqCBACBuf()> init timeGap pool, Have: 10000
Memory Address: 0x00655200 ~ 0x00685f54
reqCBACBuf()> init sameHost pool, Have: 2000
Memory Address: 0x003cbf50 ~ 0x003db970
CBAC rule pool initialized !!

Init NAT data structure
RUNTASK id=2 if_task if0...
RUNTASK id=3 if_task if1...
RUNTASK id=4 if_task if2...
RUNTASK id=5 if_task if4...
RUNTASK id=6 timer_task...
RUNTASK id=7 conn_mgr...
RUNTASK id=8 main_8021x...
RUNTASK id=9 period_task...
RUNTASK id=10 dhcp_daemon...
RUNTASK id=11 dhcp_clt...on interface 2
RUNTASK id=12 pptp_callmgr...
httpd: listen at 192.168.2.1:1900
HTTPD TIMER_RESOURCE:5, FS_RESOURCE:6
RUNTASK httpd...
RUNTASK id=16 dnsproxy...
RUNTASK id=17 dhcpd_mgmt_task...
UPnP is disabled
Intersil firmware version: 1.0.2.0
aLinkState: 0x0, sys_time=4
[HWLAN INIT] MAC addr=00-04-e2
aMaxFrameBurst: 250 usec
aFixedRate: 255 255 255 255
