A small HowTo on how to setup siproxd with transparent proxy and the Nokia E61.

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
