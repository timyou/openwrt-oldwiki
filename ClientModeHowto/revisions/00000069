'''Client mode howto'''


[[TableOfContents]]


= Client Mode =

If you want to use OpenWrt to connect to another access point (AP) or
computer rather than to use it as an AP, follow the next steps.

To understand the client mode better, you may be should read the
[http://forum.openwrt.org/viewtopic.php?pid=13151#p13151 Setting up OpenWrt in client mode]
thread in the forum.


== Configuring client mode ==

You need to have a recent version of !OpenWrt White Russian installed.
This howto was written for RC3 and later versions.

The first step would be changing the Wrt's behavior from AP to client
mode (station/client mode or {{{wet}}} for short):

{{{
nvram set wl0_mode=wet
}}}

'''TIP:''' When {{{wet}}} mode is not working for you try {{{sta}}} mode instead.

'''NOTE:''' As soon as your AP is in client mode you _can't_ connect any
wireless clients to it anymore because it's not in AP mode ({{{wl0_mode=ap}}}).


=== Bridged client mode ===

In bridged client mode, all computers connected to the client will be
connected to the subnet of the access point you are connecting to (no
firewalling).

When using the bridged client mode, you should disable the DNS/DHCP server:

{{{
chmod -x /etc/init.d/S50dnsmasq
}}}

When your configuration was set to routed client mode before, you need to add
the wireless interface to the bridge again and remove it from the wan interface.

/!\ '''IMPORTANT:''' Use the correct [:OpenWrtDocs/Configuration#NetworkInterfaceNames:network interface names]
for your hardware version.

{{{
nvram set lan_ifnames="vlan0 eth1"
nvram set wan_ifname=vlan1
}}}


=== Routed client mode ===

Now we are breaking down the default bridge between the wireless interface
and the LAN ports. Note that we are using the {{{wan_ifname}}} to refer to
the wireless connection; this will save you from having to change
the firewall script.

/!\ '''IMPORTANT:''' Use the correct [:OpenWrtDocs/Configuration#NetworkInterfaceNames:network interface names]
for your hardware version.

{{{
nvram set lan_ifname=br0
nvram set lan_ifnames=vlan0
nvram set wan_ifname=eth1
}}}

Then configure the interfaces normally. For example, assuming the wifi
interface uses DHCP and the LAN interface has the static IP address
{{{192.168.2.1}}}:

{{{
nvram set lan_ipaddr=192.168.2.1
nvram set lan_proto=static
nvram set wan_proto=dhcp
}}}

You can configure other options if you need to, like {{{wan_dns}}} or
{{{wan_gateway}}}.

When you are done with setting up the NVRAM, just commit and reboot:

{{{
nvram commit
reboot
}}}


== Finding and joining networks ==

You can now scan for nearby access points. If {{{iwlist}}} doesn't find any
networks on the first run, repeat the scanning a few times.

'''TIP:''' With {{{iwlist}}} you can only scan for networks when your AP
is in client mode.

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

When you set an interface to DHCP, !OpenWrt runs the DHCP client on that
interface automatically at boot time. If you want to re-run the dhcp
client, for example because you joined another network, you can either
reboot, or you can run the {{{ifup}}} command:

{{{
ifup wan; /sbin/wifi
}}}

This will set up the wireless interface according to your nvram settings.


= Links =

 * Detailed information on setting up a wired-wireless bridge with encryption
 [[BR]]- [:WirelessBridgeWithWPAHowto]
 [http://openwrt.ertl-net.net/downloads/test/counter-ClientModeHowto.gif]
