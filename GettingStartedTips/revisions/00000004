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

This firewall rule forward ssh connections to an internal machine's ssh daemon.  Requests from inside the internal network go direct to the router.

Put this after "$IPT -t filter -A INPUT -p icmp -j ACCEPT" in /etc/init.d/S45firewall

{{{$IPT -A FORWARD -p tcp -i $WAN --dport 22 -j ACCEPT
$IPT -A PREROUTING -t nat -p tcp -i $WAN --dport 22 -j DNAT --to 192.168.1.100:22
$IPT -A INPUT -p tcp -i eth0 --dport 22 -j ACCEPT}}}
