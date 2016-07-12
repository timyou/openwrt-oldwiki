= Building the firmware =

The latest beta, b4, is available only in source form.  To build it, you'll need a linux-based system.  The build will build the development environment (a gcc cross-compiler for MIPS).  You'll need about a gig of disk space to build everything.
{{{
wget http://openwrt.ksilebo.net/cgi-bin/viewcvs.cgi/buildroot/buildroot.tar.gz
tar zxvf buildroot.tar.gz
cd buildroot
make
}}}

At this point you'll have a openwrt-linux.trx and two openwrt-*-code.bin files. The openwrt-g-code.bin is for the WRT54G, openwrt-gs-code.bin is for the WRT54GS (speedbooster).

= Sending the firmware =

It's a good idea to fully reset the router before loading OpenWrt, but this is not absolutely required.  In fact, it is probably a good idea to use the web administration menu to set the WAP parameters to your liking so you don't have to tweak the nvram directly after loading OpenWRT, since there is no web administration (as of b4).  Just don't change the IP address range so that dhcpd will work correctly after you reboot.

To fully reset the router back to factory defaults, connect the power, and press and hold the reset button for 30 seconds or so.

== Set boot_wait ==
'''IMPORTANT: '''set boot_wait.  If you don't do this, you may have to open your router to upload new firmware. Read about [http://openwrt.ksilebo.net/temp/00-WARNING.TXT boot_wait warning].  If you are still running the original ROM, use the ping.asp exploit to set boot_wait.
== Upload the ROM ==
There are two ways to do the initial ROM upload:
=== Using the current firmware ===
You can use the administration menu and upload the new .bin file.  You can do this using the stock ROM image off the Administration menu.  If you're reinstalling OpenWRT, you can use the "mtd write" command explained in the [OpenWrtFaq].
=== Using tftp ===
This is a better approach because you get familiar with reloading the ROM in case the OS doesn't boot correctly.
With the standard tftp client (I'm using the standard Debian package "tftp"), do this.  '''Caution:''' The file in the example is for a WRT54g.  If you have a GS, make sure you send the openwrt-gs-code.bin instead!

{{{ tftp 192.168.1.1
> binary
> rexmt 1
> verbose
> trace
> put openwrt-g-code.bin}}}

Before you press enter on that last one, take the power cord out and plug back in.  Wait somewhere between 0.5 and 2 seconds, then press enter.  You might have to try a few times.  The trace output will tell you whether it's working.

Note that for this to work, your host machine (the one you are sending the firmware from) must be configured in the 192.168.1.0/24 subnet (e.g. ifconfig eth0 inet 192.168.1.2 netmask 255.255.255.0).  Whatever other IP address or netmask you may have configured in the NVRAM does not take effect until the boot_wait period has passed and it is too late to load a new firmware. 

= Logging in first time =

telnet to 192.168.1.1 and run "firstboot".  Wait until it does its thing, then reboot.

= Logging in after that =

telnet to 192.168.1.1 and you're away.

= Suggested packages =

Install dropbear, which is the ssh server, and then disable telnet.  To install dropbear, change /etc/ipkg.conf (see [OpenWrtPackages]), then use ipkg to do the install.

Make sure ssh works before you disable telnet.  Reboot the router once to make sure it will come up automatically on the next reboot also.  When you're sure it's safe, comment out the line in /etc/init.d/S50Services.  (Of course, first you have to delete the symlink and copy it across from /rom).

= ssh from the outside =

put the line "$IPT -t filter -A INPUT -p tcp --dport 22 -j ACCEPT" after the line "$IPT -t filter -A INPUT -p icmp -j ACCEPT" in /etc/init.d/S45firewall to be able to ssh into the box from the wanport.

= ssh foward on WAN and to router from inside =

This firewall rule forwards ssh connections from outside your network (WAN) to an internal machine's ssh daemon (192.168.1.100).  Requests from inside the internal network go to the router's ssh daemon.

Put this after "$IPT -t filter -A INPUT -p icmp -j ACCEPT" in /etc/init.d/S45firewall

{{{$IPT -A FORWARD -p tcp -i $WAN --dport 22 -j ACCEPT
$IPT -A PREROUTING -t nat -p tcp -i $WAN --dport 22 -j DNAT --to 192.168.1.100:22
$IPT -A INPUT -p tcp -i eth0 --dport 22 -j ACCEPT}}}

= AWK script to build iptables rules from nvram's forward_port variable =
If you had all your port forwarding configured before you flashed to OpenWRT and it's still in NVRAM then this awk script will show it to you.
{{{
{
IPT="iptables"
split($0, rule)
for(idx in rule) {
    tmp = rule[idx]
    split(tmp, pts, ":")
    split(pts[5], wtf, ">")
    if (pts[2] == "off") break
    if (pts[3] == "both") {
        print "#___tcp & udp for " pts[1]
        print IPT " -A FORWARD -p tcp -i " WANIF " --dport " pts[4] " -j ACCEPT"
        print IPT " -A PREROUTING -t nat -p tcp -i " WANIF " --dport " pts[4] " -j DNAT --to " wtf[2] ":" wtf[1]
        print IPT " -A INPUT -p tcp -i " WANIF " --dport " pts[4] " -j ACCEPT"
        print IPT " -A FORWARD -p udp -i " WANIF " --dport " pts[4] " -j ACCEPT"
        print IPT " -A PREROUTING -t nat -p udp -i " WANIF " --dport " pts[4] " -j DNAT --to " wtf[2] ":" wtf[1]
        print IPT " -A INPUT -p udp -i " WANIF " --dport " pts[4] " -j ACCEPT"
    } else if (pts[3] == "udp") {         
        print "#___udp for " pts[1]
        print IPT " -A FORWARD -p udp -i " WANIF " --dport " pts[4] " -j ACCEPT"
        print IPT " -A PREROUTING -t nat -p udp -i " WANIF " --dport " pts[4] " -j DNAT --to " wtf[2] ":" wtf[1]
        print IPT " -A INPUT -p udp -i " WANIF " --dport " pts[4] " -j ACCEPT"
    } else if (pts[3] == "tcp") {
        print "#___tcp for " pts[1]
        print IPT " -A FORWARD -p tcp -i " WANIF " --dport " pts[4] " -j ACCEPT"
        print IPT " -A PREROUTING -t nat -p tcp -i " WANIF " --dport " pts[4] " -j DNAT --to " wtf[2] ":" wtf[1]
        print IPT " -A INPUT -p tcp -i " WANIF " --dport " pts[4] " -j ACCEPT"
    } }
}
}}} 
save that as forward_port.awk and then run this:
{{{
nvram get forward_port | awk -f forward_port.awk -v WANIF=$(nvram get wan_ifname)
}}}
That will print the iptables cmdlines to the screen, if you want to paste them somewhere

To add this to your init scripts put the command below in '''/etc/init.d/S45firewall''':
{{{
nvram_get forward_port | awk -f /etc/init.d/forward_port.awk -v WANIF=$(nvram_get wan_ifname) | sh
}}}
it goes immediately after the '''$IPT -t filter -A INPUT -p icmp -j ACCEPT''' line.

now we just need someone to write a web interface for us, one that stores the rules in nvram :)
