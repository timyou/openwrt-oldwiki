#format nowiki

#!/bin/sh
# Quality of service script for Cable

. /etc/functions.sh

IPT=/usr/sbin/iptables
IP=/usr/sbin/ip
TC=/usr/sbin/tc

# Specify ethernet device, queue length, MTU
DEV=vlan1
OUT_QLEN=30
MTU=1492

# Set to ~80% of tested maximum
UPLINK=300

# Specify class rates
UPLINK_1_R=200  # VOIP only
UPLINK_2_R=64   # Interactive traffic and ICMP/ACK
UPLINK_3_R=36   # Everything else

# Each class is also permitted to consume all of available bandwidth
# if no other classes are in use
UPLINK_1_C=${UPLINK}
UPLINK_2_C=${UPLINK}
UPLINK_3_C=${UPLINK}

# Set outgoing queue length 
$IP link set dev $DEV qlen ${OUT_QLEN} 

# Remove old qdiscs
$TC qdisc del dev $DEV root 2> /dev/null > /dev/null
$TC qdisc del dev $DEV ingress 2> /dev/null > /dev/null

# Create HTB root qdisc with an htb default of 30 
$TC qdisc add dev $DEV root handle 1: htb default 30 

# Create main rate limit class 
$TC class add dev $DEV parent 1: classid 1:1 htb rate ${UPLINK}kbit ceil ${UPLINK}kbit

# Create leaf rate limit classes 
$TC class add dev $DEV parent 1:1 classid 1:10 htb rate ${UPLINK_1_R}kbit ceil ${UPLINK_1_C}kbit prio 0
$TC class add dev $DEV parent 1:1 classid 1:20 htb rate ${UPLINK_2_R}kbit ceil ${UPLINK_2_C}kbit prio 1
$TC class add dev $DEV parent 1:1 classid 1:30 htb rate ${UPLINK_3_R}kbit ceil ${UPLINK_3_C}kbit prio 2 

# Attach qdisc to leaf classes - here we at SFQ to each priority class. SFQ 
# insures that within each class connections will be treated (almost) fairly. 
$TC qdisc add dev $DEV parent 1:10 handle 10: sfq perturb 10 
$TC qdisc add dev $DEV parent 1:20 handle 20: sfq perturb 10 
$TC qdisc add dev $DEV parent 1:30 handle 30: sfq perturb 10  

$TC filter add dev $DEV parent 1:0 protocol ip prio 1 handle 1 fw classid 1:10
$TC filter add dev $DEV parent 1:0 protocol ip prio 2 handle 2 fw classid 1:20
$TC filter add dev $DEV parent 1:0 protocol ip prio 3 handle 3 fw classid 1:30

# UDP traffic in 1:10
tc filter add dev $DEV parent 1:0 protocol ip prio 10 u32 match ip protocol 17 0xff flowid 1:10

# Already marked TOS Minimum Delay (ssh, NOT scp) in 1:20:
tc filter add dev $DEV parent 1:0 protocol ip prio 10 u32 match ip tos 0x10 0xff  flowid 1:20

# ICMP (ip protocol 1) in the interactive class 1:20 so we 
# can do measurements & impress our friends:
tc filter add dev $DEV parent 1:0 protocol ip prio 10 u32 match ip protocol 1 0xff flowid 1:20
        
# To speed up downloads while an upload is going on, put ACK packets in
# the interactive class:
tc filter add dev $DEV parent 1: protocol ip prio 10 u32 match ip protocol 6 0xff match u8 0x05 0x0f at 0 match u16 0x0000 0xffc0 at 2 match u8 0x10 0xff at 33 flowid 1:20
