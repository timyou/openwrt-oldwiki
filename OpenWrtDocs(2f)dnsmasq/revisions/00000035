= dnsmasq =

Dnsmasq is lightweight, easy to configure DNS forwarder and DHCP server. It is
designed to provide DNS and, optionally, DHCP, to a small network. It can serve
the names of local machines which are not in the global DNS. The DHCP server
integrates with the DNS server and allows machines with DHCP-allocated addresses
to appear in the DNS with names configured either in each host or in a central
configuration file. Dnsmasq supports static and dynamic DHCP leases and BOOTP
for network booting of diskless machines.

Dnsmasq is targeted at home networks using NAT and connected to the internet
via a modem, cable-modem or ADSL connection but would be a good choice for any
small network where low resource use and ease of configuration are important.


== FAQ ==

=== Problem: on starting, dnsmasq reports something like, "Syntax error: network+192.168.1.100" ===

An initial symptom of this problem is that DNS forwarding doesn't seem to work
and a call to {{{ps -A}}} reports that dnsmasq isn't running. Check the output
of {{{logread}}} for information about what happened when dnsmasq tried to run:

{{{
logread | grep dnsmasq | less
}}}

The problem lies in that the init script for dnsmasq expects the NVRAM variable,
{{{dhcp_start}}}, to be in an integer format instead of an IP. Variable
{{{dhcp_start}}} defines offset from beginning of your network addresses and
variable {{{dhcp_num}}} defines how many IP addresses to use in DHCP pool. DHCP
pool consists of addresses {{{NETWORK+dhcp_start..NETWORK+dhcp_start+dhcp_num}}}
(oops, you have got {{{dhcp_num+1}}} dynamic addresses :-).

Example 1: Your network is {{{192.168.1.0/255.255.255.0}}}, your starting address
is {{{192.168.1.100}}}, your ending address is {{{192.168.1.150}}} try this:

{{{
nvram set dhcp_start=100
nvram set dhcp_num=50
nvram commit
killall -9 dnsmasq ; /etc/init.d/S50dnsmasq
}}}

Example 2: Your network is {{{192.168.10.40/255.255.255.248}}}, your starting
address is {{{192.168.10.42}}}, your ending address is {{{192.168.10.45}}} try
this:

{{{
nvram set dhcp_start=2
nvram set dhcp_num=3
nvram commit
killall -9 dnsmasq ; /etc/init.d/S50dnsmasq
}}}


=== Where to set names for private IP address ===

Puting information about that in {{{/etc/hosts}}} file, and format is

{{{
[IP_address] host_name host_name_short ...
}}}

{{{
192.168.1.1 router.lan router
}}}

dnsmasq needs read permission on {{{/etc/hosts}}} (check your logs if you
can't resolve hostnames from your clients)

{{{
chmod +r /etc/hosts
}}}


=== Static IP address (leases) based on the MAC address of the client ===

When a client should get always the same IP address from the DHCP server then
use the line below in your {{{/etc/ethers}}} file.

{{{
# <mac> <ip>
00:aa:bb:cc:dd:ee 192.168.1.2
}}}

Put the hostname for this IP address in the {{{/etc/hosts}}} file.


=== Configuring dnsmasq to use different IP ranges for wired and wireless ===

Suppose you have the following:

{{{
vlan0     Link encap:Ethernet  HWaddr XX:XX:XX:XX:XX:XX
          inet addr:192.168.1.1    Bcast:192.168.1.255    Mask:255.255.255.0

eth1      Link encap:Ethernet  HWaddr XX:XX:XX:XX:XX:XX
          inet addr:10.75.9.1      Bcast:10.75.9.255      Mask:255.255.255.0
}}}

Simply put 2 "dhcp-range" options in your {{{/etc/dnsmasq.conf}}} file:

{{{
# dhcp-range=[network-id,]<start-addr>,<end-addr>[[,<netmask>],<broadcast>][,<default lease time>]
dhcp-range=lan,192.168.1.101,192.168.1.104,255.255.255.0,24h
dhcp-range=wlan,10.75.9.111,10.75.9.119,255.255.255.0,2h
}}}

You can then use the different "network-id" values with "dhcp-option" to customize the
options your DHCP server will supply to your wired and wireless DHCP clients.

for example

{{{
#set the default route for dhcp clients on the wlan side to 10.10.6.33
dhcp-option=wlan,3,10.10.6.33
#set the dns server for the dhcp clients on the wlan side to 10.10.6.33
dhcp-option=wlan,6,10.10.6.33
#set the default route for dhcp clients on the lan side to 10.10.6.1
dhcp-option=lan,3,10.10.6.1
#set the dns server for the dhcp clients on the lan side to 10.10.6.1
dhcp-option=lan,6,10.10.6.1
}}}
