## Please edit system and help pages ONLY in the moinmaster wiki! For more
## information, please see MoinMaster:MoinPagesEditorGroup.
##acl MoinPagesEditorGroup:read,write,delete,revert All:read
##master-date:Unknown-Date
#format wiki
#language en

{i} Note: this page is brand new and may contain errors.



[[TableOfContents]]

= OpenWRT and IPTables Overview =
OpenWRT can serve as a very flexible network firewall. The templates and configuration tools included with the distribution should prove sufficient for most applications; however, for a more complex installation, it may be necessary to extend the iptables configuration more directly than the web-based tools permit.

OpenWRT defines a set of rules for network address translation (NAT) and packet filtering.  These rules are arranged to allow users to extend them without needing to reorganize OpenWRT's iptables structure. Administrators will benefit from creating a local configuration that fits within the structure OpenWRT expects.  As this document will show, a high degree of flexibility can be achieved ''without'' modifying OpenWRT's distribution start-up or configuration scripts.

The reader should already be familiar with iptables and have reviewed the [http://iptables-tutorial.frozentux.net/iptables-tutorial.html Iptables Tutorial], available in many places including [http://iptables-tutorial.frozentux.net/iptables-tutorial.html here] and [http://www.faqs.org/docs/iptables/ here].

= The Firewall Startup Script =
OpenWRT begins firewall initialization by running a startup script in ''/etc/init.d''. This script sets default policies for all chains, creates basic targets for accepting and dropping packets, and configures basic network address translation. It then calls the user configuration file ''/etc/firewall.user''. '''It is neither necessary nor desirable to modify the startup script. Customization should be done in the user configuration file.'''

== Environment Variables ==
The following environment variables are available to your ''/etc/firewall.user'' script:
||'''Variable''' ||'''Description''' ||'''Example''' ||
||WAN ||Name of the external interface ||vlan1 ||
||LAN ||Name of the internal interface ||vlan0 ||
||WANDEV ||Name of the external (WAN) device ||For typical installations, this will be the same as $WAN and can be ignored. ||


'''Note:''' These variables are not exported to the environment. They are only available in the ''/etc/firewall.user'' script because it is ''included'' by the startup script. This fact is important if you plan to split your user configuration into multiple files.

== Default chains ==
The startup script defines a few chains that the ''/etc/firewall.user'' may wish to use:
||'''Rule Name''' ||'''Description''' ||
||LAN_ACCEPT ||Serves as a conditional target that ACCEPTs packets if the originating interface is the LAN, but does nothing if the packet originated from a non-LAN interface. (In most cases, LAN means the combination of LAN and WLAN). ||
||NEW ||Performs burst limit checking during nat prerouting.  This is an internal rule not intended to be accessed by the user, explained here for educational purposes only.  Its purpose is to limit the number of new address translation mappings to protect against certain kinds of denial of service attacks. ||


= OpenWrt Chains =
The following diagram is adapted from the IPTables tutorial, with detail added to explain what rules OpenWRT defines.  Detail boxes describes the actions that take place in the firewall start-up script (which, as a polite administrator, you will not modify).

http://wiki.autofrog.com/_media/openwrt/openwrtiptables.png

= Rules for User Modification =
== prerouting_rule (nat) ==
This rule defines incoming network address translation on all interfaces, including the LAN.  Typical installations do not need to use this rule, as inbound address translation only occurs from the WAN interface, which has its own rule (below).

Termination possibilities from this chain include:
||'''Target''' ||'''Description''' ||
||DNAT ||Remap the destination address, port, or both. ||


If you think you need to modify this rule consider that network address translation usually occurs on dynamic outbound connections or on static inbound connections.  This rule applies to neither of those situations.  An example situation where this ''would'' be applicable is if you wished to redirect outbound connections to an external server and remap them to a different place.

You probably don't need this rule.

== prerouting_wan (nat) ==
Unlike ''prerouting_rule'', this rule is important. It allows you to map external (WAN) connection requests to an internal (LAN) service, implementing what is casually known as ''port redirection''.

For example, suppose you want to map all HTTP requests into your firewall and direct them to the internal server 192.168.1.2:

{{{iptables --table nat --append prerouting_wan --protocol tcp --dport 80 --jump DNAT --to 192.168.1.2:80}}}

Note that for port redirection, ''nat'' alone is not sufficient; you also have to allow the packet to pass in the appropriate filter, typically ''input_wan'' or ''forwarding_wan''.

== input_rule (filter) ==
This filter checks incoming packets, regardless of the input interface.  This rule only applies to packets destined for OpenWrt.

This chain applies to all packets destined for local services, i.e. running on the firewall itself, regardless of the originating interface.

Possible terminations:
||ACCEPT ||Packet is forwarded to the local service regardless of originating interface. ||
||LAN_ACCEPT ||Packet is forwarded to the local service ''only'' if it originated from the internal network (LAN). ||
||DROP || Packet is dropped. ||
||RETURN ||No additional processing in this rule; packet is passed to ''input_wan'' if it originated from the WAN interface. ||


If you wish to block packets from ''all'' sources, this is the place to do it.  For example, if you wish to entirely close http access, from both the WAN and LAN, you could do this:

{{{iptables --append input_rule --protocol tcp --dport 80 --jump DROP}}}

Since firewalls are typically concerned with protecting themselves from the outside, use of this chain is atypical and probably not necessary.

== input_wan (filter) ==
This filter checks incoming packets that originate from the WAN interface and are destined for the firewall itself.  The policy on the ''INPUT'' chain specifies that packets are by default dropped.  To allow these packets to reach the desired service on the firewall, add a rule here. For example:

{{{iptables --append input_wan --protocol tcp --dport 22 --jump ACCEPT}}}

Possible terminations:
||ACCEPT ||Packet is forwarded to a service running on the local firewall. ||
||DROP ||Packet is dropped. ||
||RETURN ||No additional processing in this rule; since the policy on the ''INPUT'' chain is ''DROP'', this is effectively a less-safe way to ''DROP''. You probably want to be explicit and use ''DROP'' instead. ||


== output_rule (filter) ==
This rule applies to packets originating from a local service, one running on the firewall itself. Note that if a the packet is related to a previous connection, it is automatically opened; therefore, in most cases it is not necessary to add an explicit rule here. If you have a service that runs on the firewall and periodically initiates connections to any interface, it should be added here.  For example, to allow the firewall to make NTP requests (port 123) using UDP:

{{{iptables --append output_rule --protocol udp --dport 123 --ACCEPT}}}

== forwarding_rule (filter) ==
This rule applies to packets to be forwarded from one interface to the other.  It is called regardless of the originating interface, meaning that it may be used to target packets either inbound (WAN to LAN) or outbound (LAN to WAN).

Note that the FORWARD chain automatically accepts packets that are related to a previous connection.

== forwarding_wan (filter) ==
This rule applies to packets to be forwarded from the WAN interface to the LAN interface.  If you have a redirect from an external port to an internal service, it will be necessary to add it here.

== postrouting_rule (nat) ==
This rule applies to packets originating from the OpenWrt port destinated for the WAN.  The default postrouting rules takes care of masquerading for packets destined for the WAN interface.  Under normal circumstances it will not be necessary to modify this rule.

= Multiple Files Example =
For organizational purposes you may wish to split your /etc/firewall.user into several files.  However, when doing this, bear in mind that subscripts must be included rather than invoked in order for shell variables such as $WAN and $LAN to be visible.

For example:

{{{
#!/bin/sh
#
# This is ''/etc/firewall.user''
#
# Begin by flushing all existing chains, so that this works in the event of a restart
#
iptables -F input_rule
iptables -F output_rule
iptables -F forwarding_rule
iptables -t nat -F prerouting_rule
iptables -t nat -F postrouting_rule
iptables -F input_wan
iptables -F forwarding_wan
iptables -t nat -F prerouting_wan
#
# Include port redirects
#
. /etc/firewall.redirects
}}}
{{{
#
# Written by Christopher Piggott, chrisp @t rochester d.t rr d.t com
# Public domain, Free to use or modify however you wish.
#
# This is ''/etc/firewall.redirects''
#
# Define a function that adds redirects
#
redirect()
{
        local port=$1
        local protocol=$2
        local redirect_to=$3
        local limit=$4
        local limit_burst=$5

        #
        # First, do NAT on the incoming port to direct it
        # to the right server
        #
        iptables \
                --table nat \
                --append prerouting_wan \
                --protocol $protocol \
                --dport $port \
                --jump DNAT \
                --to-destination $redirect_to
        #
        # Then, have the forwarding filter allow it
        #

        if [ -z "$limit" -o -z "$limit_burst" ]  ; then
                iptables \
                        --append forwarding_wan \
                        --protocol $protocol \
                        --destination $redirect_to \
                        --dport $port \
                        --jump ACCEPT
        else
                iptables \
                        --append forwarding_wan \
                        --protocol $protocol \
                        --dport $port \
                        --destination $redirect_to \
                        --match state --state NEW \
                        --match limit --limit $limit --limit-burst $limit_burst \
                        --jump ACCEPT
        fi
}


# Redirect table

#   Command    port   proto   destination      limit      burst size
#   --------  ------  -----  --------------  ---------   ------------
    redirect    22     tcp    192.168.0.101   5/minute        5
    redirect    80     tcp    192.168.0.101
    redirect    443    tcp    192.168.0.101
    redirect    113    tcp    192.168.0.125
    redirect    8180   tcp    192.168.0.101
    redirect    21     tcp    192.168.0.101
    redirect    993    tcp    192.168.0.101
}}}
