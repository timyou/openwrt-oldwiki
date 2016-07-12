This wireless LAN router with an internal 4 port switch and an internal DSL modem is mostly sold from alice dsl in Berlin, Germany and Hamburg, Germany.

There are only few hardware details known. The device is based on a Broadcom chipset with an onboard 802.11g wireless.

You can download firmware from the Thomson website: http://www.thomson-broadband.co.uk/codepages/content3.asp?c=7&ProductID=511

The latest firmware is an actual binary file used to flash this device. Searching through the strings in this image file you can find references to "ipkg":

{{{
$ strings  585v6_UK_62T2.bin|grep ipkg
q3ipkg2_sign(in=7=2594287[byte], out=1=2594638[byte]) (ipkg2-header=351[byte])
}}}
Does this mean there is some Linux code running here?

The memsize should be 16MB, but the flashsize is 4MB - strange.

Board photo:
http://www.visigoth.de/~alx/speedtouch_585iv6_thomson_2.jpg
