'''Bridging Access Point'''

I wanted to upgrade my home private LAN, which consists of some wired hosts and an Apple Airport, all behind a machine that acts as firewall and DHCP server. I hoped to be able to handle 802.11G and clean up some of the clutter - the WRT54G seems like the perfect box to do this.

The goal was completely transparent bridging of all five ethernet ports and the wireless, with the WRT getting configured by DHCP. It took a number of iterations (and reflash), but this seems to be a complete list of what's needed: 

 1. Set up the machine with White Russian, and connect the WAN port to the local network. Telnet to the address that the machine got via DHCP.

 1. Get rid of the firewall/NAT: {{{rm /etc/init.d/S45firewall}}}

 1. Get rid of DHCP: {{{rm /etc/init.d/S50dnsmasq}}}

 1. Undo the WAN port: {{{
nvram set wan_proto=none
nvram set wan_ifname=""
nvram set vlan1ports="5"
}}}
 1. Set up the LAN to use all five ports and get configured by DHCP: {{{
nvram set lan_proto="dhcp"
nvram set vlan0ports="0 1 2 3 4 5*"
nvram set vlan0hwnam=et0
}}}
 1. Save to flash and reboot {{{
nvram commit
reboot
}}}
