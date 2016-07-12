[[TableOfContents]]

= Preface =
This HOWTO describes how to setup IPv6 on your OpenWrt based router. 

It is based on the OpenWrt [http://openwrt.org/downloads/experimental/ experimental] version. 

There is 2 big different steps :
  1. setup a working ipv6 connection on the OpenWRT router. This can either be:
      * using a tunnel broker (like [http://www.sixxs.net SixXS] or [http://www.tunnelbroker.net hurricane electric]).
      * using 6to4, a standard encapsulation protocol for IPv6 over IPv4
  2. propagate the IPv6 subnet to the LAN with radvd



= Install necessary software =
To use IPv6 we need the following modules:
 * IPv6 kernel module (always)
 * IPv6 routing software (always, to configure IPv6 routing)
 * ip6tables kernel modules (optional, if you need an IPv6 firewall)
 * ip6tables commandline tool (optional, to configure the IPv6 firewall)

== Install the IPv6 kernel modules ==
{{{
ipkg install kmod-ipv6
}}}

== Install the routing software ==
To configure the interfaces and the routing tables we need the new iputils. Additionally we need the route advertising daemon to propagate the IPv6 route to our local subnet.
{{{
ipkg install ip radvd
}}}

== Install the ip6tables kernel modules ==
{{{
ipkg install kmod-ip6tables
}}}

== Install the ip6tables package ==
{{{
ipkg install ip6tables
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

After this your router has IPv6 support. To check this you could use ifconfig to validate the ::1/128 IPv6 address is assigned to the loopback device.
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

You can choose between using 6to4 (standard, works from anywhere) or a SixXS tunnel (if you are near a Point of Presence).
6to4 is probably the quickest to setup at first.

== 6to4 with a direct connection to the Internet ==

This applies e.g. if you WAN port (on vlan1) receives an public IPv4 address through DHCP or is assigned a static public IPv4 address.

To have the 6to4 tunnel start up automatically on boot, copy this script in ''/etc/init.d/S42tun6to4'':

{{{
#!/bin/sh

# 6to4 tunnel

# retrieve the public IPv4 address
ipv4=`ip -4 addr | awk '/^[0-9]+[:] vlan1[:]/ {l=NR+1} /inet (([0-9]{1,3}\.){3}[0-9]{1,3})\// {if (NR == l) split($2,a,"/")} END {print a[1]}'`
# (you may also write e.g. "ipv4=82.54.194.11" if your IP address does not change)

# get the IPv6 prefix from the IPv4 address
ipv6prefix=`echo $ipv4 | awk -F. '{ printf "2002:%02x%02x:%02x%02x", $1, $2, $3, $4 }'`

# the local subnet (any 4 digit hex number)
ipv6subnet=1234


# The 6to4 relay: here are a few, use the anycast address when possible
# For others see http://www.kfu.com/~nsayer/6to4/#list or google

# anycast:
relay6to4=192.88.99.1

# uni-leipzig.de:
#relay6to4=139.18.25.33

# 6to4.ipv6.bt.com
#relay6to4=194.73.82.244

# microsoft
#relay6to4=131.107.33.60

# japan kddilab.6to4.jp
#relay6to4=192.26.91.178


case "$1" in
  start)

    echo "Creating tunnel interface..."
    ip tunnel add tun6to4 mode sit ttl 64 remote any local $ipv4

    echo "Setting tunnel interface up..."
    ip link set dev tun6to4 up

    echo "Assigning ${ipv6prefix}::1/16 address to tunnel interface..."
    ip -6 addr add ${ipv6prefix}::1/16 dev tun6to4

    echo "Adding route to IPv6 internet on tunnel interface via relay..."
    ip -6 route add 2000::/3 via ::${relay6to4} dev tun6to4 metric 1

    # the following lines do not seem to be necessary
    #ip -6 addr add ${ipv6prefix}:${ipv6subnet}::3/64 dev vlan1
    #ip -6 route del ${ipv6prefix}:${ipv6subnet}::/64 dev vlan1

    echo "Assigning ${ipv6prefix}:${ipv6subnet}::1/64 address to br0 (local lan interface)..."
    ip -6 addr add ${ipv6prefix}:${ipv6subnet}::1/64 dev br0

    echo "Done."


    ;;
  stop)

    #echo "Removing WAN (external) interface IPv6 address..."
    #ip -6 addr del ${ipv6prefix}:${ipv6subnet}::3/64 dev vlan1

    echo "Removing br0 (internal lan) interface IPv6 address..."
    ip -6 addr del ${ipv6prefix}:${ipv6subnet}::1/64 dev br0

    echo "Removing routes to 6to4 tunnel interface..."
    ip -6 route flush dev tun6to4

    echo "Setting tunnel interface down..."
    ip link set dev tun6to4 down

    echo "Removing tunnel interface..."
    ip tunnel del tun6to4

    echo "Done."

    ;;
  restart)

    echo "=== 1. Stopping ==="
    /etc/init.d/S42tun6to4 stop
    echo "=== 2. Starting ==="
    /etc/init.d/S42tun6to4 start
    echo "=== 3. Done ==="
    ;;
  *)
    echo "Usage: /etc/init.d/S42tun6to4 {start|stop|restart}"
    ;;

esac
}}}

== 6to4 tunnel with an Internet connection that uses PPP ==
If you connect to your ISP using PPP (usually PPPoE):
When the ppp interface comes up, the ppp daemon calls the ip-up script, when it goes down the ip-down script. To place these scripts in /etc/ppp/ you must create a symbolic link from /tmp/ppp to /etc/ppp:
{{{
mkdir /etc/ppp
ln -s /etc/ppp /tmp/ppp
}}}

The content of the /etc/ppp/ip-up script:
{{{
#!/bin/sh

# set default route
sbin/route add default ppp0

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


== Static tunnel to SixXS.net ==
''Note: this script should works with any Tunnel Broker''
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
ipkg install aiccu
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

Using our mythical `2001:db8:0:f101::/64` network, we would put in /etc/radvd.conf the following lines:
{{{
# For more examples, see the radvd documentation.

interface br0
{
        AdvSendAdvert on;

        prefix 2001:db8:0:f101::/64
        {
                AdvOnLink on;
                AdvAutonomous on;
        };

};
}}}

Now we add `2001:db8:0:f101::1` to br0 & forward our delegated /64 subnet to br0 :
{{{
ip -6 addr add 2001:db8:0:f101::1/64 dev br0
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

= Using IPv6 by default with Windows XP =

Now you have 6to4 installed on your OpenWrt router with a radvd server, you can enable IPv6 on your Windows box by typing
{{{
ipv6 install
}}}
at the command prompt. This will install IPv6 and you will get a 6to4 address. However Windows will only use it to communicate with
other 6to4 addresses or other IPv6 only hosts by default (it will prefer IPv4 otherwise). To force IPv6 with dual stack non-6to4 hosts, use this:
{{{
C:\>netsh
netsh>interface ipv6
netsh interface ipv6>show prefixpolicy
Querying active state...

Precedence  Label  Prefix
----------  -----  --------------------------------
         5      5  3ffe:831f::/32
        10      4  ::ffff:0:0/96
        20      3  ::/96
        30      2  2002::/16
        40      1  ::/0
        50      0  ::1/128

netsh interface ipv6>set prefixpolicy
One or more essential parameters were not entered.
Verify the required parameters, and reenter them.
The syntax supplied for this command is not valid. Check help for the correct syntax.

Usage: set prefixpolicy [prefix=]<IPv6 address>/<integer> [precedence=]<integer>
             [label=]<integer> [[store=]active|persistent]

Parameters:

       Tag              Value
       prefix         - Prefix for which to add a policy.
       precedence     - Precedence value for ordering.
       label          - Label value for matching.
       store          - One of the following values:
                        active: Change only lasts until next boot.
                        persistent: Change is persistent (default).

Remarks: Modifies a source and destination address selection policy
         for a given prefix.

Example:

       set prefixpolicy ::/96 3 4


netsh interface ipv6>set prefixpolicy ::1/128 50 0
Ok.

netsh interface ipv6>set prefixpolicy ::/0 40 1
Ok.

netsh interface ipv6>set prefixpolicy 2002::/16 30 1
Ok.

netsh interface ipv6>set prefixpolicy ::/96 20 3
Ok.

netsh interface ipv6>set prefixpolicy ::ffff:0:0/96 10 4
Ok.

netsh interface ipv6>set prefixpolicy 3ffe:831f::/32 5 5
Ok.

netsh interface ipv6>show prefixpolicy
Querying active state...

Precedence  Label  Prefix
----------  -----  --------------------------------
         5      5  3ffe:831f::/32
        10      4  ::ffff:0:0/96
        20      3  ::/96
        30      1  2002::/16
        40      1  ::/0
        50      0  ::1/128

netsh interface ipv6>exit


C:\>
}}}

Notice how the same label is used for both 6to4 (2002::/16) and normal IPv6 (::/0) telling Windows they can be used together at each end of a communication link. Now if you go to an IPv6 enabled website (e.g. www.kame.net) you will connect to it using IPv6 instead of IPv4.

= Links =
 * [http://www.757.org/~joat/wiki/index.php/IPv6_on_the_WRT54G_via_OpenWRT IPv6 on OpenWrt with Hurricane Electric]
 * [http://www.join.uni-muenster.de/TestTools/IPv6_Verbindungstests.php JOIN IPv6 Test Page (ping, traceroute, tracepath)]
 * [http://www.litech.org/radvd/ Route Advertising Daemon Homepage]
 * [http://www.bieringer.de/linux/IPv6/index.html Peter Bieringer's IPv6 HOWTO]

= ToDo =
 * list of IPv6 ready application available in OpenWrt
 * start/stop radvd when connection goes up/down
 * provide IPv6 support to PPP

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

How would i go about setting up radvd to announce an v6 address (6to4), derived from an DHCP assigned v4 address (it changes every few weeks)?

I found my own answer, this is how you use radvd with an 6to4 address, provided by DHCP

change the prefix in the radvd.conf (first 3 sections) to 0, so 2001:db8:0:f101::/48 becomes 0:0:0:f101::/48, and add "Base6to4Interface ppp0;" (where ppp0 is your wan interface) to the section, and set AdvValidLifetime and AdvPreferredLifetime to a low number, so if the v4 address changes, the v6 routing info will be updated quickly, so the finished section would look something like this:

{{{
        prefix 0:0:0:f101::/48
        {
                AdvOnLink on;
                AdvAutonomous on;
                Base6to4Interface vlan1;

                # Very short lifetimes for dynamic addresses
                AdvValidLifetime 300;
                AdvPreferredLifetime 120;
        };
}}}
That assumes vlan1 is your wan interface, and that you have a /48 address (according to [http://ezine.daemonnews.org/200101/6to4.html] you do get one with 6to4)

hope that helps somebody
