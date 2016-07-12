'''IPSec Howto'''

This section is under a first and raw version - Please correct, annotate - but not complain yet.


[[TableOfContents]]


= Plain IPSec =
(edit me - I won't cover this section)

= L2TP over IPSec =
Read http://www.jacco2.dds.nl/networking/freeswan-l2tp.html which is a very useful and detailed description on how to setup l2tp over ipsec

== Devide Wireless from wired network ==

== Install openswan ==
{{{
ipkg install openswan kmod_openswan
}}}

Adapt ipsec.conf
A good start is:
{{{
config setup
        interfaces="ipsec0=eth1"

conn L2TP-PSK
        authby=secret
        ike=aes-sha,3des-sha
        esp=aes-sha1,3des-sha1
        pfs=no
        rekey=no
        keyingtries=3
        left=10.0.1.1
        leftprotoport=17/1701
        right=%any
        rightprotoport=17/%any
        auto=add

#Disable Opportunistic Encryption
include /etc/ipsec.d/examples/no_oe.conf
}}}

explain options here.


== Install l2tpd ==
Get l2tpd from http://www.linuxops.net/ipkg/l2tpd_0.69_mipsel.ipk and install
{{{
ipkg install l2tpd_0.69_mipsel.ipk
}}}

Config l2tpd according to your needs
/etc/l2tpd/l2tpd.conf might be a good start - which is not sure since l2tpd doesn't work yet
{{{
[global]

[lns default]
ip range = 10.10.0.201-10.10.0.220
local ip = 10.10.0.199
require chap = yes
refuse pap = yes
require authentication = yes
name = home
ppp debug = yes
pppoptfile = /etc/ppp/options.l2tpd
length bit = yes
}}}

You need /etc/ppp/options.l2tpd
this one might server as a sample - but this too doesn't work yet
{{{
ipcp-accept-local
ipcp-accept-remote
ms-dns 10.10.0.1
noccp
auth
crtscts
idle 1800
mtu 1400
mru 1400
nodefaultroute
debug
lock
proxyarp
connect-delay 5000
}}}

now update chap-secrets according to your needs.

pray!
