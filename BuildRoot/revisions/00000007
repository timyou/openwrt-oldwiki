BuildRoot refers to the organization of the Makefiles, scripts, etc. in the OpenWrt development environment.

Substantial improvements to the build environment were made under the [:OpenWrtDocs/BuildrootNg:BuildrootNg] fork in August and September 2006, and these were merged back into the main Kamikaze development branch in mid-October 2006. This page describes the build environment ''after'' that back-merge.

[http://downloads.openwrt.org/docs/buildroot-documentation.html | Here] is some documentation of the earlier system (used on [:OpenWrtDocs:"White Russian"] builds). The basics remain similar.

==== Introduction to the The OpenWrt build environment ====

One of the biggest challenges to getting started with embedded devices is that you just can't install a copy of Linux and expect to be able to compile a firmware. Even if you did remember to install a compiler and every development tool offered, you still wouldn't have the basic set of tools needed to produce a firmware image. The embedded device represents an entirely new hardware platform, which is incompatible with the hardware on your development machine, so in a process called cross compiling you need to produce a new compiler capable of generating code for your embedded platform, and then use it to compile a basic Linux distribution to run on your device.

The process of creating a cross compiler can be tricky, it's not something that's regularly attempted and so the there's a certain amount of mystery and black magic associated with it. In many cases when you're dealing with embedded devices you'll be provided with a binary copy of a compiler and basic libraries rather than instructions for creating your own -- it's a time saving step but at the same time often means you'll be using a rather dated set. Likewise, it's also common to be provided with a patched copy of the Linux kernel from the board or chip vendor, but this is also dated and it can be difficult to spot exactly what has been changed to make the kernel run on the embedded platform.


OpenWrt takes a different approach to building a firmware, downloading, patching and compiling everything from scratch, including the cross compiler. Or to put it in simpler terms, OpenWrt doesn't contain any executables or even sources, it's an automated system for downloading the sources, patching them to work with the given platform and compiling them correctly for the platform. What this means is that just by changing the template, you can change any step in the process.

As an example, if a new kernel is released, a simple change to one of the Makefiles will download the latest kernel, patch it to run on the embedded platform and produce a new firmware image -- there's no work to be done trying to track down an unmodified copy of the existing kernel to see what changes had been made, the patches are already provided and the process ends up almost completely transparent. This doesn't just apply to the kernel, but to anything included with OpenWrt -- It's this one simple understated concept which is what allows OpenWrt to stay on the bleeding edge with the latest compilers, latest kernels and latest applications.

==== Getting started with buildroot ====

So let's take a look at OpenWrt and see how this all works

===== prerequisites =====

Other than svn and make, you will be notified of any missing packages or libraries.

If you get {{{ImportError: No module named distutils.core}}} when running make you need to install the python-devel package for you distribution.

Note: make sure your system clock is set correctly.

===== download openwrt =====

This article refers to the kamikaze (trunk) version of OpenWrt, which can be downloaded via subversion using the following command:

svn co https://svn.openwrt.org/openwrt/trunk

Additionally, there's a trac interface on http://dev.openwrt.org/ which can be used to monitor svn commits and browse the sources.

===== The directory structure =====

There are three key directories in the base:
 . toolchain
 . target
 . package

''Toolchain'' refers to the compiler, the c library, and common tools which will be used to build the firmware image. The result of this is two new directories, toolchain_build_<arch> which is a temporary directory used for building the toolchain for a specific architecture, and staging_dir_<arch> where the resulting toolchain is installed. You won't need to do anything with the toolchain directory unless you intend to add a new version of one of the components above.

''Target'' refers to the embedded platform, this contains items which are specific to a specific embedded platform. Of particular interest here is the "target/linux" directory which is broken down by platform and contains the kernel config and patches to the kernel for a particular platform. There's also the "target/image" directory which describes how to package a firmware for a specific platform.

''Package'' is for exactly that -- packages. In an OpenWrt firmware, almost everything is an ipk, a software package which can be added to the firmware to provide new features or removed to save space.

Both the target and package steps will use the directory "build_<arch>" as a temporary directory for compiling. Additionally, anything downloaded by the toolchain, target or package steps will be placed in the "dl" directory.

==== Building openwrt ====

While the OpenWrt build environment was intended mostly for developers, it also has to be simple enough that an inexperienced end user can easily build his or her own customized firmware.

Running the command "make menuconfig" will bring up OpenWrt's configuration menu screen, through this menu you can select which platform you're targeting, which versions of the toolchain you want to use to build and what packages you want to install into the firmware image. Similar to the linux kernel config,
almost every option has three choices, y/m/n which are represented as follows:
 . `<*>` (pressing `y`) This will be included in the firmware image
 . `<m>` (pressing `m`) This will be compiled but not included (for later install)
 . `<n>` (pressing `n`) This will not be compiled

After you've finished with the menu configuration, exit and when prompted, save your configuration changes. To begin compiling the firmware, type "make". By default OpenWrt will only display a high level overview of the compile process and not each individual command.

{{{
  make[2] toolchain/install
  make[3] -C toolchain install
  make[2] target/compile
  make[3] -C target compile
  make[4] -C target/utils prepare
  ...
}}}

This makes it easier to monitor which step it's actually compiling and reduces the amount of noise caused by the compile output. To see the full output, run the command `make V=99`.

During the build process, buildroot will download all sources to the "dl" directory and will start patching and compiling them in the "build_<arch>" directory. When finished, the resulting firmware will be in the "bin" directory and packages will be in the "bin/packages" directory.

===== Creating your own packages =====

One of the things that we've attempted to do with OpenWrt's template system is make it incredibly easy to port software to OpenWrt. If you look at a typical package directory in OpenWrt you'll find two things:

 . package/<name>/Makefile
 . package/<name>/patches

The patches directory is optional and typically contains bug fixes or optimizations to reduce the size of the executable. The package makefile is the important item, provides the steps actually needed to download and compile the package.

Looking at one of the package makefiles, you'd hardly recognize it as a makefile. Through what can only be described as blatant disregard and abuse of the traditional make format, the makefile has been transformed into an object oriented template which simplifies the entire ordeal.

Here for example, is package/bridge/Makefile:

{{{
include $(TOPDIR)/rules.mk

PKG_NAME:=bridge
PKG_VERSION:=1.0.6
PKG_RELEASE:=1

PKG_BUILD_DIR:=$(BUILD_DIR)/bridge-utils-$(PKG_VERSION)
PKG_SOURCE:=bridge-utils-$(PKG_VERSION).tar.gz
PKG_SOURCE_URL:=@SF/bridge
PKG_MD5SUM:=9b7dc52656f5cbec846a7ba3299f73bd
PKG_CAT:=zcat

include $(INCLUDE_DIR)/package.mk

define Package/bridge
  SECTION:=base
  CATEGORY:=Network
  DEFAULT:=y
  TITLE:=Ethernet bridging configuration utility
  DESCRIPTION:=Ethernet bridging configuration utility\\\
    Manage ethernet bridging; a way to connect networks together to\\\
    form a larger network.
  URL:=http://bridge.sourceforge.net/
endef

define Build/Configure
  $(call Build/Configure/Default,--with-linux-headers=$(LINUX_DIR))
endef

define Package/bridge/install
        install -m0755 -d $(1)/usr/sbin
        install -m0755 $(PKG_BUILD_DIR)/brctl/brctl $(1)/usr/sbin/
endef

$(eval $(call BuildPackage,bridge))
}}}

As you can see, there's not much work to be done; everything is hidden in other makefiles and abstracted to the point where you only need to specify a few variables.

 . PKG_NAME        -The name of the package, as seen via menuconfig and ipkg
 . PKG_VERSION     -The upstream version number that we're downloading
 . PKG_RELEASE     -The version of this package Makefile
 . PKG_BUILD_DIR   -Where to compile the package
 . PKG_SOURCE      -The filename of the original sources
 . PKG_SOURCE_URL  -Where to download the sources from
 . PKG_MD5SUM      -A checksum to validate the download
 . PKG_CAT         -How to decompress the sources (zcat, bzcat, unzip)


The PKG_* variables define where to download the package from; @SF is a special keyword for downloading packages from sourceforge. The md5sum is used to verify the package was downloaded correctly and PKG_BUILD_DIR defines where to find the package after the sources are uncompressed into $(BUILD_DIR).

At the bottom of the file is where the real magic happens, "BuildPackage" is a macro setup by the earlier include statements. BuildPackage only takes one argument directly -- the name of the package to be built, in this case "bridge". All other information is taken from the define blocks. This is a way of providing a level of verbosity, it's inherently clear what the DESCRIPTION variable in Package/bridge is, which wouldn't be the case if we passed this information directly as the Nth argument to BuildPackage.

BuildPackage uses the following defines:

Package/<name>
   <name> matches the argument passed to buildroot, this describes the package
   the menuconfig and ipkg entries. Within Package/<name> you can define the
   following variables:

 .  SECTION     - The type of package (currently unused)
 .  CATEGORY    - Which menu it appears in menuconfig
 .  TITLE       - A short description of the package
 .  DESCRIPTION - A long description of the package
 .  URL         - Where to find the original software
 .  MAINTAINER  - (optional) Who to contact concerning the package
 .  DEPENDS     - (optional) Which packages must be built/installed before this package

Package/<name>/conffiles (optional)
   A list of config files installed by this package, one file per line.
 
Build/Prepare (optional)
   A set of commands to unpack and patch the sources. You may safely leave this
   undefined.

Build/Configure (optional)
   You can leave this undefined if the source doesn't use configure or has a
   normal config script, otherwise you can put your own commands here or use
   "$(call Build/Configure/Default,<args>)" as above to pass in additional
   arguments for a standard configure script.

Build/Compile (optional)
   How to compile the source; in most cases you should leave this undefined.

Package/<name>/install
   A set of commands to copy files out of the compiled source and into the ipkg
   which is represented by the $(1) directory.
   
The reason that some of the defines are prefixed by "Package/<name>" and others are simply "Build" is because of the possibility of generating multiple packages from a single source. OpenWrt works under the assumption of one source per package makefile, but you can split that source into as many packages as
desired. Since you only need to compile the sources once, there's one global set of "Build" defines, but you can add as many "Package/<name>" defines as you want by adding extra calls to BuildPackage -- see the dropbear package for an example.

After you've created your package/<name>/Makefile, the new package will automatically show in the menu the next time you run "make menuconfig" and if selected will be built automatically the next time "make" is run.

===== Creating packages for kernel modules =====

A kernel module <name> appears in the package/<name> directory, just as any other package does. The package/<name>/Makefile uses {{{KernelPackage/xxx}}} definitions in place of {{{Package/xxx}}}. For example, here is package/madwifi/Makefile:
{{{
# 
# Copyright (C) 2006 OpenWrt.org
#
# This is free software, licensed under the GNU General Public License v2.
# See /LICENSE for more information.
#
# $Id$

include $(TOPDIR)/rules.mk
include $(INCLUDE_DIR)/kernel.mk

PKG_NAME:=madwifi
PKG_VERSION:=0.9.2
PKG_RELEASE:=1

PKG_SOURCE:=$(PKG_NAME)-$(PKG_VERSION).tar.bz2
PKG_SOURCE_URL:=@SF/$(PKG_NAME)
PKG_MD5SUM:=a75baacbe07085ddc5cb28e1fb43edbb
PKG_CAT:=bzcat

PKG_BUILD_DIR:=$(KERNEL_BUILD_DIR)/$(PKG_NAME)-$(PKG_VERSION)

include $(INCLUDE_DIR)/package.mk

RATE_CONTROL:=sample

ifeq ($(ARCH),mips)
  HAL_TARGET:=mips-be-elf
endif
ifeq ($(ARCH),mipsel)
  HAL_TARGET:=mips-le-elf
endif
ifeq ($(ARCH),i386)
  HAL_TARGET:=i386-elf
endif
ifeq ($(ARCH),armeb)
  HAL_TARGET:=xscale-be-elf
endif
ifeq ($(ARCH),powerpc)
  HAL_TARGET:=powerpc-be-elf
endif

BUS:=PCI
ifneq ($(CONFIG_LINUX_2_4_AR531X),)
  BUS:=AHB
endif
ifneq ($(CONFIG_LINUX_2_6_ARUBA),)
  BUS:=PCI AHB	# no suitable HAL for AHB yet.
endif

BUS_MODULES:=
ifeq ($(findstring AHB,$(BUS)),AHB)
  BUS_MODULES+=$(PKG_BUILD_DIR)/ath/ath_ahb.$(LINUX_KMOD_SUFFIX)
endif
ifeq ($(findstring PCI,$(BUS)),PCI)
  BUS_MODULES+=$(PKG_BUILD_DIR)/ath/ath_pci.$(LINUX_KMOD_SUFFIX)
endif

MADWIFI_AUTOLOAD:= \
	wlan \
	wlan_scan_ap \
	wlan_scan_sta \
	ath_hal \
	ath_rate_$(RATE_CONTROL) \
	wlan_acl \
	wlan_ccmp \
	wlan_tkip \
	wlan_wep \
	wlan_xauth

ifeq ($(findstring AHB,$(BUS)),AHB)
	MADWIFI_AUTOLOAD += ath_ahb
endif
ifeq ($(findstring PCI,$(BUS)),PCI)
	MADWIFI_AUTOLOAD += ath_pci
endif

define KernelPackage/madwifi
  SUBMENU:=Wireless Drivers
  DEFAULT:=y if LINUX_2_6_BRCM || LINUX_2_6_ARUBA || LINUX_2_4_AR531X || LINUX_2_6_XSCALE, m if ALL
  TITLE:=Driver for Atheros wireless chipsets
  DESCRIPTION:=\
	This package contains a driver for Atheros 802.11a/b/g chipsets.
  URL:=http://madwifi.org/
  VERSION:=$(LINUX_VERSION)+$(PKG_VERSION)-$(BOARD)-$(PKG_RELEASE)
  FILES:= \
		$(PKG_BUILD_DIR)/ath/ath_hal.$(LINUX_KMOD_SUFFIX) \
		$(BUS_MODULES) \
		$(PKG_BUILD_DIR)/ath_rate/$(RATE_CONTROL)/ath_rate_$(RATE_CONTROL).$(LINUX_KMOD_SUFFIX) \
		$(PKG_BUILD_DIR)/net80211/wlan*.$(LINUX_KMOD_SUFFIX)
  AUTOLOAD:=$(call AutoLoad,50,$(MADWIFI_AUTOLOAD))
endef

MADWIFI_MAKEOPTS= -C $(PKG_BUILD_DIR) \
		PATH="$(TARGET_PATH)" \
		ARCH="$(LINUX_KARCH)" \
		CROSS_COMPILE="$(TARGET_CROSS)" \
		TARGET="$(HAL_TARGET)" \
		TOOLPREFIX="$(KERNEL_CROSS)" \
		TOOLPATH="$(KERNEL_CROSS)" \
		KERNELPATH="$(LINUX_DIR)" \
		LDOPTS=" " \
		ATH_RATE="ath_rate/$(RATE_CONTROL)" \
		DOMULTI=1

ifeq ($(findstring AHB,$(BUS)),AHB)
  define Build/Compile/ahb
	$(MAKE) $(MADWIFI_MAKEOPTS) BUS="AHB" all
  endef
endif

ifeq ($(findstring PCI,$(BUS)),PCI)
  define Build/Compile/pci
	$(MAKE) $(MADWIFI_MAKEOPTS) BUS="PCI" all
  endef
endif

define Build/Compile
	$(call Build/Compile/ahb)
	$(call Build/Compile/pci)
endef

define Build/InstallDev
	mkdir -p $(STAGING_DIR)/usr/include/madwifi
	$(CP) $(PKG_BUILD_DIR)/include $(STAGING_DIR)/usr/include/madwifi/
	mkdir -p $(STAGING_DIR)/usr/include/madwifi/net80211
	$(CP) $(PKG_BUILD_DIR)/net80211/*.h $(STAGING_DIR)/usr/include/madwifi/net80211/
endef

define Build/UninstallDev
	rm -rf	$(STAGING_DIR)/usr/include/madwifi
endef

define KernelPackage/madwifi/install
	mkdir -p $(1)/etc/init.d
	mkdir -p $(1)/lib/modules/$(LINUX_VERSION)
	mkdir -p $(1)/usr/sbin
	install -m0755 ./files/madwifi.init $(1)/etc/init.d/madwifi
	$(CP) $(PKG_BUILD_DIR)/tools/{madwifi_multi,80211debug,80211stats,athchans,athctrl,athdebug,athkey,athstats,wlanconfig} $(1)/usr/sbin/
endef

$(eval $(call KernelPackage,madwifi))
}}}

==== Troubleshooting ====

If you find your package doesn't show up in menuconfig, try the following command to see if you get the correct description:

  {{{TOPDIR=$PWD make -C package/<name> DUMP=1 V=99}}}

If you're just having trouble getting your package to compile, there's a few shortcuts you can take. Instead of waiting for make to get to your package, you can run one of the following:

  {{{make package/<name>-clean V=99}}}
  {{{make package/<name>-install V=99}}}

Another nice trick is that if the source directory under build_<arch> is newer than the package directory, it won't clobber it by unpacking the sources again. If you were working on a patch you could simply edit the sources under build_<arch>/<source> and run the install command above, when satisfied, copy the patched sources elsewhere and diff them with the unpatched sources. A warning though - if you go modify anything under package/<name> it will remove the old sources and unpack a fresh copy.

==== Final notes ====

I'm always interested to hear about people's experience with OpenWrt or answer questions about it so please don't hesitate to contact me [mbm].
