= Adding a UART to some BCM4702KPB-based boards =
Unfortunately, BCM4702KPB SoC shares some UART pins with Ethernet0 port, so UART is disabled via GPIO. You have to use '''external''' 3.3V LVTTL or CMOS NS16c550-compatible UART or DUART for devices based on this SoC (i.e. [:WAP54GHowto:WAP54Gv1], Belkin F5D7330 or Asus [:OpenWrtDocs/Hardware/Asus/WL300G:WL-300G]). (Philips [http://www.semiconductors.philips.com/pip/SC16C550IA44.html SC16c550]). Use a 12.75 MHz (25.5MHz/2) crystal for 115200 baud (the UART clock divider is 7). There is the large 20-pin jumper block connected to the CPU I/O data lines, which can be connected to an external UART.

{{{
              -----
   D0      1>| 0 o | 20  A0
   D1      2 | o o | 19  A1
   D2      3 | o o | 18  A2
   D3      4 | o o | 17  CHSL
   D4      5 | o o | 16  /CS
   D5      6 | o o | 15  /RD
   D6      7 | o o | 14  /WR
   D7      8 | o o | 13  MR
   VDD     9 | o o | 12  INTR1, INTR2
VSS (GND) 10 | o o | 11  SIN
              -----
}}}

ASUS WL-500b/g: http://wl500g.info/showthread.php?t=587&page=1&pp=15
