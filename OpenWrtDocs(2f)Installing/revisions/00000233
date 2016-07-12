#acl Known:read,write All:read
##
## Note: these pages document the firmware itself, not packages
##       questions/comments should be posted to the forum
##
OpenWrtDocs [[TableOfContents]]

!OpenWrt is free software, provided AS-IS under the terms of the GNU General Public License. We expect that you are knowledgeable about GNU/Linux and basic networking concepts, before you install !OpenWrt on your router. Support may be provided on a voluntary basis by developers and fellow users, but support is not guaranteed.

= Supported hardware =
See TableOfHardware.

= Choosing the right firmware =
You can get the latest !OpenWrt White Russian firmware images at: http://downloads.openwrt.org/whiterussian/newest/

Bugs in the firmware should be reported via the ticket system [https://dev.openwrt.org/newticket here].

White Russian ships in several variations, each with a slightly different set of packages installed by default. You're still free to add whatever packages you want, but this will save you from manually installing some common packages immediately after reflashing.

 . micro/
  . The least amount of packages required for a functional system; there isn't even a web interface.
 bin/ (aka default)
  . Standard image (web interface, pppoe)
 pptp/
  . Standard image (web interface, pptp)
|| ||micro ||bin ||pptp ||
||base-files || (./) || (./) || (./) ||
||base-files-brcm || (./) || (./) || (./) ||
||bridge || (./) || (./) || (./) ||
||["busybox"] || (./) || (./) || (./) ||
||dnsmasq || (./) || (./) || (./) ||
||["dropbear"] || (./) || (./) || (./) ||
||haserl || {X} || (./) || (./) ||
||ipkg* || (./) || (./) || (./) ||
||iptables || (./) || (./) || (./) ||
||["iwlib"] || (./) || (./) || (./) ||
||kmod-brcm-wl || (./) || (./) || (./) ||
||kmod-diag || (./) || (./) || (./) ||
||kmod-gre || {X} || {X} || (./) ||
||kmod-pppoe || {X} || (./) || {X} ||
||kmod-wlcompat || (./) || (./) || (./) ||
||kmod-switch || (./) || (./) || (./) ||
||["mtd"] || (./) || (./) || (./) ||
||nvram || (./) || (./) || (./) ||
||ppp || {X} || (./) || (./) ||
||ppp-mod-pppoe || {X} || (./) || {X} ||
||pptp || {X} || {X} || (./) ||
||["uclibc"] || (./) || (./) || (./) ||
||webif || {X} || (./) || (./) ||
||wificonf || (./) || (./) || (./) ||
||wireless-tools || {X} || (./) || (./) ||

* note: micro includes a stripped down version of the ipkg util


== TRX vs. BIN ==
The firmware files are shipped as either "trx" or "bin" files. The bin file is nothing more than a trx file with additional information added to make it compatible with the vendor's upgrade utilities. You should only use the bin files when you cannot use the trx files directly.

 * openwrt-brcm-2.4-<type>.trx
  . This is the firmware in raw format, exactly as it will be written to the flash. This format is used when upgrading from within OpenWrt or during the initial install on one of the following:
   * Asus WL500g
   * Asus WL500gx
   * Buffalo Airstation WBR2-G54S
   * WRT54G v5 - v6 (only, not officially supported)
   * WRT54GS v5 - v6 (only, not officially supported)
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
There are 3 trx files, found in the micro, pptp and bin directories explained above. Size restrictions aside, it doesn't matter which directory you pick, although if your device only has 2M of flash you will need to use micro.

After downloading the firmware image you should make sure that the file is not corrupt. This can be verified by comparing the md5sum from your downloaded image with the md5sum listed in the [http://downloads.openwrt.org/whiterussian/newest/MD5SUMS md5sums] file found in the download directory. For win32 platforms use [http://www.pc-tools.net/win32/ md5sums.exe] for GNU/Linux systems use the {{{md5sum}}} command.

= Installing OpenWrt =
There are multiple ways to reflash the firmware, we will explain each method below. You can use any method, the end result will be the same. After reflashing, the device will automatically reboot into the new firmware.

If you are not happy with !OpenWrt, you can always reinstall your original firmware. Please be sure you have it downloaded and saved on your PC.

/!\ '''We strongly suggest print a copy of ["OpenWrtDocs/Troubleshooting"] in case you have any trouble with the install'''

== via vendor supplied web interface ==
This is the easiest method, Open your web browser and use the firmware upgrade page on your device to upload the !OpenWrt firmware.

== via tftp ==
If you're being extremely cautious or are attempting to reflash from a failed upgrade, you can use tftp to install the firmware. This method is explained in detail on the OpenWrtViaTftp page.

/!\ Note: some models have additional requirements, please refer to the CategoryModel page for documentation specific to your router model.

== via CFE ==
If you already have the serial cable, you'll know how to do it, nevertheless... go ["OpenWrtDocs/Installing/CFE"]

== via JTAG ==
It's not recommended to flash the kernel image via jtag, as it will take more than 2 hours, but it is possible ["OpenWrtDocs/Installing/JTAG"]

== via the OpenWrt commandline ==
Reflashing OpenWrt will overwrite the filesystem, erasing all previous applications and data. You are strongly urged to back up any changes you may have made to the system.

{{{
mtd -r write firmware.trx linux
}}}
