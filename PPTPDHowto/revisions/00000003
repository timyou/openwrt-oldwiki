== PPTPD on OpenWrt ==

This howto describes how to install and configure pptpd on OpenWrt.

== Installing pptpd ==

We begin by installing the necesarry packages. All packages mentioned are included in Whiterussian RC2. To allow clients to use proper encryption we get the corresponding kmod-mppe and kmod-crypto packages as well as the pptpd package.
{{{
ipkg kmod-mppe
ipkg kmod-crypto
ipkg pptpd
}}}

Now we should have all necesarry modules and a typo. The typo is hidden in /etc/init.d/pptpd where in the following line "shlc" should be "slhc". So we go ahead and change it:
{{{
 for m in arc4 sha1 slhc ppp_generic ppp_async ppp_mppe_mppc; do
   insmod $m >/dev/null 2>&1
}}}

While we are at it we mark the startup script executable and put it so that it will load on boot.

{{{
chmod a+x /etc/init.d/ppptp
mv /etc/init.d/pptpd /etc/init.d/S51pptpd
}}}

== Configuring pptpd ==

First we take a look at /etc/pptpd.conf where we see the options parameter pointing to /etc/ppp/options.pptpd but since no such file exists we move the ppp options for pptpd to that file.

{{{
mv /etc/ppp/ppptp-server-options /etc/ppp/options.pptpd
}}}

Also take note of the commented debug option. We uncomment that line for debugging purpose.

Next we change /etc/ppp/options.pptpd to suit our needs. Again start by uncommenting the debug option and the logfile option. Since pptpd was compiled with the "--with-pppd-ip-alloc" flag note that the only way to specify a local ip is with the "<ipaddress>:" line. Change that line to the IP address you want to give the server end of your pptp tunnel, in our example options.pptpd begins:
{{{
debug
logfile /tmp/pptp-server.log
192.168.0.1:
.
.
.
}}}

For pptp clients to be able to connect we need to set the usernames and passwords in /etc/ppp/chap-secrets. The format is:
{{{
username provider password ipaddress
}}}

We have to specify the ipaddress for every client since pptpd ignores the remoteip option in ppptpd.conf. An example chap-secrets looks like this:
{{{
vpnuser * vpnpassword 192.168.0.101
}}}

We are now set and ready to give pptpd a first try. So either insmod all modules and start pptpd or just call the startup script and take a look at the logs if pptpd is starting correctly.
{{{
/etc/init.d/S51pptpd
}}}

== Rules for iptables ==

We need to open port 1723 to accept the PPTP control connections so we add in /etc/firewall.user

{{{
### Allow PPTP control connections from WAN
iptables -t nat -A prerouting_rule -i $WAN -p tcp --dport 1723 -j ACCEPT
iptables        -A input_rule      -i $WAN -p tcp --dport 1723 -j ACCEPT
}}}



== Routing ==

While we now have a VPN ready where the clients can connect to the OpenWrt router we might want to allow the clients to see inside the LAN. Of course we can alway give appropriate routes to server and clients but another simple. In our example we have a LAN network 192.168.0.1/24 on the LAN port of our router. We want multiple clients to connect to the pptpd server and be able to connect to the LAN without the need of client routes. This is especially usefull for Windows machines as they either route everything through the pptpd tunnel or nothing and we want them to be able to connect without much configuration hassle for the users. We will use proxyarp for that purpose and add the following line to /etc/ppp/options.pptp
{{{
proxyarp
}}}

When we restart the pptpd server now we should see something like 
{{{
found interface vlan0 for proxy arp
}}}
in the logs. The pptpd server will now answer arp request for the clients connected through the pptp tunnel and thus the packages are routed correctly to either the according ppp+ device or vlan0. We will have to add additional iptables rules of course (again given without any guarantee of safety, please correct this if you know better):
{{{
### Allow GRE protocol
iptables        -A output_rule             -p 47               -j ACCEPT
iptables        -A input_rule              -p 47               -j ACCEPT

### VPN Section
iptables        -A forwarding_rule -s 10.0.0.0/24 -d 10.0.0.0/24 -j ACCEPT
iptables        -A output_rule     -o ppp+ -s 10.0.0.0/24 -d 10.0.0.0/24 -j ACCEPT
iptables        -A input_rule      -i ppp+ -s 10.0.0.0/24 -d 10.0.0.0/24 -j ACCEPT
}}}


== Finally ==

Gratulations you have now set up your own pptpd and can start connecting with pptp clients. Don't forget to comment the debug options the appropriate config files again.


== Troubleshooting and further information ==

If you can connect to the pptpd and can ping the client from the server and vice versa but are not able to ping anything else refer to this checklist for diagnosis: http://poptop.sourceforge.net/dox/diagnose-forwarding.phtml;

For a Windows XP client howto see here: http://www.windowsecurity.com/articles/Configure-VPN-Connection-Windows-XP.html;

Information on the pptp linux client can be found here: http://pptpclient.sourceforge.net/ or check the appropriate [PPTPClientHowto].
