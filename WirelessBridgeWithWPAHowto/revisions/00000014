= Work in progress: Setting up OpenWRT to be a wireless bridge on a WPA2-PSK wireless network =

== Rationale ==
This page describes how to set up an OpenWRT install -- a WRT54G v4 in my case -- to be a wireless bridge.  The goal is to end up with a plain bridge, no WDS, no routing, no anything except for holding one IP for administration, on a WPA2-PSK enabled wireless network.

Although it's very easy to set up client mode on an unsecured network (see ClientModeHowto) it's not a great idea to leave your network unprotected.  It turns out that client mode on a WPA network is not quite as easy.

This how-to is a work in progress - at least until I get everything working on my install!  All of the information was gleaned from the OpenWRT wiki and posts made in forum.openwrt.org and dozens of other web sites and I thank the multitude of unattributed contributors for sharing their knowledge.

== Instructions (to be expanded + completed) ==
 1. Delete /etc/init.d/S45firewall
 1. Delete /etc/init.d/S50dnsmasq
 1. Install nas and wl
 1. Install parprouted (from http://downloads.openwrt.org/people/nico/testing/mipsel/packages/)
 1. Set NVRAM
    * Networking:
        * wl0_mode=sta
        * wl0_akm=psk2
            * psk is also acceptable, but use wl0_crypto=tkip
            * "psk psk2" will not work - pick only one
        * wl0_crypto=aes+tkip
            * This is the group=tkip, pairwise=aes mix that is commonly used
        *  wl0_wpa_psk=''your psk'' (ASCII)
    * Break the bridge:
        * (This seems to be required to enable EAPOL negotiation to succeed.)
        * Note: These interface names are specific to the WRT54G and other related models but maybe not yours.
        * lan_ifname=vlan0 ''(Oddly, eth0 here seems not to work.)''
        * wifi_ifname=eth1
    * Enable DHCP on wireless side:
        * wifi_proto=dhcp
 1. Edit /etc/init.d/S41wpa and rename it S41wpa-supplicant
    * Remove the -l parameter from nas - it does not work in Supplicant mode (see ["OpenWrtDocs/nas"])
 1. Double-check everything, then mentally prepare yourself for a bricking.  (Failsafe mode should still work fine, but who knows?  I bricked mine enough times while figuring all of this out that the circuit board is sitting naked on top of a stack of paper as I type this.)
 1. nvram commit
 1. reboot

== Testing it out ==

At this point, you should have a more or less working wireless bridge: plug something in the LAN port and it'll be virtually connected to the same network as your other wireless clients.

As noted in the parprouted documentation, broadcasting will not cross the bridge.  In particular, that means that DHCP will need to be relayed explicitly using dhrelay or similar.  (I haven't gotten around to doing this yet.)

If nothing seems to work, try clearing your arp cache: arp -d

If still nothing seems to work, go grab a coffee and come back - the DHCP seems to take a while due to a timing conflict between the interface coming up, udhcpc making DHCP requests, and nas configuring the encryption.

== Troubleshooting ==

This section needs to be expanded.  If you try this and it doesn't work, please list some things you tried (and why) here for the benefit of future readers.

 * Check that the wireless connection is up:
    1. Set a machine to a static IP address on the same subnet as the lan_ipaddr and ssh in.
    1. Try ''wl assoclist'' to see if the bridge has associated with the AP.  (The AP's MAC address appears if so.)
    1. Try ''wl sta_info <AP MAC address>'' to see how far the connection has gone.
        * ASSOCIATED AUTHENTICATED AUTHORIZED is fully connected on the transport layer.
        * ASSOCIATED AUTHENTICATED probably means the encryption is not correct; double-check the wl0_akm and wl0_crypto and wl0_psk_key variables.
    1. Look at ''iwconfig eth1'' - the Encryption: field should show a key, not "off".

== Confirmation ==

If you follow this how-to, please note here if it worked or didn't work for you!

== Appendix: Data Listings ==

{{{
root@OpenWRT:~# nvram show | sort
...
lan_ifname=vlan0
lan_ifnames=vlan0 eth1 eth2                 # This is set by S05nvram and is not needed
lan_ipaddr=192.168.1.1                      # This doesn't matter
lan_netmask=255.255.255.0
lan_proto=static
...
vlan0hwname=et0                             # I changed this to enable all LAN ports to
vlan0ports=4 3 2 1 0 5*                     # be available for use
...
wifi_ifname=eth1
wifi_proto=dhcp
...
wl0_akm=psk2
wl0_crypto=aes+tkip
wl0_ifname=eth1
wl0_infra=1
wl0_mode=sta
wl0_radio=1
wl0_ssid=<< SSID >>
wl0_wpa_psk=<< PSK >>
...
}}}
