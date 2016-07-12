[[TableOfContents]]



!OpenWrt is free software, provided AS-IS under the terms of the GNU General Public License. Please understand that you are expected to have knowledge about GNU/Linux and basic networking concepts before you install !OpenWrt on your router, however, for all intended purposes of this document it is not required. :) Support may be provided on a voluntary basis by developers and fellow users, but support is not guaranteed. 

The latest version of !OpenWrt is also know as White Russian, however, !OpenWrt will be used instead of White Russian for simplicity.

/!\ '''WARNING  LOADING AN UNOFFICIAL FIRMWARE WILL VOID YOUR WARRANTY''' /!\

= Introduction =
This guide is intended for beginners to Linux and/or !OpenWrt.  This guide is dedicated to the installation of !OpenWrt on the !LinkSys WRT54GL router and the experiences gained by the installation.  
Installation of !OpenWrt on the WRT54GL is possible, either through the Firmware upgrade web interface on the !LinkSys router or through tftp on Windows or Linux.  The easiest method by far is installation through the web interface, mainly because of the small window of opportunity to connect and transfer !OpenWrt using tftp.  The problems of using tftp for installation on the  Wrt54GL and how to overcome those problems are discussed here as well.  

Even though this document focuses on the WRT54GL it is also relevant to the installation of !OpenWrt in general.  So if you are new to Linux and !OpenWrt, you will save time reading this document, especially if you are interested in compiling/building your own !OpenWrt source for installation and are interested in using tftp for installing.

= LinkSys Wrt54GL Hardware =
The WRT54GL !LinkSys router was used for this particular installation.  The specs of this router are as follows which has been taken from the TableOfHardware page.
||'''Model''' ||'''Version''' ||'''Platform & Frequency''' ||'''Flash''' ||'''RAM''' ||'''Wireless NIC''' ||'''Switch''' ||'''boot_wait''' ||'''Serial''' ||'''JTAG''' ||'''USB''' ||'''Status''' ||
|| [http://www.linksys.com/servlet/Satellite?c=L_Product_C2&childpagename=US/Layout&cid=1133202177241&pagename=Linksys/Common/VisitorWrapper WRT54GL] || ||[http://www.broadcom.com/products/Wireless-LAN/802.11-Wireless-LAN-Solutions/BCM5352E Broadcom 5352] @ 200MHz ||4MB ||16MB ||Broadcom (integrated) ||in CPU ||off ||Yes ||Yes ||No ||[:OpenWrtDocs/Hardware/Linksys/WRT54GL:Supported] ||

The Firmware version as of the latest WRT54GL models as of April 2006 is v4.30.0.  Do not be concerned with the which version you have.  You may want to take note of which version you have in case you would like to re-install it (although, even that doesn't matter as you can just go to the !LinkSys website to download the latest and greatest), however, unlike what some people say about rolling back versions to take advantage of the infamous "ping exploit"... well, that's just not needed.  Any version should work fine.

For any of those people interested in connecting serial ports to the WRT54GL.  Single and dual serial boards are available.  Two serial connections can be created using a dual serial board.

= Installing OpenWrt =
We are installing !OpenWrt on the !LinkSys WRT54GL router. 

== Select your Hardware ==
The first thing you want to do is make sure that your router hardware is supported, since we are using the WRT54GL linkSys router we are fine, otherwise confirm your hardware on the TableOfHardware page.

== Select your Firmware ==
The next step is to locate the variation of !OpenWrt you want to install.  It comes in three variations located in three differen directories.  The only difference between them is that each has a slightly different set of packages installed.

 1. micro/ - contains the least amount of packages required for a functional system.  This one is only recommended for those experience with !OpenWrt and Linux as it does not contain a web interface to the !OpenWrt firmware.
 2. bin/ - contains a decent amount of packages (referred to as a Standard image) needed for a functional system plus it contains a web interface and pppoe.  This one is recommended and is considered the default.
 3. pptp/ - contains almost the exact set of packages as the previous Standard image except it includes pptp and not pppoe.  It also has the web interface.

If you are new to !OpenWrt then simply choose the !OpenWrt found in the bin directory.   The latest !OpenWrt files can be found at http://downloads.openwrt.org/whiterussian/newest/

Before you download the files, continue to read the next two sections as it explains which file to select.

== Select your .bin/.trx file ==
In that directory you will notice two different types of files. "trx" and "bin" files, the bin files simply repackage the trx in the vendor's default firmware format and are only used when the trx files can't be used directly.  That may be a little confusing for some people however, since we are using the WRT54GL you should use:

openwrt-wrt54g-<type>.bin  (<type> is explained below)

For those people who aren't using a WRT54GL !LinkSys router refer to section 2.1. TRX vs. BIN on the !OpenWrt Installing page http://wiki.openwrt.org/InstallingWrt54gl#preview, to select the image file you need to download.

== Select SquashFS or JFFS2 ==
You will notice that in that same directory, where we have <type> you will find "SquashFS" and "JFFS2"

 * SquashFS - SquashFS files include a small compressed filesystem within the firmware itself. The disadvantage is that Squashfs is a readonly filesystem, to save changes and make the filesystem appear writable a separate JFFS2 partition has to be used; the advantage is that Squashfs takes up slightly more space than JFFS2, and you'll always have the original files on the readonly filesystem which can be used as a boot device for recovery.
 * JFFS2 - JFFS2 make the entire filesystem JFFS2. The disadvantage is that this takes slightly more space; the advantage is that changes to included files nolonger leaves behind an old copy on the readonly filesystem.

If you are new to Linux and OpenWrt simply choose SquashFS.

Two warnings:
/!\ '''The JFFS2 firmware uses an extra setup step which requires an ADDITIONAL REBOOT before the filesystem can be used.''' /!\

/!\ '''WARNING !OpenWrt White Russian prior rc5 has no failsafe mode for JFFS2 firmware images.''' /!\

== Download !OpenWrt Firmware Image ==
At this point you have read the sections above, and since we are using the !LinkSys WRT54GL you now know to choose the openwrt-wrt54g-squashfs.bin , although you can also choose openwrt-wrt54g-jffs2.bin if you don't mind rebooting after the install and the fact that is uses a little more space.

You can choose to download the !OpenWrt firmware image onto a Windows machine or Linux.  It doesn't matter.

Now, download the latest !OpenWrt file found at http://downloads.openwrt.org/whiterussian/newest/

After downloading the !OpenWrt firmware image it is good practice to make sure that the file is not corrupt. This can be verified by comparing the md5sum from your downloaded image with the md5sum listed in the [http://downloads.openwrt.org/whiterussian/newest/bin/md5sums md5sums] file found in the download directory. For win32 platforms use [http://www.pc-tools.net/win32/ md5sums.exe] for GNU/Linux systems use the {{{md5sum}}} command.  After running the command with the !OpenWrt firmware image you just downloaded, compare the results to the corresponding file found on this page [http://downloads.openwrt.org/whiterussian/newest/bin/md5sums md5sums]

== WRT54GL Connect ==
Be sure to have your WRT54GL router powered up.  Plug the power adaptor into a standard outlet and plug the other end into your router.  You should see lights on the front of the router.  Now you need to your computer to your router.  Your connection may vary based on your network configuration.  To connect your computer directly to the router run one end of an ethernet cable into your computer's network card and the other end directly into one of the four numbered ports on the back of your router (not the internet/LAN port).  If you are on a network and are plugged into a hub you can plug one end of the ethernet cable into a numbered port on the hub and the other end into a numbered port on the router (you must unplug the hub's uplink button, which will disconnect it from the internet).  In either case, if you have a dedicated IP you need to change your IP address so that you can access the router on the same subnet.  For example, if your IP address is 192.168.170.55 change it to 192.168.1.55 and you should be able to access your router.

To confirm your connection you can try pinging your router (ping 192.168.1.1) or using either Windows or Linux, simply open up your favorite Web Browser and access page 192.168.1.1.  If your !LinkSys WRT54GL router web interface appears you are connected!  If not, you need to solve this problem before moving forward. 

== Installation ==
So you have the !OpenWrt firmware image downloaded and have confirmed it isn't corrupt.  As well, you have confirmed that your computer can communicate with the WRT54GL router.

You have two choices for installation, both methods work on both Linux and Windows.  You can can use the LinkSys Web Interface for installing !OpenWrt or you can use tftp to install !OpenWrt.

If you are not compiling your own !OpenWrt source code, simply install !OpenWrt using the Routers Web Interface (this is simple... brief instructions below).  In fact, even if you plan on installing your own self compiled !OpenWrt source code it is easier to install an official version of !OpenWrt first using the Router's Web Interface.  Why you ask?  It's all about boot_wait.

By default, boot_wait is "off" on the WRT54GL routers, in fact, most routers have boot_wait "off" by default.  Turning boot_wait "on" simply increases the time it takes to boot.  Why is this relevant you may ask?  Well, try using tftp to install !OpenWrt and you'll find out.  Some people claim that atftp for linux is quicker than tftp for windows, this is not necessarily true although the 'a' in atftp does stand for "advanced".  If you try to install !OpenWrt using tftp on windows, using tftp on Linux or atftp on Linux you get the same error.

{{{
"error received from server <Invalid Password!!>"
}}}

This happens because tftp client cannot access the router's server.  Why? Because there is a small window of opportunity to connect and install !OpenWrt using tftp and as fast as you try to be it is near impossible to catch without knowing the trick.  Turning Boot_wait "on" increases that window of opportunity and makes it easier to catch and install !OpenWrt using ftp, however, turning Boot_wait "on" is a task in itself and varies across routers.  Apparently, on some routers you can install older firmware that enables a ping exploit where commands can be typed directly into the routers Web Interface to turn Boot_wait "on" or "off".  This does not work with WRT54GL so do not try to roll back the firmware, it is not recommended.  In fact, turning Boot_wait "on" for installing !OpenWrt on the WRT54GL using tftp is not necessary (but it helps).  Apparently Boot_wait can be turned on through a serial console and the serial port, however, I have not yet attempted the task, for more information read page OpenWrtDocs/BootWait.

So, it is recommended that you install an official version of !OpenWrt first using the Router's Web Interface before using tftp to install your own self compiled version.  This is because once you have installed !OpenWrt you can access its Web Interface and turn Boot_wait "on".  Then you can use tftp and have a much easier time installing !OpenWrt.  This is one of the easiest ways to turn on the Boot_wait option.  Hopefully, it saves you hours of searching the forums.

Just so that you know. You do not need the Boot_wait option on to successfully install !OpenWrt using tftp.  It does make it easier but it's not necessary.  The trick is to press the reset button and timing.  Run the ftp client, power up the WRT54GL router and hit the reset button.  If that doesn't work the first time, try again, but it does work.

=== Router Web Interface Installation ===
To install !Open Wrt using the router's web interface simply access the web interface page at 192.168.1.1, go to system - > administration - > firmware upgrade.  Locate the !OpenWrt Firmware Image file and that's it.  Be sure that the power supply is stable and not disconnected during transfer.  After your installation depending on the type of !OpenWrt you chose you may need to restart you router.  Many people have reported inconsistent results.  RussNelson notes that v4.30.0 gave the "Upgrade are failed!" error, but upgrading to Linksys.com's v4.30.5 reflashed OpenWRT just fine.

=== tftp Installation ===
tftp is mainly recommended for those looking to install their own self compiled images of !OpenWrt, because it can also be used to recover from a problem and allow you to put on another Firmware Image, whether it is !OpenWrt or the original from !LinkSys.  This is only relevant in the event that something happens to the router, the install was interrupted or the code causes the router to crash.  You can then use tftp to reflash the router with another firmware.  If something happens to you router the Web Interface may not be available to you.  This is where tftp shines!

To install !OpenWrt using atftp on Linux type the command:

atftp --trace --option "timeout 1" --option "mode octet" --put --local-file openwrt-xxx-x.x-xxx.bin 192.168.1.1

Next power up your router, and hit your reset button.  If it doesn't work keep trying.  If you have the "Boot_wait" option "on" you can probably turn the router on first, then run the atftp client and skip hitting the reset button.

For more information on installing !OpenWrt using tftp visit OpenWrtViaTftp

= Other Pages By dRax =

UpdatingWrt54gl
