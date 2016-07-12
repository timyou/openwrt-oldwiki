= HOWTO turn your USB enabled Router into the coolest Alarm clock ever =
----
'''This HOWTO is a work in progress, I have it running, but need to recreate all the steps. This message will be removed once everything is in place.'''
----

== Goals: ==

If you follow this HOWTO you should end up with a machine capable of:

 * Playing mp3/ogg/flac from any mountable source (usb-storage, shfs, cifs, nfs)
 * Using your Router as an alarm clock
 * Controlling snooze and alarm times from a bluetooth enabled phone

== Prerequisites:  ==

These are the parts i used to achieve the above.

 * Asus WL500g Premium Router
 * As of writing: Kamikaze r11112
 * A supported USB Bluetooth dongle
 * A supported USB Soundcard

== Caveats: ==

Things which still bother me

 * I had to disable USB2 support completely as it would not work with my USB hub
 * anyremote is not yet in OpenWRT, I submitted my files here: [[https://dev.openwrt.org/ticket/3433]]
 * I wanted to be able to plug USB sticks with music in and just have them added to mpd, which required me to hack the usb-storage scripts: [[https://dev.openwrt.org/ticket/3432]]
 * It is not possible to mount DAAP shares, maybe with a 2.6 Kernel and fuse-daap

== HOWTO: ==

 * Flash your router with a recent Kamikaze build
 * If required, install the provided usb-storage scripts
  * You can then add handlers to `/etc/usb-handlers.d/` to e.g. link added music to your mpd music directory
 * Disable USB2 and OSS if necesarry:
  * `rm -f /etc/modules.d/50-usb2`
  * `rm -f /etc/modules.d/60-usb-audio`
 * Make sure the following packages are installed:
  * '''anyremote''' - remote control program
  * '''mpd''' - the music player daemon
  * '''mpc''' - mpd control program
  * '''at''' - run programs at specific times, used for snooze and alarm
  * '''ntpclient''' - make sure you get up on time
  * '''bash''' - I think i used some bash features somewhere
 * Set your timezone in `/etc/TZ` (e.g. Germany: CET-1CEST-2,M3.5.0/02:00:00,M10.5.0/03:00:00)
 * Set your mpd up to use ALSA by uncommenting the ALSA config entries in `/etc/mpd.conf`
 * Create the mpd directories `mkdir -p ~/.mpd/playlists`
 * Enable ''sdpd'' in `/etc/config/bluetooth`
 * Set auth type in `/etc/bluetooth/hicd.conf` to ''auto'', set passkey to something usable (e.g. 6712)
 * Pair your phone with the router
 * Put the following scripts in `/usr/bin/`
`/usr/bin/alarm` - example: `alarm 7:00` will set an alarm clock for 7:00
{{{
#!/bin/bash
if [ -z "$2" ]; then
	vol=50
else
	vol=$2
fi
echo "/usr/bin/alarm_play $vol" | at $1
}}}
`/usr/bin/alarm_play` - helper script for the alarm
{{{
#!/bin/sh
if [ -z $(mpc | grep playing) ]; then
	mpc --no-status clear
	mpc --no-status load alarm_pl
	mpc --no-status volume 0
	mpc --no-status random on
	mpc --no-status play
	mpc --no-status pause
	echo $1 > ~/.ppvolume
	/usr/bin/pp &
fi
}}}
`/usr/bin/pp` - fade sound in and out, this might be doable in a better way
{{{
#!/bin/bash

sleep="1s"
fade_sec="10"

curvol=`mpc | grep "volume" | cut -d " " -f2 | tr -d "%"`
if [ -z "`mpc | grep playing`" ]; then
    mpc play --no-status
    start=0
    end=`cat $HOME/.ppvolume`
    inc=$(($end/$fade_sec))
else
    echo $curvol > $HOME/.ppvolume
    start=$curvol
    inc=-$(($curvol/$fade_sec))
    end=0
fi
#echo $start $inc $end
for x in `seq $start $inc $end`; do
    mpc volume $x --no-status
#    mpc volume $x
    sleep $sleep
done

if [ $end -eq 0 ]; then
    mpc volume 0 --no-status
    mpc toggle --no-status
else
    mpc volume $end --no-status
fi
}}}
 * You need a playlist `alarm_pl` in mpd which will be played at random for alarm
