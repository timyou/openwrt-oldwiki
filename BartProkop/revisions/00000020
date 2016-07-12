##master-page:HomepageTemplate
#format wiki
== Bart Prokop ==

Email: [[MailTo(bart AT SPAMFREE tt-soft DOT com)]]
Web: [[(http://bart.prokop.name)]
All coments, amedments, corrections are warmly welcome.

Real world examples.

I created this page to contribute to this project by step by step describing Open WRT instalations running in real word. I created those instalations mostly to implement advanced router features. My intention is to provide step by step log of commands and settings necessary to achieve certain configuration.

== Multi subnet small IT company router ==
=== Router requested features ===
This is the very first advanced configuration with Open WRT I want to describe. The requirements were as follow:
 1. The embeded device shall provide Internet access to all conected computers with different policy for some groups of users.
 2. The embeded device will replace the existing routing capabilities of Linux server. I do not want to route via Linux server anymore as it has many many other things to do and is under haavy reconfiguration process.
 3. List of features on embeded devices:
  * service MORE than one separate LAN conected to embeded device
  * slave DNS server (to existing Linux server)
  * PPTP server (take this feature from Linux server)
  * QoS
 4.

==== Network topology ====
The ISP provides a DLS connection terminated by SpeedStream modem. We are provided with 5 usable IP addresses (Mask of 255.255.255.248):
 * 80.55.248.80 - net address
 * 80.55.248.81 - ADSL modem IP address
 * 80.55.248.82 - free
 * 80.55.248.83 - free (we will install our OpenWRT router here)
 * 80.55.248.84 - free
 * 80.55.248.85 - Linux company server
 * 80.55.248.86 - free
 * 80.55.248.87 - broadcast address

We need a dew private subnets with different routing and QoS features:
 * 10.112.170.x / 24 as a primary LAN network for main office.
 * 10.216.208.x / 24 as a VPN acccesible via PPTP protocol.
 * 10.98.226.x  / 24 as a WiFi subnet primary for mobile laptops/guests
 * 10.90.201.x  / 24 as a separate from above LAN subnet for purpose of wiring hotel placed above main office.
 
=== Implementation ===
==== Hardware and firmware upgrade ====
I decided to purchase Linksys WRT54GL v 1.1 model. Its serial number is CL7B1FB39805. The first step was replace vendor firmware with OpenWRT. It is very trivial task. You had to download a firmware from [[http://downloads.openwrt.org/whiterussian/newest/default/]]. In my case it was file named openwrt-wrt54g-squashfs.bin. Before flashing your device I strongly recommend to compare MD5SUMs of downloaded file to those avaiable at download pages. I used vendor firmware for upgrading the firmware. After flashing, the device will boot. Please then use telnet (not ssh as it will not work) to log into your embeded device and set root password. Setting root password allows you to log in via SSH. The command to issue are:

{{{
telnet 192.168.1.1 (from your PC of course, log in as root with empty password)
passwd (after it you type and re-type your root password)
reboot (to restart device)
}}}

At this point you should be able to ssh to your router and be able to enjoy embeded linux. I also decided to clean NVRAM, as my device could have strange settings from previous firmware. To do so just type ('''please double check if it is SAFE with your hardware!!!'''):
{{{
mtd -r erase nvram
}}}
In my case it reduced variable count to 30% of this what I had originally set with vendor firmware. After ersing nvram, I strongly recommend to set up a boot_wait to on. It will really help if I cause the router to stop working by misconfiguring it.
{{{
nvram set boot_wait=on
nvram commit
}}}
==== Basic network settings ====
I changed SSID to reflect company domain:
{{{
nvram set wl0_ssid="www.tt-soft.com"
nvram commit
}}}
We need to configure our WAN port to 80.55.248.83. As we know our static IP, configuration is very simple:
{{{
nvram set wan_proto=static
nvram set wan_ipaddr=80.55.248.83
nvram set wan_netmask=255.255.255.248
nvram set wan_gateway=80.55.248.81
nvram set wan_dns=80.55.248.85
nvram commit
}}}
Now lets enable SSH on WAN port. It is disabled by default and we need it open as we want external access to our device. It is very easy. Just edit a file /etc/firewall.user, locate lines which looks like those below and uncomment last two lines:
{{{
### Open port to WAN
## -- This allows port 22 to be answered by (dropbear on) the router
# iptables -t nat -A prerouting_wan -p tcp --dport 22 -j ACCEPT
# iptables        -A input_wan      -p tcp --dport 22 -j ACCEPT
}}}

The router was now mounted and cabled in its working enviroment.

After successfull remote login, I decided to separate WiFi from LAN ports of the router. Let;s call it unbridge:
{{{
nvram set lan_ifname=vlan0    (no more bridge)
nvram set lan_ifnames=vlan0   (no more bridge)
nvram set lan_ipaddr=10.112.170.3  (set lan IP to what we want)
nvram set wifi_ifname=eth1    (configure WiFi as separate subnet)
nvram set wifi_proto=static
nvram set wifi_ipaddr=10.98.226.1
nvram set wifi_netmask=255.255.255.0
nvram commit  (save changes to NVRAM)
reboot
}}}

==== Static IP addresses with DHCP ====
First I decided that some well know machines will have certain fixed IP's. The assigment in vlan0 will be done based on MAC matching. So I edited /etc/ethers file:
{{{
root@OpenWrt:~# cat /etc/ethers
00:11:0a:b9:19:93 10.112.170.2
00:0F:FE:90:A7:18 10.112.170.41
00:15:B7:FE:74:58 10.112.170.42
00:90:F5:3C:70:E8 10.112.170.43
00:c0:a8:f5:0a:07 10.112.170.44
00:50:8d:4d:95:09 10.112.170.45
00:30:05:ba:04:a7 10.112.170.46
00:04:61:73:60:49 10.112.170.47
00:15:f2:91:c9:a7 10.112.170.48
}}}

==== Adding new subned on VLAN ====
I decided to separate port number 4 to became a port for a separate subnet for guests in hotel that is located in the same building. First it was necessary to set NVRAM. Please note that in my confguration port labeled 4 has internal switch number 0. (This is specific for Linksys GL v.2 !!!)
{{{
root@OpenWrt:~# nvram set vlan0ports="3 2 1 5*"
root@OpenWrt:~# nvram set vlan2ports="0 5"
root@OpenWrt:~# nvram set vlan2hwname=et0
root@OpenWrt:~# nvram commit
}}}

Please note that this causes only the ports on switch to became partitioned. To make an runnig interface you should do:
{{{
root@OpenWrt:/etc/init.d# nvram set hotel_ifname=vlan2
root@OpenWrt:/etc/init.d# nvram set hotel_proto=static
root@OpenWrt:/etc/init.d# nvram set hotel_ipaddr=10.90.201.1
root@OpenWrt:/etc/init.d# nvram set hotel_netmask=255.255.255.0
root@OpenWrt:~# nvram commit
root@OpenWrt:/etc/init.d# ifup hotel
}}}

To pemanently set vlan2 aka hotel up, you need to place hotel interface in NVRAM variable:
{{{
root@OpenWrt:~# nvram set ifup_interfaces="lan wan wifi hotel"
root@OpenWrt:~# nvram commit
}}}

==== Tuning up DNSMASQ ====
First it was ncessary to force OpenWRT to use /etc/dnsmasq.conf for configuration. To do this, I just added those two lines at the beginning of /etc/init.d/S60dnsmasq.
{{{
dnsmasq
exit
}}}

So the file looks now like:

{{{
#!/bin/sh

# The following is to automatically configure the DHCP settings
# based on nvram settings. Feel free to replace all this crap
# with a simple "dnsmasq" and manage everything via the
# /etc/dnsmasq.conf config file
dnsmasq
exit
# DHCP interface (lan, wan, wifi -- any ifup *)
iface=lan
ifname=$(nvram get ${iface}_ifname)
 ... continue ...
}}}

...

----
CategoryHomepage
