= Backing up and Restoring your OpenWrt box =

There are two ways: image method and file method.


== Image method ==

=== Backing up ===

It's a good idea to put the jffs2 partition in read only mode before reading it as
a device, or you could make a backup that's not up to date or corrupt. The default
commit interval for jffs2 is 5 seconds. Log into your WRT, then:

{{{
mount -o remount,ro /dev/mtdblock/4 /
dd if=/dev/mtdblock/1 > /tmp/wrt-linux.trx
mount -o remount,rw /dev/mtdblock/4 /
dd if=/dev/mtdblock/3 > /tmp/wrt-nvram.bin
}}}

And scp the files out. This assumes you have enough ram free on the WRT, which is
usually the case. wrt-linux.trx contains kernel+squashfs+jffs2 one after the other.
You could back the mtd partitions separately: 2 is squashfs and 4 is jffs2. Unlike
disk partitions mtd partitions can, and in OpenWRT do overlap: 1 includes 2 and 4.


=== Restoring ===

/!\ '''WARNING:''' Restore the NVRAM partition '''only''' on the same Wrt router where
you did the backup! Restoring the NVRAM partition can brick your router.

I'll assume you need a full restore, i. e. you've totally botched your box, and you
have either restored to factory firmware, or bought a new box :)

1. install standard openwrt firmware on your box, if you haven't already. Set up a
password so you can use scp:

{{{
telnet 192.168.1.1
passwd
}}}

2. Transfer the files

{{{
scp wrt-linux.trx wrt-nvram.bin root@192.168.1.1:/tmp
}}}

3. On the wrt box, don't forget to put jffs2 in ro mode if your're writing the
whole kernel+squashfs+jffs2 image.

{{{
dd if=/tmp/wrt-nvram.bin of=/dev/mtdblock/3
mount -o remount,ro /dev/mtdblock/4 /
mtd -r write /tmp/wrt-linux.trx linux
}}}

The second command will take a minute or so to flash the rest and then reboot.


== File method ==

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
