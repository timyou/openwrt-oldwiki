'''DemilitarizedZoneHowto'''

[[TableOfContents]]
= Introduction =
Lots of users requested a howto on IRC and the forum for a sample demilitarized zone configuration using !OpenWrt. Well, here is the howto. Take it AS-IS. If you don't like how it's written please feel free to change it.

This example is tested with a WRT54GS v1.0 and a standard White Russian RC4 image.

(Note for users looking to duplicate the poorly-named DMZ feature found on most native firmwares - just skip straight to step 2.4. This is not as proper, but allows for a "moving DMZ host", which may not be limited to a given port.  - MarkZiesemer)

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
You now have to decide which one of the LAN ports on the back of your router you wan't to use for the demilitarized zone. On this page it's LAN port 4.

The configuration is easily done by changing the vlan* NVRAM variables.

/!\ '''WARNING:''' Doublecheck these settings before commit them!

{{{
vlan0hwname=et0
vlan0ports="1 2 3 5*"
vlan1hwname=et0
vlan1ports="0 5"
vlan2hwname=et0
vlan2ports="4 5"
}}}

The {{{vlan2hwname}}} and {{{vlan2ports}}} NVRAM variables creates the new vlan2 for our DMZ.

== Configure dmz_* variables ==
Set the following:

{{{
dmz_ifname=vlan2
dmz_ifnames=vlan2
dmz_ipaddr=192.168.2.1
dmz_netmask=255.255.255.0
dmz_proto=static
}}}

== Modify the init scripts ==
Next is to change your init scripts to bring up the DMZ on every reboot. You have to edit the {{{/etc/init.d/S40network}}} file and add {{{ifup dmz}}} after the line {{{ifup wan}}}.

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

Note that most of this already exists in the default {{{/etc/firewall.user}}}, and only needs to be uncommented, with the IP edited as necessary.

(Can't edit the file?  Check the [http://wiki.openwrt.org/Faq FAQ].)

== Clean up ==
Now it's time to commit the changes and a reboot your router which hopefully comes up again with a vlan2 interface (check it with {{{ifconfig}}}).

(If {{{firewall.user}}} is all that has changed, {{{/etc/firewall.user}}} will do nicely; no reboot required.)

= Testing =
First make sure your vlan2 interface is up and pingable on the router. Next thing you could try is to hook up a PC or another Wrt to the LAN port 4 and see if you can reach it's httpd server.

That's it. Have fun!

= Links =
 * [http://en.wikipedia.org/wiki/Demilitarized_zone_(computing) Demilitarized zone (computing)]

= Misc. =Easy way to put any host in DMZ mode=
Prerequisite:

 * Tested under WRTSL54GS. Comparable router recommended.

 * OpenWRT WhiteRussian RC4

 * Assumes text editor nano is installed

Instructions:

1.Login to your router via SSH.

2.Type:

||<tablewidth="200px" tablestyle="">nvram show | grep "dmz" ||


3.You should see the follow variables: "dmz_enable" and "dmz_ipaddr"

4.Type:

||<tablewidth="200px" tablestyle="">nvram set dmz_enable=1 ||


4-a. Type:

||<tablewidth="381px" tableheight="46px" tablestyle="">nvram set dmz_ipaddr=<your LAN host IP here> ||


5.Now, you have to go edit your iptables. Type:

||<tablewidth="200px" tablestyle="">nano /etc/firewall.user ||


5a. If it says it is Read-Only, just delete and it make a new copy. 

5b. Type:


||<tablewidth="200px" tablealign="">rm /etc/firewall.user||





||cp /rom/etc/firewall.user /etc/ ||


6.You should see this in firewall script:

### DMZ (should be placed after port forwarding / accept rules)
||<tablewidth="720px" tableheight="65px" tablestyle=""># iptables -t nat -A prerouting_rule -i $WAN -j DNAT --to 192.168.1.2 ||
||# iptables -A forwarding_rule -i $WAN -d 192.168.1.2 -j ACCEPT ||


7.Change those lines to suit your needs. Comment out # to have the line in effect. Just change 192.168.1.2 part to the value that "dmz_ipaddr" has. For example:

### DMZ (should be placed after port forwarding / accept rules)
||<tablewidth="633px" tableheight="65px" tablestyle="">iptables -t nat -A prerouting_rule -i $WAN -j DNAT --to 192.168.1.101 ||
|| iptables        -A forwarding_rule -i $WAN -d 192.168.1.101 -j ACCEPT ||


8.Now client 192.168.1.101 in under DMZ.

ENJOY!
