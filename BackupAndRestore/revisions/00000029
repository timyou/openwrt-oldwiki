[[TableOfContents(4)]]

= Backing up and Restoring your OpenWrt box =
There are two ways to backup your OpenWrt box. The [#image image] method involves copying full [http://en.wikipedia.org/wiki/Disk_image disk images] from an OpenWrt box. The [#file file] method only involves copying the files from OpenWrt box filesystems.

Some of the commands in this document assume that DNS is configured such that {{{linuxbox}}} points to the backup target machine and {{{router}}} points to the router which is being backed up. In cases when DNS is not available (eg: new router installation), simply substitute the hostnames with appropriate IP numbers.

[[Anchor(image)]]

== Image method ==
These methods use the [http://en.wikipedia.org/wiki/Dd_(Unix) dd] tool to copy disks byte by byte.

=== Backing up ===
There are a number of ways to get disk image copies from an OpenWrt box. If you are using KAMIKAZE you can Ignore the NVRAM steps.

==== using Netcat (recommended) ====
[http://en.wikipedia.org/wiki/Netcat Netcat] (nc) is a simple yet powerful way to transfer bits and bytes across a network. The following steps show how to use it to backup a full OpenWrt disk image as well as the NVRAM data.

 1. Start listening for data with netcat on the target machine.
 {{{
plouj@linuxbox $ nc -l -p 7777 | dd of=wrt-linux.trx}}}
 1. Remount the main partition as read-only to prevent disk changes during the backup process.
 {{{
root@router $ mount -o remount,ro /dev/mtdblock/4 /jffs}}}
 1. Copy the data from the router's disk across a network to the listening target machine.
 {{{
root@router $ dd if=/dev/mtdblock/1 | nc linuxbox 7777}}}
 1. Remount the partition back as read-write.
 {{{
root@router $ mount -o remount,rw /dev/mtdblock/4 /jffs}}}
 1. Prepare to receive the NVRAM data on the target machine.
 {{{
plouj@linuxbox $ nc -l -p 7777 | dd of=wrt-nvram.bin}}}
 1. Send the NVRAM data to the target machine
 {{{
root@router $ dd if=/dev/mtdblock/3 | nc linuxbox 7777}}}

==== using /tmp as intermediate ====
It's a good idea to put the jffs2 partition in read only mode before reading it as a device, or you could make a backup that's not up to date or corrupt. The default commit interval for jffs2 is 5 seconds. Log into your OpenWrt, then:

{{{
mount -o remount,ro /dev/mtdblock/4 /jffs
dd if=/dev/mtdblock/1 > /tmp/wrt-linux.trx
mount -o remount,rw /dev/mtdblock/4 /jffs
dd if=/dev/mtdblock/3 > /tmp/wrt-nvram.bin
}}}

Note: I had to write {{{/}}} instead of {{{/jffs}}}, otherwise it gave an error. -- Xerces8

And scp the files out. This assumes you have enough ram free on the OpenWrt, which is usually the case.

If you do not have enough free space in your {{{/tmp}}} filesystem, you can generate and copy in one operation.  Please make sure you use the right quotes; double quotes (") won't work.  From another workstation, and assuming that {{{router}}} is the name of your OpenWrt router:

==== using SSH transfer ====
{{{
ssh router -C 'mount -o remount,ro /dev/mtdblock/4 /jffs ; dd if=/dev/mtdblock/1 ; mount -o remount,rw /dev/mtdblock/4 /jffs' > wrt-linux.trx
ssh router -C 'dd if=/dev/mtdblock/3' > wrt-nvram.bin
}}}
If you did everything right, {{{wrt-linux.trx}}} contains {{{kernel+squashfs+jffs2}}} one after the other. You could back the mtd partitions separately: 2 is squashfs and 4 is jffs2. Unlike disk partitions mtd partitions can, and in OpenWrt do overlap: 1 includes 2 and 4.

=== Restoring ===
/!\ '''WARNING:''' Restore the NVRAM partition '''only''' on the same OpenWrt router where you did the backup! Restoring the NVRAM partition can brick your router.

I'll assume you need a full restore, i. e. you've totally botched your box, and you have either restored to factory firmware, or bought a new box :)

 1. install standard OpenWrt firmware on your box, if you haven't already. Set up a password so you can use scp:
 {{{
telnet 192.168.1.1
passwd
}}}

 1. Transfer the files
 {{{
scp wrt-linux.trx wrt-nvram.bin root@192.168.1.1:/tmp
}}}

 1. On the OpenWrt box, don't forget to put jffs2 in read-only mode if you're writing the whole {{{kernel+squashfs+jffs2}}} image.
 {{{
dd if=/tmp/wrt-nvram.bin of=/dev/mtdblock/3
mount -o remount,ro /dev/mtdblock/4 /jffs
mtd -r write /tmp/wrt-linux.trx linux
}}}
 The second command will take a minute or so to flash the rest and then reboot.

*If you are using kamikaze replace the /dev/mtdblock/NUMBER to /dev/mtdblockNUMBER[br][br]

You can also restore your image using the {{{TFTP}}} method. If you are using Kamikaze just TFTP the backup you made of /dev/mtdblock1 and it will work fine. Remember that after sending the image, wait around 240 seconds for the CPE to commit the information into the flash.[br]


== File method ==
Of course you can use a shell script and the well known {{{tar}}} to backup your files and some system informations too. In the example below I installed the package {{{wput}}}, to upload the backup to my main FTP server.

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
This is an alternative backup script based on the above one. The transfer of the archive is done via SSH instead of FTP using Publickey authentification (much more secure) and only /etc and /tmp are backup. Please read the instructions at the beginning of the script. Without reading this, it probably won't work.

{{{
#!/bin/sh
#
# Copyright 2006 Enrico Tröger <enrico.troeger@uvena.de>
#
# Simple backup script for OpenWRT
# - read the complete nvram into a file
# - read some system and status information into a file
# - backups all files in /etc
# - put all files into a gzipped tar archive
# - send the archive to a ssh server using publickey authentification
#
# The script uses scp to transfer the created archive to a SSH server somewhere in the
# internet or your local area network. To be able to do this automatically via cron
# you have to create a key pair for PublicKey authentification using dropbear.
# Just run the following command on your OpenWRT and copy the public part of the created
# key (it is printed out by the command) into your ~/.ssh/authorized_keys file on the
# destination host. Create the key pair:
#
# dropbearkey -t dss -f /etc/dropbear/id_dss
#
# Then you have to store the list of known hosts permanently. To do this, try to establish
# a SSH connection from your OpenWRT device to the destination host. You should be asked
# whether you want to continue connection to the host after its finger print is printed.
# Now say 'y' and the connection should be established. Now, run the following command on your
# OpenWRT device:
#
# cp /tmp/.ssh/known_hosts /etc/dropbear/
#
# And then add the following to lines to your /etc/init.d/S50dropbear:
#
# mkdir -p /tmp/.ssh
# ln -s /etc/dropbear/known_hosts /tmp/.ssh/
#
# After doing this you should test if all works fine and then the script could be run
# via cron on a daily base or if your OpenWRT device isn't running 24/7 (like in my case)
# set the variable CHECK_RUN_SINCE_REBOOT below to "1". This causes the script to run only
# once and stores the state that it already ran in /tmp/backup_ran. If you reboot
# (or turn it off and on again) the device, this file will be deleted and then script will do
# the backup again. Sample cron entry for this case:
# 0 * * * * /usr/bin/backup >/tmp/backup_log 2>&1
#
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
### configuration ###
# if set to 1 the script runs only once as long as you reboot your device
# this can be useful if your router is not running 24/7
# the cronjob for this case should be some kind of
# 0 * * * * /usr/bin/backup >/tmp/backup_log 2>&1
# so it will be run every hour but it will do the actual backup only on the first run
CHECK_RUN_SINCE_REBOOT="1"
# get the own name, to difference different WRTs
HOST=$(nvram get wan_hostname)
REMOTEFILE=/tmp/backup-$HOST.tar.gz
NVRAMFILE=/tmp/nvram-$(date +%Y.%m.%d-%X)-$HOST
SYSINFOFILE=/tmp/sysinfo-$(date +%Y.%m.%d-%X)-$HOST
### end of configuration ###
# check if we already ran since last reboot
if [ $CHECK_RUN_SINCE_REBOOT = "1" ]
then
        if [ -e "/tmp/backup_ran" ]
        then
                # exit silently
                exit 0;
        else
                # mark that we have been ran
                touch "/tmp/backup_ran"
        fi
fi
# save the nvram values
nvram show | sort > $NVRAMFILE
# save some other runtime information
echo "ps axf" > $SYSINFOFILE
ps axf >> $SYSINFOFILE
echo "uptime" >> $SYSINFOFILE
uptime >> $SYSINFOFILE
echo "ifconfig" >> $SYSINFOFILE
ifconfig >> $SYSINFOFILE
echo "route -n" >> $SYSINFOFILE
route -n >> $SYSINFOFILE
echo "iwconfig" >> $SYSINFOFILE
iwconfig >> $SYSINFOFILE
# create the tar archive, maybe you want to backup more than /etc, so just add the directories
cd /
tar czf $REMOTEFILE etc/ tmp/
# now upload the tar file to your prefered SSH server (please change username and host address)
# (or change this line to use a FTP server or whatever)
scp -i /etc/dropbear/id_dss $REMOTEFILE enrico@192.168.0.2:/home/enrico/
# remove the used files
rm -r $NVRAMFILE
rm -r $SYSINFOFILE
rm -r $REMOTEFILE
}}}
Could someone show us an example how to restore a file based backup and remove this paragraph? Thank you in advance. -- Wigy
