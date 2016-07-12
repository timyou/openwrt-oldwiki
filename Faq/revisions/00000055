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


== How do I install/flash OpenWrt? ==

See [:http://wiki.openwrt.org/OpenWrtDocs/Installing]


== Do I need to run firstboot on every boot? ==

No. {{{firstboot}}} is for formatting the JFFS2 partition on flash and creating the
directory structure; you only need to run it after upgrading the firmware or if you
like to restore the default filesystem.


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

'''NOTE:''' On JFFS2 images you can edit the files like on every other Linux system.

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

/!\ '''WARNING:''' WRT54GS v2.0: Holding down the reset button for 5 seconds during
power up will erase all NVRAM variables and restore defaults.

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

On bootup it's always {{{192.168.1.1}}}, so flash it with this LAN IP!

'''NOTE:''' The default LAN IP address could be different on some routers.


= Misc =

== Where can I find the FAQ? ==

This is the FAQ; you'd be amazed at how many people ask where the FAQ is,
even after being told that question is answered in the FAQ itself.


== How do I change NVRAM settings? ==

{{{
nvram show
nvram get variable
nvram set variable=value
nvram commit (to save the changes)
}}}

See [:OpenWrtNVRAM].


== What is left behind, when erasing the flash? ==

{{{mtd}}} will leave the bootloader and NVRAM settings untouched.


== Clean up the NVRAM variables ==

If you had installed other firmware before you may have probably more than
400 NVRAM variables.

To cleanup this variables (the safe way) use nbd's NVRAM cleanup script found
at [http://openwrt.inf.fh-brs.de/~nbd/nvram-clean.sh].

{{{
cd /tmp
wget http://openwrt.inf.fh-brs.de/~nbd/nvram-clean.sh
chmod a+x /tmp/nvram-clean.sh
/tmp/nvram-clean.sh
}}}

Watch out the before and after size. That is how much the script cleaned up.

The {{{nvram-clean.sh}}} script is not commiting the changes to NVRAM.
So you have to do this with:

{{{
nvram commit
}}}

The changes the script made take only affect if you reboot or power cycle
the router after committing.


== Where can I find packages? ==

All packages included in the stable White Russian release can be listed with:

{{{
ipkg list | more
}}}

A list of installed packages can be displayed with:

{{{
ipkg list_installed
}}}

'''TIP:''' If there are no package descriptions listed you have to run
{{{ipkg update}}}.


Sites with OpenWrt compatible IPKG packages are listed in [:OpenWrtPackages].


== Why isn't a package for ____ available? ==

Good question. The most likely answer is that nobody has needed that package
yet or that nobody has had time to package it.

 * Wait until the package becomes available
 * Package it yourself (using the [:BuildingPackagesHowTo:OpenWrt SDK])
 * Find/Pay someone to package it for you


== How much space is available for the JFFS2 partition? ==

 * On systems with a 4 MB flash: roughly 2 MB
 * On systems with a 8 MB flash: roughly 6 MB

The actual size allocated to the partition will vary slightly depending on
the OpenWrt build. JFFS2 uses compression, the amount of data that can be
stored on that partition will be higher than the above values.


== How do I reflash / How do I revert back to my previous firmware? ==

Make sure you have set {{{boot_wait=on}}}. To verify this do:

{{{
nvram get boot_wait
}}}

should return {{{on}}}. You can set {{{boot_wait=on}}} to on by doing:

{{{
nvram set boot_wait=on
nvram commit
}}}

When this is done you can follow the [:OpenWrtDocs/Deinstalling] page.


== Does OpenWrt have a web interface (webif) GUI? ==

Not yet. The upcoming OpenWrt White Russian 1.0 release will have
a web interface.

Nbd is currently working on one. The latest release can always be installed
from [http://openwrt.inf.fh-brs.de/~nbd/webif-test_1.ipk] via:

{{{
ipkg install http://openwrt.inf.fh-brs.de/~nbd/webif-test_1.ipk
}}}

'''NOTE:''' This web interface is in development. Basic features should work.
It will only work on a recent OpenWrt White Russian release candidate.

The OpenWrt web interface is based on a set of shell and AWK scripts and
the form processing is done with [http://haserl.sourceforge.net/ haserl].
It uses the BusyBox HTTPD server.

A "Screenshot" is a available at [http://openwrt.inf.fh-brs.de/~nbd/webif/wireless-config.sh.html].


== Why is the OpenWrt firmware so bare? ==

OpenWrt's design philosophy is to not lock the user down to a particular set of
features but rather to provide a base framework which can be endlessly customized
through it's package support and writable JFFS2 filesystem. The firmware itself
contains a minimal "core" filesystem with the intent on giving as much space as
possible to the JFFS2 filesystem; the core provides minimal functionality while
the JFFS2 filesystem allows the user to add software packages and modify the core
scripts. The use of a package system allows the user to customize the set of
features required with regard to available space, without wasting space on unused
features.

As an example, the typical WRT54G contains 4 MB of flash while the WRT54GS contains
8 MB of flash. The typical firmware is intended to fit on a WRT54G, leaving 4 MB of
flash completely unused on the WRT54GS. With OpenWrt, the JFFS2 partition will
inherit the extra 4 MB of space, allowing more packages and thus more features.


== Who maintains OpenWrt? ==

OpenWrt is the collaboration of many people. The two people responsible for the
creation are Gerry Rozema (aka groz) and Mike Baker (aka mbm, or embeem to tivo hacking
fans). The primary (possibly only) maintainer of the OpenWrt project and this website
is mbm, who you can often find lurking in the forums and IRC channel. Due to popular
request there is an amazon wishlist for mbm [http://www.amazon.com/gp/registry/3K14VKJP7FYUJ here].

(Groz is currently missing in action, yet occasionally submits broken CVS code ;) )


== How do I access the syslog messages? ==

For reading syslog messages, use the {{{logread}}} program.

To log to a remote Syslog server set:

{{{
nvram set log_ipaddr=aaa.bbb.ccc.ddd
}}}

Replace {{{aaa.bbb.ccc.ddd}}} with the IP address of your remote Syslog
server where you want to log to.


== How do I have it do something every YYY seconds/minutes? ==

OpenWrt uses {{{crond}}}. So you have to setup a cronjob like on every
Linux system.

See [:HowtoEnableCron] for details.


== My Linksys WRT54G or WRT54GS routers seems to be unstable ==

The core developer nbd wrote a script that should fix this problems.

The script should do exactly what the Linksys firmware does to fix the
instability problems on WRT54G v2.2+, WRT54GS v1.1+.

The problem that's fixed by this script has been reported in several forms:
[[BR]]1) Crashes on high network/wireless load
[[BR]]2) Abnormal program errors
[[BR]]3) Random source/destination ports added to iptables rules with -p tcp

If you have one of these problems, please consider trying out my script at
[http://openwrt.inf.fh-brs.de/~nbd/linksys-fixup.sh].

/!\ '''WARNING:''' Only use this script to set the NVRAM variables on the
listed Linksys routers above. Please do '''NOT''' set the NVRAM variables
or parts of them included in the script manually or on any '''non'''
Linksys router.

To execute the script on the router do:

{{{
cd /tmp
wget http://openwrt.inf.fh-brs.de/~nbd/linksys-fixup.sh
chmod a+x /tmp/linksys-fixup.sh
/tmp/linksys-fixup.sh
}}}

The {{{linksys-fixup.sh}}} script is not commiting the changes to NVRAM.
So you have to do this with:

{{{
nvram commit
}}}

The changes the script made take only affect if you reboot or power cycle
the router after committing.

/!\ '''WARNING:''' It may contain bugs, may not work at all or may even brick
your router.

/!\ '''WARNING:''' It has been reported that even this moderate increase to
{{{clkfreq}}} has caused problems. A WRT54G v2.0 went into endless reboots,
making it practically impossible to reach the console. Have your JTAG cable
ready in any case! Btw. generelly manually overlocking a router using the
{{{clkfreq}}} NVRAM variable is a bad hack/idea. So again, don't overclock
your router manually!

You should also read the
[http://forum.openwrt.org/viewtopic.php?id=2874 The "My router is unstable" thread...]
on the forum.


== What's the magic behind /sbin/wifi is doing? ==

The {{{/sbin/wifi}}} program reads the wireless {{{wl0_}}} settings from
NVRAM and reconfigures the Broadcom wireless driver ({{{wl.o}}}). This is
because the Broadcom wireless driver wants the NVRAM variables in a special
order.

The source code for {{{/sbin/wifi}}} is available in CVS.


== How do I open a WRT54G/WRT54GS? ==

/!\ '''WARNING:''' Opening the case will void your warranty; if you're running
a third party firmware you have already voided your warranty.

Linksys uses a screwless case, the blue front panel holds the case together.
Remove the antennas then pull the blue panel off, the remaining pieces will
slide apart. See [http://voidmain.is-a-geek.net/redhat/wrt54g_revival.html pictures].

The easy way to open the case is to get a firm grip on one of the blue legs
and one of the grey legs and quickly yank apart, it will take some force to
open the WRT54G for the first time.

Some cases have screws.


== When using the SSH client from OpenWrt, I get the following message: "no auths methods could be used" ==

The message {{{no auths methods could be used}}} is related to the following
utilization: {{{dropbear}}} as SSH client and {{{openssh}}} as {{{sshd}}}
server, basically, activating this option in {{{/etc/ssh/sshd_config works}}}:

{{{
PasswordAuthentication yes
}}}


= Networking =

== How do I create a DHCP server? ==

The [http://thekelleys.org.uk/dnsmasq/doc.html dnsmasq] program acts as
DNS and DHCP server in OpenWrt.

By default it hands out IP addresses from {{{192.168.1.100}}} up to
{{{192.168.1.250}}}

To change this you have to set two NVRAM variables.

{{{
nvram set dhcp_start=<start_number>
nvram set dhcp_num=<number_of_hosts>
nvram commit
}}}

and restart {{{dnsmasq}}} with:

{{{
killall -9 dnsmasq; /etc/init.d/S50dnsmasq
}}}


== dnsmasq responds to (local) DHCP requests but not DNS queries. What do I do? ==

== Where should I put custom firewall rules? ==

They go into the file /etc/firewall.user. This file has a view examples in it as well.

Since OpenWrt uses the standard Linux {{{iptables}}} for firewalling a good starting
point for documenation is [http://www.netfilter.org/documentation/].


== How do I use it as a router, instead of a bridge? ==

== How do I set the timezone and make it stick between reboots? ==

OpenWrt stores the timezone in the {{{/etc/TZ}}} file.

For details on configuring your timezone see [:OpenWrtDocs/Configuration].


== What is br0? ==

== What are all these VLANs, how do I get rid of them? ==



== Howto enable WEP ==

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


== How do I use Wi-Fi Protected Access (WPA)? ==

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


== How can I put it in Client Mode? ==

OpenWrt can be configured as Bridged Client Mode or Routed Client Mode.

For more details on configuring the WRT as a wireless client, see [:ClientModeHowto].


== Wireless Distribution System (WDS) / Repeater / Bridge ==

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


== How do I disable ESSID broadcast? ==

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


== What is the difference between wl0_* and wl_* variables? ==

Use the {{{wl0_}}} variables.

The {{{wl_}}} variables are obsolete and unused.



== How do I configure PPPoE? ==

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

== How do I configure PPTP? ==

== How do I configure DHCP? ==



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


== Should I report bugs releated to the buildroot system ==

Yes. If you find any bugs, please use our [http://forum.openwrt.org/ forum] or
send a report to openwrt-devel@openwrt.org or use IRC channel to report. You
can send patches for the bugs as well.

/!\ '''NOTE:''' Changes to the buildroot system or the associated {{{Makefiles}}}
could break the compile process. Please do not submit bug reports against modified
copies of buildroot. Thanks.


== Where is the buildroot documentation? ==

See [http://downloads.openwrt.org/docs/buildroot-documentation.html buildroot documentation].
