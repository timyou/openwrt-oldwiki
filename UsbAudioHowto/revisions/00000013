= USB Audio Support =
USB capable routers such as the ASUS WL-500g/gx/g Premium support USB Audio adapters to turn your router into a networked music player.

USB Audio support is included in !OpenWrt Kamikaze and higher.

To use USB Audio you will need to build your own firmware using buildroot CVS.

= Kernel Packages =
Support is provided by several packages which you have to install.

Soundcard Support ('''KMOD_SOUNDCORE'''):

 . This selects the kernel module soundcore.o which is reqired by both OSS and ALSA.
Support for USB Soundcards ('''KMOD_USB_AUDIO'''):

 . This adds the standard kernel module audio.o which provides OSS sound support.
kmod-alsa ('''KMOD_ALSA'''):

 . This is an alternative to KMOD_USB_AUDIO which cross-compiles the latest ALSA drivers. This package includes all the alsa modules (snd_*) requred for USB Audio support including OSS emulation. These drivers take up more space (and ram) than the OSS one, but they may provide better support and/or performance over kernel OSS.
If you decide to run the Kernel 2.6 you should select the ALSA drivers. It is important to know that the ALSA drivers emulate OSS compatiblity. If you use MPD for instance with this emulation you sound may not be perfect while scrolling in audio files. To make alsa work it is necessary to copy a alsa.conf to the router /usr/share/alsa/alsa.conf.You may build both oss and alsa as packages but only one can be used at a time.

= Applications =
== Music Player Daemon ==
At the time of writing, only one audio application (mpd) has been packaged.

MPD (Music Player Daemon) is a small music player with support for FLAC, MP3 and OGG files. It is a daemon process which is typically controlled by a client such as gmpc running on another desktop machine. For more information about MPD, visit the website at http://www.musicpd.org.

MPD is configured in the file /etc/mpd.conf. The default config file probably won't work as-is, but it should have enough comments to  be edited easily. The MPD package does not currently contain a script to start MPD at boot.

Your music should be accessable through the filesystem. Mine is mounted from an NFS share, you could also use a USB disk or pen drive connected locally.

Please see this link for a full install guide of MPD and phpMp2 on an ASUS Wl500gx - should work on other !OpenWrt devices too: http://mpd.wikicities.com/wiki/OpenWRT_FullInstall

== madplay ==
In Feb 2007 Kamikaze contained [http://www.underbit.com/products/mad/ madplay], which is a command-line player. In combination with wget it can act as an Internet radio. Find some MP3 stream and try something like {{{wget -O - http://64.236.34.97:80/stream/1014 | madplay -}}}

= Devices =
Any USB Audio device supported by Linux should work with !OpenWrt. I have successfully used two cheap USB-Stick cards as pictured below. These were purchased in Australia for AU $20 each. The black one has a built-in amplifier which directly drives a set of bookshelf speakers to quite a good listening volume. The one with the buttons appears as a USB HID device and you can get key press events in /dev/input/eventX. This could be used to hack up a simple control interface on the router.

[http://users.tpg.com.au/davico/images/usbsoundcard_1.jpg] [http://users.tpg.com.au/davico/images/usbsoundcard_2.jpg]

Confirmed to work with [http://www.trust.com/14366 Trust Sp-2800p USB Speaker Set].

 * Terratec AUREON 5.1 USB MKII
= Future =
I would like to find music player software supporting the UPnP Media Renderer standard. This would turn the router into a "wireless music player" simillar to those made by roku, Linksys, Netgear, Philips (streamium), etc, etc. This would allow the router to automatically discover music on other computers and allow it to be controlled though upnp compliant media players.

If anyone knows of any ''free'' music players they would like ported to !OpenWrt, please email david.collett@gmail.com .
