Client Mode Howto


= Client Mode =

If you want to use OpenWrt to connect to another access point (AP) or
Computer rather than to use it as an AP, follow these steps:


== Setting up/configuring client mode ==

You need to have a recent version of OpenWrt 'White Russian' installed.
This Howto was written for RC3.

The first step would be changing the WRT's behavior from AP to client
mode ("wet" for short):

{{{
nvram set wl0_mode=wet
}}}

or if you've problems with wet mode, try:

{{{
nvram set wl0_mode=sta
}}}


=== Bridged client mode ===

In bridged client mode, all computers connected to the client will be 
connected to the subnet of the access point you're connecting to (no
firewalling).

When using the bridged client mode, you should disable the DNS/DHCP server:

{{{
chmod -x /etc/init.d/S50dnsmasq
}}}


=== Routed client mode ===

Now we're breaking down the default bridge between the wifi interface
and the LAN ports. Note that we're using the wan_ifname to refer to
the wireless connection; this will save you from having to change
the firewall script:

{{{
nvram set lan_ifname=br0
nvram set lan_ifnames=vlan0
nvram set wan_ifname=eth1
}}}

Then configure the interfaces normally. For example, assuming the wifi
interface uses DHCP and the LAN interface has the static IP address
192.168.2.1:

{{{
nvram set lan_ipaddr=192.168.2.1
nvram set lan_proto=static
nvram set wan_proto=dhcp
}}}

You can configure other options if you need to, like wan_dns or
wan_gateway. 

When you're done with setting up the NVRAM, just commit and reboot:

{{{
nvram commit
reboot
}}}


== Finding and joining Networks ==

You can now scan for nearby access points. If iwlist doesn't find any
networks on the first run, repeat the scanning a few times.

{{{
root@OpenWrt:/# iwlist eth1 scanning
eth1      Scan completed :
          Cell 01 - Address: aa:bb:cc:dd:ee:ff
                    ESSID:"OpenWrt"
                    Channel:1
                    Quality:0/0  Signal level:-17 dBm  Noise level:-92 dBm
                    Bit Rate:1 Mb/s
                    Bit Rate:2 Mb/s
                    Bit Rate:5.5 Mb/s
                    Bit Rate:11 Mb/s
                    Bit Rate:18 Mb/s
                    Bit Rate:24 Mb/s
                    Bit Rate:36 Mb/s
                    Bit Rate:54 Mb/s
                    Bit Rate:6 Mb/s
                    Bit Rate:9 Mb/s
                    Bit Rate:12 Mb/s
                    Bit Rate:48 Mb/s

root@OpenWrt:/# 
}}}

To join a non-encrypted access point run these commands:

{{{
ifdown wan
nvram set wl0_ssid=<SSID>
nvram set wl0_channel=<CHANNEL_NUMBER>
ifup wan; /sbin/wifi
}}}

You can configure encryption like WEP or WPA the way you would
if the device was in access point mode. For example:

{{{
ifdown wan
nvram set wl0_ssid=<SSID>
nvram set wl0_channel=<CHANNEL_NUMBER>
nvram set wl0_wep=enabled
nvram set wl0_key=1
nvram set wl0_key1=<WEP key in hex format>
ifup wan; /sbin/wifi
}}}

Don't forget to commit if you want your settings to survive a reboot:

{{{
nvram commit
}}}


== Some more configuration ==

When you set an interface to DHCP, OpenWrt runs the DHCP client on that
interface automatically at boot time. If you want to re-run the dhcp
client, for example because you joined another network, you can either 
reboot, or you can run the ifup command:

{{{
ifup wan; /sbin/wifi
}}}

This will set up the Wireless interface according to your nvram settings.
