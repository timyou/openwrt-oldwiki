Not much attention seems to have been paid to the backup and restore of an OpenWRT box.  Sure, you can go

 nvram show > /tmp/log

and back that up, and maybe back up your /etc, but what if you've done all sorts of customising all over your file system?

This is what I came up with from my experimenting.

Comments appreciated.  If this method is a Bad Idea and there is a nicer way, please share it with us all.

== Backing up ==

 ssh root@wrt "dd if=/dev/mtdblock/1" > wrt-backup.trx
 ssh root@wrt "dd if=/dev/mtdblock/3" > wrt-nvram.bin

easy!

== Restoring ==

I'll assume you need a full restore, ie you've totally botched your box, and you have either restored to factory firmware, or bought a new box :)

1. install standard openwrt firmware on your box, if you haven't already.  Set up a password so you can use scp:

 telnet 192.168.1.1
 passwd

3.

 scp wrt-backup.trx wrt-nvram.bin root@192.168.1.1:/tmp

4. On the wrt box:

 dd if=/tmp/wrt-nvram.bin of=/dev/mtdblock/3
 mtd -r write /tmp/wrt-backup.trx linux

Be careful with that first command, I don't know what happens if you accidentally write to /dev/mtdblock/2.
The second command will take a minute or so to flash the rest and then reboot.
