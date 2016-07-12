#acl Known:read,write All:read
##
## This page contains random bits of information about the origin of openwrt
##
## If someone can come up with a better reason to run openwrt, please edit that section
##
## This page is reserved for the HISTORY and DEVELOPMENT of OpenWrt
##


[:OpenWrtDocs]
[[TableOfContents]]


= About OpenWrt =

With the release of the Linux sources for the Linksys WRT54G/GS series of routers came
a number of modified firmwares to extend functionality in various ways. Each firmware was
99% stock sources and 1% added functionality, and each firmware attempted to cater to a
certain market segment with the functionality that they provided. The downsides were twofold:
 1. It was often difficult to find a firmware with the combination of functionality desired (leading to forks and yet more custom firmwares)
 1. All the firmwares were based on the original Linksys sources which were far behind mainstream GNU/Linux development.

!OpenWrt takes a different route, instead of starting out with the Linksys sources, the
development started with a clean slate. Piece by piece software was added to bring the
functionality back to that of the stock firmware, using the most recent versions available.
What makes !OpenWrt really unique though is the fact it employs a writable filesystem so the
firmware is no longer a static compilation of software but can instead be dynamically adjusted
to fit the particular needs of the situation. In short, the device is turned into a mini linux
PC with !OpenWrt acting as the distribution, complete with almost all traditional linux commands
and a package management system for easily loading on extra software and features.


= Why should I run OpenWrt? =

Because GNU/Linux gives us the power to do what we need with cheap hardware while avoiding proprietary,
rigid software. !OpenWrt isn't for the faint of heart, but if you honestly need a barebones GNU/Linux
and are prepared to do some work !OpenWrt is the fastest Linux based firmware a lot of 
wireless lan routers.
At the moment the distribution contains more than 100 software packages. Furthermore the !OpenWrt
community provide more add-on packages. For developers the project provides a build system, which may
be used to create modified firmware from source. Porting of new software packages is simplified with
the use of the SDK. 


= OpenWrt Version History =

The project started in January 2004. The first !OpenWrt versions were based on 
Linksys GPL sources for WRT54G and a buildroot from the uclibc project.
This version was widely known as !OpenWrt "stable release" and was widely in use. There are still many
!OpenWrt applications, like the Freifunk-Firmware or Sip@Home, which are based on this version.

In the beginning of 2005 some new developers have joined the team. After some months of
closed development the team decided to publish the first "experimental" versions of !OpenWrt. The
experimental versions use a heavily customized buildsystem based on buildroot2 from the uclibc project.
!OpenWrt uses official GNU/Linux kernel sources and only add patches for the system on chip
and drivers for the network interfaces. The developer team try to reimplement most of the proprietary
code inside the GPL tarballs of the different vendors. There are free tools for writing new firmware
images directly into the flash (mtd), for configuring the wireless lan chip (wlcompat/wificonf) and to
program the VLAN capable switch via the proc filesystem. The codename of the first !OpenWrt release is "White Russian"
a popular cocktail. !OpenWrt 1.0 is released if it is stable enough for most of our users. White Russian is
currently in "Release Candidate" status, with numbers like "rc3" and "rc4".

The development of the next release is taken place in our subversion repository. It will contain support for many
more embedded boards (Texas Instruments AR7 (MIPS), Soekris (x86), Aruba (MIPS), Routerboard (MIPS), ...). Its codename
is Kamikaze. 
