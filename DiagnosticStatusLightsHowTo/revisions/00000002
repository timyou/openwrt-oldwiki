'''Diagnostic Status Lights Howto'''

 * Many devices supported by !OpenWrt have controllable diagnostic lights, described in ["wrtLEDCodes"]. They are controllable through {{{/proc/sys/diag}}}. 
 *A script to control diagnostic lights:

{{{
#!/bin/sh
led=0
read led </proc/sys/diag
# from http://wiki.openwrt.org/wrtLEDCodes
res=0
case "$1" in
  dmz)
    res=1
  ;;
  power)
    res=4
  ;;
  cisco_white)
    res=8
  ;;
  cisco_yellow)
    res=16
  ;;
  all)
    res=255
  ;;
  *)
    echo "Usage: $0 Light [on|off]"
    echo "  Light can be: "
    echo "    dmz  "
    echo "    power"
    echo "    cisco_white"
    echo "    cisco_yellow"
    echo "    all"
    echo "  If on or off is not specified, cycles light."
    echo "Example: $0 cisco_white on"
    exit
  ;;
esac
val="0"
case "$2" in
  on)
    val=$(($res | $led))
  ;;
  off)
    val=$(((0xff & ~$res) & $led))
  ;;
  *)
    if test "$(($led & $res))" -eq "$res";
    then echo off;$0 $1 off;exit;
    else echo on;$0 $1 on;exit;
    fi
  ;;
esac
echo $val >> /proc/sys/diag
}}}
 *This script should be put in {{{/bin}}}, or anywhere in the path, really.
 *Do '''not''' forget to {{{chmod +x}}} it. So, if you called the script {{{/bin/diag}}}, do not forget to {{{chmod +x /bin/diag}}}
 *It can be invoked as {{{diag power on}}}, which would make the power light blink.
 *Other ways to invoke it:
{{{
diag power
diag dmz on
diag dmz off
diag all off
}}}
 *When no lighting option is specified, the light is cycled. So, {{{off->on->off->...}}}.
 *Uses:
 *Put in {{{/etc/ppp/if-up}}} and similar to light up the cisco light when a VPN connection is up.
 *The file {{{/etc/inid.d/S90shorewall}}} makes the power light blink while shorewall is starting:
{{{
#!/bin/sh
diag power on
echo "Launching ShoreWall"
sleep 120
# Lockfile, use a volatile area (like /tmp)
LOCK=/tmp/shorewall.lock
if [ ! -f /tmp/shorewall.lock ]; then
/sbin/shorewall start
diag power off
fi
}}}
