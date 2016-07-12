= Work in progress: Setting up OpenWRT to be a wireless bridge on a WPA2-PSK wireless network =

== Rationale ==
This page describes how to set up an OpenWRT install -- a WRT54G v4 in my case -- to be a wireless bridge.  The goal is to end up with a plain bridge, no WDS, no routing, no anything except for holding one IP for administration, on a WPA2-PSK enabled wireless network.

Although it's very easy to set up client mode on an unsecured network (see ClientModeHowto) it's not a great idea to leave your network unprotected.  It turns out that client mode on a WPA network is not quite as easy.

This how-to is a work in progress - at least until I get everything working on my install!  All of the information was gleaned from the OpenWRT wiki and posts made in forum.openwrt.org and I thank the multitude of unattributed contributors.

== Instructions (to be expanded + completed) ==
 1. Delete /etc/init.d/S45firewall
 1. Delete /etc/init.d/S50dnsmasq
 1. Install nas and wl
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
        * lan_ifname=vlan0 '''(Oddly, eth0 here seems not to work.)'''
        * wan_ifname=eth1
 1. Edit /etc/init.d/S41wpa and rename it S41wpa-supplicant
    * Remove the -l parameter from nas - it does not work in Supplicant mode (see ["OpenWrtDocs/nas"])
    * Whether this should be run before or after S40network remains to be seen

== Results?? ==

At this point, you should have a connection established to the wireless network (check with iwconfig eth1, wl assoclist, and wl sta_info ''AP MAC address'' - the status should be ASSOCIATED AUTHENTICATED AUTHORIZED).

Unfortunately the last bit -- actually setting up the bridging -- still eludes me.  Using the br0 causes the EAPOL negotiation to come out of the wired side and the wireless side to remain unconnected.

Some forum posts suggest that true bridging will not work due to limitations of 802.11 and that some tricks are required.  One idea is to clone the MAC address of the single machine plugged into the wired side of the bridge on the wireless interface of the bridge.  Of course, this allows only one machine to be connected.  Another idea is to enable proxy ARP and manually route each IP address in the subnet that's active.  This is unfortunate.  I haven't tried either yet.

== Extra notes ==

Using DHCP to obtain an address from the wireless network works, however it takes a ''very long time'' after starting up (and the DMZ light turning off) before it will occur successfully.  This is because the key negotiation for the wireless network does not complete for a while after udhcpc starts up.  Moving the supplicant startup to 38 then sleeping (or waiting for iwconfig to show the connection is up) might be a good idea.
