= How To: VPNC on your OpenWrt router =
Some people, like students from Ghent University, Belgium, need to connect with a Cisco VPN server in order to connect to the internet. It's an ideal task for an !OpenWrt router to make that connection and share it with all the connected PC's. The only drawback is that VPNC is quite needy and on my Asus WL-500G Deluxe (300Mhz) it maxes out at 30KB/s (VPNC then uses 99% of CPU resources).

== Getting VPNC ==
Configure your device to use the backports repository, see ["OpenWrtDocs/Packages"] for instructions, then install the package:

{{{
ipkg install vpnc}}}

== Configure ==
=== VPNC Configuration ===
Create a configfile for VPNC:

{{{
vim /etc/vpnc.conf}}}

And insert the parameters for your connection in there. These parameters are normally given by your sysadmin.

Here is an example vpnc.conf:
{{{
Interface name tun0
IPSec gateway 157.193.46.4
IPSec ID ipsecclient
IPSec secret cisco123
Xauth username Yourusername
Xauth password Yourpassword}}}

Note on the first line that we'll be giving the interface we're creating the name '''tun0''', this is important for routing, we'll get there in a minute. the IP-address after ''IPSec gateway'' is the address of the VPN-server. The '''IPSec ID''' and '''IPSec secret''' must be given to you by your sysadmin, or try these values as defaults.

Obviously, '''Yourusername''' and '''Yourpassword''' need to be replaced by your username and password respectively. If you don't feel comfortable with having your password in a plain text file for everyone to see, you can remove the last line. VPNC will then prompt you for the password every time you connect.

=== Connection Script ===

You'll need to create a shellscript to set up the routes, so type:

{{{
mkdir /etc/vpn
touch /etc/vpn/initvpn.sh
chmod a+x /etc/vpn/initvpn.sh
vim /etc/vpn/initvpn.sh}}}

First, you'll need a route to the VPNC server so that it knows where to find it after it has established the connection:

{{{
# Add route to the VPNC server
route add 157.193.46.4 gw 172.16.70.254 vlan1;}}}

Here, 157.193.46.4 is again the VPNC server and 172.16.70.254 is the gateway. Change vlan1 into whatever your WAN-port is named.

Next, start VPNC

{{{
# Start VPNC
vpnc;}}}

Now we need to tell the router to route all traffic over this connection. Notice the use of '''tun0''', the interface-name we gave to the VPNC-connection in vpnc.conf:

{{{
# Add route to use VPNC for everything
route add default tun0;}}}

== Sharing the connection ==
That's that, but now you need to tell the router to share the internet connection. It takes a bit of ''iptables'' magic. Note the use of '''tun0''' here as well:

{{{
iptables -A forwarding_rule -o tun0 -j ACCEPT;
iptables -A forwarding_rule -i tun0 -j ACCEPT;
iptables -t nat -A postrouting_rule -o tun0 -j MASQUERADE;}}}

Now save the file and you're done. Execute this script to create a transparant VPNC-connection. Happy surfing.

----
CategoryHowTo CategoryHowTo
