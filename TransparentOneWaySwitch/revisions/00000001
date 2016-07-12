This page describes how to build a transparent firewall with 2 VLANs and "onway" communication. It builds a simple DMZ on the same subnet as LAN. Membership to LAN or DMZ is given by the port to which the host is connected. DMZ cannot connect or ping to LAN nor router. LAN can connect and ping to DMZ and router. 

= Transparent Onway Switch HowTo or Semipermiable Switch HowTo =

Let's build a certain kind of DMZ: 
 * anything on the same subnet
 * hosts in the DMZ must not connect or ping LAN
 * hosts on LAN must be able to connect and ping hosts on DMZ
 * gateway to internet is in DMZ
 * Router is visible from LAN only
 * no WLAN


= This is how it should look like: =

I use 192.168.1.0/24, because that's  the routers defult setting.

{{{
ex.:

                                    +--------+
 GATEWAY (192.168.1.9) -------------| Port 0 |
                                    +--------+
 HOST A  (192.168.1.111) -----------| Port 1 |
                                    +--------+
 HOST B  (192.168.1.23)  -----------| Port 2 |
                                    +--------+
 HOST C  (192.168.1.21) ------------| Port 3 |
                                    +--------+
                                    | WAN    | ---------- to LAN
                                    +--------+
                                      ROUTER
                                   (192.168.1.1)

}}}


= Hands on =

OpenWrt White Russian RC6, a WRT54GL v1.1., SQASHFS image. 

== Install extra packages ==
Set up the router so that you've got a working internet connection with dns. Ssh to the router. You need to install some extra packages:
{{{
 root@OpenWrt:~# ipkg update
 root@OpenWrt:~# ipkg install ebtables
 root@OpenWrt:~# ipkg install kmod-ebtables
 root@OpenWrt:~# ipkg install iptables-mod-extra
 root@OpenWrt:~# ipkg install kmod-ipt-extra
}}}

if you get an error, you may have to copy /etc/resolv.conf from your workstation to /tmp/resolv.conf (squashfs) or /etc/resolv.conf (jffs) on the router:
{{{ root@OpenWrt:~# scp /etc/resolv.conf root@192.168.1.1:/tmp/resolv.conf }}}

== Basic LAN setup ==
Then delete any IP associated with your WAN. That's because the bridge will take it over. You may use the webinterface to do this:
 * disable WLAN (if you want to keep it, you'll need some extra steps)
 * set WAN IP 0.0.0.0 
 * set WAN gateway = same as LAN gateway (that's just beautification)
 * set WAN netmask = same as LAN netmask (that's just beautification)

== VLAN setup ==
Bridgeing is a funny thing on the WRT54. To make things working you need to turn on vlan tagging on all bridged vlan interfaces (here on vlan1) but one (vlan0). That's no hard condition. You may tag all vlans or all but one. But all untagged vlans are handled as one ... and when you define firewall rules you may go nuts about this. 

SSH to your rooter. First take a look at your nvram vars that handle vlans:  
{{{
 root@OpenWrt:~# nvram show | grep vlan | sort
 lan_ifnames=vlan0 eth2
 vlan0hwname=et0
 vlan0ports=3 2 1 0 5*
 vlan1hwname=et0
 vlan1ports=4 5t
 wan_device=vlan1
 wan_iface=vlan1
 wan_ifname=vlan1
 wan_ifnames=vlan1
}}}
and now enable tagging on vlan1:
{{{ root@OpenWrt:~# nvram set vlan1ports="4 5t" }}}

If you've turned off WLAN, then let's remove it from our bridge. You must not add vlan1, otherwise you will have to use failsave mode:
{{{ root@OpenWrt:~# nvram set lan_ifnames=vlan0 }}}

and don't forget to commit the changes:
{{{ root@OpenWrt:~# nvram commit }}}

Now it's save to reboot your router.

== Bridge ==
Again, ssh to router. Let's take a look at the bridge:
{{{
 root@OpenWrt:~# brctl show
 bridge name     bridge id               STP enabled     interfaces
 br0             8000.001839ceaa72       no              vlan0
}}}

Let's add the WAN interface (vlan1) to the bridge:
{{{
 root@OpenWrt:~# brctl addif br0 vlan1
 root@OpenWrt:~# brctl show
 bridge name     bridge id               STP enabled     interfaces
 br0             8000.001839ceaa72       no              vlan0
                                                         vlan1
}}}

Fine, your router is now a 5 port switch with funny firewall rules :-)

Build a startup script to make the changes persistent. As I was not able to write any text with OpenWrt vi, I use cat and copy&paste. ^d means <ctrl>+<d>:
{{{
 root@OpenWrt:~# cat > /etc/init.d/S50mystuff
#!/bin/bash
brctl addif br0 vlan1
^d
}}}

Make it executeable:
{{{ root@OpenWrt:~# chmod a+x /etc/init.d/S50mystuff }}}

And now kick out the builtin firewall:
{{{ root@OpenWrt:~# chmod -x /etc/init.d/S50firewall }}}

Now reboot the router. And connect your workstation with the WAN port of the router, as we are going to set up some firewall rules in the next step.

== Check it ==
... ssh to router. Let's take a look at the firewall:
{{{ root@OpenWrt:~# iptables -L -n -v }}}

That's much better. 
Let's take a look at the bridge: 
{{{
 root@OpenWrt:~# brctl show
 bridge name     bridge id               STP enabled     interfaces
 br0             8000.001839ceaa72       no              vlan0
                                                         vlan1
}}}
Fine :-)

== Firewall ==
Now let's build our new Firewall. First you need to load some modules:
{{{
 root@OpenWrt:~# /sbin/insmod ebtables      
 root@OpenWrt:~# /sbin/insmod ebtable_broute
 root@OpenWrt:~# /sbin/insmod ebtable_filter
 root@OpenWrt:~# /sbin/insmod ebtable_nat 
 root@OpenWrt:~# /sbin/insmod ebt_ip 
 root@OpenWrt:~# /sbin/insmod ebt_snat
 root@OpenWrt:~# /sbin/insmod ipt_recent.o
}}}

Now the rules. First let's drop all new connections to vlan1, then let's hide the router from the DMZ:
{{{
 root@OpenWrt:~# iptables -I FORWARD -o vlan1 -m state --state NEW -j DROP
 root@OpenWrt:~# iptables -I INPUT -i vlan0 -d $(nvram get lan_ipaddr) -j DROP
}}}

Let's test it. Connect your workstation into the WAN port, connect some other computer to a LAN port. From your workstation enter:
{{{ ping <ip of router> }}}
{{{ ping <ip of other computer> }}}
Both should work. Now move to other computer and try:
{{{ ping <ip of router> }}}
{{{ ping <ip of workstation> }}}
None of them should work :-) 

== Finalizing ==
Put it all togather in a script:
{{{
 root@OpenWrt:~# cat > /etc/init.d/S50mystuff
#!/bin/bash
brctl addif br0 vlan1
/sbin/insmod ebtables           2> /dev/null
/sbin/insmod ebtable_broute     2> /dev/null
/sbin/insmod ebtable_filter     2> /dev/null
/sbin/insmod ebtable_nat        2> /dev/null
/sbin/insmod ebt_ip             2> /dev/null
/sbin/insmod ebt_snat           2> /dev/null
/sbin/insmod ipt_recent.o       2> /dev/null
iptables -I FORWARD -o vlan1 -m state --state NEW -j DROP
iptables -I INPUT -i vlan0 -d $(nvram get lan_ipaddr) -j DROP
^d
}}}

Reboot the router, check again.

== ... and back again ==
As it is now, your router is a switch with oneway connections. It acts much like a semipermiable membrane. It forbids connections from DMZ to LAN on the same subnet, but allows them from LAN to DMZ. There are lots of ways to improve. The firewall is primitive. You can add mor vlans. You can add WLAN ... 

... use your immagination :-D

n.
