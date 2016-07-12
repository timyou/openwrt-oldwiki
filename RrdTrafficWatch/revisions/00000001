= Downloading needed things =

* first you have to add Nico's testing directory to your /etc/ipkg.conf
  add
  {{{
  src unstable http://downloads.openwrt.org/people/nico/testing/mipsel/packages/ }}}
  to your ipkg.conf

* update your ipkg database and install the needed rrdtool
  {{{
  ipkg update
  ipkg rrdtool }}}
  now you should have rrdtool and rrdupdate installed

* have a look if your iptables are able to monitor traffic
  {{{
  iptables -N traffic
  iptables -F traffic
  iptables -I FORWARD -j traffic }}}
  if you receive an error make sure
  * you have all necessary packages installed (I think, kmod-ipt-ipopt is needed for traffic)
  * the kernel-modules are loaded
  now you are capable to monitor traffic with iptables

= Using the traff_graph - script =

Place the following script in /sbin or where you like

{{{
#!/bin/sh

# traff_graph version 0.01 by twist
# script for monitoring mac-based traffic on an openwrt-box
# comments, suggestion, patches .... --> twist _at_ evilhome _dot_ de

if [ ! -d /tmp/rrd ]
then
        mkdir /tmp/rrd
fi

iptables -L traffic -vnxZ -t filter > /tmp/traffic.tmp

echo "<html><head><title>traffic @ tuxland</title></head><body>" > /tmp/rrd/index.html

# $1 = ImageFile , $2 = Time in secs to go back , $3 = RRDfil , $4 = GraphText 
CreateGraph ()
{
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

for MAC in $(cat /proc/net/arp | grep -v address | awk '{print $4}')
do
        MAC_=$(echo $MAC | sed 's/:/-/g')
        IP=$(cat /proc/net/arp | grep $MAC | awk '{print $1}')
        # no better way??? i hate this
        NAME=$(nslookup $IP | grep "Name:" | awk '{print $2}')
        # debug
        # echo "mac: $MAC ip: $IP_ name: $NAME"

        # create db if not exists
        if [ ! -e /tmp/rrd/${MAC_}.rrd ]
        then
                # debug
                # echo "creating new /tmp/rrd/${MAC_}.rrd"
                iptables -A traffic -s $IP
                iptables -A traffic -d $IP

                rrdtool create /tmp/rrd/${MAC_}.rrd -s 300 \
                        DS:up:ABSOLUTE:600:0:600000000 \
                        DS:down:ABSOLUTE:600:0:600000000 \
                        RRA:AVERAGE:0.5:1:2016 \
                        RRA:AVERAGE:0.5:3:2688 \
                        RRA:AVERAGE:0.5:12:6360
        fi

        UP=$(cat /tmp/traffic.tmp | awk '{print $2 " " $7}' | grep $IP | awk '{print $1}')
        UP=$(($UP+0))
        DOWN=$(cat /tmp/traffic.tmp | awk '{print $2 " " $8}' | grep $IP | awk '{print $1}')
        DOWN=$(($DOWN+0))

        # debug
        # echo "up: $UP down: $DOWN"
        rrdtool update /tmp/rrd/${MAC_}.rrd N:$UP:$DOWN

        # traffic/day
        CreateGraph "/tmp/rrd/${MAC_}.day.png" 86400 /tmp/rrd/${MAC_}.rrd "IP: $IP MAC: $MAC_ Host: $NAME"
        echo "<img src='${MAC_}.day.png'><br>" >> /tmp/rrd/index.html

        # traffic/week
        # i don´t use this
        # CreateGraph "/tmp/rrd/${MAC_}.week.png" 604800 /tmp/rrd/${MAC_}.rrd "IP: $IP MAC: $MAC_ Host: $NAME"
        # echo "<img src='${MAC_}.week.png'><br>" >> /tmp/rrd/index.html

done

echo "</body></html>"  >> /tmp/rrd/index.html
}}}

This script will create und update the rrd-database for each mac found in /proc/net/arp. If a host is not online no update will be performed. This will safe some cpu-cycles :) . traff_graph stores the rrd-db, the created pictures/graphs and the index.html for viewing the graphs in /tmp/rrd. This means, after a reboot all information is lost and you will start at 0.
