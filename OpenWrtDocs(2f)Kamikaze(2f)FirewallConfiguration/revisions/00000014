= Firewall configuration =
== Parameters ==
=== Zones ===
Zones are defined in the {{{/etc/config/network}}} file in the {{{config interface <zonename>}}} lines.

 * '''syn_flood''': defend the system from [http://en.wikipedia.org/wiki/SYN_flood SYN flood] attacks.  Valid values are 1 and 0.
 * '''input''': the chain to, by default, send incoming packets to.  Valid values: "DROP," "ACCEPT."
 * '''output''': the chain to, by default, send outgoing packets to.  If the value isn't "ACCEPT," all outgoing ports must be explicitly enabled; extra effort would be required for ping, wget, and ssh to work.  Valid values: "DROP," "ACCEPT."
 * '''forward''': the chain to, by default, send forwarded packets to.  Valid values: "DROP," "ACCEPT."
 * '''masq''': enable network masquerading (i.e. IP translation aka dynamic NATting) on the zone.  Typically, a wan zone will have this enabled.  Valid values are 1 and 0.
=== Rules and forwarding ===
 * '''src''': the source ''network''; the first network the packet is seen on.  For traffic originating from the internet, this is "wan," and for traffic originating from the local network, this is "lan."  This also applies ('''please confirm''') to traffic originating from the current system, only "src" will be chosen according to the destination address, i.e. a packet on a typical network with a destination of 192.168.1.55 will have "lan" as the source, while a packet with a destination of 64.233.187.99 will have "wan" as the source.
 * '''dest''': the destination ''network''; the last network the system will see the packet on.  This option is mainly used for forwarding, routing, and NAT.
 * '''src_ip''': source IP address; the IP address of the system where the packet originated.
 * '''src_dport''': the destination port as chosen by the system at the source IP address.  This is the port that it's attempting to access on the system, e.g. a web server at port 80.
 * '''dest_ip''': destination IP address; the IP address a packet is being sent to.  Packets destined for the system will be delivered to the process bound to a specified port on this IP address.  Packets destined for another system, if either routing or NAT is set up, will be forwarded.  See [:OpenWrtDocs/Kamikaze/NetworkConfiguration:Network Configuration] for how to set routes.
 * '''src_ip''': source IP address; the IP address of the computer that originally send the packet.  This can be a remote computer on the internet, a computer on the local network, or even the local system.
 * '''target''': which chain to send the packet in a rule to.  Valid values are "DROP" and "ACCEPT."
 * '''proto''': the protocol of the packet.  It isn't strictly an [http://en.wikipedia.org/wiki/Transport_Layer transport layer] or [http://en.wikipedia.org/wiki/Internet_Layer internet layer] protocol.  Valid values are "tcp," "udp," and "ICMP."
To specify a range of ports for '''src_dport''' and '''dest_port''' separate the values with a hypen, e.g. '''27000-27999'''

== Examples ==
=== Opening ports ===
The default configuration accepts all LAN traffic, but blocks all incoming WAN traffic on ports not currently used for connections or NAT.  To open a port for a service, add a new "rule" section entry:

{{{
config rule
        option _name            SSH
        option src              wan
        option target           ACCEPT
        option dest_port        22
        option proto            tcp
}}}
To add this new section from UCI CLI do:

{{{
root@OpenWrt:~# uci add firewall rule
root@OpenWrt:~# uci set firewall.@rule[-1]._name=SSH
root@OpenWrt:~# uci set firewall.@rule[-1].src=wan
root@OpenWrt:~# uci set firewall.@rule[-1].target=ACCEPT
root@OpenWrt:~# uci set firewall.@rule[-1].dest_port=22
root@OpenWrt:~# uci set firewall.@rule[-1].proto=tcp
root@OpenWrt:~# uci commit firewall
root@OpenWrt:~# /etc/init.d/firewall restart
}}}
This example enables machines on the internet to use SSH to access your router.

=== Forwarding ports (Destination NAT/DNAT) ===
Following the "zone" entries, add a "redirect" entry:

{{{
config redirect
        option src              wan
        option src_dport        80
        option dest             lan
        option dest_ip          192.168.1.10
        option dest_port        80
        option proto            tcp
}}}
This example forwards http (but not https) traffic to the webserver running on 192.168.1.10.

=== Source NAT (SNAT) ===
Source NAT changes an outgoing packet outgoing packet destined for the system so that is looks as though the system is the source of the packet.

{{{
# options need to be confirmed, especially src_ip
config redirect
        option src              lan
        option dest             wan
        option src_ip           xx.55.34.85
        option dest_ip          63.240.161.99
        option dest_port        123
}}}
When used alone, Source NAT is used to restrict a computer's access to the internet, but allow a it to access a few services my manually forwarding what appear to be a few local services, e.g. [http://en.wikipedia.org/wiki/Network_time_protocol NTP] to the internet.  While DNAT hides the local network from the internet, SNAT hides the internet from the local network.

Source NAT and destination NAT are combined and used dynamically in IP masquerading to make computers with private (192.168.x.x, etc.) IP address to appear on the internet with the system's public WAN ip address.

=== True destination port forwarding ===
''Most users won't want this''.  It's usage is similar to SNAT, but as the the destination IP address isn't changed, machines on the destination network need to be aware that they'll receive and answer requests from a public IP address that isn't necessarily theirs.  Port forwarding in this fashion is typically used for load balancing.

{{{
config redirect
        option src              wan
        option src_dport        80
        option dest             lan
        option dest_port        80
        option proto            tcp
}}}
=== Manual iptables rules ===
iptables rules, in the standard iptables unix command form, can be specified in an external file and included in the firewall config file.

{{{
config include
       option path /etc/firewall.user
}}}
To add this new section from UCI CLI do:

{{{
root@OpenWrt:~# uci add firewall include
root@OpenWrt:~# uci set firewall.@include[0].path=/etc/firewall.user
root@OpenWrt:~# uci commit firewall
}}}
