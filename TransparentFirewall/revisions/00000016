Howto setup a transparent firewall (or possibly, a wireless bridge)

''' WARNING: You should be familiar with booting Failsafe mode on your router when using this document.  The firewall rules can be tricky, and you can easily lock yourself out.'''


== Background ==

I work at a university where every computer is connected to the internet with a public IP address.  This leaves all computers open to direct attack by hackers/worms on the internet.  I have used cheap NAT routers to protect most computers, but I need something a bit smarter to protect my servers.

Why are the servers different?  

 * The servers must use public IP addresses in order to be accessible to the clients.  If I were to use NAT with port forwarding, I would be restricted to one service per port.  This is simply not possible with the services we have running.
 * Because the cheap NAT routers block all incoming traffic that is not in the NAT table.  The servers need to have certain ports open for file sharing, printing, etc.  But I only want those services available to our local subnet.  The cheap NAT routers do not have the ability to port forward packets from the local subnet only.
 * The University's 'ISP' restricts each ethernet port to a single MAC address, very much the same way a wireless AP restricts each associated client to a single MAC address.  This means that not only do I need a transparent firewall, but I need IP layer bridging and MAC layer NAT.  


== Network Topology ==

[http://www.psyc.vt.edu/openwrt/topology.jpg]

== Kernel Patching ==

Patching the kernel is no longer necessary with WhiteRussian RC5.  You just need to install the following additional packages:

{{{
ebtables
kmod-ebtables
parprouted
}}}

Next, create the file /etc/modules.d/60-net:
{{{
ebtables
ebtable_broute
ebtable_filter
ebtable_nat
ebt_arp
ebt_arpreply
ebt_dnat
ebt_ip
ebt_log
ebt_pkttype
ebt_redirect
ebt_snat
ebt_stp
ebt_ulog
ebt_vlan
}}}


=== NVRAM Variables ===

The following nvram variables need to be set.  The variables set to '[set]' need to be set to your environment.

{{{
lan_gateway=[set]
lan_netmask=[set]
lan_ifnames=vlan0
lan_dns=[set1] [set2] ...
lan_proto=static
lan_ipaddr=[set]
lan_ifname=vlan0
wan_proto=static
wan_ifname=vlan1
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
#
# This file is /etc/init.d/S44L2firewall

${FAILSAFE:+exit}

IFCONFIG=/sbin/ifconfig
BRCTL=/usr/sbin/brctl
EBTABLES=/usr/sbin/ebtables

LAN_IF=$(nvram get lan_ifname)
LAN_IP=$(nvram get lan_ipaddr)
LAN_MASK=$(nvram get lan_netmask)
LAN_MAC=$($IFCONFIG $LAN_IF | \
  /bin/grep "HWaddr" | \
  /bin/sed 's/.*HWaddr \(.*\)/\1/g')
LAN_GW=$(nvram get lan_gateway)

WAN_IF=$(nvram get wan_ifname)
WAN_MAC=$($IFCONFIG $WAN_IF | \
  /bin/grep "HWaddr" | \
  /bin/sed 's/.*HWaddr \(.*\)/\1/g')

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

  echo "  Adding LAN interface..."
  $IFCONFIG $LAN_IF inet 0.0.0.0
  $BRCTL addif $BR_IF $LAN_IF

  echo "  Adding WAN interface..."
  $IFCONFIG $WAN_IF down hw ether $LAN_MAC
  $IFCONFIG $WAN_IF inet 0.0.0.0
  $BRCTL addif $BR_IF $WAN_IF

  echo "  Configuring Bridge interface..."
  $IFCONFIG $BR_IF inet 0.0.0.0 up

  echo "  Configuring LAN interface..."
  $IFCONFIG $LAN_IF inet $LAN_IP netmask 255.255.255.255

  echo "  Configuring WAN interface..."
  $IFCONFIG $WAN_IF inet $LAN_IP netmask $LAN_MASK

  echo "  Adding default route..."
  /sbin/route add default gw $LAN_GW dev $WAN_IF

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

# Block IP traffic sourced outside the LAN subnet
$EBTABLES -t filter -A FORWARD -i $WAN_IF \
  -p 0x0800 --ip-src ! $LAN_IP/$LAN_MASK -j DROP

# force all outgoing packets to have router's MAC address
$EBTABLES -t nat -A POSTROUTING -o $WAN_IF -j snat --to-source $WAN_MAC


}}}

Next, the layer3 firewall:

{{{
#!/bin/sh

${FAILSAFE:+exit}

echo "Configuring layer3 firewall..."

IFCONFIG=/sbin/ifconfig
BRCTL=/usr/sbin/brctl
IPTABLES=/usr/sbin/iptables

LAN_IF=$(nvram get lan_ifname)
LAN_IP=$(nvram get lan_ipaddr)
LAN_MASK=$(nvram get lan_netmask)

WAN_IF=$(nvram get wan_ifname)

BR_IF=br0
BR_STP=off


## CLEAR TABLES
for T in filter nat mangle; do
  iptables -t $T -F
  iptables -t $T -X
done

### INPUT
### (connections with the router as destination)
  echo "  Configuring INPUT chain..."

  # allow IP packets from the LAN
  iptables -A INPUT -s $LAN_IP/$LAN_MASK -j ACCEPT

  # base case
  iptables -A INPUT -m state --state INVALID -j DROP
  iptables -A INPUT -m state --state RELATED,ESTABLISHED -j ACCEPT

  # Deny the rest
  iptables -A INPUT -j DROP


### OUTPUT
### (connections with the router as source)
  echo "  Configuring OUTPUT chain..."


### OUTPUT
### (connections with the router as source)
  echo "  Configuring OUTPUT chain..."


### FORWARDING
### (connections routed through the router)
  echo "  Configuring FORWARDING chain..."

  # allow IP packets from the LAN to the LAN
  iptables -A FORWARD -s $LAN_IP/$LAN_MASK -d $LAN_IP/$LAN_MASK -j ACCEPT

  # base case
  iptables -A FORWARD -m state --state INVALID -j DROP
  iptables -A FORWARD -p tcp --tcp-flags SYN,RST SYN -j TCPMSS --clamp-mss-to-pm
  iptables -A FORWARD -m state --state RELATED,ESTABLISHED -j ACCEPT

  # allow
  iptables -A FORWARD -i ! $WAN_IF -o $WAN_IF -j ACCEPT

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
