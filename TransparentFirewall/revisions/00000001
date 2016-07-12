How to setup a transparent firewall (or possibly, a wireless bridge)

== Background ==

I work at a university where every computer is connected to the internet with a public IP address.  This leaves all computers open to direct attack by hackers/worms on the internet.  I have used cheap NAT routers to protect most computers, but I need something a bit smarter to protect my servers.

Why are the servers different?  

 * The servers must use public IP addresses in order to be accessible to the clients.  If I were to use NAT with port forwarding, I would be restricted to one service per port.  This is simply not possible with the services we have running.
 * Because the cheap NAT routers block all incoming traffic that is not in the NAT table.  The servers need to have certain ports open for file sharing, printing, etc.  But I only want those services available to our local subnet.  The cheap NAT routers do not have the ability to port forward packets from the local subnet only.
 * The University's 'ISP' restricts each ethernet port to a single MAC address, very much the same way a wireless AP restricts each associated client to a single MAC address.  This means that not only do I need a transparent firewall, but I need IP layer bridging and MAC layer NAT.  

== Network Topology == 

== Kernel Patching ==

== Setup ==

== References ==
