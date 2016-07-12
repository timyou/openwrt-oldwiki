/!\ '''NOTE:''' This is going to be the new Faq for the stable OpenWrt
White Russian release /!\


[[TableOfContents]]


= Installation =

== Will OpenWrt run on <fill in the blank> ? ==

Please check [:OpenWrtDocs/Hardware] and the [:TableOfHardware] for the list of
supported units.


== How do I identify my hardware version? ==

It's pretty simple, look on the bottom by the model number and there will be a
revision on the Linksys sticker. The exceptions are the v1.0 and the WRT54GS
which don't list their revision. The v1.0 can be easily identified by the 3 LEDs
per port (and a MiniPCI card and AMD flash chip if you open it). In v1.1 they
switched to 1 LED per port (and removed the MiniPCI and switched to an intel flash),
v2.0 brought the change from 125Mhz to 200Mhz and the WRT54GS adds more memory
(total of 32 MB) and flash (8 MB).

If you haven't installed OpenWrt yet, another way of identifying the hardware is to
open the page [http://192.168.1.1/SysInfo.htm] (where {{{192.168.1.1}}} should be
replaced with the IP address of your WRT54G or WRT54GS). The last line in the
output shows the hardware version.


== Which image should I use? ==


== Do I need to run firstboot on every boot? ==

No. {{{firstboot}}} is for formatting the JFFS2 partition on flash and creating the
directory structure; you only need to run it after upgrading the firmware.


== How do I edit files on the SquashFS image? ==

By default all files on the SquashFS image are actually symlinks to the real
(readonly) files over on {{{/rom}}}, to edit a file you will need to delete
the symlink and copy the file from {{{/rom}}}.

Example:

{{{
rm /etc/ipkg.conf
cp /rom/etc/ipkg.conf /etc/ipkg.conf
vi /etc/ipkg.conf
}}}

Now you can edit the files with an text editor.

'''NOTE:''' On JFFS2 images you can edit the files like on every other linux system.

See [:OpenWrtDocs/Using] for details.


== How do I recover / boot in failsafe mode? ==

If you should screw up the JFFS2 part or the network settings in NVRAM you can use
OpenWrt's failsafe mode to recover. The DMZ LED will light up during boot, hold down
the reset button for 1-2 seconds as the DMZ LED lights up to boot into failsafe mode.
While in failsafe mode OpenWrt will not mount the JFFS2 partition and will instead run
entirely from SquashFS and the LAN will be forced to {{{192.168.1.1}}}  with a MAC
address of {{{00:0B:AD:0A:DD:00}}}. If you don't have a DMZ LED, use this procedure:
Plug in the power cable, wait for 3 seconds, then start pressing the reset button and
hold it down for another 10-15 seconds. You should be in failsafe mode, then.

The JFFS2 filesystem can be unlocked and mounted as follows:

{{{
mtd unlock mtd4
mount -t jffs2 /dev/mtdblock/4 /jffs
}}}

/!\ WRT54GS v2.0: Holding down the reset button for 5 seconds during power up will erase
all nvram variables and restore defaults.

'''TIP:''' It's possible that you can't ping or telnet into the router in failsafe mode.
This is because you have old entries in the ARP cache table. You can delete the entries
in the ARP cache with:

On *nix operating systems use:
{{{
arp -d *
}}}

On Windows operating systems open a CMD console and do:
{{{
C:\> arp -d *
}}}


== What TFTP client should I use to flash my Wrt? ==

In GNU/Linux and other *ixes, use the {{{atftp}}} client.

On Windows operating systems use one of the following:
 * tftpd32 from [http://perso.wanadoo.fr/philippe.jounin/tftpd32.html]
 * or the included one (on the CMD console)


== Can I flash the OpenWrt image when I changed the LAN IP? ==

'''NOTE:''' On bootup it's always {{{192.168.1.1}}}, so flash it with
this LAN IP! The default LAN IP address could be different on some
routers.


= Misc =

== Where can I find the FAQ? ==

== How do I change NVRAM settings? ==

== What is left behind, when erasing the flash? ==

== Where can I find packages? ==

== Why isn't a package for ____ available? ==

== How much space is available for the JFFS2 partition? ==

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

Replace {{{aaa.bbb.ccc.ddd}}} with the IP address of your remote Syslog
server where you want to log to.


== How do I have it do something every YYY seconds/minutes? ==

== My Linksys WRT54G and WRT54GS routers seems to reboot or is unstable upon heavy network traffic ==

== What's magic behind /sbin/wifi is doing? ==

== How do I open a WRT54G/WRT54GS? ==

== When using the ssh client from OpenWrt, I get the following message : "no auths methods could be used" ==


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

To save these settings and have the WEP key set each bootup, save the changes to nvram:

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

OpenWrt can be configured as Bridged Client Mode or Routed Client Mode.

For more details on configuring the WRT as a wireless client, see [:ClientModeHowto].


=== Wireless Distribution System (WDS) / Repeater / Bridge ===

This is an ASCII art for what WDS can be useful.

{{{
                / - - - Wireless Clients
               |
INTERNET-----WRT54G_1- - - - - -WRT54G_2 - - - - - Wireless Clients
             | | | |            | | | |
            4 clients          4 clients

----- Cable link
- - - Wlan link
}}}

With WDS you can connect wireless clients to the AP. In client mode this
is not possible.

This is done again by setting up some NVRAM variables.

{{{
nvram set wl0_lazywds=0
nvram set wl0_wds=aa:bb:cc:dd:ee:ff
nvram commit
}}}

Replace {{{aa:bb:cc:dd:ee:ff}}} with the MAC address of the other router you would
like to connect via WDS.

If the other router is running OpenWrt too you can get the MAC address from output of:

{{{
iwconfig eth1
}}}

/!\ '''IMPORTANT:''' Use the correct [:OpenWrtDocs/Configuration#NetworkInterfaceNames:network interface name]
for your hardware.

See [:OpenWrtDocs/Configuration] for details.


=== How do I disable ESSID broadcast? ===

{{{
ifdown wifi
nvram set wl0_closed=1
}}}

After this, you still send out a beacon. This beacon is sent every 100 ms
(0.1 seconds). To change the beacon interval to 1 second you do:

{{{
nvram set wl0_bcn=1000
}}}

After that bring the WIFI interface up again with:

{{{
ifup wifi; /sbin/wifi
}}}

To keep the settings over a reboot run:

{{{
nvram commit
}}}


=== What is the difference between wl0_* and wl_* variables? ===

Use the {{{wl0_}}} variables.

The {{{wl_}}} variables are obsolete and unused.


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


== What are the *.mk files in buildroot? / What options can I change in the Makefile? ==


== Where is the buildroot documentation? ==

See [http://downloads.openwrt.org/docs/buildroot-documentation.html buildroot documentation].
