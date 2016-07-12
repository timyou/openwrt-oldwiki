= OpenVPN via TUN HowTo =

The intention of this guide is to enable a TUN-based (routed) tunnel with SSL/TLS certificates on your [:OpenWrtDocs/About:OpenWRT] instalation.
It was based (and largely copied from :-) ) on the ["OpenVPNHowTo"], which in turn talks about a slightly different (TAP-based) approach.

The desired final setup is an OpenVPN server running on your OpenWRT which will receive OpenVPN client connections and optionally forward them (so you can you the internet through your new tunnel)

== Install Software ==

For the OpenWRT, only a simple:

{{{ipkg install openvpn}}}

is all that is needed. Windows users can either download the standard OpenVPN distribution or get the GUI version from here:

http://openvpn.se/

Non-Windows clients just follow the OpenVPN install instructions.

== Certificate creation ==

Without delving too deeply in that incredibly annoying process of Certificate creation, you need to generate the following files (the names can be changed to suit your personal organizational preferences):

||<:> '''file''' ||<:> '''description''' ||<:> '''example of command to create it''' ||
|| ca.crt || the Root Certificate for your Certificate Authority. Should be on the server and all clients. Should be used to sign all the other certificates (both server and client) || {{{#openssl req -nodes -new -x509 -keyout ca.key -out ca.crt;}}} ||
|| server.crt, client.crt || the certificate for your server or client, signed using the Root Certificate || {{{#openssl req -nodes -new -keyout server.key -out server.csr;}}} {{{#openssl ca -cert ca.crt -keyfile ca.key -out server.crt -in server.csr;}}} ||
|| server.key, client.key || the private key generated with your server or client's certificate || ''same as above, created on the same run'' ||
|| dh.pem || the Diffie-Hellman file for secure SSL/TLS negotiation, identical on the server and all clients || {{{#openssl dhparam -out dh.pem 1024;}}} ''(change 1024 to the size of the key you want)'' ||
|| shared.key ''(optional)'' || a shared key file, identical on the server and all clients|| {{{#openvpn --genkey --secret shared.key;}}} ||


== Server Setup ==

=== Firewall ===

First we need to make sure that OpenVPN connections to port 1194 are not blocked by the firewall on OpenWRT. Add the following two lines after the section allowing WAN SSH access. 

If you intend to ssh the key across the WAN, enable the second block and if you want your tunnel to be your default route to the internet, you might need to enable the third block too.

/etc/firewall.user:
{{{
### Allow OpenVPN connections
iptables -t nat -A prerouting_rule -i $WAN -p udp --dport 1194 -j ACCEPT
iptables        -A input_rule      -i $WAN -p udp --dport 1194 -j ACCEPT

### Allow SSH from WAN (optional)
iptables -t nat -A prerouting_rule -i $WAN -p tcp --dport 22 -j ACCEPT
iptables        -A input_rule      -i $WAN -p tcp --dport 22 -j ACCEPT

### Allow forwarding for the VPN interface (optional)
iptables -A forwarding_rule -i tun0 -j ACCEPT
}}}

=== OpenVPN server config file ===

Change the addresses for your specific setup, if needed.

/etc/openvpn/server.conf:
{{{
### network options
port 1194
proto udp
dev tun

### certificate and key files
ca /etc/openvpn/ca.crt
cert /etc/openvpn/server.crt
key /etc/openvpn/server.key
tls-auth /etc/openvpn/shared.key
dh /etc/openvpn/dh.pem

### address options
server 10.0.0.0 255.255.255.0

### (optional) make the VPN server's local network accessible
push "route 192.168.1.0 255.255.255.0"

### (optional) make the VPN server a gateway for the internet
push "redirect-gateway"

### (optional) compression (might make your WRT sluggish or not, depending on the model and what you have running...)
comp-lzo

keepalive 10 120
status /tmp/openvpn.status
}}}

At this point you can start OpenVPN for testing:

{{{openvpn /etc/openvpn/server.conf}}}

== Client Setup ==

Ensure that the client has the certificates and keys explained above, perhaps by copying some of them (the ones that should be identical) via scp, with:

{{{scp <OpenWRT IP>:/etc/openvpn/* /etc/openvpn/}}}

And use this as a client configuration file:
{{{
client
dev tun
proto udp

remote your.domain.com 1194

nobind

user nobody
group nogroup

ca /etc/openvpn/ca.crt
cert /etc/openvpn/client.crt
key /etc/openvpn/client.key
tls-auth /etc/openvpn/shared.key
dh /etc/openvpn/dh.pem

comp-lzo
}}}

Now that should be it. Start the OpenVPN client either through the GUI or command line and it should link up.

== Automatic OpenVPN startup ==

If the manual startup and configuration worked fine, the only missing step is to automate OpenVPN's startup on the server side.
Simply add the following file and it should start automatically on the next boot process.

/etc/init.d/S46openvpn:
{{{
#!/bin/sh

case "$1" in
        start)
                openvpn --daemon --config /etc/server.ovpn
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

----
CategoryHowTo
