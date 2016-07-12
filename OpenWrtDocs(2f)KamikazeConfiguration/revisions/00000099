[[TableOfContents]]

= Kamikaze Configuration =
== Foreword / Background ==
In the early days of OpenWRT, the only target platforms were the WRT54G and similar Broadcom-based routers.  This platform has an NVRAM (much like high-end, commercial routers) to store configuration information.  Up until White Russian, OpenWRT used NVRAM for configuration.  As OpenWRT expanded to new platforms without NVRAM, NVRAM was abandoned in favor of configuration files in /etc/config.  This configuration method presents related information in the same area and is much like existing *nix configuration files.

Some older Kamikaze builds have configuration files which mimic the NVRAM configuration in that there are only key=value pairs in the configuration files.

== Order for Network Initialization ==
1. CFE (bootloader) may initialise switch into VLANS based on NVRAM information

2. Kamikaze initialise switch into VLANS based on information in /etc/config/network (see below) - note this creates network devices with names like ''eth0.0''. Note also this used to be done using the ''robocfg'' utility; how is it done now?

3. Kamikaze initialise the wifi card - note this can be done using ''madwifi'' or ''iwconfig'', is that what is happening during startup? (it uses self made scripts, calling wlc, isn't it?)

4. Kamikaze initialise bridges to link wireless interface with (v)LAN based on information in /etc/config/network - note this can be done using the ''brctl'' utility, is this what is used during startup?

5. Kamikaze will assign ip addresses or ask for dhcp IP leases for network devices or bridges - could be using ''ifconfig''?

== Network Configuration ==
Many of the concepts from earlier versions are retained in Kamikaze.  Both lan and wan still exist on Kamikaze, while VLANs are still used to separate WAN and LAN interfaces.

 * Network Background: OpenWrtDocs/NetworkInterfaces
 * [http://downloads.openwrt.org/kamikaze/docs/openwrt.html#x1-80001.2.1 /etc/config/network documentations]
 * Some IP, netmask, etc review site
 * Some bridging and brctl info page
=== VLANs ===
Since most routers use a single switch, you need to split up your WAN and LAN. There are some alternate configurations, like all ports switched and DMZ. See [:OpenWrtDocs/HardwareTables/switchPorts:Switch Ports] for more details.

{{{
# Normal routing configuration for WRT54Gv3
config switch eth0
        option vlan0    "0 1 2 3 5*"
        option vlan1    "4 5"
}}}
The "*" mark is set for the default VLAN. Pakets transfered between interfaces on the default VLAN are the ones that will remain unchanged, while all other will be "tagged". See more in section "VLAN Trunking" under the [:OpenWrtDocs/NetworkInterfaces:VLAN and bridging concepts] page.

If you are using a VLAN 802.11q capable external switch, you can use it simply by configuring the VLAN interfaces as instructed in the next section.  For example: VLAN 1 on the switch would correspond to eth0.1 on OpenWRT.

=== Network Layer ===
==== DHCP ====
{{{
config interface wan
        option ifname   eth0.1
        option proto    dhcp
        option hostname MyRouter  #This is only used if the proto is dhcp otherwise it is ignored.
}}}
==== Static ====
{{{
config interface lan
        option ifname   eth0.0
        option proto    static
        option ipaddr   192.168.1.2
        option netmask  255.255.255.0
        option gateway  192.168.1.1
        option dns      192.168.1.1
}}}
==== Sub interfaces / IP Alias ====
{{{
config interface lan1
        option ifname   eth0.0:0
        option proto    static
        option ipaddr   192.168.1.2
        option netmask  255.255.255.0
        option gateway  192.168.1.1
Note: The "option type" must be absent!
(http://forum.openwrt.org/viewtopic.php?id=10505)
}}}
You can configure multiple DNS servers by separating entries with space:

{{{
option dns "192.168.1.1 192.168.80.100"
}}}
==== Bridging Interfaces ====
{{{
config interface lan
        option type     bridge
        option ifname   "eth0.0"    #See note 1 for adding a wireless interface to the bridge.
        option proto    static
        option ipaddr   192.168.1.1
        option netmask  255.255.255.0
}}}
==== Bridged xDSL ====
{{{
config interface wan
        option ifname   nas0
        option proto    dhcp
}}}
==== MAC Address Cloning ====
Add the following option to /etc/config/network under the wan section:

{{{
option macaddr xx:xx:xx:xx:xx:xx
}}}
Restart the network using:

{{{
/etc/init.d/network restart
}}}
or reboot your router

Check dmesg or syslog for the change.  If the mac address does not change, clean your nvram variables using these instructions:

{{{
http://wiki.openwrt.org/Faq#head-71cacf8460752af3f5771d2fae54923ded5beb9c
}}}
=== PPPoE and PPPoA ===
Normally, these are used for DSL.

{{{
config interface wan
        option ifname   "eth0.1"
        option proto    pppoe
        option username "xxxxxx"
        option password "xxxxxx"
}}}
==== IPv6 ====
===== Using Go6.net =====
This section describe how to setup IPv6 using the [[http://go6.net/ | Go6.net]] service.

 1. Sign up for a free account with Go6.
 1. Setup your router for IPv6.
  1. Install the following packages: kmod-ipv6, kmod-tun, ip, libpthread, radvd.
  1. Install the Gateway6 client v5 from here: http://www.roadrunner.cx/openwrt/gw6c_4.2.2_mipsel.ipk
 1. Configure the Gateway6 Client. The config file is located at /etc/gw6c/
  1. Change userid and passwd to your username and password.
  1. Change server to broker.freenet6.net
  1. Change host_type to one of the following:
   1. router if you want to use IPv6 on your whole network.
   1. host if you want to use IPv6 just on your router.
  1. You should not have to mess with any other settings.
 1. Start the Gateway6 Client.
  1. Start immediately with /etc/init.d/gw6c start
  1. Reboot your router
 1. Check syslog for errors.

Most of this information came from [http://forum.openwrt.org/profile.php?id=524 jake1981] at the OpenWRT forums from this post:

[http://forum.openwrt.org/profile.php?id=524 ]
=== Wireless configuration ===
==== 802.11x ====
'''Note: Currently supported on Broadcom only, although madwifi support is almost complete :)'''

 * /etc/config/wireless documentations https://dev.openwrt.org/browser/trunk/docs/wireless.tex
 * Other types, e.g. madwifi, are not yet handled here and must use a startup script to work.
Wireless specific (Layers 1 and 2) configuration is in /etc/config/wireless.  Layer 3 (Network) is done in /etc/config/network.

Default Configuration:

{{{
config wifi-device      wl0
        option type     broadcom
        option channel  5
        option disabled 1
config wifi-iface
        option device   wl0
        option mode     ap
        option ssid     OpenWrt
        option hidden   0
        option encryption none
}}}
Full outline of the wifi config file is as follows:

{{{
config wifi-device     wifi device name
       option type     currently only broadcom and atheros
       option country  country code [not mandatory, used for setting restrictions based on country regulations]
       option channel  1-14
       option disabled 1 disables the wireless card, 0 enables the wireless card
       option maxassoc Currently only for Broadcom. Maximum number of associated clients
       option distance The distance between the ap and the furthest client in meters.
       option agmode     Currently only for Atheros.  Options are: 11b, 11g, 11a, 11bg
       option diversity Currently only for Atheros. 0 disables diversity, 1 enables diversity (default)
       option txantenna Currently only for Atheros. 0 for auto (default), 1 for antenna 1, and 2 for antenna 2
       option rxantenna Currently only for Atheros. 0 for auto (default), 1 for antenna 1, and 2 for antenna 2
config wifi-iface
       option network  the interface you want wifi to bridge with
       option device   wifi device name
       option mode     ap, sta, adhoc, or wds
       option ssid     ssid to be used
       option bssid    used for wds to set the mac address of the other wds unit
       option encryption none, wep, psk, psk2, wpa, wpa2 (note 4,5)
       option key      encryption key or radius shared secret, when used for wep if you only use one key it can be placed here otherwise set this to the key number you would like to use and use the following key1-4 options
       option key1     wep key 1
       option key2     wep key 2
       option key3     wep key 3
       option key4     wep key 4
       option server   radius server
       option port     radius port
       option txpower  Currently only for Atheros. This value is measured in dbm
       option bgscan   Currently only for Atheros. This controls client background scanning, 0 disabled, 1 enabled (default)
       option hidden   0 broadcasts the ssid; 1 disables broadcasting of the ssid
       option isolate  0 disables ap isolation (default); 1 enables ap isolation
       option wds      Atheros only. 0 disables wds (default), 1 enables wds
}}}
'''Notes: '''

'''1) "option network <interface>": This setting is mandatory if you want your wifi interface bridged to your lan (Normal bridging: "option network lan").'''  If you don't want to do that, see [:OpenWrtDocs/KamikazeConfiguration/NonBridgedWiFi:Using Non-Bridged WiFi].

'''2) "option encryption <key>": wpa and wpa2 are for radius config, use psk for WPA-PSK or psk2 for WPA-PSK2 (AES)'''

'''3) "option key <key>": You must use a key that is at least 8 characters long if you are using psk2.''' If your key is fewer than 8 characters long, you may get the following error under Kamikaze 7.09: "wl0: ignore i/f due to error(s)".

'''4) "option mode": there is no 'wet' mode any more.''' However, if you select 'sta' mode, and also bridge the wireless to another interface (e.g. 'option network lan'), then wet mode is enabled automatically. This allows the unit to act as a wireless bridge, so that one or more PCs sitting behind the OpenWrt box can join the LAN. Some ARP and DHCP masquerading is done so that this doesn't require WDS mode on the access point. ''(Tested with Kamikaze 7.07 and a Broadcom chipset and 2.4 kernel; may not work for Atheros and/or 2.6 users)''

'''5) "option type broadcom":''' If you get an error about 'broadcom unsupported', make sure you have the '''wlc''' and '''kmod-brcm-wl''' packages installed. You will probably also need '''nas''' for WPA.

'''6) hostapd:''' For WPA you may need hostapd. The kamikaze 7.07 does not include hostapd and must be installed to support WPA (at least when using madwifi).

==== MAC Filter ====
First, you need to have installed the wl package - '''ipkg install wl'''
||'''uci variable''' ||'''Description''' ||
||'''wireless.wl0.macfilter''' ||(0/1/2) used to (disable checking/deny/allow) mac addresses listed in wl0.maclist ||
||'''wireless.wl0.maclist''' ||List of space-separated mac addresses to allow/deny according to wl0.macfilter. Addresses should be entered with colons, e.g.: "00:02:2D:08:E2:1D 00:03:3E:05:E1:1B". note that if you have more than one mac use quotes or only the first will be recognized. ||


Create the following script as '''/etc/init.d/wlmacfilter'''

{{{
#!/bin/sh /etc/rc.common
# The macfilter 2 means that the filter works in "Allow" mode.
# Other options are: 0 - disabled, or 1 - Deny.
#
# The maclist is a list of mac addresses to allow/deny, quoted, with spaces
#  separating multiple entries
# eg  "00:0D:0B:B5:2A:BF 00:0D:0C:A2:2A:BA"
START=47
MACFILTER=`uci get wireless.wl0.macfilter`
MACLIST=`uci get wireless.wl0.maclist`
start() {
        wlc ifname wl0 maclist "$MACLIST"
        wlc ifname wl0 macfilter "$MACFILTER"
}
stop() {
        wlc ifname wl0 maclist none
        wlc ifname wl0 macfilter 0
}
}}}
Finally, enable the script to run at boot time:

{{{
chmod 755 /etc/init.d/wlmacfilter
/etc/init.d/wlmacfilter enable}}}
Set the variables

{{{
uci set wireless.wl0.macfilter="2"
uci set wireless.wl0.maclist="00:0D:0B:B5:2A:BF 00:0D:0C:A2:2A:BA"
uci commit}}}
After making changes to the mac list with uci, run '''/etc/init.d/wlmacfilter start'''

== Services ==
=== DHCP ===
OpenWrt uses the lightweight [http://www.thekelleys.org.uk/dnsmasq/doc.html dnsmasq] DHCP server, which is configured in '''/etc/config/dhcp''':

{{{
config dhcp
        option interface        lan
        option start            100
        option limit            150
        option leasetime        12h
config dhcp
        option interface        wan
        option ignore   1}}}
This will make dnsmasq will offer up to 150 address leases, starting from address .100 of your network with a lease time of 12 hours. e.g. 10.0.0.100-10.0.0.249

If you think dnsmasq is not offering addresses as configured, use ''ps w'' to see what command-line arguments it was run with:

{{{
root@wrt:~# ps w | grep dnsmasq
  606 nobody      452 S   /usr/sbin/dnsmasq --dhcp-range=lan,10.0.0.10,10.0.0.60,255.255.255.0,12h -I eth0.1}}}
A common problem is to have the --dhcp-range option missing:

 . {{{/usr/sbin/dnsmasq -I eth0.1}}} (or ppp0, or whatever your WAN interface is -- -I means "don't offer addresses on this interface", more on that in ''dnsmasq --help'')
If that's the case, just append to your lan interface section:

{{{
option force 1
}}}
= HowTo =
=== How to Automatically configure Client/Ad-hoc Client/Client+Repeater Mode on a Fonera or Meraki mini ===
Visit Meltyblood's site for more Openwrt/Legend firmware upgrades: http://fon.testbox.dk  1. Read the instructions and get the tar.gz package from here http://fon.testbox.dk/packages/NEW/LEGEND4.5/clientscript/

That's it.  The package of scripts self-installs and will ask you questions to configure your wired and wireless connections.  Your current configuration will be backed up and can be restored with the "aprestore" command.  Type in "clientmode" after installation to configure client mode.  This is currently the easiest and most complete means of having client mode on an Atheros router.   These scripts are incompatible with firmwares that use NVRAM.  They are included in the Legend Rev4.5 firmware, which will soon be released on the site.

=== How to Automatically configure Standalone Repeater Mode on a Fonera or Meraki mini ===
Coming VERY soon.  This one will differ from the Client mode script package in that there will also be a option to quickly setup a repeater without restarting services.

=== HowTo run HP LaserJet 1018/1020/1022 on OpenWRT Kamikaze 7.06 ===
At first a install foo2zjs  drivers from http://foo2zjs.rkkda.com/ on linux box.

It's instruction from  http://foo2zjs.rkkda.com/

{{{
„Click the link, or cut and paste the whole command line below to download the driver.
    $ wget -O foo2zjs.tar.gz http://foo2zjs.rkkda.com/foo2zjs.tar.gz
Now unpack it:
Unpack:
    $ tar zxf foo2zjs.tar.gz
    $ cd foo2zjs
Now compile and install it. The INSTALL file contains more detailed instructions; please read it now.
Compile:
    $ make
Get extra files from the web, such as .ICM profiles for color correction,
and firmware.  Select the model number for your printer:
    $ ./getweb 2430     # Get Minolta 2430 DL .ICM files
    $ ./getweb 2300     # Get Minolta 2300 DL .ICM files
    $ ./getweb 2200     # Get Minolta 2200 DL .ICM files
    $ ./getweb cpwl     # Get Minolta Color PageWorks/Pro L .ICM files
    $ ./getweb 1020     # Get HP LaserJet 1020 firmware file
    $ ./getweb 1018     # Get HP LaserJet 1018 firmware file
    $ ./getweb 1005     # Get HP LaserJet 1005 firmware file
    $ ./getweb 1000     # Get HP LaserJet 1000 firmware file
Install driver, foomatic XML files, and extra files:
    $ su                        OR      $ sudo make install
    # make install
(Optional) Configure hotplug (USB; HP LJ 1000/1005/1018/1020):
    # make install-hotplug      OR      $ sudo make install-hotplug
(Optional) If you use CUPS, restart the spooler:
    # make cups                 OR      $ sudo make cups ”
}}}
Next you must transfer  sihp1020.dl to your Asus box.

On Asus You should install packages :

{{{
 ipkg install kmod-usb-pinter
 ipkg install p910nd
}}}
When do you have problem with depends  kmod-nls-base. You should edit /usr/lib/ipkg/lists and remove depends for your pacage.

Next:

{{{
/etc/init.d/p910nd enable
/etc/default/p910nd I leave without any changes !!!!
}}}
And next You need create script which upload frimware to your printer when she had pluged.

Create a new file /etc/hotplug.d/usb/hplj1020:

{{{
#!/bin/sh
FIRMWARE="/mnt/pendrive/sihp1020.dl"
 < -- place where you have your .dl file.
if [ "$PRODUCT" = "3f0/2b17/100" ]
then
        if [ "$ACTION" = "add" ]
        then
                echo "`date` : Sending firmware to printer..." > /var/log/hp
                cat $FIRMWARE > /dev/usb/lp0
                echo "`date` : done." > /var/log/hp
          fi
}}}
You must change parameter 3f0/2b17/100 for your printer.

3f0/517/120 it is idVendor/idProduct/bcdDevice, from device descriptor. Numbers are hexadecimal, without leading '0x' or zeros.

This parameters you can get from ls with v option. More info you can find at http://linux-hotplug.sourceforge.net/?selected=usb .

=== Using WRT54G(S/L) SES button for Radio Control ===
This is a remake of a code that is found on http://wiki.openwrt.org/OpenWrtDocs/Customizing/Software/WifiToggle

Step 1: Create the button/ folder inside /etc/hotplug.d/ if it doesn't exist

Step 2: cd to this dir and edit a new file named 01-radio-toggle

Step 3: Paste this code inside the file

{{{
if [ "$BUTTON" = "ses" ] ; then
        if [ "$ACTION" = "pressed" ] ; then
                WIFI_RADIOSTATUS=$(wlc radio)
                case "$WIFI_RADIOSTATUS" in
                0)
                        echo 2 > /proc/diag/led/power
                        wlc radio 1
                        wifi
                        echo 1 > /proc/diag/led/ses_white
                        echo 1 > /proc/diag/led/power ;;
                1)
                        echo 2 > /proc/diag/led/power
                        wlc radio 0
                        echo 0 > /proc/diag/led/ses_white
                        echo 2 > /proc/diag/led/wlan
                        echo 1 > /proc/diag/led/power ;;
                esac
        fi
fi
}}}
Step 4: Save the file and just test it, it will lit Wlan and White SES Led when radio is on, and turn both off when radio is off

=== Problems running vsftp on OpenWRT Kamikaze 7.06 ===
If you just install vsftp on Kamikaze 7.06 with ipkg install vsftpd and start it with "vsftpd" you will not be able to login into your ftp-server due to a missing directory. Just add a new line to your vsftpd.conf in /etc/. This line is secure_chroot_dir=existing_dir (existing_dir musst be a directory which will be "be" once the service is started. So point to a directory which exists all the time or one which will be created at boot time)

=== timezone/ntp ===
With the x-wrt webif^2, use System -> Settings page. :)

Otherwise, in /etc/config/timezone an example is (for info about other zones and DST rules, see http://wiki.openwrt.org/OpenWrtDocs/Configuration and look for Timezone)

{{{
config timezone
        option posixtz  MST7MDT,M3.2.0,M11.1.0
        option zoneinfo 'America/Denver'
}}}
~-Note: The '''zoneinfo''' field is designed to contain the same information like the timezone setting in most current *nix implementations (the Olson's database). It will later enable to simply synchronize changes in the POSIX TZ strings.-~

Do the following on a *nix system to find out your timezone string:

{{{
cat /usr/share/zoneinfo/posix/continent/city
}}}
and look at the last line.

Next you either create the /etc/TZ file and copy the posixtz field to it or you can create a simple timezone init script which will handle all TZ changes and the creation of the /etc/TZ file:

{{{
#!/bin/sh /etc/rc.common
START=11
timezone_config() {
        local cfg="$1"
        local posixtz
        local etctz="/etc/TZ"
        config_get posixtz "$cfg" posixtz
        if [ ! -h $etctz ]; then
                ln -sf /tmp/TZ "$etctz"
        fi
        [ -n "$posixtz" ] && echo "$posixtz" > "$etctz" || echo "UTC+0" > "$etctz"
}
start() {
        config_load timezone
        config_foreach timezone_config timezone
}
restart() {
        start
}
}}}
and issue

{{{
/etc/init.d/timezone start
/etc/init.d/timezone enable
}}}
You could use rdate in a script to set the time just at boot time and rely on the router's timer to keep it current.  But, to use ntp install ntpclient, and in modify /etc/config/ntpclient to your needs:

{{{
config ntpclient
        option hostname 'pool.ntp.org'
        option port     '123'
        option count    '1'
config ntpclient
        option hostname 'ntp.ubuntu.com'
        option port     '123'
        option count    '1'
}}}
OpenWrt will soon advertise its [http://www.pool.ntp.org/vendors.html NTP Vendor Zone] with appropriate entries in all relevant packages. A [http://lists.openwrt.org/pipermail/openwrt-devel/2008-January/001524.html patch] for fixing this in ntpclient has these additional timeservers:

{{{
config ntpclient
        option hostname '0.openwrt.pool.ntp.org'
        option port     '123'
        option count    '1'
config ntpclient
        option hostname '1.openwrt.pool.ntp.org'
        option port     '123'
        option count    '1'
config ntpclient
        option hostname '2.openwrt.pool.ntp.org'
        option port     '123'
        option count    '1'
config ntpclient
        option hostname '3.openwrt.pool.ntp.org'
        option port     '123'
        option count    '1'
}}}
Of course there are even more alternatives, i.e. feel free to substitute your local ntp server for pool.ntp.org.

Then run

{{{
ACTION=ifup /etc/hotplug.d/iface/20-ntpclient
}}}
or restart the network and check what date says.

== More HowTos ==
For more How-To's (for example setting up Kamikaze, step by step) have a look at  http://forum.openwrt.org/viewforum.php?id=17

= Sample Application Config Scripts =
 * Repeater http://wiki.openwrt.org/Repeater
 * Routed client-mode wireless on a Fonera http://wiki.openwrt.org/ClientModeKamikazeStyleHowto
== multi wan configuration on kamikaze ==
OpenWrtDocs/KamikazeConfiguration/MultipleWan

----
 . CategoryHowTo
----
 . CategoryHowTo
