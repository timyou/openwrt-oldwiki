This page is '''NOT''' maintained by the OpenWrt developers. Furthermore, it is actively under development. It is also used as a sandbox for new documentation that may eventually be moved to the primary OpenWrt documentation.

== X-Wrt ==

[http://www.bitsum.com/xwrt.htm X-Wrt] is a project to enhance the end user experience of OpenWrt. It is currently under active development. X-Wrt is developed by a different group than is the base OpenWrt firmware and is therefore not affiliated with OpenWrt, nor is it supported by OpenWrt. Since many users may be interested what X-Wrt has to offer, some basic information about it is included here.

'''X-Wrt Links:'''

 * [http://www.bitsum.com/xwrt.asp X-Wrt General Information] and Webif^2 Install/Auto-Install
 * [http://developer.berlios.de/projects/xwrt/ Project Hosting (repository, mailing lists, etc..)]
 * [http://www.bitsum.com/smf/index.php?board=17.0 User Forums]

=== X-Wrt Packages ===

Packages documented here are only those in the X-Wrt repository that are not included in the OpenWrt White Russian repository, or have been updated.

The X-Wrt White Russian repository is here: ftp://ftp.berlios.de/pub/xwrt/packages/

==== webif^2: Enhanced HTTP management console ====

X-Wrt's most popular package should be mentioned first. '''webif^2^''' is an enhanced webif (HTTP based management console). It offers a large number of new features and is constantly  being improved. Some of the more popular additions are the real-time traffic and CPU graphs, a switchable color theme, and a number of new webif pages for both configuration and status reporting.

 * [http://www.bitsum.com/smf/index.php?topic=267.0 Screenshots] (not necessarily up-to-date with latest build)

To install the latest daily build of webif^2^:

{{{
ipkg install http://ftp.berlios.de/pub/xwrt/webif_latest.ipk
}}}

==== Busybox 1.2.1 ====

BusyBox 1.00 has been included in White Russian RC5 and RC6. There have been many releases of Busybox since v1.00, with the current release at 1.2.1. Kamikaze uses the latest 1.2.1. For White Russian users who desire to use a newer Busybox, we've migrated this package to White Russian.

busybox 1.2.1 package: ftp://ftp.berlios.de/pub/xwrt/packages/busybox_1.2.1-5_mipsel.ipk  

==== UPNP: Linksys's IGD ====

'''WARNING:''' Not well tested at all.

You can install UPNP by installing linux-igd (and libupnp) from the X-Wrt repository.

linux-igd package: ftp://ftp.berlios.de/pub/xwrt/packages/libupnp_1.2.1a_mipsel.ipk

==== Wireless tools v29 pre 10 ====

This is simply a newer package than is available at the time of this writing in either White Russian or Kamikaze repositories.

wireless-tools: ftp://ftp.berlios.de/pub/xwrt/packages/wireless-tools_29.pre10-1_mipsel.ipk

=== Webif Developer Documentation ===

''This is very much a work in progress --- some inaccuracies may be present in the first drafts.''

The webif system is a combination of shell, awk, html, and javascript (a little). 

The "Programmers Guide to Webif^2" is available @ ProgrammersGuideToWebif

Use the existing webif pages as guides and start playing around until you understand how the system works. It's not complex at all, but is a little different than what many may be used to - especially web developers.

==== What is a webif page? ====

A webif page is essentially an HTML page with embedded shell script. Core functions, like the page header/footer and settings forms are implemented by an AWK back-end. For example, see /usr/lib/webif/form.awk, which implements 'display_form' calls in the webif pages.

The 'Save' button on a page causes a submit event which the page can handle as it loads. When FORM_submit is not-empty, the page saves itself through a series of calls to 'save_setting GROUP SETTING' or alternate functions. Conversly, a page should always load its settings via 'load_settings GROUP' to make sure any saved but not yet applied changes are indicated on the page.

==== Using your router for real-time development ====

To use your router as an active development box, do the following:

  * Mount an NFS or SAMBA share somewhere onto your router. (i.e. to /mnt/myshare).
  * Copy /www and /usr/lib/webif folders recursively to your network share. (i.e. cp -r /www /mnt/myshare/).
  * Remove old /www and /usr/lib/webif folders (i.e. rm -rf /www).
  * Symlink the www folder on your network share to the /www folder on your router (i.e. ln -s /mnt/myshare/www /www).
  * Symlink the usr/lib/webif folder on your network share to the /usr/lib/webif folder on your router (i.e. ln -s /mnt/myshare/usr/lib/webif /usr/lib/webif).

Afterwards, restart the httpd or reboot your router. 

This change will persist, so from now on you can work on webif pages by simply editing them on the network share. Changes are shown in real-time as you access the webif on the router.

==== NG-style UCI config vs. nvram ====

OpenWrt is migrating away from nvram, with it completely removed from buildroot-ng. The webif is doing the same. There are new config functions able to load and store files in the UCI config file format.

===== Using NVRAM config functions =====

These functions load and store nvram variables (untyped tuples). An example invocation of saving an nvram varaible is: 'save_setting GROUPNAME VARIABLE=VALUE'.

===== Using UCI config functions =====

See /usr/lib/webif/functions.sh , the '_ex' functions for further information.

==== CSS ====

Webif^2^ makes extensive use of CSS. In fact, everything style related should be defined in the CSS. Pages that define their own styles are considered non-conformant and should be changed. 

The CSS is spread out over a few files in /www. The '/www/webif.css' file contains the core CSS style. Over-rides for specific browsers, like Internet Explorer, may also exist in this folder under different names. Color themes are named after their representative colors, of which there are currently 6.

==== Localization ====

Localization is accomplished by a pre-processor which replaces all '@TR<<symbolname>>' variables with the corresponding symbol value in the currently active language symbol file. If no symbol is found, the symbol name itself is used for the text. Therefore, simply using many @TR<<text>> macros for strings is all that initially needs to be done to make a webif page ready for localization. Translators can later add the symbols to the localized symbol file.

The localized symbol files are, as of White Russian RC6, stored in seperate packages instead of all being included in the base webif set.

=== Firmware Image Technical Details ===

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


==== Linksys WRT54G(S) Images ====

These images are simple TRX images with a small proprietary header pre-pended.

==== ASUS images ====

On a variety of devices, even non-Broadcom devices, ASUS uses a TRX-style image with an appended proprietary version information block.
 

=== Building OpenWrt White Russian Sources ===

Need a linux OS.

Package pre-requisites: gcc, g++, binutils, patch, bzip2, flex, bison, make, gettext, unzip, libz-dev or zlib1g-dev, and libc headers.

Run 'make' to build. Run 'make menuconfig' to configure.

See general OpenWrt documentation.
