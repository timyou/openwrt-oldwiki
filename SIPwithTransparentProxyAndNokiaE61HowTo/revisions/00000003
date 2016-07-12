= A small HowTo on how to setup siproxd with transparent proxy and the Nokia E61. =

 1. Install '''ipkg install siproxd'''
 1. Install '''ipkg install iptables-mod-nat'''
 1. Install '''siproxd.conf'''
  {{{
  if_inbound = br0 
  if_outbound = vlan1 
  ... 
  outbound_domain_name = proxy01.sipphone.com 
  outbound_domain_host = proxy01.sipphone.com 
  outbound_domain_port = 5060 
  }}}
 1. Edit '''siproxd_passwd.cfg''' (add your user)
 1. '''mkdir -p /var/lib/siproxd'''
 1. '''chmod 777 /var/lib/siproxd'''
 1. '''mkdir -p /var/run/siproxd'''
 1. '''chmod 777 /var/run/siproxd'''
 1. Edit '''firewall.user''' and append
  {{{
   insmod ipt_REDIRECT
   iptables -A input_vlan1 -p udp -m udp --dport 7070:7079 -j ACCEPT 
   iptables -t nat -I prerouting_rule -m udp -p udp -i br0 --destination-port 5060 -j   REDIRECT 
  }}}


On the Nokia E61 I got the following settings

 * Public user name: sip:<userid>@proxy01.sipphone.com
 * Use compression: no
 * Registration: always on
 * Use security: no
 * Proxy server
   * Proxy server address: proxy01.sipphone.com
   * Realm: proxy01.sipphone.com
   * Username: <userid>
   * Password: <password>
   * Allow loose routing: yes
   * Transport type: UDP
   * Port: 5060
 * Registrar server
   * Registrar serv. addr.: proxy01.sipphone.com
   * Realm: proxy01.sipphone.com
   * Username: <userid>
   * Password: <password>
   * Transport type: UDP
   * Port: 5060

Have fun, though I have a litte knacking during calls. Don't know the reason yet.

----
= Another way of making NOKIA E60, E61 (and probably other) phones work behind the OpenWRT router. =

Those "litte knackings during calls" mentioned above may have caused by high CPU consumption of siproxd processes. I have two SIP clients connected and CPU usage sometimes raises up to 40%. I also noticed much longer delays when establishing or receiving calls (really longer, up to 10-15 seconds depending on the system load). 

Another way of making some SIP clients (like NOKIA E60 or E61) to work through OpenWRT is changing the default NAT behaviour from MASQUERADE to SourceNAT (SNAT), which will make your NOKIA (or any other SIP client) transparently work with OpenWRT ''without'' siproxd and additional ipt_REDIRECT firewall rules. 

This setup was tested with NOKIA E60 phone and Asterisk VoIP server (Trixbox based). I think it should work with other service providers as well. If you are using Asterisk and this solution is not working for you, try to add the following parameters to your extension configuration of the Asterisk box:

  {{{
   nat=yes
   qualify=yes
  }}}

If you have already followed the above instructions and installed '''siproxd''' and '''iptables-mod-nat''', then you may safely uninstall them to save flash space:
  1. '''ipkg remove siproxd'''
  1. '''ipkg remove libosip2'''
  1. '''ipkg remove iptables-mod-nat'''

And you '''have to remove''' those three lines from '''/etc/firewall.user''' (if you have already appended them):
  {{{
   insmod ipt_REDIRECT
   iptables -A input_vlan1 -p udp -m udp --dport 7070:7079 -j ACCEPT
   iptables -t nat -I prerouting_rule -m udp -p udp -i br0 --destination-port 5060 -j REDIRECT
  }}}

After it's done, edit the '''/etc/init.d/S45firewall''' script and change the following:

1. add this line at the beginning of the file right after the LAN=...... statement:
  {{{
  WAN=$(nvram get wan_ifname)
  LAN=$(nvram get lan_ifname)
  EXTIP=$(ifconfig vlan1 | grep 'inet addr' | cut -f 2 -d\: | cut -f 1 -d' ')
  }}}

This line will automagically extract your WAN ip address from '''ifconfig''' output to use later in this script (maybe there is a more correct way to do this but I don't know).

2. replace the following line at the MASQ section:
  {{{
  iptables -t nat -A POSTROUTING -o $WAN -j MASQUERADE
  }}}
with
  {{{
  iptables -t nat -A POSTROUTING -o $WAN -j SNAT --to-source $EXTIP
  }}}

That's all, just save the file and reboot the router. The NOKIA SIP account configuration should remain unchanged and it will work with your new settings.

SIP calls work without any problems and calls are established with no delay at all.
