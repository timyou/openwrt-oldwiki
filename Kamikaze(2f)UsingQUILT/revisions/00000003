= Using QUILT to add patches (for packages) =
{{{
cd ~/trunk/
make package/busybox/{clean,prepare} V=99 QUILT=1
cd build_dir/i386/busybox-1.8.1
quilt new 530-gunzip_src_fd.patch
quilt add 530-gunzip_src_fd.patch
EDITOR=gedit quilt edit archival/libunarchive/decompress_unzip.c      # make the changes and save and exit the editor
quilt refresh
cd ~/trunk/
make package/busybox/update V=99                                       # copies the new patch to package/busybox/patches/530-gunzip_src_fd.patch
make package/busybox/{clean,compile}
}}}
== Refreshing patches ==
If you updated a !OpenWrt package and also like to refresh the patches you can also do this with quilt.

{{{
make package/<pkg_name>-{clean,refresh} V=99}}}

= Using QUILT to add Kernel patches =

{{{cd ~/trunk/
make target/linux/{clean,prepare} V=99 QUILT=1
cd build_dir/linux-ar7/linux-2.6.24.2/
quilt new patches/platform/170-cpmac-mypatch.diff
quilt add patches/platform/170-cpmac-mypatch.diff
EDITOR=gedit quilt edit drivers/net/cpmac.c
quilt refresh
cd ../../../
make target/linux/update V=99

cat target/linux/ar7/patches-2.6.24/170-cpmac-mypatch.diff
Index: linux-2.6.24.2/drivers/net/cpmac.c
===================================================================
--- linux-2.6.24.2.orig/drivers/net/cpmac.c     2008-04-18 17:05:12.000000000 +0200
+++ linux-2.6.24.2/drivers/net/cpmac.c  2008-04-18 17:05:28.000000000 +0200
 -1,5 +1,5 @@
 /*
- * Copyright (C) 2006, 2007 Eugene Konev
+ * Copyright (C) 2006, 2007 Eugene Konev - TEST with QUILT
  *
  * This program is free software; you can redistribute it and/or modify
  * it under the terms of the GNU General Public License as published by


make target/linux/{clean,compile} V=99}}}
