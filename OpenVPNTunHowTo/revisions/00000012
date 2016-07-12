'''OpenVPN via TUN !HowTo'''

[[TableOfContents]]

= Introduction =
The intention of this guide is to enable a TUN-based (routed) tunnel with SSL/TLS certificates on your [:OpenWrtDocs/About:OpenWRT] installation. It was based (and largely copied from :) ) on the ["OpenVPNHowTo"], which in turn talks about a slightly different (TAP-based) approach.

For more information regarding the differences between bridging (TAP) and routing (TUN) and which solution is more appropriate in your case please see [http://openvpn.net/faq.html#bridge2].

The desired final setup is an OpenVPN server running on your OpenWRT which will receive OpenVPN client connections and optionally forward them (so you can you the internet through your new tunnel).

= Install Software =
To install OpenVPN on OpenWRT, only a simple command is needed:
{{{
ipkg install openvpn
}}}

Windows users can either download the standard [http://openvpn.net/ OpenVPN distribution] or get the [http://openvpn.se/ OpenVPN GUI for Windows] from Mathias Sundman.

Non-Windows clients just follow the OpenVPN install instructions.

= Certificate creation =
Without delving too deeply in that incredibly annoying process of Certificate creation, you need to generate the following files (the names can be changed to suit your personal organizational preferences).
||<style="text-align: center;"> '''file''' ||<style="text-align: center;"> '''description''' ||<style="text-align: center;"> '''example of command to create it''' ||
|| ca.crt || the Root Certificate for your Certificate Authority. Should be on the server and all clients. Should be used to sign all the other certificates (both server and client) || {{{#openssl req -nodes -new -x509 -days 1825 -keyout ca.key -out ca.crt;}}} ||
|| server.crt, client.crt || the certificate for your server or client, signed using the Root Certificate || {{{#openssl req -nodes -new -keyout server.key -out server.csr;}}} {{{#openssl ca -cert ca.crt -keyfile ca.key -out server.crt -in server.csr; *}}} {{{#openssl req -nodes -new -keyout client.key -out client.csr;}}} {{{#openssl ca -cert ca.crt -keyfile ca.key -out client.crt -in client.csr; *}}} ||
|| server.key, client.key || the private key generated with your server or client's certificate || ''same as above, created on the same run'' ||
|| dh.pem || the Diffie-Hellman file for secure SSL/TLS negotiation, identical on the server and all clients || {{{#openssl dhparam -out dh.pem 1024;}}} ''(change 1024 to the size of the key you want)'' ||
|| shared.key ''(optional)'' || a shared key file, identical on the server and all clients || {{{#openvpn --genkey --secret shared.key;}}} ||

* If you receive an error like {{{I am unable to access the ./demoCA/newcerts directory. /demoCA/newcerts: No such file or directory}}}, take a look at your {{{openssl.cnf}}} file. For instance, in Ubuntu and OpenWRT RC9 openssl expect a {{{demoCA}}} directory with a {{{newcerts}}} and a {{{private}}} subdirectory. Run these commands to create everything in Ubuntu:
{{{
mkdir demoCA
mkdir demoCA/newcerts
mkdir demoCA/private
touch demoCA/index.txt
echo "01" >> demoCA/serial
}}}

For more details check out the PKI part of the [http://openvpn.net/howto.html#pki OpenVPN 2.0 HowTo] which uses the {{{EASY-RSA}}} package.
Another useful tool to generate the certificates is [http://www.eduroam.edu.au/tech/ cascript].

At last the server key has to be made inaccessible for others:
{{{
chmod 0600 /etc/openvpn/server.key
}}}
= Server Setup =
== OpenVPN server config file ==
Change the addresses for your specific setup, if needed.

{{{/etc/openvpn/server.conf:}}}
{{{
### network options
port 1194
proto udp
dev tun
### certificate and key files
ca /etc/openvpn/ca.crt
cert /etc/openvpn/server.crt
key /etc/openvpn/server.key
dh /etc/openvpn/dh.pem
### (optional) use a shared key to initialize TLS negotiation
tls-auth /etc/openvpn/shared.key
### VPN subnet
server 10.8.0.0 255.255.255.0
### (optional) make local network behind the VPN server accessible for the VPN clients
push "route 192.168.1.0 255.255.255.0"
### (optional) make the VPN server a gateway for the internet for the VPN clients
push "redirect-gateway"
### (optional) compression (might make your WRT sluggish or not, depending on the model and what you have running...)
comp-lzo
keepalive 10 120
status /tmp/openvpn.status
}}}
'''Note:''' on the merits of tls-auth, please read [http://openvpn.net/howto.html#security this].

At this point you can start OpenVPN for testing:
{{{
openvpn /etc/openvpn/server.conf
}}}
=== Make VPN accessible through proxy and/or restrictive firewall ===
If access to the VPN through a proxy and/or a restrictive firewall is needed, then using the TCP protocol for the proxy and port 443 for the firewall will be the solution for nearly all cases.
{{{
port 443
proto tcp
}}}
It is possible to keep port 1194, but then you have to redirect port 443 with a firewall rule.
== Firewall ==
To access the VPN from the internet (WAN) the firewall rules must accept outside connections for your VPN port (e.g. udp-1194).
The firewall rules are stored in {{{/etc/firewall.user}}}.
There is already an example (WR 0.9) for accepting SSH connections from outside, which can be copied and changed to:
{{{
### OpenVPN
## allow connections from outside
iptables -t nat -A prerouting_wan -p udp --dport 1194 -j ACCEPT
iptables        -A input_wan      -p udp --dport 1194 -j ACCEPT
}}}
Also as mentioned in the OpenVPN FAQ [http://openvpn.net/faq.html#ip-forward ip_foward must be enabled] ([http://forum.openwrt.org/viewtopic.php?pid=20428#p20428 default in WR 0.9]) and [http://openvpn.net/faq.html#firewall packets for the OpenVPN interfaces have to be allowed/forwarded]:
{{{
## allow input/forwarding for the VPN interfaces, see http://openvpn.net/faq.html#firewall
## also needs ip_forward, see http://openvpn.net/faq.html#ip-forward and http://forum.openwrt.org/viewtopic.php?pid=20428#p20428
iptables -A INPUT   -i tun+ -j ACCEPT
iptables -A FORWARD -i tun+ -j ACCEPT
iptables -A INPUT   -i tap+ -j ACCEPT
iptables -A FORWARD -i tap+ -j ACCEPT
}}}

If you want to block DoS attacks then have a look at [http://forum.openwrt.org/viewtopic.php?id=7493 this forum thread].
It is based on the information of the documents ["OpenWrtDocs/IPTables"] and ThrottleConnectionsHowTo. It also provides an example how to access SSH via a non-standard port (e.g. 443 for restrictive firewalls) although SSH is still running on the standard port 22.
You can easily adopt it to VPN.

If it is intended that keys are send via SSH across the WAN, then also enable accepting SSH connections from outside:
{{{
### SSH (optional)
## allow connections from outside
iptables -t nat -A prerouting_wan -p tcp --dport 22 -j ACCEPT
iptables        -A input_wan      -p tcp --dport 22 -j ACCEPT
}}}

== Automatic OpenVPN startup ==
If the manual startup and configuration worked fine, the only missing step is to automate OpenVPN's startup on the server side. Simply add the following file and it should start automatically on the next boot process.
{{{/etc/init.d/S46openvpn:}}}
{{{
#!/bin/sh
case "$1" in
        start)
                openvpn --daemon --config /etc/openvpn/server.conf
        ;;
        restart)
                $0 stop
                sleep 3
                $0 start
        ;;
        reload)
                killall -SIGHUP openvpn
        ;;
        stop)
                killall openvpn
        ;;
esac
}}}
At last the script has to be made executable:
{{{
chmod 0755 /etc/init.d/S46openvpn
}}}
= Client Setup =
Copy shared.key, ca.crt, client.crt, client.key and dh.pem to your openvpn directory on your client (/etc/openvpn/ in Linux). You can copy them securely via {{{scp}}}, with:

{{{
scp <OpenWRT IP>:/etc/openvpn/<file.name> /etc/openvpn/
}}}

And use this as a client configuration file:
{{{
client
dev tun
proto udp
remote your.domain.com 1194
nobind
### (optional) degrade privileges to this user and group after initialization
#user nobody
#group nogroup
ca /etc/openvpn/ca.crt
cert /etc/openvpn/client.crt
key /etc/openvpn/client.key
dh /etc/openvpn/dh.pem
### (optional) use a shared key to initialize TLS negotiation
tls-auth /etc/openvpn/shared.key
### (optional) compression (use only if the server has it)
comp-lzo
}}}
'''Note:''' ''your.domain.com'' should be set to your static IP or to your dynamic DNS configured with [:DDNSHowTo:ez-ipupdate].

Now that should be it. Start the OpenVPN client either through the GUI or command line and it should link up.
= Troubleshooting =
== "Certificate not yet valid" error ==
This is probably the first problem you'll encounter and it's related to the server date. To fix it, just:
{{{
ipkg install ntpclient
}}}
And start it after installation.
== LAN behind VPN server not accesible  ==
First check your firewall rules and your server config that it pushes a route to the VPN clients.

Second make sure that all LAN clients use the VPN server as their default gateway or have a route for the VPN subnet to the VPN server.
----
 . CategoryHowTo
