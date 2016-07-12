= Thomson ST 780WL =

== The device ==
The Thomson ST 780 is a DSL broadband access device that allows ADSL connectivity while providing Voice over IP functions for home and office users. The ST780WL offers an additional 802.11g wireless LAN interface. Both IADs support ADSL2/ADSL2+ and are backward compatible to ADSL offering auto-negotiation capability.

http://www.speedtouch.co.uk/products/Details.asp?ProductID=528

This device is based on BCM6348@???Mhz and it seems to have a 4MB flash (TBV).
 
== Firware infos ==
This device supports the mdap protocol which allows to start the upgrade process on multiple devices via IP multicast (although the firmware is uploaded to the device via tftp).
See http://svn.rot13.org/index.cgi/mdap/ for a basic (yet functional) mdap framework.

It is possible to start the firmware upgrade via telnet/serial CLI or via web GUI. 

I can't recognize the firmware format (yet). :)
The vendor firmware seems to have the following header (od -tx1z -Ad)

{{{
0000000 42 4c 49 32 32 33 51 48 30 00 00 00 00 00 00 00  >BLI223QH0.......<
0000016 00 00 00 00 30 00 00 00 00 00 00 00 00 00 00 00  >....0...........<
0000032 06 02 11 05 00 00 00 00 00 00 01 5f 00 30 57 1f  >..........._.0W.<
0000048 fb 8b c0 86 27 3a e3 6f b7 60 84 ac ee b5 23 99  >....':.o.`....#.<
0000064 7a 4a 77 34 a7 5b 54 1d 43 73 79 67 21 72 c9 09  >zJw4.[T.Csyg!r..<
0000080 30 95 78 05 7f 3f bc a2 66 46 dd c3 ce 34 df 25  >0.x..?..fF...4.%<
0000096 26 ca 69 0e e8 06 f5 c9 4b 77 df dd 38 10 f7 5d  >&.i.....Kw..8..]<
0000112 c9 93 7f 30 14 2d 8a 42 5d 83 ff b7 05 1c c4 a2  >...0.-.B].......<
0000128 89 ca a6 50 8e 74 c8 00 7e 3e 65 e2 33 ca ff bb  >...P.t..~>e.3...<
0000144 48 28 2d 06 af ba b0 91 18 be bf 72 52 72 12 1e  >H(-........rRr..<
0000160 e3 a7 86 f9 95 86 b9 f3 ad 58 12 23 c7 9c 8e 58  >.........X.#...X<
0000176 ff 41 69 46 2b 53 9d 73 80 12 c5 3b 59 7e 5d 6c  >.AiF+S.s...;Y~]l<
0000192 9f b3 b3 77 e3 4d cb 5e e3 95 d3 62 41 ca e3 b2  >...w.M.^...bA...<
0000208 fe c3 69 18 59 cd 64 4f 15 c6 3c 86 d8 d7 72 62  >..i.Y.dO..<...rb<
0000224 cc 05 41 69 1d 94 76 17 7c e8 77 d8 7e 05 0c a0  >..Ai..v.|.w.~...<
0000240 42 0a c6 52 ef 08 de a3 73 5e 66 cf 3b de c4 05  >B..R....s^f.;...<
0000256 58 0b e6 8c e1 a4 d0 43 3f af 04 8a 05 8d e0 0d  >X......C?.......<
0000272 0c cb 84 a5 40 69 67 d6 3b ed 6d 07 d8 e3 ae 9b  >....@ig.;.m.....<
0000288 d4 77 30 7d 35 c4 fc d5 7e bb 15 4d 15 12 0e b6  >.w0}5...~..M....<
0000304 b7 bd 45 02 08 06 42 41 4e 54 2d 52 01 04 bf c4  >..E...BANT-R....<
0000320 00 10 09 0e 53 70 65 65 64 54 6f 75 63 68 20 37  >....SpeedTouch 7<
0000336 38 30 0a 00 20 03 32 30 30 81 04 bf c4 00 04 b2  >80.. .200.......<
}}} 

The following trailer seems to carry some hints about the firmware file format (...i don't like the "sign" word...)

{{{
[...]
3168368 92 16 8d 23 66 6e e1 0c 0c c4 77 ab 97 21 69 70  >...#fn....w..!ip<
3168384 6b 67 32 5f 73 69 67 6e 28 69 6e 3d 37 3d 33 31  >kg2_sign(in=7=31<
3168400 36 38 30 33 31 5b 62 79 74 65 5d 2c 20 6f 75 74  >68031[byte], out<
3168416 3d 31 3d 33 31 36 38 33 38 32 5b 62 79 74 65 5d  >=1=3168382[byte]<
3168432 29 20 28 69 70 6b 67 32 2d 68 65 61 64 65 72 3d  >) (ipkg2-header=<
3168448 33 35 31 5b 62 79 74 65 5d 29 0a                 >351[byte]).<
}}}

The firmware seems to be compressed (no gain if compressed with gzip).
I can't recognize the compression alg used. After the header there are following bytes:
{{{
[...]
0000352 4d 55 54 45 0a 00 30 57 15 56 4a a2 e3 04 d8 4c  >MUTE..0W.VJ....L<
0000368 74 a9 7b e0 f4 fa 35 9a 50 a6 4c 32 8a 2c 22 23  >t.{...5.P.L2.,"#<
0000384 6c e8 51 e2 00 07 6e df 24 d2 98 14 09 2a eb 7c  >l.Q...n.$....*.|<
0000400 c6 82 2a 5f e2 bb b1 0b 16 e6 1a 7d 62 89 a9 7e  >..*_.......}b..~<
0000416 06 93 75 5e 8f 70 67 10 c9 f8 10 19 b2 ec 53 c0  >..u^.pg.......S.<
[...]
}}}

== i/f's ==

http://xoomer.alice.it/uxguerri/images/TST-cnct.jpg

Serial pinout
{{{
1 --> Vcc (3.3V)
2 --> Gnd
3 --> Tx
4 --> Rx

9600,8,N,1
}}}

== Bootlog ==
{{{
Unzipping started

 UNZIP DONE -> starting bootloader


 Speedtouch initialization sequence started.

Secondary boot

Unzipping started

 UNZIP DONE -> starting uncompressed file


 Speedtouch initialization sequence started.


[OSI2]  File "/ZZOGAA6.2H5": Format OSI2 compliant (offset=340, prodid="0", varid="0").
[SS]    Device mounted (prodid="0", prodname="SpeedTouch 780", varid="0", varname="").
[ELF]   Loading file "/ZZOGAA6.2H5" ...
c

 Speedtouch initialization sequence started.
loading : firmware/pob6w_init
Calibrating delay loop... ts/
archfs opened /ZZOGAA6.2H5 offset 2203507
loading : firmware/pots/ZZW6AA.gz
lmem size 53772
sdram size 390932
pSdramPHY=0xA0FFFFF8, 0x6F5FF5EC 0xD7EFECEF
AdslCoreHwReset: AdslOemDataAddr = 0xA0F252.31 BogoMIPS
mpi: device 0x4318 found in PCI slot 1, function 0
FDE2wl: srom not detected, using main memory mapped srom info (wombo board)
4
wl0: wlc_attach: using main broad MAC address base in NVRAM (wombo board srom: 1 )
wl0 MAC Address: 00:90:D0:DE:65:1A
For EMAC2 - select for non-managed switch (single EMAC).

appl_init: BUILD VERIFIED!
3.131.35.1.cpe0.0: Broadcom BCM4318 802.11 Wireless Controller
Build startup 8068b90c
[IGD-MBUS] in igd_mbus_init(), register s_mbus_igd.
[IGD-MBUS] IGD IPInterface successfully registered.
[IGD-MBUS] mbus object type WANPPPConnection successfully registered
[IGD-MBUS] mbus object type WANIPConnection successfully registered
[IGD-MBUS] mbus object type WANDSLInterfaceConfig successfully registered
[IGD-MBUS] mbus object type WANConnectionDevice successfully registered
[IGD-MBUS] IGD NATApplicationList successfully registered.
[IGD-MBUS] mbus object type DYNDNS successfully registered
[IGD-MBUS] mbus object type Internet successfully registered
[IGD-MBUS] mbus igd object type VoiceServices.Capabilities successfully registered
[IGD-MBUS] mbus object type voiceprofile successfully registered
[IGD-MBUS] mbus object type VoiceServices successfully registered
SNTP: SERVMGMT initialized: success!
archfs opened /ZZOGAA6.2H5 offset 2203507
archfs opened /ZZOGAA6.2H5 offset 2203507
<4> SysUpTime: 00:00:01 KERNEL Cold restart
[EXPR] intf _intf_0 new()
[EXPR] ip _addr_127_0_0_1 new()
archfs opened /ZZOGAA6.2H5 offset 2203507

************* ERROR RECORD *************
time            : 000000:00:00.000000
Application /ZZOGAA6.2H5 started after POWERON.
****************** END *****************
Username : Administrator
Password :
------------------------------------------------------------------------

                             ______  SpeedTouch 780
                         ___/_____/\
                        /         /\  6.2.17.5
                  _____/__       /  \
                _/       /\_____/___ \  Copyright (c) 1999-2007, THOMSON
               //       /  \       /\ \
       _______//_______/    \     / _\/______
      /      / \       \    /    / /        /\
   __/      /   \       \  /    / /        / _\__
  / /      /     \_______\/    / /        / /   /\
 /_/______/___________________/ /________/ /___/  \
 \ \      \    ___________    \ \        \ \   \  /
  \_\      \  /          /\    \ \        \ \___\/
     \      \/          /  \    \ \        \  /
      \_____/          /    \    \ \________\/
           /__________/      \    \  /
           \   _____  \      /_____\/
            \ /    /\  \    /___\/
             /____/  \  \  /
             \    \  /___\/
              \____\/

------------------------------------------------------------------------

{Administrator}=>
}}}
----
["CategoryBCM63xx"]
----
["CategoryBCM63xx"]
