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
 * Disable USB2 and OSS if necesarry:
  * ''rm -f /etc/modules.d/50-usb2''
  * ''rm -f /etc/modules.d/60-usb-audio''
 * Make sure the following packages are installed:
  * '''anyremote''' - remote control program
  * '''mpd''' - the music player daemon
  * '''mpc''' - mpd control program
  * '''at''' - run programs at specific times, used for snooze and alarm
  * '''ntpclient''' - make sure you get up on time

 * Set your timezone in ''/etc/TZ'' (e.g. Germany: CET-1CEST-2,M3.5.0/02:00:00,M10.5.0/03:00:00)
 * Set your mpd up to use ALSA by uncommenting the ALSA config entries in ''/etc/mpd.conf''
