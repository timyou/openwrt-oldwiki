## Please edit system and help pages ONLY in the moinmaster wiki! For more
## information, please see MoinMaster:MoinPagesEditorGroup.
##master-page:Unknown-Page
##master-date:Unknown-Date
##acl MoinPagesEditorGroup:read,write,delete,revert All:read
#format wiki
#language en
[[TableOfContents([3])]]

= Overview =
MaraDNS is a full featured DNS server and can be used as a replacement for the DNS part of dnsmasq. Its main advantage over dnsmasq is that it supports redundant DNS setups, using primary and secondary servers. It is available as an ipkg and can be easily installed. It comes with extensive documentation in english and french which can be found [http://www.4haus.buettemeyer.net/playground/maradns.doc/ here]. The best starting point is the [http://www.4haus.buettemeyer.net/playground/maradns.doc/en/tutorial/tutorial.html good tutorial].

== Components ==
The main MaraDNS configuration file is located in `/etc/mararc` and you have 4 main programs:
 * `maradns`: dns server; answers requests from clients
 * `askmara`: corresponding query tool; like dig or nslookup
 * `zoneserver`: zone transfer server; answers requests from secondary servers
 * `getzone`: corresponding query tool; like dig -axfr

= Configurations =
Depending on what you are trying to do with MaraDNS, you'll need to integrate some or all of the above tools.

== Recursive Server ==
If you want MaraDNS to act as a recursive and/or authoritative server, you may need to edit `/etc/mararc` and run maradns in the background through `/etc/init.d/S60maradns`, which is installed along with the ipkg. See [http://www.4haus.buettemeyer.net/playground/maradns.doc/en/tutorial/recursive.html this] part of the MaraDNS tutorial for instructions and examples.

Normally you can stick with the defaults provided by the ipkg, but you may need to customize the following line in `/etc/mararc` to match your network:
{{{
recursive_acl="192.168.1.0/24"
}}}

If you want to tie the process to a specific interface, edit the {{{bind_address}}} parameter. This defaults to 0.0.0.0 meaning any interface.

You may also want to remove the {{{run_as_root=1}}} parameter and replace it with {{{maradns_uid=65534}}}.

== Primary Server ==
If you want to act as a primary server to other secondaries, you'll also need to start zoneserver and set up a new init-script for that. You can either set up a new file `/etc/init.d/S60zoneserver` like this:
{{{
#!/bin/sh
/usr/sbin/zoneserver >/dev/null 2>&1 &
}}}
Or you can append the above command to the existing file `/etc/init.d/S60maradns`.

You also need to add your zonefiles to `/etc/maradns/` in MaraDNS's [http://www.4haus.buettemeyer.net/playground/maradns.doc/en/tutorial/man.csv1.html CSV1 format]. Detailed instructions can be found [http://www.4haus.buettemeyer.net/playground/maradns.doc/en/tutorial/authoritative.html here].

== Secondary Server ==
If you want to act as a secondary server, you'll need to do regular zonetransfers with getzone. See [http://www.4haus.buettemeyer.net/playground/maradns.doc/en/faq.html#secondary this FAQ] for more information.

Generally you want to run a command like this on either a regular basis or triggered by some external event:
{{{
getzone domain.test 192.168.1.2 > /etc/maradns/db.domain.test
}}}
Where `domain.test` is the domain name, `192.168.1.2` is the primary name server and `db.domain.test` is the filename of the zonefile. You will also have to restart maradns and/or zoneserver after you transferred to zones.  The HowtoEnableCron document explains how to configure cron on your OpenWrt system.

= dnsmasq Considerations =
If your MaraDNS machine also provides DHCP services, you probably use dnsmasq for that task. dnsmasq also provides DNS services and there is no way to shut that part off. To avoid errors about ports being already in use, you have to change to default bahaviour of dnsmasq. More informatio about dnsmasq in general can be found at OpenWrtDocs/dnsmasq.

== Hiding dnsmasq ==
To hide dsnmasq's DNS server on a different port, you have to add a line like this to your dnsmasq.conf:
{{{
port=5353
}}} 
Change that to any free, unused port you like and use your packet filter to block traffic to that port.

== Separating internal and external DNS ==
It is possible to run dnsmasq and MaraDNS concurrently and have both listen on different interfaces. This allows for the seperation of internal and external DNS services, as detailed by synthrax on [http://forum.openwrt.org/viewtopic.php?id=4558 this post]:

I have both maradns and dnsmasq running on port 53. maradns serves public dns at the wan interface and dnsmasq takes care of the private subnet. in order for both to get along, you have to start maradns BEFORE dnsmasq.

Additionally, you need to have the line:
{{{
bind_address="external_ip"
}}}
in your mararc file. To start the two name servers, i slightly modified /etc/init.d/S50dnsmasq:

{{{
#!/bin/sh
. /etc/functions.sh

# maradns stuff starts here
publicip=$(whatismyip vlan1)
zonefile=/etc/maradns/my_dns_zone
cat $zonefile.template |sed s/external_ip/$publicip/ > $zonefile.zone
cat /etc/maradns/mararc.template |sed s/external_ip/$publicip/ > /etc/mararc
/usr/sbin/maradns >/var/log/maradns 2>&1 &
# maradns stuff ends here

# interface to use for DHCP
iface=lan
[...the script continues...]
}}}

this script does the following things:
 1. it determines my external (wan) IP with a script i got from the openwrt wiki (whatismyip)
 2. it rewrites my maradns zone file to insert the external ip (just put "external_ip" in place of the actual ip in the zone template)
 3. it rewrites mararc to insert the correct IP in "bind_address=..."
 4. finally, it starts maradns

After maradns has started, port 53 of the external iface will be "occupied", which dnsmasq will complain about in the syslog ("[dnsmasq] setting --bind-interfaces option because of OS limitations"). you can safely ignore this message or you could probably start dnsmasq explicitly with the --bind-interfaces option to get rid of the message. i didn't, as i'm too lazy

BTW: this works fine for me, as my internet provider does (almost) never change my assigned IP. if you have a provider which changes your ip with every dhcp lease period or so, you would probably need to place something similar in /etc/hotplug.d/iface (or i don't know where)


----
CategoryHowTo
