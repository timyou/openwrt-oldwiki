## Please edit system and help pages ONLY in the moinmaster wiki! For more
## information, please see MoinMaster:MoinPagesEditorGroup.
##acl MoinPagesEditorGroup:read,write,delete,revert All:read
##master-date:Unknown-Date
#format wiki
#language en
= OpenWRT Custom IPTables Configuration =


== Introduction ==

The distribution template should prove sufficient for most uses.  However, if one wishes to do something more complicated with iptables it is helpful to understand how OpenWrt's default rules fit in with the traditional IPTables packet flow.

== Where to Edit ==

The basic structure of the firewall is established by the firewall start-up script, ''/etc/init.d/S35firewall''.  '''You should not modify this file.'''  Rather, customization should begin in ''/etc/firewall.user''.

However, it is worth examining ''/etc/init.d/s35firewall'' for educational purposes.  It establishes the basic framework under which your custom rules should exist.  The purpose of this document is to explain the structure of those pre-defined rules.

== OpenWrt Rules ==

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
