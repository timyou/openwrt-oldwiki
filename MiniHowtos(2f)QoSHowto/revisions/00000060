/!\ '''This page needs an update!''' /!\

[[TableOfContents]]
= Qos MiniHowto =
== Boring Intro and Dry Theory ==
/!\ '''This page needs an update!''' /!\
This document will outline a bit what QoS is, and two great ways to do it.  QoS may be the single most important feature of a router.  It allows for bandwidth management and prioritization.

How does it do this?  Well, let's consider how the internet works.  Here's the watered-down version.  It's a big network, it has routers and servers and PCs, all these have interfaces.  A network device puts packets on the wire by placing them in a queue for it's interfaces.  With Qos, we can manipulate that queue.

See, everyone thinks they want more bandwidth.  That's not entirely true.  We all use the internet differently and the way I use it, may not be the same as the way you do.  What we need is '''''bandwidth management'''''.  And because I don't use it the way you do, my management will be different than yours.  If we can avoid excess queing at the ISP, and manage our own queues, locally, the internet will be efficient for us, and our most important traffic will always get out.

So back to the interface queue.  Imagine you're working at work, and your boss says "Johnson, this is important, drop what you're doing and take care of this now!".  You've just prioritized whatever it was he wanted done.  You've shoved it to the top of the queue.  Or, based on your policies , you've told him to shove it up his queue and you have better things to do.

To make a long, boring, drawn out story short, there are two parts.  The interesting traffic, and the policy.  Interesting traffic is usually marked somehow... the policy dictates what's to be done with how it was marked.

So, for a simple example.  You could have broken your queue into three parts, or buckets.  One bucket is High, one is Normal, one is Low.  SSH traffic is important to me, so I would mark that traffic as high.  How can I do this?  On Linux, with netfilter (iptables).  I just say, all port 22 traffic is marked as 1 (which may be my "high" number).  SIP/VOIP traffic is important too.  But SIP can be a tricky protocol.  It uses UDP and starts with port 5060, then gets really funky.  So either I mark those packets with an application level marker (L7 filter) or do something simple, like mark any traffic coming from my MAC address of my ATA as 1, High.  Then let's say I don't care about web traffic (but other folks in my household still do), so we'll leave that at 2, Normal.  But I despise peer-to-peer applications.  I'll stick them in 3, Low.

These three buckets might be named something entirely different as well.  Such as "Priority", "Normal" and "Bulk".  The beginning of the policy is how this traffic is divided up.  You can't prioritize something if you don't create a bucket to put it in.  Likewise, if you prioritize everything (or only have one bucket), nothing is prioritized.

So your goal here is to define policies, mark interesting traffic, and avoid congestion at your ISP.  My ISP provides 8 Mbps download and 512 Kbps upload.  That's quite a bit.  If I want to send more than 512 Kbps, my information is queued in their router (or modem, as it were).

So my information may have to wait in an outbound queue.  This slows things down and brings up the fundamental differences between what people percieve as speed and bandwidth, when they're really dealing with latency and bandwidth.  But that's for another discussion.

Which brings up another interesting question.  Sure, I can manage what I send out (upload) but how do I manage what's being sent to me (download)?  If you're playing catch with someone you can throw however you want, but if the guy at the other end is a major league baseball player, how are you going to stop Jose from ripping your hand off with a fastball?

To be honest, most of the time you do not want download (or ingress) management.  I have 8 Mbps at home, and it's very rare that I find a site that sends that to me.  Most residential connections are asymmetic, and you have much more download bandwidth than upload.  But there are methods (in TCP, for example) to ask a session to "slow down" when things come in quickly.  But most people will want to manage their outbound bandwidth solely.

Last but not least it should be mentioned exactly how the queing is performed.  Most default queues are "fifo" meaning first-in first-out.  You get in line and get processed in the order by which you came.  This describes the queing discipline, as well as the type of queue.  There are other algorithims for queing disciplines, such as HTB ([http://luxik.cdi.cz/~devik/qos/htb/ Hierarchichal Token Bucket]) and HFSC ([http://www.cs.cmu.edu/~hzhang/HFSC/main.html Hierarchical Fair Service Curve]).  For more information on queues and advanced routing in general, see [http://lartc.org/ Linux Advanced Routing & Traffic Control].  Note these are also referred to as "packet schedulers".

== QoS in OpenWrt ==
'''New 2006-07-02''' QoS in OpenWrt can be done with nbd's '''qos-scripts''' package. The other options mentioned here are outdated, as far as I can see. So only try them if you know what you are doing!
Inexperienced users should stick with '''qos-scripts'''.

Old text (please delete if appropriate!): ''I went from not having a QoS option (well, to be honest, the tools were always there, just needed a sane script) to having two options.  Debate as to which is the "better" one is probably not important.  I'd personally call them "two great ways to do it".
One involves nbd's qosif scripts.  And the other involves ctshaper, a script written by Carlos Rodrigues, based on wondershaper.  These two guys deserve the credit for the scripts I'm going to mention.
Perhaps I can outline the pros and cons of each.  But there's a few things you will need to get started.  For both sets of scripts, at a bare minimum, you should have the tc, ip and kmod-sched packages.''

=== qos-scripts package ===
QoS in !OpenWrt is based on {{{tc}}}, [http://www.cs.cmu.edu/~hzhang/HFSC/main.html HFSC] and [http://l7-filter.sourceforge.net/ Layer 7 filters]. The QoS package only works in White Russian RC5 and later version. With the {{{qos-scripts}}} package (version 0.4 and later) it's also possible to setup simple port forwarding rules in in the config file.

==== Installation ====
Download and install the {{{qos-scripts}}} package from http://downloads.openwrt.org/people/nbd/qos/
{{{
ipkg install qos-scripts
}}}

==== Configuration ====
Then edit {{{/etc/config/qos}}}. This file has a number of examples and the syntax description in it. Be sure to set the {{{option:upload}}} and {{{option:download}}} correctly, as the package is enabled by default! The units for {{{option:upload}}} and {{{option:download}}} are ''kilobits/second''

If you don't configure port forwarding in {{{/etc/config/qos}}} then you can use {{{/etc/firewall.user}}} as normal for iptables rules.

{{{qos-scripts}}} depends on the {{{iptables-mod-filter}}} package, so you can use L7 filters with extra configuration. This package contains a few L7 filters. Alternativly you can download extra filters from [http://l7-filter.sourceforge.net/protocols Layer 7 filters] and save the {{{.pat}}} files into the {{{/etc/l7-protocols}}} directory.

==== Starting ====
Start the script and make sure it starts after a reboot
{{{
/etc/init.d/qos start
/etc/init.d/qos enable
}}}

==== Starting - alternative ====
Finally start QoS with

{{{
ifup wan
}}}

This calls the QoS script via the hotplug code.

Then do a
{{{
env -i ACTION=ifup INTERFACE=wan /sbin/hotplug iface
}}}

This simulates a ifup on the WAN interface and reruns the hotplug scripts.

==== Checking ====
To show the QoS related rules execute:

{{{
iptables -L -v -t mangle
}}}

You should see output similar to the following:
{{{
Chain PREROUTING (policy ACCEPT 49M packets, 42G bytes)
 pkts bytes target     prot opt in     out     source               destination
  31M   38G Default    all  --  ppp0   any     anywhere             anywhere
  31M   38G IMQ        all  --  ppp0   any     anywhere             anywhere            IMQ: todev 0

Chain INPUT (policy ACCEPT 121K packets, 16M bytes)
 pkts bytes target     prot opt in     out     source               destination

Chain FORWARD (policy ACCEPT 49M packets, 42G bytes)
 pkts bytes target     prot opt in     out     source               destination
  18M 4172M Default    all  --  any    ppp0    anywhere             anywhere

Chain OUTPUT (policy ACCEPT 113K packets, 16M bytes)
 pkts bytes target     prot opt in     out     source               destination
75940 8011K Default    all  --  any    ppp0    anywhere             anywhere

Chain POSTROUTING (policy ACCEPT 49M packets, 42G bytes)
 pkts bytes target     prot opt in     out     source               destination
  18M 4180M Default    all  --  any    ppp0    anywhere             anywhere

Chain Default (4 references)
 pkts bytes target     prot opt in     out     source               destination
  67M   46G CONNMARK   all  --  any    any     anywhere             anywhere            CONNMARK restore
  44M   32G Default_ct  all  --  any    any     anywhere             anywhere            MARK match 0x0
 9318 5859K MARK       all  --  any    any     anywhere             anywhere            MARK match 0x1 length 400:65535 MARK set 0x0
 1101 1330K MARK       all  --  any    any     anywhere             anywhere            MARK match 0x2 length 800:65535 MARK set 0x0
2896K  382M MARK       udp  --  any    any     anywhere             anywhere            MARK match 0x0 length 0:500 MARK set 0x2
33370 7748K MARK       icmp --  any    any     anywhere             anywhere            MARK set 0x1
7932K 4986M MARK       tcp  --  any    any     anywhere             anywhere            MARK match 0x0 tcp spts:1024:65535 dpts:1024:65535 MARK set 0x4
62193   48M MARK       udp  --  any    any     anywhere             anywhere            MARK match 0x0 udp spts:1024:65535 dpts:1024:65535 MARK set 0x4
 106K 6317K MARK       tcp  --  any    any     anywhere             anywhere            length 0:128 MARK match !0x4 tcp flags:FIN,SYN,RST,PSH,ACK,URG/SYN MARK set 0x1
  25M 1277M MARK       tcp  --  any    any     anywhere             anywhere            length 0:128 MARK match !0x4 tcp flags:FIN,SYN,RST,PSH,ACK,URG/ACK MARK set 0x1

Chain Default_ct (1 references)
 pkts bytes target     prot opt in     out     source               destination
 6306  738K MARK       all  --  any    any     anywhere             anywhere            MARK match 0x0 ipp2p v0.8.1_rc1 --kazaa --gnu --edk --dc --bit MARK set 0x4
   46  7873 MARK       all  --  any    any     anywhere             anywhere            MARK match 0x0 LAYER7 l7proto edonkey MARK set 0x4
  134 14130 MARK       all  --  any    any     anywhere             anywhere            MARK match 0x0 LAYER7 l7proto bittorrent MARK set 0x4
  213 13484 MARK       tcp  --  any    any     anywhere             anywhere            MARK match 0x0 tcp multiport ports 22,53 MARK set 0x1
 1304 82528 MARK       udp  --  any    any     anywhere             anywhere            MARK match 0x0 udp multiport ports 22,53 MARK set 0x1
48819 2967K MARK       tcp  --  any    any     anywhere             anywhere            MARK match 0x0 tcp multiport ports 20,21,25,80,110,443,993,995 MARK set 0x3
  144  8222 MARK       tcp  --  any    any     anywhere             anywhere            MARK match 0x0 tcp multiport ports 5190 MARK set 0x2
    0     0 MARK       udp  --  any    any     anywhere             anywhere            MARK match 0x0 udp multiport ports 5190 MARK set 0x2
  44M   32G CONNMARK   all  --  any    any     anywhere             anywhere            CONNMARK save
}}}

=== QoS via X-Wrt - Web Interface (Easy QoS) ===
The X-Wrt Web Interface at http://x-wrt.org/ supports a QoS package and is easy to use.  Just install X-Wrt, then navigate to the QoS page in the X-Wrt web interface and use the web interface to install and configure the QoS package.


=== outdated - qosfw-scripts package (was qosif) ===
/!\ '''This page needs an update!''' /!\
(''Somewhat updated for qosfw-scripts, could use some editing - especially now qosfw-scripts doesn't seem to exist any more!'')

----
If looking at someone's code, you can peer into their minds, then there's much to be said about these scripts. It's small, fast, efficient, and does just about all the heavy lifting for you.

Install qosfw-scripts with {{{ipkg install http://openwrt.inf.fh-brs.de/~nbd/qosfw-scripts_0.5_all.ipk}}} (you many want to check [http://openwrt.inf.fh-brs.de/~nbd/ here] or [http://downloads.openwrt.org/people/nbd/qos/ here] for a newer update).

{{{
/etc/config/firewall
/etc/config/qos-wan
/etc/hotplug.d/iface/10-qos
/usr/lib/qosfw/qos.awk
/usr/lib/qosfw/common.awk
/usr/lib/qosfw/firewall.awk
/usr/lib/qosfw/fw.sh
}}}

The files in /usr/lib/qosfw do the heavy lifting.  {{{/etc/hotplug.d/iface/10-qos}}} is run everytime an interface is brought up, and looks for a qos-[interface] file in {{{/etc/config}}}, if it finds one then it'll setup the qos settings for that interface.

Which leaves us with the format of the {{{config}}} file.  It's formatted in stanzas (I did say that nbd guy was pretty clever, right?) and the stanzas can be broken down into policies and marking rules.

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

These are pretty self explainatory as well.  The first line uses a layer7 filter (the patterns for these are stored in /etc/l7-protocols, see [http://l7-filter.sourceforge.net/protocols l7-filter] for more) to classify edonkey traffic as bulk. The others all classify by port  numbers.

Take the second and third examples.  Anything with a destination of udp/53 or udp/5190 (dns and aim, respectively), will be classified as Priority.  Pretty simple, huh?

Next, we enable qos, and set the up/downstream bandwidth

{{{
#option:enabled
option:upload:128
option:download:1024
}}}

Uncomment the option:enabled line, or else you'll wonder why this isn't doing anything. The upload and download lines should be set slightly lower (1 to 2%) than your connection speeds in kbps. This ensures that no packets ever end up queued in your modem, while still nearly maximising the available bandwidth.

(''TODO: document this section'')

{{{
option:priority:Priority
option:bulk:Bulk
option:defaultlow:Normal
option:default:Bulk
option:bulk_dl:Normal:10
}}}

Finally to activate your settings run {{{ ifdown wan && ifup wan }}}.

You can see what commands the script is running by looking at {{{/tmp/.qos-wan.sh}}}. You can get an idea of how much traffic is hitting each of your rules with {{{iptables -t mangle -L -v}}}

So, '''qosfw''' in three steps:

 * install the package
 * modify {{{/etc/config/qos-wan}}} to suit your needs, don't forget the option:enabled line
 * {{{ifdown wan && ifup wan}}} to activate

==== Notes and Caveats ====
 * There is no ingress capabilities.  As I mentioned earlier, most people won't want that anyhow.
 * Rules like the first ''edonkey'' one above require the L7 filter from http://l7-filter.sourceforge.net (this is now a dependency of the package).
 * You might need other packages, like the ''iptables-extra'' package for fancy marking of packets.
 * Based on {{{hfsc}}} packet scheduler, not {{{htb}}}.  You may be more familiar with one over the other.

==== Show QoS Packet info on the webif ====
If you want to show the output of {{{iptables -t mangle -L -v}}} on the webif, put this into /www/cgi-bin/webif/QoS.sh Note: This has only been tested on nbd's pre-RC5 and RC5, so if it doesn't work on your version of !OpenWrt, change this to reflect that.

{{{
#!/usr/bin/webif-page
<?
. /usr/lib/webif/webif.sh

header "Status" "QoS Packets" "@TR<<QoS Packets>>"
?>
<table style="width: 90%; text-align: left;" border="0" cellpadding="2" cellspacing="2" align="center">
<tbody>
        <tr>
                <th><b>@TR<<QoS Packets|Quality Of Service Packet Info>></b></th>
        </tr>
        <tr>
                <td><pre><? iptables -t mangle -L -v ?></pre></td>
        </tr>
</tbody>
</table>
<? footer ?>
<!--
##WEBIF:name:Status:4:QoS Packets
-->
}}}

Then chmod a+x it.

=== unsupported - ctshaper ===
/!\ '''This page needs an update!''' /!\
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

I then copied it to {{{/usr/sbin/ctshaper}}} on the OpenWRT router.

Next, modify {{{ctshaper.conf}}} to suit your needs, and copy over to {{{/etc/ctshaper/ctshaper.conf}}} on the router.

Then, I made a file called {{{S75qos}}} and put it in {{{/etc/init.d/}}} ... it's just a copy of the {{{crond}}} init script, modified a bit:

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

That's it!  Now when you reboot, your QoS will be applied at bootup.  Notice, with this setup, you must mark your own packets, possibly in {{{/etc/firewall.user}}}.

Try issuing the command {{{ctshaper status}}} to see current configuration.

==== Notes and Caveats ====
 * As I said, it requires you to mark your own packets.  Not as elegant as the '''qosif''' script, but it works.
 * Necessary to modify it a bit first to get it working.
 * Based on {{{htb}}} packet scheduler, not {{{hfsc}}}.

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

=== Another Qos Package ===
Searching in the forums'''''''''[http://forum.openwrt.org/profile.php?id=4425 rudy]'''made this package:

http://forum.openwrt.org/viewtopic.php?pid=26979#p26979

The best feature: Qos on downloads :)
The objective:
'''Comfortably surf the web while running several p2p apps at unthrottled speeds

'''http://forum.openwrt.org/viewtopic.php?id=4112

Run:
{{{
ipkg install http://files.eschauzier.org/qos-re_1.0_all.ipk}}}

Other thing to do is to edit /etc/qos.conf, as may 15 2006 the qos.conf is:
{{{
################################################################################
##
## User configuration of the QoS script
##
## At a minimum, set the DOWNLOAD and UPLOAD variables below. Setting these
## slightly slower than the actual line speeds is critical to good QoS
## performance. With download and upload speeds set too high, the traffic queues
## in the modem (upload) and on the ISP side (download) will quickly fill up. As
## these queues can be very long --on the order of several seconds-- filling
## them will prohibit any meaningful traffic shaping.
##
## The default configuration, with the proper upload and download speeds set,
## should be adequate for most situations to separate out low-priority peer-to
## -peer traffic (eMule, Bittorrent, etc.) from interactive traffic such as web
## browsing and SSH sessions.
##
## The configuration can be refined by modifying the settings below. As an
## example, consider including support for VoIP. This may be accomplished by
## adding the IP address of a VoIP adapter to the IP_EXPR variable (e.g.
## IP_EXPR="192.168.1.10"). Doing so will elevate the status of traffic to and
## from the VoIP box to 'express'.
##
## In general, the configuration of the QoS script requires the setting of
## several variables. Most variables expect a space separated list of elements
## (ports, IP addresses, protocols). Adding an element to a list will, based on
## the variable name, either promote a certain connection to 'express' (highest
## priority) or 'priority' status, or demote it to 'bulk' status. The default
## status for all traffic is 'normal'. An example of setting a configuration
## variable to classify traffic is the statement
##
## TCP_PRIO="80 443"
##
## Including this line in the configuration will ensure that all TCP traffic to
## the listed ports (in this particular case for the http and https protocols)
## will be treated as 'priority' traffic.
##
## Another example (from the default configuration) is:
##
## TCP_BULK="1024: 21"
##
## which adds port 21 (the port used for ftp) and all ports 1024 and up to the
## list of destination ports for 'bulk' traffic. The result is that ftp
## downloads get a low priority, as does traffic to non-reserved ports (mostly
## peer-to-peer protocols). The notation '1024:' indicates a port range, in this
## case including all ports 1024 and higher. Another example of a port range is
## ':10' which means all ports from 0 to 10. A range from 10 to 20 is denoted as
## '10:20'.
##
## It is important to note that some variables take precedence over others. This
## becomes significant in cases where the same traffic is identified by
## different rules. An example is adding an UDP game port above 1024 to the
## express list. In the default configuration, all high ports (1024:) are
## included in the UDP_BULK variable. Without knowing the order of the rules, it
## is not possible to determine what the status of traffic to the game port will
## be. It turns out, the traffic will be classified as priority, since UDP_EXPR
## takes precedence over UDP_BULK.
##
## The order of the variables is (lowest precedence first): TCP_BULK, UDP_BULK,
## TCP_PRIO, UDP_PRIO, TCP_EXPR, UDP_EXPR, IP_BULK, IP_PRIO, IP_EXPR, L7_BULK,
## L7_PRIO, L7_EXPR, IPP2P_BULK, IPP2P_PRIO, IPP2P_EXPR, TOS_BULK, TOS_PRIO,
## TOS_EXPR, DSCP_BULK, DSCP_PRIO, DSCP_EXPR
##
################################################################################

# Download speed in kilobits per second
# Set 5% - 10% lower than *measured* line speed (set to zero to disable)
DOWNLOAD=100

# Upload speed in kilobits per second
# Set 5% - 10% lower than *measured* line speed (set to zero to disable)
UPLOAD=50

# Destination ports for classifying 'bulk' traffic
TCP_BULK="1024: 21"
UDP_BULK="1024:"

# Destination ports for classifying 'priority' traffic
TCP_PRIO="22 23"
UDP_PRIO=""

# Destination ports for classifying 'express' traffic
TCP_EXPR="53"
UDP_EXPR="53"

# LAN IP addresses for 'bulk', 'priority' and 'express' traffic
IP_BULK=""
IP_PRIO=""
IP_EXPR=""

# Bulk, prio and express Layer 7 protocol matches
L7_BULK=""
L7_PRIO=""
L7_EXPR=""

# IPP2P protocol matches
# Default 'ipp2p' includes all well-knows peer-to-peer protocols
IPP2P_BULK="ipp2p"
IPP2P_PRIO=""
IPP2P_EXPR=""

# ToS (Type of Service) matches (egress only)
#TOS_BULK="0x02"
#TOS_PRIO=""
#TOS_EXPR="0x10"

# DSCP (Differentiated Services Code Point) matches (egress only)
DSCP_BULK=""
DSCP_PRIO=""
DSCP_EXPR=""

# Define custom QoS interface. Defaults to wan interface.
#QOS_IF=eth1

# Enable 'small UDP packets get priority' feature.
# Sets the maximum length for priority UDP packets.
#UDP_LENGTH=256

# Set to 1 to enable logging of packets to syslog
DEBUG=0
}}}

[http://files.eschauzier.org/qos.gif]
