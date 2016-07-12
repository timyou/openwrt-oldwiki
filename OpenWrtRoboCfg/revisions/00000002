/!\ Robocfg will be obsolete soon. (?in which version / by what?)

Robocfg is a utility written by Oleg Vdovikin to enable the hardware configuration
of the Broadcom BCM5325E/536x VLAN enabled 6-port ethernet switch.  When used properly,
it can configure the switch in such a way that enables each of the five exposed ports
of the switch to be treated as a separate, individual ethernet interface. Using robocfg,
the switch can also be configured to tag packets for use in VLAN enabled networks, and
to configure each port's MDI, duplex, and speed settings. Robocfg options can be issued
individually, or strung together on one line, each new option and parameter separated by
a space. See the bottom of this section for a copy of Robocfg's own stated parameters.

'''Sample Command Uses'''

Show current switch configuration:

{{{
robocfg show
}}}

Enable or disable a port (note: tx/rx_disabled can be useful for traffic monitoring):

{{{
robocfg port X state <enabled|disabled|rx_disabled|tx_disabled>
}}}

Set port speed and duplex:

{{{
robocfg port X media <auto|10HD|10FD|100HD|100FD>
}}}

Set port crossover state:

{{{
robocfg port X mdi-x <auto|on|off>
}}}

'''Advanced Configuration'''

When changing port assignments for VLANs, the switch should be disabled before changing
the settings, and then re-enabled after the settings have been entered. Of course, the
configuration should also be done using a serial console or executed as a script, since
reconfiguration of the switch will disconnect any current telnet or SSH session. Port
numbers followed by a "t" will pass tagged packets(necessary for port 5), while port
numbers with a "u", or no "t", will untag packets when passing them through the interface.
The following example (which configures each physical port with it's own VLAN) has been
stretched out to better show each action:

{{{
robocfg switch disable
robocfg vlans enable reset
robocfg vlan 0 ports "0 5t"
robocfg vlan 1 ports "1 5t"
robocfg vlan 2 ports "2 5t"
robocfg vlan 3 ports "3 5t"
robocfg vlan 4 ports "4 5t"
robocfg switch enable
}}}

Now that the switch has been configured to tag the appropriate packets, the VLANs can be
created using the vconfig command:

{{{
vconfig add eth0 0
vconfig add eth0 1
vconfig add eth0 2
vconfig add eth0 3
vconfig add eth0 4
}}}

Now VLANs 0-4 have been created, and these can be seen with the "ifconfig -a" command.
Each VLAN now needs to be assigned a unique hardware MAC address:

{{{
ifconfig vlan0 hw ether XX:XX:XX:XX:XX:00
ifconfig vlan1 hw ether XX:XX:XX:XX:XX:01
ifconfig vlan2 hw ether XX:XX:XX:XX:XX:02
ifconfig vlan3 hw ether XX:XX:XX:XX:XX:03
ifconfig vlan4 hw ether XX:XX:XX:XX:XX:04
}}}

An IP address can be assigned to each VLAN interface now, if desired:

{{{
ifconfig vlanX xx.xx.xx.xx netmask xx.xx.xx.xx
}}}

Finally, each interface can be brought up:

{{{
ifconfig vlanX up
}}}

Alternately, all ports can be placed on vlan0:

{{{
robocfg switch disable
robocfg vlans enable reset
robocfg vlan 0 ports "0 1 2 3 4 5t"
robocfg switch enable
vconfig add eth0 0
ifconfig vlan0 xx.xx.xx.xx netmask xx.xx.xx.xx
ifconfig vlan0 up
}}}

'''Original Robocfg Parameter List'''

{{{
Usage: robocfg <op> ... <op>
Operations are as below:
        show
        switch <enable|disable>
        port <port_number> [state <enabled|rx_disabled|tx_disabled|disabled>]
                [stp none|disable|block|listen|learn|forward] [tag <vlan_tag>]
                [media auto|10HD|10FD|100HD|100FD] [mdi-x auto|on|off]
        vlan <vlan_number> [ports <ports_list>]
        vlans <enable|disable|reset>

        ports_list should be one argument, space separated, quoted if needed,
        port number could be followed by 't' to leave packet vlan tagged (CPU
        port default) or by 'u' to untag packet (other ports default) before
        bringing it to the port, '*' is ignored

Samples:
1) ASUS WL-500g Deluxe stock config (eth0 is WAN, eth0.1 is LAN):
robocfg switch disable vlans enable reset vlan 0 ports "0 5u" vlan 1 ports "1 2
3 4 5t" port 0 state enabled stp none switch enable
2) WRT54g, WL-500g Deluxe OpenWRT config (vlan0 is LAN, vlan1 is WAN):
robocfg switch disable vlans enable reset vlan 0 ports "1 2 3 4 5t" vlan 1 ports
 "0 5t" port 0 state enabled stp none switch enable
}}}
