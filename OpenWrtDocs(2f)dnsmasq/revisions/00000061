'''dnsmasq'''

[[TableOfContents]]

= Introduction =
Dnsmasq is lightweight, easy to configure DNS forwarder and DHCP server. It is designed to provide DNS and, optionally, DHCP, to a small network. It can serve the names of local machines which are not in the global DNS. The DHCP server integrates with the DNS server and allows machines with DHCP-allocated addresses to appear in the DNS with names configured either in each host or in a central configuration file. Dnsmasq supports static and dynamic DHCP leases and BOOTP for network booting of diskless machines.

Dnsmasq is targeted at home networks using NAT and connected to the internet via a modem, cable-modem or ADSL connection but would be a good choice for any small network where low resource use and ease of configuration are important.

= Basic Configuration =
== Nvram vs Config file ==
In white Russian 0.9 the init script use nvram by default[[BR]]
in order to make dnsmask work with the config file(/etc/dnsmasq.conf) we need to remplace the init script(/etc/init.d/S60dnsmasq) by the following script:
{{{ 
[ ! -f /tmp/dhcp.leases ] && {
 touch /tmp/dhcp.leases
 }

 dnsmasq -C /etc/dnsmasq.conf
}}}
== Web Interface Notes ==
Your {{{/etc/ethers}}} and {{{/etc/hosts}}} files can now be modified through the White Russian web interface. While you'll still need to manually setup your {{{/etc/dnsmasq.conf}}} file for things like domains, you can do simple configuration through the web interface.

== DNS Names ==
DNS entries are configured through the {{{/etc/hosts}}} file. dnsmasq will pickup these entries and use them when answering DNS queries on your network.

Format:

{{{
[IP_address] host_name host_name_short ...
}}}
Example:

{{{
192.168.1.1 router OpenWrt localhost
192.168.1.2 ubuntu-desktop
192.168.1.3 ubuntu-laptop
}}}
== DNS Local Domain ==
By default, dnsmasq comes configured to put your hosts into the {{{.lan}}} domain. This is specified in the configuration file as :

{{{
# allow /etc/hosts and dhcp lookups via *.lan
local=/lan/
domain=lan
}}}
You can change this to whatever you'd like your home domain to be. Also, if you want your hosts to be available via your home domain without having to specify the domain in your {{{/etc/hosts}}} file, add the {{{expand-hosts}}} directive to your {{{/etc/dnsmasq.conf}}} file.

As an example, without {{{expand-hosts}}}, you can only reach {{{router, ubuntu-desktop and ubuntu-laptop}}}. With {{{expand-hosts}}} on, you can reach {{{router, router.lan, ubuntu-desktop, ubuntu-desktop.lan, etc}}}. This probably matches what you're looking for anyway.

Without this setting, you'll have to add {{{.lan}}} entries to your host file.

== Related Links ==
 * Homepage
  * http://thekelleys.org.uk/dnsmasq/doc.html
 * Tutorial
  * http://www.enterprisenetworkingplanet.com/netos/article.php/3377351
 * Tutorial
  * http://martybugs.net/wireless/openwrt/dnsmasq.cgi
= FAQ =
== Problem: on starting, dnsmasq reports something like, "Syntax error: network+192.168.1.100" ==
An initial symptom of this problem is that DNS forwarding doesn't seem to work and a call to {{{ps -A}}} reports that dnsmasq isn't running. Check the output of {{{logread}}} for information about what happened when dnsmasq tried to run:

{{{
logread | grep dnsmasq | less
}}}
The problem lies in that the init script for dnsmasq expects the NVRAM variable, {{{dhcp_start}}}, to be in an integer format instead of an IP address (which some other firmwares may leave in your NVRAM after an upgrade to OpenWrt). The variable {{{dhcp_start}}} defines offset from beginning of your network addresses and variable {{{dhcp_num}}} defines how many IP addresses to use in DHCP pool. DHCP pool consists of addresses {{{NETWORK+dhcp_start..NETWORK+dhcp_start+dhcp_num}}} (oops, you have got {{{dhcp_num+1}}} dynamic addresses :-).

Example 1: Your network is {{{192.168.1.0/255.255.255.0}}}, your starting address is {{{192.168.1.100}}}, your ending address is {{{192.168.1.149}}} try this:

{{{
nvram set dhcp_start=100
nvram set dhcp_num=50
nvram commit
killall -9 dnsmasq ; /etc/init.d/S60dnsmasq
}}}
Example 2: Your network is {{{192.168.10.40/255.255.255.248}}}, your starting address is {{{192.168.10.42}}}, your ending address is {{{192.168.10.45}}} try this:

{{{
nvram set dhcp_start=2
nvram set dhcp_num=3
nvram commit
killall -9 dnsmasq ; /etc/init.d/S60dnsmasq
}}}

NOTE: this appears to be fixed in WHITE RUSSIAN 0.9 (dnsmasq - 2.35-1) since the init script will correct {{{dhcp_start}}} entries.

== Configuring dnsmasq to use different IP ranges for wired and wireless ==
Suppose you have the following:

{{{
vlan0     Link encap:Ethernet  HWaddr XX:XX:XX:XX:XX:XX
          inet addr:192.168.1.1    Bcast:192.168.1.255    Mask:255.255.255.0
eth1      Link encap:Ethernet  HWaddr XX:XX:XX:XX:XX:XX
          inet addr:10.75.9.1      Bcast:10.75.9.255      Mask:255.255.255.0
}}}
Simply put 2 "dhcp-range" options in your {{{/etc/dnsmasq.conf}}} file:

{{{
# dhcp-range=[network-id,]<start-addr>,<end-addr>[[,<netmask>],<broadcast>][,<default lease time>]
dhcp-range=lan,192.168.1.101,192.168.1.104,255.255.255.0,24h
dhcp-range=wlan,10.75.9.111,10.75.9.119,255.255.255.0,2h
}}}
You can then use the different "network-id" values with "dhcp-option" to customize the options your DHCP server will supply to your wired and wireless DHCP clients.

for example

{{{
#set the default route for dhcp clients on the wlan side to 10.10.6.33
dhcp-option=wlan,3,10.10.6.33
#set the dns server for the dhcp clients on the wlan side to 10.10.6.33
dhcp-option=wlan,6,10.10.6.33
#set the default route for dhcp clients on the lan side to 10.10.6.1
dhcp-option=lan,3,10.10.6.1
#set the dns server for the dhcp clients on the lan side to 10.10.6.1
dhcp-option=lan,6,10.10.6.1
}}}
== Configuring dnsmasq to generate DHCP responses to ONLY know clients ==
There are situations where you want dnsmasq to generate DHCP addresses for
only know clients (as defined in {{{/etc/ethers}}}).  First, set {{{lan_dhcp_num=0}}}
to indicate that no addresses are to be generated.
Then, modify the file {{{/etc/init.d/S60dnsmasq}}} to included the lines
{{{
        if [ "${num:-150}" = "0" ]; then
                END=static
        fi
}}} 
after the calls to {{{ipcalc.sh}}}.  Restart the daemon or reboot.
== Configuring dnsmasq to associate client hostnames with DHCP-supplied IP addresses ==
You will need the following lines in your {{{/etc/dnsmasq.conf}}} file: (Adjust IP address if your router is not 192.168.1.1)

{{{
dhcp-option=3,192.168.1.1
dhcp-option=6,192.168.1.1
}}}
That's it for dnsmasq on the router. The trick is that the DHCP client must send its hostname during the DHCP negotiation. The {{{dhclient.conf}}} file, which may be in {{{/etc/}}} (debian) or {{{/etc/dhcp3/}}} (kubuntu), needs to have a single line uncommented and edited:

{{{
send host-name "hostname";
}}}
Save the file, then restart the interface. Repeat on all client systems.

== Configuring dnsmasq to broadcast WINS server information ==
You will need the following line in your {{{/etc/dnsmasq.conf}}} file: (Adjust IP address if your WINS server is not 192.168.1.2)

{{{
dhcp-option=44,192.168.1.2
}}}
Now as your machines release and renew DHCP information they will obtain the address of the WINS server automatically.

== Configuring dnsmasq to broadcast External DNS server information ==
The following change to your {{{/etc/dnsmasq.conf}}} file will allow for automatic configuration of your DHCP clients to use DNS servers other than that of the router.

{{{
dhcp-option=6,ipaddress1,ipaddress2
}}}
As your machines release and renew their DHCP configuration they will obtain the address of the new DNS servers automatically.

== SIP-Phones and dnsmasq ==
By default, the option {{{filterwin2k}}} in dnsmasq is activated, which seems to  cause dnsmasq to block any queries for {{{SRV}}} records. {{{SRV}}} records are '''not''' only used by windows computers to find the domaincontroller and such, they are also used by e.g SIP-Phones to find the server responsible for a given domain ({{{SRV}}} records are a kind of generalized {{{MX}}} records). Therefore, the {{{filterwin2k}}} options needs to be disabled (commented out in {{{/etc/dnsmasq.conf}}}) in order to let SIP-Phones work that use dnsmasq as their DNS server.

== Add a secondary DNS ==
what to do if you already have a DNS server(secondary DNS server) but you want your router(primary DNS server) to resolve some of the DNS queries:
simply do the following:
{{{
rm /etc/resolv.conf
}}}
That will remove the resolv.conf simlink[[BR]]
then we will add the ip address of the secondary DNS inside the /etc/resolve.conf file
{{{
echo "nameserver 192.168.1.2">/etc/resolv.conf
}}}
remplace 192.168.1.2 by the ip of your dns server[[BR]]
then reboot or restart the dnsmasq service
{{{
reboot
}}}
or
{{{
killall dnsmasq
/etc/init.d/S60dnsmasq start
}}}

Then you'll need to set-up your secondary dns for resolving internet's DNS queries:[[BR]]
ssh into your router then:
{{{
cat /tmp/resolv.conf.auto
}}}
it will give you something like that:[[BR]]
{{{
nameserver 212.68.193.110
nameserver 212.68.193.196
}}}
copy the information and then add it to your secondary DNS's /etc/resolv.conf:[[BR]]
into your secondary dns do:
{{{
rm /etc/resolv.conf
echo "nameserver 212.68.193.110">>/etc/resolv.conf
echo "nameserver 212.68.193.196">>/etc/resolv.conf
}}}
remplace 212.68.193.110 and 212.68.193.196 by the dns you have get with the cat /tmp/resolv.conf.auto command
