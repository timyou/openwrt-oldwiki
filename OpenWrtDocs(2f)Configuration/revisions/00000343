#acl Known:read,write All:read
##
## Note: these pages document the firmware itself, not packages
##       QUESTIONS AND COMMENTS SHOULD BE POSTED TO THE FORUM
##       DO NOT ADD "On my router..." COMMENTS TO THIS PAGE
##
## THIS PAGE DOCUMENTS THE FIRMWARE, NOT PACKAGES
## DO NOT ADD PACKAGE DOCUMENTATION/CONFIGURATION TO THIS PAGE
##
OpenWrtDocs [[TableOfContents]]

= NVRAM =
NVRAM stands for Non-Volatile RAM, in this case the last 64K of the flash chip used to store various configuration information in a ''name=value'' format.

{{{
#!CSV
Command; Description
nvram show | sort | less; Display everything in NVRAM
nvram get boot_wait; Get a specific variable
nvram set boot_wait=on; Set a value
nvram set lan_ifnames="vlan0 vlan1 vlan2"; set multiple values to one param
nvram unset foo; Delete a variable
nvram commit; Write changes to the flash chip (otherwise only stored in RAM)
}}}
A complete list of nvram options can be found at ["OpenWrtNVRAM"].

= Network configuration =
'''Quick overview of the router architecture:'''

The WRT54G is made up of an Ethernet switch, a wireless access point and a router chip that connects them together.

Diagrams of the internal switch architectures can be found via the following table
||'''Device & Version''' || ||
||WRT54G v2/v3 & WRT54GS v1/v2 ||[http://voidmain.is-a-geek.net/i/WRT54_sw1_internal_architecture.png Switch diagram] ||
||WRT54G v4 & WRT54GS v3 ||[http://voidmain.is-a-geek.net/i/WRT54_sw2_internal_architecture.png Switch diagram] ||


[[Anchor(NetworkInterfaceNames)]]The names of the network interfaces will depend largely on what hardware !OpenWrt is run on. A more detailed explanation of the networking internals is on the page OpenWrtDocs/NetworkInterfaces
||'''Manufacturer''' ||'''Model''' ||'''Hardware version''' ||'''LAN''' ||'''WAN''' ||'''WIFI''' ||'''Comments''' ||
||Linksys ||WRT54G ||v1.0 ||vlan2 ||vlan1 ||eth2 || ||
||Linksys ||WRT54G ||v1.1/v2.x/v3.x/v4.0 ||vlan0 ||vlan1 ||eth1 || ||
||Linksys ||WRT54GL ||v1.0 ||vlan0 ||vlan1 ||eth1 || ||
||Linksys ||WRT54GL ||v1.1 ||vlan0 ||vlan1 ||eth1 ||LAN is ports 0-3, WAN is port 4 ||
||Linksys ||WRT54GS ||v1.x/v2.x/v3/v4 ||vlan0 ||vlan1 ||eth1 || ||
||Linksys ||WRTSL54GS || ||eth0 ||eth1 ||eth2 || ||
||Linksys ||WAP54G ||v1.0 ||br0 ||N/A ||eth1 ||Someone should double check this too ||
||Linksys ||WAP54G ||v2.0 ||eth0 ||N/A ||eth1 ||note^2^ ||
||Linksys ||WRT300N ||v1 ||eth0 ||eth1 ||eth2 || ||
||Asus ||WL-300g || ||eth0 ||None ||eth2 || ||
||Asus ||WL-500g || ||eth0 ||eth1 ||eth2 || ||
||Asus ||WL-500g Deluxe || ||vlan0 ||vlan1 ||eth1 ||note^1^ ||
||Asus ||WL-500g Premium || ||vlan0 ||vlan1 ||eth2 ||note^1^ ||
||Asus ||WL-HDD || ||eth1 ||N/A ||eth2 ||No switch and no WAN port ||
||Belkin ||["OpenWrtDocs/Hardware/Belkin/F5D7130"] ||1010 ||eth0 ||eth1 ||eth2 ||By default, LAN is br0 bridging eth0 and eth2 ||
||Buffalo ||WBR-G54 || ||eth0 ||eth1 ||eth2 || ||
||Buffalo ||WBR2-G54 || ||vlan0 ||vlan1 ||eth1 ||note^1^ ||
||Buffalo ||WBR2-G54S || ||vlan0 ||vlan1 ||eth1 ||note^1^ ||
||Buffalo ||WHR-G54S || ||vlan0 ||vlan1 ||eth1 ||note^1^ ||
||Buffalo ||WHR-G54S ||SN:7407 ||br0 ||vlan1 ||eth1 ||SVN-2006-09-15 ||
||Buffalo ||WHR3-G54 || ||eth0 ||eth1 ||eth2 ||no vlan support (switch BCM5325A2KQM) ||
||Buffalo ||WHR-HP-G54 || ||br0 ||vlan1 ||eth1 || ||
||Buffalo ||WLA-G54 || ||eth0 ||N/A ||eth2 ||No WAN port on this device ||
||Buffalo ||WZR-RS-G54 || ||eth0 ||eth1 ||eth2 ||no vlan support (switch BCM5325A2KQM) ||
||Dell ||!TrueMobile 2300 || ||eth0 ||eth1 ||eth2 ||BCM5325MA2KQM switch ||
||Motorola ||["WR850G"] ||v2 ||eth0 ||eth1 ||eth2 || ||
||Motorola ||["WR850G"] ||v3 ||vlan0 ||vlan1 ||eth1 ||note^1^ ||
||Microsoft ||MN700 ||v.x ||eth0 ||eth1 ||eth2 || ||
||Netgear ||WGT-634U || ||vlan0 ||vlan1 ||ath0 ||note^1^ ||
||Siemens ||SE505 ||v1 ||eth0 ||eth1 ||eth2 || ||
||Siemens ||SE505 ||v2 ||vlan0 ||vlan1 ||eth1 ||note^1^ ||


note^1^: This model uses a switch with vlan tagging; eth0 represents the connection from the router to the switch and the vlans ontop of eth0 will control which switch port(s) the packet is transmitted.

note^2^: Be careful: after flashing with OpenWRT, LAN stops working. Before flashing, set WAP54g to AP mode and after OpenWRT has been loaded, connect to the device through wireless and do: {{{nvram set lan_ifnames=eth0 eth1 ; nvram commit}}}

Please update to include other models.

'''NOTE:''' LAN and WIFI are bridged together in br0 by default, on some devices WAN can be eth1 and LAN eth0.

The basic network configuration is handled by a series of NVRAM variables:

{{{
#!CSV
NVRAM; Description
<name>_ifname; The name of the Linux interface the settings apply to
<name>_ifnames; Devices to be added to the bridge (only if the above is a bridge)
<name>_proto; The protocol which will be used to configure an IP
            ; static: Manual configuration (see below)
            ; dhcpclient: Perform a DHCP request (used to be just "dhcp")
            ; pppoe: Create a ppp tunnel
<name>_ipaddr; ip address (x.x.x.x)
<name>_netmask; netmask (x.x.x.x)
<name>_gateway; Default Gateway (x.x.x.x)
<name>_dns; DNS server (x.x.x.x)
<name>_hostname; hostname requested with dhcp
<name>_hwaddr; MAC address (aa:bb:cc:dd:ee:ff) if you want to use a different MAC of the ROM
}}}
Where <name> is either one of 'wl0', 'lan', or 'wan' for the wireless, local area network, or the wide area network respectively.

The command ''ifup <name>'' will configure the interface defined by <name>_ifname according to the above variables. As an example, the {{{/etc/init.d/S40network}}} script will automatically run the following commands at boot:

{{{
ifup lan
ifup wan
ifup wifi
}}}
The ''ifup lan'' command will bring up the interface specified by lan_ifname. Normally the lan_ifname is set to br0 which will cause it to create the bridge br0 and add the the interfaces from lan_ifnames to the bridge; lan_proto is usually static which means that br0 will have the IP address from lan_ipaddr, and so on for the rest of the variables listed above.

It's important to remember that it's the <name>_ifname that specifies the interfaces, the <name> component itself has almost no value. This means that if you changed lan_ifname to be the internet port, vlan1, then ''ifup lan'' would bring up the internet port, not the lan ports (despite using the command ''ifup lan'' and using the lan_ variables). Also, it means that you can create any <name> variables you want, foo_ifname, foo_proto .... and they would be used by ''ifup foo''.

The only <name> with any significance is '''wan''', used by the /etc/init.d/S45firewall script. The firewall script will NAT traffic through the wan_ifname, blocking connections to wan_ifname.

Further information about the variables used can be found at ["OpenWrtNVRAM"].

Don't forget to check the OpenWrtFaq for information about howto setup PPPoE etc.

'''Sample network configurations'''

For client mode configuration (rather than AP mode), see this page: ClientModeHowto. For further information on '''DHCP''' see this page ["OpenWrtDocs/dnsmasq"]

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
If you just want to use !OpenWrt as an access point you can avoid the WAN interface completely (LAN+wireless bridged as 192.168.1.25/24, routed through 192.168.1.1, WAN ignored):

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
The above configuration also serves as a wireless to Ethernet bridge. For e.g. you can have a PC with a wlan card with a static IP address be switched (bridged) to an Ethernet LAN. Neither the IP address of the lan gateway, or the dhcp server on the LAN interface interferes with this bridged configuration.

You can also have the lan interface fetch its configuration via DHCP, but to do so, you'll have to comment out the line:

{{{
# linksys bug; remove when not using static configuration for lan
nvram set lan_proto="static"
}}}
in /etc/init.d/S05nvram (For RC5 and earlier the usual story about replacing the symlink with a copy of the file before editing applies, see Editing files at ["OpenWrtDocs/Using"] ). After doing this, you need to set the appropriate nvram variable:

{{{
lan_proto=dhcp
}}}
To separate the LAN from the WIFI (LAN as 192.168.1.25/24, wireless as 192.168.2.25/24, WAN as DHCP, remove your WIFI interface (eth1 on v2/3 linksys routers) from the lan_ifnames variable):

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
lan_ifnames=vlan0
}}}
'''You MUST do this if you want to use ad-hoc mode, otherwise your throughput WILL suffer!'''

/!\ '''Tip:''' Don't forget to adjust packet filtering. For instance:
{{{iptables -I forwarding_rule -j ACCEPT}}}
enables packet forwarding (good for test, but insecure for
production).

= Ethernet switch configuration =
Most of the routers supported by OpenWrt include a builtin switch; four lan ports and one wan port. What most people don't realize is that all of these ports are actually the same interface -- there is a single 10/100 Ethernet which is fed into a 6 port switch. 5 of the ports are external and make the lan and wan ports seen on the back of the router, and one port is internally wired to the router's Ethernet interface.

The separation of lan and wan comes from the use of VLANs. By grouping ports into VLANs, the switch can be broken up into smaller virtual switches, and by adding VLAN tags to packets, OpenWrt can control which virtual switch (which ports) the packet gets routed.

There are normally two VLANs, vlan0 and vlan1. For each VLAN, there are two nvram variables, vlan*ports and vlan*hwname. So, the variables for vlan0 might look like this:

{{{
vlan0ports="1 2 3 4 5*" (use ports 1-4 on the back, 5 is the WRT54G itself)
vlan0hwname=et0
}}}
(See switch diagrams in OpenWrtDocs/NetworkInterfaces)

The vlan0ports variable is a space-separated list of port numbers to be included in vlan0. Ports "1-4" on this router represent the lan ports on the back of the router, port 5 represents the connection between the switch itself and OpenWrt's Ethernet interface. Since port 5 is OpenWrt's only connection to the switch, it is tagged by default -- this means that the VLAN information is preserved so OpenWrt is able to tell if a packet came from vlan0 or vlan1. All other ports are untagged by default, meaning that the VLAN information is removed by the switch so the port can be used by devices that aren't VLAN aware.

The port numbers used in the vlan*ports may optionally include a character after the port number. If a port number is followed by a "t" then the port is tagged, a "u" means untagged.

A "*" means that this VLAN is the primary VLAN (PVID); if a port is used in multiple vlans, packets without any VLAN information will be given to the primary VLAN for that port.

The second variable, vlan0hwname is used by the network configuration program (the ifup scripts) to determine the parent interface. This should be set to "et0" meaning the interface matching et0macaddr. The reason it's labeled "et0" and not "eth0" is mostly due to vxworks -- it's a legacy issue and OpenWrt keeps the "et0" name to be compatible with the existing settings.

As of RC4, the switch is programmed and controlled by a set of switch modules (switch-core and switch-robo or switch-adm, depending on your hardware). These switch modules will create a /proc/switch/eth0, showing the current settings for the switch. The /proc/switch/eth0/vlan/0/ports is used the exact same way as the vlan0ports nvram variable, allowing you to change the switch settings in realtime.

'''Sample configurations''' (unless otherwise specified, vlan variables not shown are assumed to be unset)

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
It's a good idea when choosing a vlan layout to keep port 1 in vlan0. At least the WRT54GS v1.0 will not accept new firmware via TFTP if port 1 is in another VLAN.

= Wireless configuration =
== Basic settings ==
||'''NVRAM variable''' ||'''Description''' ||
||wl0_mode ||'''ap''' = Access Point (master mode), '''sta''' = Routing client mode, '''wet''' = Bridged client mode ||
||wl0_ssid ||ESSID ||
||wl0_infra ||'''0''' = Ad Hoc mode, '''1''' = normal AP/Client mode ||
||wl0_closed ||'''0''' = Broadcast ESSID, '''1''' Hide ESSID ||
||wl0_channel ||1 / 2 / 3 /.../ 11 channel ||
See ["OpenWrtNVRAM"] for more NVRAM settings.

== MAC filter ==
||'''NVRAM variable''' ||'''Description''' ||
||'''wl0_macmode''' ||(disabled/allow/deny) used to (allow/deny) mac addresses listed in wl0_maclist ||
||'''wl0_maclist''' ||List of space-separated mac addresses to allow/deny according to wl0_macmode. Addresses should be entered with colons, e.g.: "00:02:2D:08:E2:1D 00:03:3E:05:E1:1B". note that if you have more than one mac use quotes or only the first will be recognized. ||
After changes run /sbin/wifi to activate them.

== WEP encryption ==
||'''NVRAM variable''' ||'''Description''' ||
||wl0_wep ||'''disabled''' = disabled WEP, '''enabled''' = enable WEP ||
||wl0_key ||'''1''' .. '''4''' = Select WEP key to use ||
||wl0_key[1..4] ||WEP key in hexadecimal format (allowed hex chars are 0-9a-f). '''Example:''' nvram set wl0_key1=0D77F08849E4B1D839C9489A48 ||
||wl0_auth ||'''1''' (shared key) / '''0''' (open); the 'shared key' option is not recommended as it allows an intruder to exploit a fundamental security flaw in WEP (WPA was introduced as the better system; see below). The 'open' setting will allow association but will make it an intruder more difficult to find the encryption key, needed for traffic. ||
Avoid using WEP keys with 00 at the end, otherwise the driver won't be able to detect the key length correctly. A 128-bit WEP key must be 26 hex digits long ; string key format is also supported : '''nvram set wl0_key1='s:my string key' '''

Setting up WPA will override any WEP settings.

== WPA encryption ==
For enabling WPA, you need to install the nas package. When you enable or disable WPA settings, you should make sure that the NVRAM variable '''wl0_auth_mode''' is unset, because it is obsolete.

'''YOU HAVE TO INSTALL THE NAS PACKAGE''' ( {{{ipkg install nas}}} )

More information is on ["OpenWrtDocs/nas"].

See OpenWrtDocs/Wpa2Enterprise for a detailed setup using Freeradius for user authentication.
||'''NVRAM variable''' ||'''Description''' ||
||<style="TEXT-ALIGN: center" |6>wl0_akm ||'''open''' = No WPA; Note: OpenWRT v0.9 uses the value '''none''' ||
||'''psk''' = WPA Personal/PSK (Preshared Key) ||
||'''wpa''' = WPA with a RADIUS server ||
||'''psk2''' = WPA2 PSK ||
||'''wpa2''' = WPA2 with RADIUS ||
||'''"psk psk2"''' or '''"wpa wpa2"''' = support both WPA and WPA2 '''Note:''' Do not use this value when wl0_mode=sta because supplicant mode does not seem to auto-negotiate. You must select one protocol which the access point supports (refer to the AP's specs) ||
||<style="TEXT-ALIGN: center" 
