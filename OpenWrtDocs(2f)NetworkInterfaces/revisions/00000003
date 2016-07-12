= Interfaces on the ASUS WL-500GP (and others) =
This page describes the network interface mapping on the Asus WL-500GP, and probably also describes most other OpenWRT compatible networking devices. The goal is to help users understand how the complex mix of ports, vlans, bridges and interfaces actually all tie together. It's focussed on the WL-500G Premium, but is probably also valid for Linksys boxes, however interface numbers might differ.

In this page, "the OpenWRT" refers to any such supported network device running OpenWRT that has a similar network config.

== Understanding VLANs ==
=== Basics ===
Before getting too far into the details, it's important to know what VLANs are and how they work.

A VLAN (Virtual LAN) is, in basic terms, a group of physial interfaces on a switch that behave as if they are a separate standalone switch. This allows us to use one physical switch, but partition it into multiple LANs, each one completely isolated from the others. The switch must support VLAN configurations - most cheap switches don't allow this, but high end manageable switches do, as does the internal switch on the OpenWRT.

VLANs are used when you need to separate traffic between groups of devices, but you only want to use one physical switch. For example you might want one VLAN outside your firewall, for public web/mail servers, and another VLAN for your internal machines such as desktops and boxes with private data. They can't be placed on the same LAN for security reasons, so you use VLANs to isolate the groups of ports.

Lets say we have a 10 port switch, and we configure ports 1-5 as VLAN1 and 6-10 as VLAN2. All devices which are plugged into ports 1 thru 5 behave as if they are on their own switch, and devices in ports 6-10 act as if they're in another switch. The main rule is that communication between ports on separate VLANs is blocked - even if you configure devices with the same subnet, they will not be reachable to devices in other VLANs.

And of course, it's also possible to configure it differently - if you later decide you need to put another device in VLAN1 and you've only used 4 ports in VLAN2, you can reconfigure _any_ of the VLAN2 ports into VLAN1 (not just port 6). So then you might end up with VLAN1 as ports 1-5 and 8, and VLAN2 as ports 6,7,9,10.

The number of VLANs that you can configure on any device is only limited by the number of ports.

There subject of VLANs can get very complicated and extensive, but this quick summary covers what's needed for using VLANs on the OpenWRT platform.

=== VLAN Trunking ===
If you have a switch with multiple VLANs, you may want to attach a device (such as another switch) that needs to talk to more than one VLAN. This could be a firewall, which will take packets from one VLAN, filter them, then pass them to another VLAN. Alternatively, you might have a second switch that has the same two VLANs on them, and you want to two switches to exchange packets between each other for both VLANs, whilst maintaining the separation.

This is done with a process known as trunking. One port on the switch must be configured as a trunk port, and this port will have connectivity to all VLANS for which it's set to be a trunk port. If you have a switch with 3 VLANs, you can configure one (or more) trunk port(s) to have connectivity to all VLANs, or just a subset of the VLANs.

How does the switch maintain isolation with this port? This is done with "tagging". Every packet sent or received from the trunk port has a little tag attached to it, indicating what VLAN it is for or from. So a device receiving packets looks at the tag to see what VLAN that packet is from. When the device sends traffic to the switch, it will add a tag itself, and the switch will look at the tag and send the packet to the VLAN indicated.

In the example of an attached firewall, a packet coming in from the internal LAN will be sent out the trunk port to the firewall, tagged with the internal VLAN number. The firewall will process the packet, then send it back to the switch with a tag for the external VLAN, and the switch will look at this tag and send it to the outside device.

You can see that a device such as a firewall will see each separate VLAN as if it's a different network interface. The internal VLAN is like a NIC on the inside of the network, and the external interface behaves just like a NIC on the outside. Because of this, most hosts and firewalls that support VLAN tags are setup such that each VLAN tag is as if it was another separate network interface, even though it's the same physical wire.

== Bridging ==

Under Linux, a bridge is a link between two ethernet interfaces in such a way as to link them together to the same LAN. If you have a Linux box with two ethernet interfaces, then connect each interface to separate switches, the two switches are effectively linked together as if they're connected with a cable. You can also link together a wired ethernet interface with a wireless interface - the two are then linked together, much like a wireless AP or bridge.

One useful feature of bridging is that the Linux box which is doing the bridging can listen to and send its own traffic. It does this by creating another interface. If you link eth0 and eth1, they will be bound to an interface br0 (or br1, etc). You can then assign an IP address to br0 and it will behave like a normal network interface attached to this bridged network. You cannot configure an IP address on the bridge members (eth0 or eth1), it needs to be done on the bridge interface.

This knowledge of bridges is important below.

== Interfaces under OpenWRT ==

An OpenWRT box is actually two devices in one. It consists of a VLAN-configurable switch and a Linux host. The switch and host are connected by one internal "wire", over which VLAN tagged packets are exchanged. All of the physical ethernet ports on the box are ports on a single internal switch. VLANs are then used to separate the ports into groups. The diagram below shows the architecture.

attachment:ASUS-Internals-default-sm.png

By default, the switch is partitioned into two VLANs. Port 0 is configured as VLAN0, and this is labelled on the chassis as WAN. Ports 1-4 are configured as VLAN1, labelled as LAN1-4.

There is an internal port, Port 5, which has a VLAN-tagged connection into the Linux internals. This port is linked to 'eth0' on the Asus WL-500gP. 'eth0' is not configured with an IP address - the kernel takes the raw packets from eth0 and using the VLAN tags, it sorts the packets from VLAN0 and VLAN1. Packets to/from VLAN1 are then mapped to a logical interface called 'vlan1', and packets to/from VLAN0 are mapped to a logical interface called 'vlan0'.

Under OpenWRT, the vlan1 interface is then usually configured with the WAN ip address, and all configuration that applies to the WAN interface (eg iptables rules and routes) are applied to the vlan1 interface.

The vlan0 interface is done a bit differently. By default, the wifi interface (eth2) is bridged to the LAN ports, ie any host associated on the wireless port is automatically in the same VLAN/subnet as hosts on the LAN ports. This is done with bridging (see above). As described above, when a bridge is created, a new logical interface is created, called br0, and also as above, this br0 interface is the one that needs to have any IP address configured. So, by default, vlan0 does not have an IP address configure, instead, the LAN interface address is configured on the br0 interface.

There's also another interface visible from the shell - "eth1". This doesn't appear to be linked to anything, and is probably an unused wire on the ethernet controller, so it's ignored in all configuration.

== Interface configuration ==
With a knowledge of how interface are partitioned, it's now easier to understand how to configure interfaces under OpenWRT.

The following block configured the physical ports into VLANS:

{{{
vlan0hwname=et0
vlan0ports=1 2 3 4 5*
vlan1hwname=et0
vlan1ports=0 5*
}}}

The "hwname" part is always "et0". The device "et0" is the switch itself and tells the system which switch to configure with VLANS. As there's only one switch, this must always be set to "et0".

The ports then are configured. The vlan0 (LAN) is configured with four ports, plus the internal tagged port, port 5. The vlan1 (WAN) is configured with only the one port, plus also the tagged port.

This configuration then gives us "vlan0", tied to the WAN port, and "vlan1" tied to the other ports.

The WAN port is then configured with an IP address and mapped to the logical 'wan' interface name:

{{{
wan_ifname=vlan1
wan_ipaddr=a.b.c.d
wan_netmask=255.255.255.0
wan_proto=static
}}}

Next the LAN side is configured. Because of the bridging, there's an extra step, but overall it's similar:

{{{
lan_ifname=br0
lan_ifnames=vlan0 eth2
lan_proto=static
lan_ipaddr=10.0.0.1
lan_netmask=255.255.255.0
}}}

The variable "lan_ifname", which sets the actual interface to configure the IP parameters with, should of course be br0 for a bridged interface. Then the variable "lan_ifnames" actually sets the interfaces which are to be bound to the bridge interface, in this case the vlan0 interface and the wireless interface. The vlan0 ports were defined earlier as wired ports 1-4, so these plus the wireless interface are now one single logical LAN.

That's basically how the entire network device architecture is on this box. Below is an example of adding another VLAN.

== DMZ Vlan ==

If you're running some public servers and are security concious, you'll probably want to make use of DMZ (Demilitarised Zone). This is a third VLAN in a network, configured with different rules to the internal secure network. Generally the DMZ is configured to allow access to certain ports from the internet that wouldn't normally be allowed to inside hosts.

Under OpenWRT, a DMZ is easy to configure. A third VLAN is created, and one or more physical ports is mapped to this VLAN, then suitable firewall rules are created for this VLAN. The pictur below shows how a DMZ configuration would look inside the device:

attachment:ASUS-Internals-dmz.png

The configuration lines that would be changed for this are:

{{{
vlan0ports=3 4 5*
vlan2hwname=et0
vlan2ports=1 2 5*
dmz_ifname=vlan2
dmz_proto=static
dmz_ipaddr=192.168.1.0
dmz_netmask=255.255.255.0
}}}

This configuration firstly changes the vlan0 to exclude ports 1&2 which will be our DMZ ports. Then the DMZ vlan is created, with ports 1, 2 and 5 (remember 5 is the internal tagged port). Then the logical interface 'dmz' is configured and attached to vlan2. To bring up the new interface, just run "ifup dmz". And of course do your firewall configuration.
