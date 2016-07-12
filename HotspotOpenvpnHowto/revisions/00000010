'''Hotspot with OpenWrt
+
Private VPN access'''

Jan Beba mail@janbeba.de [[BR]]
Bjoern Biesenbach bjoern@bjoern-b.de

20. May 2005

'''PDF-Version: http://bjoern-b.de/files/HotspotOpenvpn.pdf ''' [[BR]]
''' Experimental snapshot 23.4.05 including required packages: http://bjoern-b.de/files/openwrt-wrt54g-jffs2.bin '''

'''Contents'''

    * Intro
    * Network
    * What you need
    * OpenWrt
          o Network devices [[BR]]
          o ipkg setup [[BR]]
          o DHCP-Server [[BR]]
          o OpenVPN [[BR]]
          o Iptables setup [[BR]]

    * Clientside
          o OpenVPN 

= Intro =
Today many people have a broadband Internet connection and surely don't use the whole bandwidth all the time. So why don't give others the opportunity to use your connection? With this document we want to describe how to set up a hotspot using an accesspoint running with OpenWrt. A very important aspect when you decide to open your wireless network for everyone often is, that you still want to use it for your own purpose. This might be accessing a local file- or printserver or anything else not everybody in front of your house should be able to see and to use. Also your own connection should be encrypted. WEP-encryption is not only quite insecure but would also conflict with the idea of an open hotspot. So we decided to create a VPN using OpenVPN.

= Network =
The structure of our network is quite easy. We will use three separated networks; the first will be our own private network, the second the public wireless lan and the last our VPN.

    LAN: 192.168.1.0/24 

    WLAN: 192.168.2.0/24 

    VPN: 192.168.3.0/24 

= What you need =
To use this howto I recommend you to use the newest White Russian RC3. You can build your own firmware or use the generic images in [http://downloads.openwrt.org/whiterussian/rc3/]

To use openvpn you have to install the following packages:

    * openssl 
    * lzo 
    * kmod-tun 
    * openvpn 

I will install them later with ipkg.

= OpenWrt =
Our configuration has been tested with the Linksys WRT54g versions 2.0 and 2.2. If you use other hardware please mind that the interface names may be changed. Assuming your OpenWrt installation is untouched your box is reachable via telnet on 192.168.1.1. The first thing to do is to set a password. Log into your box, type "passwd" and set your new root password. After doing so disconnect and reconnect via ssh.


== Network devices ==
The default config is a little tricky. The LAN-device (vlan0) and the WLAN-device (eth1) are bridged together to "br0". But as we want to have separated nets for those devices, we have to split them. Also the Internet (WAN) device has to be configured.
''Note that the following commands are examples! You have to adapt them to your box. For example on some WRTs you have substitute wifi_ifname with wl0_ifname and so on.'' 



nvram set lan_ifname=vlan0[[BR]]
nvram set lan_proto=static[[BR]]
nvram set lan_ipaddr=192.168.1.1[[BR]]
nvram set lan_netmask=255.255.255.0[[BR]]

nvram set wifi_ifname=eth1[[BR]]
nvram set wifi_proto=static[[BR]]
nvram set wifi_ipaddr=192.168.2.1[[BR]]
nvram set wifi_netmask=255.255.255.0[[BR]]

nvram set wan_ifname=ppp0[[BR]]
nvram set wan_proto=pppoe[[BR]]
nvram set wan_mtu=1492[[BR]]

nvram set pppoe_ifname=vlan1[[BR]]
nvram set pppoe_username=user at provider.name[[BR]]
nvram set pppoe_passwd=yourpassword[[BR]]

nvram set wl0_ssid=Hotspot[[BR]]
nvram commit[[BR]]

reboot

The box will restart and *hopefully* come up again.
If your wlan interface (eth1) is not reachable, make sure it is ''up''.


== DHCP-Server ==
The dnsmasq package in OpenWrt is responsible for the dhcpd functions. As we have a local LAN and a public WLAN we want to serve both with dynamically IP-address allocation. IP-addresses in the range between 192.168.1.200-192.168.1.250 and 192.168.2.200-192.168.2.250 are being offered.

'''/etc/dnsmasq.conf'''[[BR]]
domain-needed[[BR]]
bogus-priv[[BR]]
filterwin2k[[BR]]
local=/lan/[[BR]]
domain=lan[[BR]]

except-interface=vlan1

dhcp-range=vlan0,192.168.1.200,192.168.1.250,255.255.255.0,3h[[BR]]
dhcp-range=eth1,192.168.2.200,192.168.2.250,255.255.255.0,3h[[BR]]

dhcp-leasefile=/tmp/dhcp.leases[[BR]]

dhcp-option=vlan0,3,192.168.1.1[[BR]]
dhcp-option=vlan0,6,192.168.1.1[[BR]]
dhcp-option=eth1,3,192.168.2.1[[BR]]
dhcp-option=eth1,6,192.168.2.1[[BR]]

== OpenVPN ==
First we should install the required software.

    ipkg install openvpn 

Let's create the directory and a private key for our VPN.

    mkdir /etc/openvpn [[BR]]
    openvpn --genkey --secret /etc/openvpn/wlan_home.key 

Load the tunneling module and add it to the autoloader.

    insmod tun 

    echo "tun" » /etc/modules 

'''/etc/openvpn/wlan_home.conf'''[[BR]]
dev tun0[[BR]]
ifconfig 192.168.3.1 192.168.3.2[[BR]]
secret /etc/openvpn/wlan_home.key[[BR]]
port 1194[[BR]]
ping 15[[BR]]
ping-restart 45[[BR]]
ping-timer-rem[[BR]]
persist-key[[BR]]
persist-tun[[BR]]
verb 3[[BR]]

'''/etc/init.d/S60openvpn'''[[BR]]
#!/bin/sh[[BR]]
openvpn --daemon --config /etc/openvpn/wlan_home.conf

Don't forget to assign executable rights to this file.

    chmod a+x /etc/init.d/S60openvpn 

== Iptables setup ==
'''/etc/firewall.user'''[[BR]]

[...][[BR]]
iptables -A FORWARD -i eth1 -o ppp0 -j ACCEPT[[BR]]
iptables -A FORWARD -i tun0 -j ACCEPT[[BR]]
iptables -A FORWARD -i vlan0 -o tun0 -j ACCEPT[[BR]]

This has to be appended! The whole file is much longer.[[BR]]
'''Finally you can do a last reboot.'''

= Clientside =

Now if you want to access the Internet from either your local network or via wifi you just have to select dhcp for your network device. To access your local network from out the wifi, the OpenVPN client has to be installed.
OpenVPN
Install the fitting OpenVPN client for your operating system. Copy the /etc/openvpn/wlan_home.key file from the Wrt to your client. We prefer using scp.

    scp 192.168.1.1:/etc/openvpn/wlan_home.key /etc/openvpn/ 

If you're using M$ Windows copy the file to "C:\Program Files\OpenVPN\config". [[BR]]

Now create the config file.

'''/etc/openvpn/wlan_home.conf[[BR]]''' or 
'''C:\Program Files\OpenVPN\config\wlan_home.conf'''[[BR]]
dev tun[[BR]]
remote 192.168.2.1[[BR]]
ifconfig 192.168.3.2 192.168.3.1[[BR]]
secret wlan_home.key[[BR]]
port 1194[[BR]]
route-gateway 192.168.3.1[[BR]]
route 0.0.0.0 0.0.0.0[[BR]]
redirect-gateway[[BR]]
	
ping 15[[BR]]
ping-restart 45[[BR]]
ping-timer-rem[[BR]]
persist-tun[[BR]]
persist-key[[BR]]

verb 3[[BR]]

Using '''Linux''' you have to load the tunnel module.

    modprobe tun 

Now you can start the tunnel using

    openvpn --daemon --config /etc/openvpn/wlan_home.conf 

For '''Windows''' just right-click onto your config and choose the second point to execute the config.
