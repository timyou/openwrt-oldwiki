#acl Known:read,write All:read
##
## Note: these pages document the firmware itself, not packages
##       QUESTIONS AND COMMENTS SHOULD BE POSTED TO THE FORUM
##       DO NOT ADD "On my router..." COMMENTS TO THIS PAGE
##
## THIS PAGE DOCUMENTS THE FIRMWARE, NOT PACKAGES
## DO NOT ADD PACKAGE DOCUMENTATION/CONFIGURATION TO THIS PAGE
##


[:OpenWrtDocs]
[[TableOfContents]]

= NVRAM =

NVRAM stands for Non-Volatile RAM, in this case the last 64K of the flash chip used to
store various configuration information in a ''name=value'' format.

{{{#!CSV
Command; Description
nvram show | sort | less; Display everything in NVRAM
nvram get boot_wait; Get a specific variable
nvram set boot_wait=on; Set a value
nvram set lan_ifnames="vlan0 vlan1 vlan2"; set multiple values to one param
nvram unset foo; Delete a variable
nvram commit; Write changes to the flash chip (otherwise only stored in RAM)
}}}

A complete list of nvram options can be found at [:OpenWrtNVRAM].


= Network configuration =

'''Quick overview of the router architecture:'''

The WRT54G is made up of an Ethernet switch, a wireless access point and a router chip
that connects them together.

Diagrams of the internal switch architectures on can be found on the following table

||'''Device & Version'''||||
||WRT54G v2/v3 & WRT54GS v1/v2||[http://voidmain.is-a-geek.net/i/WRT54_sw1_internal_architecture.png Switch diagram]||
||WRT54G v4 & WRT54GS v3||[http://voidmain.is-a-geek.net/i/WRT54_sw2_internal_architecture.png Switch diagram]||

[[Anchor(NetworkInterfaceNames)]]
The names of the network interfaces will depend largely on what hardware !OpenWrt is run on.

||'''Manufacturer'''||'''Model'''||'''Hardware version'''||'''LAN'''||'''WAN'''||'''WIFI'''||'''Comments'''||
||Linksys||WRT54G||v1.x||vlan2||vlan1||eth2|| ||
||Linksys||WRT54G||v2.x/v3.x/v4.0||vlan0||vlan1||eth1|| ||
||Linksys||WRT54GL||v1.0||vlan0||vlan1||eth1|| ||
||Linksys||WRT54GS||v1.x/v2.x/v3/v4||vlan0||vlan1||eth1|| ||
||Linksys||WRTSL54GS|| ||eth0||eth1||eth2||Someone should double check this||
||Asus||WL-300g|| ||eth0||None||eth2|| ||
||Asus||WL-500g|| ||eth0||eth1||eth2|| ||
||Asus||WL-500g Deluxe|| ||vlan0||vlan1||eth1||note^1^||
||Asus||Wl-HDD|| ||eth1||N/A||eth2||No switch and no WAN port||
||Buffalo||WBR-G54|| ||eth0||eth1||eth2|| ||
||Buffalo||WBR2-G54|| ||vlan0||vlan1||eth1||note^1^||
||Buffalo||WBR2-G54S|| ||vlan0||vlan1||eth1||note^1^||
||Buffalo||WLA-G54|| ||eth0||N/A||eth2||No WAN port on this device||
||Buffalo||WZR-RS-G54||  ||eth0||eth1||eth2||no vlan support (switch BCM5325A2KQM)||
||Dell||!TrueMobile 2300||  ||eth0||eth1||eth2||BCM5325MA2KQM switch||
||Motorola||WR850G||v3||vlan0||vlan1||eth1||note^1^||
||Microsoft||MN700||v.x||eth0||eth1||eth2|| ||
||Netgear||WGT-634U|| ||vlan0||vlan1||ath0||note^1^||
||Siemens||SE505||v1||eth0||eth1||eth2|| ||
||Siemens||SE505||v2||vlan0||vlan1||eth1||note^1^||

note^1^: This model uses a switch with vlan tagging; eth0 represents the connection from the router to the switch and the vlans ontop of eth0 will control which switch port(s) the packet is transmitted.


Please update to include other models.

'''NOTE:''' LAN and WIFI are bridged together in br0 by default, on some devices WAN
can be eth1 and LAN eth0.

In general, the switch works the following way: It recieves data (physical) on either
lan port or on the wan port. Then the switch tags the packages (with VLAN), so Linux
is able to see the difference and that way we have the vlan devices, which describe wan
or lan port.

[[BR]]The basic network configuration is handled by a series of NVRAM variables:

{{{#!CSV
NVRAM; Description
<name>_ifname; The name of the linux interface the settings apply to
<name>_ifnames; Devices to be added to the bridge (only if the above is a bridge)
<name>_proto; The protocol which will be used to configure an IP
            ; static: Manual configuration (see below)
            ; dhcp: Perform a DHCP request
            ; pppoe: Create a ppp tunnel
<name>_ipaddr; ip address (x.x.x.x)
<name>_netmask; netmask (x.x.x.x)
<name>_gateway; Default Gateway (x.x.x.x)
<name>_dns; DNS server (x.x.x.x)
<name>_hostname; hostname requested with dhcp
}}}

The command ''ifup <name>'' will configure the interface defined by <name>_ifname according
to the above variables. As an example, the {{{/etc/init.d/S40network}}} script will automatically
run the following commands at boot:

{{{
ifup lan
ifup wan
ifup wifi
}}}

The ''ifup lan'' command will bring up the interface specified by lan_ifname. Normally the
lan_ifname is set to br0 which will cause it to create the bridge br0 and add the the interfaces
from lan_ifnames to the bridge; lan_proto is usually static which means that br0 will have the IP
address from lan_ipaddr, and so on for the rest of the variables listed above.

It's important to remember that it's the <name>_ifname that specifies the interfaces, the <name>
compontent itself has almost no value. This means that if you changed lan_ifname to be the internet
port, vlan1, then ''ifup lan'' would bring up the internet port, not the lan ports (despite using
the command ''ifup lan'' and using the lan_ variables). Also, it means that you can create any
<name> variables you want, foo_ifname, foo_proto .... and they would be used by ''ifup foo''.

The only <name> with any significance is '''wan''', used by the /etc/init.d/S45firewall script.
The firewall script will NAT traffic through the wan_ifname, blocking connections to wan_ifname.

Further information about the variables used can be found at [:OpenWrtNVRAM].

Don't forget to check the [:OpenWrtFaq] for information about howto setup PPPoE etc.


'''Sample network configurations'''

For client mode configuration (rather than AP mode), see this page: [:ClientModeHowto].

('''NOTE:''' these examples use WRT54G v2.x/WRT54GS v1.x interface names)

The default network configuration (LAN + wireless bridged as 192.168.1.1/24, WAN as DHCP):

{{{
lan_ifname=br0
lan_ifnames="vlan0 eth1"
lan_proto=static
lan_ipaddr=192.168.1.1
lan_netmask=255.255.255.0

wan_ifname=vlan1
wan_proto=dhcp
}}}

If you just want to use !OpenWrt as an access point you can avoid the WAN interface completely
(LAN+wireless bridged as 192.168.1.25/24, routed through 192.168.1.1, WAN ignored):

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

You can also have the lan interface fetch its configuration via DHCP, but to do so, you'll
have to comment out the line:

{{{
# linksys bug; remove when not using static configuration for lan
nvram set lan_proto="static"
}}}

in /etc/init.d/S05nvram (The usual story about replacing the symlink with a copy of the
file before editting applies). After doing this, you need to set the appropriate nvram
variable:

{{{
lan_proto=dhcp
}}}

To separate the LAN from the WIFI (LAN as 192.168.1.25/24, wireless as 192.168.2.25/24,
WAN as DHCP, remove your WIFI interface (eth1 on v2/3 linksys routers) from the lan_ifnames
variable):

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

lan_ifnames="vlan0 vlan1 eth1"
}}}

'''You MUST do this if you want to use ad-hoc mode, otherwise your throughput WILL suffer!'''

= Ethernet switch configuration =

FIXME

OpenWrtRoboCfg

The WRT54G is essentially a WAP54G (wireless access point) with a 6 port switch. There's
only one physical ethernet connection and that's wired internally into port 5 of the switch;
the WAN is port 0 and the LAN is ports 1-4. The separation of the WAN and LAN interfaces is
done by the switch itself. The switch has a VLAN map which tells it which VLANs can be accessed
through which ports.

The VLAN configuration is based on two variables (per VLAN) in NVRAM.

{{{
vlan0ports="1 2 3 4 5*" (use ports 1-4 on the back, 5 is the WRT54G itself)
vlan0hwname=et0
}}}

(See switch diagram in section 2)

This is only the case if the NVRAM variable boardflags is set. On the WRT54G V1.1 and
earlier, it's not set.

When the et module (ethernet driver) loads it will read from vlan0ports to vlan15ports,
behind the scenes the ethernet driver is using these variables to generate a more complex
configuration which will be sent to the switch. When packets are received from external
devices they need to be assigned a vlan id, and when packets are sent to those external
devices the VLAN tags need to be removed.

PVID represents the primary VLAN id, in other words if a packet doesn't have a VLAN tag,
which VLAN does it belong to? The ethernet driver handles this rather trivially, in the
case of vlan0ports="1 2 3 4 5*", ports 1-4 are set to PVID 0 (vlan0). Since the wrt needs
to receive packets from both the LAN (vlan0) and the WAN (vlan1), port 5 is a special case
appearing in both vlan0ports and vlan1ports. This is where the '*' is used -- it determines
the PVID of port 5, which is also the only port not to untag packets (for hopefully obvious
reasons).

Remark to "*": On ASUS-500GX is possible make external port tagged in this way vlan0ports="1t 2 5*".
This is syntax like robocfg tool. Tested on White Russian RC2, may be possible on all BCM5325
HWs. "*" have no effect, maybe exist for compatibility. This behaviour is at least confirmed with
WRT54G(v3.1) and WRT54GS(v2.1) and White Russian RC3.

The second variable, vlan0hwname is used by the network configuration program (or script in
the case of !OpenWrt) to determine the parent interface. This should be set to "et0" meaning
the interface matching et0macaddr.

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

It's a good idea when choosing a vlan layout to keep port 1 in vlan0. At least the WRT54GS
v1.0 will not accept new firmware via TFTP if port 1 is in another VLAN.

= Wireless configuration =

== Basic settings ==

|| '''NVRAM variable''' || '''Description''' ||
|| wl0_mode  || '''ap''' = Access Point (master mode), '''sta''' = Routing client mode, '''wet''' = Bridged client mode||
|| wl0_ssid  || ESSID ||
|| wl0_infra || '''0''' = Ad Hoc mode, '''1''' = normal AP/Client mode ||
|| wl0_closed || '''0''' = Broadcast ESSID, '''1''' Hide ESSID ||
|| wl0_channel || 1 / 2 / 3 /.../ 11 channel ||

See [:OpenWrtNVRAM] for more NVRAM settings.

== MAC filter ==

|| '''NVRAM variable''' || '''Description''' ||
||'''wl0_macmode'''||(disabled/allow/deny) used to (allow/deny) mac addresses listed in wl0_maclist||
||'''wl0_maclist'''||List of space separated mac addresses to allow/deny according to wl0_macmode. Addresses should be entered with colons, e.g.: "00:02:2D:08:E2:1D 00:03:3E:05:E1:1B". note that if you have more than one mac use quotes or only the first will be recognized. ||

After changes run /sbin/wifi to activate them

== WEP encryption ==

|| '''NVRAM variable''' || '''Description''' ||
|| wl0_wep || '''disabled''' = disabled WEP, '''enabled''' = enable WEP ||
|| wl0_key || '''1''' .. '''4''' = Select WEP key to use ||
|| wl0_key[1..4] || WEP key in hexadecimal format (allowed hex chars are 0-9a-f). '''Example:''' nvram set wl0_key1=0D77F08849E4B1D839C9489A48 ||
|| wl0_auth || '''1''' (shared key) / '''0''' (open); the 'shared key' option is not recommended as it allows an intruder to exploit a fundamental security flaw in WEP (WPA was introduced as the better system; see below). The 'open' setting will allow association but will make it an intruder more difficult to find the encryption key, needed for traffic. ||

Avoid using WEP keys with 00 at the end, otherwise the driver won't be able to detect the
key length correctly. A 128 bit WEP key must be 26 hex digits long ; string key format is also supported : '''nvram set wl0_key1='s:my string key' '''

Setting up WPA will override any WEP settings.


== WPA encryption ==

For enabling WPA, you need to install the nas package. When you enable or disable WPA
settings, you should make sure that the NVRAM variable '''wl0_auth_mode''' is unset,
because it is obsolete.

'''YOU HAVE TO INSTALL THE NAS PACKAGE''' ( {{{ipkg install nas}}} )

More information is on [:OpenWrtDocs/nas].

See [:OpenWrtDocs/Wpa2Enterprise] for a detailed setup using Freeradius for user authentication.

|| '''NVRAM variable''' || '''Description''' ||
||<|6> wl0_akm || '''open''' = No WPA ||
||  '''psk''' = WPA Personal/PSK (Preshared Key) ||
||  '''wpa''' = WPA with a RADIUS server ||
||  '''psk2''' = WPA2 PSK ||
||  '''wpa2''' = WPA2 with RADIUS ||
||  '''"psk psk2"''' or '''"wpa wpa2"''' = support both WPA and WPA2 ||
||<|3> wl0_crypto || '''tkip''' = RC4 encryption ||
||  '''aes''' = AES encryption ||
||  '''aes+tkip''' = support both ||
|| wl0_wpa_psk || Password to use with WPA/WPA2 PSK (at least 8, up to 63 chars) ||
|| wl0_radius_key || Shared Secret for connection to the Radius server ||
|| wl0_radius_ipaddr || IP to connect... ||
|| wl0_radius_port || Port# to connect... ||
|| wl0_auth|| '''0''' ||


== Wireless Distribution System (WDS) / Repeater / Bridge ==

!OpenWrt supports the WDS protocol, which allows a point to point link to be established
between two access points. By default, WDS links are added to the br0 bridge, treating
them as part of the lan/wifi segment; clients will be able to seamlessly connect through
either access point using wireless or the wired lan ports as if they were directly connected.

Configuration of WDS is simple, and depends on one of two variables

{{{#!CSV
NVRAM; Description
wl0_lazywds; Accept WDS connections from anyone (0:disabled 1:enabled)
wl0_wds; List of WDS peer mac addresses (xx:xx:xx:xx:xx:xx, space separated)
}}}

For security reasons, it's recommended that you leave wl0_lazywds off and use wl0_wds to control
WDS access to your AP. wl0_wds functions as an access list of peers to accept connections from
and peers to try to connect to; the peers will either need the mac address of your AP in their
wl0_wds list, or wl0_lazywds enabled.

Easy steps for a successful WDS:

First do it without wireless protection and then activate the protection.
If you activate both you will double the pain to find a problem.

 1. Configure the IPs of each AP - don't use the same! For easier maintenance you can use the same subnet.
 1. Add the '''other''' APs MAC address to the list of allowed peers to each AP. With OpenWRT it's the variable wl0_wds.
 1. Disable all the unneeded services like DHCP, port forwarding, firewalling etc. '''except''' on the AP the has the internet connection. Remember: The other APs only act as the extended arm of the internet connected AP.
 1. Configure the WLAN parameters on all APs identical. That is SSID, channel, etc. - keep it simple. If you want to try boosters etc. do this later. (In [:JonathanKollasch: my] experience the SSIDs need not be identical for WDS to work, but YMMV.)
 1. Have you commited your values? Do it. And reboot.
 1. Now connect a lan cable to each AP and try to ping the internet AP. It should answer. Else start checking the settings.
 1. You are done. Now activate security on the devices. Optionally hide the SSID (wl0_closed=1). If WPA-PSK doesn't work chances are that a peer partner doesn't support it. Try WEP.

/!\ '''NOTE:''' If you broke up your bridge as detailed in "To separate the LAN from the
WIFI" above, this will not just work, since you no longer have a br0 device. You will have
to add a bridge to one of your devices again, and create appropriate firewall rules, to make
things work. There are currently no detailed instructions on how to set this up, so you
better know what you are doing...


== Wireless client / wireless bridge ==

The only thing you have to do is to switch the WL mode like with the bridge:

{{{
nvram set wl0_mode=wet
}}}

For more information, see [:ClientModeHowto].

## == SecureEasySetup button (a.k.a. CISCO button) ==
##
## obsolete text removed - please use the /proc/sys/diag and /proc/sys/button interfaces

= Basic system configuration and usage =

== busybox - The Swiss Army Knife of Embedded Linux ==

== cron - job scheduler ==

See [:HowtoEnableCron].

== syslog - Logging ==

To read the syslog messages, use the '''logread''' command.
See MiniHowtos to set up remote logging.

== dropbear - Secure Shell server ==

For SSH login without password, put your keys in /etc/dropbear/authorized_keys.
See DropbearPublicKeyAuthenticationHowto.

== iptables - Firewall ==

The rules and some small samples for your firewall can be found in /etc/firewall.user.  If you want to make changes to this file, you'll have to remove it first, since it is actually a symlink to /rom/etc/firewall.user.

{{{
ls -l /etc/firewall.user
rm /etc/firewall.user
cp /rom/etc/firewall.user /etc
}}}

Be sure to read the notes about the firewall rules before changing anything.  The important thing to note is that if you setup port forwarding, you won't be able to see the changes inside the router's LAN.  You will have to access the router from outside to verify the setup.

The first section, '''Open port to WAN''' shows an example of opening a port for your router running OpenWRT to listen to and accept.  In the case given, it will open up port 22 and accept connections using dropbear (the SSH server).  Just delete the '''#''' sign in front of the two rules to enable access.

If you wanted to open up any other ports for the router to listen to, just copy those two lines and change just the port number from 22 to something else.

The second section, '''Port forwarding''' is for accepting incoming connections from the WAN (outside the router) and sending the requests to a networked device on your LAN (inside your router).

Before setting up any port forwarding, you'll have to install some OpenWRT packages first, such as iptables-nat and ip (any others?).

In the example provided, if someone on the Internet were to connect to your router on port 8080, it would forward them to port 80 on whatever computer / device had the IP address of 192.168.1.2.

If you are running a webserver on that address, and want to listen on port 80 instead, change the 8080 on the first line.

The same is true for any other ports you'd want to forward to your LAN.  Just follow the example as a guide.

The last section, '''DMZ''' is sending all connections to a port not specified in the rules above to a certain IP address.  If you do decide to use this, it would be a good idea to have a firewall managing the ports on the destination.  The DMZ can be considered a simple way to let another computer handle the firewall rules, if you don't want to configure them on OpenWRT and at the same time you want to send all connections to one device.

Once you're finished making changes to your firewall, restart it by running the init script:

{{{
/etc/init.d/S45firewall restart
}}}

Remember to test the changes outside your LAN!

== dnsmasq - DNS and DHCP server ==

Dnsmasq is a lightweight, easy to configure DNS forwarder and DHCP server.

Documentation can be found at [:OpenWrtDocs/dnsmasq].

== Time ==

Most devices supported by !OpenWrt have no real-time clock hardware onboard,
and must get the date and time at boot or use the default of 2000-01-01.

You must have the correct time to use OpenVPN on !OpenWrt.

You may use either ''ntpclient'', ''rdate'', ''htpdate'' or ''openntpd''.

'''ntpclient'''

The ''ntpclient'' package will maintain the system time using the Network Time Protocol (NTP) while a link is up that provides a default route.  If the link goes down, the kernel maintains the time based on the processor oscillator, and it will slowly drift.  If the link comes back up, the system time will be resynchronised.

Install the package, reboot, and then check the system time.

You may wish to choose an NTP server close to your router.

||'''NVRAM Setting'''||'''Default Value'''||'''Meaning'''||
||'''ntp_server'''||pool.ntp.org||host name or IP address of NTP server to use when default route begins||

You may use the ''openntpd'' package to provide NTP service to other hosts.

'''rdate'''

The ''rdate'' command synchronises the system time to the time on a remote host
using the time protocol on TCP port 37.  It is normally used once during boot, and
then the kernel maintains the time based on the processor oscillator.
It will slowly drift.  ''rdate'' is part of the ''busybox'' package and is already installed.

Create the file {{{/etc/init.d/S42rdate}}} with the contents:
{{{
#!/bin/sh
/usr/sbin/rdate HOST}}}

replacing HOST with the IP address or host name of the time server, then make it executable:
{{{
chmod a+x /etc/init.d/S42rdate}}}

then either reboot or run it this once:
{{{
/etc/init.d/S42rdate}}}

'''htpdate'''

The ''htpdate'' package synchronises the time using innocuous web page requests as if it is a web browser.  It obtains the time from part of the HTTP header reply sent by web servers.

Install the ''htpdate'' package using ''ipkg'':
{{{
ipkg install htpdate}}}

Test by asking ''htpdate'' to set the time to that provided by a remote web server:
{{{
htpdate -s HOSTNAME}}}

Configure ''/etc/default/htpdate'' with a set of servers to probe.

Rename ''/etc/init.d/htpdate'' to ''/etc/init.d/S41htpdate''.

## TODO: add openntpd explanation, 
## openntpd could be useful for distributing NTP services further to clients near to the !OpenWrt system.

== Timezone ==

Without a time zone set, !OpenWrt will display UTC.

To set a time zone use the {{{/etc/TZ}}} file. Copy & paste the time zones from the
table below into the file. In this example it's done with the {{{echo}}} command.

{{{
echo "CET-1CEST-2,M3.5.0/02:00:00,M10.5.0/03:00:00" > /etc/TZ
}}}

'''NOTE:''' This sets the time zone for CET/CEST (Central European Time UTC+1 / Central European
Summer Time UTC+2) and the starting (5th week of March at 02:00) and endtime (5th week of October
at 03:00) of DST (Daylight Saving Time).

More can be found here [http://leaf.sourceforge.net/doc/guide/buci-tz.html#id2594640]
and [http://openwrt.org/forum/viewtopic.php?id=131].

Examples:
||<|6>Australia||Melbourne,Canberra,Sydney||EST-10EDT-11,M10.5.0/02:00:00,M3.5.0/03:00:00||
||Perth||WST-8||
||Brisbane||EST-10||
||Adelaide||CST-9:30CDT-10:30,M10.5.0/02:00:00,M3.5.0/03:00:00||
||Darwin||CST-9:30||
||Hobart||EST-10EDT-11,M10.1.0/02:00:00,M3.5.0/03:00:00||
||<|21>Europe||Amsterdam, Netherlands||CET-1CEST-2,M3.5.0/02:00:00,M10.5.0/03:00:00||
||Athens, Greece||EET-2EEST-3,M3.5.0/03:00:00,M10.5.0/04:00:00||
||Barcelona, Spain||CET-1CEST-2,M3.5.0/02:00:00,M10.5.0/03:00:00||
||Berlin, Germany||CET-1CEST-2,M3.5.0/02:00:00,M10.5.0/03:00:00||
||Brussels, Belgium||CET-1CEST-2,M3.5.0/02:00:00,M10.5.0/03:00:00||
||Budapest, Hungary||CET-1CEST-2,M3.5.0/02:00:00,M10.5.0/03:00:00||
||Copenhagen, Denmark||CET-1CEST-2,M3.5.0/02:00:00,M10.5.0/03:00:00||
||Dublin, Ireland||GMT+0IST-1,M3.5.0/01:00:00,M10.5.0/02:00:00||
||Geneva, Switzerland||CET-1CEST-2,M3.5.0/02:00:00,M10.5.0/03:00:00||
||Helsinki, Finland||EET-2EEST-3,M3.5.0/03:00:00,M10.5.0/04:00:00||
||Kyiv, Ukraine||EET-2EEST,M3.5.0/3,M10.5.0/4||
||Lisbon, Portugal||WET-0WEST-1,M3.5.0/01:00:00,M10.5.0/02:00:00||
||London, Great Britain||GMT+0BST-1,M3.5.0/01:00:00,M10.5.0/02:00:00||
||Madrid, Spain||CET-1CEST-2,M3.5.0/02:00:00,M10.5.0/03:00:00||
||Oslo, Norway||CET-1CEST-2,M3.5.0/02:00:00,M10.5.0/03:00:00||
||Paris, France||CET-1CEST-2,M3.5.0/02:00:00,M10.5.0/03:00:00||
||Prague, Czech Republic||CET-1CEST-2,M3.5.0/02:00:00,M10.5.0/03:00:00||
||Roma, Italy||CET-1CEST-2,M3.5.0/02:00:00,M10.5.0/03:00:00||
||Moscow, Russia||MSK-3MSD,M3.5.0/2,M10.5.0/3||
||St.Petersburg, Russia||MST-3MDT,M3.5.0/2,M10.5.0/3||
||Stockholm, Sweden||CET-1CEST-2,M3.5.0/02:00:00,M10.5.0/03:00:00||
||New Zealand||Auckland, Wellington||NZST-12NZDT-13,M10.1.0/02:00:00,M3.3.0/03:00:00||
||<|7>USA & Canada^1^||Hawaii Time||HAW10||
||Alaska Time||AKST9AKDT||
||Pacific Time||PST8PDT||
||Mountain Time||MST7MDT||
||Mountain Time (Arizona, no DST)||MST7||
||Central Time||CST6CDT||
||Eastern Time||EST5EDT||
||Atlantic Time||AST4ADT||
||<|3>Asia||Jakarta||WIB-7||
||Singapore||SGT-8||
||Ulaanbaatar, Mongolia||ULAT-8ULAST,M3.5.0/2,M9.5.0/2||
||<|3>Central and South America||Brazil, São Paulo||BRST+3BRDT+2,M10.3.0,M2.3.0||
||Argentina||UTC+3||
||Central America||CST+6||

Please update and include your time zone. You can find more on time zones on
[http://www.timeanddate.com/worldclock/ timeanddate.com].

^1^in August of 2005, the United States President Bush passed the [http://www.fedcenter.gov/_kd/Items/actions.cfm?action=Show&item_id=2969&destination=ShowItem Energy Policy Act], which, among other things, changes the time change dates for daylight saving time from the first Sunday in April to the second Sunday in March and from the last Sunday in October to the first Sunday in November. This pattern starts in 2007, however, and Congress still has time to revert the DST back. As such, these changes have not yet been incorporated into mainline uClibc (which provides the time functions for the C library used by OpenWrt). Therefore, it might be a good idea to change {{{/etc/TZ}}} explicitly (around mid-November 2006) to reflect this change (i.e., instead of {{{EST5EDT}}} write {{{EST5EDT,M3.2.0,M9.1.0}}}).
