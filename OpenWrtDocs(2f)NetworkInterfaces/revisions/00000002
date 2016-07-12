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

== Interfaces under OpenWRT ==

An OpenWRT box is actually two devices in one. It consists of a VLAN-configurable switch and a Linux host. The switch and host are connected by one internal "wire", over which VLAN tagged packets are exchanged. All of the physical ethernet ports on the box are ports on a single internal switch. VLANs are then used to separate the ports into groups. The diagram below shows the architecture.

attachment:ASUS-Internals-default.png

By default, the switch is partitioned into two VLANs. Port 0 is configured as VLAN0, and this is labelled on the chassis as WAN. Ports 1-4 are configured as VLAN1, labelled as LAN1-4.

There is an internal port, Port 5, which has a VLAN-tagged connection into the Linux internals. This port is bound to 'eth0' on the Asus WL-500gP. 'eth0' is not configured with an IP address - the kernel takes the raw packets from eth0 and using the VLAN tags, it sorts the packets from VLAN0 and VLAN1. Packets to/from VLAN1 are mapped to a logical interface called 'vlan1', and packets to/from VLAN0 are mapped to a logical interface called VLAN0.
