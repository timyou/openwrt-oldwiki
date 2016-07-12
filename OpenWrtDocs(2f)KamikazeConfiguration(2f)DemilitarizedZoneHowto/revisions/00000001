'''DemilitarizedZoneHowto'''


[[TableOfContents]]


= Introduction =

Lots of users requested a howto on IRC and the forum for a sample demilitarized zone configuration using !OpenWrt. Well, here is the howto. Take it AS-IS. If you don't like how it's written please feel free to change it.

This example is tested with a ASUS WL-500g Premium v1 with Athros !WiFi and a recent Kamikaze (trunk) build.

(Note for users looking to duplicate the poorly-named DMZ feature found on most native firmwares - just skip straight to step 2.4. This is not as proper, but allows for a "moving DMZ host", which may not be limited to a given port. - MarkZiesemer)

This document is written for experienced users only.

{{{
             (vlan1)       (br0)
INTERNET ---------- OpenWrt ------------ Clients
                       |
                       | (vlan2)
                       |
                       |
                       |

              Demilitarized Zone

vlan1:  WAN
vlan2:  LAN Port 4 (= DMZ)
br-lan: LAN (Ports 1 to 3) and WiFi

vlan1:  IP address from DHCP, PPPoE, static, ...
vlan2:  192.168.2.1 (192.168.2.0/24)
br-lan: 192.168.1.1 (192.168.1.0/24)
}}}


= Configuration =

== Create a new vlan ==

You now have to decide which one of the LAN ports on the back of your router you want to use for the demilitarized zone. On this page it's LAN port 4.

The configuration is easily done by reconfiguring the switch via UCI.

/!\ '''WARNING:''' Doublecheck these settings before commit them!

Remove switch port 4 from vlan0
{{{
uci set network.eth0.vlan0='1 2 3 5*'}}}

Create a new vlan. The name will be vlan2.
{{{
uci set network.eth0.vlan2='4 5'}}}

Save the network configuration
{{{
uci commit network}}}

The option network.eth0.vlan2 creates the new vlan2 for our DMZ.


== Create a new network ==

Set the following:
{{{
uci set network.dmz=interface
uci set network.dmz.proto=static
uci set network.dmz.ipaddr=192.168.2.1
uci set network.dmz.netmask=255.255.255.0
uci set network.dmz.ifname=eth0.2
uci commit network}}}

== Configure DHCP for our DMZ (optional) ==

Set the following:
{{{
uci add dhcp dhcp
uci set dhcp.@dhcp[-1].interface=dmz
uci set dhcp.@dhcp[-1].start=100
uci set dhcp.@dhcp[-1].limit=150
uci set dhcp.@dhcp[-1].leasetime=12h
uci commit dhcp}}}

== Configure the firewall ==

=== Create a new zone ===

{{{
uci add firewall zone
uci set firewall.@zone[-1].name=dmz
uci set firewall.@zone[-1].network=dmz
uci set firewall.@zone[-1].input=ACCEPT
uci set firewall.@zone[-1].output=ACCEPT
uci set firewall.@zone[-1].forward=DROP}}}

=== Forwarding (allow dmz -> wan and lan -> dmz) ===

{{{
uci add firewall forwarding
uci set firewall.@forwarding[-1].src=dmz
uci set firewall.@forwarding[-1].dest=wan
uci add firewall forwarding
uci set firewall.@forwarding[-1].src=lan
uci set firewall.@forwarding[-1].dest=dmz}}}

=== Save the config ===

{{{
uci commit firewall}}}

== Reboot ==

Reboot if you are finished with the configuration.
{{{
reboot}}}
