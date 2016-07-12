The objective is to configure a box that serve as an imap server of all your mails.

So we need the following tools
 * fetchmail to get your mails from the outside accounts
 * procmail to deliver it to the right recipient ad eventually process the messages
 * dovecot to configure an imap server

----

As we need to have the ssl support in fetchmail (to be able to connect to gmail for example) we need to recompile it as the version you find the repositories doesn't support ssl.

So you have to download the build environment

{{{
mkdir ~/src
cd ~/src
svn co https://svn.openwrt.org/openwrt/tags/kamikaze_7.09
svn co https://svn.openwrt.org/openwrt/packages/
}}}

Now move in '''./packages/mail''' and do the following:

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

PKG_NAME:=fetchmail
PKG_VERSION:=6.3.8
PKG_RELEASE:=1

PKG_SOURCE:=$(PKG_NAME)-$(PKG_VERSION).tar.bz2
PKG_SOURCE_URL:=http://download.berlios.de/fetchmail/
PKG_MD5SUM:=66b97500b0a1e3c0916b3b5314f597f5

include $(INCLUDE_DIR)/package.mk

define Package/fetchmail
  SECTION:=mail
  CATEGORY:=Mail
  TITLE:=Remote mail retriever with ssl support
  URL:=http://fetchmail.berlios.de/
  DEPENDS+= +libopenssl
endef

define Package/fetchmail/description
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

define Package/fetchmail/install
	$(INSTALL_DIR) $(1)/usr/bin
	$(INSTALL_BIN) $(PKG_INSTALL_DIR)/usr/bin/fetchmail $(1)/usr/bin/
endef

$(eval $(call BuildPackage,fetchmail))
}}}

Now create the file '''fetchmail-ssl/patches/dn_skipname.diff''' with the following content
(the diff file come from ["http://forum.openwrt.org/viewtopic.php?id=10793"]):

{{{
diff -U 3 -Br fetchmail-6.3.8.org/mxget.c fetchmail-6.3.8/mxget.c
--- fetchmail-6.3.8.orig/mxget.c        2007-12-01 18:16:11.000000000 +0100
+++ fetchmail-6.3.8/mxget.c     2007-12-01 18:16:59.000000000 +0100
@@ -6,6 +6,7 @@
  */

 #include "config.h"
+#include <errno.h>
 #include <stdio.h>
 #ifdef HAVE_RES_SEARCH
 #include <string.h>
@@ -51,6 +52,54 @@
 #define        INT16SZ         2               /* for systems without 16-bit ints */
 #endif

+/* Ripped from glibc 2.4 sources. */
+
+/*
+ * ns_name_skip(ptrptr, eom)
+ *      Advance *ptrptr to skip over the compressed name it points at.
+ * return:
+ *      0 on success, -1 (with errno set) on failure.
+ */
+int ns_name_skip(const u_char **ptrptr, const u_char *eom)
+{
+        const u_char *cp;
+        u_int n;
+
+        cp = *ptrptr;
+        while (cp < eom && (n = *cp++) != 0)
+        {
+                /* Check for indirection. */
+                switch (n & NS_CMPRSFLGS) {
+                case 0:                 /* normal case, n == len */
+                        cp += n;
+                        continue;
+                case NS_CMPRSFLGS:      /* indirection */
+                        cp++;
+                        break;
+                default:                /* illegal type */
+                        errno = EMSGSIZE;
+                        return (-1);
+                }
+                break;
+        }
+        if (cp > eom)
+        {
+                errno = EMSGSIZE;
+                return (-1);
+        }
+        *ptrptr = cp;
+        return (0);
+}
+
+int dn_skipname(const u_char *ptr, const u_char *eom)
+{
+        const u_char *saveptr = ptr;
+
+        if(ns_name_skip(&ptr, eom) == -1)
+                return (-1);
+        return (ptr - saveptr);
+}
+
 /* minimum possible size of MX record in packet */
  #define MIN_MX_SIZE    8       /* corresp to "a.com 0" w/ terminating space */
}}}

Then move in '''~/src/kamikaze_7.09/package''' and create the following link:

{{{
ln -s ~/src/packages/mail/fetchmail-ssl fetchmail-ssl
}}}

Now from '''~/src/kamikaze_7.09''' execute:

{{{
make menuconfig
}}}

and select from the '''Mail''' menu '''fetchmail''' then excute:

{{{
make package/fetchmail-compile
}}}

Now in '''~/src/kamikaze_7.09/bin/packages''' you'll find the fetchmail package with all it's dependencies:

{{{
fetchmail_6.3.8-1_mipsel.ipk
libopenssl_0.9.8e-1_mipsel.ipk
zlib_1.2.3-4_mipsel.ipk
}}}

'''TO BE CONTINUED'''
----
