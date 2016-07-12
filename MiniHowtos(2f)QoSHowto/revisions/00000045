/!\ '''This page is currently under construction''' /!\

[[TableOfContents]]

= Qos MiniHowto =

== Boring Intro and Dry Theory ==

Someone once said technical guys hate writing documentation.  I guess they were right.  Disclaimer: I'm a network nerd and admin at an ISP.  My hope is I'll start this and someone will jump in and clean it up. If you already know what it is, and don't want to ridicule me, you can skip this part.

Anyhow.  This document will outline a bit what QoS is, and two great ways to do it.  As far as I was concerned, it was the single most important feature of the (or any) router.  It allows for bandwidth management and prioritization.

How does it do this?  Well, let's consider how the internet works.  Here's the watered-down version.  It's a big network, it has routers and servers and PCs, all these have interfaces.  A network device puts packets on the wire by placing them in a queue for it's interfaces.  With Qos, we can manipulate that queue.

See, everyone thinks they want more bandwidth.  That's not entirely true.  We all use the internet differently and the way I use it, may not be the same as the way you do.  What we need is '''''bandwidth management'''''.  And because I don't use it the way you do, my management will be different than yours.  If we can avoid excess queing at the ISP, and manage our own queues, locally, the internet will be efficient for us, and our most important traffic will always get out.

So back to the interface queue.  Imagine you're working at work, and your boss says "Johnson, this is important, drop what you're doing and take care of this now!" you do so.  You've just prioritized whatever it was he wanted done.  You've shoved it to the top of the queue.  Or, based on your policies , you've told him to shove it up his queue and you have better things to do.

To make a long, boring, drawn out story short, there are two parts.  The interesting traffic, and the policy.  Interesting traffic is usually marked somehow... the policy dictates what's to be done with how it was marked.

So, for a simple example.  You could have broken your queue into three parts, or buckets.  One bucket is High, one is Normal, one is Low.  Ssh traffic is important to me, so I would mark that traffic as high.  How can I do this?  With netfilter (iptables).  I just say, all port 22 traffic is marked as 1 (which may be my "high" number).  Sip traffic (voip) is important too.  But sip can be a tricky protocol.  It uses udp and starts with port 5060, then gets really funky.  So either I mark those packets with an application level marker (L7 filter) or do something simple, like mark any traffic coming from my MAC address of my ATA as 1, High.  Then let's say I don't care about web traffic (but other folks in my household still do), so we'll leave that at 2, Normal.  But I despise peer-to-peer applications.  I'll stick them in 3, Low.

These three buckets might be named something entirely different as well.  Such as "Priority", "Normal" and "Bulk".  The beginning of the policy is how this traffic is divided up.  You can't prioritize something if you don't create a bucket to put it in.  Likewise, if you prioritize everything (or only have one bucket), nothing is prioritized.

So your goal here, is to, define policies, mark interesting traffic... and avoid congestion at your ISP.  My ISP provides 8mbit download and 512kbit upload.  That's quite a bit.  If I want to send more than 512kbit, my information is queued in their router (or modem, as it were).

So my information may have to wait in an outbound queue.  This slows things down... and brings up the fundamental differences between what people percieve as speed and bandwidth... when they're really dealing with latency and bandwidth.  But that's for another discussion.

Which brings up another interesting question.  Sure, I can manage what I send out (upload) but how do I manage what's being sent to me (download)?  If you're playing catch with someone, that's great, you can throw however you want, but if the guy at the other end is a major league baseball player, how're you going to stop Jose from ripping your hand off with a fastball?

To be honest, and candid, most of the time you do not want download (or ingress) management.  I have 8mbit at home, and it's very rare that I find a site that sends that to me.  Most residential connections are asynchronous, and you have multitudes more download bandwidth than upload.  But there are methods (in tcp, for example) to ask a session to "slow down" when things come in quickly.  But most people will want to manage their outbound bandwidth solely.

Last but not least... it should be mentioned, exactly how the queing is performed.  Most default queues are "fifo" meaning first-in first-out.  You get in line and get processed in the order by which you came.  This describes the queing discipline, as well as the type of queue.  There are other algorithims for queing disciplines, other types, such as htb ([http://luxik.cdi.cz/~devik/qos/htb/ Hierarchichal Token Bucket]) and hfsc ([http://www.cs.cmu.edu/~hzhang/HFSC/main.html Hierarchical Fair Service Curve]).  For more information on queues and advanced routing in general, see [http://lartc.org/ Linux Advanced Routing & Traffic Control].  Note these are also referred to as "packet schedulers".

== QoS in OpenWrt ==

I went from not having a QoS option (well, to be honest, the tools were always there, just needed a sane script) to having two options.  Debate as to which is the "better" one is probably not important.  I'd personally call them "two great ways to do it".

One involves nbd's qosif scripts.  And the other involves ctshaper, a script written by Carlos Rodrigues, based on wondershaper.  These two guys deserve the credit for the scripts I'm going to mention.

Perhaps I can outline the pros and cons of each.  But there's a few things you will need to get started.  For both sets of scripts, at a bare minimum, you should have the tc, ip and kmod-sched packages.

=== qosfw-scripts package (was qosif) ===

(''Somewhat updated for qosfw-scripts, could use some editing'')
----

If looking at someone's code, you can peer into their minds, then there's much to be said about these scripts. It's small, fast, efficient, and does just about all the heavy lifting for you.  

Install qosfw-scripts with {{{ipkg install http://openwrt.inf.fh-brs.de/~nbd/qosfw-scripts_0.5_all.ipk}}} (you many want to check [http://openwrt.inf.fh-brs.de/~nbd/ here] for a newer update.

{{{
/etc/config/firewall
/etc/config/qos-wan
/etc/hotplug.d/iface/10-qos
/usr/lib/qosfw/qos.awk
/usr/lib/qosfw/common.awk
/usr/lib/qosfw/firewall.awk
/usr/lib/qosfw/fw.sh
}}}

The files in /usr/lib/qosfw do the heavy lifting. 
`/etc/hotplug.d/iface/10-qos` is run everytime an interface is brought up, and looks for a qos-[interface] file in `/etc/config`, if it finds one then it'll setup the qos settings for that interface.

Which leaves us with the format of the `config` file.  It's formatted in stanzas (I did say that nbd guy was pretty clever, right?) and the stanzas can be broken down into policies and marking rules.

For example, the first four stanzas (or blocks) are policies:

{{{
class:Priority
pktsize:150        
pktdelay:10                            
avgrate:20 
share:75                                                 
end                                           
               
class:VOIP                                 
pktsize:200                                                          
pktdelay:10                              
avgrate:30                                   
share:75                                    
end                                                               
                                         
class:Normal                
pktsize:1500    
pktdelay:30                                 
avgrate:10                                                         
share:50                 
end                                                            
                                                              
class:Bulk                                                      
share:10                       
limit:90                                  
end
}}}

This first part of the config file sets up our 4 buckets.  (''Fix this to correspond to pktsize/pktdelay/avgrate/share'') "Class" names the policy, "maxdelay" is the maximum delay we would like to craft (in ms).  "Rate" and "limit" are pretty self-explainatory, in kbits/sec.  Last but not least, is the type of queue (priority, normal, bulk) and of course the end of the config file.

The next section of the config file crafts the rules for marking, in iptables:

{{{
classify:Bulk:layer7=edonkey
classify:Priority:proto=udp dport=53,5190
classify:Priority:proto=tcp dport=22,53,5190
#classify:VOIP:proto=tcp sport=60168
#classify:VOIP:proto=udp sport=60168
}}}

These are pretty self explainatory as well.  The first line uses a layer7 filter (the patterns for these are stored in /etc/l7-protocols, see [http://l7-filter.sourceforge.net/protocols l7-filter] for more) to classify edonkey traffic as bulk. The others all classify by port 
numbers.

Take the second and third examples.  Anything with a destination of udp/53 or udp/5190 (dns and aim, respectively), will be classified as Priority.  Pretty simple, huh?

Next, we enable qos, and set the up/downstream bandwidth
{{{
#option:enabled
option:upload:128
option:download:1024
}}}

Uncomment the option:enabled line, or else you'll wonder why this isn't doing anything.
The upload and download lines should be set to your connection speeds in kbps.

(''TODO: document this section'')
{{{
option:priority:Priority
option:bulk:Bulk
option:defaultlow:Normal
option:default:Bulk
option:bulk_dl:Normal:10
}}}

Finally to activate your settings run ` ifdown wan && ifup wan `. 

You can see what commands the script is running by looking at `/tmp/.qos-wan.sh`. You can get an idea of how much traffic is hitting each of your rules with `iptables -t mangle -L -v`

So, '''qosfw''' in three steps:

 * install the package
 * modify `/etc/config/qos-wan` to suit your needs, don't forget the option:enabled line
 * `ifdown wan && ifup wan` to activate

==== Notes and Caveats ====

 * There is no ingress capabilities.  As I mentioned earlier, most people won't want that anyhow.
 * Rules like the first ''edonkey'' one above require the L7 filter from [http://l7-filter.sourceforge.net] (this is now a dependency of the package).
 * You might need other packages, like the ''iptables-extra'' package for fancy marking of packets.
 * Based on `hfsc` packet scheduler, not `htb`.  You may be more familiar with one over the other.
 * See http://forum.openwrt.org/viewtopic.php?id=3847 for a possible issue with the full link speed not being used when using this script (v0.4&0.5) in some instances.

=== ctshaper ===

/!\ '''NOTE:''' ctshaper is not supported by the !OpenWrt developers!

First, download the script from [http://students.fct.unl.pt/~cer09566/ctshaper/ this link].  Tarball is at the bottom of the page.  I made it work for me with a few changes.

I chose not to use the install script.  I changed the following values in the '''ctshaper''' file:

{{{
from:

#!/bin/bash

to:

#!/bin/sh


from:

TC="/sbin/tc"

to:

TC="/usr/sbin/tc"


from:

source ${CONFIG_FILE}

to:

. ${CONFIG_FILE}


from:

DEFAULT_RATE=$[${UPLINK} - ${CLASS1_RATE} - ${CLASS2_RATE} - ${CLASS3_RATE}]

to:

DEFAULT_RATE=$((${UPLINK} - ${CLASS1_RATE} - ${CLASS2_RATE} - ${CLASS3_RATE}))
}}}

I then copied it to `/usr/sbin/ctshaper` on the OpenWRT router.

Next, modify `ctshaper.conf` to suit your needs, and copy over to `/etc/ctshaper/ctshaper.conf` on the router.

Then, I made a file called `S75qos` and put it in `/etc/init.d/` ... it's just a copy of the `crond` init script, modified a bit:

{{{
#!/bin/sh
#
# Starts ctshaper
#

mods="sch_sfq sch_ingress sch_htb cls_u32 cls_fw"

CTSHAPER=/usr/sbin/ctshaper

start() {
        echo "Starting ctshaper: "
        for m in $mods
          do insmod $m >/dev/null 2>&1
        done
        $CTSHAPER start
}
stop() {
        echo "Stopping ctshaper: "
        $CTSHAPER stop
        for m in $mods
          do rmmod $m >/dev/null 2>&1
        done
}
restart() {
        stop
        start
}
status() {
        $CTSHAPER status
}

case "$1" in
  start)
        start
        ;;
  stop)
        stop
        ;;
  restart|reload)
        restart
        ;;
  status)
        status
        ;;
  *)
        echo $"Usage: $0 {start|stop|restart|status}"
        exit 1
esac

exit $?
}}}

That's it!  Now when you reboot, your QoS will be applied at bootup.  Notice, with this setup, you must mark your own packets, possibly in `/etc/firewall.user`.

Try issuing the command `ctshaper status` to see current configuration.

==== Notes and Caveats ====

 * As I said, it requires you to mark your own packets.  Not as elegant as the '''qosif''' script, but it works.
 * Necessary to modify it a bit first to get it working.
 * Based on `htb` packet scheduler, not `hfsc`.

==== Iptables packet marking ====

Here are some examples for marking traffic with iptables - only needed when using the ctshaper script.

In this example, the packets are marked as follows:
{{{
1: ICMP, SSH
2: IRC, Quake1, Skype to Skype calls
3: All other traffic (the default priority)
4: p2p (Bittorrent, Direct Connect)
}}}

The example goes as follows:
{{{
#load the layer7 iptables module
insmod ipt_layer7

#flushing chain
iptables -t mangle -F POSTROUTING

iptables -t mangle -A POSTROUTING -o $WAN -p icmp -j MARK --set-mark 1
iptables -t mangle -A POSTROUTING -o $WAN -p tcp --dport 22 -j MARK --set-mark 1
iptables -t mangle -A POSTROUTING -o $WAN -p tcp --sport 22 -j MARK --set-mark 1

#quake
iptables -t mangle -A POSTROUTING -o $WAN -p udp --dport 26000 -j MARK --set-mark 2
iptables -t mangle -A POSTROUTING -o $WAN -p udp --sport 26000 -j MARK --set-mark 2

#irc
iptables -t mangle -A POSTROUTING -o $WAN -m layer7 --l7proto irc -j MARK --set-mark 2
#skype to skype VoIP calls
iptables -t mangle -A POSTROUTING -o $WAN -m layer7 --l7proto skypetoskype -j MARK --set-mark 2

#all unmarked packets
iptables -t mangle -A POSTROUTING -o $WAN -m mark --mark 0 -j MARK --set-mark 3

#p2p
iptables -t mangle -A POSTROUTING -o $WAN -m layer7 --l7proto bittorrent -j MARK --set-mark 4
iptables -t mangle -A POSTROUTING -o $WAN -m layer7 --l7proto directconnect -j MARK --set-mark 4
}}}

Note that you could mark the packets in any of the mangle table's chains, however most likely the best choice would be POSTROUTING, as used in this example. There are two reasons for that:
 * You only need to match packets going out on the WAN interface, so you can use the -o parameter (which doesn't exist in PREROUTING).
 * You also match locally generated packets (which isn't true for the FORWARD chain).
