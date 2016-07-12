## Please edit system and help pages ONLY in the moinmaster wiki! For more
## information, please see MoinMaster:MoinPagesEditorGroup.
##acl MoinPagesEditorGroup:read,write,delete,revert All:read
##master-page:HelpTemplate
##master-date:Unknown-Date
#format wiki
#language en
== Installing Onto USB Drive ==

=== Preparation ===
Install the kernel modules you will need (assuming usb2 here):

{{{
ipkg install kmod-fs-ext3 kmod-scsi-core kmod-usb-core kmod-usb-storage kmod-usb2
}}} 

=== Mount the drive ===
Plug in your drive and work out what device you have.  This is on 2.4 with devfs. Then mount it.
{{{
  find /dev/scsi -type f 
  mkdir -p /usb
  mount /dev/scsi/host0/bus0/target0/lun0/part1 /usb
}}}

=== Some Configuration details ===
Add in a destination to your ipkg.conf

{{{
  echo "dest usb /usb/">> /etc/ipkg.conf
}}}

This allows you to install things onto your thumb-drive.  The init scripts aren't really
sorted properly.

One solution is to create a /etc/fstab and place your drive in there.  Then you need to link your /usb/etc/init.d/  into /etc/rc.d/

My solution is to mount and fsck in parallel to the main init.  This way the base system is up as quickly as possible.  The extra processes are then started as soon as the drive is mounted.



MORE TO COME.

=== Display ===
xxx
