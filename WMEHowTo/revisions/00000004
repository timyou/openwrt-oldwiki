[[TableOfContents]]

= Introduction =
If you're using a wireless multimedia device, such as a SIP WLAN phone, you might want to enable the WME extensions (802.11e) to enable those devices to save power. This tutorial assumes that your WIFI device is eth1. To find out what device your router uses please consult the ["OpenWrtDocs/Configuration"] page.

= Enable WME (802.11e) =

== Install the wl package ==
{{{
ipkg install wl
}}}

== Find out if WME is already enabled ==

{{{
wl -i eth1 wme
}}}

If the output of the command is 1 then WME is already enabled. In this case you don't have to proceed.

== Shutdown the WIFI interface ==

{{{
ifconfig eth1 down
}}}

== Enable WME (802.11e) ==

{{{
wl -i eth1 wme 1
}}}

== Bring up the WIFI interace again ==

{{{
ifconfig eth1 up
}}}

= Enable WME (802.11e) on boot time =

To enable WME on boot time insert the following line to the file /etc/init.d/S40network (above the loop where all interfaces are brought up with ifup):

{{{
wl -i $(nvram get wl0_ifname) wme 1
}}}

After a reboot WME should be enabled automatically.
