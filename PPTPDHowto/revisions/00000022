== PPTPD on OpenWrt ==

This HOWTO describes how to install and configure ''pptpd'' on OpenWrt.

== Installing pptpd ==

Install the ''pptpd'' package. This will also install ''kmod-mppe'' and ''kmod-crypto'' packages if they are not present.
{{{
ipkg install pptpd
}}}

== Configuring pptpd ==

Look at ''/etc/pptpd.conf''.

Take note of the commented ''debug'' option. Uncomment that line for debugging purposes if you have trouble.

Change ''/etc/ppp/options.pptpd'' to suit your needs. Again start by uncommenting the debug option and the logfile option. Since pptpd was built with the "--with-pppd-ip-alloc" configure flag the only way to specify a local IP is with the "<ipaddress>:" line. Change that line to the IP address you want to give the server end of your PPTP tunnel, in our example options.pptpd begins:
{{{
debug
logfile /tmp/pptp-server.log
192.168.0.1:
.
.
.
}}}

For PPTP clients to be able to connect we need to set the usernames and passwords in /etc/ppp/chap-secrets. The format is:
{{{
username provider password ipaddress
}}}

We have to specify the ipaddress for every client since pptpd ignores the remoteip option in pptpd.conf (due to ''--with-pppd-ip-alloc''). An example chap-secrets looks like this:
{{{
vpnuser * vpnpassword 192.168.0.101
}}}

We are now set and ready to give pptpd a first try. So either insmod all modules and start pptpd or just call the startup script and take a look at the logs if pptpd is starting correctly.
{{{
/etc/init.d/S51pptpd start
}}}

== Rules for iptables ==

We need to open port 1723 to accept the PPTP control connections, and open protocol 47 for the data stream, so we add in /etc/firewall.user

{{{
### Allow PPTP control connections from WAN
iptables -t nat -A prerouting_rule -i $WAN -p tcp --dport 1723 -j ACCEPT
iptables        -A input_rule      -i $WAN -p tcp --dport 1723 -j ACCEPT

### Allow GRE protocol (used by PPTP data stream)
iptables        -A output_rule             -p 47               -j ACCEPT
iptables        -A input_rule              -p 47               -j ACCEPT
}}}



== Routing ==

While we now have a VPN ready where the clients can connect to the OpenWrt router we might want to allow the clients to see inside the LAN. Of course we can alway give appropriate routes to server and clients but there's another way. In our example we have a LAN network 192.168.0.1/24 on the LAN port of our router. We want multiple clients to connect to the pptpd server and be able to connect to the LAN without the need of client routes. This is especially useful for Windows machines as they either route everything through the pptpd tunnel or nothing and we want them to be able to connect without much configuration hassle for the users. We will use ''proxyarp'' for that purpose and add the following line to /etc/ppp/options.pptpd
{{{
proxyarp
}}}

When we restart the pptpd server now we should see something like 
{{{
found interface vlan0 for proxy arp
}}}
in the logs. The kernel will now answer arp requests for the clients connected through the PPTP tunnel and thus the packets are routed correctly to either the ppp+ device or vlan0. We will have to add additional iptables rules of course (again given without any guarantee of safety, please correct this if you know better):
{{{
### VPN Section
iptables        -A forwarding_rule -s 192.168.1.0/24 -d 192.168.1.0/24 -j ACCEPT
iptables        -A output_rule     -o ppp+ -s 192.168.1.0/24 -d 192.168.1.0/24 -j ACCEPT
iptables        -A input_rule      -i ppp+ -s 192.168.1.0/24 -d 192.168.1.0/24 -j ACCEPT

# allow VPN connections to get out WAN interface (to internet)
iptables        -A forwarding_rule -i ppp+ -o $WAN -j ACCEPT
}}}


== Finally ==

Congratulations, you have now set up your own ''pptpd'' and can start connecting with PPTP clients. Don't forget to comment out the debug options in the appropriate config files again.


== Troubleshooting and further information ==

If you can connect to the pptpd and can ping the client from the server and vice versa but are not able to ping anything else refer to this checklist for diagnosis: [http://poptop.sourceforge.net/dox/diagnose-forwarding.phtml]

For a Windows XP client howto see here: [http://www.windowsecurity.com/articles/Configure-VPN-Connection-Windows-XP.html]

Information on the PPTP Linux client can be found here: [http://pptpclient.sourceforge.net/] or check the appropriate ["PPTPClientHowto"].

## reviewed 2006-03-15 by james.cameron@hp.com, the current pptpd maintainer
