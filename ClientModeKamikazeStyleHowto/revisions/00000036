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
WPA requires a program that interfaces with the driver called a supplicant.  There are two supplicants available for OpenWRT (and Linux, in general): wpa_supplicant and xsupplicant.  Xsupplicant supports both Atheros and Broadcom devices (e.g. WRT54G), while wpa_supplicant supports Atheros (among other chipsets), but not Broadcom.

=== wpa_supplicant ===

wpa_supplicant is available as a package in Kamikaze 7.09, but it might not have support for MadWifi (the Atheros driver).  You need to obtain the OpenWRT source, edit the config file, and build the wpa_supplicant package to get MadWifi support. If you run `make menuconfig` you can build wpa_supplicant by marking it in the Network category.

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
WPA supplicant is run like this (for an Atheros device):
{{{wpa_supplicant -d -c /etc/wpa_supplicant.conf -i ath0 -D wext}}}

Note: having wpa_supplicant interact with madwifi using the Linux wireless extensions (-d wext) is strongly recommended by the madwifi developers, and direct ioctl access (-d madwifi) is discouraged.

-B sends it to the background (use this once you get it working)
-d increases debugging level

=== xsupplicant ===
Info needed

Maybe it is not possible at all to use WPA together with the proprietary Broadcom nas driver, see this [http://thread.gmane.org/gmane.network.wireless.open1x.xsupplicant.general/462 message from xsupplicant's main developer], Chris Hessing.

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

== Automated Script for Fonera and Meraki ==
/!\ '''These scripts are third party content. They are not released or supported by the !OpenWrt developers.'''

/!\ '''These scripts are only compatible with Kamikaze, not White Russian'''

'''For Fonera and Meraki Mini (or related) routers only.'''

Read the instructions and get the tar.gz package from here http://fon.testbox.dk/packages/NEW/LEGEND4.5/clientscript/

That's it. The package of scripts self-installs and will ask you questions to configure your wired and wireless connections. Your current configuration will be backed up and can be restored with the "aprestore" command. Type in "clientmode" after installation to configure client mode. This is currently the easiest and most complete means of having client mode on an Atheros router.  They are included in the Legend Rev4.5 firmware, which will soon be released on the site above.

== Useful Commands ==
 * ifconfig
 * iwconfig
 * wpa_cli
'''List of pages in this category:'''

[[FullSearch()]]

----
 . CategoryCategory
