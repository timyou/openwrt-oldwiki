## Please edit system and help pages ONLY in the moinmaster wiki! For more
## information, please see MoinMaster:MoinPagesEditorGroup.
##acl MoinPagesEditorGroup:read,write,delete,revert All:read
##master-page:HelpTemplate
##master-date:Unknown-Date
#format wiki
#language en
== PPPOE over Wireless Howto ==
For anyone who has to connect to the internet through a wireless connection, but also needs PPPOE authentication, this is for you (me and at least one other person!).

=== Set up wireless ===
First thing's first: set up your wireless. This is actually easy.

Your wl0_mode should be sta (do a ''nvram set wl0_mode=sta'' )
Your wl0_ssid should be the ssid of the WISP (''nvram set ...'')
If you want to make sure it's working, set wifi_proto to dhcp.
Do an nvram commit, reboot.
Once you're back in, try pinging the WISP's ip (if you set wifi_proto), or just ''iwconfig ethX'', where ethX is your wireless.

Good job!

=== Set up PPPoE ===
Set wifi_proto to pppoe, and ppp_ifname to ethX (check the last one, might not be needed.)

Create a /sbin/ifup.wlppp :

==== ifup.wlppp ====
{{{
#!/bin/sh
[ $# = 0 ] && { echo "  $0 <group>"; exit; }
. /etc/functions.sh

for module in slhc ppp_generic pppox pppoe; do
        /sbin/insmod $module 2>&- >&-
done

(while :; do
        IFNAME=[ethX] (wireless)
        USERNAME=[username]
        PASSWORD=[password]
        KEEPALIVE=redialperiod
        KEEPALIVE=${KEEPALIVE:+lcp-echo-interval 1 lcp-echo-failure $KEEPALIVE}
        DEMAND=[demand]
        case "$DEMAND" in
                on|1|enabled)
                        DEMAND=idletime
                        DEMAND=${DEMAND:+demand idle $DEMAND}
                        [ -f /etc/ppp/filter ] && DEMAND=${DEMAND:+precompiled-active-filter /etc/ppp/filter $DEMAND}
                ;;
                *) DEMAND="";;
        esac

        MTU=[mtu]
        MTU=${MTU:-1492}

        ifconfig $IFNAME up
        /usr/sbin/pppd nodetach \
                plugin rp-pppoe.so \
                connect /bin/true \
                usepeerdns \
                defaultroute \
                replacedefaultroute \
                ipparam "$type" \
                linkname "$type" \
                user "$USERNAME" \
                password "$PASSWORD" \
                mtu $MTU \
                mru $MTU \
                $DEMAND \
                $KEEPALIVE \
                nic-$IFNAME
done 2>&1 >/dev/null ) &

}}} 

Obviously change the stuff in the middle that I put in brackets.

=== Setting up Firewall ===

If you rebooted now and ran ifup.wlppp, your router would be on the internet, but not much else would be. Let's change that.
Edit your S45firewall so that all of the "wan" references become "ppp0" references.

==== /etc/init.d/S45firewall changes ====
{{{
WAN=ppp0
}}}

I mean, duh, but it took me a while to figure it out. Take firmware original, and pop this line where WAN=whatever was.

=== Finishing up ===

If you want the internet to come up on router boot, put 'ifup.wlppp' in your S40network, towards the end.

Now ''nvram commit'', reboot, and hope it works!

Your clients should be set to grab DNS via DHCP from the router, but if not, get the DNS server addresses, and give them to the clients.

Have fun with a 25 watt internet gateway! 
