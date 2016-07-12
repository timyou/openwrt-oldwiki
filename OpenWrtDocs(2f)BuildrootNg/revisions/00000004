= Buildroot-ng =
[mbm]'s forum post: http://forum.openwrt.org/viewtopic.php?pid=31794#p31794

[["Buildroot"]-ng has been remerged with kamikaze]

== Prerequisites ==
Other than svn and make, you will be notified of any missing packages or libraries.

If you get "ImportError: No module named distutils.core" when running make you need to install the python-devel package for you distribution.

Note: make sure your system clock is set correctly.

  * svn
  * make
  * ...

== Obtaining Buildroot-ng ==
svn co https://svn.openwrt.org/openwrt/branches/buildroot-ng

== Configuring ==
Configuration is done through a curses interface similar to the Linux make menuconfig.  This interface allows selection of target plaform (BRCM, AR7, x86), desired kernel modules, and desired packages.

{{{
make menuconfig
}}}

== Building ==
{{{
make
}}}

== Installing OpenWRT ==
Files will be in ./bin.  Follow the instructions in OpenWrtDocs/Installing to flash your router.

== Building your own Binaries ==

== Tracking Progress ==
The OpenWRT developers have a web interface for users to track the progress and modifications to branches,  http://dev.openwrt.org/
