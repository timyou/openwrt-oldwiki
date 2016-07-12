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

The configuration is easily done by reconfiguring the switch via UCI CLI.

/!\ '''WARNING:''' Doublecheck these settings before commit them!

Remove switch port 4 from vlan0

{{{
root@OpenWrt:~# uci set network.eth0.vlan0='1 2 3 5*'}}}
Create a new vlan. The name will be vlan2.

{{{
root@OpenWrt:~# uci set network.eth0.vlan2='4 5'}}}
Save the network configuration

{{{
root@OpenWrt:~# uci commit network}}}
The option network.eth0.vlan2 creates the new vlan2 for our DMZ.

== Create a new network ==
Set the following:

{{{
root@OpenWrt:~# uci set network.dmz=interface
root@OpenWrt:~# uci set network.dmz.proto=static
root@OpenWrt:~# uci set network.dmz.ipaddr=192.168.2.1
root@OpenWrt:~# uci set network.dmz.netmask=255.255.255.0
root@OpenWrt:~# uci set network.dmz.ifname=eth0.2
root@OpenWrt:~# uci commit network}}}
== Routing (optional) ==
{{{
root@OpenWrt:~# uci add network route
root@OpenWrt:~# uci set network.@route[-1].interface=dmz
root@OpenWrt:~# uci set network.@route[-1].target=192.168.2.0
root@OpenWrt:~# uci set network.@route[-1].netmask=255.255.255.0
root@OpenWrt:~# uci set network.@route[-1].gateway=192.168.2.1
root@OpenWrt:~# uci commit network}}}
== Configure DHCP for our DMZ (optional) ==
Set the following:

{{{
root@OpenWrt:~# uci add dhcp dhcp
root@OpenWrt:~# uci set dhcp.@dhcp[-1].interface=dmz
root@OpenWrt:~# uci set dhcp.@dhcp[-1].start=100
root@OpenWrt:~# uci set dhcp.@dhcp[-1].limit=150
root@OpenWrt:~# uci set dhcp.@dhcp[-1].leasetime=12h
root@OpenWrt:~# uci commit dhcp}}}
== Configure the firewall ==
=== Create a new zone ===
{{{
root@OpenWrt:~# uci add firewall zone
root@OpenWrt:~# uci set firewall.@zone[-1].name=dmz
root@OpenWrt:~# uci set firewall.@zone[-1].network=dmz
root@OpenWrt:~# uci set firewall.@zone[-1].input=ACCEPT
root@OpenWrt:~# uci set firewall.@zone[-1].output=ACCEPT
root@OpenWrt:~# uci set firewall.@zone[-1].forward=DROP}}}
=== Forwarding (allow dmz -> wan and lan -> dmz) ===
{{{
root@OpenWrt:~# uci add firewall forwarding
root@OpenWrt:~# uci set firewall.@forwarding[-1].src=dmz
root@OpenWrt:~# uci set firewall.@forwarding[-1].dest=wan
root@OpenWrt:~# uci add firewall forwarding
root@OpenWrt:~# uci set firewall.@forwarding[-1].src=lan
root@OpenWrt:~# uci set firewall.@forwarding[-1].dest=dmz}}}
=== Save the config ===
{{{
root@OpenWrt:~# uci commit firewall}}}
== Reboot ==
Reboot if you are finished with the configuration.

{{{
root@OpenWrt:~# reboot}}}
