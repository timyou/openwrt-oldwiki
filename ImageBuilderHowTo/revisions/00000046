'''!OpenWrt Image Builder howto'''

[[TableOfContents]]
= About the OpenWrt Image Builder =
This guide should guide you in building your own individual custom OpenWrt firmware images by using the !OpenWrt Image Builder.

Why custom images?[[BR]] These images are for people who want to do less configuration on the router itself, or who want to distribute the images to friends, or for backup purposes. This list could be continued by your own ideas.

= Requirements =
 * a recent GNU/Linux distribution

 . .. to be continued ...

= Using the OpenWrt Image Builder =
If you just want to see how the default images (default, micro and pptp included in the Image Builder) get built, continue with the steps [:ImageBuilderHowTo#Obtaining+and+installing+the+Image+Builder:3.1 Obtaining and installing the Image Builder] and [:ImageBuilderHowTo#Building+the+image:3.5 Building the image].

Everyone else should follow step-by-step in this HOWTO.

[[Anchor(Obtaining_and_installing_the_Image_Builder)]]
== Obtaining and installing the Image Builder ==
The Image Builder can be downloaded from http://downloads.openwrt.org/whiterussian/newest/.

Download it into your home directory (don't use the root account) and untar the tarball. After that change into the new directory.

{{{
cd ~
wget http://downloads.openwrt.org/whiterussian/ \
        newest/OpenWrt-ImageBuilder-Linux-i686.tar.bz2
bzcat OpenWrt-ImageBuilder-Linux-i686.tar.bz2 | tar -xvf -
cd ~/OpenWrt-ImageBuilder-Linux-i686
}}}

[[Anchor(The_package_lists)]]
== The package lists ==
Now you are ready to build your own images. By default the Image Builder builds three types of images: default, micro and pptp. In the file {{{lists/<image_name>.brcm-2.4}}} are the packages defined which go into the image. It will use the ipkg packages from the {{{packages}}} directory.

When removing packages just remove the line with the package name from the {{{<image_name>.brcm-2.4}}} file.

'''NOTE:''' Dependencies are not automatically resolved for ipkg packages by the Image Builder.

Let's start with an example by adding the nas package into your new image.

First download the nas package into the {{{packages}}} directory since it's not included by default.

{{{
cd ~/OpenWrt-ImageBuilder-Linux-i686/packages
wget http://downloads.openwrt.org/whiterussian/packages/non-free/ \
        nas_3.90.37-16_mipsel.ipk
}}}

Create a new package list by copying the default one:

{{{
cd ~/OpenWrt-ImageBuilder-Linux-i686
cd lists
cp -v default.brcm-2.4 my-image.brcm-2.4
}}}

Now edit {{{my-image.brcm-2.4}}} with your favorite editor or just append the nas package with:

{{{
echo "nas" >> my-image.brcm-2.4
}}}

The {{{my-image.brcm-2.4}}} file should look like this after appending nas:

{{{
cat my-image.brcm-2.4
}}}

{{{
# This is a comment line

base-files
base-files-brcm
bridge
busybox
dnsmasq
dropbear
haserl
ipkg
iptables
iwlib
kmod-brcm-wl
kmod-diag
kmod-ppp
kmod-pppoe
kmod-switch
kmod-wlcompat
mtd
nvram
ppp
ppp-mod-pppoe
uclibc
webif
wificonf
wireless-tools
nas
}}}

That's all.

If you don't need any special tweaks you can go ahead with [:ImageBuilderHowTo#Building+the+image:3.5 Building the image].

== Additional packages ==
When you have additional packages which are not listed (e.g. {{{nas}}}) in the {{{packages}}} directory you can add them by copying the package directly into the {{{packages}}} directory. After that add the package as described in [:ImageBuilderHowTo#The+package+lists:3.2 The package lists] above.

{{{
cd ~/OpenWrt-ImageBuilder-Linux-i686/packages
wget http://downloads.openwrt.org/whiterussian/packages/non-free/ \
        nas_3.90.37-16_mipsel.ipk
}}}

== Custom files ==
Sometimes it's useful to add and/or replace files, directories and links in the images with your own.

You have two options here.

'''files directory:'''[[BR]] Files, directories and links in here would go into every image. Existing ones are replaced.

{{{
cd ~/OpenWrt-ImageBuilder-Linux-i686
mkdir -p files
mkdir -p files/etc
touch files/etc/example.txt
}}}

'''files.<image_name> directory:'''[[BR]] Files, directories and links in here will only go into the image you defined by {{{<image_name>}}}. Existing ones are replaced.

{{{
cd ~/OpenWrt-ImageBuilder-Linux-i686
mkdir -p files.my-image
mkdir -p files.my-image/etc
touch files.my-image/etc/example.txt
}}}

You can copy or create files, directories and links as you like.

[[Anchor(Building_the_image)]]
== Building the image ==
This is easy. Just type {{{make}}} and all images you defined in the {{{lists}}} directory get built.

{{{
cd ~/OpenWrt-ImageBuilder-Linux-i686
make clean all
}}}

All built images can be found in the {{{bin/<image_name>}}} directory.

Building the images looks like this (here only for the image {{{my-image}}}):

{{{
### BUILDING IMAGE FROM lists/my-image.brcm-2.4

Unpacking kernel...Done.
Configuring kernel...Done.
Unpacking base-files...Done.
Configuring base-files...Done.
Unpacking base-files-brcm...Done.
Configuring base-files-brcm...Done.
Unpacking bridge...Done.
Configuring bridge...Done.
Unpacking busybox...Done.
Configuring busybox...Done.
Unpacking dnsmasq...Done.
Configuring dnsmasq...Done.
Unpacking dropbear...Done.
Configuring dropbear...Done.
Unpacking ipkg...Done.
Configuring ipkg...Done.
Unpacking iptables...Done.
Configuring iptables...Done.
Unpacking kmod-brcm-et...Done.
Configuring kmod-brcm-et...Done.
Unpacking kmod-brcm-wl...Done.
Configuring kmod-brcm-wl...Done.
Unpacking kmod-diag...Done.
Configuring kmod-diag...Done.
Unpacking kmod-ppp...Done.
Configuring kmod-ppp...Done.
Unpacking kmod-pppoe...Done.
Configuring kmod-pppoe...Done.
Unpacking kmod-wlcompat...Done.
Configuring kmod-wlcompat...Done.
Unpacking libgcc...Done.
Configuring libgcc...Done.
Unpacking mtd...Done.
Configuring mtd...Done.
Unpacking nvram...Done.
Configuring nvram...Done.
Unpacking ppp...Done.
Configuring ppp...Done.
Unpacking ppp-mod-pppoe...Done.
Configuring ppp-mod-pppoe...Done.
Unpacking uclibc...Done.
Configuring uclibc...Done.
Unpacking wireless-tools...Done.
Configuring wireless-tools...Done.
Unpacking wificonf...Done.
Configuring wificonf...Done.
Unpacking zlib...Done.
Configuring zlib...Done.
Unpacking nas...Done.
Configuring nas...Done.
mjn3's trx replacement - v0.81.1
mjn3's addpattern replacement - v0.81
writing firmware v4.20.6 on 5/9/19 (y/m/d)
adding 992 bytes of garbage
mjn3's addpattern replacement - v0.81
writing firmware v1.5.0 on 5/9/19 (y/m/d)
adding 992 bytes of garbage
mjn3's trx replacement - v0.81.1
mjn3's addpattern replacement - v0.81
writing firmware v4.70.6 on 5/9/19 (y/m/d)
adding 992 bytes of garbage
Creating little endian 2.1 filesystem on /tmp/OpenWrt-ImageBuilder-Linux-i686/build_mipsel/linux-2.4-brcm/root.squashfs, block size 65536.

Little endian filesystem, data block size 65536, compressed data, compressed metadata, compressed fragments
Filesystem size 1049.81 Kbytes (1.03 Mbytes)
        33.93% of uncompressed filesystem size (3094.18 Kbytes)
Inode table size 1459 bytes (1.42 Kbytes)
        24.69% of uncompressed inode table size (5910 bytes)
Directory table size 1938 bytes (1.89 Kbytes)
        65.43% of uncompressed directory table size (2962 bytes)
Number of duplicate files found 0
Number of inodes 278
Number of files 123
Number of fragments 12
Number of symbolic links  127
Number of device nodes 0
Number of fifo nodes 0
Number of socket nodes 0
Number of directories 28
Number of uids 1
        root (0)
Number of gids 0
mjn3's trx replacement - v0.81.1
mjn3's addpattern replacement - v0.81
writing firmware v4.20.6 on 5/9/19 (y/m/d)
adding 992 bytes of garbage
mjn3's addpattern replacement - v0.81
writing firmware v1.5.0 on 5/9/19 (y/m/d)
adding 992 bytes of garbage
mjn3's addpattern replacement - v0.81
writing firmware v4.70.6 on 5/9/19 (y/m/d)
adding 992 bytes of garbage
}}}

And here are the results (your new images):

{{{
cd ~/OpenWrt-ImageBuilder-Linux-i686
ls -al bin/my-image/
total 34532
-rw-r--r--  1 user users 2162688 2006-03-30 12:53 openwrt-brcm-2.4-jffs2-4MB.trx
-rw-r--r--  1 user users 2097152 2006-03-30 12:53 openwrt-brcm-2.4-jffs2-8MB.trx
-rw-r--r--  1 user users 1531904 2006-03-30 12:54 openwrt-brcm-2.4-squashfs.trx
-rw-r--r--  1 user users 2162696 2006-03-30 12:53 openwrt-wa840g-jffs2.bin
-rw-r--r--  1 user users 1531912 2006-03-30 12:54 openwrt-wa840g-squashfs.bin
-rw-r--r--  1 user users 2162696 2006-03-30 12:53 openwrt-we800g-jffs2.bin
-rw-r--r--  1 user users 1531912 2006-03-30 12:54 openwrt-we800g-squashfs.bin
-rw-r--r--  1 user users 2162696 2006-03-30 12:53 openwrt-wr850g-jffs2.bin
-rw-r--r--  1 user users 1531912 2006-03-30 12:54 openwrt-wr850g-squashfs.bin
-rw-r--r--  1 user users 2163712 2006-03-30 12:53 openwrt-wrt54g3g-jffs2.bin
-rw-r--r--  1 user users 1532928 2006-03-30 12:54 openwrt-wrt54g3g-squashfs.bin
-rw-r--r--  1 user users 2163712 2006-03-30 12:53 openwrt-wrt54g-jffs2.bin
-rw-r--r--  1 user users 2098176 2006-03-30 12:53 openwrt-wrt54gs-jffs2.bin
-rw-r--r--  1 user users 1532928 2006-03-30 12:54 openwrt-wrt54g-squashfs.bin
-rw-r--r--  1 user users 1532928 2006-03-30 12:54 openwrt-wrt54gs-squashfs.bin
-rw-r--r--  1 user users 2163712 2006-03-30 12:53 openwrt-wrt54gs_v4-jffs2.bin
-rw-r--r--  1 user users 1532928 2006-03-30 12:54 openwrt-wrt54gs_v4-squashfs.bin
-rw-r--r--  1 user users 2098176 2006-03-30 12:53 openwrt-wrtsl54gs-jffs2.bin
-rw-r--r--  1 user users 1532928 2006-03-30 12:54 openwrt-wrtsl54gs-squashfs.bin

}}}

= Some more information =
 * <image_name>
  . This is how you called/named your image. For example lists/default.brcm-2.4, here "default" is the {{{<image_name>}}}

== Important directories ==
Some directories inside the Image Builder in which you would be interested in. These are:

||'''Directory''' ||'''Description''' ||
||bin/<image_name>/ ||Contains directories with the firmware images ||
||build_mipsel/linux-2.4-brcm/root/ ||Contains the files and directories which goes into the image (willbe deleted everytime a new image gets build) ||
||files/ ||Files, directories and links in here would go into every image. Existing ones are replaced. ||
||files.<image_name>/ ||Files, directories and links in here would go only into the image you defined by <image_name>. Existing ones are replaced. ||
||packages/ ||In here are all !OpenWrt packages you can include in the image. ||
