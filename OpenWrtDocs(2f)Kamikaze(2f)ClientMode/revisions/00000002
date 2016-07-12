#pragma section-numbers off
||<tablebgcolor="#f1f1ed" tablewidth="40%" tablestyle="margin: 0pt 0pt 1em 1em; float: right; font-size: 0.9em;"style="padding: 0.5em;">[[TableOfContents]]||
= Client Mode Wireless =
== AP without authentication (open) ==
/etc/config/wireless

{{{
  # This section is chipset specific
  # Do not copy it for your own use
  # config wifi-device      <dev>
  #   ...

  config wifi-iface
      option device       <dev>
  #   Set this to the /etc/config/network network that it's linked to
  #   option network      <network>
  #   "sta" means client mode.
      option mode         "sta"
      option ssid         <network name>
}}}
== AP using WEP ==
Using WEP in client mode is simple; two more options need to be set:

{{{
  config wifi-iface
      ...
      option encryption   "wep"
      option key          <encryption key>
}}}
== AP using WPA/WPA2 ==
WPA requires a "supplicant" -- that is, code that deals with the whole encryption and authentication dealie.  While some have had success with the proprietary Broadcom chipset and the wpa_supplicant package (more on that in a moment), others have had to utilize the Broadcom proprietary supplicant, "nas" [[OpenWrtDocs/nas]] to get this stuff working -- see section below.  Don't blame me, man, I didn't do it.

=== wpa_supplicant ===
wpa_supplicant is the tool that deals with AP authentication, reconnects, etc.  It can even be configured to scan and select APs (useful for hidden APs and APs broadcasting multiple ESSIDs from a single BSSID).  Among [http://hostap.epitest.fi/wpa_supplicant/ other chipets], it supports the two wireless chipsets supported by OpenWRT, Atheros and the Broadcom wl.o binary.

It is available as a precompiled package in Kamikaze 7.09, and is in the "Network" category of buildroot's {{{make menuconfig}}}.

Note: wpa_supplicant.conf should have permissions of 600 and ownership of root:root.

==== Example /etc/wpa_supplicant.conf ====
{{{
ctrl_interface=/var/run/wpa_supplicant
ctrl_interface_group=0
# Obviously, different networks will require different options.  The wpa_supplicant documentation covers them
# This is what most Radius authentication (corporate, school, etc) networks look like
network={
        ssid="RadiusAuthNetwork"
        key_mgmt=WPA-EAP
        pairwise=CCMP TKIP
        group=CCMP TKIP
        eap=PEAP TLS
        identity="<username>"
        password="<password>"
        phase2="auth=MSCHAPV2"
        priority=10
}
# wpa_supplicant supports multiple networks, hence the "priority" option
# it also supports open APs
network={
        ssid="OpenAP"
        key_mgmt=NONE
        priority=5
}
# WPA-PSK/TKIP
network={
        ssid="example wpa-psk network"
        key_mgmt=WPA-PSK
        proto=WPA
        pairwise=TKIP
        group=TKIP
        psk="secret passphrase"
}
}}}
More examples can be found at http://hostap.epitest.fi/wpa_supplicant/ down at the bottom

==== Running WPA Supplicant ====
WPA supplicant is run like this (for an Atheros device): {{{wpa_supplicant -d -c /etc/wpa_supplicant.conf -i ath0 -D wext}}}

Note: having wpa_supplicant interact with madwifi using the Linux wireless extensions (-d wext) is strongly recommended by the madwifi developers, and direct ioctl access (-d madwifi) is discouraged.

-B sends it to the background (use this once you get it working) -d increases debugging level

=== Using nas (an example with Kamikaze & Broadcom) ===
On Kamikaze, you can use:

{{{
nas -P /tmp/nas.lan.pid -l br0 -H 34954 -i wl0 -A -m 4 -k MYKEY -s MYSSID -w 4 -g 3600
}}}
to get a broadcom chipset (such as the one on the Linksys series of routers) to work.

If you wish, you can even start this up when you reboot based on your config files.  Imagine that! ;-)

Cut and paste this snippet to create a startup script:

{{{
cat <<EOF > /etc/init.d/nas
#!/bin/sh /etc/rc.common
## @(#) - /etc/init.d/nas - start the nas proprietary supplicant with /etc/config/wireless
## @(#) - /etc/init.d/nas - Blame it all on Jonathan Feldman jf@feldman.org
START=55
start() {
# ok, inefficient to call awk twice but I'm lazy tonight. :-P
#
MYSSID=$(awk '($1 == "option") && ($2 == "ssid") {
  gsub("['\'']","",$3); print $3}' </etc/config/wireless)
MYKEY=$(awk '($1 == "option") && ($2 == "key") {
  gsub("['\'']","",$3); print $3}' < /etc/config/wireless)
nas -P /tmp/nas.lan.pid -l br0 -H 34954 -i wl0 -A -m 4 -k $MYKEY -s $MYSSID -w 4 -g 3600 &
}
stop() {
        killall nas
}
EOF
ln -s /etc/init.d/nas S55nas
sync

}}}
== Bridged and routed client modes ==
There are no bridged and routed modes on Kamikaze, per se.  Instead, multiple interfaces are bridged with an entry in /etc/config/network like this:

{{{
  config interface     <network>
      option type     "bridge"
      option ifname    "eth0.0"
      ...
}}}
Then in /etc/config/wireless, set the network to the same network specified in the bridge:

{{{
config wifi-device  <type>
        ...
config wifi-iface
        ...
        option network  <network>
}}}
Alternatively, but a little less flexibly, you can use this line in /etc/config/network:

{{{
      # athx for Atheros, Or wl0 for Broadcom
      option ifname    "eth0.0 ath0"
}}}
For routed mode, the wireless device needs to be used in a normal network configuration in /etc/config/network.  Then, iptables rules are used to forward packets between the networks.  The default gateway on each network (this is routing; you're connecting two networks together) needs to forward packets destined for the other network to the  wifi router, or each host on each network needs to know that the wifi router is the router for packets to the respective network.

== Finding networks ==
Both Broadcom and Atheros chipsets support scanning with the iwlist command.  This command will scan all interfaces for networks:

{{{
iwlist scanning
}}}
== Useful Commands ==
 * ifconfig
 * iwconfig
 * wpa_cli
== Automated Script for Fonera and Meraki ==
/!\ '''These scripts are third party content. They are not released or supported by the !OpenWrt developers.'''

/!\ '''These scripts are only compatible with Kamikaze, not White Russian'''

'''For Fonera and Meraki Mini (or related) routers only.'''

Read the instructions and get the tar.gz package from here http://fon.testbox.dk/packages/NEW/LEGEND4.5/clientscript/

That's it. The package of scripts self-installs and will ask you questions to configure your wired and wireless connections. Your current configuration will be backed up and can be restored with the "aprestore" command. Type in "clientmode" after installation to configure client mode. This is currently the easiest and most complete means of having client mode on an Atheros router.  They are included in the Legend Rev4.5 firmware, which will soon be released on the site above.

CategoryKamikaze
