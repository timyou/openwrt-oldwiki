## Please edit system and help pages ONLY in the moin*master wiki! For more
## information, please see MoinMaster:MoinPagesEditorGroup.
##acl MoinPagesEditorGroup:read,write,delete,revert All:read
##master-page:HelpTemplate
##master-date:Unknown-Date
#format wiki
#language en
== Installing Onto USB Drive ==

This is a supplement to the [:UsbStorageHowto:USB Storage HowTo], which has many useful tips like formatting an ext3 drive and handling usb1.1 devices.  Realistically, if it's not USB2, then forget swap-space.

I will assume that you have formatted a USB drive with a linux compatible (not fat32) filesystem, or that you will once the modules are loaded.

=== Preparation ===
Install the kernel modules you will need (assuming usb2 here):

{{{
opkg install kmod-fs-ext3 kmod-scsi-core kmod-usb-core kmod-usb-storage kmod-usb2
}}} 

=== Mount the drive ===
Plug in your drive and work out what device you have.  This is on 2.4 with devfs. Then mount it.
{{{
  find /dev/scsi -type b 
  mkdir -p /usb
  mount /dev/scsi/host0/bus0/target0/lun0/part1 /usb
}}}

=== Some Configuration details ===
Add in a destination to your opkg.conf (ipkg.conf for older versions):

{{{
  echo "dest usb /usb/">> /etc/opkg.conf
}}}

This allows you to install things onto your thumb-drive. However, the activating of init scripts on alternate destinations isn't really sorted out properly yet - so you will need to get a little creative.

One solution is to create a /etc/fstab and place your drive in there.  Then you need to activate your /usb/etc/init.d/  into /etc/rc.d/. Be aware that the '''default''' 'init.d/drivername activate' function will fail here - it will place a symlink in /etc/rc.d pointing to /etc/init.d/drivername - which won't get you far.

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

You will also need to modify your profile to add the paths in.

==== /etc/profile ====
{{{
#export PATH=/bin:/sbin:/usr/bin:/usr/sbin
export PATH=/bin:/usb/bin:/sbin:/usb/sbin:/usr/bin:/usb/usr/bin:/usr/sbin:/usb/usr/sbin
}}}

I have modified disable() enable() and enabled() in /etc/rc.common.  The 'init.d/drivername enable' function will place a link in ../rc.d that points to ../init.d/drivername. ''Note: This has been modified (2/7/2008) to support being placed into files/etc directory on a custom build.  If IPKG_INSTROOT isn't supported, the image (from bitter experience) will turn your router into a switch and you will have to use the inbuilt rescue mode.''

{{{

disable() {
	name="$(basename "${initscript}")"

        if [ "$IPKG_INSTROOT" == "" ]; then
                basedir=${initscript%/[^/]*}
                [ -z $basedir ] || cd $basedir
                cd ../rc.d
        else
                cd "$IPKG_INSTROOT"/etc/rc.d
        fi

        stripname=${name##[SK][0-9][0-9]}
	rm -f [SK]??$stripname
}

enable() {
	name="$(basename "${initscript}")"

        if [ "$IPKG_INSTROOT" == "" ]; then
                basedir=${initscript%/[^/]*}
                [ -z $basedir ] || cd $basedir
                cd ../rc.d
        else
                cd "$IPKG_INSTROOT"/etc/rc.d
        fi

	stripname=${name##[SK][0-9][0-9]}
	rm -f [SK]??$stripname

	[ "$START" ] && ln -s "../init.d/$name" S${START}${stripname}
	[ "$STOP" ] && ln -s "../init.d/$name" K${STOP}${stripname}
}

enabled() {
	name="$(basename "${initscript}")"

        if [ "$IPKG_INSTROOT" == "" ]; then
                basedir=${initscript%/[^/]*}
                [ -z $basedir ] || cd $basedir
                cd ../rc.d
        else
                cd "$IPKG_INSTROOT"/etc/rc.d
        fi
	stripname=${name##[SK][0-9][0-9]}
	[ -x "S${START}${stripname}" ]
}

}}}

=== Installing onto the USB Drive ===

Installation onto the USB drive is now easy.  One small caveat though - don't install kernel modules or iptables modules onto your alternate drive.  They will not get loaded.  It is probably easy to fix - but I decided it wasn't worth the effort - kernel modules are generally better off on the main memory.

{{{
  opkg -d usb install asterisk14
  /usb/etc/init.d/asterisk enable
}}}

=== Adding a swap space to the USB ===

For this you will need some extra utilities
{{{
  opkg install kmod-loop
  opkg -d usb install losetup swap-utils
}}}

.. and a nice little init script.  This is not generic. It would be very easy to make
it so - however I haven't yet done it.  It should be easily able to support multiple files.

==== /usb/etc/init.d/swapfile ====

{{{

#!/bin/sh /opt/etc/rc.common
START=01 
STOP=99

DEST=/usb
PIDFILE=$DEST/var/run/swapfile.loop
SWAPPATH=$DEST/tmp
SWAPFILE=swapfile
SWAPSIZE=100000
export EXTRA_COMMANDS="status prepare"
export EXTRA_HELP=$(echo -e "        status  Status of service\n        prepare Initialise Swap")
LOGFILE=/opt/var/log/swapstart
LOSETUP=/opt/usr/sbin/losetup

status() {
  swapon -s
}

prepare() {
  [ -d $SWAPPATH ] || mkdir -p $SWAPPATH
  dd if=/dev/zero of=/$SWAPPATH/$SWAPFILE count=$SWAPSIZE
  if [ -f $SWAPPATH/$SWAPFILE ]
  then
    TMPLOOP=$($LOSETUP -f)
    $LOSETUP $TMPLOOP /$SWAPPATH/$SWAPFILE
    mkswap $TMPLOOP
    $LOSETUP -d $TMPLOOP
  fi
}
start() {
  if [ -n $SWAPPATH ] && [ -n $SWAPFILE ]
  then

    [ -f $PIDFILE ] && ($LOSETUP $(cat $PIDFILE) || rm $PIDFILE)

    if [ -f $PIDFILE ]
    then
      echo $PIDFILE exists
    else
      [ -f $SWAPPATH/$SWAPFILE ] || prepare

      if [ -f "$SWAPPATH/$SWAPFILE" ]
      then
	[ -f $LOGFILE ] && rm $LOGFILE
	TMPLOOP=$($LOSETUP -f)
	echo Setup $SWAPPATH/$SWAPFILE on $TMPLOOP as swap | tee -a $LOGFILE

	if [ -z $TMPLOOP ]
	then
	  echo No loop available
	else
          $LOSETUP $TMPLOOP /$SWAPPATH/$SWAPFILE | tee -a $LOGFILE
          sleep 2
          echo $TMPLOOP > $PIDFILE
          swapon $TMPLOOP | tee -a $LOGFILE
          swapon -s >> $LOGFILE
	fi
      fi
    fi
  fi
}

stop() {
  if [ -f $PIDFILE ]
  then
    TMPLOOP=$(cat $PIDFILE)
    swapoff $TMPLOOP && $LOSETUP -d $TMPLOOP && rm $PIDFILE
  fi
}

}}}

Once again, this is activated and enabled using:

{{{
  /usb/etc/init.d/swapfile start
  /usb/etc/init.d/swapfile enable
}}}

.. and there you have it.  Your router with a USB mounted, a swap-file and more space to play with while you get things sorted.  Pipe your logs to it.  Put xmail on your router and have a small mail server.  Run asterisk and have voicemail.  I have all of these working.

Be aware that installing kernel modules or iptables modules onto an alternate drive does not work.  You would need to fix up both the modules.conf and possibly symlink in the modules directory somehow.  I decided it was not worth doing.

I even have xmail receiving VOIP mailbox emails - unpacking them and placing them in the asterisk voicemail directory (appropriately ''soxed'' into shape). I've added this (filter script included) to the voip-info wiki here:  [http://www.voip-info.org/wiki/view/Xmail+filter+to+Voicemail+script Xmail Filter to Voicemail]

=== Updated /etc/rc.common === 

{{{
#!/bin/sh
# Copyright (C) 2006 OpenWrt.org

. $IPKG_INSTROOT/etc/functions.sh

start() {
	return 0
}

stop() {
	return 0
}

reload() {
	return 1
}

restart() {
	trap '' TERM
	stop
	start
}

boot() {
	start
}

shutdown() {
	return 0
}

disable() {
	name="$(basename "${initscript}")"
	if [ "$IPKG_INSTROOT" == "" ]; then
		basedir=${initscript%/[^/]*}
		[ -z $basedir ] || cd $basedir
		cd ../rc.d
	else
		cd "$IPKG_INSTROOT"/etc/rc.d
	fi
	
	stripname=${name##[SK][0-9][0-9]}
	rm -f [SK]??$stripname
}

enable() {
	name="$(basename "${initscript}")"

	if [ "$IPKG_INSTROOT" == "" ]; then
		basedir=${initscript%/[^/]*}
		[ -z $basedir ] || cd $basedir
		cd ../rc.d
	else
		cd "$IPKG_INSTROOT"/etc/rc.d
	fi

	stripname=${name##[SK][0-9][0-9]}
	rm -f [SK]??$stripname

	[ "$START" ] && ln -s "../init.d/$name" S${START}${stripname}
	[ "$STOP" ] && ln -s "../init.d/$name" K${STOP}${stripname}
}

enabled() {
	name="$(basename "${initscript}")"

	if [ "$IPKG_INSTROOT" == "" ]; then
		basedir=${initscript%/[^/]*}
		[ -z $basedir ] || cd $basedir
		cd ../rc.d
	else
		cd "$IPKG_INSTROOT"/etc/rc.d
	fi

	stripname=${name##[SK][0-9][0-9]}
	[ -x "S${START}${stripname}" ]
}

depends() {
	return 0
}

help() {
	cat <<EOF
Syntax: $initscript [command]

Available commands:
	start	Start the service
	stop	Stop the service
	restart	Restart the service
	reload	Reload configuration files (or restart if that fails)
	enable	Enable service autostart
	disable	Disable service autostart
$EXTRA_HELP
EOF
}

initscript="$1"
[ "$#" -ge 1 ] && shift
action="$1"
[ "$#" -ge 1 ] && shift

. "$initscript"

cmds=
for cmd in $EXTRA_COMMANDS; do
	cmds="${cmds:+$cmds$N}$cmd) $cmd \"\$@\";;"
done

eval "case \"\$action\" in
	start) start \"\$@\";;
	stop) stop \"\$@\";;
	reload) reload \"\$@\" || restart \"\$@\";;
	restart) restart \"\$@\";;
	boot) boot \"\$@\";;
	shutdown) shutdown \"\$@\";;
	enable) enable \"\$@\";;
	enabled) enabled \"\$@\";;
	disable) disable \"\$@\";;
	$cmds
	*) help;;
esac"
}}}

----
CategoryHowTo
