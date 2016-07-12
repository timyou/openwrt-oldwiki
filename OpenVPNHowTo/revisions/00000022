'''OpenVPN via TAP !HowTo'''

[[TableOfContents]]

= Introduction =
This guide originated in this http://forum.openwrt.org/viewtopic.php?pid=8495#p8495 forum post, written by legodude on 2005-06-18.

It describes using OpenVPN to allow a "road warrior" remote user to connect to the home network from the wan interface i.e. anywhere on the internet.#

This guide describes a TAP-based (bridged tunnel) solution with preshared keys, for a TUN-based (routed tunnel) with SSL/TLS certificates, try the slightly different ["OpenVPNTunHowTo"] (which was based on this how-to).

For more information regarding the differences between bridging (TAP) and routing (TUN) and which solution is more appropriate in your case please see http://openvpn.net/faq.html#bridge2.

It has been updated to include fixes to get OpenVPN working on OpenWRT Kamikaze.

= HowTo =
This is a quick !HowTo for getting OpenVPN v2.0 up and running on OpenWRT. There are many possible ways to configure OpenVPN; the one we will use here is designed for ease of setup and one server with a few clients. To that end we will use bridged mode with static keys.

But first some words of caution. This setup works for me. I do not claim to be an OpenVPN expert and this may have gaping security holes or hose your system.

== Install Software ==
This !HowTo assumes an OpenWRT machine will be the OpenVPN server and a Windows client machine, however, client setup should be basically the same no matter which OS is used.

To install OpenVPN on OpenWRT, only a simple command is needed:

{{{
ipkg install openvpn
}}}
Windows users can either download the standard [http://openvpn.net/ OpenVPN distribution] or get the [http://openvpn.se/ OpenVPN GUI for Windows] from Mathias Sundman.

Non-Windows clients just follow the OpenVPN install instructions.

== Generate Static Key ==
Windows users click the icon to generate a static key. Everyone else run:

{{{
openvpn --genkey --secret secret.key
}}}
This only needs to be done once and then copied to all machines to be part of the VPN. I suggest you create /etc/openvpn on the OpenWRT computer, place the secret.key file there, and leave everything in the default place on Windows.

== Setup Server ==
=== Bridge Startup ===
We need to add a script to start the bridge.

{{{/etc/openvpn/startupscript:}}}

{{{
#!/bin/sh
#/etc/openvpn/startupscript
# OpenVPN Bridge Config File
# Creates TAP devices for use by OpenVPN and bridges them into OpenWRT Bridge
# Taken from http://openvpn.net/bridge.html
# Define Bridge Interface
# Preexisting on OpenWRT
br="br0"
# Define list of TAP interfaces to be bridged,
# for example tap="tap0 tap1 tap2".
tap="tap0"
case "$1" in
        up)
                # Make sure module is loaded
                insmod tun
                # Build tap devices
                for t in $tap; do
                    openvpn --mktun --dev $t
                done
                # Add TAP interfaces to OpenWRT bridge
                for t in $tap; do
                    brctl addif $br $t
                done
                #Configure bridged interfaces
                for t in $tap; do
                    ifconfig $t 0.0.0.0 promisc up
                done
        ;;
        down)
                for t in $tap; do
                    ifconfig $t 0.0.0.0 down
                done
                for t in $tap; do
                    brctl delif $br $t
                done
                for t in $tap; do
                    openvpn --rmtun --dev $t
                done
                rmmod tun
        ;;
        *)
                echo "$0 {up|down}"
        ;;
esac
}}}
This file will create the OpenVPN tap devices and add them to the default OpenWRT ethernet/wifi bridge.

If you are using Kamikaze change the line:

{{{
br="br0"
}}}
to:
{{{
br="br-lan"
}}}

At last the script has to be made executable:

{{{
chmod +x /etc/openvpn/startupscript
}}}
=== OpenVPN server config file ===
{{{/etc/openvpn/server.ovpn:}}}

{{{
# Which TCP/UDP port should OpenVPN listen on?
port 1194
# TCP or UDP server?
proto udp
# "dev tap" will create an ethernet tunnel.
# This must be tap0 instead of tap (as previously
# recommended).  If only tap is used, a new tap
# device is created when openvpn is started
# that isn't bridged to br0 by the script above.
dev tap0
# The keepalive directive causes ping-like
# messages to be sent back and forth over
# the link so that each side knows when
# the other side has gone down.
# Ping every 10 seconds, assume that remote
# peer is down if no ping received during
# a 120 second time period.
keepalive 10 120
# Enable compression on the VPN link.
# If you enable it here, you must also
# enable it in the client config file.
;comp-lzo
# The persist options will try to avoid
# accessing certain resources on restart
# that may no longer be accessible because
# of the privilege downgrade.
;persist-key
;persist-tun
# Output a short status file showing
# current connections, truncated
# and rewritten every minute.
status /etc/openvpn/status.log
# Set the appropriate level of log
# file verbosity.
#
# 0 is silent, except for fatal errors
# 4 is reasonable for general usage
# 5 and 6 can help to debug connection problems
# 9 is extremely verbose
verb 3
# Silence repeating messages.  At most 20
# sequential messages of the same message
# category will be output to the log.
;mute 20
#Static Key
secret /etc/openvpn/secret.key
}}}
At this point you can start OpenVPN for testing:

{{{
openvpn /etc/openvpn/server.ovpn
}}}
With {{{logread}}} you should be able to see if it started up normally.

If it does start up but you do not get a connection from the WAN check if you have a line in your server config file that says: "local 192.168.1.1" and comment it out.  This line is marked as optional in the original OpenVPN distribution, but will not work with the settings described in this !HowTo.

=== Firewall ===
To access the VPN from the internet (WAN) the firewall rules must accept outside connections for your VPN port (e.g. udp-1194). The firewall rules are stored in {{{/etc/firewall.user}}}. There is already an example (WR 0.9) for accepting SSH connections from outside, which can be copied and changed to:

{{{
### OpenVPN
## allow connections from outside
iptables -t nat -A prerouting_wan -p udp --dport 1194 -j ACCEPT
iptables        -A input_wan      -p udp --dport 1194 -j ACCEPT
}}}
Also as mentioned in the OpenVPN FAQ [http://openvpn.net/faq.html#ip-forward ip_foward must be enabled] ([http://forum.openwrt.org/viewtopic.php?pid=20428#p20428 default in WR 0.9]) and [http://openvpn.net/faq.html#firewall packets for the OpenVPN interfaces have to be allowed/forwarded]:

{{{
## allow input/forwarding for the VPN interfaces, see http://openvpn.net/faq.html#firewall
## also needs ip_forward, see http://openvpn.net/faq.html#ip-forward and http://forum.openwrt.org/viewtopic.php?pid=20428#p20428
iptables -A INPUT   -i tap+ -j ACCEPT
iptables -A FORWARD -i tap+ -j ACCEPT
}}}
If you want to block DoS attacks then have a look at [http://forum.openwrt.org/viewtopic.php?id=7493 this forum thread]. It is based on the information of the documents ["OpenWrtDocs/IPTables"] and ThrottleConnectionsHowTo. It also provides an example how to access SSH via a non-standard port (e.g. 443 for restrictive firewalls) although SSH is still running on the standard port 22. You can easily adopt it to VPN.

If it is intended that keys are sent via SSH across the WAN, then also enable accepting SSH connections from outside:

{{{
### SSH (optional)
## allow connections from outside
iptables -t nat -A prerouting_wan -p tcp --dport 22 -j ACCEPT
iptables        -A input_wan      -p tcp --dport 22 -j ACCEPT
}}}
== Configure Client ==
Client configuration is pretty simple. First, transfer over the key file. This can be done by "scp" which is a file transfer over SSH. Example:

{{{
scp root@192.168.1.1:/etc/openvpn/secret.key /etc/openvpn/
}}}
Now place the following file in the config directory and remember to change the server IP address to match, as well as the secrets file.

{{{
dev tap
proto udp
# The hostname/IP and port of the server.
# You can have multiple remote entries
# to load balance between the servers.
remote Your.IP.Goes.Here 1194
# Keep trying indefinitely to resolve the
# host name of the OpenVPN server.  Very useful
# on machines which are not permanently connected
# to the internet such as laptops.
resolv-retry infinite
# Most clients don't need to bind to
# a specific local port number.
nobind
# Try to preserve some state across restarts.
;persist-key
;persist-tun
# Wireless networks often produce a lot
# of duplicate packets.  Set this flag
# to silence duplicate packet warnings.
mute-replay-warnings
secret secret.key
# Enable compression on the VPN link.
# Don't enable this unless it is also
# enabled in the server config file.
;comp-lzo
# Set log file verbosity.
verb 3
# Silence repeating messages
;mute 20
# Allow LAN IP to reply to client
float
}}}
Now that should be it. Start the OpenVPN client either through the GUI or command line and it should link up.

== Wrap Up ==
If your setup did not work then it is time to start reading the quite excellent OpenVPN documentation. The #openvpn channel on Freenode is also quite helpful.

If your setup is working fine then the only remaining step is to automate the startup of the OpenVPN server on the OpenWRT machine. To this end create the following file:

=== White Russian ===
{{{/etc/init.d/S46openvpn:}}}

{{{
#!/bin/sh
case "$1" in
        start)
                /etc/openvpn/startupscript up
                openvpn --daemon --config /etc/openvpn/server.ovpn
        ;;
        restart)
                $0 stop
                sleep 3
                $0 start
        ;;
        reload)
                killall -SIGHUP openvpn
        ;;
        stop)
                killall openvpn
                /etc/openvpn/startupscript down
        ;;
esac
}}}
At last the script has to be made executable:

{{{
chmod 0755 /etc/init.d/S46openvpn
}}}

Now on a reboot, the server should come up.

=== Kamikaze ===
{{{/etc/init.d/openvpn:}}}

{{{
#!/bin/sh

START=65
STOP=35

start() { 
                /etc/openvpn/startupscript up
                openvpn --daemon --config /etc/openvpn/server.ovpn
}

restart() {
                $0 stop
                sleep 3
                $0 start
}

reload() {
                killall -SIGHUP openvpn
}

stop() {
                killall openvpn
                /etc/openvpn/startupscript down
}
}}}
At last the script has to be made executable and enabled to run at startup:

{{{
chmod +x /etc/init.d/openvpn
/etc/init.d/openvpn enable
}}}

Now on a reboot, the server should come up.

----
 CategoryHowTo
