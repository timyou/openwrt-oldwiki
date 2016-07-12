= Preface =
This howto describes how to setup ipv6 on your openwrt based router. 

It is based on the openwrt [http://openwrt.org/downloads/experimental/ experimental] version. 

There is 2 big different steps :
  * setup an ipv6 connection to a tunnel broker (like [http://www.sixxs.net SixXS] or [http://www.tunnelbroker.net hurricane electric])
  * propagate the IPv6 route to the LAN with radvd


= Install necessary software =
To use ipv6 we need the following modules:
 * ipv6 kernel module (always)
 * ipv6 routing software (always, to configure ipv6 routing)
 * ip6tables kernel modules (optional, if you need an ipv6 firewall)
 * ip6tables commandline tool (optional, to configure the ipv6 firewall)

== Install the ipv6 kernel modules ==
{{{
ipkg install http://nbd.vd-s.ath.cx/openwrt/packages/kmod-ipv6_2.4.30-1_mipsel.ipk
}}}

== Install the routing software ==
To configure the interfaces and the routing tables we need the new iputils. Additionally we need the route advertising daemon to propagate the IPv6 route to our local subnet.
{{{
ipkg install http://nbd.vd-s.ath.cx/openwrt/packages/ip_2.6.9-1_mipsel.ipk
ipkg install http://nbd.vd-s.ath.cx/openwrt/packages/radvd_0.7.3-1_mipsel.ipk
}}}

== Install the ip6tables kernel modules ==
{{{
ipkg install http://nbd.vd-s.ath.cx/openwrt/packages/kmod-ip6tables_2.4.30-1_mipsel.ipk
}}}

== Install the ip6tables package ==
{{{
ipkg install http://nbd.vd-s.ath.cx/openwrt/packages/ip6tables_1.3.1-1_mipsel.ipk
}}}

= Setup software =
== Kernel ==
Load the ipv6 module into the kernel:
{{{
insmod ipv6
}}}

If you want to load ipv6 module at boot time, just add 'ipv6' to /etc/modules:
{{{
echo ipv6 >> /etc/modules
}}}

After this your router has ipv6 support. To check this you could use ifconfig to validate the ::1/128 ipv6 address is assigned to the loopback device.
{{{
# ifconfig lo 
lo        Link encap:Local Loopback  
          inet addr:127.0.0.1  Mask:255.0.0.0
          inet6 addr: ::1/128 Scope:Host
          UP LOOPBACK RUNNING  MTU:16436  Metric:1
          RX packets:116 errors:0 dropped:0 overruns:0 frame:0
          TX packets:116 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0 
          RX bytes:10395 (10.1 KiB)  TX bytes:10395 (10.1 KiB)
}}}


Optionally, you can load the ip6table modules into the kernel
{{{
insmod ip6_tables
insmod ip6table_filter
}}}

To check the installation of ip6tables you can use the ip6tables show command.
{{{
# ip6tables -L
Chain INPUT (policy ACCEPT)
target     prot opt source               destination         

Chain FORWARD (policy ACCEPT)
target     prot opt source               destination         

Chain OUTPUT (policy ACCEPT)
target     prot opt source               destination
}}}

== IPTables ==
In my firewall script I had to add the following rule to let the encapsulated
packets pass:
{{{
iptables -A INPUT -p 41 -i $WAN -j ACCEPT
}}}
You need to place it into the right position of your firewall script (eg: just after/before "iptables -A INPUT -p 47 -j ACCEPT" ).

= Setup IPv6 connectivity =
## == PPP(oe): 6to4 tunnel with dynamic ip address ==
## When the ppp interface comes up, the ppp daemon calls the ip-up script, when it goes down the ip-down script. To place these ## scripts in /etc/ppp/ you must create a symbolic link from /tmp/ppp to /etc/ppp:
## {{{
## mkdir /etc/ppp
## ln -s /etc/ppp /tmp/ppp
## }}}
## 
## The content of the /etc/ppp/ip-up script:
## {{{
## #!/bin/sh
## 
## # set default route
## sbin/route add default ppp0
## 
## # 6to4 tunnel
## ipv4=$4
## ipv6prefix=`echo $ipv4 | awk -F. '{ printf "2002:%02x%02x:%02x%02x", $1, $2, $3, $4 }'`
## 
## ip tunnel add tun6to4 mode sit ttl 64 remote any local $ipv4
## ip link set dev tun6to4 up
## ip -6 addr add ${ipv6prefix}::1/16 dev tun6to4
## ip -6 route add 2000::/3 via ::192.88.99.1 dev tun6to4 metric 1
## 
## ip -6 addr add ${ipv6prefix}:5678::1/64 dev vlan2
## }}}
## 
## When the link goes down, the tunnel should be removed via /etc/ppp/ip-down
## {{{
## #!/bin/sh
## 
## # 6to4 tunnel
## ipv4=$4
## ipv6prefix=`echo $ipv4 | awk -F. '{ printf "2002:%02x%02x:%02x%02x", $1, $2, $3, $4 }'`
## 
## ip -6 addr del ${ipv6prefix}:5678::1/64 dev vlan2
## 
## ip -6 route flush dev tun6to4
## ip link set dev tun6to4 down
## ip tunnel del tun6to4
## }}}

== Static tunnel to SixXS.net ==
''Note: this script should works with all Tunnel Broker''
----
{{{
#!/bin/sh

LOCALIP=Your IPv4 Endpoint
POPIP=POP IPv4 Endpoint
LOCTUN=Your IPv6 Endpoint
REMTUN=SixXS IPv6 Endpoint

case $1 in
start)
	echo -n "Starting SixXS.Net IPv6 tunnel: "
	ip tunnel add sixxs mode sit local $LOCALIP remote $POPIP
	ip link set sixxs up
	ip link set mtu 1280 dev sixxs
	ip tunnel change sixxs ttl 64
	ip -6 addr add $LOCTUN/64 dev sixxs
	ip -6 ro add default via $REMTUN dev sixxs
	echo "Done."
	;;
stop)
	echo -n "Stopping SixXS.Net IPv6 tunnel: "
	ip link set sixxs down
	ip tunnel del sixxs
	echo "Done."
	;;
restart)
	$0 stop
	$0 start
	;;
*)
	echo "Usage: $0 {start | stop | restart}"
	;;
esac
exit 0
}}}

== Dynamic (heartbeat) tunnel to SixXS.net ==
{{{
ipkg install http://nbd.vd-s.ath.cx/openwrt/packages/aiccu_2005.01.31-1_mipsel.ipk
}}}

Edit /etc/aiccu.conf :
 * put your login/passwd
 * configure "ipv4_interface" (usually vlan1)
 * comment the "tunnel_id" line if you have only one tunnel

/!\  From the SixXS documentation :
'''Keep your machine NTP synced, if the timestamp difference is bigger than 120
seconds the heartbeat will be silently dropped. Note also that you need to select
the correct time zone.'''

This can be solved by installing ntpclient (to correctly set the clock on boot) and openntpd (to manage the drift).

Now start the sixxs client :
{{{
aiccu start
}}}

If it doesn't work use {{{logread}}} to see what occurs


= IPv6 on the LAN =
At this point I suppose that you have a working ipv6 connection on the wrt, that you can ''ping6 www.kame.net'' without error.

Using our mythical 3ffe:ffff:0:f101::/64 network, we would put in /etc/radvd.conf the following lines:
{{{
# For more examples, see the radvd documentation.

interface br0
{
        AdvSendAdvert on;

        prefix 3ffe:ffff:0:f101::/64
        {
                AdvOnLink on;
                AdvAutonomous on;
        };

};
}}}

Now we add {{{3ffe:ffff:0:f101::1}}} to br0 & forward our delegated /64 subnet to br0 :
{{{
ip -6 addr add 3ffe:ffff:0:f101::1/64 dev br0
}}}

After all this you can start the daemon:
{{{
/etc/init.d/S51radvd start
}}}
You can listen to its advertisments via the ''radvdump'' program.

= Example for debugging purposes =
Interface configuration:
{{{
root@OpenWrt:~# ip addr show
1: lo: <LOOPBACK,UP> mtu 16436 qdisc noqueue
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
    inet6 ::1/128 scope host
2: eth0: <BROADCAST,MULTICAST,PROMISC,UP> mtu 1500 qdisc pfifo_fast qlen 1000
    link/ether 00:0f:66:56:ee:6f brd ff:ff:ff:ff:ff:ff
    inet6 fe80::20f:66ff:fe56:ee6f/64 scope link
3: eth1: <BROADCAST,MULTICAST,PROMISC,UP> mtu 1500 qdisc pfifo_fast qlen 1000
    link/ether 00:0f:66:56:ee:71 brd ff:ff:ff:ff:ff:ff
    inet6 fe80::20f:66ff:fe56:ee71/64 scope link
4: sit0@NONE: <NOARP> mtu 1480 qdisc noop
    link/sit 0.0.0.0 brd 0.0.0.0
5: br0: <BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue
    link/ether 00:0f:66:56:ee:6f brd ff:ff:ff:ff:ff:ff
    inet 192.168.1.1/24 brd 192.168.1.255 scope global br0
    inet6 2001:6f8:309:1::1/64 scope global
    inet6 fe80::20f:66ff:fe56:ee6f/64 scope link
6: vlan0: <BROADCAST,MULTICAST,PROMISC,UP> mtu 1500 qdisc noqueue
    link/ether 00:0f:66:56:ee:6f brd ff:ff:ff:ff:ff:ff
    inet6 fe80::20f:66ff:fe56:ee6f/64 scope link
7: vlan1: <BROADCAST,MULTICAST,PROMISC,UP> mtu 1500 qdisc noqueue
    link/ether 00:0f:66:56:ee:70 brd ff:ff:ff:ff:ff:ff
    inet 212.68.233.114/24 brd 212.68.233.255 scope global vlan1
    inet6 fe80::20f:66ff:fe56:ee70/64 scope link
8: sixxs@NONE: <POINTOPOINT,NOARP,UP> mtu 1280 qdisc noqueue
    link/sit 212.68.233.114 peer 212.100.184.146
    inet6 2001:6f8:202:e::2/64 scope global
    inet6 fe80::d444:e972/64 scope link
    inet6 fe80::c0a8:101/64 scope link
}}}

Routing table:
{{{
root@OpenWrt:~# ip route show
192.168.1.0/24 dev br0  proto kernel  scope link  src 192.168.1.1
212.68.233.0/24 dev vlan1  proto kernel  scope link  src 212.68.233.114
default via 212.68.233.1 dev vlan1

root@openwrt:~# ip -6 route show
2001:6f8:202:e::/64 via :: dev sixxs  metric 256  mtu 1280 advmss 1220
2001:6f8:309:1::/64 dev br0  metric 256  mtu 1500 advmss 1220
fe80::/64 dev eth0  metric 256  mtu 1500 advmss 1220
fe80::/64 dev vlan0  metric 256  mtu 1500 advmss 1220
fe80::/64 dev eth1  metric 256  mtu 1500 advmss 1220
fe80::/64 dev br0  metric 256  mtu 1500 advmss 1220
fe80::/64 dev vlan1  metric 256  mtu 1500 advmss 1220
fe80::/64 via :: dev sixxs  metric 256  mtu 1280 advmss 1220
ff00::/8 dev eth0  metric 256  mtu 1500 advmss 1220
ff00::/8 dev vlan0  metric 256  mtu 1500 advmss 1220
ff00::/8 dev eth1  metric 256  mtu 1500 advmss 1220
ff00::/8 dev br0  metric 256  mtu 1500 advmss 1220
ff00::/8 dev vlan1  metric 256  mtu 1500 advmss 1220
ff00::/8 dev sixxs  metric 256  mtu 1280 advmss 1220
default via 2001:6f8:202:e::1 dev sixxs  metric 1024  mtu 1280 advmss 1220
}}}

Interface configuration of a client machine:
{{{
~$ ip addr show
1: lo: <LOOPBACK,UP> mtu 16436 qdisc noqueue
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
2: sit0: <NOARP> mtu 1480 qdisc noop
    link/sit 0.0.0.0 brd 0.0.0.0
3: eth0: <BROADCAST,MULTICAST,UP> mtu 1500 qdisc pfifo_fast qlen 1000
    link/ether 00:11:2f:1e:bf:65 brd ff:ff:ff:ff:ff:ff
    inet 192.168.1.42/24 brd 192.168.1.255 scope global eth0
    inet6 2001:6f8:309:1:211:2fff:fe1e:bf65/64 scope global dynamic
       valid_lft 2591812sec preferred_lft 604612sec
    inet6 fe80::211:2fff:fe1e:bf65/64 scope link
       valid_lft forever preferred_lft forever
}}}

= Links =
 * [http://www.757.org/~joat/wiki/index.php/IPv6_on_the_WRT54G_via_OpenWRT IPv6 on OpenWrt with Hurricane Electric]
 * [http://www.join.uni-muenster.de/TestTools/IPv6_Verbindungstests.php JOIN IPv6 Test Page (ping, traceroute, tracepath)]
 * [http://www.litech.org/radvd/ Route Advertising Daemon Homepage]
 * [http://www.bieringer.de/linux/IPv6/index.html Peter Bieringer's IPv6 HOWTO]

= ToDo =
 * list of ipv6 ready application available in openwrt
 * start/stop radvd when connection goes up/down

= Questions =
Any ideas?
{{{
@ap:/# ping6 fe80::20d:88ff:fea6:f554
Segmentation fault
@ap:/#
}}}

You probably have an ipv6.o which is incompatible with your version of the openwrt kernel. You should use kernel and modules from the same source; mixing them might not work (and probably does not).

Thanks - this worked!

{{{
May 20 01:29:22 wrt54gs radvd[376]: version 0.7.2 started
May 20 01:29:22 wrt54gs radvd[376]: IPv6 forwarding setting is: 0, should be 1
May 20 01:29:22 wrt54gs radvd[376]: IPv6 forwarding seems to be disabled, exiting
}}}

You need to add
{{{
echo 1 > /proc/sys/net/ipv6/conf/all/forwarding
}}}
to your enable script to enable ipv6 forwarding before you can run radvd.
