#acl Known:read,write All:read
##
## Note: these pages document the firmware itself, not packages
##       questions/comments should be posted to the forum
##
## THIS PAGE DOCUMENTS THE FIRMWARE, NOT PACKAGES
## DO NOT ADD PACKAGE DOCUMENTATION/CONFIGURATION TO THIS PAGE
##
[:OpenWrtDocs]
[[TableOfContents]]

= NVRAM =
NVRAM stands for Non-Volatile RAM, in this case the last 64K of the flash chip used to store various configuration information in a ''name=value'' format.

{{{#!CSV
Command; Description
nvram show | sort | less; Display everything in nvram
nvram get boot_wait; Get a specific variable
nvram set boot_wait=on; Set a value
nvram set lan_ifnames="vlan0 vlan1 vlan2"; set multiple values to one param
nvram unset foo; Delete a variable
nvram commit; Write changes to the flash chip (otherwise only stored in RAM)
}}}

A complete list of nvram options can be found at [:OpenWrtNVRAM].

= Network configuration =

'''Quick overview of the router architecture:'''

The WRT54G is made up of an Ethernet switch, a wireless access point and a router chip that connects them together.

[http://upload.wikimedia.org/wikipedia/commons/0/0f/WRT54G_internal_architecture.png]

[[BR]][[Anchor(NetworkInterfaceNames)]]
The names of the network interfaces will depend largely on what hardware OpenWrt is run on.
||'''Manufacturer'''||'''Model'''||'''Hardware version'''||'''LAN'''||'''WAN'''||'''WIFI'''||'''Comments'''||
||Linksys||WRT54G||v1.x||vlan2||vlan1||eth2|| ||
||Linksys||WRT54G||v2.x/v3.0||vlan0||vlan1||eth1|| ||
||Linksys||WRT54GS||v1.x/v2.0/v3||vlan0||vlan1||eth1|| ||
||Asus||WL-300g|| ||eth0||None||eth2|| ||
||Asus||WL-500g|| ||eth0||eth1||eth2|| ||
||Asus||WL-500g Deluxe|| ||vlan0||vlan1||eth1||eth0 is the whole switch, with lan and wan ports||
||Buffalo||WBR-G54|| ||eth0||eth1||eth2|| ||
||Buffalo||WBR2-G54S|| ||vlan0||vlan1||eth1||eth0 is the whole switch, with lan and wan ports||
||Buffalo||WLA-G54|| ||eth0||N/A||eth2||No WAN port on this device||
||Motorola||WR850G||v3||vlan0||vlan1||eth1||eth0 is the whole switch, with lan and wan ports||
||Microsoft||MN700||v.x||eth0||eth1||eth2|| ||
||Siemens||SE505||v1||eth0||eth1||eth2|| ||
||Siemens||SE505||v2||vlan0||vlan1||eth1||eth0 is the whole switch, with lan and wan ports||
Please update to include other models.

NOTE: LAN and WIFI are bridged together in br0 by default, on some devices WAN can be eth1 and LAN eth0.

In general, the switch works the following way: It recieves data (physical) on either
lan port or on the wan port. Then the switch tags the packages (with VLAN), so Linux
is able to see the difference and that way we have the vlan devices, which describe wan
or lan port.

[[BR]]
The basic (802.3) network configuration is handled by a series of NVRAM variables:
{{{#!CSV
NVRAM; Description
<name>_ifname; The name of the linux interface the settings apply to
<name>_ifnames; Devices to be added to the bridge (only if the above is a bridge)
<name>_proto; The protocol which will be used to configure an IP
            ; static: Manual configuration (see below)
            ; dhcp: Perform a DHCP request
            ; pppoe: Create a ppp tunnel (requires pppoecd package)
<name>_ipaddr; ip address (x.x.x.x)
<name>_netmask; netmask (x.x.x.x)
<name>_gateway; Default Gateway (x.x.x.x)
<name>_dns; DNS server (x.x.x.x)
}}}
The command ''ifup <name>'' will configure the interface defined by <name>_ifname according to the above variables. As an example, the /etc/init.d/S40network script will automatically run the following commands at boot:
{{{
ifup lan
ifup wan
ifup wifi
}}}
The ''ifup lan'' command will bring up the interface specified by lan_ifname. Normally the lan_ifname is set to br0 which will cause it to create the bridge br0 and add the the interfaces from lan_ifnames to the bridge; lan_proto is usually static which means that br0 will have the ip address from lan_ipaddr, and so on for the rest of the variables listed above.

It's important to remember that it's the <name>_ifname that specifies the interfaces, the <name> compontent itself has almost no value. This means that if you changed lan_ifname to be the internet port, vlan1, then ''ifup lan'' would bring up the internet port, not the lan ports (despite using the command ''ifup lan'' and using the lan_ variables). Also, it means that you can create any <name> variables you want, foo_ifname, foo_proto .... and they would be used by ''ifup foo''.

The only <name> with any significance is '''wan''', used by the /etc/S45firewall script. The firewall script will NAT traffic through the wan_ifname, blocking connections to wan_ifname.

Further information about the variables used can be found at [:OpenWrtNVRAM]

Don't forget to check the [:OpenWrtFaq] for information about howto setup PPPOE etc.

== Sample network configurations ==

For client mode configuration (rather than AP mode), see this page: [:ClientModeHowto]

(note these examples use wrt54g v2.x/wrt54gs v1.x interface names)

The default network configuration:
(lan+wireless bridged as 192.168.1.1/24, wan as dhcp)
{{{
lan_ifname=br0
lan_ifnames="vlan0 eth1"
lan_proto=static
lan_ipaddr=192.168.1.1
lan_netmask=255.255.255.0

wan_ifname=vlan1
wan_proto=dhcp
}}}


If you just want to use OpenWrt as an access point you can avoid the WAN interface completely:
(lan+wireless bridged as 192.168.1.25/24, routed through 192.168.1.1, wan ignored)
{{{
lan_ifname=br0
lan_ifnames="vlan0 eth1"
lan_proto=static
lan_ipaddr=192.168.1.25
lan_netmask=255.255.255.0
lan_gateway=192.168.1.1
lan_dns=192.168.1.1

wan_proto=none
}}}

You can also have the lan interface fetch its configuration via dhcp, but to do so, you'll have to comment out the line:
{{{
# linksys bug; remove when not using static configuration for lan
nvram set lan_proto="static"
}}}
in /etc/init.d/S05nvram (The usual story about replacing the symlink with a copy of the file before editting applies).
After doing this, you need to set the appropriate nvram variable:
{{{
lan_proto=dhcp
}}}

To separate the LAN from the WIFI:
(lan as 192.168.1.25/24, wireless as 192.168.2.25/24, wan as dhcp, remove your wifi interface (eth1 on v2/3 linksys routers) from the lan_ifnames variable)
{{{
lan_ifname=vlan0
lan_proto=static
lan_ipaddr=192.168.1.25
lan_netmask=255.255.255.0

wifi_ifname=eth1
wifi_proto=static
wifi_ipaddr=192.168.2.25
wifi_netmask=255.255.255.0

wan_ifname=vlan1
wan_proto=dhcp

lan_ifnames=vlan0 eth2 eth3
}}}

== The ethernet switch ==

The WRT54G is essentially a WAP54G (wireless access point) with a 6 port switch. There's only one physical ethernet connection and that's wired internally into port 5 of the switch; the WAN is port 0 and the LAN is ports 1-4. The separation of the WAN and LAN interfaces is done by the switch itself. The switch has a vlan map which tells it which vlans can be accessed through which ports.

The vlan configuration is based on two variables (per vlan) in nvram.

{{{
vlan0ports="1 2 3 4 5*" (use ports 1-4 on the back, 5 is the wrt54g itself)
vlan0hwname=et0
}}}

=== Normal Behavior ===

This is only the case if the nvram variable boardflags is set. On the WRT54G V1.1 and earlier, it's not set.

When the et module (ethernet driver) loads it will read from vlan0ports to vlan15ports, behind the scenes the ethernet driver is using these variables to generate a more complex configuration which will be sent to the switch. When packets are recieved from external devices they need to be assigned a vlan id, and when packets are sent to those external devices the vlan tags need to be removed.

PVID represents the primary vlan id, in other words if a packet doesn't have a vlan tag, which vlan does it belong to? The ethernet driver handles this rather trivially, in the case of vlan0ports="1 2 3 4 5*", ports 1-4 are set to PVID 0 (vlan0). Since the wrt needs to recieve packets from both the LAN (vlan0) and the WAN (vlan1), port 5 is a special case appearing in both vlan0ports and vlan1ports. This is where the '*' is used -- it determines the PVID of port 5, which is also the only port not to untag packets (for hopefully obvious reasons).

The second variable, vlan0hwname is used by the network configuration program (or script in the case of openwrt) to determine the parent interface. This should be set to "et0" meaning the interface matching et0macaddr.

'''Sample configurations'''
(unless otherwise specified, vlan variables not shown are assumed to be unset)

Default:
{{{
vlan0ports="1 2 3 4 5*"
vlan0hwname=et0
vlan1ports="0 5"
vlan1hwname=et0
}}}

All ports lan (vlan0):
{{{
vlan0ports="0 1 2 3 4 5*"
vlan0hwname=et0
}}}

LAN (vlan0), WAN (vlan1), DMZ (vlan2):
{{{
vlan0ports="1 2 5*"
vlan0hwname=et0
vlan1ports="0 5"
vlan1hwname=et0
vlan2ports="3 4 5"
vlan2hwname=et0
}}}

It's a good idea when choosing a vlan layout to keep port 1 in vlan0. At least the WRT54GS v1.0 will not accept new firmware via tftp if port 1 is in another vlan.

=== Using Robocfg ===

Robocfg is a utility written by Oleg Vdovikin to enable the hardware configuration of the Broadcom BCM5325E/536x VLAN enabled 6-port ethernet switch.  When used properly, it can configure the switch in such a way that enables each of the five exposed ports of the switch to be treated as a separate, individual ethernet interface.  Using robocfg, the switch can also be configured to tag packets for use in VLAN enabled networks, and to configure each port's MDI, duplex, and speed settings.  Robocfg options can be issued individually, or strung together on one line, each new option and parameter separated by a space.  See the bottom of this section for a copy of Robocfg's own stated parameters.

'''Sample Command Uses'''

Show current switch configuration:
{{{
robocfg show
}}}

Enable or disable a port(note: tx/rx_disabled can be useful for traffic monitoring):
{{{
robocfg port X state <enabled|disabled|rx_disabled|tx_disabled>
}}}

Set port speed and duplex:
{{{
robocfg port X media <auto|10HD|10FD|100HD|100FD>
}}}

Set port crossover state:
{{{
robocfg port X mdi-x <auto|on|off>
}}}

'''Advanced Configuration'''

When changing port assignments for VLANs, the switch should be disabled before changing the settings, and then re-enabled after the settings have been entered.  Of course, the configuration should also be done using a serial console or executed as a script, since reconfiguration of the switch will disconnect any current telnet or ssh session.  Port numbers followed by a "t" will pass tagged packets(necessary for port 5), while port numbers with a "u", or no "t", will untag packets when passing them through the interface.  The following example(which configures each physical port with it's own VLAN) has been stretched out to better show each action:
{{{
robocfg switch disable
robocfg vlans enable reset
robocfg vlan 0 ports "0 5t"
robocfg vlan 1 ports "1 5t"
robocfg vlan 2 ports "2 5t"
robocfg vlan 3 ports "3 5t"
robocfg vlan 4 ports "4 5t"
robocfg switch enable
}}}

Now that the switch has been configured to tag the appropriate packets, the VLANs can be created using the vconfig command:
{{{
vconfig add eth0 0
vconfig add eth0 1
vconfig add eth0 2
vconfig add eth0 3
vconfig add eth0 4
}}}

Now VLANs 0-4 have been created, and these can be seen with the "ifconfig -a" command.  Each VLAN now needs to be assigned a unique hardware MAC address:
{{{
ifconfig vlan0 hw ether XX:XX:XX:XX:XX:00
ifconfig vlan1 hw ether XX:XX:XX:XX:XX:01
ifconfig vlan2 hw ether XX:XX:XX:XX:XX:02
ifconfig vlan3 hw ether XX:XX:XX:XX:XX:03
ifconfig vlan4 hw ether XX:XX:XX:XX:XX:04
}}}

An IP address can be assigned to each VLAN interface now, if desired:
{{{
ifconfig vlanX xx.xx.xx.xx netmask xx.xx.xx.xx
}}}

Finally, each interface can be brought up:
{{{
ifconfig vlanX up
}}}

Alternately, all ports can be placed on vlan0:
{{{
robocfg switch disable
robocfg vlans enable reset
robocfg vlan 0 ports "0 1 2 3 4 5t"
robocfg switch enable
vconfig eth0 0
ifconfig vlan0 xx.xx.xx.xx netmask xx.xx.xx.xx
ifconfig vlan0 up
}}}

'''Original Robocfg Parameter List'''
{{{
Usage: robocfg <op> ... <op>
Operations are as below:
        show
        switch <enable|disable>
        port <port_number> [state <enabled|rx_disabled|tx_disabled|disabled>]
                [stp none|disable|block|listen|learn|forward] [tag <vlan_tag>]
                [media auto|10HD|10FD|100HD|100FD] [mdi-x auto|on|off]
        vlan <vlan_number> [ports <ports_list>]
        vlans <enable|disable|reset>

        ports_list should be one argument, space separated, quoted if needed,
        port number could be followed by 't' to leave packet vlan tagged (CPU
        port default) or by 'u' to untag packet (other ports default) before
        bringing it to the port, '*' is ignored

Samples:
1) ASUS WL-500g Deluxe stock config (eth0 is WAN, eth0.1 is LAN):
robocfg switch disable vlans enable reset vlan 0 ports "0 5u" vlan 1 ports "1 2
3 4 5t" port 0 state enabled stp none switch enable
2) WRT54g, WL-500g Deluxe OpenWRT config (vlan0 is LAN, vlan1 is WAN):
robocfg switch disable vlans enable reset vlan 0 ports "1 2 3 4 5t" vlan 1 ports
 "0 5t" port 0 state enabled stp none switch enable
}}}

= Wireless configuration =

== Basic settings ==

|| '''NVRAM variable''' || '''Description''' ||
|| wl0_mode  || '''ap''' = Access Point (master mode), '''sta''' Client mode ||
|| wl0_ssid  || ESSID ||
|| wl0_infra || '''0''' = Ad Hoc mode, '''1''' = normal AP/Client mode ||
|| wl0_closed || '''0''' = Broadcast ESSID, '''1''' Hide ESSID ||
|| wl0_channel || 1 / 2 / 3 /.../ 11 vhannel ||

See ["OpenWrtNVRAM"] for more NVRAM settings.

== WEP encryption ==

|| '''NVRAM variable''' || '''Description''' ||
|| wl0_wep || '''disabled''' = disabled WEP, '''enabled''' = enable WEP ||
|| wl0_key || '''1''' .. '''4''' = Select WEP key to use ||
|| wl0_key[1..4] || WEP key in hexadecimal format (allowed hex chars are 0-9a-f) ||

Avoid using WEP keys with 00 at the end, otherwise the driver won't be able to detect the key length correctly.

A 128-Bit WEP key must be 26 hex digits long.

Setting up WPA will override any WEP settings.

== WPA encryption ==

For enabling WPA, you need to install the nas package.
When you enable or disable WPA settings, you should make sure that the NVRAM variable '''wl0_auth_mode''' is unset, because it is obsolete.

More information is on ["OpenWrtDocs/nas"]. (solve problem with WhiteRussian RC2 and client mode)

|| '''NVRAM variable''' || '''Description''' ||
||<rowspan=6> wl0_akm || '''open''' = No WPA ||
||  '''psk''' = WPA Personal/PSK (Preshared Key) ||
||  '''wpa''' WPA with a RADIUS server ||
||  '''psk2''' = WPA2 PSK ||
||  '''wpa2''' WPA2 with RADIUS ||
||  '''"psk psk2"''' or '''"wpa wpa2"''' = support both WPA and WPA2 ||
||<rowspan=3> wl0_crypto || '''tkip''' = RC4 encryption ||
||  '''aes''' = AES encryption ||
||  '''aes+tkip''' = support both ||
|| wl0_wpa_psk || Password to use with WPA/WPA2 PSK (at least 8, up to 63 chars) ||
|| wl0_radius_key || Shared Secret for connection to the Radius server ||
|| wl0_radius_ipaddr || IP to connect... ||
|| wl0_radius_port || Port# to connect... ||

== Wireless Distribution System (WDS) / Repeater / Bridge ==

OpenWrt supports the WDS protocol, which allows a point to point link to be established between two access points. By default, WDS links are added to the br0 bridge, treating them as part of the lan/wifi segment; clients will be able to seamlessly connect through either access point using wireless or the wired lan ports as if they were directly connected.

Configuration of WDS is simple, and depends on one of two variables

{{{#!CSV
NVRAM; Description
wl0_lazywds; Accept WDS connections from anyone (0:disabled 1:enabled)
wl0_wds; List of WDS peer mac addresses (xx:xx:xx:xx:xx:xx, space separated)
}}}

For security reasons, it's recommended that you leave wl0_lazywds off and use wl0_wds to control WDS access to your AP.
wl0_wds functions as an access list of peers to accept connections from and peers to try to connect to; the peers will either need the mac address of your AP in their wl0_wds list, or wl0_lazywds enabled.

Easy steps for a successfull WDS:

First do it without wireless protection and then activate the protection.
If you activate both you will double the pain to find a problem.

 1. Configure the IPs of each AP - don't use the same! For easier maintenance you can use the same subnet.
 1. Add the '''other''' APs MAC address to the list of allowed peers to each AP. With OpenWRT it's the variable wl0_wds.
 1. Disable all the unneeded services like DHCP, port forwarding, firewalling etc. '''except''' on the AP the has the internet connection. Remember: The other APs only act as the extended arm of the internet connected AP.
 1. Configure the WLAN parameters on all APs identical. That is SSID, channel, etc. - keep it simple. If you want to try boosters etc. do this later.
 1. Have you commited your values? Do it. And reboot.
 1. Now connect a lan cable to each AP and try to ping the internet AP. It should answer. Else start checking the settings.
 1. You are done. Now activate security on the devices. Optionally hide the SSID (wl0_closed=1). If WPA-PSK doesn't work chances are that a peer partner doesn't support it. Try WEP.

/!\ Note: if you broke up your bridge as detailed in
"To separate the LAN from the WIFI" above, this will not just work, since you no longer have a br0 device. You will have to add a bridge to one of your devices again, and create appropriate firewall rules, to make things work. There are currently no detailed instructions on how to set this up, so you better no what you are doing...

== OpenWrt as client / wireless bridge ==

Starting with RC2 WhiteRussian basically the only thing you have to do is to switch the WL mode like with the bridge:

{{{
nvram set wl0_mode=sta
}}}

For more information, see ["ClientModeHowto"]

= Software configuration =

== System ==

=== dnsmasq ===

Dnsmasq is lightweight, easy to configure DNS forwarder and DHCP server.

Documentation can be found at ["OpenWrtDocs/dnsmasq"]

=== nas ===

'''nas''' is the binary, Broadcom proprietary, tool that sets up security connection on wireless device.

Documentation with discovered feature can be found at ["OpenWrtDocs/nas"] .

=== wl ===

'''wl''' is a proprietary Linksys binary tool for setting the parameters of the wireless interface.

Documentation with discovered feature can be found at ["OpenWrtDocs/wl"] .

=== TimeZone and NTP ===

To set a Time Zone type something like the following line in /etc/profile:
{{{
export TZ="CET-1CETDST"
}}}
''note: This sets TimeZome to GMT+1''

If you want to use a TimeClient to Syncronize, use rdate
for that (Note: rdate uses port 37/tcp on remote host). Create a file in /etc/init.d/ called S51rdate, with the contents:

{{{
#!/bin/sh
/usr/sbin/rdate 128.138.140.44
}}}

save it, and then type this at a prompt to make it executable:

{{{
chmod a+x /etc/init.d/S51rdate
}}}

Putting a TimeZone entry for the Systemlogger could also be an good idea
simply put a line like something in /etc/TZ:

{{{
CET-1CEST-2,M3.5.0/02:00:00,M10.5.0/03:00:00
}}}
''note: this sets TimeZone for CET/CEST (Central European Time UTC+1 / Central European Summer Time UTC+2) and the starting (5th week of March at 02:00) and endtime (5th week of October at 03:00) of DST (Daylight Saving Time).''

More can be found here: http://leaf.sourceforge.net/doc/guide/buci-tz.html#id2594640
and: http://openwrt.org/forum/viewtopic.php?id=131

Examples:
||<rowspan=6>Australia||Melbourne,Canberra,Sydney||EST-10EDT-11,M10.5.0/02:00:00,M3.5.0/03:00:00||
||Perth||WST-8||
||Brisbane||EST-10||
||Adelaide||CST-9:30CDT-10:30,M10.5.0/02:00:00,M3.5.0/03:00:00||
||Darwin||CST-9:30||
||Hobart||EST-10EDT-11,M10.1.0/02:00:00,M3.5.0/03:00:00||
||<rowspan=18>Europe||Amsterdam, Netherlands||CET-1CEST-2,M3.5.0/02:00:00,M10.5.0/03:00:00||
||Athens, Greece||EET-2EEST-3,M3.5.0/03:00:00,M10.5.0/04:00:00||
||Barcelona, Spain||CET-1CEST-2,M3.5.0/02:00:00,M10.5.0/03:00:00||
||Berlin, Germany||CET-1CEST-2,M3.5.0/02:00:00,M10.5.0/03:00:00||
||Brussels, Belgium||CET-1CEST-2,M3.5.0/02:00:00,M10.5.0/03:00:00||
||Budapest, Hungary||CET-1CEST-2,M3.5.0/02:00:00,M10.5.0/03:00:00||
||Copenhagen, Denmark||CET-1CEST-2,M3.5.0/02:00:00,M10.5.0/03:00:00||
||Dublin, Ireland||GMT+0IST-1,M3.5.0/01:00:00,M10.5.0/02:00:00||
||Geneva, Switzerland||CET-1CEST-2,M3.5.0/02:00:00,M10.5.0/03:00:00||
||Helsinki, Finland||EET-2EEST-3,M3.5.0/03:00:00,M10.5.0/04:00:00||
||Lisbon, Portugal||WET-0WEST-1,M3.5.0/01:00:00,M10.5.0/02:00:00||
||London, Great Britain||GMT+0BST-1,M3.5.0/01:00:00,M10.5.0/02:00:00||
||Madrid, Spain||CET-1CEST-2,M3.5.0/02:00:00,M10.5.0/03:00:00||
||Oslo, Norway||CET-1CEST-2,M3.5.0/02:00:00,M10.5.0/03:00:00||
||Paris, France||CET-1CEST-2,M3.5.0/02:00:00,M10.5.0/03:00:00||
||Prague, Czech Republic||CET-1CEST-2,M3.5.0/02:00:00,M10.5.0/03:00:00||
||Roma, Italy||CET-1CEST-2,M3.5.0/02:00:00,M10.5.0/03:00:00||
||Stockholm, Sweden||CET-1CEST-2,M3.5.0/02:00:00,M10.5.0/03:00:00||
||New Zealand||Auckland,Wellington||NZST-12NZDT-13,M10.1.0/02:00:00,M3.3.0/03:00:00||
||<rowspan=7>USA & Canada||Hawaii Time||HAW10||
||Alaska Time||AKST9AKDT||
||Pacific Time||PST8PDT||
||Mountain Time||MST7MDT||
||Central Time||CST6CDT||
||Eastern Time||EST5EDT||
||Atlantic Time||AST4ADT||
Please update and include your Time Zone.[[BR]]
You can find more on timezones on [http://www.timeanddate.com/worldclock/ timeanddate.com].

=== Crontab ===
HowtoEnableCron


=== PPPoE Internet Connection ===
Be sure you have the pppoe modules/packages installed!

Set the nvram according to
{{{
nvram set wan_ifname=ppp0
nvram set wan_proto=pppoe
nvram set ppp_mtu=1492 # The MTU of your ISP
nvram set pppoe_ifname=vlan1 # For WRT54GS only. This should be your wan port.
nvram set ppp_username=your_isp_login
nvram set ppp_passwd=your_isp_password
nvram commit
}}}
and reboot.

Use ifconfig (device ppp0) or ping to determine the link is up. If there is no link enable '''debug''' in ''/etc/ppp/options'' and use '''logread''' to check the error messages.

If you have services (vpn, ntpd) that should be started after the link is up, put the start-scripts in ''/etc/ppp/ip-up'' (don't forget to chmod +x).
For example:
{{{
#!/bin/sh

sh /etc/init.d/S55ntpd start
/usr/sbin/openvpn /etc/openvpn.conf
}}}

=== Access to syslog ===
If you want to read the syslog messages, use the '''logread''' tool.

== Applications ==

=== httpd ===

'''httpd''' is the binary, part of BusyBox, tool that start http daemon.

Documentation can be found at ["OpenWrtDocs/httpd"] .

=== socks-Proxy ===

There is a socks-proxy available for OpenWRT, it is called '''srelay''' (Find via the package tracker). However, there is no documentation for this package. So, here is a quick guide:

srelay comes with a configuration file: /etc/srelay.conf (surprise surprise).
It has some examples, but basically you will want to do this:

{{{
192.168.1.0/24 any -
}}}

This should give every computer in the 192.168.1-Subnet access to srelay while keeping everything else out.

Then start srelay: '''srelay -c /etc/srelay.conf -r -s'''. Find out more about the available options with '''srelay -h'''.

Keep in mind that this information was found using trial-and-error-methods, so it might still be faulty or have unwanted side effects.

=== uPnP ===

'''uPnP''' is Universal Plug and Play.  You can use either the LinkSys binary from the original firmware or the compiled version.

Documentation and the background of uPnP can be found at ["OpenWrtDocs/upnp"]

=== CUPSD ===

Known bugs:

Tespage printing doesn´t work. This is due to missing of the .css file from which will generate the Testpage.
Wrong permissions:

You have to replace

<Location />
AuthType Basic
AuthClass System
Order Allow,Deny
Allow From All
</Location>

with:

<Location />
Order Deny,Allow
Deny From All
Allow from 127.0.0.1
Allow from 192.168.1.0/24 #your ip area.
</Location>

Helpfull information for Steve disciple:

Its all you have to do. If you want to connect, your macosx with your mac you have to use the extended printer settings. If you use the standard printer settings and add an ipp printer, macosx will add after the server adress /ipp . But this class etc. does not exist on your cupsd.

= Hardware =

== LED ==

Document can be found at ["wrtLEDCodes"]
