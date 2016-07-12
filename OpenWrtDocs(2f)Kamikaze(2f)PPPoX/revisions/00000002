= PPPoE and PPPoA =
A normal DSL connection requires an ATM-Ethernet bridge and PPPoE configuration.  Bridged DSL requires the bridge, but the wan interface is configured as though the nas0 interface is connected to the internet directly, so usually just DHCP.

== Setting up an ATM-Ethernet bridge ==
Typically, a gateway with a built-in DSL modem needs this set up.  Use this if your DSL provider uses PPPoE.  This config entry creates the nas0 device.

Note: in order to use this, you probably need the br2684ctl package.

{{{/etc/config/network}}}
{{{
config atm-bridge
    option unit     0
    option encaps   llc

    # Ask your ISP for the correct vpi and vci values
    option vpi      0
    option vci      35

    # Most of the time this should be set to "bridged," but some ISPs require "routed"
    option payload  bridged
}}}

== Setting up PPPoE ==
Once you set up the bridge, or once you plug in a DSL ''or'' cable modem, set up the "dial-up" PPPoE connection.  If using a built-in DSL modem, the interface name will be nas0.  If the router is plugged into a DSL or cable modem in '''bridged mode''', set the interface name to the vlan device, typically something like eth0.1.  This configuration is uncommon.  Most people set their cable and DSL modems to do PPP, not have an external device handle it.

{{{/etc/config/network}}}
{{{
config interface wan
    option ifname       nas0
    option proto        pppoe
    option username    "username"
    option password    "password"
}}}

== Setting up PPPoA ==
{{{
config interface wan
    option ifname   atm0
    option proto    pppoa
    option encaps   llc
    option vpi      0
    option vci      35
    option username "username"
    option password "password"
}}}
