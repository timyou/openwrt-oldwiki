/!\ '''NOTE:''' This is going to be the new Faq for the stable OpenWrt
White Russian release /!\


[[TableOfContents]]


= Installation =

== Will OpenWrt run on <fill in the blank> ? ==

== How do I identify my hardware version? ==

== Which image should I use? ==

== Do I need to run firstboot on every boot? ==

== How do I edit files on the filesystem? ==

== How do I recover / boot failsafe? ==

== What TFTP client should I use to flash my Wrt? ==


= Misc =

== How do I change NVRAM settings? ==

== Where can I find packages? ==

== Why isn't a package for ____ available? ==

== How do I reflash / How do I revert back to my previous firmware? ==

== Does OpenWrt have a web interface (webif) GUI? ==

== Why is the OpenWrt firmware so bare? ==

== Who maintains OpenWrt? ==

== How do I open a WRT54G/WRT54GS ? ==

== How do I access the syslog messages? ==

For reading syslog messages, use the {{{logread}}} program.

To log to a remote Syslog server set:

{{{
nvram set log_ipaddr=aaa.bbb.ccc.ddd
}}}


== How do I have it do something every YYY seconds/minutes? ==

== My WRT54Gv2.2 seems to reboot upon heavy wlan traffic ==


= Networking =

== Misc ==

=== How do I create a DHCP server? ===

=== dnsmasq responds to (local) DHCP requests but not DNS queries. What do I do? ===

=== How do I use it as a router, instead of a bridge? ===

=== How do I set the timezone and make it stick between reboots? ===

=== What is br0? ===

=== What are all these vlans, how do I get rid of them? ===


== Local Area Network (LAN) ==


== Wireless ==

=== Howto enable WEP ===

{{{
ifdown wifi
nvram set wl0_wep=enabled
nvram set wl0_key=1
nvram set wl0_key1=DEADBEEF12345DEADBEEF12345
ifup wifi; /sbin/wifi
}}}

The WEP key {{{wl0_key1}}} must be in '''HEX''' format (allowed HEX digits are 0-9a-f).
The length of the key must be exact 26 HEX digits than you have a 128 bit WEP key.
Avoid using WEP keys with 00 at the end, otherwise the driver won't be able to detect
the key length correctly.

To save these settings and have the wep key set each bootup, save the changes to nvram:

{{{
nvram commit
}}}

See [:OpenWrtDocs/Configuration] for details.


=== How do I use Wi-Fi Protected Access (WPA)? ===

You have to install the {{{nas}}} package (which provides WPA encryption) if not already
done with:

{{{
ipkg install nas
}}}

Now set some NVRAM variables:

{{{
wl0_akm=psk
wl0_crypto=tkip
wl0_wpa_psk=<your_preshared_key>
}}}

Replace {{{<your_preshared_key>}}} to appropriate.

'''NOTE:''' The length of the {{{wl0_wpa_psk}}} NVRAM variable must be at least 8 chars
up to 63 chars.

For details and howto configure WPA2 or AES encryption see [:OpenWrtDocs/Configuration].


=== How can I put it in Client Mode? ===

See [:ClientModeHowto].


=== How can I expand my network (aka repeater) with two wrt54g(s) devices ===

=== Creating a repeater with WDS ===

=== How do I disable ESSID broadcast? ===

=== Can I eliminate BSSID partitioning in a network of OpenWrt nodes? ===

=== What is the difference between wl0_* and wl_* variables? ===


== Internet connection (WAN) ==

=== How do I configure PPPoE? ===

That's ease. Just set some NVRAM variables.

/!\ '''IMPORTANT:''' Use the correct [:OpenWrtDocs/Configuration#NetworkInterfaceNames:network interface name]
for your hardware version in the {{{pppoe_ifname}}} NVRAM variable.

{{{
nvram set wan_ifname=ppp0
nvram set wan_proto=pppoe
nvram set ppp_mtu=1492 # The MTU of your ISP
nvram set pppoe_ifname=vlan1
nvram set ppp_username=<your_isp_login>
nvram set ppp_passwd=<your_isp_password>
nvram commit
}}}

When done bring up the WAN connection with:

{{{
ifup wan
}}}

See [:OpenWrtDocs/Configuration] for details.

=== How do I configure PPTP? ===

=== How do I configure DHCP? ===



= Development =


== How do I create a package? ==

See [:BuildingPackagesHowTo].


== Requirements for compiling OpenWrt ==

For compiling OpenWrt (from CVS or from the tarball, both the White Russian stable release)
you need at least a recent GNU/Linux distribution and the following programs installed:

{{{
gcc, g++, binutils, patch, bzip2, flex, bison, make, gettext, unzip, libz-dev and
libc headers
}}}

When you get error messages related to libnvram, upgrade {{{make}}} to version 3.80.
If that is not working as expected patch {{{make}}} 3.80 with the
[http://ftp.debian.org/debian/pool/main/m/make/make_3.80-9.diff.gz Debian make patches].

Approximately required disc space for compiling OpenWrt:

||'''Branch'''||'''Min.'''||'''Max.'''||
||Stable Source||1.5 GB||3.5 GB||
||Development||x||x||


== Where is the CVS repository ? ==

'''Stable Release'''

At the moment we have no stable supported release. You can get release candidates for
the next stable OpenWrt release in binary format: [http://downloads.openwrt.org/whiterussian/].

'''Stable Source'''

The stable source code can be found in the above directory or from our CVS repository.
This is not recommended for beginners; we will not troubleshoot failed compiles.

{{{
cvs -d:pserver:anonymous@openwrt.org:/openwrt -z3 co -r whiterussian openwrt
}}}

Viewcvs is available for [http://openwrt.org/cgi-bin/viewcvs.cgi/openwrt/?only_with_tag=whiterussian#dirlist browsing]
the stable source CVS branch.

'''Development'''

Development take place in CVS. You get the source via:

{{{
cvs -d:pserver:anonymous@openwrt.org:/openwrt -z3 co openwrt
}}}

Viewcvs is available for [http://openwrt.org/cgi-bin/viewcvs.cgi/openwrt/?only_with_tag=HEAD#dirlist browsing]
the developmant CVS branch.

If you find any bugs, please use our [http://forum.openwrt.org/ forum] or IRC channel
to report.


== Where is the buildroot documentation? ==

See [http://downloads.openwrt.org/docs/buildroot-documentation.html buildroot documentation].
