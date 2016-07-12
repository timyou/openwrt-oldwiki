= Viewsonic WAPBR-100 (A.K.A. VS10407) Howto =

= Specifications =
== Hardware ==

 *Processor: BCM4712KPB
 *Ethernet: one port
 *Wireless: BCM2050KMI supporting 802.11g
 *Rom: ISSI IS42S32200B-6T (8MB)
 *Flash: Intel TE28F160 (2MB)

== Software ==

This unit apparently uses a version of linksys firmware (similar to that from a WAP54G with bridging, repeating, client, and AP modes).

It comes with boot_wait set to off, and I could not find a way to enable it.

This unit DOES have fw-conf.asp to enable changing options for downgrading and also firmware header verification.

= Getting OpenWRT on this unit =
== Preperation ==

 *I don't know if it's required or just simpler, but I set my unit to use a static ip (192.168.90.2 in my case).
 *Go to http://192.168.90.2/fw-conf.asp (substitute your device's IP) and disable the firmware header.
 *Get a WAP54G patched image from http://downloads.openwrt.org/people/nbd/whiterussian/ (must be squashfs) or build your own using the [:ImageBuilderHowto:ImageBuilder] there (kudos to nbd for the patch!!!). Make sure its small. I suggest building a basic image (at most the size of the 'micro' image) and then seeing how much space you have free...

== Installation ==

 *Upload the firmware using the web interface on the unit. I know it's normal to use TFTP, but I could not find a way to enable boot_wait.
 *Let it finish... and voila... your new device should now be running OpenWRT!

= Notes =
== My ImageBuilder list ==

{{{
base-files
base-files-brcm
bridge
busybox
cifsmount
ipkg
kmod-brcm-et
kmod-brcm-wl
kmod-cifs
kmod-diag
kmod-ext2
kmod-loop
kmod-wlcompat
libgcc
mtd
nvram
uclibc
wireless-tools
wificonf
}}}

This includes functionality to mount a cifs filesystem and mount a ext2 filesystem stored there (in a file) via loop.

== Photos of the unit ==

http://curto.us/WAPBR-100/
