'''How To: VPNC on !OpenWrt'''

Some people, like students from Ghent University, Belgium, need to connect with a Cisco VPN server in order to connect to the internet. It's an ideal task for an !OpenWrt router to make that connection and share it with all the connected PC's.
{{{
Performance Reports
 - On Asus WL-500G Deluxe (300Mhz) it maxes out at 30KB/s.
 - With a Asus WL-500gPremium (266Mhz) I got 250KB/s.
 - Tested WRT54GSv4 (200MHz) with Ethernet connection to Cisco Pix, 1des encryption, from NAT'd client behind WRT to ftp server behind Pix. 2.3 Mbps down and 1.9Mbps up. }}}
 - WRT54GL v1.1 (200mhz) - scp test at 45Kbytes a second with  31% CPU usage..

= Installation =
Configure your device to use the backports repository, see ["OpenWrtDocs/Packages"] for instructions, then install the packages:

{{{
ipkg install vpnc
ipkg install libgcrypt
ipkg install kmod-tun}}}

After the kmod-tun is installed a reboot is required.

{{{
reboot}}}

= Configuration =

Create a configuration file:

{{{
vi /etc/vpnc.conf}}}

And insert the parameters for your connection in there. These parameters are normally given by your sysadmin.

Here is an example ''vpnc.conf'':
{{{
IPSec gateway 157.193.46.4
IPSec ID ipsecclient
IPSec secret cisco123
Xauth username YOURUSERNAME
Xauth password YOURPASSWORD}}}

The IP-address after ''IPSec gateway'' is the address of the VPN-server. The ''IPSec ID'' and ''IPSec secret'' must be given to you by your sysadmin, or try these values as defaults.

Change '''YOURUSERNAME''' and '''YOURPASSWORD''' to your username and password respectively. If you don't feel comfortable with having your password in a plain text file on your !OpenWrt device, you can remove the ''Xauth password'' line, then VPNC will prompt you for the password every time you connect.

= vpnc-script =
VPNC automatically calls /etc/vpnc/vpnc-script to handle most of the maintenance operations like routing table and resolv.conf updates when a connection is established or broken. Unfortunately, the standard vpnc-script included with VPNC 0.3.3 won't run on OpenWRT's ash shell without a couple of changes. The modified script can be [http://www.dades.ca/openwrt/vpnc-script downloaded] or you can apply the changes shown below.

The stock script uses a c-style "for" expression that we'll replace with an equivalent "while".

The first location is in the "do_connect" function (approx. line 222) and the part we care about looks like this:
{{{
for ((i = 0 ; i < CISCO_SPLIT_INC ; i++ )) ; do
    eval NETWORK="\${CISCO_SPLIT_INC_${i}_ADDR}"
    eval NETMASK="\${CISCO_SPLIT_INC_${i}_MASK}"
    eval NETMASKLEN="\${CISCO_SPLIT_INC_${i}_MASKLEN}"
    set_network_route "$NETWORK" "$NETMASK" "$NETMASKLEN"
done}}}

Change the first line and insert a line just above the "done" so you end up with this:
{{{
i=0 ; while [ "$i" -lt "$CISCO_SPLIT_INC" ] ; do
    eval NETWORK="\${CISCO_SPLIT_INC_${i}_ADDR}"
    eval NETMASK="\${CISCO_SPLIT_INC_${i}_MASK}"
    eval NETMASKLEN="\${CISCO_SPLIT_INC_${i}_MASKLEN}"
    set_network_route "$NETWORK" "$NETMASK" "$NETMASKLEN"
    i=$(($i + 1))
done}}}

A similar pair of changes are required in the do_disconnect function just below the last change.

{{{
for ((i = 0 ; i < CISCO_SPLIT_INC ; i++ )) ; do
    eval NETWORK="\${CISCO_SPLIT_INC_${i}_ADDR}"
    eval NETMASK="\${CISCO_SPLIT_INC_${i}_MASK}"
    eval NETMASKLEN="\${CISCO_SPLIT_INC_${i}_MASKLEN}"
    del_network_route "$NETWORK" "$NETMASK" "$NETMASKLEN"
done}}}

Change to:

{{{
i=0 ; while [ "$i" -lt "$CISCO_SPLIT_INC" ] ; do
    eval NETWORK="\${CISCO_SPLIT_INC_${i}_ADDR}"
    eval NETMASK="\${CISCO_SPLIT_INC_${i}_MASK}"
    eval NETMASKLEN="\${CISCO_SPLIT_INC_${i}_MASKLEN}"
    del_network_route "$NETWORK" "$NETMASK" "$NETMASKLEN"
    i=$(($i + 1))
done}}}

= Start-up Script =
This script can either be placed in the /etc/init.d directory if you'd like the VPN to come up automatically or another location if you want manual control over the starting of the VPN.

It is a good idea to create the /var/run/vpnc directory in the start-up script as this is where vpnc will attempt to store original versions of the files it changes.

For automatic start, place this in /etc/init.d/S75vpnc:
{{{
#!/bin/sh
mkdir -p -m777 /var/run/vpnc
vpnc /etc/vpnc/vpnc.conf}}}

= Testing =
Save the script and execute it to start the connection.
{{{
/etc/init.d/S75vpnc}}}

= Sharing the VPN - Optional =
An additional change to vpnc-script is required to share the VPN with the router's clients. These changes are already in the modified file [http://www.dades.ca/openwrt/vpnc-script here].


Add these two functions to the /etc/vpnc-script:
{{{
start_vpn_nat() {
        iptables -A forwarding_rule -o tun0 -j ACCEPT
        iptables -A forwarding_rule -i tun0 -j ACCEPT
        iptables -t nat -A postrouting_rule -o tun0 -j MASQUERADE
}

stop_vpn_nat() {
        iptables -t nat -D postrouting_rule -o tun0 -j MASQUERADE
        iptables -D forwarding_rule -i tun0 -j ACCEPT
        iptables -D forwarding_rule -o tun0 -j ACCEPT
}
}}}

These functions should be called right after the connection is established and just before it is torn down. The "connect" and "disconnect" cases at the end of the vpnc-script should be modified to look like this if you want to share the vpn:
{{{
connect)
    do_connect
    start_vpn_nat
    ;;
disconnect)
    stop_vpn_nat
    do_disconnect
    ;;}}}

The connection can be stopped by killing the vpnc process and then restarted:
{{{
kill `cat /var/run/vpnc/pid`
/etc/init.d/S75vpnc}}}

= Visual Indicator - Optional =
With RC5, the Cisco LED that is on some Linksys units can be used as an up/down/error indicator. If you [http://www.dades.ca/openwrt/vpnc-script downloaded] the modified vpnc-script then you already have these changes and can skip down to S99done below.

== vpnc-script changes ==
Add these functions to the vpnc-script:
{{{
# LED Codes
# 0x01 - DMZ
# 0x04 - Power flashing
# 0x08 - Cisco White
# 0x10 - Cisco Orange
#
pend=0x10
conn=0x08
vpn_led_pending() {
        ledstat=`cat /proc/sys/diag`
        ledstat=$(($ledstat | $pend))
        echo "$ledstat" >/proc/sys/diag
}

vpn_led_connected() {
        ledstat=`cat /proc/sys/diag`
        ledstat=$(($ledstat ^ $pend))
        ledstat=$(($ledstat | $conn))
        echo "$ledstat" >/proc/sys/diag
}

vpn_led_disconnected() {
        ledstat=`cat /proc/sys/diag`
        ledstat=$(($ledstat ^ $conn))
        echo "$ledstat" >/proc/sys/diag
}
}}}

And finally, add calls to these functions in the pre-init, connect, and disconnect cases at the bottom of the script:
{{{
pre-init)
    vpn_led_pending
    do_pre_init
    ;;
connect)
    do_connect
    start_vpn_nat
    vpn_led_connected
    ;;
disconnect)
    stop_vpn_nat
    do_disconnect
    vpn_led_disconnected
    ;;}}}

== S99done ==
At the end of the boot process, the S99done script is called and one of the things it does is turn off all the controllable LED indicators. We need to change it to only turn off the DMZ LED to indicate Linux is finished booting without changing the other indicators. You can make the changes below or [http://www.dades.ca/openwrt/S99done download] a modified copy.

The last two lines of the file are:
{{{
# set leds to normal state
echo "0x00" > /proc/sys/diag}}}

Change to:
{{{
# set leds to normal state
# remove DMZ
ledstat=`cat /proc/sys/diag`
ledstat=$(($ledstat ^ 0x01))
echo "$ledstat" > /proc/sys/diag}}}


----
CategoryHowTo
