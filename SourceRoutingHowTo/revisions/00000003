source routing on OpenWrt How-To[[BR]]

the purpose of source routing:[[BR]]
to decide, on basis of the source address of packets, through which interface those packets should leave the router.

example of its use:[[BR]]
a system with multiple routes towards the internet.[[BR]] 

examples:[[BR]]
1) Two routers, each with an an adsl link and interconnected via lan, and each serving via their shared lan or a secondary lan a number of clients; but you want some clients to go out through one adsl line, and other clients through the other.[[BR]]
2) A router with two adsl connections, ppp0 and ppp1, and you want some clients to use ppp0 , and others to use ppp1.[[BR]]

prerequisites:[[BR]]
ip package (use 'ipkg install')[[BR]]

example script that should be executed upon boot; in Whiterussian place in //etc/init.d e.g. as S80routes_2ISPS[[BR]]

#!/bin/sh[[BR]]
# S80routes_2ISPS ; script for OpenWrt by 'doddel'[[BR]]
# separate traffic between two adsl connections, one on this router ('HERE') and the other on a router[[BR]] 
# that is reached via vlan2 and has in this example ip address 192.168.2.14 ('THERE')[[BR]]
# assumption is that this router talks to clients through vlan0 (lan) and through eth1 (wifi)[[BR]]
# I normally do not use the bridge br0 as it pollutes the scarce radio channel resource with[[BR]]
# unnecessary traffic but this is unrelated to the essentials of source routing.[[BR]]
# This router 'HERE'is assumed to have following interfaces:[[BR]]
# ppp0 ; dynamical ip address, assigned by isp[[BR]]
# vlan0 ; the lan with ip address 192.168.10.10/24[[BR]]
# vlan1 ; used by pppd to create ppp0[[BR]]
# vlan2 ; the lan2 used to connect to the other router that also has adsl; ip address HERE 192.168.2.10[[BR]]
# eth1 ; wifi, with ip address 192.168.6.10, talking per radio to router 192.168.6.100 that serves clients[[BR]]
# IMPORTANT: modify  //sbin/ifup.pppoe: change 'defaultroute' option into 'nodefaultroute';[[BR]]
# when adsl gets connected the routing settings. made by this script, do not get overwritten by pppd[[BR]]

# the client's ip addresses[[BR]]
client1_lan="192.168.10.0/24"	# just an example of a group of clients on 'lan'(vlan0) to be routed equally[[BR]]
client2_wlan="192.168.12.1/32"	# just another example of a unique client reached per radio here and needing unique routing[[BR]]
# add the list of clients[[BR]]


# abbreviations used filling the 'main' routing table using 'route' commands[[BR]] 
HERE="netmask 255.255.255.0 gw 192.168.6.100 dev eth1"	# define the gateway that serves the clients reached per radio[[BR]]
THERE="netmask 255.255.255.0 gw 192.168.2.14 dev vlan2" # define the route to the second router[[BR]]

# define routes to subnets hidden behind routers reached via radio[[BR]]
route add -net 192.168.11.0 ${HERE} # one subnet reachable via eth1 and gateway 192.168.6.100[[BR]]
route add -net 192.168.12.0 ${HERE} # another subnet reachable via eth1 and gateway 192.168.6.100[[BR]]
# .... more[[BR]]

# define routes to subnets that are reacheable via the other adsl router[[BR]]
route add -net 192.168.4.0   ${THERE} # one subnet reachable via vlan2 and gateway 192.168.2.14[[BR]]
route add -net 192.168.57.0  ${THERE} # one subnet reachable via vlan2 and gateway 192.168.2.14[[BR]]
# .....more[[BR]]

# get current ip numbers of the ppp0 interface[[BR]]
pubip=$(ifconfig ppp0 | grep 'inet addr' | awk '{print $2}' | sed -e 's/.*://') # public dynamic IP[[BR]]
gwyip=$(ifconfig ppp0 | grep 'inet addr' | awk '{print $3}' | sed -e 's/.*://') # ISP P-t-p gateway IP[[BR]]

# abbreviations used filling the tables '200' '201' and '202' using 'ip route ' commands[[BR]] 
# table 200 is always checked and has all internal routes, table 201 will be checked only for those source addresses[[BR]]
# that should leave via THERE and contains THERE as default route, 202 contains HERE as default route[[BR]]
HERE="via 192.168.6.100 dev eth1 table 200"[[BR]]
THERE="via 192.168.2.14 dev vlan2 table 200"[[BR]]
THERE202="via 192.168.2.14 dev vlan2 table 202"[[BR]]

# populate the table [200] with routes equal for all (know to reach all clients)[[BR]]
ip route flush table 200[[BR]]
# the native interfaces (are set by OS in table 'main' but need being set manually in table [200])[[BR]]
ip route add to $gwyip dev ppp0 protocol kernel scope link src $pubip table 200					# ppp0[[BR]]
ip route add to 192.168.10.0/24	dev vlan0	protocol kernel scope link src 192.168.10.10	table 200	# lan[[BR]] 
ip route add to 192.168.2.0/24	dev vlan2	protocol kernel scope link src 192.168.2.10	table 200	# vlan2[[BR]]
ip route add to 192.168.6.0/24	dev eth1	protocol kernel scope link src 192.168.6.10	table 200	# eth1[[BR]]

# always forced towards or via ISP via local adsl[[BR]]
ip route add to <subnet of isp dns>/24	via $gwyip dev ppp0 table main		# reach isp's dns servers via local adsl[[BR]]
ip route add to <subnet of dynamic dns>/24	via $gwyip dev ppp0 table main	# reach the the dynamic dns servers[[BR]]
ip route add to <subnet of isp dns>/24	via $gwyip dev ppp0 table 200		# same in table 200 as in table main[[BR]]
ip route add to <subnet of dynamic dns>/24	via $gwyip dev ppp0 table 200	# same in table 200 as in table main[[BR]]

# the routes via HERE wifi network[[BR]]
ip route add to 192.168.11.0/24 ${HERE}		# clients reached via local radio[[BR]]
ip route add to 192.168.12.0/24 ${HERE}		# more clients reached via local radio[[BR]]
# more ...[[BR]]

# the routes via THERE wifi and/or lan network[[BR]]
ip route add to 192.168.4.0/24   ${THERE}	# clients reached via THERE[[BR]]
ip route add to 192.168.57.0/24  ${THERE}	# more clients reached via THERE[[BR]]
# more ....[[BR]]

# populate table [201], the default HERE gateway[[BR]]
ip route flush table 201[[BR]]
ip route add to default via $gwyip dev ppp0 table 201[[BR]]

# populate table [202], the alternative THERE gateway[[BR]]
ip route flush table 202[[BR]]
ip route add to default ${THERE202}[[BR]]

# now define rules for table selection, starting with highest priority[[BR]]
# find internal destination, this table gets checked for any source address [200][[BR]]
ip rule delete from 0/0 priority 50 table 200[[BR]]
ip rule add from 0/0 priority 50 table 200[[BR]]
# more ... delete/add pairs, one for each client that should use THERE[[BR]]

# what comes in via HERE's lan and wifi[[BR]]
# decide what should go out THERE and therefore should use table [202][[BR]]
ip rule delete	from ${client1_lan}	iif vlan0	priority 51 table 202[[BR]]
ip rule add	from ${client1_lan}	iif vlan0	priority 51 table 202	# client1 uses THERE's adsl to reach internet[[BR]]

# rest must go out HERE and should therefore check table [201][[BR]]
ip rule delete	from 0/0				priority 52 table 201[[BR]]
ip rule add	from 0/0				priority 52 table 201[[BR]]
ip rule delete	iif lo					priority 53 table 201[[BR]]
ip rule add	iif lo					priority 53 table 201[[BR]]
ip rule delete	from 127.0.0.0/8			priority 54 table 201[[BR]]
ip rule add	from 127.0.0.0/8			priority 54 table 201	# anything else is HERE default[[BR]]

# now client1's traffic will use the adsl of the other router while client2's traffic goes out here locally.[[BR]]
# when adding more rules make sure that the priorities are unique per client and increase per rule (higher priority number is checked later, so the internal destinations are always checked first, then whatever should leave THERE, and what remains must leave HERE)[[BR]]

# make the rules active, deleting old stuff[[BR]]
ip route flush cache
[[BR]]
