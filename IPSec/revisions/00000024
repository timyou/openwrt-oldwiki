'''IPSec Howto'''

This section contains information on howto setup Plain IPSec as protection for your WLAN. It provides a clean & simple protection mechanism with a high level of security. For Windows and OS X Clients another way might be more comfortable since both, Windows and OS X, don't come with graphical clients (and that is what these users are used to) for plain IPSec. These Platforms provide clients for a protocol defined in rfc 3193 using [:L2TP+IPSEC].

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
ipkg install openswan kmod-openswan ntpclient
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
