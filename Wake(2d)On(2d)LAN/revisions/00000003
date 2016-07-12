'''Wake-On-LAN !HowTo''' (2007-04-23: WR 0.9)

[[TableOfContents]]

= General =
Wake-On-LAN (short WOL) can be used to awake a network machine (computer, printer, etc.) from standby mode over the network with a "magic packet". Lots of information about WOL can be found on [http://gsd.di.uminho.pt/jpo/software/wakeonlan/mini-howto/ José Pedro Oliveira's Wake on LAN mini HOWTO].
When something is not explained here, then it is already documented in José's WOL !HowTo.

Before setting up OpenWRT to wake up your machines, you should test if your machines can be waked up at all. Test this from another machine on your LAN. Use the information and tools from José's !HowTo mentioned above, e.g. AMD's Magic Packet tool.

= Setting up OpenWRT for WOL =
== Using WOL (=UDP packet) ==
With {{{wol}}} you can send a magic packet via IP. For this you have to know the broadcasting address of your network, e.g. 10.1.255.255 for a 10.1.0.0/16 network.

For {{{wol}}} install the following package
{{{
ipkg install wol
}}}

To awake a machine with {{{wol}}} use
{{{
wol -h <broadcast address> <mac address of the target> (e.g. wol -h 10.1.255.255 11:22:33:44:55:66)
}}}

If doesn't work have a look at your network topology and check if the packet is forwarded to the router/switch the target is connected to.

Note: Maybe you are lucky and it even works without the broadcast address, but don't count on it.

== Using Ether-Wake (=ether frame) ==
With {{{ether-wake}}} you can send a magic packet as an ethernet frame. You don't need any broadcast address for it, but all routers in your LAN have to forward ethernet frames.

{{{ether-wake}}} is provided as a backport, so you have to add the backport repository for your OpenWRT version in {{{/etc/ipkg.conf}}}. Check if it is already present, otherwise add it via 
{{{
echo "src 0.9-backports http://downloads.openwrt.org/backports/0.9" >> /etc/ipkg.conf (this is for WhiteRussion 0.9)
}}}
Then update the list of available packages
{{{
ipkg update
}}}
And finally install the {{{ether-wake}}} package
{{{
ipkg install ether-wake
}}}

To awake a machine with {{{ether-wake}}} use
{{{
ether-wake <mac address of the target> (e.g. ether-wake 11:22:33:44:55:66)
}}}

Note: If it doesn't work, switch to {{{wol}}} as all routers should forward IP packets correctly.
= Tip: Not to remember all your MAC addresses =
Create a small script for each machine you want to awake.
Create the script files in the folder {{{/jffs/bin}}}, use the extension {{{.sh}}} and begin all of them with the line {{{#!/bin/sh}}}.
After this add lines with {{{wol}}} or {{{ether-wake}}} calls.
Use several lines if you want to wake up a group of machines at once.
{{{
#!/bin/sh
ether-wake 11:11:11:11:11:11
ether-wake 22:22:22:22:22:22
}}}
At last you have to make them executable via
{{{
chmod 0700 wol-example.sh 
}}}
Now you can call them from anywhere by just entering their name.
