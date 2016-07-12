This page describes setting up a simple wireless hotspot with the following features:

 * Open access to the hotspot
 * Capture (splash) page
 * Port restrictions
 * Bandwidth Limit
 * Separate, secure wireless access for local use

The goal was to use a single WRT54GL to both provide local secure wifi, and share a portion of our bandwidth as a free hotspot, with a splash page to advertise who is providing the hotspot, and the fact that secure, faster access is available for a small contribution towards costs. It uses the nodogsplash package which provides a trivial splash page and authentication system and seems more simple than chillispot. The secure wireless is bridged to the hard-wired ports, but the hotspot is separate, and isolated from the local network.

Author: [http://carroll.org.uk/contact Matthew Carroll]

OpenWRT Version: Kamikaze

Hardware: WRT54GL

== Install necessary packages ==

{{{
ipkg install nodogsplash
}}}

== Configure network settings ==

/etc/config/network

{{{
#### LAN configuration
config interface lan
option type      bridge
option ifname    eth0.0
option proto     static
option ipaddr    10.10.10.1
option netmask   255.255.255.0

#### WAN configuration
config interface wan
option ifname    eth0.1
option proto     dhcp

#### HOTSPOT configuration
config interface wifi
option ifname    eth1.0
option proto     static
option ipaddr    10.10.15.1
option netmask   255.255.255.0
}}}

== Configure wireless settings ==

/etc/config/wireless

{{{
config wifi-device  wl0
option type         broadcom
option channel      11
option disabled     0

config wifi-iface
option device       wl0
option network      lan
option mode         ap
option ssid         mywifi-secure
option encryption   psk2
option hidden       0
option key          'your%verylong.andsecure-pskkey'

config wifi-iface
option device       wl0
option network      wifi
option mode         ap
option ssid         public-hotspot
option encryption   none
option hidden       0
}}}

== Configure DHCP ==

/etc/config/dhcp

{{{
config dhcp
        option interface        lan
        option start    100
        option limit    150
        option leasetime        12h

config dhcp
        option interface        wan
        option ignore   1

config dhcp
        option interface        wifi
        option start    100
        option limit    150
        option leasetime        2h
}}}

== Configure nodogsplash ==

/etc/nodogsplash/nodogsplash.conf

(relevant changes only)

Tell nodogsplash to manage the public hotspot connection:

{{{
GatewayInterface wl0.1
}}}

Allow access to email:

{{{
FirewallRuleSet authenticated-users {
...
FirewallRule allow tcp port 995
FirewallRule allow tcp port 993
FirewallRule allow tcp port 465
FirewallRule allow tcp port 110
FirewallRule allow tcp port 143
}}}

Restrict access to the gateway from the hotspot side:

{{{
FirewallRuleSet users-to-router {
...
#    FirewallRule allow tcp port 22
#    FirewallRule allow tcp port 80
#    FirewallRule allow tcp port 443
}}}

Restrict bandwidth available to hotspot (adjust according to preference):

{{{
trafficControl yes
...
DownloadLimit 200
...
UploadLimit 100
}}}

== Customise splash page ==

Edit these files to customise the splash page / error page:

/etc/nodogsplash/htdocs/splash.html

/etc/nodogsplash/htdocs/infoskel.html

Note, to include an external css file, put it in the images dir, and include as so:

{{{
@import url("$imagesdir/stylesheet.css");
}}}

Somewhere in splash.html you should include a link for the authentication, e.g:

{{{
<a href="$authtarget">Connect...</a>
}}}
