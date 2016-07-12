'''zt8qmwz''' (time of last update: [[Date(2005-10-13T17:41:52Z)]])

Hello, world! This page will contain my correspondence with
hairydairymaid (lightbulb) - I asked for his help in debricking
a TI AR7 based router. If everything goes well, hairydairymaid
will write an AR7 compatible debrick utility.



'''hairydairymaid'''  (time of last update: [[Date(2005-10-13T21:17:00Z)]])

zt8qmwz, got your link and reading over the couple things I asked
about.  The CHIP ID CODE you sent ... CHIP ID: 00000000000000000001000000001111 (0000100F)
looks really fishy to me.  That *might* be real, but it is also remotely possible the 
TI AR7 chip has a broken CHIP ID (there have been some chips in the past that way); 
however, I would triple check the JTAG cabling and make sure it is connected correctly
for a standard 14-pin JTAG cable pinout on the board end of the cable.  In order to
write a debricker for Non-DMA capable units the EJTAG 2.5/2.6 PrAcc method will need
to be employed.  I need to work up some MIPS assembler that will run on the debug
hosted memory in the EJTAG debugging portion of the chip in order to "run" the needed reads
and writes to memory (i.e. - for flash reads/writes).  The PrAcc routines have to "feed"
in MIPS instructions over EJTAG in order for the debugging unit to actually execute
those instructions and they have to be formed in such a way as to meaningfully run code that
will read and write the desired regions.  This is not as easy as DMA access; however, it is doable.
zt8qmwz - please triple check JTAG wiring there, especially since I am doing this blind without
any equipment in front of me.  In the meantime, I'll start on the MIPS isntructions needed for
this little exercise.


----
CategoryHomepage
