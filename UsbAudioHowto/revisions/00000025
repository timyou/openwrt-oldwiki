= USB Audio Support =
USB capable routers such as the ASUS WL-500g/gx/g Premium support USB Audio adapters to turn your router into a networked music player.

USB Audio support is included in !OpenWrt Kamikaze and higher.

== Kernel Module Packages ==
Support is provided by several packages, which you have to install with ipkg. Those packages inlcude: kmod-sound-core, kmod-usb-audio, 

=== OSS Sound ===
 * This selects the kernel module soundcore.o which is reqired by both OSS and ALSA.
Support for USB Soundcards ('''kmod-usb-audio'''):

ipkg install kmod-usb-audio kmod-soundcore 
 * This adds the standard kernel module audio.o which provides OSS sound support. ''moved from kmod_alsa, audio.o is for OSS''
to play sound you can install sox, but be aware that it installs lots of dependencies.

#ipkg install sox

test it as follows:
#sox -q $1 -t ossdsp /dev/sound/dsp


=== ALSA Sound ===

kmod-alsa ('''KMOD_ALSA'''):

 * This is an alternative to KMOD_USB_AUDIO which cross-compiles the latest ALSA drivers. This package includes all the alsa modules (snd_*) requred for USB Audio support including OSS emulation. These drivers take up more space (and ram) than the OSS one, but they may provide better support and/or performance over kernel OSS.
If you decide to run the Kernel 2.6 you should select the ALSA drivers. It is important to know that the ALSA drivers emulate OSS compatiblity. If you use MPD for instance with this emulation you sound may not be perfect while scrolling in audio files. To make alsa work it is necessary to copy a alsa.conf to the router /usr/share/alsa/alsa.conf.You may build both oss and alsa as packages but only one can be used at a time.

=== Esound (esd) ===

Support for this hasn't yet been integrated into the official repositories, but there's a preliminary package available.

# ipkg install kmod-usb-audio

# ipkg install http://klasseonline.dyndns.org/openwrt/kamikaze/7.09/packages/esound-oss_0.2.38-1_mipsel.ipk

You can start the eSound daemon by typing

# esd -d /dev/sound/dsp -tcp -public &

Enter this command into a startup script to have the daemon started at boot. You should now be able to stream audio to your router's IP on port 16001 from any application that has an ESD output plugin. For Linux Desktops, that includes Mplayer, amaroK, xmms and others (take a look [http://wl500g.info/showthread.php?t=6508 HERE] for instructions). On Windows there's an ESD output plugin for WinAmp.



= Applications =
== Music Player Daemon ==
MPD (Music Player Daemon) is a small music player with support for FLAC, MP3 and OGG files. It is a daemon process which is typically controlled by a client such as gmpc running on another desktop machine. For more information about MPD, visit the website at http://www.musicpd.org.

MPD is configured in the file /etc/mpd.conf. The default config file probably won't work as-is, but it should have enough comments to  be edited easily. The MPD package does not currently contain a script to start MPD at boot.

Your music should be accessible through the filesystem. Mine is mounted from an NFS share, you could also use a USB disk or pen drive connected locally.

Please see this link for a full install guide of MPD and phpMp2 on an ASUS Wl500gx - should work on other !OpenWrt devices too: http://mpd.wikicities.com/wiki/OpenWRT_FullInstall

== madplay ==
In Feb 2007 Kamikaze contained [http://www.underbit.com/products/mad/ madplay], which is a command-line player. In combination with wget it can act as an Internet radio. Find some MP3 stream and try something like {{{wget -O - http://64.236.34.97:80/stream/1014 | madplay -}}}

The madplay and mp3blaster packages are also available as part of the ["Optware"] collection of installable packages.

= Devices =
Any USB Audio device supported by Linux should work with !OpenWrt. I have successfully used two cheap USB-Stick cards as pictured below. These were purchased in Australia for AU $20 each. The black one has a built-in amplifier which directly drives a set of bookshelf speakers to quite a good listening volume. The one with the buttons appears as a USB HID device and you can get key press events in /dev/input/eventX. This could be used to hack up a simple control interface on the router.

[http://users.tpg.com.au/davico/images/usbsoundcard_1.jpg] [http://users.tpg.com.au/davico/images/usbsoundcard_2.jpg]

Confirmed to work with [http://www.trust.com/14366 Trust Sp-2800p USB Speaker Set].

 * Terratec AUREON 5.1 USB MKII

Note: There are problems with USB 1.1 sound cards connected through USB 2.0 hubs with the 2.4 kernels. This has been resolved in 2.6; another option is to enable the CONFIG_USB_EHCI_SPLIT_ISO option described [http://www.nslu2-linux.org/wiki/Peripherals/AudioAdapter here]. With Linksys WRTSL54GS (only one USB connector, installing another requires hardware modification) or USB "universal laptop docking stations" (a USB2.0 hub plus some combination of USB 1.1 audio, HID, serial/parallel and a LAN interface in one integrated unit), the presence of a USB hub may be unavoidable.

See TableOfPeripheralHardware for additional information on these devices.

= User interfaces =
The makers of mpd / mpc provide (unsupported) C source code for a [http://musicpd.org/mpcstick.shtml mpcstick] application. This could allow a joystick to be used to provide simple control (ff/rewind, prev, next...) for a media player, or could serve as example code if one were to attempt to develop an application to interface other HID units (such as USB numeric keypads and mice). Most USB numeric keypads provide at least seventeen keys (0-9 . + - * / enter numlock) which could, if suitably-adapted software was created, operate a fully self-contained audio player. The ability to jump directly to any playlist entry by number, as well as a full set of standard functions such as prev/next, play, stop, pause or volume control, could easily be possible.

= Future =
I would like to find music player software supporting the UPnP Media Renderer standard. This would turn the router into a "wireless music player" simillar to those made by Roku, Linksys, Netgear, Philips (streamium), etc, etc. This would allow the router to automatically discover music on other computers and allow it to be controlled though upnp compliant media players.

If anyone knows of any ''free'' music players they would like ported to !OpenWrt, please email david.collett@gmail.com .
----
CategoryHowTo
