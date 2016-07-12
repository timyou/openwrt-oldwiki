= dnsmasq =

Dnsmasq is lightweight, easy to configure DNS forwarder and DHCP server. It is designed to provide DNS and, optionally, DHCP, to a small network. It can serve the names of local machines which are not in the global DNS. The DHCP server integrates with the DNS server and allows machines with DHCP-allocated addresses to appear in the DNS with names configured either in each host or in a central configuration file. Dnsmasq supports static and dynamic DHCP leases and BOOTP for network booting of diskless machines.

Dnsmasq is targeted at home networks using NAT and connected to the internet via a modem, cable-modem or ADSL connection but would be a good choice for any small network where low resource use and ease of configuration are important.


== FAQ ==


=== Problem: nslookup says something like "[routername] can't find [hostname]: Query refused" ===

Described problem can appear when you use router in AP mode with experimental distribution.

dnsmasq responds with this message if it doesn't know where to forward DNS request for resolution. This IP address is provided in /etc/resolv.conf (on squashfs it is aliased to /rom/etc/resolv.conf, which in turn alias of /tmp/resolv.conf). Some programs, like ppp/pppoe, create resolv.conf dynamically and put there IP address they got from ISP. Basically if you are not connected with ppp, you don't have resolv.conf file. dnsmasq checks modification time of resolv.conf file and, if it is changed from last request, it will reload info from resolv.conf. This feature gives you possibility to start dnsmasq before actual information is received from ISP.

If you got this message and you have resolv.conf file, most probably your dnsmasq is running like user nobody, which is standard behavior in experimental distribution of OpenWRT. Just put following line in /etc/dnsmasq.conf

{{{
  user=root
}}}

and stop/start dnsmasq daemon. That should solve your problem.

Be aware that router itself doesn't use dnsmasq to resolve its own DNS requests. Instead it uses IP address of DNS set to WAN(vlan1) interface.


=== Problem: on starting, dnsmasq reports something like, "Syntax error: network+192.168.1.100" ===

An initial symptom of this problem is that DNS forwarding doesn't seem to work and a call to 'ps -A' reports that dnsmasq isn't running. Check the output of 'logread' for information about what happened when dnsmasq tried to run:

{{{
logread |grep dnsmasq|less
}}}

The problem lies in that the init script for dnsmasq expects the nvram variable, dhcp_start, to be in an integer format instead of an IP. Variable dhcp_start defines offset from beginning of your network adresses and variable dhcp_num defines how many IP adresses to use in DHCP pool. DHCP pool consists of adresses NETWORK+dhcp_start..NETWORK+dhcp_start+dhcp_num.

Example 1: Your network is 192.168.1.0/255.255.255.0, your starting address is 192.168.1.100, your ending address is 192.168.1.150 try this:

{{{
nvram set dhcp_start=100
nvram set dhcp_num=50
nvram commit
/etc/init.d/S50dnsmasq restart
}}}

Example 2: Your network is 192.168.10.40/255.255.255.248, your starting address is 192.168.10.42, your ending address is 192.168.10.45 try this:

{{{
nvram set dhcp_start=2
nvram set dhcp_num=3
nvram commit
/etc/init.d/S50dnsmasq restart
}}}

=== Where to set names for private IP address ===
Puting information about that in /etc/hosts file, and format is
{{{
[IP_address] host_name host_name_short ...

192.168.1.1 router.lan router
}}}

dnsmasq needs read permission on /etc/hosts (check your logs if you can't resolve hostnames from your clients)
{{{
chmod +r /etc/hosts
}}}

=== Static IP-Address (leases) based on the MAC-Address of the client ===

'''NOTE:''' There is a known bug in dnsmasq. dnsmasq can't read the /etc/ethers file because it runs as user nobody.
nbd fixed that bug in versions later than "White Russian RC4" and it is already fixed in "White Russian CVS".

To get rid of this bug, just do:

{{{
ipkg -force-overwrite -force-reinstall install \
        http://downloads.openwrt.org/people/nbd/ \
        whiterussian/packages/dnsmasq_2.22-2_mipsel.ipk
}}}

When a client should get always the same IP address from the DHCP server then use the line below in your {{{/etc/ethers}}} file

{{{
# <mac> <ip>
00:aa:bb:cc:dd:ee 192.168.1.2
}}}

Put the hostname for that IP address in the {{{/etc/hosts}}} file.
