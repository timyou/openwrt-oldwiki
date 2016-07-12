#pragma section-numbers off
||<tablebgcolor="#f1f1ed" tablewidth="40%" tablestyle="margin: 0pt 0pt 1em 1em; float: right; font-size: 0.9em;"style="padding: 0.5em;">[[TableOfContents]]||
'''Wake-On-LAN !HowTo'''

= General =
Wake-On-LAN (short WOL) can be used to awake a network machine (computer, printer, etc.) from standby mode over the network with a "magic packet". Lots of information about WOL can be found on [http://gsd.di.uminho.pt/jpo/software/wakeonlan/mini-howto/ José Pedro Oliveira's Wake on LAN mini HOWTO]. When something is not explained here, then it is already documented in José's WOL !HowTo.

Before setting up !OpenWrt to wake up your machines, you should test if your machines can be waked up at all. Test this from another machine on your LAN. Use the information and tools from José's !HowTo mentioned above, e.g. AMDs Magic Packet tool.

= Setting up OpenWrt for WOL =
With {{{wol}}} you can send a magic packet via IP. For this you have to know the broadcasting address of your network, e.g. 10.1.255.255 for a 10.1.0.0/16 network.

== Installation ==
For {{{wol}}} install the following package

{{{
ipkg install wol
}}}

== Configuration ==

== Usage ==
To awake a machine with {{{wol}}} use

{{{
wol -h <broadcast address> <mac address of the target> (e.g. wol -h 10.1.255.255 11:22:33:44:55:66)
}}}
If doesn't work have a look at your network topology and check if the packet is forwarded to the router/switch the target is connected to.

Note: Maybe you are lucky and it even works without the broadcast address, but do not count on it.
