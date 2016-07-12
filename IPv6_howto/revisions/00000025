= Preface =
This howto first describes how to setup ipv6 on your openwrt based router. 

It also describes how to setup ipv6 for
 * A 6to4 tunnel over a ppp(oe) connection with a dynamic IP address. 
 * A tunnel to an ipv6 tunnel broker (e.g. [http://www.sixxs.net/ Sixxs])

= Install necessary software =
To use ipv6 we need the following modules
 * The '''ipv6 kernel module''' (always)
 * ipv6 '''routing software''' (recommended, to configure ipv6 routing)
 * The '''ip6tables kernel modules''' (optional, if you need an ipv6 firewall)
 * '''ip6tables commandline tool''' (optional, to configure the ipv6 router)

== Install the ipv6 kernel modules ==
Kernel modules are compiled for a specific version of the linux kernel on the openwrt router. If you use kernel modules for a slightly different kernel version, you might experience several problems with the kernel and/or configuration tools.

If you used a [http://www.openwrt.org/downloads/snapshots/ CVS snapshot] without ipv6 packages to install your routers kernel, you already have a file called openwrt-kmodules.tar.bz2 with several kernel modules compiled for this specific kernel. This file contains in the modules/2.4.20/kernel/net/ipv6/ directory the module ipv6.o. This file should be copied to the /lib/modules/2.4.20/kernel/net/ipv6/ directory on your router.

If you used a CVS snapshot with ipv6 packages (should be available from 2004-08-25) or when you have built the packages from CVS, you can just install the '''kmod-ipv6''' package from this tarball.

If you used an older kernel without openwrt-kmodules.tar.bz2 or one from an other source, you should use the ipv6.o from that kernel source.

== Install the routing software ==
To configure the interfaces and the routing tables we need the new iputils. Additionally we need the route advertising daemon to propagate the IPv6 route to our local subnet.
{{{
ipkg install http://www.linuxops.net/ipkg/ip_1.0_mipsel.ipk
ipkg install http://www.openwrt.org/ipkg/radvd_0.7.2_mipsel.ipk
}}}

== Install the ip6tables kernel modules ==
If you used a CVS snapshot with ipv6 packages (should be available from 2004-08-25) or when you have built the packages from CVS, you can just install the '''kmod-ipt6''' package from this tarball.

If you used an other package, you already have a file called openwrt-kmodules.tar.bz2 with several kernel modules compiled for this specific kernel. This file contains in the modules/2.4.20/kernel/net/ipv6/netfilter/ directory the modules needed for ip6tables. These files [[FootNote(or at least ip_6tables.o and ip6table_filter.o)]] should be copied to the /lib/modules/2.4.20/kernel/net/ipv6/ directory on your router.

== Install the ip6tables package ==
The latest [http://www.openwrt.org/downloads/snapshots/ CVS snapshots] contain an ip6tables package with the ip6tables program compiled for the exact kernel version. An other option is to install te package with
{{{
ipkg install <todo: Find up-to-date ipkg reference>
}}}

= Setup software =
== Kernel ==
Load the ipv6 module into the kernel:
{{{
insmod ipv6
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

= Setup IPv6 connectivity =
== PPPD: 6to4 tunnel with dynamic ip address ==
When the ppp interface comes up, the ppp daemon calls the ip-up script, when it goes down the ip-down script. To place these scripts in /etc/ppp/ you must create a symbolic link from /tmp/ppp to /etc/ppp:
{{{
mkdir /etc/ppp
ln -s /etc/ppp /tmp/ppp
}}}

The content of the /etc/ppp/ip-up script:
{{{
#!/bin/sh

# set default route
/sbin/route add default ppp0

# set time
/bin/sleep 2
/usr/sbin/rdate rtime.urz.tu-dresden.de

# 6to4 tunnel
ipv4=$4
ipv6prefix=`echo $ipv4 | awk -F. '{ printf "2002:%02x%02x:%02x%02x", $1, $2, $3, $4 }'`

ip tunnel add tun6to4 mode sit ttl 64 remote any local $ipv4
ip link set dev tun6to4 up
ip -6 addr add ${ipv6prefix}::1/16 dev tun6to4
ip -6 route add 2000::/3 via ::192.88.99.1 dev tun6to4 metric 1

ip -6 addr add ${ipv6prefix}:5678::1/64 dev vlan2
}}}

When the link goes down, the tunnel should be removed via /etc/ppp/ip-down
{{{
#!/bin/sh

# 6to4 tunnel
ipv4=$4
ipv6prefix=`echo $ipv4 | awk -F. '{ printf "2002:%02x%02x:%02x%02x", $1, $2, $3, $4 }'`

ip -6 addr del ${ipv6prefix}:5678::1/64 dev vlan2

ip -6 route flush dev tun6to4
ip link set dev tun6to4 down
ip tunnel del tun6to4
}}}

=== IPTables ===
In my firewall scrip I had to add the following rule to let the encapsulated packets pass:
{{{
$IPT -A INPUT -p 41 -i ppp0 -j ACCEPT
}}}
You need to place it into the right position of your firewall script.

=== route advertising daemon ===
This is the configuration file /etc/radvd.conf:
{{{
# For more examples, see the radvd documentation.

interface vlan2
{
        AdvSendAdvert on;

#
# These settings cause advertisements to be sent every 3-10 seconds.  This
# range is good for 6to4 with a dynamic IPv4 address, but can be greatly
# increased when not using 6to4 prefixes.
#

        MaxRtrAdvInterval 30;

        prefix 0:0:0:5678::/64
        {
                AdvOnLink on;
                AdvAutonomous on;
        #       AdvRouterAddr off;
                Base6to4Interface ppp0;

                AdvValidLifetime 300;
                AdvPreferredLifetime 120;
        };

};
}}}
After wrting the configfile you need to start the daemon:
{{{
radvd
}}}
You can listen to its advertisments via the ''radvdump'' program.

== Static tunnel to IPv6 tunnel broker ==
Bert Huijben: I'm busy creating a extensible configuration package for IPv6 support on openwrt. I will add a howto entry for it afterwards.

From [http://www.tldp.org/HOWTO/Linux+IPv6-HOWTO/conf-ipv6-in-ipv4-point-to-point-tunnels.html]
{{{
# ip tunnel add <device> mode sit ttl <ttldefault> remote <ipv4addressofforeigntunnel> local <ipv4addresslocal>
# ip link set dev sit1 up
# ip addr add <local-ipv6endpoint>/64 dev sit1
# ip -6 route add default dev sit1
}}} 


= Example for debugging purposes =
Interface configuration:
{{{
root@openwrt:~# ip addr show
1: lo: <LOOPBACK,UP> mtu 16436 qdisc noqueue
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
    inet6 ::1/128 scope host
2: eth0: <BROADCAST,MULTICAST,PROMISC,UP> mtu 1500 qdisc pfifo_fast qlen 100
    link/ether 00:0c:41:9d:22:33 brd ff:ff:ff:ff:ff:ff
    inet6 fe80::20c:41ff:fe9d:2233/10 scope link
3: eth1: <BROADCAST,MULTICAST> mtu 1500 qdisc noop qlen 100
    link/ether 00:0c:41:9d:22:34 brd ff:ff:ff:ff:ff:ff
4: eth2: <BROADCAST,MULTICAST,UP> mtu 1500 qdisc pfifo_fast qlen 100
    link/ether 00:0c:41:9d:22:35 brd ff:ff:ff:ff:ff:ff
    inet 192.168.1.1/24 brd 192.168.1.255 scope global eth2
    inet6 fe80::20c:41ff:fe9d:2235/10 scope link
5: vlan2: <BROADCAST,MULTICAST,PROMISC,UP> mtu 1500 qdisc noqueue
    link/ether 00:0c:41:9d:22:33 brd ff:ff:ff:ff:ff:ff
    inet 192.168.0.1/24 brd 192.168.0.255 scope global vlan2
    inet6 fe80::20c:41ff:fe9d:2233/10 scope link
    inet6 2002:d536:c887:5678::1/64 scope global
6: vlan1: <BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue
    link/ether 00:0c:41:9d:22:34 brd ff:ff:ff:ff:ff:ff
    inet6 fe80::20c:41ff:fe9d:2234/10 scope link
22: sit0@NONE: <NOARP> mtu 1480 qdisc noqueue
    link/sit 0.0.0.0 brd 0.0.0.0
48: ppp0: <POINTOPOINT,MULTICAST,NOARP,UP> mtu 1492 qdisc pfifo_fast qlen 3
    link/ppp
    inet 213.54.200.135 peer 62.26.136.17/32 scope global ppp0
49: tun6to4@NONE: <NOARP,UP> mtu 1480 qdisc noqueue
    link/sit 213.54.200.135 brd 0.0.0.0
    inet6 ::213.54.200.135/128 scope global
    inet6 2002:d536:c887::1/16 scope global
}}}

Routing table:
{{{
root@openwrt:~# ip route show
62.26.136.17 dev ppp0  proto kernel  scope link  src 213.54.200.135
192.168.1.0/24 dev eth2  proto kernel  scope link  src 192.168.1.1
192.168.0.0/24 dev vlan2  proto kernel  scope link  src 192.168.0.1
default dev ppp0  scope link

root@openwrt:~# ip -6 route show
::/96 via :: dev tun6to4  metric 256  mtu 1480 advmss 1420
2002:d536:c887:5678::/64 dev vlan2  proto kernel  metric 256  mtu 1500 advmss 1440
2002::/16 dev tun6to4  proto kernel  metric 256  mtu 1480 advmss 1420
2000::/3 via ::192.88.99.1 dev tun6to4  metric 1  mtu 1480 advmss 1420
fe80::/10 dev eth0  proto kernel  metric 256  mtu 1500 advmss 1440
fe80::/10 dev eth2  proto kernel  metric 256  mtu 1500 advmss 1440
fe80::/10 dev vlan2  proto kernel  metric 256  mtu 1500 advmss 1440
fe80::/10 dev vlan1  proto kernel  metric 256  mtu 1500 advmss 1440
fe80::/10 dev tun6to4  proto kernel  metric 256  mtu 1480 advmss 1420
ff00::/8 dev eth0  proto kernel  metric 256  mtu 1500 advmss 1440
ff00::/8 dev eth2  proto kernel  metric 256  mtu 1500 advmss 1440
ff00::/8 dev vlan2  proto kernel  metric 256  mtu 1500 advmss 1440
ff00::/8 dev vlan1  proto kernel  metric 256  mtu 1500 advmss 1440
ff00::/8 dev tun6to4  proto kernel  metric 256  mtu 1480 advmss 1420
unreachable default dev lo  metric -1  error -128
}}}

Radvd advertisment:
{{{
root@openwrt:~# radvdump
Router advertisement from fe80::20c:41ff:fe9d:2233 (hoplimit 255)
Received by interface vlan2
        # Note: {Min,Max}RtrAdvInterval cannot be obtained with radvdump
        AdvCurHopLimit: 64
        AdvManagedFlag: off
        AdvOtherConfigFlag: off
        AdvHomeAgentFlag: off
        AdvReachableTime: 0
        AdvRetransTimer: 0
        Prefix 2002:d536:c887:5678::/64
                AdvValidLifetime: 300
                AdvPreferredLifetime: 120
                AdvOnLink: on
                AdvAutonomous: on
                AdvRouterAddr: off
        AdvSourceLLAddress: 00 0C 41 9D 22 33
}}}

Interface configuration of a client machine:
{{{
gjasny@Rincewind:~$ ip addr show
1: lo: <LOOPBACK,UP> mtu 16436 qdisc noqueue
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
2: eth0: <BROADCAST,MULTICAST,UP> mtu 1500 qdisc pfifo_fast qlen 1000
    link/ether 00:0c:6e:44:72:68 brd ff:ff:ff:ff:ff:ff
    inet 192.168.0.6/24 brd 192.168.0.255 scope global eth0
    inet6 2002:d536:c887:5678:20c:6eff:fe44:7268/64 scope global dynamic
       valid_lft 276sec preferred_lft 96sec
    inet6 fe80::20c:6eff:fe44:7268/64 scope link
       valid_lft forever preferred_lft forever
3: sit0: <NOARP> mtu 1480 qdisc noop
    link/sit 0.0.0.0 brd 0.0.0.0
}}}

= Links =
 * [http://www.bieringer.de/linux/IPv6/index.html Peter Bieringer's IPv6 HOWTO]
 * [http://www.join.uni-muenster.de/TestTools/IPv6_Verbindungstests.php JOIN IPv6 Test Page (ping, traceroute, tracepath)]
 * [http://www.litech.org/radvd/ Route Advertising Daemon Homepage]

= ToDo =
 * load modules on every restart
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
