'''NOTE:''' This section is under development- Please correct, annotate - but do not complain yet.

'''Caution:''' This Setup doesn't work yet.

= Introduction =
The howto part of this section can be read as a description howto get as far as got configuring l2tp over ipsec. Corrections are highly appreciated.

At the moment the l2tp-daemon is causing trouble. So the ipsec section is kept as easy as possible just to be able to communicate with l2tpd.

[[TableOfContents]]

= Howto =
Read http://www.jacco2.dds.nl/networking/freeswan-l2tp.html which is a very useful and detailed description on how to setup l2tp over ipsec

Instructions are for rc5 on a wrt54gs1.1



== Divide wireless from wired network ==
Divide the wireless from the wired network as described in [:Configuration]

== Base Configuration ==
The wrt has 10.1.1.1 on at least one wired-port, the rig you're using to configure the stuff has 10.1.1.2 on the wire.
The wrt has 10.1.10.1 on the wireless interface, where your test rig has 10.1.10.2. 
Netmasks are 255.255.255.0 in both cases - Firewall is set up to allow everything.

The following relies on this configuration.


== Needed Packages ==
You need to install OpenSwan, the OpenSwan-Kernel-Module and the L2TPd:
{{{
ipkg install openswan kmod-openswan l2tpd
}}}

== Debug stuff which is not needed for the real setup ==
To debug your setup it is a good idea to install tcpdump and nmap right away:
{{{
ipkg install tcpdump nmap
}}}

Having syslogd running to log events from the router to your rig is a good idea too. Howto set this up is beyond the scope of this document.

== Configure IPSec ==
ipsec.conf should look like this:
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
        left=10.1.10.1
        leftprotoport=17/1701
        right=%any
        rightprotoport=17/%any
        auto=add

#Disable Opportunistic Encryption
include /etc/ipsec.d/examples/no_oe.conf
}}}

/etc/ipsec.secrets
{{{
10.1.10.1 %any: PSK "this-is-a-test-i-will-change-it-later"
}}}


It's time for a first test:

Now lets see wether this part is working:
Reboot and bring up tcpdump on the ipsec interface
{{{
tcpdump -i ipsec0
}}}

Now - when you connect to your wrt using your l2tp/ipsec client it should not work yet - but in case you set things up correctly you should see incoming packages on ipsec0.

 
== Configure l2tpd ==

/etc/l2tpd/l2tpd.conf 
{{{
[global]

[lns default]
ip range = 10.1.1.202-10.1.1.220
local ip = 10.1.1.201
require chap = yes
refuse pap = yes
require authentication = yes
name = home
ppp debug = yes
pppoptfile = /etc/ppp/options.l2tpd
length bit = yes
}}}

/etc/ppp/options.l2tpd
{{{
ipcp-accept-local
ipcp-accept-remote
ms-dns 10.1.10.1
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

/etc/ppp/chap-secrets
{{{
#USERNAME  PROVIDER  PASSWORD  IPADDRESS
duffy     *         "duck" *
}}}

= Errors = 
