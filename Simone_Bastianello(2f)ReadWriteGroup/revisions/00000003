## Please edit system and help pages ONLY in the moinmaster wiki! For more
## information, please see MoinMaster:MoinPagesEditorGroup.
##acl MoinPagesEditorGroup:read,write,delete,revert All:read
##master-page:HelpTemplate
##master-date:Unknown-Date
#format wiki
#language en
== OpenWrt as failover router ==
In this small how-to we will explain hot to set up an OpenWrt router as a failover router in order to provide quick and automatic switchover from a dead Internet connection (the primary ppp connection) to an operational one (i.e. a secondary connection on a different router).

=== Setting up routing ===
Assuming your secondary router has been already configured, you just need to add this router as default gateway on the OpenWrt. Add these lines on /etc/config/network:

{{{
config route backup
        option interface lan
        option target 0.0.0.0
        option netmask 0.0.0.0
        option gateway <<GATEWAY_IP>>
        option metric <<METRIC>>
}}}
where GATEWAY_IP is the secondary gateway address and METRIC is expected to be 1 or more in order to set lower priority compared to the primary connection.

Now you will have to setup the time (seconds)  after which the kernel declares a route to be inactive and it automatically switches to the other route. Add this line to /etc/sysctl.conf:

{{{
net.ipv4.route.gc_timeout=5
}}}
 . to enable automatical configuration on boot time or execute
{{{
echo 5 > /proc/sys/net/ipv4/route/gc_timeout
}}}
if you wish to find the best value for you.

=== Setting up pppd ===
You also need some small changes on ppp configuration. Delete the following line:

{{{
replacedefaultroute \
}}}
from /lib/network/ppp.sh in order to prevent pppd from replacing your default route. Now you will have to manage routing as ppp connection goes up or down. Save this script

{{{
#!/bin/sh
case "$ACTION" in
 ifup)
   /sbin/route add default gw <<PPPGATEWAY_IP>> metric 0
   ;;
ifdown)
  /sbin/ route del default gw <<PPPGATEWAY_IP>> metric 0
   ;;
esac
}}}
to /etc/hotplug.d/iface/00-route where <<PPPGATEWAY_IP>> is usually 192.168.100.1 on an adsl connection.

----
=== Setup for german DSL ===
In Germany there is something like a forced disconnect of the pppoe-connection every 24h, so the remote IP of the pppoe-tunnel is not static and has to be set dynamically. The solution is the following:

Add PPP_REMOTE="$PPP_REMOTE" to line 9 of /etc/ppp/ip-up:

{{{
[ -z "$PPP_IPPARAM" ] || env -i ACTION="ifup" INTERFACE="$PPP_IPPARAM" PPP_REMOTE="$PPP_REMOTE" DEVICE="$PPP_IFACE" PROTO=ppp /sbin/hotplug-call "iface"}}}
The hotplug-script then looks like this:

{{{
#!/bin/sh
if [ "$INTERFACE" = "wan" ]; then
  case "$ACTION" in
    ifup)
      /sbin/route add default gw $PPP_REMOTE metric 0
      ;;
    ifdown)
      /sbin/route del default gw $PPP_REMOTE metric 0
      ;;
 esac
fi
}}}
Thanks to cato for this update!

CategoryHowTo
