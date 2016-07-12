#acl Known:read,write All:read
##
## Note: these pages document the firmware itself, not packages
##       questions/comments should be posted to the forum
##
OpenWrtDocs [[TableOfContents]]

!OpenWrt is free software, provided AS-IS under the terms of the GNU General Public License. We expect that you are knowledgeable about GNU/Linux and basic networking concepts, before you install !OpenWrt on your router. Support may be provided on a voluntary basis by developers and fellow users, but support is not guaranteed.

/!\ '''WARNING LOADING AN UNOFFICIAL FIRMWARE WILL VOID YOUR WARRANTY''' /!\

'''If you have WRT54G v1 and can't get tftp to work, try uploading the original firmware, then from the webpage on that (192.168.1.1) upload the OpenWrt firmware. '''

= Supported hardware =
See TableOfHardware.

= Choosing the right firmware =
You can get the latest !OpenWrt White Russian firmware images at: http://downloads.openwrt.org/whiterussian/newest/

Please test our release candidates and [https://dev.openwrt.org/newticket report] any problems, so that we can actually release a stable !OpenWrt 1.0.

White Russian ships in several variations, each with a slightly different set of packages installed by default. You're still free to add whatever packages you want, but this will save you from manually installing some common packages immediately after reflashing.

 . micro/
  . The least amount of packages required for a functional system; there isn't even a web interface.
 bin/ (aka default)
  . Standard image (web interface, pppoe)
 pptp/
  . Standard image (web interface, pptp)
||'''Folder''' ||'''Package list''' ||
||micro ||base-files, base-files-brcm, bridge, busybox, dnsmasq, dropbear, ipkg-sh, iptables, iwlib, kmod-switch, kmod-brcm-wl, kmod-diag, kmod-wlcompat, mtd, nvram, uclibc, wificonf ||
||bin=default ||base-files, base-files-brcm, bridge, busybox, dnsmasq, dropbear, haserl, ipkg, iptables, iwlib, kmod-switch, kmod-brcm-wl, kmod-diag, kmod-ppp, kmod-pppoe, kmod-wlcompat, mtd, nvram, ppp, ppp-mod-pppoe, uclibc, webif, wificonf, wireless-tools ||
||pptp ||base-files, base-files-brcm, bridge, busybox, dnsmasq, dropbear, haserl, ipkg, iptables, iwlib, kmod-switch, kmod-brcm-wl, kmod-diag, kmod-ppp, kmod-gre, kmod-wlcompat, mtd, nvram, ppp, pptp, uclibc, webif, wificonf, wireless-tools ||
== TRX vs. BIN ==
That explains the directories, now what the hell are the files? They are [wiki:WikiPedia:Disk_image disk image]s. There's two types of files, the "trx" files and the "bin" files; the bin files simply repackage the trx in the vendor's default firmware format and are only used when the trx file can't be used directly. Older versions of mtd will choke on bin files, so if your upgrading from an existing OpenWRT it's wise to use the trx files. New versions of mtd when applied on bin files will guide you through what you need to do to convert trx files to mtd files.

 * openwrt-brcm-2.4-<type>.trx
  . This is the firmware in raw format, exactly as it will be written to the flash. This format is used when upgrading from within OpenWrt or during the initial install on one of the following:
   * Asus WL500g
   * Asus WL500gx
   * Buffalo Airstation WBR2-G54S
   * WRT54G v5 - v6 (only)
   * WRT54GS v5 - v6 (only)
 * openwrt-wrt54g-<type>.bin; openwrt-wrt54gs-<type>.bin; openwrt-wrt54gs_v4-<type>.bin; openwrt-wrtsl54gs-<type>.bin
  . This is the exact same as the trx file above, with one exception -- a small header has been added to the start of the file, marking it as a valid upgrade for Linksys models. Supported models:
   * openwrt-wrt54g-<type>.bin
    * [:OpenWrtDocs/Hardware/Linksys/WRT54G:Linksys WRT54G] (v1.0, v1.1, v2.0, v2.2, v3.0, v4.0)
    * [:OpenWrtDocs/Hardware/Linksys/WRT54GL:Linksys WRT54GL]
   * openwrt-wrt54gs-<type>.bin
    * [:OpenWrtDocs/Hardware/Linksys/WRT54GS:Linksys WRT54GS] (v1.0, v1.1, v2.0, v3.0)
   * openety-wrt54g3g-<type>.bin
    * [:OpenWrtDocs/Hardware/Linksys/WRT54G3G:Linksys WRT54G3G]
   * openwrt-wrt54gs_v4-<type>.bin
    * [:OpenWrtDocs/Hardware/Linksys/WRT54GSv4:Linksys WRT54GS (v4.0)]
   * openwrt-wrtsl54gs-<type>.bin
    * [:OpenWrtDocs/Hardware/Linksys/WRTSL54GS:Linksys WRTSL54GS]
 * openwrt-wa840g-<type>.bin; openwrt-we800g-<type>.bin; openwrt-wr850g-<type>.bin
  . This is also a trx file, but with a Motorola header added to the start of the file, making it a valid firmware file for a Motorola device.
There are 3 trx files, found in the micro, pptp and bin directories. Size restrictions aside, it doesn't matter which directory you pick, although if your device only has 2M of flash you will need to use micro. As for which trx file to use, we strongly suggest using the squashfs for reasons explained below.

== SquashFS vs. JFFS2 ==
That's a ton of files, what's with the "<type>"? !OpenWrt gives you your choice of root filesystems; you can either have the root filesystem as SquashFS or JFFS2, We'll explain both. '''If you don't understand, or can't decide, pick SquashFS. It is the most optimal choice for the vast majority of users anyway.  '''Also please note that as of White Russian RC6, it is no longer necessary to worry about SquashFS vs JFFS2, as RC6 uses mini-fo to automatically move things to the JFFS2 partition as needed.

 . WikiPedia:SquashFS
  . The files marked squashfs include a small compressed filesystem within the firmware itself. The disadvantage is that Squashfs is a readonly filesystem, so a separate JFFS2 partition has to be used to store changes and make the filesystem appear writable; the advantage is that Squashfs gets better compression than JFFS2, and you'll always have the original files on the readonly filesystem which can be used as a boot device for recovery.
 WikiPedia:JFFS2
  . The files marked JFFS2 make the entire filesystem JFFS2. The disadvantage is that this takes a few hundred kilobytes more space; the advantage is that changes to included files no longer leaves behind an old copy on the readonly filesystem. There is almost always no good reason to use JFFS2 images. It is extremely rare that a person would ever change enough of the base install to make use of the SquashFs build less optimal than that of the JFFS2 builds. In short, JFFS2 images are not as optimal as SquashFs and provide no effective advantage in real-world use. '''Note:''' The "4M" and "8M" in the filename indicate the flash type, either a 64k erase block or a 128k erase block respectively. In most cases, this means that a 4 megabyte flash chip will use the "4M" version.
/!\ '''The JFFS2 firmware uses an extra setup step which requires an ADDITIONAL REBOOT before the filesystem can be used. Therefore, immediately after installation, you should telnet into your router and run "reboot", or just cycle the power. ''' /!\

/!\ '''OpenWrt White Russian has no failsafe mode for JFFS2 firmware images.''' /!\

After downloading the firmware image you should make sure that the file is not corrupt. This can be verified by comparing the md5sum from your downloaded image with the md5sum listed in the [http://downloads.openwrt.org/whiterussian/newest/bin/md5sum md5sums] file found in the download directory. For win32 platforms use [http://www.pc-tools.net/win32/ md5sums.exe] for GNU/Linux systems use the {{{md5sum}}} command.

= Installing OpenWrt =
To install !OpenWrt on a supported device (see TableOfHardware), download the correct firmware for your device, verify the md5sum and then use the webupgrade of the preinstalled firmware. Be sure that your power supply is stable and do not disconnect it while flashing OpenWrt to your router. After the installation is successful, your router will be booting into your shiny new Linux system.

If you are not happy with !OpenWrt, you can always reinstall your original firmware. Please be sure you have it downloaded and saved on your PC.

== via vendor supplied web interface ==
This is the easiest method on supported devices. This method works fine for Linksys WRT54GL (see http://wiki.openwrt.org/InstallingWrt54gl#head-01985ece7d7673e68766ec20d4667677cfffc7ac). This method requires that the original web interface is available and might not work if you are trying to repair a previously botched install or other abnormal situations.  RussNelson reports that reflashing WRT54GL using v4.30.0 failed, but upgrading to v4.30.5 succeeded.

== via tftp ==
If you are extremely cautious, or are trying to install a self-compiled or modified version of OpenWrt White Russian, please consider using the OpenWrtViaTftp installation method. For some of the hardware models they have special requirements. To avoid potentially serious damage to your router caused by an unbootable firmware you should always read the documentation for your specific router model, see ["http://wiki.openwrt.org/CategoryModel" Category Model].

== via CFE ==
If you already have the serial cable, you'll know how to do it, nevertheless... go ["OpenWrtDocs/Installing/CFE"]

== via JTAG ==
It's not recommended to flash the kernel image via jtag, as it will take more than 2 hours, but it is possible ["OpenWrtDocs/Installing/JTAG"]

/!\ '''We strongly suggest you also read ["OpenWrtDocs/Troubleshooting"] before installing'''

= Upgrading from previous OpenWrt install =
== Backup /etc changes and package list ==
Before you upgrade, please consider making a backup of your /etc directory and then write down the list of packages installed. Alternatively, you can back up the package list by saving a copy of the file {{{/usr/lib/ipkg/status}}}.

/!\ '''Reflashing with OpenWrt WILL RESET THE FILESYSTEM''' /!\

All the changes you have made to the configuration files and all the packages that you have installed will be purged and replaced with the new firmware.

NVRAM is NOT modified by a reflash. Any NVRAM values will remain intact after reflashing.

== Backing up the old OpenWrt as a firmware image ==
To backup an existing !OpenWrt install, use the command:

 . {{{dd if=/dev/mtdblock/1 of=/tmp/firmware.trx}}}
This will produce a pseudo-trx file containing the firmware (trx) followed by a dump of the JFFS2 filesystem -- basically everything except the bootloader and NVRAM. Copy this to a safe place and only restore it to a device with the same size flash chip.

If you don't have enough space to backup the firmware to /tmp, you can use ssh from another machine. Replace {{{$GATEWAY}}} with the hostname or IP address of your !OpenWrt system:

 . {{{ssh $GATEWAY 'dd if=/dev/mtdblock/1' > firmware-backup.trx}}}
== Upgrading / Restoring ==
To reflash from within !OpenWrt you will need to use a trx file:

 . {{{mtd -r write firmware.trx linux}}}
The "-r" will force an automatic reboot after the reflashing. See also: BackupAndRestore.
