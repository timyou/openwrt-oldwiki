= Downloading needed things =
 * first you have to add Nico's testing directory to your /etc/ipkg.conf
  . add
  {{{
  src unstable http://downloads.openwrt.org/people/nico/testing/mipsel/packages/ }}}
  to your ipkg.conf
  . '''The URL above is not valid!'''
  . Use
  {{{
  src unstable http://home.mag.cx/openwrt/packages/ }}}
  instead
  . '''This URL stopped working 2006-08-11'''

 * update your ipkg database and install the needed rrdtool
  . {{{
  ipkg update
  ipkg install rrdtool1 }}}
  now you should have rrdtool and rrdupdate installed

 * have a look if your iptables are able to monitor traffic
  . {{{
  iptables -N traffic
  iptables -F traffic
  iptables -I FORWARD -j traffic }}}
  if you receive an error make sure
  * you have all necessary packages installed
  * the kernel-modules are loaded
  * make sure, that the traffic-chain exists after booting. (Just add the iptable-commands to a start-up script. Remember to load the needed kernel-modules befor running the iptable-stuff)

  * To Create the start-up script:
  {{{
  cat > /etc/init.d/S50rrd
  }}}
  {{{
  #!/bin/sh
  iptables -N traffic
  iptables -F traffic
  iptables -I FORWARD -j traffic
  }}}
  After pasting it, press {{{ENTER}}} and then hit {{{CTRL-D}}} keys to save the file. Now make sure the init script is executable and start it with
  {{{
  chmod a+x /etc/init.d/S50rrd
  /etc/init.d/S50rrd start
  }}}
  now you are capable to monitor traffic with iptables

= Using the traff_graph - script =
Place the following script in /sbin or where you like

{{{
cat > /sbin/traff_graph
}}}

{{{
#!/bin/sh

# traff_graph version 0.0.2 by twist
# script for monitoring mac-based traffic on an openwrt-box
# comments, suggestion, patches .... --> twist _at_ evilhome _dot_ de

SITENAME="tuxland"      # change for your site

mkdir -p /tmp/rrd

iptables -L traffic -vnxZ -t filter > /tmp/traffic.tmp

ALL_UP=0
ALL_DOWN=0
INDEX="<html><head><title>traffic @ $SITENAME</title></head><body>"

# $1 = ImageFile, $2 = Time in secs to go back, $3 = RRDfile, $4 = GraphText
CreateGraph ()
{
        # only run, if no other rrdtool is running
        if [ -n "$(ps | grep rrdtool | grep -v grep)" ] ; then
                return
        fi

        rrdtool graph "${1}" -a PNG -s -"${2}" -w 550 -h 240 -v "bytes/s" \
                'DEF:in='${3}':down:AVERAGE' \
                'DEF:out='${3}':up:AVERAGE' \
                'CDEF:out_neg=out,-1,*' \
                'AREA:in#32CD32:Incoming' \
                'LINE1:in#336600' \
                GPRINT:in:"MAX:  Max\\: %5.1lf %s" \
                GPRINT:in:"AVERAGE: Avg\\: %5.1lf %S" \
                GPRINT:in:"LAST: Current\\: %5.1lf %Sbytes/sec\\n" \
                'AREA:out_neg#4169E1:Outgoing' \
                'LINE1:out_neg#0033CC' \
                GPRINT:out:"MAX:  Max\\: %5.1lf %S" \
                GPRINT:out:"AVERAGE: Avg\\: %5.1lf %S" \
                GPRINT:out:"LAST: Current\\: %5.1lf %Sbytes/sec" \
                'HRULE:0#000000' -t "${4}"
}

for MAC in $(cat /proc/net/arp | grep -v address | awk '{print $4}') ; do
        MAC_=$(echo $MAC | sed 's/:/-/g')
        IP=$(cat /proc/net/arp | grep $MAC | awk '{print $1}')
        # This assumes that a local dns server (like dnsmasq) is running
        NAME=$(nslookup $IP 127.0.0.1 | grep "Name:" | awk '{print $2}')
        # echo "mac: $MAC ip: $IP_ name: $NAME"

        UP=$(cat /tmp/traffic.tmp | awk '{print $2 " " $7}' | grep $IP | awk '{print $1}' | tr -d '\n' )
        UP=$(($UP+0))
        ALL_UP=$(($ALL_UP+$UP))
        DOWN=$(cat /tmp/traffic.tmp | awk '{print $2 " " $8}' | grep $IP | awk '{print $1}' | tr -d '\n' )
        DOWN=$(($DOWN+0))
        ALL_DOWN=$(($ALL_DOWN+$DOWN))

        # create db if not exists
        if [ ! -e /tmp/rrd/${MAC_}.rrd ] ; then
                # echo creating /tmp/rrd/${MAC_}.rrd
                iptables -A traffic -s $IP
                iptables -A traffic -d $IP

                rrdtool create /tmp/rrd/${MAC_}.rrd -s 300 \
                        DS:up:ABSOLUTE:600:0:600000000 \
                        DS:down:ABSOLUTE:600:0:600000000 \
                        RRA:AVERAGE:0.5:1:2016 \
                        RRA:AVERAGE:0.5:3:2688 \
                        RRA:AVERAGE:0.5:12:6360
        fi

        # echo "up: $UP down: $DOWN"
        rrdtool update /tmp/rrd/${MAC_}.rrd N:$UP:$DOWN

        CreateGraph "/tmp/rrd/${MAC_}.day.png" 86400 /tmp/rrd/${MAC_}.rrd "IP: $IP MAC: $MAC_ Host: $NAME"
        INDEX=$INDEX"<img src='${MAC_}.day.png'><br>"

        # traffic/week
        # i don´t use this
        # CreateGraph "/tmp/rrd/${MAC_}.week.png" 604800 /tmp/rrd/${MAC_}.rrd "IP: $IP MAC: $MAC_ Host: $NAME"
        # INDEX=$INDEX"<img src='${MAC_}.week.png'><br>"
done

# build sum-graph
if [ ! -e /tmp/rrd/all.rrd ] ; then
        rrdtool create /tmp/rrd/all.rrd -s 300 \
                DS:up:ABSOLUTE:600:0:600000000 \
                DS:down:ABSOLUTE:600:0:600000000 \
                RRA:AVERAGE:0.5:1:2016 \
                RRA:AVERAGE:0.5:3:2688 \
                RRA:AVERAGE:0.5:12:6360
fi

rrdtool update /tmp/rrd/all.rrd N:$ALL_UP:$ALL_DOWN
CreateGraph /tmp/rrd/all.png 86400 /tmp/rrd/all.rrd "all traffic from $SITENAME"

INDEX=$INDEX"<br><img src='all.png'></body></html>"

echo $INDEX > /tmp/rrd/index.html
}}}

Make the file executable

{{{
chmod a+x /sbin/traff_graph
}}}

This script will create and update the rrd-database for each mac found in /proc/net/arp. If a host is not online no update will be performed. This will safe some cpu-cycles :) . traff_graph stores the rrd-db, the created pictures/graphs and the index.html for viewing the graphs in /tmp/rrd. This means, after a reboot all informations are lost and you will start at 0.

Now you can test traff_graph. Make sure, you have only a single traffic-chain/host in your iptable rules. You can list this with

{{{
iptables -L traffic -vx}}}

Now run traff_graph. This will need a while... get a coffee ;-) Add traff_graph to your crontab and run it every 5 minutes. Be carefull not to monitore to much hosts since rrdtool graph needs a lot of time. For viewing the graphs you have to add an symlink in /www which points to /tmp/rrd.

{{{
cd /www
ln -s /tmp/rrd/ traffic }}}

everything will be available via

{{{
http://192.168.0.1/traffic/ }}}

To schedule an update every 5 minutes, use crontab.

Add this to the /etc/crontabs/root file :

{{{
# create traffic graphs every 5 minutes (i.e. run if minutes mod 5 == 0)
0/5 * * * * /sbin/traff_graph > /dev/null 2>&1}}}

= Other links =
[http://forum.openwrt.org/viewtopic.php?id=3741]
