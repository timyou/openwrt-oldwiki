#pragma section-numbers off
||<tablebgcolor="#f1f1ed" tablewidth="40%" tablestyle="margin: 0pt 0pt 1em 1em; float: right; font-size: 0.9em;"style="padding: 0.5em;">[[TableOfContents]]||
== ASUS WL-500g Premium V2 ==
The redesigned version of the ASUS WL-500g Premium router, ["OpenWrtDocs/Hardware/Asus/WL500GP"] , has the following changes:

 * Broadcom BCM5354 CPU @ 240 Mhz
 * On-board wireless LAN controller
 * WLAN port and antenna port have changed sides
Support in trunk since [https://dev.openwrt.org/changeset/10693 changeset 10693].

Sancho: After a long period of fiddling with the SVN trunk, patching, re-compiling, etc. I found out, that the wireless is simply not working. On the other hand, the Kamikaze with 2.4 kernel works just fine. The wireless is turned off, but it's enough to turn it on using web interface. Works like a charm than.

== Hardware ==
There is an [http://www.vr-zone.com/?i=5624 article about the wl-500gPv2] with a picture.

=== Info ===
||<tablewidth="400px" tableheight="289px">'''Architecture''' ||MIPS ||
||'''Vendor''' ||Broadcom ||
||'''Bootloader''' ||CFE ||
||'''System-On-Chip''' ||Broadcom BCM5354 ||
||'''CPU Speed''' ||240 Mhz ||
||'''Flash''' ||8MiB (Macronix 29LV640DB, 64K sector size) ||
||'''RAM''' ||32MiB ||
||'''Wireless''' ||Onboard BCM5354 802.11b/g ||
||'''Ethernet Switch''' || ? ||
||'''USB''' ||2x USB 2.0 ||
||'''Serial''' ||Yes ||
||'''JTAG''' ||No ||
=== Serial Port ===
This 500g v2 has two sets of soldering points.  The first is two rows of 6 pins (JTAG perhaps).  The second, which is the serial port, is one row of four pins.
||Pin 4 || GND ||
||Pin 3 || UART_TX ||
||Pin 2 || UART_RX ||
||Pin 1 || 3.3V ||


When examining the board carefully, one can see that pin 4 has no trace leading to it -- it is simply part of the top layer ground plane.  Pin 1 is connected to a relatively fat power trace.

These serial ports use TTL levels. You need an additional voltage convertor to get a standard serial port. The parameters are 115200 baud and 8-n-1.

=== Getting Kamikaze and Kernel 2.6 Running on the WL500GPV2 ===
==== Preface ====
There are many opportunities for this to not work. You should be wise in the ways of building and debugging software. You should engineer a console tty connection. You will probably need a lot of patience. This is all written vs. revision 11765 of kamikaze, with kernel 2.6.25-10.

==== Get the source ====
Issue the following, to pull down the latest kamikaze and packages images:

{{{
svn checkout https://svn.openwrt.org/openwrt/trunk kamikaze
svn checkout https://svn.openwrt.org/openwrt/packages packages
}}}
==== Link the packages you care about ====
Take a look in the resulting packages directory; you'll see there's a lot of stuff. You probably don't need to build everything in there. Instead I recommend making symlinks for only the packages you need. For example, suppose you're following the UsbAudioHowto, and you want to use madplay to decode streaming MPEGs.

First, check madplay's dependencies:

{{{
% grep DEPENDS packages/sound/madplay/Makefile
  DEPENDS:=+libid3tag +libmad
}}}
So, we'll have to include the libid3tag and libmad packages, as well. Check those packages for dependencies as well:

{{{
% grep DEPENDS packages/libs/libmad/Makefile packages/libs/libid3tag/Makefile
packages/libs/libid3tag/Makefile:  DEPENDS:=+zlib
}}}
zlib is provided by the kamikaze distribution, in kamikaze/package/zlib, so we don't have to mess with that.

Provide symlinks in kamikaze/package, to the packages you want to build:

{{{
cd kamikaze/package
ln -s ../../packages/sound/madplay .
ln -s ../../packages/libs/libmad .
ln -s ../../packages/libs/libid3tag .
}}}
NB - alternatively, you can link every package in the packages distribution into kamikaze with e.g.:

{{{
cd kamikaze/package
ln -s ../../packages/*/* .
}}}
But! This will lead to very long build times.

==== Configure Kamikaze ====
Do the following, to invoke kamikaze's interactive configuration menu system:

{{{
% cd kamikaze; make menuconfig
}}}
Configured as:

 * Target System (Broadcom BCM947xx/953xx [2.6])
 * Target Profile (No WiFi)
 * Select all packages by default
Do not be tempted to mess with wireless, yet. Here be dragons.

Exit and save your configuration.

==== 1st Build of Kamikaze ====
In the kamikaze directory, begin the build with:

{{{
% make
}}}
Hopefully, there are no errors during the build. If there are, a message about re-running with V=99 will be produced, and you'll have to dig yourself out. If you just want to see the compilation proces in ditail, yum also may use V=99.

It'll take maybe an hour and a half to finish? Be sure thet you conectet to the Internet: the compilation proces downloads tarbols of src-codes during 1st building.

==== Patching Kamikaze to Work With the BCM5354 ====
The patching occurs after the 1st build, because all of the patches target build_dir. Sorry.

First, the CFE (Common Firmware Environment, the lowest level firmware in this router) does not interact correctly with the kernel, and a hang during boot occurs. Modify these two files:

{{{
build_dir/linux-brcm47xx/linux-2.6.25.16/arch/mips/kernel/setup.c
build_dir/linux-brcm47xx/linux-2.6.25.16/arch/mips/bcm47xx/prom.c
}}}
as per sbrown's post at http://forum.openwrt.org/viewtopic.php?id=15443&p=2.

Next, the USB2 support needs to be patched. You can review the patch at https://dev.openwrt.org/cgi-bin/trac.fcgi/attachment/ticket/3365/ssb-ehci-25.patch, and you can pull down the patch file via a little, tiny, grey link at the bottom. That patch targets kernel 2.6.25-4, which is probably not your kernel. The following appears to do an okay job of pulling down the patch, and rewriting it for kernel 2.6.25-10:

{{{
% wget -nv -O - http://dev.openwrt.org/cgi-bin/trac.fcgi/raw-attachment/ticket/3365/ssb-ehci-25.patch | sed s:/linux-2.6.25.4/:/linux-2.6.25.16/:g > ssb-ehci-25.patch
}}}
Then apply the patch:

{{{
% patch -p2 < ../ssb-ehci-25.patch
}}}
And configure the kernel:

{{{
% make kernel_menuconfig
}}}
Navigate and select:

 * Device Drivers  --->
 * USB support  --->
 * EHCI support for Broadcom SSB EHCI core
 * OHCI support for Broadcom SSB OHCI core
Exit and save the configuration.

==== 2nd Build of Kamikaze ====
In the kamikaze directory, begin the build with:

{{{
% make
}}}
It should only take a few minutes this time.

==== Download the Image Into Your Router ====
First, make sure you've got a tftp client. I use atftk. You can get the source at http://downloads.openwrt.org/sources/atftp-0.7.tar.gz.

The image is in the bin directory. The commands on the build machine look like:

{{{
% cd bin
% atftp --trace --option "timeout 1" --option "mode octet" --put --local-file openwrt-brcm47xx-squashfs.trx 192.168.1.1
}}}
However! First you've got to wire the router from the build machine to LAN port 1, and bring the router up in diagnostic mode. The latter is accomplished by:

 * make sure the router is powered off
 * hold down the reset button on the back
 * plug in the power
 * don't release the reset button until the power light flashes on and off at 1Hz
Then! Execute the above commands, and you should see a lot of block transfers scrolling by. When those complete wait a while; wiki knowledge suggests 6 minutes, but my WL500GP-V2 completes the flash inside of 30 seconds. Mostly you should have a console connection so you can get positive feedback for all this.

==== Logging In, and Configuring ====
This is not WL500GP-V2 specific, but it isn't immediately clear if you're new to OpenWRT.

After the waiting, power cycle the unit, and wait a while for it to boot. When it responds to pings at 192.168.1.1, it should be telnet-accessible.

Edit /etc/pkg.conf:

{{{
# vi /etc/opkg.conf
}}}
Change the URL to your host machine. You'll have to configure your host machine to run httpd, and serve the bin/packages/mipsel directory you just built. I added the following to /etc/httpd/conf.d/ipkg.conf:

{{{
<VirtualHost 192.168.1.100:80>
  DocumentRoot "/home/biomorph/build/OpenWRT/kamikaze/bin/packages/mipsel"
</VirtualHost>
}}}
Hopefully, you get the idea. When you can update ipkg's database, you'll know you've succeeded:

{{{
# opkg update
}}}
Packages can then be installed as with e.g.:

{{{
# opkg install madplay
}}}
==== Epilogue ====
You got it to work?[[BR]] Nice. Share your joy with the world;[[BR]] buy someone a beer.[[BR]]
