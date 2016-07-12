== PPTPD on OpenWrt ==

This HOWTO describes how to install and configure ''pptpd'' on !OpenWrt.

== Install pptpd ==

Install the ''pptpd'' package:
{{{
ipkg install pptpd}}}

This will also install ''kmod-mppe'' and ''kmod-crypto'' packages if they are not yet installed.

== Start pptpd ==

The package installs without running ''pptpd''.  To start it this once:
{{{
/etc/init.d/pptpd start}}}

== Configure OpenWrt to start on reboot ==

The package installs without running ''pptpd'' on boot.  To configure !OpenWrt to start ''pptpd'' on boot, move the script so that ''rcS'' runs it:
{{{
cd /etc/init.d && mv pptpd S50pptpd}}}

== Configure Tunnel Local IP Address ==

The default IP address of the server end of the tunnel is 172.16.1.1, and is set in the file ''/etc/ppp/options.pptpd'', with a colon after it, like this:
{{{
172.16.1.1:}}}

Change this if you want a different IP address.  There is no need to restart ''pptpd'' if you change this file.
See ''man pppd'' on a Linux system for more information on this file.

== Configure Tunnel Remote IP Addresses ==

Add lines to ''/etc/ppp/chap-secrets'' for each client. The format is:
{{{
username provider password ipaddress}}}

Specify the IP address for every client.
An example ''chap-secrets'' looks like this:
{{{
vpnuser pptp-server vpnpassword 172.16.1.2}}}

See ''man pppd'' on a Linux system for more information on this file.  Take care that the provider field matches the ''name'' option in ''/etc/ppp/options.pptpd''.  The default is ''pptp-server''.

== Test Connection ==

Direct a client to connect to the PPTP server, using the username and password you set in ''chap-secrets''.

== Configure Debug Logging ==

If you have problems making a connection, increase the amount of information logged:
 * edit ''/etc/pptpd.conf'' and add the line ''debug'', and restart ''pptpd'' using ''/etc/init.d/pptpd stop'' followed by ''/etc/init.d/pptpd start''
 * edit ''/etc/ppp/options.pptpd'' and add the line ''debug'', and the line ''logfile "/tmp/pptpd.log"'' ... these changes take effect on next client connection, there is no need to restart ''pptpd''

== Configure iptables Rules ==

If you have no iptables configuration, this section is not necessary.

Open TCP port 1723 to accept the PPTP control connections, and open protocol 47 for the data stream, so add in ''/etc/firewall.user'':

{{{
### Allow PPTP control connections from WAN
iptables -t nat -A prerouting_rule -i $WAN -p tcp --dport 1723 -j ACCEPT
iptables        -A input_rule      -i $WAN -p tcp --dport 1723 -j ACCEPT

### Allow GRE protocol (used by PPTP data stream)
iptables        -A output_rule             -p 47               -j ACCEPT
iptables        -A input_rule              -p 47               -j ACCEPT
}}}

== Configure Routing ==

While we now have a VPN ready where the clients can connect to the !OpenWrt router we might want to allow the clients to see inside the LAN. Of course we can alway give appropriate routes to server and clients but there's another way. In our example we have a LAN network 192.168.0.1/24 on the LAN port of our router. We want multiple clients to connect to the ''pptpd'' server and be able to connect to the LAN without the need of client routes. This is especially useful for Windows machines as they either route everything through the ''pptpd'' tunnel or nothing and we want them to be able to connect without much configuration hassle for the users. We will use ''proxyarp'' for that purpose and add the following line to ''/etc/ppp/options.pptpd'':
{{{
proxyarp
}}}

When the next client connection arrives you should see something like:
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

== Troubleshooting ==

If you can connect to the ''pptpd'' and can ping the client from the server and vice versa but are not able to ping anything else refer to this [http://poptop.sourceforge.net/dox/diagnose-forwarding.phtml checklist for diagnosis]

For a Windows XP client HOWTO see here: [http://www.windowsecurity.com/articles/Configure-VPN-Connection-Windows-XP.html]

Information on the PPTP Linux client can be found here: [http://pptpclient.sourceforge.net/] or check the appropriate ["PPTPClientHowto"].

## reviewed 2006-03-15 by james.cameron@hp.com, the current pptpd maintainer, against pptpd 1.2.3-2 ipk
