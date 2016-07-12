= Introduction =

This guide originated in this[http://forum.openwrt.org/viewtopic.php?pid=8495#p8495] forum post, written by legodude on 2005-06-18.

It describes using OpenVPN to allow a "road warrier" remote user to connect to the home network from the wan interface i.e. anywhere on the internet.

= HowTo =

This is a quick howto for getting OpenVPN v2.0 up and running on OpenWRT. There are many possible ways to configure OpenVPN; the one we will use here is designed for ease of setup and one server with a few clients. To that end we will use bridged mode with static keys.

But first some words of caution. This setup works for me. I do not claim to be an OpenVPN expert and this may have gaping security holes or hose your system.

== Install Software ==
This howto assumes an OpenWRT machine will be the OpenVPN server and a Windows client machine, however, client setup should be basically the same no matter which OS is used.

For the OpenWRT, only a simple:

{{{ipkg install openvpn}}}

is all that is needed. Windows users can either download the standard OpenVPN distribution or get the GUI version from here:

http://openvpn.se/

Non-Windows clients just follow the OpenVPN install instructions.

== Generate Static Key ==
Windows users click the icon to generate a static key. Everyone else run:

{{{openvpn --genkey --secret static.key}}}

This only needs to be done once and then copied to all machines to be part of the VPN. I suggest placing the key file in /etc on the OpenWRT computer and leaving in the default place on Windows.

== Setup Server ==

=== Firewall ===

First we need to make sure that OpenVPN connections to port 1194 are not blocked by the firewall on OpenWRT. Add the following two lines after the section allowing WAN SSH access. 

If you intend to ssh the key across the WAN, opening up SSH for WAN access can be done just now.

/etc/firewall.user:
{{{
### Allow SSH from WAN (optional)
iptables -t nat -A prerouting_rule -i $WAN -p tcp --dport 22 -j ACCEPT
iptables        -A input_rule      -i $WAN -p tcp --dport 22 -j ACCEPT

### Allow OpenVPN connections
iptables -t nat -A prerouting_rule -i $WAN -p udp --dport 1194 -j ACCEPT
iptables        -A input_rule      -i $WAN -p udp --dport 1194 -j ACCEPT

### Port forwarding
}}}

=== Bridge Startup ===

Next we need to add the script to start the bridge

/etc/openvpnbridge:
{{{
#!/bin/sh

#/etc/openvpnbridge
# OpenVPN Bridge Config File
# Creates TAP devices for use by OpenVPN and bridges them into OpenWRT Bridge
# Taken from http://openvpn.net/bridge.html

# Make sure module is loaded
insmod tun

# Define Bridge Interface
# Preexisting on OpenWRT
br="br0"

# Define list of TAP interfaces to be bridged,
# for example tap="tap0 tap1 tap2".
tap="tap0"

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
}}}

This file will create the OpenVPN tap devices and add them to the default OpenWRT ethernet/wifi bridge. '''Make sure to chmod +x to ensure that it is executable'''.

=== OpenVPN server config file ===

/etc/server.ovpn:
{{{
# Which TCP/UDP port should OpenVPN listen on?
port 1194

# TCP or UDP server?
proto udp

# "dev tap" will create an ethernet tunnel.
dev tap


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
status openvpn-status.log

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
secret /etc/openvpn.key
}}}

At this point you can start OpenVPN for testing:

{{{openvpn /etc/server.ovpn}}}

With logread you should be able to see if it started up normally.

== Configure Client ==

Client configuration is pretty simple. First, transfer over the key file. This can be done by "scp" which is a file transfer over SSH. Example:

{{{scp 192.168.1.1:/etc/openvpn/wlan_home.key /etc/openvpn/}}}

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
}}}

Now that should be it. Start the OpenVPN client either through the GUI or command line and it should link up.

== Wrap Up ==
If your setup did not work then it is time to start reading the quite excellent OpenVPN documentation. The #openvpn channel on Freenode is also quite helpful.

If your setup is working fine then the only remaining step is to automate the startup of the OpenVPN server on the OpenWRT machine. To this end create the following file and make sure it is executable:

/etc/init.d/S46openvpn:
{{{
#!/bin/sh
#/etc/init.d/S46openvpn
/etc/openvpnbridge
openvpn --daemon /etc/server.ovpn
}}}
Now on a reboot, the server should come up.
----
CategoryHowTo
