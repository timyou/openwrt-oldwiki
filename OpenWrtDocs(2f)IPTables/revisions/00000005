## Please edit system and help pages ONLY in the moinmaster wiki! For more
## information, please see MoinMaster:MoinPagesEditorGroup.
##acl MoinPagesEditorGroup:read,write,delete,revert All:read
##master-date:Unknown-Date
#format wiki
#language en
= OpenWRT Custom IPTables =


== Introduction ==

A main purpose of OpenWRT is to serve as a highly configurable network firewall.  OpenWRT's firewall rules can be configured in many ways.  Distribution templates and configuration tools should prove sufficiently flexible for most applications.  However, for a more complex installation it may be necessary to extend the iptables configuration directly.

OpenWRT defines a set of rules for network address translation (NAT) and packet filtering.  These rules are arranged to allow user extension without the need to reorganize OpenWRT's iptables structure.  The administrator will benefit from creating a local configuration that fits within the structure OpenWRT expects.  As this document will show, a high degree of flexibility can be achieved ''without'' modifying OpenWRT's distribution start-up or reconfiguration scripts.

The reader should already be familiar with iptables and have reviewed the [http://iptables-tutorial.frozentux.net/iptables-tutorial.html Iptables Tutorial], available many places including [http://iptables-tutorial.frozentux.net/iptables-tutorial.html Here] and [http://www.faqs.org/docs/iptables/ Here].

== User Filter Configuration File ==

User-defined iptables should be placed in the local configuration file ''/etc/firewall.user''.  The firewall startup script (which you ''don't'' modify) establishes the basic rules framework under which your local configuration exists.  ''/etc/firewall.user'' is accessed both when the firewall is started or restarted.

== OpenWrt Chains ==

The following diagram is adapted from the IPTables tutorial, with detail added to explain where each firewall.user rule fits in.  Each one of the detail boxes describes the actions that take place in the /etc/init.d firewall start-up script.  At certain points this script invokes user-defined chains of rules; these are the rules that you customize in ''/etc/firewall.user''.

http://wiki.autofrog.com/_media/openwrt/openwrtiptables.png

== Rules ==

=== prerouting_rule (nat) ===

Description of rule TBD.

=== prerouting_wan (nat) ===

Description of rule TBD.

=== input_rule (filter) ===

This filter checks incoming packets, regardless of the input interface.  This rule only applies to packets destined for OpenWrt.

Possible terminations:

|| ACCEPT || Packet is fowarded to a service running on OpenWrt ||
|| DROP || Packet is dropped ||
|| RETURN || No additional processing in this rule; packet is passed to ''input_wan'' if it originated from the WAN interface ||

It may be desirable to have the ''input_rule'' only apply to packets sourced from the LAN (possibly including WLAN) interface.  To do this, begin ''input_rule'' with:

{ { {
iptables -A input_rule -i $WAN -j return
} } }

=== input_wan (filter) ===

This filter checks incoming packets that 1. were not already ACCEPTed by ''input_rule'', and 2. arrived in the WAN interface.  This rule only applies to packets destined for OpenWrt.

Possible terminations:

|| ACCEPT || Packet is fowarded to a service running on OpenWrt ||
|| DROP || Packet is dropped ||
|| RETURN || No additional processing in this rule; packet is passed to ''input_wan'' if it originated from the WAN interface ||


=== forwarding_rule (filter) ===

This rule applies to packets to be forwarded from one interface to the other.

=== forwarding_wan (filter) ===

This rule applies to packets to be forwarded from the WAN interface to the LAN interface.

=== output_rule (filter) ===

This rule applies to packets originating from a local OpenWrt port.

=== postrouting_rule (nat) ===

This rule applies to packets originating from the OpenWrt port destinated for the WAN.
