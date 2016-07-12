= Firewall configuration =
== Parameters ==
  * src: the source ''network''; the first network the packet is seen on.  For traffic originating from the internet, this is "wan," and for traffic originating from the local network, this is "lan."  This also apples ('''please confirm''') to traffic originating from the current system, only "src" will be chosen according to the destination address, i.e. a packet on a typical network with a destination of 192.168.1.55 will have "lan" as the source, while a packet with a destination of 64.233.187.99 will have "wan" as the source.
  * dest: the destination ''network''; the last network the system will see the packet on.  This option is mainly used for forwarding, routing, and NAT.
  * src_ip: source IP address; the IP address of the system where the packet originated.
  * src_dport: the destination port as chosen by the system at the source IP address.  This is the port that it's attempting to access on the system, e.g. a web server at port 80.
  * dest_ip: destination IP address; the IP address a packet is being sent to.  Packets destined for the system will be delivered to the process bound to a specified port on this IP address.  Packets destined for another system, if either routing or NAT is set up, will be forwarded.  See [:OpenWrtDocs/Kamikaze/NetworkConfiguration: Network Configuration] for how to set routes.
== Examples ==
=== Opening ports ===
The default configuration accepts all LAN traffic, but blocks all incoming WAN traffic on ports not currently used for connections or NAT.  To open a port for a service, add a "rule" entry:
{{{
config rule
        option dst              wan
        option src_dport        22
        option target           ACCEPT
        option protocol         tcp
}}}
This example enables machines on the internet to use SSH to access your router.

=== Forwarding ports ===
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
