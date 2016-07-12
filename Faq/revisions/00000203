'''New FAQ for the stable !OpenWrt White Russian release candidates.'''

[[TableOfContents]]
= Installation =
== Will OpenWrt run on <fill in the blank> ? ==
Please check ["OpenWrtDocs/Hardware"] and the TableOfHardware for the list of supported units.

== How do I identify my hardware version? ==
The model and version numbers are always printed on the unit.

'''Linksys models'''

For Linksys models look on the bottom for a silver and black linksys sticker and find the words "Model No". The model number will be printed followed by a "vN.N" where "N.N" is the version. The exception to this is the v1.0 revisions, "v1.0" is never printed; if you don't see a version number it's a v1.0.

If you haven't installed !OpenWrt yet, another way of identifying the hardware is to open the page http://192.168.1.1/SysInfo.htm (where {{{192.168.1.1}}} should be replaced with the IP address of your WRT54G or WRT54GS). The last line in the output shows the hardware version.

== Which image should I use? ==
'''Deciding on a filesystem layout'''

Both the SquashFS and JFFS2 filesystems use heavy compression to save disk (flash) space. The choice of layouts really depends on usage patterns. At this point, the recommended install is the SquashFS version which will provide you with failsafe mode and a slightly better compression ratio than the JFFS2 partitions. Should you feel the need to switch over to JFFS2 later, the {{{jffs2root}}} script can be run -- the reverse can't be said.

See [http://downloads.openwrt.org/whiterussian/00-README 00-README].

== How do I install/flash OpenWrt? ==
'''NOTE:''' Before you install !OpenWrt make sure you have at least basic GNU/Linux knowledge and *nix shell skills.

'''TIP:''' You can flash the White Russian images ({{{*.bin}}}) directly from the other web interfaces now. It should to be safe even without {{{boot_wait=on}}}. But there is no garantee it will work.

See ["OpenWrtDocs/Installing"].

== Do I need to run firstboot on every boot? ==
No. {{{firstboot}}} is for formatting the JFFS2 partition on flash and creating the directory structure; you only need to run it after upgrading the firmware or if you like to restore the default filesystem.

'''NOTE:''' The {{{firstboot}}} script doesn't do anything if you're using one of the JFFS2 only images.

== How do I edit files on the SquashFS image? ==
By default all files on the SquashFS image are actually symlinks to the real (readonly) files over on {{{/rom}}}, to edit a file you will need to delete the symlink and copy the file from {{{/rom}}}.

Example:

{{{
rm /etc/ipkg.conf
cp /rom/etc/ipkg.conf /etc/ipkg.conf
vi /etc/ipkg.conf
}}}

Now you can edit the files with an text editor.

'''NOTE:''' On JFFS2 images you can edit the files like on every other Linux system.

See ["OpenWrtDocs/Using"] for details.

== How do I recover / boot in failsafe mode? ==
See ["OpenWrtDocs/Troubleshooting"].

== What TFTP client should I use to flash my Wrt? ==
In GNU/Linux and other *ixes, use the {{{atftp}}} client.

On Windows operating systems use one of the following:

 * tftpd32 from http://perso.wanadoo.fr/philippe.jounin/tftpd32.html
 * or the [http://martybugs.net/wireless/openwrt/flash.cgi one included with Windows] (from the CMD console)

== Can I flash the OpenWrt image when I changed the LAN IP? ==
Linksys routers are always 192.168.1.1 for the bootloader's TFTP. See ["OpenWrtDocs/Installing"] for more information.

== How do I convert a .bin image to .trx to use with mtd? ==
"You need to convert the bin (eg. openwrt-wrt54g-squashfs.bin) file to a trx file before reflashing"

'''WRONG!''' The openwrt-brcm-squashfs.trx is a generic trx file that will work on any supported broadcom platform. The openwrt-wrt54g-squashfs.bin is just "bin header + openwrt-brcm-squashfs.trx', the bin header just contains the firmware version number and what models the firmware can be loaded on; the bin header is only used for verification before writing the trx data to the flash. The mtd utility writes the given file to flash without verifying it; use one of the openwrt-brcm-squashfs.trx when using mtd. Converting the openwrt-wrt54g-squashfs.bin file back to a trx is just plain ignorant.

= Misc =
== Where can I find the FAQ? ==
This is the FAQ; you'd be amazed at how many people ask where the FAQ is, even after being told that question is answered in the FAQ itself.

== When should I NOT install OpenWrt? ==
Please do '''NOT''' install !OpenWrt if you don't know anything about GNU/Linux and shells.

== How do I change NVRAM settings? ==
{{{
nvram show
nvram get variable
nvram set variable=value
nvram commit (to save the changes)
}}}

'''TIP:''' Use quotes when you have a list of MAC addresses or interface names separated by space.  For example:

{{{
nvram set variable="aa:bb:cc:dd:ee:ff aa:bb:cc:dd:ee:ff"
}}}

See ["OpenWrtNVRAM"].

== How to create a NVRAM dump for debugging? ==
Sometimes it's useful to have a dump of the NVRAM variables to show them other people for debugging. This can be done with:

{{{
nvram show 2>&1 | sort | more
}}}

or even:

{{{
strings /dev/nvram | sort | more
}}}

{{{sort}}} will sort the list alphabetically to make it easier to read. Use {{{more}}} to list the output page by page. You can also save the dump into a text file. Use {{{> /tmp/nvram-dump.txt}}} instead of {{{more}}}. Then SCP the file to another computer.

'''NOTE:''' Do '''NOT''' post the dump directly into the IRC channel, for that use a pastebin service like [http://www.pastebin.ca/ pastebin.ca] or [http://www.pastebin.com/ pastebin.com]. Only post the URL on IRC.

== Where should I send bug reports? ==
Please send reproducible bugs to our [http://dev.openwrt.org/report ticket system].

== How do I find out the installed OpenWrt version ==
Check if you have a file {{{/etc/banner}}}. Do

{{{
cat /etc/banner
}}}

and watch for a line like this:

{{{
WHITE RUSSIAN (RC5) -------------------------------
}}}

If you don't have that file execute

{{{
busybox 2>&1 | grep -i ^busybox
}}}

{{{
BusyBox v1.00 (2005.10.10-12:42+0000) multi-call binary
}}}

Your version is based on the reported date where !BusyBox has been compiled.

== What is left behind when the flash is erased? ==
{{{mtd}}} will leave the bootloader and NVRAM settings untouched.

== How do I clean up the NVRAM variables (the safe way)? ==
If you have used other firmware in the past you probably have more than 400 NVRAM variables. Most of these NVRAM variables are not necessary for !OpenWrt. You can safely delete them with the {{{nvram-clean.sh}}} script and have a more readable NVRAM dump.

To safely clean up these variables use nbd's NVRAM cleanup script found at http://openwrt.inf.fh-brs.de/~nbd/nvram-clean.sh.

{{{
cd /tmp
wget http://openwrt.inf.fh-brs.de/~nbd/nvram-clean.sh
chmod a+x /tmp/nvram-clean.sh
/tmp/nvram-clean.sh
}}}

The before and after sizes will show you how much space was recovered.

The {{{nvram-clean.sh}}} script does not commit the changes to NVRAM so you will have to do this manually with:

{{{
nvram commit
}}}

== How often can I write on the flash chip? ==
Flash devices can be written to, at minimum, anywhere between 100,000 and 1,000,000 times (according to the manufacturers).

== Where can I find packages? ==
All packages included in the stable White Russian release can be listed with:

{{{
ipkg list | more
}}}

A list of installed packages can be displayed with:

{{{
ipkg list_installed
}}}

'''TIP:''' If there are no package descriptions listed you have to run {{{ipkg update}}}.

== Why isn't a package for ____ available? ==
Good question. The most likely answer is that nobody has needed that package yet or that nobody has had time to package it.

 * Wait until the package becomes available
 * Package it yourself (using the [:BuildingPackagesHowTo:OpenWrt SDK])
 * Find/Pay someone to package it for you

== How much space is available for the JFFS2 partition? ==
 * On systems with a 4 MB flash: roughly 2 MB
 * On systems with a 8 MB flash: roughly 6 MB

The actual size allocated to the partition will vary slightly depending on the !OpenWrt build. JFFS2 uses compression, the amount of data that can be stored on that partition will be higher than the above values.

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

When this is done you can follow the ["OpenWrtDocs/Deinstalling"] page.

== Does OpenWrt have a web interface? ==
'''Yes.''' The {{{default}}} and {{{pptp}}} optimized images will have the web interface (called !OpenWrt Administrative Console or webif for short) integrated.

The !OpenWrt web interface is based on a set of shell and awk scripts and the form processing is done with [http://haserl.sourceforge.net/ haserl]. It uses the !BusyBox HTTPD server.

'''TIP:''' You still can configure everything in the pure CLI (command line interface) too. If you prefer this way than do so. When you like images without the haserl and webif packages use either the {{{micro}}} image or create your own images using the !OpenWrt [:ImageBuilderHowTo:Image Builder].

== Why is the OpenWrt firmware so bare? ==
!OpenWrt's design philosophy is to not lock the user down to a particular set of features but rather to provide a basic framework which can be endlessly customized through it's package support and writable JFFS2 filesystem. The firmware itself contains a minimal "core" filesystem with the intent on giving as much space as possible to the JFFS2 filesystem; the core provides minimal functionality while the JFFS2 filesystem allows the user to add software packages and modify the core scripts. The use of a package system allows the user to customize the set of features required with regard to available space, without wasting space on unused features.

As an example, the typical WRT54G contains 4 MB of flash while the WRT54GS contains 8 MB of flash. The typical firmware is intended to fit on a WRT54G, leaving 4 MB of flash completely unused on the WRT54GS. With !OpenWrt, the JFFS2 partition will inherit the extra 4 MB of space, allowing more packages and thus more features.

== Who maintains OpenWrt? ==
!OpenWrt is the collaboration of many people. The two people responsible for the creation are Gerry Rozema (aka groz) and Mike Baker (aka mbm, or embeem to tivo hacking fans). The core developers with write access to the subversion repository are:

{{{
Mike Baker <mbm>
Imre Kaloz <Kaloz>
Waldemar Brodkorb <wbx>
Nicolas Thill <Nico>
Felix Fietkau <nbd>
Florian Fainelli <florian>
Oliver Ertl <olli>
}}}

== How do I access the syslog messages? ==
Use the {{{logread}}} program to read syslog messages. Syslog stores the messages in the Wrt's RAM. When the specified part of the RAM gets full syslog deletes the old messages.

To log to a remote syslog server use:

{{{
nvram set log_ipaddr=aaa.bbb.ccc.ddd
}}}

Replace {{{aaa.bbb.ccc.ddd}}} with the IP address of your remote syslog server where you want to log to.

See MiniHowtos for details on remote logging.

== How do I have it do something every YYY seconds/minutes? ==
!OpenWrt uses {{{crond}}}. So you have to setup a cronjob like on every Linux system.

See HowtoEnableCron for details.

== What does /sbin/wifi do? ==
The {{{/sbin/wifi}}} program reads the wireless {{{wl0_}}} settings from NVRAM and reconfigures the Broadcom wireless driver ({{{wl.o}}}). This is because the Broadcom wireless driver wants the NVRAM variables in a special order.

The source code for {{{/sbin/wifi}}} is available in SVN. Browse the [https://dev.openwrt.org/file/branches/whiterussian/openwrt/package/wificonf/wificonf.c wificonf.c source].

== How do I open a WRT54G/WRT54GS? ==
/!\ '''WARNING:''' Opening the case will void your warranty.  Note that if you're running third party firmware you've already voided the warranty. ;-)

For the most part Linksys uses a screwless case, although some models (unspecified as to exactly which ones) do have screws.  On the screwless cases the blue front panel holds everything together. Remove the antennas then pull the blue panel off.  The remaining pieces will then slide apart. See [http://voidmain.is-a-geek.net/redhat/wrt54g_revival.html pictures].

The easiest way to open the case is to get a firm grip on one of the blue legs and one of the grey legs and quickly yank apart.  It will take some force to open the WRT54G for the first time, so be gentle but firm.  Apply enough force, but not too much.

== When using the SSH client from OpenWrt, I get the following message: "no auths methods could be used". ==
The message {{{no auths methods could be used}}} is related to the following utilization: {{{dropbear}}} as SSH client and {{{openssh}}} as {{{sshd}}} server, basically, activating this option in {{{/etc/ssh/sshd_config}}} works:

{{{
PasswordAuthentication yes
}}}

## ##################################################
= Networking =
== How do I create a DHCP server? ==
The [http://thekelleys.org.uk/dnsmasq/doc.html dnsmasq] program acts as DNS and DHCP server in !OpenWrt. By default it hands out IP addresses from

{{{192.168.1.100}}} to {{{192.168.1.250}}}.

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

For more details on howto configure static IP addresses see ["OpenWrtDocs/dnsmasq"].

== Where should I put custom firewall rules? ==
They go into the file {{{/etc/firewall.user}}}. This file has a few examples in it as well. Don't forget to rerun the {{{/etc/firewall.user}}} scirpt to activate your changes.

{{{/etc/firewall.user}}} gets called from the {{{/etc/init.d/S45firewall}}} script on each reboot.

Since !OpenWrt uses the standard Linux {{{iptables}}} for firewalling a good starting point for documentation is http://www.netfilter.org/documentation/.

'''TIP:''' If you install {{{qosfw-scripts}}} than it's easier to configure port forwarding.

== How do I configure QoS aka traffic shaping in OpenWrt? ==
QoS in !OpenWrt is based on {{{tc}}}, HFSC and [http://l7-filter.sourceforge.net/ Layer 7 filters]. This script is only shaping on your uplink. The QoS package only works in White Russian RC5 and later version. With the {{{qos-scripts}}} package (version 0.4 and later) it's also possible to setup simple port forwarding rules in in the config file.

Download and install the {{{qos-scripts}}} package from http://downloads.openwrt.org/people/nbd/qos/

Then edit {{{/etc/config/qos-wan}}}. This file has a number of examples and the syntax description in it. Be sure to uncomment the {{{option:enabled}}} line and set the {{{option:upload}}} and {{{option:download}}} correctly.

If you don't configure port forwarding in {{{/etc/config/qos-wan}}} than you can make use {{{/etc/firewall.user}}} as normal for iptables rules.

If you're using L7 filters in the config file you have to install the {{{iptables-mod-filter}}} package. This package contains a few L7 filters. Alternativly you can download extra filters from [http://l7-filter.sourceforge.net/protocols Layer 7 filters] and save the {{{.pat}}} files into the {{{/etc/l7-protocols}}} directory.

Finally start QoS with

{{{
ifup wan
}}}

This calls the QoS script via the hotplug code.

To show the QoS related rules execute:

{{{
iptables -L -v -t mangle
}}}

== How do I route wireless instead of a bridging LAN and WIFI? ==
See ["OpenWrtDocs/Configuration"].

== How do I set the timezone and make it stick between reboots? ==
!OpenWrt stores the timezone in the {{{/etc/TZ}}} file.

'''NOTE:''' Most routers does '''NOT''' have a CMOS hardware clock. That means you have to sync the time after every reboot.

For details on configuring your timezone see ["OpenWrtDocs/Configuration"].

== What is br0? ==
By default the LAN ports and the wireless interface are bridged together as the virtual interface {{{br0}}}, allowing the LAN and wireless to share the same IP range.

== How do I configure MAC address cloning in OpenWrt? ==
To enable MAC address cloning in !OpenWrt on the WAN interface you have to set the {{{wan_hwaddr}}} NVRAM variable.

{{{
nvram set wan_hwaddr="aa:bb:cc:dd:ee:ff"
nvram commit
}}}

After that reboot your Wrt router.

{{{
reboot
}}}

Now check the MAC address on the your WAN interface with the {{{ifconfig}}} command. Your WAN interface should have the MAC address which you set in the NVRAM variable above.

== How do I enable WEP encryption? ==
{{{
ifdown wifi
nvram set wl0_wep=enabled
nvram set wl0_key=1
nvram set wl0_key1=deadbeef12345deadbeef12345
ifup wifi
/sbin/wifi
}}}

The WEP key {{{wl0_key1}}} must be in '''HEX''' format (allowed HEX digits are 0-9 and a-f lower case). The length of the key must be exact 26 HEX digits than you have a 128 bit WEP key. Avoid using WEP keys with 00 at the end, otherwise the driver won't be able to detect the key length correctly.

To save these settings and have the WEP key set each bootup, save the changes to NVRAM:

{{{
nvram commit
}}}

See ["OpenWrtDocs/Configuration"] for details.

== How do I use WiFi Protected Access (WPA)? ==
You have to install the {{{nas}}} package (which provides WPA encryption) if not already done with:

{{{
ipkg install nas
}}}

Now set some NVRAM variables:

{{{
nvram set wl0_akm=psk
nvram set wl0_crypto=tkip
nvram set wl0_wpa_psk=<your_preshared_key>
nvram commit
}}}

Replace {{{<your_preshared_key>}}} to appropriate.

'''NOTE:''' The length of the {{{wl0_wpa_psk}}} NVRAM variable must be at least 8 chars up to 63 chars.

Start WPA with

{{{
/etc/init.d/S41wpa
}}}

Check with the {{{ps}}} command if there is a {{{nas}}} process running. If it's not working try rebooting the router.

For details and howto configure WPA2 or AES encryption see ["OpenWrtDocs/Configuration"].

== How can I enable Client Mode? ==
OpenWrt can be configured as Bridged Client Mode or Routed Client Mode.

For more details on configuring the Wrt as a wireless client, see ClientModeHowto.

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

With WDS you can connect wireless clients to all APs. In client mode this is not possible.

For connection of two AP together, both machines has be set up.

{{{
nvram set wl0_lazywds=0
nvram set wl0_wds=aa:bb:cc:dd:ee:ff
nvram commit
ifup wifi; /sbin/wifi
}}}

Replace {{{aa:bb:cc:dd:ee:ff}}} with the MAC address of the router you would like to connect via WDS. On WRT54G_1 set MAC of WRT54G_2 and on WRT54G_2 set MAC of WRT54G_1.

If the other router is running OpenWrt too you can get the MAC address from output of:

{{{
iwconfig eth1
}}}

/!\ '''IMPORTANT:''' Use the correct [:OpenWrtDocs/Configuration#NetworkInterfaceNames:network interface name] for your hardware.

See ["OpenWrtDocs/Configuration"] for details.

== How do I disable ESSID broadcast? ==
This can be done easily with

{{{
nvram set wl0_closed=1
/sbin/wifi
}}}

To keep the settings over a reboot run:

{{{
nvram commit
}}}

== Why does it report 255 mW / 31 dBm for the wireless txpwr? ==
It lies.

The txpwr is not actually 255, 255 is just the target value. The actual value will be capped by the driver to a maximum of maximum of {{{pa0maxpwr}}} (unless you turn on the override). This is the exact same way it's handled in the OEM firmwares. (Chances are that we'll just set it to {{{pa0maxpwr}}} in future releases to finally kill this question).

== Can I adjust the transmit power? ==
Yes, but cranking the power to the maximum won't help you any. You might transmit farther but the noise level will be higher (and will probably bleed into the neighbouring channels; that looks like [http://wl500g.info/showthread.php?t=12&page=2 this] then) and your recieve sensitivity won't be improved any, limiting your distance. If you want better range go buy better antennas.

== What is the difference between wl0_* and wl_* variables? ==
Use the {{{wl0_*}}} variables. The {{{wl_*}}} variables are obsolete and unused.

== How do I configure PPPoE for Internet access? ==
That's easy. Just set some NVRAM variables and plug your DSL modem into the WAN port.

/!\ '''IMPORTANT:''' Use the correct [:OpenWrtDocs/Configuration#NetworkInterfaceNames:network interface name] for your hardware version in the {{{pppoe_ifname}}} NVRAM variable.

{{{
nvram set wan_ifname=ppp0
nvram set wan_proto=pppoe
nvram set ppp_idletime=10
nvram set ppp_mtu=1492 # The MTU of your ISP
nvram set ppp_passwd=<your_isp_password>
nvram set ppp_redialperiod=15
nvram set ppp_username=<your_isp_login>
nvram set pppoe_ifname=<your_WAN_interface_name>
nvram commit
}}}

When done bring up the WAN connection with:

{{{
ifup wan
}}}

See ["OpenWrtDocs/Configuration"] for details.

== How do I configure DHCP for internet access? ==
By default !OpenWrt will listen on the WAN interface for a another DHCP server in your LAN. Use this kind of internet access f.e. if you have a cable modem.

When you have configured PPPoE before than set the following NVRAM variables to activate DHCP on the WAN interface.

{{{
nvram set wan_ifname=<your_WAN_interface_name>
nvram set wan_proto=dhcp
nvram commit
}}}

/!\ '''IMPORTANT:''' Use the correct [:OpenWrtDocs/Configuration#NetworkInterfaceNames:network interface name] for your hardware.

When done bring up the WAN connection with:

{{{
ifup wan
}}}

== How do I configure PPTP for internet access? ==
Install the {{{pptp}}} package via

{{{
ipkg install pptp
}}}

'''TIP:''' If you have no Internet connection for installing the package, you can flash the PPTP optimized images (with preinstalled PPTP packages instead of PPPoE packages) from his [http://downloads.openwrt.org/whiterussian/newest/pptp/ download directory].

When you have done this set the following NVRAM variables.

/!\ '''IMPORTANT:''' Use the correct [:OpenWrtDocs/Configuration#NetworkInterfaceNames:network interface name] for your hardware version in the {{{pptp_ifname}}} NVRAM variable.

{{{
nvram set wan_proto=pptp
nvram set wan_ifname=ppp0
nvram set pptp_ifname=<your_WAN_interface_name>
nvram set pptp_proto=static
nvram set pptp_server_ip=<pptp_server_ip_from_your_isp>
nvram set ppp_username=<your_isp_login>
nvram set ppp_passwd=<your_isp_password>
nvram set ppp_redialperiod=30
nvram set ppp_idletime=5
nvram set ppp_mtu=1492 # The MTU of your ISP
nvram set wan_ipaddr=<your_wan_ip>
nvram set wan_netmask=255.255.255.0
nvram commit
}}}

Than bring up your WAN interface where your modem is connected to via:

{{{
ifup wan
}}}

For more information see the ["PPTPClientHowto"].

## ##################################################
= Development =
See also the !OpenWrt [http://dev.openwrt.org/ development center] website. There you can browse the source code and send reproducible bugs with the ticket system (in trac).

== How do I create a package? ==
See BuildingPackagesHowTo.

== Requirements for compiling OpenWrt ==
For compiling !OpenWrt (from SVN or from the tarball, both the White Russian stable release) you need at least a recent GNU/Linux distribution and the following programs installed:

{{{
gcc, g++, binutils, patch, bzip2, flex, bison, make, gettext, unzip, libz-dev and
libc headers -- additional package dependencies: madwifi: uudecode(sharutils), privoxy: autoconf
}}}

When you get error messages related to libnvram, upgrade {{{make}}} to version 3.80. If that is not working as expected patch {{{make}}} 3.80 with the [http://ftp.debian.org/debian/pool/main/m/make/make_3.80-9.diff.gz Debian make patches].

Approximately required disc space for compiling OpenWrt:

||'''Branch''' ||'''Min.''' ||'''Max.''' ||
||Stable Source ||1.5 GB ||3.5 GB ||
||Development ||? ||3.8 GB ||


== Where is the subversion (SVN) repository ? ==
'''Stable Source'''

The stable source code can be found in the above directory or from our SVN repository. This is not recommended for beginners; we will not troubleshoot failed compiles.

{{{
svn co https://svn.openwrt.org/openwrt/branches/whiterussian/openwrt/
}}}

[http://dev.openwrt.org/browser/branches/whiterussian/openwrt/ Browse] the stable source SVN branch.

'''Development'''

/!\ '''WARNING:''' Please never use any image of Kamikaze, if you have no access to serial console. The chance to brick your router with the development version is very high.

Development take place in SVN. You get the source via:

{{{
svn co https://svn.openwrt.org/openwrt/trunk/openwrt/}}}

[http://dev.openwrt.org/browser/trunk/openwrt/ Browse] the development SVN branch.

== Should I report bugs releated to the buildroot system ==
Yes. If you find any bugs, please use our [http://dev.openwrt.org/report ticket system] or send a report to openwrt-devel@openwrt.org . You can send patches for the bugs as well.

/!\ '''NOTE:''' Changes to the buildroot system or the associated {{{Makefiles}}} could break the compile process. Please do not submit bug reports against modified copies of buildroot. Thanks.

== Where is the buildroot documentation? ==
See [http://downloads.openwrt.org/docs/buildroot-documentation.html buildroot documentation].
