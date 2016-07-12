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

=== Where to set names for private IP address ===
Puting information about that in /etc/hosts file, and format is
{{{
[IP_address] host_name host_name_short ...

192.168.1.1 router.lan router
}}}

=== Make sure that the configuration files it needs are readable by 'nobody'. ===

If you are using the squashfs root, and your umask is 077 (the default in the experimental distribution), when you remove the symlink to the configuration file in /etc/ and cp the /rom/etc/ file into etc so you can edit it, dnsmasq will not be able to read the conffile, and lookups will fail.  Set the umask to 022 or chmod the files and it works fine.

=== Static IP-Address (leases) based on the MAC-Address of the client ===

When a client should get always the same IP-Address from the DHCP-Server then use the line below in your /etc/dnsmasq.conf file
{{{
dhcp-host=<mac address client>,<hostname client>,<ip address client>,12h

dhcp-host=00:11:22:ff:bb:af,foobar,192.168.1.2,12h
}}}
