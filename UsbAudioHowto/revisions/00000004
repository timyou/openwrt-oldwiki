= USB Audio Support =

USB Capable routers such as the Asus WL-500g/gx support USB Audio adapters to turn your router into a networked music player.

USB Audio support entered OpenWRT CVS around Sept 2005, at the time of writing it is not included in any releases (eg. White Russian).

To use USB Audio you will need to build your own firmware using buildroot CVS.

= Kernel Packages =

Support is provided by several packages which can be selected while configuring buildroot (make menuconfig).

Soundcard Support ('''KMOD_SOUNDCORE'''):

    This selects the kernel module soundcore.o which is reqired by both OSS and ALSA.

Support for USB Soundcards ('''KMOD_USB_AUDIO'''):

    This adds the standard kernel module audio.o which provides OSS sound support.

kmod-alsa ('''KMOD_ALSA'''):

    This is an alternative to KMOD_USB_AUDIO which cross-compiles the latest ALSA drivers. This package includes all the alsa modules (snd_*) requred for USB Audio support including OSS emulation. These drivers take up more space (and ram) than the OSS one, but they may provide better support and/or performance over kernel OSS. (they do for me)

You may build both oss and alsa as packages but only one can be used at a time.

= Applications =

At the time of writing, only one audio application (mpd) has been packaged.

MPD (Music Player Daemon) is a small music player with support for FLAC, MP3 and OGG files. It is a daemon process which is typically controlled by a client such as gmpc running on another desktop machine. For more information about MPD, visit the website at http://www.musicpd.org.

MPD is configured in the file /etc/mpd.conf. The default config file probably won't work as-is, but it should have enough comments to  be edited easily. The MPD package does not currently contain a script to start MPD at boot.

Your music should be accessable through the filesystem. Mine is mounted from an NFS share, you could also use a USB disk connected locally.

= Future =

I would like to find music player software supporting the UPnP Media Renderer standard. This would turn the router into a "wireless music player" simillar to those made by roku, linksys, netgear, philips (streamium), etc, etc. This would allow the router to automatically discover music on other computers and allow it to be controlled though upnp compliant media players.

If anyone knows of any ''free'' music players they would like ported to openwrt, please email david.collett@gmail.com.
