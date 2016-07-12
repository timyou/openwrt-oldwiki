## Please edit system and help pages ONLY in the moinmaster wiki! For more
## information, please see MoinMaster:MoinPagesEditorGroup.
##acl MoinPagesEditorGroup:read,write,delete,revert All:read
##master-page:HelpTemplate
##master-date:Unknown-Date
#format wiki
#language en
== Prestige 645 ==
Single ethernet port ADSL router.

=== Status ===
Info Entered

=== Hardware ===
|| Component || Type || Hardware ||
|| CPU || ARM || SAMSUNG S3C4510X01 ||
|| RAM || 8MB || ||
|| FLASH || 1MB || INTEL TE28F800 ||
|| MODEM || ADSL ||Alcatel DynaMiTe ||
|| ETHERNET || 10/100MB || ||
=== Serial Console ===
TTL level serial cable on board. Labeled J1

Counting from the edge nearest the board.

{{{
1 - gnd
2 - missing (chopped off pin)
3 - receive data
4 - transmit data
5 - +3.3v (not sure about this)
}}}
I used a USB mobile phone data cable (Prolific PL2303)

==== MiniCom ====
Linux : Minicom 57600  8N1

Macosx : ZTerm 57600  8N1

=== Boot ===
Step 1

{{{
Bootbase Version: V2.07 | 3/15/2002 14:29:16
RAM: Size = 8192 Kbytes
DRAM POST: Testing:  8192K OK
FLASH: Intel 8M
ZyNOS Version: V2.50(EI.2) | 3/28/2002 13:30:26
Press any key to enter debug mode within 3 seconds.
.................
Enter Debug Mode
}}}
Step 2

{{{
Copyright (c) 1994 - 2002 ZyXEL Communications Corp.
initialize ch =0, ethernet address: 00:a0:c5:48:a6:31
HWSAR (FPGA) : testing ... done
Wan Channel init ........ done
Loading ADSL modem F/W
................................................................. done
Press ENTER to continue...
}}}
=== Enabling privileged commands ===
See [:OpenWrtDocs/Hardware/ZyXEL/Prestige 660HW-61:ZyXEL Prestige 660HW-61]

=== Memory layout ===
Bootbase provides a powerful flashing/debugging console, for instance, the ATMP command shows us how is the memory allocated. Later on, you can use the ATDUx,y command to dump memory contents starting at x plus an y offset:

{{{
OMIO image start at 06008000
code version:
code start: 00000100
code length: F7456
memMapTab: 14 entries, start = 02020000, checksum = FC21
$RAM Section:
  0: BootExt(RAMBOOT), start=00000100, len=17F00
  1: HTPCode(RAMCODE), start=00020000, len=10000
  2: RasCode(RAMCODE), start=00020000, len=1E0000
$ROM Section:
  3: BootBas(ROMIMG), start=02000000, len=4000
  4: DbgArea(ROMIMG), start=02004000, len=2000
  5: RomDir2(ROMDIR), start=02006000, len=2000
  6: BootExt(ROMIMG), start=02008030, len=10FD0
  7: HTPCode(ROMBIN), start=02019000, len=7000
     (Compressed)
     Version: HTP_P645 V 1.00, start: 02019030
     Length: 98D0, Checksum: 2ABE
     Compressed Length: 54A4, Checksum: 8474
  8: MemMapT(ROMMAP), start=02020000, len=C00
9: termcap(ROMIMG), start=02020c00, len=400
 10: parinit(ROMIMG), start=02021000, len=500
 11: swnt(ROMBIN), start=02021500, len=35B00
     (Compressed)
     Version: ADSL ATU-R, start: 02021530
     Length: 4F8C0, Checksum: C3FE
     Compressed Length: 32CE3, Checksum: 7A8F
 12: xhsar(ROMIMG), start=02057000, len=3000
 13: RasCode(ROMBIN), start=0205a000, len=A6000
     (Compressed)
     Version: P645 ATU-R, start: 0205a030
     Length: 129E34, Checksum: 4ECA
     Compressed Length: A5455, Checksum: F7FB
$USER Section:
Msecs   48
Heap0   16   320 32
Heap1   32   160 32
Heap2   64   160 32
Heap3   128  600 128
Heap4   192  460 128
Heap5   256  30 12
Heap6   320  24 6
Heap7   384  16 6
Heap8   448  32 6
Heap9   512  20 8
Heap10  576  40 8
Heap11  1024 20 4
Heap12  2560 6  2
Heap13  4096 4  2
Heap14  0 0
Heap15  0 0
MbufInt 20 10 10
MbufIO  60 50 160 0 0
Queue   100 # 64 troy 5/14/99
Cbuf    100
FuncId  20
Proc    24
Timer   32
DNS             16
FilterSet       12
IpRoute         8
IpxRoute        4
IpMaxRt         128
IpxMaxRt        128
IpxMaxSap       128
AppleTalkRoute  0
Bridge          4
RemoteNode      8
Profile         8
Endpoint        4
SUAserver       8
DHCPEntry       254
IpPolicySet     12
PoeSvrCnt       4
ScheduleSet     12
Model  1 108
Vendor 1 0
HwVerRange 2 0 0
}}}
=== Link ===
[http://www.nslu2-linux.org/wiki/HowTo/AddASerialPort USB Serial cable]

[:BootBase:Bootbase]
