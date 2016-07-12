## Please edit system and help pages ONLY in the moinmaster wiki! For more
## information, please see MoinMaster:MoinPagesEditorGroup.
##acl MoinPagesEditorGroup:read,write,delete,revert All:read
##master-page:HelpTemplate
##master-date:Unknown-Date
#format wiki
#language en
== IPSEC VPN using OpenSWAN to Cisco 851 ==
This guide is for setting up an IPSEC tunnel between a router with OpenWRT and a Cisco 851 router.
The Cisco router needs to have a static IP on the wan side, but the other side (the OpenWRT router) can be connected with a dynamic ip.

The networks in this example are as follows:


---- /!\ '''Edit conflict - other version:''' ----
=== OpenWRT Router ===

---- /!\ '''Edit conflict - your version:''' ----
=== OpenWRT Router ===

---- /!\ '''End of edit conflict''' ----
LAN Ip: 192.168.20.254
Lan network: 192.168.20.0/24
Wan IP: Dynamic


---- /!\ '''Edit conflict - other version:''' ----
=== Cisco Router ===

---- /!\ '''Edit conflict - your version:''' ----
=== Cisco Router ===

---- /!\ '''End of edit conflict''' ----
Lan IP: 192.168.1.254
Lan Network: 192.168.1.0/24
Wan IP: 192.168.40.162


---- /!\ '''Edit conflict - other version:''' ----
== OpenSwan Configuration ==

---- /!\ '''Edit conflict - your version:''' ----
== OpenSwan Configuration ==

---- /!\ '''End of edit conflict''' ----
/etc/ipsec.conf
{{{
# This file holds shared secrets or RSA private keys for inter-Pluto
# authentication.  See ipsec_pluto(8) manpage, and HTML documentation.
        nat_traversal=yes
        # virtual_private=%v4:10.0.0.0/8,%v4:192.168.0.0/16,%v4:172.16.0.0/12
        #
        # enable this if you see "failed to find any available worker"
        nhelpers=0
        interfaces=%defaultroute
        klipsdebug=none
        plutodebug=none

# Add connections here
conn tunnelipsec
        type=tunnel
        authby=secret
        left=192.168.40.160
        leftnexthop=%defaultroute
        leftsubnet=192.168.20.0/24
        right=192.168.40.162
        rightsubnet=192.168.1.0/24
        esp=3des-md5-96
        keyexchange=ike
        pfs=no
        auth=esp
        auto=start
# sample VPN connections, see /etc/ipsec.d/examples/

#Disable Opportunistic Encryption
include /etc/ipsec.d/examples/no_oe.conf
}}}

/etc/ipsec.secrets
{{{
# This file holds shared secrets or RSA private keys for inter-Pluto
# authentication.  See ipsec_pluto(8) manpage, and HTML documentation.
  
# You might have an RSA key here depending on if you installed from a .deb
   
: PSK "secretkey"

}}} 
These lines need to be added to:
/etc/firewall.user
{{{
### allow ipsec traffic from your wan port to the router
iptables -A input_wan -p esp              -j ACCEPT # allow IPSEC
iptables -A input_wan -p udp --dport 500  -j ACCEPT # allow ISAKMP
iptables -A input_wan -p udp --dport 4500 -j ACCEPT # allow NAT-T
### disable nat for the remote peer subnet, in this example 192.168.2.0/24
iptables -t nat -A postrouting_rule -d 192.168.1.0/24 -j ACCEPT
### Allow any traffic between your local LAN and remote peer LAN
iptables -A forwarding_rule -i $LAN -o ipsec0 -j ACCEPT
iptables -A forwarding_rule -i ipsec0 -o $LAN -j ACCEPT
}}}


---- /!\ '''Edit conflict - other version:''' ----
== Cisco Router ==

---- /!\ '''Edit conflict - your version:''' ----
== Cisco Router ==

---- /!\ '''End of edit conflict''' ----
These commands configure the Cisco to have the same IPSEC policy as Openswan, and disable NAT from the remote network.
This is handled in the 101 access list
{{{
crypto isakmp policy 1
 encr 3des
 hash md5
 authentication pre-share
 group 2

crypto isakmp key secretkey address 0.0.0.0 0.0.0.0

crypto ipsec transform-set RemoteSiteName esp-3des esp-md5-hmac 
!
crypto dynamic-map SDM_DYNMAP_1 1
 set transform-set RemoteSiteName 
 match address 100

crypto map SDM_CMAP_1 65535 ipsec-isakmp dynamic SDM_DYNMAP_1 

interface FastEthernet4
 description Connected to WAN
 ip address dhcp
 no ip redirects
 no ip proxy-arp
 ip nat outside
 ip nat enable
 ip virtual-reassembly
 duplex auto
 speed auto
 crypto map SDM_CMAP_1

interface Vlan1
 description Connected to LAN
 ip address 192.168.1.254 255.255.255.0
 no ip redirects
 no ip unreachables
 no ip proxy-arp
 ip nat inside
 ip nat enable
 ip virtual-reassembly
 ip tcp adjust-mss 1452

ip nat inside source route-map SDM_RMAP_1 interface FastEthernet4 overload

access-list 100 remark SDM_ACL Category=4
access-list 100 remark IPSec Rule
access-list 100 permit ip 192.168.1.0 0.0.0.255 192.168.20.0 0.0.0.255
access-list 101 deny   ip any 192.168.20.0 0.0.0.255
access-list 101 remark SDM_ACL Category=2
access-list 101 remark IPSec Rule
access-list 101 permit ip 192.168.1.0 0.0.0.255 any

route-map SDM_RMAP_1 permit 1
 match ip address 101
}}}
