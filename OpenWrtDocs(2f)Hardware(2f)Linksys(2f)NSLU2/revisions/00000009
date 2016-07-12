= Linksys NSLU2 =
The Linksys NSLU2 (a.k.a. SLUG) is a network storage link based on the IXP42x processor clocked  at 266Mhz (older versions of the NSLU2 defaulted to 133MHz, but can be easily "de-underclocked").  It contains 8MB flash, 32MB RAM, one ethernet i/f, two USB2.0 ports, and is provided  with a 2.0A 5V power supply.

= Why Run OpenWRT? =
The SLUG has an active user community with several popular firmware distros (e.g. Debian Slug)  so why bother to port OpenWRT?  Well, most likely you agree with OpenWRT's minimalist philosophy  and would rather spend your time adding the features you want rather than deleting those you don't. However, that doesn't mean that you should ignore the vast amount of experience gathered and documented by the SLUG developers...

Note that the NSLU2-Linux project (http://www.nslu2-linux.org) fully supports the porting of OpenWRT to the NSLU2, and intends to "bless" OpenWRT as the firmware of choice for people who want to run all their applications from the internal flash memory only (i.e. with no external storage at all).
= NSLU2 Hardware Reference =
http://www.nslu2-linux.org/wiki/Info/HomePage

= Status of the Port =

Kamikaze image builds and boots.  squashfs image reports:

 . Warning: unable to open an initial console.

but that warning seems to be harmless.

jffs2 image gets farther but reports:

 . init started:  BusyBox v1.4.1 (2007-04-21 18:44:24 EDT) multi-call binary [[BR]] syslogd: /dev/null: No such file or directory [[BR]] /etc/init.d/rcS: /etc/init.d/rcS: 19: Can't open /dev/null [[BR]]

It works great for me. I guess you where missing the parameter "init=/etc/preinit", as kamikaze fills in /dev on-the-fly after bootup. I didn't have to change anything and just installed with upslug2 using the default Kamikaze images from the openwrt download server. Things to look out for are:
 * The default IP is the one that is set in the NVRAM, so OpenWRT will boot up with the IP it had under the former firmware. This is not the default for other Kamikaze platforms! Note: This is not true for Kamikaze SVN (tested with r8003). Note2: On upslugging the default IP of NSLU2 is 192.168.1.77 (the same as the factory, Unslung and SlugOS behaviour) as of 08-2007.
 * After initial installation with the squashfs firmware, it can take up to five minutes to initialize the jffs2 payload partition. I would wait at least this time before you reboot it forcefully (although unplugging it while it is initializing didn't harm it in my tests)
 * The status LED indication differs from openslug. It is always amber for me (whereas openslug turns green after bootup is complete). This might confuse users migrating from openslug.

= Installation instructions =

You can download the image from the kamikaze-7.06 dir [http://downloads.openwrt.org/kamikaze/7.06/ixp4xx-2.6/openwrt-nslu2-2.6-squashfs.bin]. Then install the upslug2 utility. Many distributions already include it in their package management. You will find more information on the topic on the excellect NSLU2-Linux wiki [http://www.nslu2-linux.org/], specific information on upslug2 is at [http://www.nslu2-linux.org/wiki/Main/UpSlug]. Then set the NSLU2 into upgrade mode. To do this, make sure the NSLU2 is turned off. Then press the reset button with a paper clip or small screwdriver and keep it pressed. Turn the NSLU2 on. The "Ready/Status" led will be yellow. When it changes to a reddish amber shade, immediately release the reset button. If it flashes an alternating amber and green, you have succeded (if not, unplug and try again). Now ''upslug2'' should find the nslu2 over the LAN and display the information. Install the image with ''upslug2 -i filename''. It will flash and verify the upload and then reboot automatically - this is what I call a comfortable firmware interface :)

The NSLU2 will take a few minutes to initialize the JFFS2 partition, don't reboot if you cannot access it immediately. It will start up using the network parameters that are stored in the NVRAM partition, so it will default to DHCP (I think) if not setup differently. If you have set a fixed IP under the original firmware or a previous linux distribution, OpenWRT will retain this. Try telnet and ping to access it. Then follow the standard Kamikaze installation procudures.

= Package repositories =
Look at the [http://www.nslu2-linux.org/wiki/OpenWrt/HomePage OpenWRT page on NSLU2-Linux wiki] for more information on publicly available NSLU2 package repositories.

= TODO =
Little endian images?
