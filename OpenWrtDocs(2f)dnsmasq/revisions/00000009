= dnsmasq =

 Dnsmasq is lightweight, easy to configure DNS forwarder and DHCP server. It is designed to provide DNS and, optionally, DHCP, to a small network. It can serve the names of local machines which are not in the global DNS. The DHCP server integrates with the DNS server and allows machines with DHCP-allocated addresses to appear in the DNS with names configured either in each host or in a central configuration file. Dnsmasq supports static and dynamic DHCP leases and BOOTP for network booting of diskless machines.

 Dnsmasq is targeted at home networks using NAT and connected to the internet via a modem, cable-modem or ADSL connection but would be a good choice for any small network where low resource use and ease of configuration are important. 

== FAQ ==

=== Whay local client nslookup request respond like "[routername]can't find [hostname]: Query refused" ===

dnsmasq will reaspond with that message if isnt know IP address where to forward DNS request. That IP address is provided in /etc/resolve.conf. Some programs like (ppp/pppoe) create dinamicly resolve.conf file and fill it with IP address got from ISP provider (basicly if you are not connected with ppp, you dont have resolve.conf file). dnsmasq check modification time of resolve.conf file and if is changed from last request, it will reload info from resolve.conf file (that feature give you possibility to start dnsmasq on booting time, and creating resolve conf on time knowing IP address of DNS server).

If you got that message and you have reslove.conf file, very probably your dnsmasq is running like user nobody (standard behavior in experimental distribution of OpenWRT). Put next line in /etc/dnsmasq.conf
{{{
  user=root
}}}

and stop/start dnsmasq daemon. That should solve your problem.

Be aware that router itself doesnt use dnsmasq for resolving DNS request, insted it use IP address of DNS set to WAN(vlan1) interface.

Before described problem appear if you use router in AP mode and standard experimental distribution (LAN an WiFI behaind NAT) and WAN use some PPP (pppoe/xDSL). DHCP return clients (PC) connected on WiFi or LAN local IP address and for DNS server local IP address of router (so clients will use dnsmasq for resolving hostname).

=== Where to set names for private IP address ===
Puting information about that in /etc/hosts file, and format is
{{{
[IP_address] host_name host_name_short ...

192.168.1.1 router.lan router
}}}

=== Make sure that the configuration files it needs are readable by 'nobody'. ===

If you are using the squashf root, and your umask is 077 (the default in the experimental distribution), when you remove the symlink to the configuration file in /etc/ and cp the /rom/etc/ file into etc so you can edit it, dnsmasq will not be able to read the conffile, and lookups will fail.  Set the umask to 022 or chmod the files and it works fine.
