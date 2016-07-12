## Please edit system and help pages ONLY in the moinmaster wiki! For more
## information, please see MoinMaster:MoinPagesEditorGroup.
##acl MoinPagesEditorGroup:read,write,delete,revert All:read
##master-page:HelpTemplate
##master-date:Unknown-Date
#format wiki
#language en
== Installing Onto USB Drive ==

Install the kernel modules you will need (assuming usb2 here):

=== Preparation ===
{{{
ipkg install kmod-fs-ext3 kmod-scsi-core kmod-usb-core kmod-usb-storage kmod-usb2
}}} 

Plug in your drive and work out what device you have.  This is on 2.4 with devfs. Then mount it.
{{
  find /dev/scsi -type f 
  mkdir -p /usb
  mount /dev/scsi/host0/bus0/target0/lun0/part1 /usb
}}

Add in a destination to your ipkg.conf

{{
  echo "dest usb /usb/">> /etc/ipkg.conf
}}

MORE TO COME.

=== Display ===
xxx
