~+'''Wake-On-LAN !HowTo'''+~

__Valid for the following releases:__ Kamikaze, White Russian

[[TableOfContents]]

= General =
Wake-On-LAN (short WOL) can be used to awake a network machine (computer, printer, etc.) from standby mode over the network with a "magic packet". Lots of information about WOL can be found on [http://gsd.di.uminho.pt/jpo/software/wakeonlan/mini-howto/ José Pedro Oliveira's Wake on LAN mini HOWTO]. When something is not explained here, then it is already documented in José's WOL !HowTo.

Before setting up !OpenWrt to wake up your machines, you should test if your machines can be waked up at all. Test this from another machine on your LAN. Use the information and tools from José's !HowTo mentioned above, e.g. AMDs Magic Packet tool.

As of October 2007 there is only a {{{wol}}} package for Kamikaze.
There is no {{{ether-wake}}} package yet, but it is already reported in [https://dev.openwrt.org/ticket/2460 ticket 2460].
For the old White Russian release you find {{{ether-wake}}} in the [ftp://ftp.berlios.de/pub/xwrt/packages X-Wrt WR backport repository].

= Setting up OpenWrt for WOL =
With {{{wol}}} you can send a magic packet via IP. For this you have to know the broadcasting address of your network, e.g. 10.1.255.255 for a 10.1.0.0/16 network.

== Installation ==
For {{{wol}}} install the following package

{{{
ipkg install wol
}}}

== Usage ==
To awake a machine with {{{wol}}} use

{{{
wol -h <broadcast address> <mac address of the target> (e.g. wol -h 10.1.255.255 11:22:33:44:55:66)
}}}
If doesn't work have a look at your network topology and check if the packet is forwarded to the router/switch the target is connected to.

Note: Maybe you are lucky and it even works without the broadcast address, but do not count on it.

== Easy Usage ==
Make sure your /etc/hosts and /etc/ethers files are populated properly.

Save the following script to /usr/bin/wake

{{{
#!/bin/ash
if [ -z "$1" ]; then 
	echo Usage:  $0  hostname
	exit
fi

sucky_resolve () {	grep  -i $1  /etc/hosts  | awk '{ print $1 }'
}
sucky_ether   () {	grep  -i $1  /etc/ethers | awk '{ print $1 }'
}
broadcast_ip4 () {	echo $IPADDRESS | sed s/\.[0-9]*$/.255/
}

IPADDRESS=`sucky_resolve  $1`
    ETHER=`sucky_ether    $IPADDRESS`
BROADCAST=`broadcast_ip4  $IPADDRESS`
wol -i $BROADCAST $ETHER
}}}

Set the executable bit
{{{
chmod +x /usr/bin/wake
}}}

And now you should just be able to wake machines by using their hostname
{{{
root@openwrt:~# wake aeris
Waking up 00:99:d4:0f:dc:62...
root@openwrt:~#
}}}

CategoryPackage
