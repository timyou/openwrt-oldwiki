= How To: VPNC on your OpenWRT router =

Some people, like students from Ghent University, Belgium, need to connect with a Cisco VPN server in order to connect to the internet. It's an ideal task for an OpenWRT router to make that connection and share it with all the connected PC's. The only drawback is that VPNC is quite needy and on my Asus WL-500G Deluxe (300Mhz) it maxes out at 30KB/s (VPNC then uses 99% of CPU resources).

== Getting VPNC ==

You're in luck. Alphacore.net has a repository that includes an ipkg'd VPNC. Just add the following line to /etc/ipkg.conf:

{{{
src alphacore http://openwrt.alphacore.net/
}}}

Next, update ipkg and install vpnc by typing (you'll need internet-access for this):

{{{
ipkg update
ipkg install vpnc
}}}

It'll check for dependencies and get all the packages it needs from the alphacore repository.

== Configure ==

Create a configfile for VPNC:
{{{
vim /etc/vpnc.conf
}}}
And insert the parameters for your connection in there. These parameters are normally given by your sysadmin.


You'll need to create a shellscript to set up the routes, so go right ahead and type
{{{
mkdir /etc/vpn
touch /etc/vpn/initvpn.sh
chmod a+x /etc/vpn/initvpn.sh
vim /etc/vpn/initvpn.sh
}}}

First, you'll need a route to the VPNC server so that it knows where to find it after it has established the connection:
{{{
# Add route to the VPNC server
route add 157.193.46.4 gw 172.16.70.254 vlan1;
}}}
Here, 157.193.46.4 is the VPNC server and 172.16.70.254 is the gateway. Change vlan1 into whatever your WAN-port is named.

Next, start VPNC
{{{
# Start VPNC
vpnc;
}}}

Now we need to tell the router to route all traffic over this connection...:
{{{
# Add route to use VPNC for everything
route add default tun0;
}}}

== Sharing the connection ==

That's that, but now you need to tell the router to share the internetconnection. It takes a bit of iptables' magic:
{{{
iptables -A forwarding_rule -o tun0 -j ACCEPT;
iptables -A forwarding_rule -i tun0 -j ACCEPT;
iptables -t nat -A postrouting_rule -o tun0 -j MASQUERADE;
}}}

Now save the file and you're done. Execute this script to create a transparant VPNC-connection. Happy surfing.
----
CategoryHowTo
