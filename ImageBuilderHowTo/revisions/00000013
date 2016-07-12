OpenWrt Image Builder Howto

[[TableOfContents]]


= About the OpenWrt Image Builder =

This guide should process you in building your own individual/custom
OpenWrt firmware image by using the OpenWrt Image Builder.

Why custom images?
[[BR]]These images are for people who wan't to do less configuration on the
router or wan't to distribute the images for friends, or for backup
perposes this list could to be continued by your own ideas.


= Requirements =
   * a recent GNU/Linux distribution

   ... to be continued ...


= Using the OpenWrt Image Builder =

If you just like to see how the default images (default, micro and pptp
included in the Image Builder) gets build, only follow the next step
"3.1 Obtaining and installing the Image Builder" and the step
"3.5 Building the image".

Everyone else show follow point by point on this howto.


== Obtaining and installing the Image Builder ==

The Image Builder could be downloaded from http://downloads.openwrt.org/whiterussian/.

Download it into your homedir (don't use the root account) and untar the
tarball. After that change into the new directory.

{{{
cd ~
wget http://downloads.openwrt.org/whiterussian/ \
        rc3/bin/OpenWrt-ImageBuilder-Linux-i686.tar.bz2
bzcat OpenWrt-ImageBuilder-Linux-i686.tar.bz2 | tar -xvf -
cd ~/OpenWrt-ImageBuilder-Linux-i686
}}}


== The image/package lists ==

Now you're ready to build your own images. By default the Image Builder
builds three types of images. They're default, micro and pptp. In the
file lists/<image_name>.brcm-2.4 are the packages defined which go into
the image. It takes the ipkg packages out of the packages directory.

When removing packages just remove the package name from the
<image_name>.brcm-2.4 file.

Let's start with an example by adding the haserl package into your new
image.


Create a new package list by copying the default one:

{{{
cd ~/OpenWrt-ImageBuilder-Linux-i686
cd lists
cp -v default.brcm-2.4 my-image.brcm-2.4
}}}


Now edit my-image.brcm-2.4 with your favourite editor or just append the
haserl package with:

{{{
echo "haserl" >> my-image.brcm-2.4
}}}

The my-image.brcm-2.4 file should look like this after appending haserl:

{{{
cat my-image.brcm-2.4
base-files
base-files-brcm
bridge
busybox
dnsmasq
dropbear
ipkg
iptables
kmod-brcm-et
kmod-brcm-wl
kmod-diag
kmod-ppp
kmod-pppoe
kmod-wlcompat
libgcc
mtd
nvram
ppp
ppp-mod-pppoe
uclibc
wireless-tools
wificonf
zlib
haserl
}}}

That's all.

If you don't need any special tweaks you can go a head with
"3.5 Building the image".


== Additinal packages ==

When you've additinal packages which are not listed (f. e. nas) in the
packages directory you can add them by copying the package directly into
the packages directory. After that add the package as described in 3.2
above.

{{{
cd ~/OpenWrt-ImageBuilder-Linux-i686
wget http://downloads.openwrt.org/whiterussian/ \
        packages/non-free/nas_3.90.37-7_mipsel.ipk
mv -v nas_3.90.37-7_mipsel.ipk packages/
}}}


== Custom files ==

Sometimes it's useful to add and/or replace files, directories and links
in the images with your own.

You've two options here.


files directory[[BR]]
Files, directories and links in here would go into every image. Existing
ones gets overwritten/replaced.

{{{
cd ~/OpenWrt-ImageBuilder-Linux-i686
mkdir -p files
mkdir -p files/etc
touch files/etc/example.txt
}}}

files.<image_name> directory[[BR]]
Files, directories and links in here would only go into the image you
defined by <image_name>. Existing ones gets overwritten/replaced.

{{{
cd ~/OpenWrt-ImageBuilder-Linux-i686
mkdir -p files.my-image
mkdir -p files.my-image/etc
touch files.my-image/etc/example.txt
}}}

You can copy/create files, directories and links as you like.


== Building the image ==

That's very easy. Just type make and all images you defined in the
lists directory gets build.

{{{
make clean && make
}}}

All created images can be found in the bin/<image_name>/ directory.


Building the images looks like this (here only for the my-image image):

{{{
cd ~/OpenWrt-ImageBuilder-Linux-i686
make clean && make

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
Unpacking haserl...Done.
Configuring haserl...Done.
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
insgesamt 23024
drwxr-xr-x  2 user user    4096 2005-09-19 20:14 .
drwxr-xr-x  3 user user    4096 2005-09-19 20:14 ..
-rw-r--r--  1 user user 2228224 2005-09-19 20:14 openwrt-brcm-2.4-jffs2-4MB.trx
-rw-r--r--  1 user user 2228224 2005-09-19 20:14 openwrt-brcm-2.4-jffs2-8MB.trx
-rw-r--r--  1 user user 1576960 2005-09-19 20:14 openwrt-brcm-2.4-squashfs.trx
-rw-r--r--  1 user user 2228232 2005-09-19 20:14 openwrt-motorola-jffs2-4MB.bin
-rw-r--r--  1 user user 2228232 2005-09-19 20:14 openwrt-motorola-jffs2-8MB.bin
-rw-r--r--  1 user user 1576968 2005-09-19 20:14 openwrt-motorola-squashfs.bin
-rw-r--r--  1 user user 2229248 2005-09-19 20:14 openwrt-wrt54g-jffs2.bin
-rw-r--r--  1 user user 2229248 2005-09-19 20:14 openwrt-wrt54gs-jffs2.bin
-rw-r--r--  1 user user 1577984 2005-09-19 20:14 openwrt-wrt54g-squashfs.bin
-rw-r--r--  1 user user 1577984 2005-09-19 20:14 openwrt-wrt54gs-squashfs.bin
-rw-r--r--  1 user user 2229248 2005-09-19 20:14 openwrt-wrt54gs_v4-jffs2.bin
-rw-r--r--  1 user user 1577984 2005-09-19 20:14 openwrt-wrt54gs_v4-squashfs.bin
}}}


= Some more information =

   * <image_name>

     This is how you called/named you image. For example lists/default.brcm-2.4,
     here "default" is the <image_name>

== Important directories ==

Some directories inside the Image Builder in which you would be
interested in. These are:

   * bin/<image_name>/[[BR]]
   Contains directories with the firmware images

   * build_mipsel/linux-2.4-brcm/root/[[BR]]
   Contains the files and directories which goes into the image (will
   be deleted everytime a new image gets build)

   * files/[[BR]]
   Files, directories and links in here would go into every image. Existing
   ones gets overwritten/replaced

   * files.<image_name>/[[BR]]
   Files, directories and links in here would go only into the image you
   defined by <image_name>. Existing ones gets overwritten/replaced.

   * packages/[[BR]]
   In here are all OpenWrt packages you can use/include in the image.
