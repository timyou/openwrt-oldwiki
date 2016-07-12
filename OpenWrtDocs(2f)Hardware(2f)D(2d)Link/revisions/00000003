= D-Link hardware notes =
[[PageList(OpenWrtDocs/Hardware/D-Link)]]
= Shared Information =
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

== DSL-500T pinout ==
JP1 connector on the board is AR7 EJTAG.

Xilinx cable to LPT port and pinout

{{{
LPT (pin)----------- EJTAG JP1(pin)
2  <- 100om -> 2 (TDI)
3  <- 100om -> 5 (TCK)
4  <- 100om -> 4 (TMS)
13 <- 51om -> 3 (TDO)
20,25 <------> 12 (GND)
               connect JTAG pins 1<-100om->8
}}}

----
CategoryBrand ["CategoryAR7Device"]
