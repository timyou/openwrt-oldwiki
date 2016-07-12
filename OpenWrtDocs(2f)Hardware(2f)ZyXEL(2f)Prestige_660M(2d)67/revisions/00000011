= Prestige 660M-67 (aka as Arcor Speed Modem 50Z) =
This device is very similar to the [:OpenWrtDocs/Hardware/ZyXEL/Prestige 660HW-61:Prestige 660HW-61], please see that entry for a lot of info that also applies to this model.

== Status ==
The 2.4 AR7 Kamikaze kernel boots up more or less, but serial, VLYNQ and the flash map are non-functional. So it isn't useful yet at all :(

== Running code ==
Kolja Waschk posted his [http://www.ixo.de/info/zyxel_uclinux/ in-depth findings] on a previous Zyxel router. Except for the different memory layout, everything said there applies to the AR7 based model. So a console sessiont to upload code would look like this:

{{{
Bootbase Version: V1.05 | 02/27/2003 02:00:00
RAM: Size = 8192 Kbytes
DRAM POST: Testing:  8192K
OK
FLASH: Intel 16M *1
ZyNOS Version: V3.40(SP.0) | 9/13/2004 21:55:56
Press any key to enter debug mode within 3 seconds.
......
Enter Debug Mode
ATEN1,8C43C295
OK
ATBA5
Now, console speed will be changed to 115200 bps
ATUP94020000,186000
Starting XMODEM upload (CRC mode)....
C
Total 1597440 bytes received
ATGO9417c04c
}}}
== BootBase info ==
Zyxel apparently decided to put the AR7 CPU into big endian mode, not in little endian like with other AR7 based routers. I tried to analyze the environment ["Bootbase"] offers the code it jumps to. These programs do the following:

 1. invalidate primary data and instruction cache indizes ?
 1. setting ERL, EXL and BEV in the CP0 status register - does this set the CPU into kernel mode?
 1. write 0xFFFFFFFF into the Avalanche INTC registers 0x2430 and 0x2434 (in segment 0xA861).
 1. write first 0x7777, then 0xCCCC into the watchdog reg at 0x0B10, then 0x0001 into 0x0B14
 1. Set the CP0 cause reg to 0x80
 1. Copy a bunch of stuff around
 1. Enable ints, set the IRQ mask to 00011100 and enable COPRO3 (?) through the CP0 status reg.
Does any of this make sense? Maybe an experienced AR7 veteran could help me with some of this. ZynOS programs put the stack at the end of the memory, too (0x947FFFC), while Bootbase itself uses a different address for that (0x94001000 I think).

== Memory Map ==
Using Kolja Waschks excellent informations I extracted the memory map from my router:

{{{
ROMIO image start at b0008000
code version:
code start: 94008000
code length: 132C5A
memMapTab: 13 entries, start = b0030000, checksum = 13AA
$RAM Section:
  0: BootExt(RAMBOOT), start=94008000, len=18000
  1: HTPCode(RAMCODE), start=94020000, len=E0000
  2: RasCode(RAMCODE), start=94020000, len=800000
$ROM Section:
  3: BootBas(ROMIMG), start=b0000000, len=4000
  4: DbgArea(ROMIMG), start=b0004000, len=2000
  5: RomDir2(ROMDIR), start=b0006000, len=2000
  6: BootExt(ROMIMG), start=b0008030, len=17FD0
  7: HTPCode(ROMBIN), start=b0020000, len=10000
          (Compressed)
          Version: HTP_P660 V 0.04, start: b0020030
          Length: 15BF4, Checksum: 1521
          Compressed Length: 73BE, Checksum: 28DD
  8: MemMapT(ROMMAP), start=b0030000, len=C00
< Press any key to Continue >
  9: termcap(ROMIMG), start=b0030c00, len=400
 10: tiadsl(ROMBIN), start=b0031000, len=24A00
          (Compressed)
          Version: ADSL ATU-R, start: b0031030
          Length: 3066E, Checksum: 2498
          Compressed Length: 17FA7, Checksum: A0A6
 11: RomDefa(ROMIMG), start=b0055a00, len=2000
 12: RasCode(ROMBIN), start=b0057a00, len=1FA8600
          (Compressed)
          Version: P660R-63/67 ATU, start: b0057a30
          Length: 2C05FC, Checksum: BF18
          Compressed Length: E325A, Checksum: 244C
}}}
So there are 2MB flash at mapped address 0xb0000000 (uncached) = physical address 0x1000000 and 8MB of RAM at mapped address 0x94000000 (cached) = physical address 0x14000000.

AR7 is based on MIPS, so memory 0xa0000000-0xbfffffff (uncached) and 0x80000000-0x9fffffff (cached) both correspond to physical memory 0x00000000-0x1fffffff.

== JTAG ==
According to [http://routertech.org/viewtopic.php?p=15194 this forum post] the 660 family often has MIPS EJTAG 2.6 compatible JTAG pads on the backside of the board. My 660M-67 has the needed pads here, I need to check them with a multimeter later on. Here is an incredibly bad pic of the (supposed) JTAG pads:

attachment:660m-jtag.png

Taking measurements according to the forum post the layout is as follows. If you look at the bottom side of your board, and the connectors (power, LAN, etc) are looking upwards, the 2x7 pin pads are in standard EJTAG format:

{{{
   TRST  + o  GND
    TDI  o o  GND
    TDO  o o  GND
    TMS  o o  GND
    TCK  o o  GND
    RST  o    key
   DINT  o o  VIO (3.3V)}}}
["CategoryAR7Device"]
