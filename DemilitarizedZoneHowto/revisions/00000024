'''DemilitarizedZoneHowto'''


[[TableOfContents]]


= Introduction =

Lots of users requested a howto on IRC and the forum for a sample
demilitarized zone configuration using !OpenWrt. Well, here is the
howto. Take it AS-IS. If you don't like how it's written please feel
free to change it.

This example is tested with a WRT54GS v1.0 and a standard White Russian
RC4 image.

(Note for users looking to duplicate the poorly-named DMZ feature found on most native firmwares - just skip straight to step 2.4.
This is not as proper, but allows for a "moving DMZ host", which may not be limited to a given port.  - MarkZiesemer)

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

vlan1: WAN
vlan2: LAN Port 4 (= DMZ)
br0:   LAN (Ports 1 to 3) and WiFi

vlan1: IP address from DHCP, PPPoE, static, ..
vlan2: 192.168.2.1 (192.168.2.0/24)
br0:   192.168.1.1 (192.168.1.0/24)
}}}


= Configuration =

== Create a new vlan ==

You now have to decide which one of the LAN ports on the back of your router
you want to use for the demilitarized zone. On this page it's LAN port 4.

The configuration is easily done by changing the vlan* NVRAM variables.

/!\ '''WARNING:''' Doublecheck these settings before commit them!

{{{
nvram set vlan0hwname=et0
nvram set vlan0ports="1 2 3 5*"
nvram set vlan1hwname=et0
nvram set vlan1ports="0 5"
nvram set vlan2hwname=et0
nvram set vlan2ports="4 5"
}}}

The {{{vlan2hwname}}} and {{{vlan2ports}}} NVRAM variables creates the new
vlan2 for our DMZ.


== Configure dmz_* variables ==

Set the following:

{{{
nvram set dmz_ifname=vlan2
nvram set dmz_ifnames=vlan2
nvram set dmz_ipaddr=192.168.2.1
nvram set dmz_netmask=255.255.255.0
nvram set dmz_proto=static
}}}


== Modify the init scripts ==

Next is to change your init scripts to bring up the DMZ on every reboot. You have to edit
the {{{/etc/init.d/S40network}}} file and add {{{ifup dmz}}} after the line {{{ifup wan}}}.

For whiterussian 0.9, you don't need to edit {{{/etc/init.d/S40network}}}. Instead, execute the following:
{{{nvram set ifup_interfaces="lan wan wifi dmz"
nvram commit}}}

== Configure the firewall ==

{{{/etc/firewall.user}}} should look like this:

{{{
[..]
iptables -A forwarding_rule -i vlan2 -o $WAN  -j ACCEPT
iptables -A forwarding_rule -i vlan2 -o br0   -j ACCEPT

### Port forwarding
# http to DMZ
iptables -t nat -A prerouting_rule -i $WAN -p tcp --dport 80 -j DNAT --to 192.168.2.2
iptables        -A forwarding_rule -i $WAN -p tcp --dport 80 -d 192.168.2.2 -j ACCEPT

### DMZ (should be placed after port forwarding / accept rules)
iptables -t nat -A prerouting_rule -i $WAN -j DNAT --to 192.168.2.2
iptables        -A forwarding_rule -i $WAN -d 192.168.2.2 -j ACCEPT
}}}

Note that most of this already exists in the default {{{/etc/firewall.user}}}, and only needs to be
uncommented, with the IP edited as necessary.

(Can't edit the file?  Check the [http://wiki.openwrt.org/Faq#head-74da83e07a26f01d739113dad7d8aaa31aae24e7 FAQ].)


== Clean up ==

Now it's time to commit the changes and a reboot your router which hopefully
comes up again with a vlan2 interface (check it with {{{ifconfig}}}).

(If {{{firewall.user}}} is all that has changed, {{{/etc/firewall.user}}} will do nicely; no reboot
required.)


= Testing =

First make sure your vlan2 interface is up and pingable on the router. Next
thing you could try is to hook up a PC or another Wrt to the LAN port 4 and see if
you can reach its httpd server.

That's it. Have fun!


= Links =

 * [http://en.wikipedia.org/wiki/Demilitarized_zone_%28computing%29 Demilitarized zone (computing)]
