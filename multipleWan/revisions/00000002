~+multipleWan+~

This page list action and configuration for multiwan on kamikaze. I've used this on a WRT54G(V1.1 to 3.1).

'''WARNING:''' this only work on kernel 2.4 kamikaze for wrt54G, 2.6 kernel doesn't have the right patch for iproute2 equalize with iptables nat from http://www.ssi.bg/~ja/#routes

This first is to create vlan (one per wan connection)

in the '''/etc/config/network''' for two wan you'll have:
{{{
config switch eth0
        option vlan0    "2 3 4 5*"
        option vlan1    "0 5"
        option vlan2    "1 5"
}}}
...
{{{
#### WAN configuration
config interface        wan
        option ifname   "eth0.1"
        option proto    dhcp

config interface        wan2
        option  ifname  "eth0.2"
        option  proto   dhcp
}}}

during this tutorial I'l consider both your ISP use DHCP, but you can easily change it to static IP


Now we need to install right package for multi wan to work:
{{{
ipkg install ip iptables-mod-conntrack iptables-mod-extra iptables-mod-imq iptables-mod-ipopt 
}}}

once ip(iproute2) is install create as many table as wan you have by editing the '''/etc/iproute2/rt_tables''' (this is easier also you can use numbers instead of table name in the scripts) the file contains :
{{{
201 eth0.1 
202 eth0.2 
}}}

'''warning''' here I've choose to name table the same as the vlan they appear so that it's easier in the udhcp script, if you change this be sure to change any reference to 'table $interface' to 'table <your_table>' in the udhcpc/default.script with a tweak of you own.

Next once vlan and tables are setup, dhcp comes into action, it rely on the '''/usr/share/udhcpc/default.script'''. I've decided to change this file so that on any dhcp request the whole route, DNS etc.. get updated.

{{{
#!/bin/sh
[ -z "$1" ] && echo "Error: should be run by udhcpc" && exit 1
. /etc/functions.sh
include /lib/network

RESOLV_CONF="/tmp/resolv.conf.auto"

hotplug_event() {
        scan_interfaces
        for ifc in $interfaces; do
                config_get ifname $ifc ifname
                [ "$ifname" = "$interface" ] || continue

                config_get proto $ifc proto
                [ "$proto" = "dhcp" ] || continue

                env -i ACTION="$1" INTERFACE="$ifc" DEVICE="$ifname" PROTO=dhcp /sbin/hotplug-call iface
        done
}

case "$1" in
        deconfig)
                ifconfig $interface 0.0.0.0
                hotplug_event ifdown
        ;;
        renew|bound)
                ifconfig $interface $ip \
                netmask ${subnet:-255.255.255.0} \
                broadcast ${broadcast:-+}
                #get the network mask for you ISP ip
                TT=`echo $ip | awk -F. '{print $1"."$2"."$3}'`.0/$mask

                [ -n "$router" ] && {
                        #remove previous rule/table
                        ip route flush table $interface

                        for i in $router ; do
                                echo "adding router $i"
                                ip rule add from $ip table $interface
                                ip route add $TT dev $interface src $ip table $interface
                                ip route add 192.168.1.0/24 dev eth0.0 table $interface
                                ip route add default via $i table $interface
                                valid="$valid|$i"
                        done

                        #add the default route with equalize mpath
                        echo "deleting and updating routes"
                        while route del default >&- 2>&- ; do :; done
                        P1=`ip route list table eth0.1 | grep via | cut -d" " -f 3`
                        P2=`ip route list table eth0.2 | grep via | cut -d" " -f 3`
                        ip route add default scope global \
                          nexthop via $P1 dev eth0.1 weight 1 \
                          nexthop via $P2 dev eth0.2 weight 1

                        #echo "deleting old routes"
                        #$(route -n | awk '/^0.0.0.0\W{9}('$valid')\W/ {next} /^0.0.0.0/ {print "route del -net "$1" gw "$2";"}')
                        #flush previous route
                        ip route flush cache
                }

                [ -n "$dns" ] && {
                        RESOLV_CONF_IF=$RESOLV_CONF.$interface
                        #remove previous DNS routes
                        OLD_DNS=`cat $RESOLV_CONF_IF | cut -d" " -f2`
                        for i in $OLD_DNS ; do
                               ip route del $i 
                        done
                        echo -n > $RESOLV_CONF_IF                                                                          
                        ${domain:+echo search $domain} >> $RESOLV_CONF_IF                                                  
                        for i in $dns ; do                                                                                 
                                echo "adding dns $i"                                                                       
                                echo "nameserver $i" >> $RESOLV_CONF_IF
                                #ATTENTION peut y avaoir plusieurs router a modifier                                        
                                ip route add $i via $router table main                                                     
                        done                                                                                               
                        cat $RESOLV_CONF.eth0.1 $RESOLV_CONF.eth0.2 > $RESOLV_CONF
                }

                hotplug_event ifup

                # mise a l'heure barbare
                rdate -s ntp.dedibox.com

                # user rules
                [ -f /etc/udhcpc.user ] && . /etc/udhcpc.user
        ;;
esac

exit 0
}}}

I have to aknoledge that this script have so part 'hardcoded' like the number of nexthop etc.. but you rarely add/remove wan isn't it ?

last but not list '''/etc/init.d/firewall''' (basically you simply copy/rename every lies where WAN appear to WAN2 in the file)
{{{
#!/bin/sh /etc/rc.common
# Copyright (C) 2006 OpenWrt.org

## Please make changes in /etc/firewall.user
START=45
start() {
        include /lib/network
        scan_interfaces

        config_get WAN wan ifname
        config_get WANDEV wan device
        config_get WAN2 wan2 ifname
        config_get WAN2DEV wan2 device
        config_get LAN lan ifname

        ## CLEAR TABLES
        for T in filter nat; do
                iptables -t $T -F
                iptables -t $T -X
        done

        iptables -N input_rule
        iptables -N input_wan
        iptables -N output_rule
        iptables -N forwarding_rule
        iptables -N forwarding_wan

        iptables -t nat -N NEW
        iptables -t nat -N prerouting_rule
        iptables -t nat -N prerouting_wan
        iptables -t nat -N postrouting_rule

        iptables -N LAN_ACCEPT
        [ -z "$WAN" ] || iptables -A LAN_ACCEPT -i "$WAN" -j RETURN
        [ -z "$WAN2" ] || iptables -A LAN_ACCEPT -i "$WAN2" -j RETURN
        [ -z "$WANDEV" -o "$WANDEV" = "$WAN" ] || iptables -A LAN_ACCEPT -i "$WANDEV" -j RETURN
        [ -z "$WAN2DEV" -o "$WAN2DEV" = "$WAN2" ] || iptables -A LAN_ACCEPT -i "$WAN2DEV" -j RETURN
        iptables -A LAN_ACCEPT -j ACCEPT

        ### INPUT
        ###  (connections with the router as destination)

        # base case
        iptables -P INPUT DROP
        iptables -A INPUT -m state --state INVALID -j DROP
        iptables -A INPUT -m state --state RELATED,ESTABLISHED -j ACCEPT
        iptables -A INPUT -p tcp --tcp-flags SYN SYN --tcp-option \! 2 -j  DROP

        #
        # insert accept rule or to jump to new accept-check table here
        #
        iptables -A INPUT -j input_rule
        [ -z "$WAN" ] || iptables -A INPUT -i $WAN -j input_wan
        [ -z "$WAN2" ] || iptables -A INPUT -i $WAN2 -j input_wan

        # allow
        iptables -A INPUT -j LAN_ACCEPT # allow from lan/wifi interfaces 
        iptables -A INPUT -p icmp       -j ACCEPT       # allow ICMP
        iptables -A INPUT -p gre        -j ACCEPT       # allow GRE

        # reject (what to do with anything not allowed earlier)
        iptables -A INPUT -p tcp -j REJECT --reject-with tcp-reset
        iptables -A INPUT -j REJECT --reject-with icmp-port-unreachable

        ### OUTPUT
        ### (connections with the router as source)

        # base case
        iptables -P OUTPUT DROP
        iptables -A OUTPUT -m state --state INVALID -j DROP
        iptables -A OUTPUT -m state --state RELATED,ESTABLISHED -j ACCEPT

        #
        # insert accept rule or to jump to new accept-check table here
        #
        iptables -A OUTPUT -j output_rule

        # allow
        iptables -A OUTPUT -j ACCEPT            #allow everything out

        # reject (what to do with anything not allowed earlier)
        iptables -A OUTPUT -p tcp -j REJECT --reject-with tcp-reset
        iptables -A OUTPUT -j REJECT --reject-with icmp-port-unreachable

        ### FORWARDING
        ### (connections routed through the router)

        # base case
        iptables -P FORWARD DROP 
        iptables -A FORWARD -m state --state INVALID -j DROP
        iptables -A FORWARD -p tcp --tcp-flags SYN,RST SYN -j TCPMSS --clamp-mss-to-pmtu
        iptables -A FORWARD -m state --state RELATED,ESTABLISHED -j ACCEPT

        #
        # insert accept rule or to jump to new accept-check table here
        #
        iptables -A FORWARD -j forwarding_rule
        [ -z "$WAN" ] || iptables -A FORWARD -i $WAN -j forwarding_wan
        [ -z "$WAN2" ] || iptables -A FORWARD -i $WAN2 -j forwarding_wan

        # allow
        iptables -A FORWARD -i $LAN -o $LAN -j ACCEPT
        [ -z "$WAN" ] || iptables -A FORWARD -i $LAN -o $WAN -j ACCEPT
        [ -z "$WAN2" ] || iptables -A FORWARD -i $LAN -o $WAN2 -j ACCEPT

        # reject (what to do with anything not allowed earlier)
        # uses the default -P DROP

        ### MASQ
        iptables -t nat -A PREROUTING -m state --state NEW -p tcp -j NEW 
        iptables -t nat -A PREROUTING -j prerouting_rule
        [ -z "$WAN" ] || iptables -t nat -A PREROUTING -i "$WAN" -j prerouting_wan
        [ -z "$WAN2" ] || iptables -t nat -A PREROUTING -i "$WAN2" -j prerouting_wan
        iptables -t nat -A POSTROUTING -j postrouting_rule
        [ -z "$WAN" ] || iptables -t nat -A POSTROUTING -o $WAN -j MASQUERADE
        [ -z "$WAN2" ] || iptables -t nat -A POSTROUTING -o $WAN2 -j MASQUERADE

        iptables -t nat -A NEW -m limit --limit 50 --limit-burst 100 -j RETURN && \
                iptables -t nat -A NEW -j DROP

        ## USER RULES
        [ -f /etc/firewall.user ] && . /etc/firewall.user
        [ -n "$WAN" -a -e /etc/config/firewall ] && {
                export WAN
                awk -f /usr/lib/common.awk -f /usr/lib/firewall.awk /etc/config/firewall | ash
        }
}

stop() {
        iptables -P INPUT ACCEPT
        iptables -P OUTPUT ACCEPT
        iptables -P FORWARD ACCEPT
        iptables -F
        iptables -X
        iptables -t nat -P PREROUTING ACCEPT
        iptables -t nat -P POSTROUTING ACCEPT
        iptables -t nat -P OUTPUT ACCEPT
        iptables -t nat -F
        iptables -t nat -X
}
}}}

Here you are, you now have a dual wan setup. Notice that some of you ISP services are only accessible when the source IP is part of its network. For example if you use SMTP or DNS from ISP1 (smtp.isp1.com) it will only be accessible as smtp relay if your IP belong to ISP1. round robin multiple wan break this, so you might want to add rule to your setup so that mail.isp1.com only use the wan1. If you've read the udhcpc script you have noticed we have already done this by adding static route to each ISP DNS server. Now how to tell iproute than smtp must done through isp1 only ? we will mark each outgoing packet for port 25(Smtp) and assign this mark to a specific table. simply add those 2 lines to '''/etc/firewall.user''':
{{{
iptables -t mangle -A PREROUTING -p tcp --dport 25 -j MARK --set-mark 0x100
ip rule add fwmark 0x100 table eth0.2
}}}

for other services just do the same changing the 0x100 to 0x101 and dport 25 to the service port number.

At last for firewall, the new kamikaze firewall script is simplier than before and adding a forward or rule in it will apply to any wan. so opening the ssh 22 port with the example '''/etc/firewall.user''' line
{{{
iptables -t nat -A prerouting_wan -p tcp --dport 22 -j ACCEPT 
iptables        -A input_wan      -p tcp --dport 22 -j ACCEPT
}}}
will open port 22 to you router from both wan and wan2

This is it hope it can help
Ben
