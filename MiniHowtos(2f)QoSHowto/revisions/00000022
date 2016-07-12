/!\ This page is currently under construction /!\

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

== QoS in OpenWRT ==

I went from not having a QoS option (well, to be honest, the tools were always there, just needed a sane script) to having two options.  Debate as to which is the "better" one is probably not important.  I'd personally call them "two great ways to do it".

One involves nbd's qosif scripts.  And the other involves ctshaper, a script written by Carlos Rodrigues, based on wondershaper.

Perhaps I can outline the pros and cons of each.  But there's a few things you will need to get started.  For both sets of scripts, at a bare minimum, you should have the tc, ip and kmod-sched packages.

=== qosif ===

If looking at someone's code, you can peer into their minds, then there's much to be said about these scripts. It's small, fast, efficient, and does just about all the heavy lifting for you.  The archive is located [http://openwrt.inf.fh-brs.de/~nbd/qosif.tar.gz here] and contains four files. 


{{{
config
firewall.awk
genscript.awk
test.sh
}}}

The file `test.sh` is just a simple one line awk script:

{{{
awk -v device=ppp0 -v linespeed=128 -f genscript.awk config
}}}

This runs awk, setting two variables, the first "device" being the device that QoS will be applied on.  For me, this would be the WAN interface, or vlan1.  (Might differ depending on your hardware revision).  The second variable is linespeed.  Appearently this is for a 128kbit uplink.  Mine would be 512, for example.

It then passes these variables to the "genscript.awk" file, running it on the "config" file.  Firewall.awk is called from within genscript.awk.

So, all one needs to do, is copy these files over to the router, and either edit test.sh with your own values, or enter the one line command by itself, using your own values.  If you redirect the output, you have a nice Qos script.  Note that it requires firewall.awk.  

{{{
awk -v device=vlan1 -v linespeed=512 -f genscript.awk config > S55qos 

cp S55qos config firewall.awk /etc/init.d/
}}}

Which leaves us with the format of the `config` file.  It's formatted in stanzas (I did say that nbd guy was pretty clever, right?) and the stanzas can be broken down into policies and marking rules.

For example, the first three stanzas (or blocks) are policies:

{{{
class:Priority
maxdelay:30
rate:60
priority
end

class:Normal
maxdelay:100
limit:95
rate:30
normal
end

class:Bulk
maxdelay:1000
rate:10
limit:80
default
bulk
end
}}}

This first part of the config file sets up our 3 buckets.  "Class" names the policy, "maxdelay" is the maximum delay we would like to craft (in ms).  "Rate" and "limit" are pretty self-explainatory, in kbits/sec.  Last but not least, is the type of queue (priority, normal, bulk) and of course the end of the config file.
