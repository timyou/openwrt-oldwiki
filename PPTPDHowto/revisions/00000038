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
/etc/init.d/S50pptpd start}}}
== Configure Tunnel Local IP Address ==
The default IP address of the server end of the tunnel is 172.16.1.1, and is set in the file ''/etc/ppp/options.pptpd'', with a colon after it, like this:

{{{
172.16.1.1:}}}
Change this if you want a different IP address. There is no need to restart ''pptpd'' if you change this file, because it is used by ''pppd'' as soon as the next connection arrives. The file contains options for ''pppd'', see ''man pppd'' on a Linux system for more information on the options available.

== Configure Tunnel Remote IP Addresses ==
Add lines to ''/etc/ppp/chap-secrets'' for each client. The format is:

{{{
username provider password ipaddress}}}
Add an IP address for every client. An example ''chap-secrets'' looks like this:

{{{
vpnuser pptp-server vpnpassword 172.16.1.2}}}
See ''man pppd'' on a Linux system for more information on this file. Take care that the provider field matches the ''name'' option in ''/etc/ppp/options.pptpd''. The default is ''pptp-server''.

/!\ For the ''bin'' and ''pptp'' builds of OpenWrt, the file will start out being a symbolic link to a template in ''/rom'', so remove the link, copy the template, and make sure it is ''chmod 600''.

/!\ It is important to set an IP address rather than use the default asterisk.  If you use an asterisk, the peer may propose it's own address, which could cause a routing loop.  This results in very large transmit counters on ''ifconfig ppp0'' and a badly performing router, as it spends all it's time trying to move packets through the loop.

== Configure Firewall ==
For your security !OpenWrt will ignore connections on the WAN interface, but accept connection from a client on the LAN or wireless interfaces.  If your client is to connect on the WAN interface, edit the ''/etc/firewall.user'' file and add the following:

{{{
### Allow PPTP control connections from WAN
iptables -t nat -A prerouting_rule -i $WAN -p tcp --dport 1723 -j ACCEPT
iptables        -A input_rule      -i $WAN -p tcp --dport 1723 -j ACCEPT
### Allow GRE protocol (used by PPTP data stream)
iptables        -A output_rule             -p 47               -j ACCEPT
iptables        -A input_rule              -p 47               -j ACCEPT
}}}
See the ["OpenWrtDocs/Configuration"] section ''iptables  - Firewall'' for more help with firewall configuration.

== Test Connection ==
Tell a client to connect to the PPTP server, using the username and password you set in ''chap-secrets''.

The connection should work, ping between the client and the server should work, but you may have to do some more configuring to let the client use your PPTP server as a gateway to the internet, or to see inside your LAN.  See the routing section below.

== Configure Debug Logging ==
If you have problems making a connection, increase the amount of information logged:

 * edit ''/etc/pptpd.conf'' and add the line ''debug'', and restart ''pptpd'' using ''/etc/init.d/S50pptpd stop'' followed by ''/etc/init.d/S50pptpd start'',
 * edit ''/etc/ppp/options.pptpd'' and add the line ''debug'', and the line ''logfile "/tmp/pptpd.log"'' ... these changes take effect on next client connection, there is no need to restart ''pptpd''.
To understand the ''pppd'' debug log, read these key sections of the PPTP Client Diagnosis HOWTO:

 * [http://pptpclient.sourceforge.net/howto-diagnosis.phtml#confreqacknakrej What does ConfReq, ConfAck, ConfNak, and ConfRej mean?]
 * [http://pptpclient.sourceforge.net/howto-diagnosis.phtml#mppe_bits What are those CCP MPPE bitmasks?]
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
iptables        -A forwarding_rule -s 192.168.0.0/24 -d 192.168.0.0/24 -j ACCEPT
iptables        -A output_rule     -o ppp+ -s 192.168.0.0/24 -d 192.168.0.0/24 -j ACCEPT
iptables        -A input_rule      -i ppp+ -s 192.168.0.0/24 -d 192.168.0.0/24 -j ACCEPT
# allow VPN connections to get out WAN interface (to internet)
iptables        -A forwarding_rule -i ppp+ -o $WAN -j ACCEPT
}}}
I had better luck with this:

{{{
### VPN Section
iptables        -A forwarding_rule -s 172.16.1.0/24 -d 192.168.1.0/24 -j ACCEPT
iptables        -A forwarding_rule -s 192.168.1.0/24 -d 172.16.1.0/24 -j ACCEPT
}}}
It alows two way communication. NOTE:  The ip address range in the iptables section above is the LAN ip address range.

== Setup for Windows filesharing ==
If you have Windows PPTP clients and you want them to be able to access file shares on the LAN, you need to set the  IP addresses of the PPTP clients to be on the same subnet as the LAN.  This is because of a limitation in proxyarp.  They also cannot be on the same subnet as the local addresses of the PPTP clients.  For example, if your PPTP clients have addresses in the 192.168.0.0/24 subnet, you can set you LAN to be 192.168.30.0/24 with DCHP assigning 192.168.30.50-192.168.30.100.  You can set the IP address of the PPTP server to be 192.168.30.200 by adding the following line to /etc/ppp/options.pptpd:

{{{
192.168.30.200:
}}}

You can then assign the client IP address beginning with 192.168.30.201.  Use the following settings for VPN in /etc/firewall.user.

{{{
### VPN Section
iptables        -A forwarding_rule -s 192.168.30.0/24 -d 192.168.30.0/24 -j ACCEPT
iptables        -A output_rule     -o ppp+ -s 192.168.30.0/24 -d 192.168.30.0/24 -j ACCEPT
iptables        -A input_rule      -i ppp+ -s 192.168.30.0/24 -d 192.168.30.0/24 -j ACCEPT
# allow VPN connections to get out WAN interface (to internet)
iptables        -A forwarding_rule -i ppp+ -o $WAN -j ACCEPT
}}}

You will now be able to access file shares by IP address.  For example, you can type
{{{
\\192.168.30.50
}}}
into the address bar of Windows Explorer.  Network neighborhood still doesn't detect available computers.  If anyone knows how to make this work please post the instructions here.
==> In general the way for computers to appear in Net-Hood is to have server (master browser) to populate browse list across networks + have hosts or lmhosts file setup on client machines(that is only way I discovered so far). For samba servers you need to have config options in smb.conf:  (ip address of router/name of workgroup), but I'm not sure how it works on wrt (as it only have cups I couldn't get them installed due to space limitation) 
remote announce = 192.168.11.1/UR-WG-NAME
and hosts file in windoze (c:\Windows\System32\drivers\etc\hosts) like
192.168.11.10    mypc       mypc.behind-wrt54g.org
..

== Troubleshooting ==
If you can connect to the ''pptpd'' and can ping the client from the server and vice versa but are not able to ping anything else refer to this [http://poptop.sourceforge.net/dox/diagnose-forwarding.phtml checklist for diagnosis]

There is a [http://www.windowsecurity.com/articles/Configure-VPN-Connection-Windows-XP.html Windows XP client HOWTO] that may help.

There is also the [http://pptpclient.sourceforge.net/ PPTP Client for Linux] or check the !OpenWrt  ["PPTPClientHowto"].

If the PPTP clients are behind an Actiontec DSL Modem/Router, only one of them will be able to connect.  This is do to a bug in the Actiontec.  Apparently it locks the connection to one client.  If the router is rebooted the first client to reconnect is locked in.  Putting the Actiontec into bridged mode and using a different router will probably bypass the problem.  Does anyone else have any experience with this?

## reviewed 2006-03-27 by james.cameron@hp.com, the current pptpd maintainer, against White Russian RC5 and pptpd 1.2.3-2 ipk
