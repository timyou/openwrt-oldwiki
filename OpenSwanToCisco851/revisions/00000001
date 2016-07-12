## Please edit system and help pages ONLY in the moinmaster wiki! For more
## information, please see MoinMaster:MoinPagesEditorGroup.
##acl MoinPagesEditorGroup:read,write,delete,revert All:read
##master-page:HelpTemplate
##master-date:Unknown-Date
#format wiki
#language en
== IPSEC VPN using OpenSWAN to Cisco 851 ==


=== OpenSwan ===
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

=== Display ===
xxx
