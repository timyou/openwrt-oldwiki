The objective is to configure a box that serve as an imap server of all your mails.

So we need the following tools
 * fetchmail to get your mails from the outside accounts
 * procmail to deliver it to the right recipient ad eventually process the messages
 * dovecot to configure an imap server

----

As we need to have the ssl support in fetchmail (to be able to connect to gmail for example) we need to recompile it as the version you find in kamikaze 7.09 doesn't support ssl.

So you have to download the build environment

{{{
svn co https://svn.openwrt.org/openwrt/tags/kamikaze_7.09
svn co https://svn.openwrt.org/openwrt/packages/
}}}

Now move in '''packages/mail''' and do the following:

{{{
mkdir fetchmail-ssl fetchmail-ssl/patches
}}}

then create the file '''fetchmail-ssl/Makefile''' with the following content:
{{{
#
# Copyright (C) 2006-2008 OpenWrt.org
#
# This is free software, licensed under the GNU General Public License v2.
# See /LICENSE for more information.
#
# $Id: Makefile 11014 2008-05-03 02:42:43Z nico $

include $(TOPDIR)/rules.mk

PKG_NAME:=fetchmail-ssl
PKG_VERSION:=6.3.8
PKG_RELEASE:=1

PKG_SOURCE:=$(PKG_NAME)-$(PKG_VERSION).tar.bz2
PKG_SOURCE_URL:=http://download.berlios.de/fetchmail/
PKG_MD5SUM:=66b97500b0a1e3c0916b3b5314f597f5

include $(INCLUDE_DIR)/package.mk

define Package/fetchmail-ssl
  SECTION:=mail
  CATEGORY:=Mail
  TITLE:=Remote mail retriever with ssl support
  URL:=http://fetchmail.berlios.de/
  DEPENDS+= +libopenssl
endef

define Package/fetchmail-ssl/description
 Retrieves remote mail via POP/IMAP.
 Very useful in conjunction with mutt.
endef

define Build/Configure
	$(call Build/Configure/Default, \
		--enable-fallback=procmail \
		--with-ssl="$(STAGING_DIR)/usr" \
		--without-hesiod \
		, \
		ac_cv_path_procmail=/usr/sbin/procmail \
	)
endef

define Build/Compile
	$(MAKE) -C $(PKG_BUILD_DIR) \
		DESTDIR="$(PKG_INSTALL_DIR)" \
		all install
endef

define Package/fetchmail-ssl/install
	$(INSTALL_DIR) $(1)/usr/bin
	$(INSTALL_BIN) $(PKG_INSTALL_DIR)/usr/bin/fetchmail $(1)/usr/bin/
endef

$(eval $(call BuildPackage,fetchmail-ssl))
}}}

----
