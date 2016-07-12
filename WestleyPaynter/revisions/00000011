##master-page:HomepageTemplate
#format wiki
== Westley Paynter ==

Email: [[MailTo(wpaynter AT SPAMFREE multitechsystems DOT com)]]

=== Pages I Have Contributed to ===

 * [http://wiki.openwrt.org/OpenWrtDocs/Hardware/Linksys/WRT160N WRT160N]
 * [http://wiki.openwrt.org/OpenWrtDocs/Hardware/Airlink101/ANAS350 ANAS350]

=== Devices I Have ===

 * Airlink101 ANAS350
 * Linksys WRT54-GL
 * Linksys NSLU2 (Running OpenWRT)
 * Linksys WRT160N

=== Patches ===

 *  Linksys WRT160N Detection [http://wiki.openwrt.org/WestleyPaynter?action=AttachFile&do=view&target=openwrt-wrt160n-detection-rev12384.diff View in Browser] [http://wiki.openwrt.org/WestleyPaynter?action=AttachFile&do=get&target=openwrt-wrt160n-detection-rev12384.diff Download] [http://snipes420.googlepages.com/openwrt-wrt160n-detection-rev12384.diff Another copy here]

=== Notes about TFTP ===

TFTP commands that I use that are useful. (using tftp in Back|Track linux livecd)
{{{tftp 192.168.1.1
binary
rexmt 1
trace
put firmware.bin}}}
Also sometimes it is helpful to set the session timeout high. (5000 seconds)

{{{
timeout 5000
}}}

=== Pages that have excellent formatting ===

 * [http://wiki.openwrt.org/OpenWrtDocs/Hardware/Linksys/WRT54GL WRT54GL]

...

== WIP ==

=== Running OpenWrt on an xbox ===
An xbox is a gaming console made by microsoft that is basically a x86 computer with some custom tweaks.
We should be able to use the x86 build option and add the xbox-linux kernel patches to that to get openwrt on the xbox.
I will focus first on getting it running with the xbox-linux bios 'cromwell' and then perhaps get it going from a live booting cd for the xbox.


OK now we start.
Get build source.

{{{
svn checkout https://svn.openwrt.org/openwrt/trunk/ ~/xbox-openwrt/
}}}

go to ~/xbox-openwrt/target/linux/x86 and download this config to this folder

{{{
cd ~/xbox-openwrt/target/linux/x86
wget http://snipes420.googlepages.com/config-2.6.22
}}}

go to ~/xbox-openwrt/target/linux/x86/patches and download this patch to this folder

{{{
cd ~/xbox-openwrt/target/linux/x86/patches
wget http://snipes420.googlepages.com/linux-2.6.22.7-xbox.patch
}}}

edit the target/linux/x86/Makefile and change the kernel version to 2.6.22.7

{{{
nano ~/xbox-openwrt/target/linux/x86/Makefile
}}}

install the raincoat package

{{{
cd ~/xbox-openwrt/
wget http://snipes420.googlepages.com/raincoat-openwrt-package.tgz
tar -zxvf raincoat-openwrt-package.tgz
rm raincoat-openwrt-package.tgz
}}}

make a folder for the extra files we need for packaging.

{{{
mkdir ~/xbox-openwrt/files
mkdir ~/xbox-openwrt/files/boot
}}}

Make the whole thing

{{{
make
}}}

----
CategoryHomepage
