OpenWrt SDK Howto
[[TableOfContents]]

= About the OpenWrt SDK =

This howto is for people who would like to port/package applications
to OpenWrt with the OpenWrt Software Development Kit (SDK).

When using the SDK you don't require a full buildroot. The SDK is
a stripped down version of it, which includes the toolchain and all the
required libs and header files to cross-compile the package and the
applications for OpenWrt.

Sience the usage of the SDK is similar to the Buildroot also look at
the buildroot documentation which can be found at:
http://downloads.openwrt.org/docs/buildroot-documentation.html


= Using the OpenWrt SDK =

Let's start with porting and packaging the well known "Hello world"
program as an example.


== Obtaining and installing the SDK ==

The SDK could be downloaded from http://downloads.openwrt.org/whiterussian/

Download it into your homedir (don't use the root account) and untar
the tarball. After that change into the new directory.

{{{
cd ~
wget http://downloads.openwrt.org/whiterussian/rc2/bin/OpenWrt-SDK-Linux-i686-1.tar.bz2
bzcat OpenWrt-SDK-Linux-i686-1.tar.bz2 | tar -xvf -
cd ~/OpenWrt-SDK-Linux-i686-1
}}}


== Creating the directories ==

{{{
mkdir -p package/helloworld/ipkg
mkdir -p package/helloworld/patches
}}}

Directories and their contents:
{{{#!CSV
Directory; Description
ipkg; Control file which contains information about your package
patches; Patch files for example 100-foo.patch
}}}


== Creating the required files ==

TIP: When creating the files via copy & paste use the Unix command
unexpand to translate the spaces into tabs.

{{{
unexpand --first-only - | cat >Config.in
}}}

When you paste it press CRTL+D keys to safe the file.


=== package/helloworld/Config.in ===

{{{
config BR2_PACKAGE_HELLO
	tristate "hello - The classic greeting, and a good example"
	default m if CONFIG_DEVEL
	help
	The GNU hello program produces a familiar, friendly greeting.  It
	allows non-programmers to use a classic computer science tool which
	would otherwise be unavailable to them.
	.
	Seriously, though: this is an example of how to do a Debian package.
	It is the Debian version of the GNU Project's `hello world' program
	(which is itself an example for the GNU Project).
}}}


=== package/helloworld/Makefile ===

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

$(eval $(call PKG_template,HELLO,hello,$(PKG_VERSION)-$(PKG_RELEASE),$(ARCH)))

$(PKG_BUILD_DIR)/.configured: $(PKG_BUILD_DIR)/.prepared
	(cd $(PKG_BUILD_DIR); \
$(TARGET_CONFIGURE_OPTS) \
		CFLAGS="$(TARGET_CFLAGS)" \
		./configure \
		--target=$(GNU_TARGET_NAME) \
		--host=$(GNU_TARGET_NAME) \
		--build=$(GNU_HOST_NAME) \
		--prefix=/usr \
		--without-libiconv-prefix \
		--without-libintl-prefix \
		\
		--disable-nls \
	);
	touch $@

$(PKG_BUILD_DIR)/.built:
	rm -rf $(PKG_INSTALL_DIR)
	mkdir -p $(PKG_INSTALL_DIR)/usr/bin
	$(MAKE) -C $(PKG_BUILD_DIR)/src \
		$(TARGET_CONFIGURE_OPTS) \
		prefix="$(PKG_INSTALL_DIR)/usr"
	cp -fpR $(PKG_BUILD_DIR)/src/hello $(PKG_INSTALL_DIR)/usr/bin
	touch $@

$(IPKG_HELLO):
	install -d -m0755 $(IDIR_HELLO)/usr/bin
	cp -fpR $(PKG_INSTALL_DIR)/usr/bin/hello $(IDIR_HELLO)/usr/bin
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
Maintainer: Name <maintainer@example.com>
Source: http://ftp.debian.org/debian/pool/main/h/hello
Description: The classic greeting, and a good example
	The GNU hello program produces a familiar, friendly greeting.  It
	allows non-programmers to use a classic computer science tool which
	would otherwise be unavailable to them.
	.
	Seriously, though: this is an example of how to do a Debian package.
	It is the Debian version of the GNU Project's `hello world' program
	(which is itself an example for the GNU Project).
}}}


=== package/helloworld/patches/100-hello.patch ===

This example will also work without the Debian patch. So you can skip this point.

{{{
cd patches
wget http://ftp.debian.org/debian/pool/main/h/hello/hello_2.1.1-4.diff.gz
gunzip hello_2.1.1-4.diff.gz
mv hello_2.1.1-4.diff 100-hello.patch
cd ..
}}}


== Compiling ==

The make command below compiles every package that you've created in the
package directory.

{{{
cd ~/OpenWrt-SDK-Linux-i686-1
make clean && make compile
}}}


When the compiling is finished you've a ready to use ipk package for OpenWrt
in the ~/OpenWrt-SDK-Linux-i686-1/bin/packages directory

{{{
cd bin/packages; ls -al hello_2.1.1-1_mipsel.ipk
-rw-r--r--  1 openwrt-dev openwrt-dev 3976 Sep 14 13:03 hello_2.1.1-1_mipsel.ipk
}}}


= Contribute your new ported program =

When you like you can contribute your program/package to the OpenWrt community.
It may be included in further versions of OpenWrt.

Todo this create a tarball from your package directory, and send the tarball
to openwrt-devel@openwrt.org .

{{{
cd ~/OpenWrt-SDK-Linux-i686-1/package
tar cvjf ~/OpenWrt-SDK-Linux-i686-1/helloworld-sdk.tar.bz2 helloworld
cd ..
}}}
