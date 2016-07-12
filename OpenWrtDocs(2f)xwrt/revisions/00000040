{{{
This page is NOT maintained by the OpenWrt developers.
Furthermore, it is actively under development.
It is also used as a sandbox for new documentation that may eventually be moved to the primary OpenWrt documentation.
}}}
 attachment:webif.jpg

'''X-Wrt'''

[http://www.bitsum.com/xwrt.htm X-Wrt] is a project to enhance the end user experience of OpenWrt. It is currently under active development. X-Wrt is developed by a different group than is the base OpenWrt firmware and is therefore not affiliated with OpenWrt, nor is it supported by OpenWrt. Since many users may be interested what X-Wrt has to offer, some basic information about it is included here.

X-Wrt Links

 * [http://www.bitsum.com/xwrt.asp X-Wrt General Information] and Webif^2 Install/Auto-Install
 * [http://developer.berlios.de/projects/xwrt/ Project Hosting (repository, mailing lists, etc..)]
 * [http://www.bitsum.com/smf/index.php?board=17.0 User Forums]
-------
[[TableOfContents(3)]]

= X-Wrt Packages =
Packages documented here are only those in the X-Wrt repository that are not included in the OpenWrt White Russian repository, or have been updated.

The X-Wrt White Russian repository is here: ftp://ftp.berlios.de/pub/xwrt/packages/

== webif^2: Enhanced HTTP management console ==
X-Wrt's most popular package should be mentioned first. '''webif^2^''' is an enhanced webif (HTTP based management console).

It offers a large number of new features and is constantly being improved.

Some of the more popular additions are the real-time traffic and CPU graphs, a switchable color theme, and a number of new webif pages for both configuration and status reporting.

attachment:Screenshot-1.png

( * [http://www.bitsum.com/smf/index.php?topic=267.0 Screenshots] (not necessarily up-to-date with latest build)    )

=== Install the latest daily ===

{{{
ipkg install http://ftp.berlios.de/pub/xwrt/webif_latest.ipk
}}}
=== Webif Developer Documentation ===
''This is very much a work in progress --- some inaccuracies may be present in the first drafts.''

The webif system is a combination of shell, awk, html, and javascript (a little).

The "Programmers Guide to Webif^2" is available @ ProgrammersGuideToWebif. If there are inaccuracies here, please participate and share your knowledge

Apart from the Programmers Guide, use the existing webif pages as guides and start playing around until you understand how the system works. It's not complex at all, but is a little different than what many may be used to - especially web developers.

== Busybox 1.2.1 ==
BusyBox 1.00 has been included in White Russian RC5 and RC6. There have been many releases of Busybox since v1.00, with the current release at 1.2.1. Kamikaze uses the latest 1.2.1. For White Russian users who desire to use a newer Busybox, we've migrated this package to White Russian.

busybox 1.2.1 package: ftp://ftp.berlios.de/pub/xwrt/packages/busybox_1.2.1-5_mipsel.ipk

== UPNP: Linksys's IGD ==
'''WARNING:''' Not well tested at all.

You can install UPNP by installing linux-igd (and libupnp) from the X-Wrt repository.

linux-igd package: ftp://ftp.berlios.de/pub/xwrt/packages/libupnp_1.2.1a_mipsel.ipk

== Wireless tools v29 pre 10 ==
This is simply a newer package than is available at the time of this writing in either White Russian or Kamikaze repositories.

wireless-tools: ftp://ftp.berlios.de/pub/xwrt/packages/wireless-tools_29.pre10-1_mipsel.ipk

= Building OpenWrt White Russian Sources =
??[[FootNote(Is this really needed as it can be found elsewhere)]]

Need a linux OS.

Package pre-requisites: gcc, g++, binutils, patch, bzip2, flex, bison, make, gettext, unzip, libz-dev or zlib1g-dev, and libc headers.

Run 'make' to build. Run 'make menuconfig' to configure.

See general OpenWrt documentation.

= Firmware Image Technical Details =
???[[FootNote(Maybe should be deleted as well ...)]]
...(TODO: writing up from memory, check details later)...

Different devices require different firmware images, but most Broadcom baed devices compatible with OpenWrt White Russian use TRX images, or derivatives of TRX images. Often times vendors simply prepend or append a proprietary header onto a stock TRX image. Vanilla TRX images are usually named with the extension '.trx', or with 'generic' in the filename.

A TRX image contains up to 4 segments that can be used for any purpose. A fixed-size (4*DWORD) array of segment offsets is included in the header. OpenWrt uses the segments as shown below:

 * Segment 1: Kernel Decompression Stub/Loader
 * Segment 2: Compressed Kernel
 * Segment 3: ROOTFS (Squashfs or JFFS2)
 * Segment 4: unused
The TRX header has a signature of 'HDR0', so you can easily identify this header when you see it. Tools to manipulate TRX images are below. All are maintained in the Firmware Modification Kit, a project created by one of the X-Wrt developers but distinct from X-Wrt.

 * '''''ADDVER''''' - (unnecessary) Tool to append an ASUS version info header to a TRX image. Unnecessary with ASUSTRX.
 * '''''ADDPATTERN''''' - Tool to prepend a Linksys WRT54G(S) style header on to a TRX image.
 * '''''ASUSTRX''''' - Tool to build TRX images and *optionally* TRX images with appended ASUS version blocks.
 * '''''TRX''''' - (unnecessary) Tool to build vanilla TRX images. ASUSTRX will do the job of this tool since it produces vanilla images if no version information is provided.
 * '''''UNTRX''''' - Tool to extract TRX images to their component parts.
== Linksys WRT54G(S) Images ==
These images are simple TRX images with a small proprietary header pre-pended.

== ASUS images ==
On a variety of devices, even non-Broadcom devices, ASUS uses a TRX-style image with an appended proprietary version information block.
= Foot Notes =
