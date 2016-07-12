= Setting up OpenWRT to be a wireless bridge on a WPA2-PSK wireless network =

== Rationale ==
This page describes how to set up an OpenWRT install -- a WRT54G v4 in my case -- to be a wireless bridge to an existing wireless network.  The goal is to end up with a plain bridge, no WDS, no routing, no anything except for holding one IP for administration, on a WPA2-PSK enabled wireless network.  This allows the following network configuration:

{{{
    +---------+                                   +--------------+
    | OpenWRT |  <--- WPA2-PSK secured WiFi --->  | Existing     |
    | bridge  |                                   | access point | -- (DHCP server)
    +---------+                                   +--------------+
     |   |   |
     PC  PC  PC

   (DHCP clients)

  * No wireless repeater on this end *
}}}

It's very easy to set up client mode on an unsecured network - see ClientModeHowto for example.  It turns out, however, that client mode on a WPA network is not quite as easy, and setting it up as a bridge is a bit tricky, too.  It's also easy to get this configuration working in WDS mode, but where the bridge and the AP are located close to each other, some clients would jump on the repeater side of the network and cause a loss in throughput.

Most of the information was gleaned from the OpenWRT wiki and posts made in http://forum.openwrt.org and dozens of other web sites, and I thank the multitude of unattributed contributors for sharing their knowledge.

== Instructions (This section should be expanded) ==
 1. Install wl
 1. Install nas
 1. Install dhcp-forwarder
 1. Install libpthread and parprouted (from http://downloads.openwrt.org/people/nico/testing/mipsel/packages/)
 1. Delete /etc/init.d/S45firewall
 1. Delete /etc/init.d/S50dnsmasq
 1. Delete /etc/init.d/dhcp-fwd
 1. Delete /etc/dhcp-fwd.conf
 1. Create /etc/init.d/S50dhcp-fwd (code below)
 1. Create /etc/init.d/S47sleep (code below)
 1. Edit /etc/init.d/S41wpa and rename it S41supplicant
    * Remove the -l parameter from nas - it does not work in Supplicant mode (see ["OpenWrtDocs/nas"])
        * On two separate lines, this text must be deleted:
        * ${wifi_ifname:+ -l ${wifi_ifname}}
 1. Set NVRAM
    * Networking:
        * wl0_radio=1
        * wl0_infra=1
        * wl0_ssid=''<your SSID>''
        * wl0_mode=sta
        * wl0_akm=psk2
            * psk is also acceptable, but use wl0_crypto=tkip
            * "psk psk2" will not work - pick only one
        * wl0_crypto=aes+tkip
            * This is the group=tkip, pairwise=aes mix that is commonly used
        *  wl0_wpa_psk=''<your psk>'' (in ASCII)
    * Break the bridge:
        * Note:
            * The built-in hardware bridge would see a mix of encrypted and unencrypted frames, so the bridging needs to be done in software.
            * If you are using vlan1 (or whatever wan_ifname is) then you will need to unset wan_ifname and change the failsafes in S05nvram.
            * Change these interface names to match your hardware - these work for the WRT54G v4 and similar hardware.
        * lan_ifname=vlan0 ''(Oddly, eth0 here seems not to work.)''
        * wifi_ifname=eth1
    * Enable DHCP on wireless side:
        * wifi_proto=dhcp
    * Put all LAN ports on vlan0:
        * unset vlan1ports
        * unset vlan1hwname
        * vlan0ports="4 3 2 1 0 5*"
 1. Double-check everything, then mentally prepare yourself for a bricking.  (Failsafe mode should still work fine, but who knows?  I bricked mine enough times while figuring all of this out that the circuit board is sitting naked on top of a stack of paper as I type this.)
 1. nvram commit
 1. reboot

== S47sleep ==

{{{
#!/bin/sh
# S47sleep - Delay before starting services
# Sometimes the interfaces take a while to come up after being started.
# This script simply sleeps for 20 seconds while flashing the Power LED,
# giving enough time for the network to come up before continuing.

DIAG=`cat /proc/sys/diag`

echo 0x05 > /proc/sys/diag
sleep 20
echo ${DIAG} > /proc/sys/diag
}}}

== S50dhcp-fwd ==

The DHCP forwarder (dhcp-fwd) configuration file contains several hard-coded values that are better being detected from NVRAM and the current network configuration.  This start-up script queries those sources and writes a configuration file tailored to the current environment, then starts dhcp-fwd using that configuration file.

{{{
#!/bin/sh

# /etc/init.d/S50dhcp-fwd
# Runs dhcp-fwd after creating configuration file

# Start configuration section
LOG_DIR=/var/log
RUN_DIR=/var/run
JAIL_DIR=${RUN_DIR}/dhcp-fwd
PID_FILE=${RUN_DIR}/dhcp-fwd.pid
CFG_FILE=${RUN_DIR}/dhcp-fwd.conf
LOG_FILE=${LOG_DIR}/dhcp-fwd.log
# End configuration section

. /etc/functions.sh

WIFI_IF=$(nvram get wifi_ifname)
LAN_IF=$(nvram get lan_ifname)

GIADDR=`ifconfig \
        | awk 'BEGIN { RS="\n\n" } /^'${WIFI_IF}' / { print $7 }' \
        | cut -d ':' -f 2`

if [ "$GIADDR" = "" ]; then
        logger -s "Unable to detect GIADDR - no IP address on $IFACE?"
        exit 1
fi


createdirs () {
        [ -e $LOG_DIR ] && [ ! -d $LOG_DIR ] && rm -f $LOG_DIR
        [ ! -d $LOG_DIR ] && mkdir -p $LOG_DIR

        [ -e $RUN_DIR ] && [ ! -d $RUN_DIR ] && rm -f $RUN_DIR
        [ ! -d $RUN_DIR ] && mkdir -p $RUN_DIR

        [ -e $JAIL_DIR ] && [ ! -d $JAIL_DIR ] && rm -f $JAIL_DIR
        [ ! -d $JAIL_DIR ] && mkdir -p $JAIL_DIR
}

createcfg () {
        cat << EOF > $CFG_FILE
# This file was generated automatically by $0 - Do not edit!

user            0
group           0
chroot          $JAIL_DIR

logfile         $LOG_FILE
loglevel        1

pidfile         $PID_FILE

ulimit core     0
ulimit stack    64K
ulimit data     32K
ulimit rss      200K
ulimit nproc    0
ulimit nofile   0
ulimit as       0

#       IFNAME  clients servers bcast
if      $LAN_IF true    false   true
if      $WIFI_IF        false   true    true

server bcast $WIFI_IF

ip $LAN_IF $GIADDR

EOF
}

startdhcpfwd () {
        dhcp-fwd -c $CFG_FILE
}

killdhcpfwd () {
        [ -f $PID_FILE ] && kill `cat $PID_FILE`
}


case $1 in
        start)
                createdirs
                createcfg
                startdhcpfwd
                ;;
        stop)
                killdhcpfwd
                ;;
        *)
                echo "usage: $0 start|stop"
                exit 1
esac

exit $?
}}}

== Testing it out ==

At this point, you should have a more or less working wireless bridge: plug something in the LAN port and it'll be virtually connected to the same network as your other wireless clients.

Note the delay in starting up - if there's a power failure to the bridge, the DHCP clients behnid the bridge must be willing to wait a while before giving up on getting a lease.  On UNIX, this may involve adding a S47sleep-like script on the client hosts, too.  Windows systems may have problems with this arrangement.

As noted in the parprouted documentation, broadcasting will not cross the bridge.  DHCP relaying was added as a special case.  If you have other applications that use broadcast, you'll have to work around those, too.

== Troubleshooting ==

This section needs to be expanded.  If you try this and it doesn't work, please list some things you tried (and why) here for the benefit of future readers.

 * Check that the wireless connection is up:
    1. Set a machine to a static IP address on the same subnet as the lan_ipaddr and ssh in.
    1. Try ''wl assoclist'' to see if the bridge has associated with the AP.  (The AP's MAC address appears if so.)
    1. Try ''wl sta_info <AP MAC address>'' to see how far the connection has gone.
        * ASSOCIATED AUTHENTICATED AUTHORIZED is fully connected on the transport layer.
        * ASSOCIATED AUTHENTICATED probably means the encryption is not correct; double-check the wl0_akm and wl0_crypto and wl0_psk_key variables.
    1. Look at ''iwconfig eth1'' - the Encryption: field should show a key, not "off".

== Confirmation ==

If you follow this how-to, please note here if it worked or didn't work for you!

== Appendix: Sample NVRAM configuration ==

{{{
root@OpenWRT:~# nvram show | sort
...
lan_ifname=vlan0
lan_ifnames=vlan0 eth1 eth2       # This is set by S05nvram and is not needed
lan_ipaddr=192.168.1.1            # This value doesn't matter
lan_netmask=255.255.255.0
lan_proto=static
...
vlan0hwname=et0
vlan0ports=4 3 2 1 0 5*
...
wifi_ifname=eth1
wifi_proto=dhcp
...
wl0_akm=psk2
wl0_crypto=aes+tkip
wl0_ifname=eth1
wl0_infra=1
wl0_mode=sta
wl0_radio=1
wl0_ssid=<<SSID>>
wl0_wpa_psk=<<PSK>>
...
}}}
