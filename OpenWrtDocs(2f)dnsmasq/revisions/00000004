= dnsmasq =

 Dnsmasq is lightweight, easy to configure DNS forwarder and DHCP server. It is designed to provide DNS and, optionally, DHCP, to a small network. It can serve the names of local machines which are not in the global DNS. The DHCP server integrates with the DNS server and allows machines with DHCP-allocated addresses to appear in the DNS with names configured either in each host or in a central configuration file. Dnsmasq supports static and dynamic DHCP leases and BOOTP for network booting of diskless machines.

 Dnsmasq is targeted at home networks using NAT and connected to the internet via a modem, cable-modem or ADSL connection but would be a good choice for any small network where low resource use and ease of configuration are important. 

== FAQ ==

=== Whay local client nslookup request respond like "[rutername]can't find [hostname]: Query refused ===

dnsmasq will reaspond with that message if isnt know IP address where to forward DNS request. That IP address is provided in /etc/resolve.conf. Some programs like (ppp/pppoe) create dinamicly resolve.conf file and fill it with IP address got from ISP provider (basicly if you are not connected with ppp, you dont have resolve.conf file).

If you got that message and you have reslove.conf file, very probably your dnsmasq is running like user nobody (standard behavior in experimental distribution of OpenWRT). Put next line in /etc/dnsmasq.conf
{{{
  user=root
}}}

and stop/start dnsmasq daemon. That should solve your problem.

=== Where to set names for privet IP address ===
Puting information about that in /etc/hosts file, and format is
{{{
[IP_address] host_name host_name_short ...

192.168.1.1 router.lan router
}}}
