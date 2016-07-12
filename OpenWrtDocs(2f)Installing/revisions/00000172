#acl Known:read,write All:read
##
## Note: these pages document the firmware itself, not packages
##       questions/comments should be posted to the forum
##
OpenWrtDocs [[TableOfContents]]

= Introduction =

!OpenWrt is free software, provided AS-IS under the terms of the GNU General Public License. We are expect that you have knowledge about GNU/Linux and basic networking concepts, before you install !OpenWrt on your router. Support may be provided on a voluntary basis by developers and fellow users, but support is not guaranteed. 

/!\ '''WARNING  LOADING AN UNOFFICIAL FIRMWARE WILL VOID YOUR WARRANTY''' /!\


= Supported hardware =
See TableOfHardware.

= Obtaining the firmware =

You can get the latest OpenWrt White Russian at: http://downloads.openwrt.org/whiterussian/newest/

Please test our release candidates and report back any problems, so that we can actually release OpenWrt 1.0. 

There are different pre-compiled firmware images for every supported router model in these folders:

||'''Folder''' ||'''Description''' ||'''Package list''' ||
||bin=default ||standard image with pppoe and webif||base-files, base-files-brcm, bridge, busybox, dnsmasq, dropbear, haserl, ipkg, iptables, iwlib, kmod-switch, kmod-brcm-wl, kmod-diag, kmod-ppp, kmod-pppoe, kmod-wlcompat, mtd, nvram, ppp, ppp-mod-pppoe, uclibc, webif, wificonf, wireless-tools||
||micro ||the minimal set of packages no webif||base-files, base-files-brcm, bridge, busybox, dnsmasq, dropbear, ipkg-sh, iptables, iwlib, kmod-switch, kmod-brcm-wl, kmod-diag, kmod-wlcompat, mtd, nvram, uclibc, wificonf||
||pptp ||standard image with pptp and webif ||base-files, base-files-brcm, bridge, busybox, dnsmasq, dropbear, haserl, ipkg, iptables, iwlib, kmod-switch, kmod-brcm-wl, kmod-diag, kmod-ppp, kmod-gre, kmod-wlcompat, mtd, nvram, ppp, pptp, uclibc, webif, wificonf, wireless-tools||

You can choose between two different types of firmware images, squashfs or JFFS2 root filesystem. Squashfs does higher compression, but is read-only. If you choose this image type, you can not update any base packages without reflashing or loosing of a lot of space. The rest of the flash will be used for a writable JFFS2 filesystem. JFFS2 does not compress as well as squashfs, but you have 
a complete writable root filesystem. It is your choice!  

. /!\ '''WARNING  !OpenWrt White Russian prior rc5 has no failsafe mode for JFFS2 firmware images.''' /!\

Choose the right firmware image for your router model and installation method, xxxx stands for the root filesystem type.

Installation via Webupgrade of the original firmware:
||'''Filename'''||'''Models'''||
||openwrt-brcm-2.4-xxxx-4MB.trx||Asus WL500g, Asus WL500gx, Buffalo !AirStation WBR2-G54S||
||openwrt-wrt54g-xxxx.bin||Linksys WRT54G (v1.0,v1.1,v2.0,v2.2,v3,v4)||
||openwrt-wrt54gs-xxxx.bin||Linksys WRT54GS (v1.0, v1.1, v2, v3)||
||openwrt-wrt54gs_v4-xxxx.bin||Linksys WRT54GS v4||
||openwrt-wrtsl54gs-xxxx.bin||Linksys WRTSL54GS||
||openwrt-wa840g-xxxx.bin||Motorola WA840g||
||openwrt-we800g-xxxx.bin||Motorola WE800g||
||openwrt-wr850g-xxxx.bin||Motorola WR850g||

Installation via !OpenWrt administrative console or mtd command line tool:
||'''Filename'''||'''Models'''||
||openwrt-brcm-2.4-jffs2-4MB.trx||mostly all models with 4MB flash size *||
||openwrt-brcm-2.4-jffs2-8MB.trx||mostly all models with 8MB flash size *||
||openwrt-brcm-2.4-squashfs.trx||all models||

* Who remembers which model has a 4 MB flash with 128 Kbyte erasesize?

After downloading the firmware image you should make sure that the file is not corrupt. This can be verified by comparing the md5sum from your downloaded image with the md5sum listed in the [http://downloads.openwrt.org/whiterussian/newest/default/md5sums md5sums] file found in the download directory. For win32 platforms use [http://www.pc-tools.net/win32/ md5sums.exe] for GNU/Linux systems use the {{{md5sum}}} command.

= Installing OpenWrt =

To install OpenWrt on a supported device (see TableOfHardware), download the correct firmware for your device, verify the md5sum and 
then use the webupgrade of the preinstalled firmware. Be sure that your power supply is stable and do not disconnect it while flashing OpenWrt to your router. After the installation was successful, your router will be booting into your new shiny linux system. 

If you are unhappy with OpenWrt, you can always reinstall your original firmware. Please be sure you have it downloaded and saved on your PC.

If you are extremely cautious or try to install a self compiled or modified version of OpenWrt White Russian, please consider
to use the OpenWrtViaTftp installation method. For some of the hardware models we support, this requires special requirements.
To avoid potentially serious damage to your router caused by an unbootable firmware you always should read the documentation for your specific router model. (see OpenWrtHardwareOverview)

/!\ '''We strongly suggest you also read ["OpenWrtDocs/Troubleshooting"] before installing'''

= Using OpenWrt =
See ["OpenWrtDocs/Using"].

= Troubleshooting =
If you have any trouble flashing to !OpenWrt please refer to ["OpenWrtDocs/Troubleshooting"].
