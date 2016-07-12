I need to forward and allow external access to various ports, but editing the default firewall.user is error-prone and complex.  Here's an example of what my firewall uses:

file: /etc/firewall.user

{{{

#!/bin/sh
. /etc/fwlib.sh
flush_firewall

### Ports accessible on the router from the WAN
# allow_tcp_port 22 # SSH
# allow_tcp_port 465 # HTTPS

### Ports accessible from specific hosts to the router from the WAN
allow_tcp_port_fromhost 80 remote_access # HTTP
allow_tcp_port_fromhost 22 remote_access # HTTP

### Ports accessible to client machines.
# forward_port 22 server
forward_port 9100 printer_01

### if we really need _all_ ports...
# register_dmz server

# forward workstation port for application development
#forward_port 8080 workstation1

# forward a few utility port-ranges to make it easier to deal with
# bittorrent configurations and the like
# forward_port 10000:10099 workstation1
# forward_port 10100:10199 laptop1
# forward_port 10200:10299 laptop2

### Translate port for client machines.
translate_port 8080 printer_01 80

### Trusted hosts, full access to router
# trusted_host my_support_company

}}}

And here's the extremely simple firewall library that it uses:

'''Note:''' if you plan on pasting this script into an ssh window, note that the character quoted in the {{{cut}}} command below should probably be a tab, not a space (unless you use spaces to format your /etc/hosts file). ('''''Not relevant now as cut has been replaced with awk''''')

file: /etc/hosts

{{{

127.0.0.1 localhost OpenWrt
192.168.1.100 server
192.168.1.50 workstation1
192.168.1.80 laptop1
192.168.1.81 laptop2
195.xxx.xxx.xxx my_support_company
192.168.1.55 printer_01
195.xxx.xxx.xxx remote_access

}}}

file: /etc/fwlib.sh

{{{

#!/bin/sh

. /etc/functions.sh

WAN=$(nvram get wan_ifname)
LAN=$(nvram get lan_ifname)

flush_firewall () {
    iptables -F input_rule
    iptables -F output_rule
    iptables -F forwarding_rule
    iptables -t nat -F prerouting_rule
    iptables -t nat -F postrouting_rule
}

### BIG FAT DISCLAIMER
### The "-i $WAN" literally means packets that came in over the $WAN interface;
### this WILL NOT MATCH packets sent from the LAN to the WAN address.

allow_tcp_port () {
    ALLOWPORT=$1
    iptables -t nat -A prerouting_rule -i $WAN -p tcp --dport $ALLOWPORT -j ACCEPT
    iptables        -A input_rule      -i $WAN -p tcp --dport $ALLOWPORT -j ACCEPT
}

allow_tcp_port_fromhost () {
    ALLOWPORT=$1
    ALLOWHOSTNAME=$2
    ALLOWHOST=`sucky_resolve $ALLOWHOSTNAME`
    echo "Allowing tcp from $ALLOWHOSTNAME to port $ALLOWPORT"
    iptables -t nat -A prerouting_rule -i $WAN -p tcp -s $ALLOWHOST --dport $ALLOWPORT -j ACCEPT
    iptables        -A input_rule      -i $WAN -p tcp -s $ALLOWHOST --dport $ALLOWPORT -j ACCEPT
}

sucky_resolve () {
    HOSTNAME=$1
    ###
    grep $HOSTNAME /etc/hosts | awk '{ print $1 }'
}

forward_port() {
    ALLOWPORT=$1
    ALLOWHOSTNAME=$2
    ALLOWHOST=`sucky_resolve $ALLOWHOSTNAME`
    echo "FORWARDING $ALLOWPORT TO $ALLOWHOSTNAME ($ALLOWHOST)"
    iptables -t nat -A prerouting_rule -i $WAN -p tcp --dport $ALLOWPORT -j DNAT --to $ALLOWHOST
    iptables        -A forwarding_rule -i $WAN -p tcp --dport $ALLOWPORT -d $ALLOWHOST -j ACCEPT
}

translate_port() {
    ALLOWPORT=$1
    ALLOWHOSTNAME=$2
    ALLOWHOSTPORT=$3
    ALLOWHOST=`sucky_resolve $ALLOWHOSTNAME`
    echo "TRANSLATING $ALLOWPORT TO $ALLOWHOSTNAME ($ALLOWHOST:$ALLOWHOSTPORT)"
    iptables -t nat -A prerouting_rule -i $WAN -p tcp --dport $ALLOWPORT -j DNAT --to $ALLOWHOST:$ALLOWHOSTPORT
    iptables        -A forwarding_rule -i $WAN -p tcp --dport $ALLOWHOSTPORT -d $ALLOWHOST -j ACCEPT
}


trusted_host (){
    ALLOWHOSTNAME=$1
    TRUSTEDHOST=`sucky_resolve $ALLOWHOSTNAME`
    iptables -t nat -A prerouting_rule -i $WAN -p tcp -s $TRUSTEDHOST -j ACCEPT
    iptables        -A input_rule      -i $WAN -p tcp -s $TRUSTEDHOST -j ACCEPT
}

}}}
