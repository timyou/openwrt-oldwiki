[[TableOfContents]]

= Fonera =

the Fonera is based on an Atheros System on a Chip (Soc). It got a MIPS 4KEc V6.4 processor. There is an ongoing process porting OpenWRT to this chip: AtherosPort


== Serial ==

It got populated serial headers

    * VCC (3.3V) – red
    * GND – blue
    * RX – white
    * TX – orange

If the ethernet jack is in front of you, it looks like
{{{
b . o w .
r . . . . 

 O    O
}}}


Serial settings are 9600-8-N-1

I have to power the fonera up wait for a few seconds before connecting the serial cable, otherwise it doesn't boot.


== JTAG == 
There seems to be a 14 pin unpopulated jtag, but it's not that important as the redboot boatloader doesn't seem to be crippled.

== Original software ==
{{{
+PHY ID is 0022:5521
Ethernet eth0: MAC address xx:xx:xx:xx:xx
IP: 0.0.0.0/255.255.255.255, Gateway: 0.0.0.0
Default server: 0.0.0.0

RedBoot(tm) bootstrap and debug environment [ROMRAM]
Non-certified release, version v1.3.0 - built 16:57:58, Aug  7 2006

Copyright (C) 2000, 2001, 2002, 2003, 2004 Red Hat, Inc.

Board: ap51
RAM: 0x80000000-0x81000000, [0x80040450-0x80fe1000] available
FLASH: 0xa8000000 - 0xa87f0000, 128 blocks of 0x00010000 bytes each.
== Executing boot script in 1.000 seconds - enter ^C to abort
^C
RedBoot>
}}}


