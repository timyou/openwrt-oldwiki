Howto setup a transparent firewall (or possibly, a wireless bridge)

''' WARNING: You should be familiar with booting Failsafe mode on your router when using this document.  The firewall rules can be tricky, and you can easily lock yourself out.'''


== Background ==

I work at a university where every computer is connected to the internet with a public IP address.  This leaves all computers open to direct attack by hackers/worms on the internet.  I have used cheap NAT routers to protect most computers, but I need something a bit smarter to protect my servers.

Why are the servers different?  

 * The servers must use public IP addresses in order to be accessible to the clients.  If I were to use NAT with port forwarding, I would be restricted to one service per port.  This is simply not possible with the services we have running, because the cheap NAT routers block all incoming traffic that is not in the NAT table.  
 * The servers need to have certain ports open for file sharing, printing, etc.  But I only want those services available to our local subnet.  The cheap NAT routers do not have the ability to port forward packets from the local subnet only.
 * The University's 'ISP' restricts each ethernet port to a single MAC address, very much the same way a wireless AP restricts each associated client to a single MAC address.  This means that not only do I need a transparent firewall, but I need IP layer bridging and MAC layer NAT.  


== Network Topology ==

[http://www.psyc.vt.edu/openwrt/topology.jpg]

== Kernel Patching ==

Patching the kernel is no longer necessary with WhiteRussian RC5.  You just need to install the following additional packages:

{{{
ebtables
kmod-ebtables
kmod-ipt-extra
parprouted
}}}



=== NVRAM Variables ===

The following nvram variables need to be set.  The variables set to '[set]' need to be set to your environment.

{{{
wan_proto=static
wan_ifname=vlan1
wan_ifnames=vlan1
wan_ipaddr=[set]
wan_netmask=[set]
wan_gateway=[set]

lan_proto=static
lan_ifname=vlan0
lan_ifnames=vlan0
lan_ipaddr=[set]
lan_netmask=[set]
}}}

=== System Variables ===

Make sure you have the following two lines in your /etc/sysctl.conf

{{{
net.bridge.bridge-nf-call-iptables=0
net.bridge.bridge-nf-filter-vlan-tagged=0
}}}

=== Firewall Scripts ===

First, the layer2 firewall:

{{{
#!/bin/ash

IFCONFIG=/sbin/ifconfig
BRCTL=/usr/sbin/brctl
EBTABLES=/usr/sbin/ebtables

LAN_IF=$(nvram get lan_ifname)
LAN_IP=$(nvram get lan_ipaddr)
LAN_MASK=$(nvram get lan_netmask)
LAN_MAC=$($IFCONFIG $LAN_IF | \
  /bin/grep "HWaddr" | \
  /bin/sed 's/.*HWaddr \(.*\)/\1/g')

WAN_IF=$(nvram get wan_ifname)
WAN_IP=$(nvram get wan_ipaddr)
WAN_MAC=$($IFCONFIG $WAN_IF | \
  /bin/grep "HWaddr" | \
  /bin/sed 's/.*HWaddr \(.*\)/\1/g')
WAN_GW=$(nvram get wan_gateway)

BR_IF=br0
BR_STP=off



# ===================================================
# ORDER IS CRITICAL IN BRIDGE SETUP, DONT MUCK IT UP!
# ===================================================

$IFCONFIG $BR_IF > /dev/null 2> /dev/null
if [ $? != 0 ]; then
  echo "Creating bridge interface:"
  echo "  Creating bridge..."
  $BRCTL addbr $BR_IF
  $BRCTL stp $BR_IF $BR_STP

  echo "  Adding WAN interface..."
  $IFCONFIG $WAN_IF inet 0.0.0.0
  $BRCTL addif $BR_IF $WAN_IF

  echo "  Adding LAN interface..."
  $IFCONFIG $LAN_IF down hw ether $WAN_MAC
  $IFCONFIG $LAN_IF inet 0.0.0.0
  $BRCTL addif $BR_IF $LAN_IF

  echo "  Configuring Bridge interface..."
  $IFCONFIG $BR_IF inet 0.0.0.0 up

  echo "  Configuring WAN outside interface..."
  $IFCONFIG $WAN_IF inet $WAN_IP netmask $WAN_MASK

  echo "  Configuring WAN inside interface..."
  $IFCONFIG $LAN_IF inet $WAN_IP netmask $WAN_MASK

  echo "    Configuring LAN interface..."
  $IFCONFIG $LAN_IF:0 inet $LAN_IP netmask $LAN_MASK

  echo "  Adding default route..."
  /sbin/route add default gw $WAN_GW dev $WAN_IF

else
  echo "Bridge already configured."
fi


echo "Configuring bridge firewall..."
## CLEAR TABLES
for T in filter nat broute; do
  $EBTABLES -t $T -F
  $EBTABLES -t $T -X
done

# force ARP requests/replies and IP traffic to be routed on layer3
$EBTABLES -t broute -A BROUTING -p 0x0806 -j DROP

# Route LAN DHCP requests
$EBTABLES -t broute -A BROUTING -p 0x0800 -i $LAN_IF --ip-protocol 17 \
  --ip-source-port 67:68 --ip-destination-port 67:68 -j DROP

# Route LAN packets
$EBTABLES -t broute -A BROUTING -p 0x0800 -i $LAN_IF \
  --ip-source $LAN_IP/$LAN_MASK -j DROP

# Route IP traffic sourced outside the LAN subnet (blocked later)
$EBTABLES -t filter -A FORWARD -i $WAN_IF \
  -p 0x0800 --ip-src ! $WAN_IP/$WAN_MASK -j DROP

# Defined accept rule for accounting purposes
$EBTABLES -t filter -A FORWARD -j ACCEPT

# force all outgoing packets to have router's MAC address
$EBTABLES -t nat -A POSTROUTING -o $WAN_IF -j snat --to-source $WAN_MAC
}}}

Next, the layer3 firewall:

{{{
#!/bin/sh

echo "Configuring layer3 firewall..."

IFCONFIG=/sbin/ifconfig
BRCTL=/usr/sbin/brctl
IPTABLES=/usr/sbin/iptables

LAN_IF=$(nvram get lan_ifname)
LAN_IP=$(nvram get lan_ipaddr)
LAN_MASK=$(nvram get lan_netmask)

WAN_IF=$(nvram get wan_ifname)
WAN_IP=$(nvram get wan_ipaddr)
WAN_MASK=$(nvram get wan_netmask)

BR_IF=br0
BR_STP=off

# Required kernel modules
/sbin/insmod ipt_recent.o       2> /dev/null
/sbin/insmod ipt_ttl.o          2> /dev/null
/sbin/insmod ipt_TTL.o          2> /dev/null
/sbin/insmod ebtables           2> /dev/null
/sbin/insmod ebtable_broute     2> /dev/null
/sbin/insmod ebtable_filter     2> /dev/null
/sbin/insmod ebtable_nat        2> /dev/null
/sbin/insmod ebt_ip             2> /dev/null
/sbin/insmod ebt_snat           2> /dev/null



## CLEAR TABLES
for T in filter nat mangle; do
  iptables -t $T -F
  iptables -t $T -X
done


### INPUT
### (connections with the router as destination)
  echo "  Configuring INPUT chain..."

  # accept dhcp packets first, they dont have source IP yet
  iptables -A INPUT -i $LAN_IF -p UDP --sport 68 --dport 67 -j ACCEPT

  # stateful packets allowed
  iptables -A INPUT -m state --state INVALID -j DROP
  iptables -A INPUT -m state --state RELATED,ESTABLISHED -j ACCEPT

  # allow packets from the private NAT LAN
  iptables -A INPUT -i ppp+ -s $LAN_IP/$LAN_MASK -j ACCEPT
  iptables -A INPUT -i $LAN_IF -s $LAN_IP/$LAN_MASK -j ACCEPT

  # allow packets from loopback
  iptables -A INPUT -i lo -s 127.0.0.1 -d 127.0.0.1 -j ACCEPT

  # Connections allowed to firewall from WAN
  # ICMP
  iptables -A INPUT -p ICMP -j ACCEPT

  # allow IP packets from the WAN
  iptables -A INPUT -s $WAN_IP/$WAN_MASK -j ACCEPT

  # SSH
  iptables -A INPUT -p TCP --dport 22 \
    -m recent --name ROUTER-SSH --update --hitcount 5 --seconds 180 -j DROP
  iptables -A INPUT -p TCP --dport 22 \
    -m recent --name ROUTER-SSH --set -j ACCEPT

  # PPTP
  iptables -A INPUT -p TCP --dport 1723 \
    -m recent --name ROUTER-PPTP --update --hitcount 5 --seconds 180 -j DROP
  iptables -A INPUT -p TCP --dport 1723 \
    -m recent --name ROUTER-PPTP --set -j ACCEPT
  iptables -A INPUT -d $LAN_IP -p 47 -j ACCEPT

  # FTP
  iptables -A INPUT -p TCP --dport 21 \
    -m recent --name ROUTER-FTP --update --hitcount 5 --seconds 180 -j DROP
  iptables -A INPUT -p TCP --dport 21 \
    -m recent --name ROUTER-FTP --set -j ACCEPT

  # Deny the rest
  iptables -A INPUT -j DROP



### Output
### (connections with the router as source)
  echo "  Configuring OUTPUT table..."
  iptables -A OUTPUT -o $WAN_IF -p ICMP --icmp-type 0 -j ACCEPT
  iptables -A OUTPUT -o $WAN_IF -p ICMP --icmp-type 8 -j ACCEPT
  iptables -A OUTPUT -o $WAN_IF -p ICMP -j DROP



### NAT
### (connections with the router as source)
  echo "  Configuring NAT table..."

  # apply NAT to local packets headed to the WAN
  iptables -t nat -A POSTROUTING -o $WAN_IF -s $LAN_IP/$LAN_MASK -j MASQUERADE
  iptables -t nat -A POSTROUTING -o $LAN_IF -s $LAN_IP/$LAN_MASK -j MASQUERADE



### PREROUTING
### (packet hacks)

  iptables -A PREROUTING -t mangle -d ! $LAN_IP -j TTL --ttl-inc 1


### FORWARD
### (connections routed through the router)
  echo "  Configuring FORWARD chain..."

  # statefull packets allowed
  iptables -A FORWARD -m state --state INVALID -j DROP
  iptables -A FORWARD -p tcp --tcp-flags SYN,RST SYN -j TCPMSS --clamp-mss-to-pmtu
  iptables -A FORWARD -m state --state RELATED,ESTABLISHED -j ACCEPT

  # allow IP packets from the LAN to the LAN
  iptables -A FORWARD -s $WAN_IP/$WAN_MASK -d $WAN_IP/$WAN_MASK -j ACCEPT

  # allow LAN and PPP connections to LAN
  iptables -A FORWARD -i ppp+ -o $LAN_IF -j ACCEPT
  iptables -A FORWARD -i $LAN_IF -o $LAN_IF -j ACCEPT

  # Block VPN clients from routing to the internet
  #iptables -A FORWARD -s 128.173.94.229 -o $WAN_IF -j DROP

  # allow outbound connections
  iptables -A FORWARD -i ppp+ -o $WAN_IF -j ACCEPT
  iptables -A FORWARD -i $LAN_IF -o $WAN_IF -j ACCEPT
  iptables -A FORWARD -i $BR_IF -o $WAN_IF -s $LAN_IP/$LAN_MASK -j ACCEPT

  # Deny the rest
  iptables -A FORWARD -j DROP

}}}


== Will this work as a wireless bridge? ==

That is a good question.  I have not tried it, but in theory it should work.  I would start off by reading the ClientModeHowto.  Get your WRT connected to your wireless AP, verify that it fully works.  Then follow this document, changing the following nvram variables above:

{{{
wan_ifname=eth1
}}}

If someone gets this working over wireless, fill in here and let us know...

== DISCLAIMER ==

As always, you need to test test test.  I am new to Linux, so dont count on my scripts to be perfect.  I'm just trying to save someone else some time, and to help demonstrate how robust OpenWRT can be.
