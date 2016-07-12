#acl Known:read,write All:read
##
## This page contains random bits of information about the origin of openwrt
##
## If someone can come up with a better reason to run openwrt, please edit that section
##

[:OpenWrtDocs]
[[TableOfContents]]
= About OpenWrt =

With the release of the Linux sources for the Linksys WRT54G/GS series of routers came a number of modified firmwares to extend functionality in various ways. Each firmware was 99% stock sources and 1% added functionality, and each firmware attempted to cater to a certain market segment with the functionality that they provided. The downsides were twofold, one - it was often difficult to find a firmware with the combination of functionality desired (leading to forks and yet more custom firmwares) and two - all the firmwares were based on the original Linksys sources which were far behind mainstream Linux development.

OpenWrt takes a different route, instead of starting out with the Linksys sources, the development started with a clean slate. Piece by piece software was added to bring the functionality back to that of the stock firmware, using the most recent versions available. What makes OpenWrt really unique though is the fact it employs a writable filesystem so the firmware is nolonger a static compilation of software but can instead be dynamically adjusted to fit the particular needs of the situation. In short, the device is turned into a mini linux PC with OpenWrt acting as the distribution, complete with almost all traditional linux commands and a package management system for easily loading on extra software and features. 

= Why should I run OpenWrt? =

Because Linux gives us the power to do what we need with cheap hardware while avoiding proprietary, rigid software. OpenWrt isn't for the faint of heart, but if you honestly need a barebones Linux and are prepared to do some work OpenWrt is the fastest Linux based firmware for the Linksys WRT's. 
At the moment the distribution contains more than 100 software packages. Furthermore the OpenWrt community provide more add-on packages. For developers the project provides 
a build system, which may be used to create modified firmware from source. Porting of new software packages is simplified with the use of the SDK.

If you aren't up to the task or simply don't need a real, full blooded Linux, here are some alternatives:

[http://www.seattlewireless.net/index.cgi/LinksysWrt54g#head-c8ffcfc4b9ddb0bd95c3d4e4b1faf349738899f1 Seattle Wireless's Customized Firmware Listing]

= OpenWrt Version History =

The project started in January 2004. The first OpenWrt versions were based on Linksys original GPL sources for WRT54g and a buildroot from the uclibc project. 
This version is known as OpenWrt "stable" and was widely in use. There are still many OpenWrt applications, like the Freifunk-Firmware or Sip@Home, which are based on this version.

In the beginning of 2005 some new developers has joined the small developer team. After some month of closed development the team decided to publish the first "experimental" versions of OpenWrt. The experimental version use a heavily customized buildsystem based on buildroot2 from the uclibc project. OpenWrt uses official linux kernel sources (2.4.30) and only add patches for the system on chip and drivers for the network interfaces. The developer team try to reimplement most of the proprietary code inside the GPL tarballs of the different vendors. There are free tools for writing new firmware images directly into the flash (mtd), for configuring the wireless lan chip (wlcompat/wificonf) and to program the VLAN capable switch (robocfg). The codename of the first OpenWrt release is "White Russian" a popular cocktail. OpenWrt 1.0 is planned for the end of 2005.  
