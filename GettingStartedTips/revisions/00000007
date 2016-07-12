= Sending the firmware =

Of course, first set boot_wait.  If you don't do this, you end up with a brick.  So read this: http://openwrt.ksilebo.net/temp/00-WARNING.TXT

Connect up an ethernet cable to one of the hub ports of the unit.

With the standard tftp client (I'm using the standard Debian package "tftp"), do this.  Note, the file you send will be different for other models of the unit.  This is the one for the WRT54g

{{{ tftp 192.168.1.1
> binary
> rexmt 1
> verbose
> trace
> put openwrt-g-code.bin}}}

Before you press enter on that last one, take the power cord out and plug back in.  Wait somewhere between 0.5 and 2 seconds, then press enter.  You might have to try a few times.  The trace output will tell you whether it's working.

= Logging in first time =

telnet to 192.168.1.1 and run "firstboot".  Wait until it does its thing, then reboot.

= Logging in after that =

telnet to 192.168.1.1 and you're away.  Once you've installed dropbear, the ssh server, you probably want to disable telnet.  Comment out the line in /etc/init.d/S50Services.  (Of course, first you have to delete the symlink and copy it across from /rom)

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
