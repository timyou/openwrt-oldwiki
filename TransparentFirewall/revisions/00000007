How to setup a transparent firewall (or possibly, a wireless bridge)

''' WARNING: You should be familiar with booting Failsafe mode on your router when using this document.  The firewall rules can be tricky, and you can easily lock yourself out.'''


== Background ==

I work at a university where every computer is connected to the internet with a public IP address.  This leaves all computers open to direct attack by hackers/worms on the internet.  I have used cheap NAT routers to protect most computers, but I need something a bit smarter to protect my servers.

Why are the servers different?  

 * The servers must use public IP addresses in order to be accessible to the clients.  If I were to use NAT with port forwarding, I would be restricted to one service per port.  This is simply not possible with the services we have running.
 * Because the cheap NAT routers block all incoming traffic that is not in the NAT table.  The servers need to have certain ports open for file sharing, printing, etc.  But I only want those services available to our local subnet.  The cheap NAT routers do not have the ability to port forward packets from the local subnet only.
 * The University's 'ISP' restricts each ethernet port to a single MAC address, very much the same way a wireless AP restricts each associated client to a single MAC address.  This means that not only do I need a transparent firewall, but I need IP layer bridging and MAC layer NAT.  


== Network Topology ==

[http://support.mprg.org/openwrt/topology.jpg]

== Kernel Patching ==

ebtables has been removed from the openWRT kernel for performanc reasons, so you will need to build a custom firmware with ebtables in the kernel.

 * Visit [http://wiki.openwrt.org/OpenWrtDocs/Installing] to download the openWRT source code.
 * Click [http://support.mprg.org/openwrt/100-ebtables.patch.txt] to download the patch.
 * Save the patch into openwrt/target/linux/linux-2.4/patches/
 * Run 'make menuconfig'
 * Be sure to include bridging and ebtables in package selection and kernel configuration.
 * Run 'make'

Please see other documentation on building a custom openWRT firmware if you are unfamiliar with the process.

== Setup ==


---- /!\ '''Edit conflict - other version:''' ----
=== Package Installation ===

Be sure the following packages are installed: ebtables, ip, parprouted

=== NVRAM Variables ===

The following nvram variables need to be set.  The variables set to '[set]' need to be set to your environment.

{{{
lan_gateway=[set]
lan_netmask=[set]
lan_ifnames=vlan0
lan_dns=[set1],[set2],...
lan_proto=static
lan_ipaddr=[set]
lan_ifname=vlan0
wan_proto=static
wan_ifname=vlan1
wl0_radio=0
}}}

---- /!\ '''Edit conflict - your version:''' ----
=== Package Installation ===

Be sure the following packages are installed: ebtables, ip, parprouted

=== NVRAM Variables ===

The following nvram variables need to be set.  The variables set to '[set]' need to be set to your environment.

{{{
lan_gateway=[set]
lan_netmask=[set]
lan_ifnames=vlan0
lan_dns=[set1],[set2],...
lan_proto=static
lan_ipaddr=[set]
lan_ifname=vlan0
wan_proto=static
wan_ifname=vlan1
wl0_radio=0
}}}

== References ==

---- /!\ '''End of edit conflict''' ----
