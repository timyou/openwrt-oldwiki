'''!OpenWrt building packages howto'''

[[TableOfContents]]
= About the OpenWrt SDK =
This howto is for people who would like to port/package applications to OpenWrt with the !OpenWrt Software Development Kit (SDK).

When using the SDK you don't require a full buildroot. The SDK is a stripped down version of it, which includes the toolchain and all the required library and header files to cross-compile applications for !OpenWrt.

= Requirements =
 * a recent GNU/Linux distribution
 * GNU Make (at least 3.80 with the Debian patch)

 . .. to be continued ...

= Using the OpenWrt SDK =
'''TIP:''' Before you begin porting your own package to !OpenWrt, check if it has not been already done by someone else. To check that [http://dev.openwrt.org/browser/trunk/openwrt/package/ browse the subversion repository] of the development version in your web browser and see if the package is already there. Don't do the work twice.

Let's start with porting and packaging the well known "Hello world" program as an example.

== Obtaining and installing the SDK ==
The SDK can be downloaded from http://downloads.openwrt.org/whiterussian/newest/.

Download it into your home directory (don't use the root account) and untar the tarball. After that change into the new directory.

{{{
cd ~
wget http://downloads.openwrt.org/whiterussian/newest/OpenWrt-SDK-Linux-i686-1.tar.bz2
bzcat OpenWrt-SDK-Linux-i686-1.tar.bz2 | tar -xvf -
cd ~/OpenWrt-SDK-Linux-i686-1
}}}

== Creating the directories ==
Create the following directories:

{{{
cd ~/OpenWrt-SDK-Linux-i686-1
mkdir -p package/helloworld/ipkg
mkdir -p package/helloworld/patches
}}}

Directories and their contents:

{{{
#!CSV 
Directory; Description
ipkg; Control file which contains information about your package
patches; Patch files for example 100-foo.patch
}}}

'''TIP:''' To compile more than one package in a special order do:

{{{
cd ~/OpenWrt-SDK-Linux-i686-1
mkdir -p package/100-packagename/ipkg
mkdir -p package/100-packagename/patches
mkdir -p package/200-packagename/ipkg
mkdir -p package/200-packagename/patches
}}}

== Creating the required files ==
'''TIP:''' When creating the files via copy & paste use the Unix command {{{unexpand}}} to translate the leading spaces into tabs.

{{{
unexpand --first-only - | cat >package/helloworld/Config.in
}}}

After pasting it, press {{{ENTER}}} and then {{{CTRL-D}}} keys to save the file.

You can also create your own files in the {{{package/helloworld}}} directory (for example config files). That files you can access in your {{{package/helloworld/Makefile}}} with {{{./filename}}} and copy it to your {{{$(PKG_INSTALL_DIR)}}} directory.

=== package/helloworld/Config.in ===
{{{
config BR2_PACKAGE_HELLO
        prompt "hello............................. The classic greeting, and a good example"
        tristate
        default m if CONFIG_DEVEL
        help
              The GNU hello program produces a familiar, friendly greeting.  It
              allows non-programmers to use a classic computer science tool which
              would otherwise be unavailable to them.
              .
              Seriously, though: this is an example of how to do a Debian package.
              It is the Debian version of the GNU Project's `hello world' program
              (which is itself an example for the GNU Project).

              http://www.wheretofindpackage.tld
}}}

=== package/helloworld/Makefile ===
The Makefile rely one the way the software you want to package is shipped. Basically we can divide the software into 2 main categories :

 * C (or ANSI-C) programs
  * shipped with configure script
  * shipped with Makefile script (with references to gcc or $(CC) )
  * sources files only
 * C++ programs
  * potentially uClibc++ linkables
  * not uClibc++ linkables

'''TIP:''' Use the {{{md5sum}}} command to create the {{{PKG_MD5SUM}}} from the original tarball. Use {{{@SF/hello}}} (choose a random !SourceForge mirror) for the {{{PKG_SOURCE_URL}}} when your program has a download location on !SourceForge.

=== Sample Makefile for C/C++ programs shipped with configure script ===
{{{
include $(TOPDIR)/rules.mk

PKG_NAME:=hello
PKG_VERSION:=2.1.1
PKG_RELEASE:=1
PKG_MD5SUM:=70c9ccf9fac07f762c24f2df2290784d

PKG_SOURCE_URL:=ftp://ftp.cs.tu-berlin.de/pub/gnu/hello \
        http://mirrors.sunsite.dk/gnu/hello \
        http://ftp.gnu.org/gnu/hello
PKG_SOURCE:=$(PKG_NAME)-$(PKG_VERSION).tar.gz
PKG_CAT:=zcat

PKG_BUILD_DIR:=$(BUILD_DIR)/$(PKG_NAME)-$(PKG_VERSION)
PKG_INSTALL_DIR:=$(PKG_BUILD_DIR)/ipkg-install

include $(TOPDIR)/package/rules.mk

$(eval $(call PKG_template,HELLO,$(PKG_NAME),$(PKG_VERSION)-$(PKG_RELEASE),$(ARCH)))

$(PKG_BUILD_DIR)/.configured: $(PKG_BUILD_DIR)/.prepared
        (cd $(PKG_BUILD_DIR); \
                $(TARGET_CONFIGURE_OPTS) \
                CFLAGS="$(TARGET_CFLAGS)" \
                CPPFLAGS="-I$(STAGING_DIR)/usr/include -I$(STAGING_DIR)/include" \
                LDFLAGS="-L$(STAGING_DIR)/usr/lib -L$(STAGING_DIR)/lib" \
                ./configure \
                        --target=$(GNU_TARGET_NAME) \
                        --host=$(GNU_TARGET_NAME) \
                        --build=$(GNU_HOST_NAME) \
                        --prefix=/usr \
                        --without-libiconv-prefix \
                        --without-libintl-prefix \
                        --disable-nls \
        );
        ## Add software specific configurable options above
        ## See : ./configure --help
        touch $@

$(PKG_BUILD_DIR)/.built:
        rm -rf $(PKG_INSTALL_DIR)
        mkdir -p $(PKG_INSTALL_DIR)/usr/bin
        $(MAKE) -C $(PKG_BUILD_DIR)/src \
                $(TARGET_CONFIGURE_OPTS) \
                prefix="$(PKG_INSTALL_DIR)/usr"
        $(CP) $(PKG_BUILD_DIR)/src/hello $(PKG_INSTALL_DIR)/usr/bin
        touch $@

$(IPKG_HELLO):
        install -d -m0755 $(IDIR_HELLO)/usr/bin
        $(CP) $(PKG_INSTALL_DIR)/usr/bin/hello $(IDIR_HELLO)/usr/bin
        $(RSTRIP) $(IDIR_HELLO)
        $(IPKG_BUILD) $(IDIR_HELLO) $(PACKAGE_DIR)

mostlyclean:
        make -C $(PKG_BUILD_DIR) clean
        rm $(PKG_BUILD_DIR)/.built
}}}

=== Sample Makefile for C/C++ software shipped with a Makefile containing references to gcc or $(CC) ===
If you Makefile contains harcoded "gcc" commands, then you will have to patch the makefile and replace gcc with $(CC) in order to define at "make time" the cross-compiler to use.

/!\ '''Note this Makefile is provided as an example only; it will not compile
{{{
include $(TOPDIR)/rules.mk

PKG_NAME:=hello
PKG_VERSION:=2.1.1
PKG_RELEASE:=1
PKG_MD5SUM:=70c9ccf9fac07f762c24f2df2290784d

PKG_SOURCE_URL:=ftp://ftp.cs.tu-berlin.de/pub/gnu/hello \
        http://mirrors.sunsite.dk/gnu/hello \
        http://ftp.gnu.org/gnu/hello
PKG_SOURCE:=$(PKG_NAME)-$(PKG_VERSION).tar.gz
PKG_CAT:=zcat

PKG_BUILD_DIR:=$(BUILD_DIR)/$(PKG_NAME)-$(PKG_VERSION)
PKG_INSTALL_DIR:=$(PKG_BUILD_DIR)/ipkg-install

include $(TOPDIR)/package/rules.mk

$(eval $(call PKG_template,HELLO,$(PKG_NAME),$(PKG_VERSION)-$(PKG_RELEASE),$(ARCH)))

$(PKG_BUILD_DIR)/.configured: $(PKG_BUILD_DIR)/.prepared
        #Since there is no configure script, we can directly go to the building step
        touch $@

$(PKG_BUILD_DIR)/.built:
        rm -rf $(PKG_INSTALL_DIR)
        mkdir -p $(PKG_INSTALL_DIR)/usr/bin
        #Note here that we pass cross-compiler as default compiler to use
        $(MAKE) -C $(PKG_BUILD_DIR)/src \
                CC=$(TARGET_CC) \
                $(TARGET_CONFIGURE_OPTS) \
                prefix="$(PKG_INSTALL_DIR)/usr"
        $(CP) $(PKG_BUILD_DIR)/src/hello $(PKG_INSTALL_DIR)/usr/bin
        touch $@

$(IPKG_HELLO):
        install -d -m0755 $(IDIR_HELLO)/usr/bin
        $(CP) $(PKG_INSTALL_DIR)/usr/bin/hello $(IDIR_HELLO)/usr/bin
        $(RSTRIP) $(IDIR_HELLO)
        $(IPKG_BUILD) $(IDIR_HELLO) $(PACKAGE_DIR)

mostlyclean:
        make -C $(PKG_BUILD_DIR) clean
        rm $(PKG_BUILD_DIR)/.built
}}}

=== Sample Makefile for C/C++ programs without makefiles (usually one or two source files) ===

/!\ '''Note this Makefile is provided as an example only; it will not compile
{{{
include $(TOPDIR)/rules.mk

PKG_NAME:=hello
PKG_VERSION:=2.1.1
PKG_RELEASE:=1
PKG_MD5SUM:=70c9ccf9fac07f762c24f2df2290784d

PKG_SOURCE_URL:=ftp://ftp.cs.tu-berlin.de/pub/gnu/hello \
        http://mirrors.sunsite.dk/gnu/hello \
        http://ftp.gnu.org/gnu/hello
PKG_SOURCE:=$(PKG_NAME)-$(PKG_VERSION).tar.gz
PKG_CAT:=zcat

PKG_BUILD_DIR:=$(BUILD_DIR)/$(PKG_NAME)-$(PKG_VERSION)
PKG_INSTALL_DIR:=$(PKG_BUILD_DIR)/ipkg-install

include $(TOPDIR)/package/rules.mk

$(eval $(call PKG_template,HELLO,$(PKG_NAME),$(PKG_VERSION)-$(PKG_RELEASE),$(ARCH)))

$(PKG_BUILD_DIR)/.configured: $(PKG_BUILD_DIR)/.prepared
        #Since there is no configure script, we can directly go to the building step
        touch $@

$(PKG_BUILD_DIR)/.built:
        rm -rf $(PKG_INSTALL_DIR)
        mkdir -p $(PKG_INSTALL_DIR)/usr/bin
        $(TARGET_CC) $(PKG_BUILD_DIR)/src/$(PKG_NAME).c -o $(PKG_BUILD_DIR)/$(PKG_NAME) ## -lyourlib #Note we directly call the cross-compiler and define its output
        $(CP) $(PKG_BUILD_DIR)/src/hello $(PKG_INSTALL_DIR)/usr/bin
        touch $@

$(IPKG_HELLO):
        install -d -m0755 $(IDIR_HELLO)/usr/bin
        $(CP) $(PKG_INSTALL_DIR)/usr/bin/hello $(IDIR_HELLO)/usr/bin
        $(RSTRIP) $(IDIR_HELLO)
        $(IPKG_BUILD) $(IDIR_HELLO) $(PACKAGE_DIR)

mostlyclean:
        make -C $(PKG_BUILD_DIR) clean
        rm $(PKG_BUILD_DIR)/.built
}}}

=== Sample Makefile for C++ shipped with configure script, and uClibc++ linkables ===

/!\ '''Note this Makefile is provided as an example only; it will not compile
{{{
include $(TOPDIR)/rules.mk

PKG_NAME:=hello
PKG_VERSION:=2.1.1
PKG_RELEASE:=1
PKG_MD5SUM:=70c9ccf9fac07f762c24f2df2290784d

PKG_SOURCE_URL:=ftp://ftp.cs.tu-berlin.de/pub/gnu/hello \
        http://mirrors.sunsite.dk/gnu/hello \
        http://ftp.gnu.org/gnu/hello
PKG_SOURCE:=$(PKG_NAME)-$(PKG_VERSION).tar.gz
PKG_CAT:=zcat

PKG_BUILD_DIR:=$(BUILD_DIR)/$(PKG_NAME)-$(PKG_VERSION)
PKG_INSTALL_DIR:=$(PKG_BUILD_DIR)/ipkg-install

include $(TOPDIR)/package/rules.mk

$(eval $(call PKG_template,HELLO,$(PKG_NAME),$(PKG_VERSION)-$(PKG_RELEASE),$(ARCH)))

$(PKG_BUILD_DIR)/.configured: $(PKG_BUILD_DIR)/.prepared
        (cd $(PKG_BUILD_DIR); \
                $(TARGET_CONFIGURE_OPTS) \
                CFLAGS="$(TARGET_CFLAGS)" \
                CPPFLAGS="-I$(STAGING_DIR)/usr/include -I$(STAGING_DIR)/include" \
                LDFLAGS="-L$(STAGING_DIR)/usr/lib -L$(STAGING_DIR)/lib" \
                ./configure \
                        CXXFLAGS="$(TARGET_CFLAGS) -fno-builtin -fno-rtti -nostdinc++" \
                        CPPFLAGS="-I$(STAGING_DIR)/usr/include -I$(STAGING_DIR)/include" \
                        LDFLAGS="-nodefaultlibs -L$(STAGING_DIR)/usr/lib -L$(STAGING_DIR)/lib" \ #do not use default libraries since we want uClibc++ linking
                        LIBS="-luClibc++ -lc -lm -lgcc" \ # You may need to add other libraries : lpcap, lssl ... #
                        --target=$(GNU_TARGET_NAME) \
                        --host=$(GNU_TARGET_NAME) \
                        --build=$(GNU_HOST_NAME) \
                        --prefix=/usr \
                        --without-libiconv-prefix \
                        --without-libintl-prefix \
                        --disable-nls \
        );
        ## Add software specific configurable options above
        ## See : ./configure --help

        touch $@

$(PKG_BUILD_DIR)/.built:
        rm -rf $(PKG_INSTALL_DIR)
        mkdir -p $(PKG_INSTALL_DIR)/usr/bin
        $(MAKE) -C $(PKG_BUILD_DIR)/src \
                $(TARGET_CONFIGURE_OPTS) \
                prefix="$(PKG_INSTALL_DIR)/usr"
        $(CC) $(PKG_BUILD_DIR)/src/hello $(PKG_INSTALL_DIR)/usr/bin
        touch $@

$(IPKG_HELLO):
        install -d -m0755 $(IDIR_HELLO)/usr/bin
        $(CP) $(PKG_INSTALL_DIR)/usr/bin/hello $(IDIR_HELLO)/usr/bin
        $(RSTRIP) $(IDIR_HELLO)
        $(IPKG_BUILD) $(IDIR_HELLO) $(PACKAGE_DIR)

mostlyclean:
        make -C $(PKG_BUILD_DIR) clean
        rm $(PKG_BUILD_DIR)/.built
}}}

=== package/helloworld/ipkg/hello.control ===
{{{
Package: hello
Priority: optional
Section: misc
Description: The GNU hello world program
}}}

=== package/helloworld/patches/100-hello.patch ===
This example will also work without the Debian patch. So you can skip this point.

{{{
cd package/helloworld/patches
wget http://ftp.debian.org/debian/pool/main/h/hello/hello_2.1.1-4.diff.gz
gunzip hello_2.1.1-4.diff.gz
mv hello_2.1.1-4.diff 100-hello.patch
}}}

'''TIP:''' You can apply as many patches as you like. To apply them in a special order name them like:

{{{
100-xxx.patch
200-xxx.patch
}}}

== Compile the package ==
The {{{make}}} command below compiles every package that you have created in the {{{package}}} directory.

{{{
cd ~/OpenWrt-SDK-Linux-i686-1
make clean && make compile
}}}

'''NOTE:''' If you are using GNU make 3.80 (current "latest") and get a "virtual memory exhausted" message while making, see [http://gamecontractor.org/Make this page].

For Slackware users there is a fixed make package [http://internetghetto.org/files/index.php?download=./make-fix/make-fixed-3.80-i386-1.tgz here] and sources + patch are [http://internetghetto.org/files/index.php?dir=./make-fix/orig/ here].

When the compiling is finished you have a ready to use ipkg package for !OpenWrt in the {{{~/OpenWrt-SDK-Linux-i686-1/bin/packages}}} directory.

{{{
cd bin/packages; ls -al hello_2.1.1-1_mipsel.ipk
-rw-r--r--  1 openwrt-dev openwrt-dev 3976 Sep 14 13:03 hello_2.1.1-1_mipsel.ipk
}}}

= Contribute your new ported program =
When you like you can contribute your program/package to the !OpenWrt community. It may be included in further versions of !OpenWrt.

To do this create a patch from your {{{package/<PKG_NAME>}}} directory with:

{{{
cd ~/OpenWrt-SDK-Linux-i686-1
diff -ruN package/<PKG_NAME>.orig package/<PKG_NAME> > <PKG_NAME>-<PKG_VERSION>.patch
}}}

Once you have created a patch [https://dev.openwrt.org/newticket open a ticket] and submit your new package (the patch).

= Native Development =
You need 150Mb storage unit (USB or SD Card)

- Download the file [http://www.uclibc.org/downloads/root_fs_mipsel.ext2.bz2 Native Mipsel Toolchain] (24Mb)

- Bunzip2 (120mb) it to the storage unit in a ext2 partition.

- unmount partition

- Execute this script, I have it at /sbin/devel.sh
{{{
#!/bin/sh
killall logger
killall syslogd
killall telnetd
killall crond
killall klogd
killall udhcpc
killall httpd
rmmod ext3
rmmod jbd

mount /dev/mmc/disc0/part1 /mnt -o noatime async
swapoff -a
mkswap  /dev/mmc/disc0/part2
swapon  /dev/mmc/disc0/part2
mount -o move /dev /mnt/dev
rm -r /dev
ln -s /mnt/dev /dev

mount -o move /tmp /mnt/tmp
rm -r /tmp
ln -s /mnt/tmp /tmp

mount -o move /proc /mnt/proc
rm -r /proc
ln -s /mnt/proc /proc

echo " *** exit *** to back - Para volver al sistema"
chroot /mnt/ /bin/ash -
echo " *** Me are here again - De vuelta al sistema original ***"

rm /tmp
rm /dev
mkdir /tmp
mkdir /dev
mount -o move /mnt/tmp/ /tmp/
mount -o move /mnt/dev/ /dev/
mkdir proc2
mount -o move /mnt/proc/ /proc2/
rm /proc
ln -s /proc2 /proc
umount /mnt
swapoff -a
}}}
- Go /home

- download the source. Example: [http://www.didiwiki.org/sources/didiwiki-0.5.tar.gz Didiwiki-0.5.tar.gz] from [http://www.didiwiki.org]

- tar -xvzf didiwiki-0.5.tar.gz

- cd didiwiki-0.5

- configure     (1 minute)

- make          (1 minute)

- You have your new Binary in the SRC directory (didiwiki)

- copy it to the /tmp directori

- type exit

You have the binary in /tmp directory. copy it to /usr/bin

The result [http://gepage.googlepages.com/didiwiki.mipsel.binary.gz didiwiki.mipsel.binary.gz] a small wiki for our router at 8000 port. If you don't use storage unit, you must create /home to store new pages. /home/.didiwiki/*

= Links =
You can find an useful reference for the packaging process in nbd's paper to the '!OpenWrt Hacking' talk on the 22C3: [[BR]]- http://events.ccc.de/congress/2005/fahrplan/attachments/567-Paper_HackingOpenWRT.pdf

Full buildroot documentation (for compiling kernel modules and such things, for the rest the SDK should be used) [[BR]]- http://downloads.openwrt.org/docs/buildroot-documentation.html
