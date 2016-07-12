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
