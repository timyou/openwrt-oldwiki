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

=== How do I use Wi-Fi Protected Access (WPA)? ===

=== How can I put it in Client Mode? ===

=== How can I expand my network (aka repeater) with two wrt54g(s) devices ===

=== Creating a repeater with WDS ===

=== How do I disable ESSID broadcast? ===

=== Can I eliminate BSSID partitioning in a network of OpenWrt nodes? ===

=== What is the difference between wl0_* and wl_* variables? ===


== Internet connection (WAN) ==

=== How do I configure PPPOE? ===

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
