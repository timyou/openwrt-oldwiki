#FORMAT
#!/bin/sh /etc/rc.common

START=11
STOP=91

bootext_cleanup() { # [cleanup_level]
 [ "$1" -ge 3 ] && grep -q '^[^ ]* /rom ' /proc/mounts && mount -o move /rom $putold/rom
 [ "$1" -ge 2 ] && { . $putold/bin/firstboot ; pivot $putold $target ; }
 [ "$1" -ge 1 ] && umount -l $target/etc
 return 0
}

bootext_fail() { # <error_message> [cleanup_level]
 echo "$1" >&2
 [ ! "$2" ] || bootext_cleanup $2
 exit 1
}

bootext_quit() { # <message>
 echo "$1" >&2
 exit 0
}

bootext_start() {
 ! grep -q "^$device / " /proc/mounts || bootext_quit "$name already on /"

 if ! grep -q "^$device $target " /proc/mounts
 then
  ! grep -q "^$device " /proc/mounts || bootext_fail "$name already mounted"

  for module in $modules
  do
   if ! grep -q "^$module " /proc/modules
   then
    [ $module != mmc ] || [ ! "$gpiomask" ] || echo "$gpiomask" > /proc/diag/gpiomask || bootext_fail "could not set gpiomask"
    insmod $module || bootext_fail "could not insert $module module"
   fi
  done

  while [ ! -b $device ]
  do
   [ "$waitdev" -gt 0 ] || bootext_fail "$device does not exist"
   waitdev=$(( $waitdev - 1 ))
   sleep 1
  done

  [ -d $target ] || mkdir $target || bootext_fail "could not create mountpoint $target"
  mount ${filesys:+-t $filesys} ${mountopt:+-o $mountopt} $device $target || bootext_fail "could not mount $name on $target"
 fi

 [ -d $target$putold ] || mkdir $target$putold || bootext_fail "could not create mountpoint $putold"
 [ -d $target/etc ] || mkdir $target/etc || bootext_fail "could not create mountpoint /etc"
 mount -o bind /etc $target/etc || bootext_fail "could not bind mount /etc"

 . /bin/firstboot
 pivot $target $putold || bootext_fail "could not pivot to $target" 1

 ! grep -q "^[^ ]* $putold/rom " /proc/mounts || { [ -d /rom ] || mkdir /rom && mount -o move $putold/rom /rom ; }

 return 0
}

bootext_stop() {
 grep -q "^$device / " /proc/mounts || bootext_quit "$name not on /"

 bootext_cleanup 999
}

bootext_config() { # <section> <action>
 local section=$1
 local action=$2
 local enabled device name target putold modules gpiomask waitdev filesys mountopt

 config_get_bool enabled $section enabled 1
 [ "$enabled" -gt 0 ] || return 0
 config_get device $section device
 [ "$device" ] || bootext_fail "external boot device not configured"
 config_get name $section name
 config_get target $section target
 config_get putold $section putold
 config_get modules $section modules
 config_get gpiomask $section gpiomask
 config_get waitdev $section waitdev
 config_get filesys $section filesys
 config_get mountopt $section mountopt

 [ "$name" ] || name="$device"
 [ "$putold" ] || putold="${target:-/old}"
 [ "$target" ] || target="/${filesys:-new}"

 bootext_$action
}

start() {
 config_load bootfromexternalmedia
 config_foreach bootext_config bootfromexternalmedia start
}

stop() {
 config_load bootfromexternalmedia
 config_foreach bootext_config bootfromexternalmedia stop
}
