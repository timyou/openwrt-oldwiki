= Backing up and Restoring your OpenWrt box =

Not much attention seems to have been paid to the backup and restore of an !OpenWrt box.
Sure, you can go

{{{
nvram show > /tmp/log
}}}

and back that up, and maybe back up your {{{/etc}}}, but what if you've done all sorts of
customising all over your file system?

This is what I came up with from my experimenting.

Comments appreciated. If this method is a Bad Idea and there is a nicer way, please share
it with us all.


== Backing up ==

{{{
ssh root@wrt "dd if=/dev/mtdblock/1" > wrt-backup.trx
ssh root@wrt "dd if=/dev/mtdblock/3" > wrt-nvram.bin
}}}

easy!

Of course you can use a shell script and the well known tar to backup your files and
some system informations too. In the example below i installed the package wput, to
upload the backup to my main FTP server.

{{{
#!/bin/sh

# get the own name, to difference different WRTs
HOST=$(nvram get wan_hostname)

# create a directory, where the backup and tempoarary files will be stored
mkdir /tmp/backupfiles

NVRAMFILE=/tmp/backupfiles/nvram-$(date +%Y.%m.%d-%X)-$HOST.txt
REMOTEFILE2=$(date +%Y.%m.%d-%X)-$HOST.tar.gz

# save the nvram values
nvram show | sort > $NVRAMFILE

# save some other runtime informations
SYSINFOFILE=/tmp/backupfiles/sysinfo-$(date +%Y.%m.%d-%X)-$HOST.txt
touch $SYSINFOFILE
ps axf > $SYSINFOFILE
uptime >> $SYSINFOFILE
ifconfig >> $SYSINFOFILE
route -n >> $SYSINFOFILE
wl scan
sleep 3;
wl scanresults >> $SYSINFOFILE
wl status >> $SYSINFOFILE
iwconfig >> $SYSINFOFILE

# create the tar archive, if you created your own directories below root ( / ), add the directory here too
tar czf /tmp/backupfiles/$REMOTEFILE2 /bin/ /dev/ /etc/ /jffs/ /lib/ /rom/ /sbin/ /usr/ /var/ /www/ /tmp/

sleep 3

# now upload the tar file to your prefered FTP server
# for the options i used with wput type wput --help
/usr/bin/wput -R -v -t 2 -B /tmp/backupfiles/$REMOTEFILE2 ftp://FTPUSERNAME:FTPPASSWORD@FTPSERVER/$REMOTEFILE2

# remove the backup directory (if wanted) to free space
rm -r /tmp/backupfiles
}}}


== Restoring ==

/!\ '''WARNING:''' Only restore the NVRAM partition '''only''' on the same Wrt router
where you did the backup!

I'll assume you need a full restore, i. e. you've totally botched your box, and you
have either restored to factory firmware, or bought a new box :)

1. install standard openwrt firmware on your box, if you haven't already. Set up a
password so you can use scp:

{{{
telnet 192.168.1.1
passwd
}}}

2. Transfer the file

{{{
scp wrt-backup.trx wrt-nvram.bin root@192.168.1.1:/tmp
}}}

3. On the wrt box:

{{{
dd if=/tmp/wrt-nvram.bin of=/dev/mtdblock/3
mtd -r write /tmp/wrt-backup.trx linux
}}}

Be careful with that first command, I don't know what happens if you accidentally write
to {{{/dev/mtdblock/2}}}. The second command will take a minute or so to flash the rest
and then reboot.
