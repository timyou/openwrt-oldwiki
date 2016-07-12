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

This allows you to install things onto your thumb-drive. However, the activating of init scripts isn't really sorted out properly.

One solution is to create a /etc/fstab and place your drive in there.  Then you need to link your /usb/etc/init.d/  into /etc/rc.d/

My solution is to mount and fsck in parallel to the main init.  This way the base system is up as quickly as possible.  The extra processes are then started as soon as the drive is mounted.

==== /etc/init.d/usbdrive ====
{{{
#!/bin/sh /etc/rc.common

START=40
STOP=40

export EXTRA_COMMANDS="startup"
export EXTRA_HELP="        startup  Start-up process for drive"


start()
{
        echo -n "Starting USB Partition:  "
	# Don't stop processing
	#/etc/init.d/usbdrive_start &
	( startup ) &

}     
stop()
{                                          
	echo -n "Stoping processes"
	for i in /usb/etc/rc.d/K*; do
	  $i stop
	done
        echo -n "Umounting USB drive:  "   
        sync
        sync                                          
        umount /dev/scsi/host0/bus0/target0/lun0/part1
        echo "Done."
}        
restart()
{           
        stop 
        start
}

startup()
{
	echo -n "Testing USB Partition:  " >/var/log/usb_init
	e2fsck -p /dev/scsi/host0/bus0/target0/lun0/part1
	echo -n "Mounting USB drive: " >>/var/log/sub_init
	mount -t ext3 -o noatime /dev/scsi/host0/bus0/target0/lun0/part1 /usb
	echo -n "Starting options" >>/var/log/usb_init
	export PATH=/bin:/usb/bin:/sbin:/usb/sbin:/usr/bin:/usb/usr/bin:/usr/sbin:/usb/usr/sbin
	export LD_LIBRARY_PATH=/lib:/usb/lib:/usr/lib:/usb/usr/lib
	for i in /usb/etc/rc.d/S*; do
	 # echo $i
	  echo -n "Starting $i" >>/var/log/usb_init
	  $i start 2>&1 >>/var/log/usb_init
	done
}

}}}

I have modified disable() enable() and enabled() in /etc/rc.common
{{{

disable() {
	name="$(basename "${initscript}")"
	basedir=${initscript%/[^/]*}
	[ -z $basedir ] || cd $basedir
	cd ../rc.d
	stripname=${name##[SK][0-9][0-9]}
	rm -f [SK]??$stripname
}

enable() {
	name="$(basename "${initscript}")"

	basedir=${initscript%/[^/]*}
	[ -z $basedir ] || cd $basedir
	cd ../rc.d

	stripname=${name##[SK][0-9][0-9]}
	rm -f [SK]??$stripname

	[ "$START" ] && ln -s "../init.d/$name" S${START}${stripname}
	[ "$STOP" ] && ln -s "../init.d/$name" K${STOP}${stripname}
}

enabled() {
	name="$(basename "${initscript}")"
	stripname=${name##[SK][0-9][0-9]}
	basedir=${initscript%/[^/]*}
	[ -z $basedir ] || cd $basedir
	cd ../rc.d
	[ -x "S${START}${stripname}" ]
}

}}}

=== Installing onto the USB Drive ===

Installation onto the USB drive is now easy:

{{{
  ipkg -d usb install asterisk
  /usb/etc/init.d/asterisk enable
}}}

MORE TO COME.
