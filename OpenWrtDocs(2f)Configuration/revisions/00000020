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
nvram show | less; Display everything in nvram
nvram get boot_wait; Get a specific variable
nvram set boot_wait=on; Set a value
nvram set lan_ifnames="vlan0 vlan1 vlan2"; set multiple values to one param
nvram unset foo; Delete a variable
nvram commit; Write changes to the flash chip (otherwise only stored in RAM)
}}}

A complete list of nvram options can be found at [:OpenWrtNVRAM].

= Network configuration =

The names of the network interfaces will depend largely on what hardware OpenWrt is run on.
{{{
WRT54G V1.x
  LAN=vlan2
  WAN=vlan1
  WIFI=eth2

WRT54G V2.x/WRT54GS V1.x
  LAN=vlan0
  WAN=vlan1
  WIFI=eth1

ASUS WL-500g
  WAN=eth0
  LAN=eth1
  WIFI=eth2
(LAN and WIFI are bridged together in br0 by default,
on some devices WAN can be eth1 and LAN eth0)

(please update to include other models)
}}}

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

The only <name> with any signfigance is '''wan''', used by the /etc/S45firewall script. The firewall script will NAT traffic through the wan_ifname, blocking connections to wan_ifname.

Further information about the variables used can be found at [:OpenWrtNVRAM]

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

To separate the LAN from the WIFI:
(lan as 192.168.1.25/24, wireless as 192.168.2.25/24, wan as dhcp)
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
}}}

== The ethernet switch ==

The WRT54G is essentially a WAP54G (wireless access point) with a 6 port switch. There's only one physical ethernet connection and that's wired internally into port 5 of the switch; the WAN is port 0 and the LAN is ports 1-4. The separation of the WAN and LAN interfaces is done by the switch itself. The switch has a vlan map which tells it which vlans can be accessed through which ports.

The vlan configuration is based on two variables (per vlan) in nvram.

{{{
vlan0ports="1 2 3 4 5*" (use ports 1-4 on the back, 5 is the wrt54g itself)
vlan0hwname=et0
}}}

=== Normal Behavior ===

This is only the case if the nvram variable boardflags is set, on the WRT54G V1.1 and earlier, it's not set.

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
vlan0ports="3 4 5*"
vlan0hwname=et0
vlan1ports="0 5"
vlan1hwname=et0
vlan2ports="1 2 5"
vlan2hwname=et0
}}}

=== Workaround ===

A workaround for devices that haven't got the boardflags set in nvram, is to install the package admcfg and add the following lines to /etc/init.d/S22admcfg:
{{{
if [ `nvram show 2> /dev/null | sed -e '/boardflags/!d'`a = "a" ]; then
  T=`mktemp /tmp/adm.XXXXXX`
  echo "admcfg port0
admcfg port1
admcfg port2
admcfg port3
admcfg port4
admcfg port5" > $T
  IFS='
'; for I in `nvram show 2> /dev/null | grep vlan.*ports | sort`; do
    L=`echo $I | sed -e 's#\(.*\)ports.*#\1#'`
    IFS=' ';for K in `echo $I | sed -e 's#.*=##' -e 's#\*##'`; do
      sed -e "s#\(port${K}.*\)#\1 $L#" $T > $T.2
      mv $T.2 $T
    done
  done
  S=`nvram show 2> /dev/null | sed -n -e 's#vlan\([0-9]*\)ports.*\*#\1#p'`
  sed -e "s#vlan\([0-9]*\)#PVID:\1 vlan\1#" \
    -e "/vlan/!s#\(.*\)#\1 DISABLED#" \
    -e "s#port5 PVID:[0-9]* #port5 PVID:$S #" $T > $T.2
  sh $T.2 > /dev/null
  rm $T $T.2
fi
}}}

It sets the vlan as the et module would do it.

== Wireless Distribution System (WDS) / Repeater / Bridge ==
OpenWrt supports the WDS protocol, which allows a point to point link to be established between two access points. By default, WDS links are added to the br0 bridge, treating them as part of the lan/wifi segment; clients will be able to seemlessly connect through either access point using wireless or the wired lan ports as if they were directly connected.

Configuration of WDS is simple, and depends on one of two variables

{{{#!CSV
NVRAM; Description
wl0_lazywds; Accept WDS connections from anyone (0:disabled 1:enabled)
wl0_wds; List of WDS peer mac addresses (xx:xx:xx:xx:xx:xx, space separated)
}}}

(Note: All APs must be on the same wireless channel and share the same encryption settings)

For security reasons, it's recommended that you leave wl0_lazywds off and use wl0_wds to control WDS access to your AP. wl0_wds functions as an access list of peers to accept connections from and peers to try to connect to; the peers will either need the mac address of your AP in their wl0_wds list, or wl0_lazywds enabled.


== OpenWRT wireless bridge ==

With 

{{{
nvram set wl0_mode=wet
}}}

you can use your AP/Router as a Bridge.

This section is work in progress, please refer to the following docs:


http://woz.gs/wifi/openwrtbridge.html

http://openwrt.org/forum/viewtopic.php?t=1078&highlight=wl0mode+wet
