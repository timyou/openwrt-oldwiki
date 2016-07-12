Remote backups via rsync using a WRTSL54GS router:    1.      Install the OpenWRT White Russian RC5 firmware on your router; DO THIS FROM A WIRED CONNECTION, NOT WIRELESSLY
 http://downloads.openwrt.org/whiterussian/rc5/bin/openwrt-wrtsl54gs-squashfs.bin

    2.      Release/renew your IP address; telnet to 192.168.0.1

    3.      Change the password upon login; then ssh to 192.168.0.1 and login as root with your new password

            4.      For already existent files in /etc, you may need to remove them first before you can edit them; we need to add a line to the ipkg.conf file, so do the following:

{{{
# rm /etc/ipkg.conf
# cat>/etc/ipkg.conf
      src whiterussian http://downloads.openwrt.org/whiterussian/packages
      src non-free http://downloads.openwrt.org/whiterussian/packages/non-free
      src backports http://downloads.openwrt.org/backports/rc5
      dest root /
      dest ram /tmp
      ^D
}}}


5.      Update the ipkg registry:  {{{
# ipkg update}}}
    6.      Add the following packages and configure USB storage

  {{{
# ipkg install kmod-usb2              (USB 2.0 support)
# ipkg install kmod-usb-storage       (USB storage device support)
# rm /etc/modules.d/60-usb-storage
# cat>/etc/modules.d/60-usb-storage   (adding the max_scsi_luns line)
      scsi_mod
      sd_mod
      usb-storage
      max_scsi_luns=8
      ^D
}}}
  7.      Reboot to activate the USB modules:

  {{{
# reboot}}}
    8.      Install the file-system support (you only need what is on your External USB drive)

  {{{
# ipkg install kmod-vfat       (for legacy FAT partitions)
# ipkg install kmod-ext2       (Recommended: for ext2 filesystems)
# ipkg install kmod-ext3       (for ext3 filesystems)
}}}
   I prefer using ext2 because it seems to be the most portable.. ext2 lets you hook the external USB drive to a Windows box if you need to, with the help of Ext2Fsd project (http://ext2fsd.sourceforge.net/). Ext3 has read-support, but doesn't have stable write-support. FAT has many limitations to it

    9.      Reboot again for the file-system support to be enabled

  {{{
# reboot}}}
    10. Install the fdisk package so you can see your USB device



{{{
# ipkg install fdisk}}}
     11. Create a mount point for the external disk  {{{
# mkdir /mnt}}}
     12. Look at what device paths your disks are on  {{{
# fdisk -l
root@localhost:~# fdisk -l

Disk /dev/scsi/host0/bus0/target0/lun0/disc: 250.0 GB, 250059350016 bytes
255 heads, 63 sectors/track, 30401 cylinders
Units = cylinders of 16065 * 512 = 8225280 bytes

                                 Device Boot      Start         End      Blocks   Id System
/dev/scsi/host0/bus0/target0/lun0/part1               1       15935   127997856    7 HPFS/NTFS
/dev/scsi/host0/bus0/target0/lun0/part2           15936       28989   104856255   83 Linux}}}
  13. Mount your filesystem  {{{
# mount /dev/scsi/host0/bus0/target0/lun0/part2 /mnt}}}
    14. Install the samba package  {{{
# ipkg install samba}}}
     15. Add an entry to your router's name to /etc/hosts  {{{
# rm /etc/hosts
# cat>/etc/hosts
      127.0.0.1 localhost OpenWrt MyRouterName
      ^D}}}
    16. Add entries as applicable to the Samba configuration  (TODO: Add better security):  {{{
# rm /etc/samba/samba.conf
# cat>/etc/samba/samba.conf
 [global]
 syslog = 0
 syslog only = yes
 workgroup = OpenWrt
 server string = OpenWrt Samba Server
 security = share
 encrypt passwords = yes
 guest account = nobody
 local master = yes
 name resolve order = lmhosts hosts bcast

[tmp]
 comment = /tmp
 path = /tmp
 browseable = yes
 public = yes
 writeable = no

[All_Partitions]
 comment = /mnt
 path = /mnt
 browseable = yes
 public = yes
 writeable = yes
^D}}}
  17. Start up Samba; you should now be able to access your shares on the network

  {{{
# /etc/init.d/samba start}}}
    18. Next is creating your SSH keys for use with rsync:  {{{
# dropbearkey -t rsa -f /etc/id_rsa -s 2048
Will output 2048 bit rsa secret key to '/etc/id_rsa'
Generating key, this may take a while...
Public key portion is:
Fingerprint: md5 aa:fa:b7:5f:05:23:53:aa:4e:09:ad:db:10:0c:58:2d
}}}
   19. Connect to the machine that will be storing the backups; copy the "ssh-rsa AAAA" line (bolded above) to .ssh/authorized_keys; '''make sure it is one line long (it's ok for it to wrap around the screen).'''

  {{{
backuphost ~/.ssh $ cat>>authorized_keys
ssh-rsa AAAA....
^D
}}}
   20. Make sure the authorized_keys and the .ssh directory have the proper permissions:

  {{{
backuphost ~/.ssh $ chmod 0600 authorized_keys
backuphost ~/.ssh $ chmod 0700 ~/.ssh
}}}
   21. Make a directory to hold the backup  {{{
# mkdir ~/backup}}}
     22. Back on the WRTSL54GS router, install the rsync package:  {{{
# ipkg install rsync}}}
    23. You can now create an rsync script or crontab entry that will rsync your files to the backup server!

    {{{
# rsync -vv -u -a --rsh="ssh -i /etc/id_rsa" --stats --progress <source> <user>@<domain>:<destination>}}}
