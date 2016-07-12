#acl Known:read,write All:read
[:OpenWrtDocs]
[[TableOfContents]]

= NVRAM =
NVRAM stands for Non-Volatile RAM, in this case the last 64K of the flash chip used to store various configuration information in a ''name=value'' format.

To display everything in nvram:
{{{
nvram show | less
}}}

To display only a specific value, eg. boot_wait
{{{
nvram get boot_wait
}}}

To set a value, eg. boot_wait
{{{
nvram set boot_wait="on"
}}}

To delete a variable, eg. foo
{{{
nvram unset foo
}}}

To save changes: (Unless commited to NVRAM, all changes are simply cached in RAM and lost on the next reboot)
{{{
nvram commit
}}}

= Network configuration =

The names of the network interfaces will depend largely on what hardware OpenWrt is run on. 
{{{
WRT54G V1.x
   LAN=vlan2
   WAN=vlan1
   WIFI=eth2

WRT54G V2.0/WRT54GS V1.0
   LAN=vlan0
   WAN=vlan1
   WIFI=eth1

(please update to include other models)
}}}

To maintain compatibility and to avoid using the limited jffs2 space, many of the network settings are stored in NVRAM.

'''Sample network configurations'''

(note these examples use wrt54g v2.0/wrt54gs v1.0 interface names)

The default network configuration:
{{{
lan_ifname="br0"
lan_ifnames="vlan0 eth1"
lan_proto="static"
lan_ipaddr="192.168.1.1"
lan_netmask="255.255.255.0"

wan_ifname="vlan1"
wan_proto="dhcp"
}}}

If you just want to use OpenWrt as an access point you can avoid the WAN interface completely:
{{{
lan_ifname="br0"
lan_ifnames="vlan0 eth1"
lan_proto="static"
lan_ipaddr="192.168.1.25"
lan_netmask="255.255.255.0"
lan_gateway="192.168.1.1"
lan_dns="192.168.1.1"

wan_proto="none"
}}}

To separate the LAN from the WIFI:
{{{
lan_ifname="vlan0"
lan_proto="static"
lan_ipaddr="192.168.1.25"
lan_netmask="255.255.255.0"

wifi_ifname="eth1"
wifi_proto="static"
wifi_ipaddr="192.168.2.25"
wifi_netmask="255.255.255.0"

wan_ifname="vlan1"
wan_proto="dhcp"
}}}
