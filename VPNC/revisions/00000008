'''How To: VPNC on !OpenWrt'''

Some people, like students from Ghent University, Belgium, need to connect with a Cisco VPN server in order to connect to the internet. It's an ideal task for an !OpenWrt router to make that connection and share it with all the connected PC's. The only drawback is that VPNC is quite needy and on my Asus WL-500G Deluxe (300Mhz) it maxes out at 30KB/s (VPNC then uses 99% of CPU resources).

= Installation =
Configure your device to use the backports repository, see ["OpenWrtDocs/Packages"] for instructions, then install the package:

{{{
ipkg install vpnc}}}

= Configuration =

Create a configuration file:

{{{
vi /etc/vpnc.conf}}}

And insert the parameters for your connection in there. These parameters are normally given by your sysadmin.

Here is an example ''vpnc.conf'':
{{{
Interface name tun0
IPSec gateway 157.193.46.4
IPSec ID ipsecclient
IPSec secret cisco123
Xauth username YOURUSERNAME
Xauth password YOURPASSWORD}}}

Note on the first line that we'll be giving the interface we're creating the name ''tun0'', this is important for routing, we'll get there in a minute. the IP-address after ''IPSec gateway'' is the address of the VPN-server. The ''IPSec ID'' and ''IPSec secret'' must be given to you by your sysadmin, or try these values as defaults.

Change '''YOURUSERNAME''' and '''YOURPASSWORD''' to your username and password respectively. If you don't feel comfortable with having your password in a plain text file on your !OpenWrt device, you can remove the ''Xauth password'' line, then VPNC will prompt you for the password every time you connect.

= Writing a Start Script =

A start script configures routing for VPNC, starts the connection, and then optionally shares the connection.

== Preparation ==
Create a shell script, for example:

{{{
mkdir /etc/vpn
touch /etc/vpn/initvpn.sh
chmod a+x /etc/vpn/initvpn.sh
vi /etc/vpn/initvpn.sh}}}

== Create Route to VPNC Server ==

You'll need a route to the VPNC server so that it knows where to find it after it has established the connection, so add these commands to the script:

{{{
#!/bin/sh
# Add route to the VPNC server
route add 157.193.46.4 gw 172.16.70.254 vlan1;}}}

Here, 157.193.46.4 is again the VPNC server and 172.16.70.254 is the gateway. Change vlan1 into whatever your WAN-port is named.

== Starting VPNC ==

Next, add to the script the command to start VPNC:

{{{
# Start VPNC
vpnc;}}}

== Create Route for All Traffic ==

Tell the router to route all traffic over this connection, add to the script:

{{{
# Add route to use VPN for everything
route add default tun0;}}}

Note the use of ''tun0'', the ''interface name'' in ''vpnc.conf''.

== Sharing the VPN ==
Tell the router to share the VPN connection to its clients. It takes a bit of ''iptables'' magic.  Add to the script:

{{{
# Share the VPN connection
iptables -A forwarding_rule -o tun0 -j ACCEPT;
iptables -A forwarding_rule -i tun0 -j ACCEPT;
iptables -t nat -A postrouting_rule -o tun0 -j MASQUERADE;}}}

Note the use of ''tun0'' here as well.

== Testing ==
Save the script.  Execute the script to start the connection.

{{{
/etc/vpn/initvpn.sh}}}
----
CategoryHowTo
