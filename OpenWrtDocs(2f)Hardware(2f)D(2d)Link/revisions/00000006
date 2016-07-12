= D-Link hardware notes =
[[PageList(OpenWrtDocs/Hardware/D-Link)]]
Dlink: support page http://support.dlink.com/products/
= Serial port pinout =
== DSL-G300T/302T/500T serial pinout ==
{{{
 ___________________________________ 
|         Pin 1: RX      ----> []   |
|         Pin 2: GND     ----> ()   |
|         Pin 3: + 3.3 v ----> ()   |
|         Pin 4: GND     ----> ()   |
|         Pin 5: TX      ----> ()   led     Front of G300T/302T/500T
|                             JP2   |
|                                   led
|                                   |
|                                   led
|                                   led
|___________________________________|
}}}

The console is located in upper right corner, if you hold board with components to you, ethernet to left and leds to right, it's JP2, the only 5-pin 2,54mm-step connector. Usualy it is already soldered-in. Voltage reference is 3.3 volts and it is set by default at 38400,8,N,1.

== DSL-G504T/604T/664T serial pinout ==
{{{
_______________________________________
|                                      \
|                                       led
|                                       led
| Pin 5: TX      ----> ()               led
| Pin 4: GND     ----> ()               led
| Pin 3: + 3.3 v ----> ()               |
| Pin 2: GND     ----> ()               |
| Pin 1: RX      ----> []               led     Front of G504T/604T/664T
|                     JP5               |
|                                       led
|                                       |
|                                       led
|                                       led
|______________________________________/
}}}

The console is located aproximately in center of a board, it's JP5, the only 5-pin 2,54mm-step connector. Usualy it is already soldered-in. Voltage reference is 3.3 volts and it is set by default at 38400,8,N,1.

= JTAG port pinout =
JP1 connector on the DSL-500T,DSL-504T and DSL-G604T board is AR7 MIPS core EJTAG. Usualy it is not soldered in, so solder in 7x2 2,54 mm DIL header here first.

Xilinx cable to LPT port and pinout

{{{
LPT (pin)------- EJTAG JP1(pin)
2  <- 100 Ohm -> 2 (TDI)
3  <- 100 Ohm -> 5 (TCK)
4  <- 100 Ohm -> 4 (TMS)
13 <- 51 Ohm  -> 3 (TDO)
20 <--*--------> 12 (GND)
25 <--+
     +100 Ohm -> 1 (connect JTAG pins 1<-100om->8)
     +---------> 8
}}}

----
CategoryBrand ["CategoryAR7Device"]
