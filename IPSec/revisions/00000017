'''IPSec Howto'''

'''NOTE:''' This section is under development- Please correct, annotate - but do not complain yet.


[[TableOfContents]]


= Plain IPSec =

This configuration assumes an OpenWRT router with dynamic Internet connection using DSL and a central site with fixed IP addresses (typical road warrior scenario). The goal is to set up IPSEC between both sites so the LAN and/or WIFI connected to the OpenWRT router can talk to the LAN connected to the central IPSEC gatway. For the sample configuration we assume the following setup:

||central site IP address||1.2.3.4||
||central site LAN||192.168.2.0/24||
||central site name||central.site.vpn||
||road warrior LAN||192.168.1.0/24||
||road warrior email||road@warrior.vpn||

== Optionally devide wireless from wired network ==

If LAN and WIFI should be handled differently by the central site, it makes sense to seperate them and use two differnet IPSEC tunnels.

== Install openswan ==
{{{
ipkg install openswan kmod_openswan ntpclient
}}}

== Configuration ==

In this example, a configuration using a X.509 PKI is being used. Shared key is not really useful for road warrior setups, as it would require all road warriors to use the same shared key.

=== Create CA and certificates for all gateways ===

In this example, the hostname is used as common name for the central station and the email address for the road warrior. Some hints on how to use openssl to manage a PKI can be found at http://www.natecarlson.com/linux/ipsec-x509.php or http://freifunk.net/wiki/X509
### Please replace the second link if you find a similar tutorial in English language

On the OpenWRT box, copy the CA certificate to /etc/ipsec.d/cacerts/cacert.pem, the road warrior certificate to /etc/ipsec.d/certs/roadwarrior.pem and the private key to /etc/ipsec.d/private/roadwarriorkey.pem

=== Create /etc/ipsec.conf ===

A sample configuration is:
{{{
version 2.0     # conforms to second version of ipsec.conf specification

# basic configuration
config setup
        # plutodebug / klipsdebug = "all", "none" or a combation from below:
        # "raw crypt parsing emitting control klips pfkey natt x509 private"
        # eg:
        plutodebug="none"
        klipsdebug="none"
        #
        # Only enable klipsdebug=all if you are a developer
        #
        # NAT-TRAVERSAL support, see README.NAT-Traversal
        nat_traversal=no
        # virtual_private=%v4:10.0.0.0/8,%v4:192.168.0.0/16,%4:172.16.0.0/12
        interfaces=%defaultroute

conn central
        authby=rsasig
        esp=aes-sha1
        right=1.2.3.4
        rightsubnet=192.168.2.0/24
        rightrsasigkey=%cert
        rightid=@central.site.vpn
        left=%defaultroute
        leftsubnet=192.168.1.0/24
        leftrsasigkey=%cert
        leftid=road@warrior.vpn
        leftcert=roadwarrior.pem
        dpddelay=5
        dpdtimeout=15
        dpdaction=restart
        auto=start
        #keylife=20m
        keyingtries=%forever

#Disable Opportunistic Encryption
include /etc/ipsec.d/examples/no_oe.conf
}}}

=== Create /etc/ipsec.secrets ===

This file contains the name of the private key file and the passphrase needed to open the file:
{{{
: RSA roadwarriorkey.pem "passphrase"
}}}

=== Permissions ===

Make sure the permissions of /etc/ipsec.secrets and /etc/ipsec.d/private/* allow read access only to root (chmod 400).

=== Hotplug ===

Configure the hotplug system to start and stop OpenSWAN each time the DSL connection is cut off by the provider:

/etc/hotplug.d/iface/30-ipsec
{{{
#!/bin/sh

if [ "$PROTO" != "ppp" ]; then exit; fi

USER=root
export USER

case "$ACTION" in
        ifup)
                /etc/rc.d/init.d/ipsec start
                ;;
        ifdown)
                /etc/rc.d/init.d/ipsec stop
                ;;
esac
}}}

=== Firewall ===

Make sure to open your firewall for ESP and ISAKMP traffic (and maybe NAT-T if your setup requires nat-traversal) and disable NAT for
the LAN of the central site:

Example /etc/firewall.user:
{{{
iptables -A input_rule -p esp -s 1.2.3.4              -j ACCEPT  # allow IPSEC
iptables -A input_rule -p udp -s 1.2.3.4 --dport 500  -j ACCEPT  # allow ISAKMP
iptables -A input_rule -p udp -s 1.2.3.4 --dport 4500 -j ACCEPT  # allow NAT-T
iptables -t nat -A postrouting_rule -d 192.168.2.0/24 -j ACCEPT
# Allow any traffic between road warrior LAN and central LAN
#iptables -A forwarding_rule -i $LAN -o ipsec0 -j ACCEPT
#iptables -A forwarding_rule -i ipsec0 -o $LAN -j ACCEPT
}}}
=== Bugfix (for RC4) ===

As of Whiterussian RC4, to fix a bug replace /etc/hotplug.d/iface/10-ntpclient by https://dev.openwrt.org/file/trunk/openwrt/package/ntpclient/files/ntpclient.init.

=== Startup files ===

Optionally remove /etc/init.d/60ipsec, as this script is not really needed in this setup.

= L2TP over IPSec =
Read http://www.jacco2.dds.nl/networking/freeswan-l2tp.html which is a very useful and detailed description on how to setup l2tp over ipsec

Instructions are for rc4 on a wrt54gs1.1

== Divide wireless from wired network ==
Divide the wireless from the wired network as described in Self:Configuration

== Needed Packages ==
You need to install OpenSwan, the OpenSwan-Kernel-Module and the L2TPd:
{{{
ipkg install openswan kmod_openswan l2tpd
}}}

To debug your setup it is a good idea to install tcpdump and nmap right away:
{{{
ipkg install tcpdump nmap
}}}

== Configure IPSec ==
Modify ipsec.conf
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


== Configure l2tpd ==

Configure l2tpd according to your needs
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

now update /etc/ppp/chap-secrets according to your needs:
this one is mine:
{{{
#USERNAME  PROVIDER  PASSWORD  IPADDRESS
<user>     *         "<password>" *
}}}

== Aftermath ==
pray!
