## NOTE:
## This is not where documentation for specific packages goes.  This page documents the packaging system.
##
## Add pages documenting packages to http://wiki.openwrt.org/OpenWrtDocs/Packages/<package name>
## and add them to the CategoryPackage category
##
OpenWrtDocs [[TableOfContents]]

= Where to get packages =
== Official packages ==
The official packages for the Kamikaze release can be found here: [http://downloads.openwrt.org/kamikaze/].  Almost all packages are architecture-dependent, and some, e.g. kmods, are kernel version specific.  The linux command {{{uname -a}}} can be used to determine architecture.  ''Most'' residential gateways are mipsel (little endian MIPS).

Legacy White Russian packages are still available:
  * [http://downloads.openwrt.org/whiterussian/packages/ White Russian packages]
  * [http://downloads.openwrt.org/backports/0.9 White Russian backports]

== Third party packages ==
Third party packages are untested and unsupported by !OpenWrt, and no warranties are made about their safety or usefulness. That said, you will find most third-party packages quite fine. Please get support for third-party packages from the maintainers of those packages, not the !OpenWrt developers.  Here are some common sources:
  * [http://www.ipkg.be/ ipkg.be package tracker]
  * [http://ipkg.nslu2-linux.org/feeds/optware/ddwrt/cross/stable nslu2 "optware" package feed] (targeted at devices with external storage)
  * [:OpenWrtDocs/xwrt: X-Wrt], a third-party quasi-supported web interface package


Most are only for mipsel, and some only support mipsel Broadcom devices.

== Creating your own packages ==
To creating your own packages for !OpenWrt use the SDK, see BuildingPackagesHowTo.

== Building OpenWrt packages ==
Some packages are supported by OpenWrt, but not precompiled or distributed.

After [:OpenWrtDocs/BuildingKamikazeHowTo: building a Kamikaze image], go to the {{{packages}}} directory, typically in {{{trunk}}}.  Then check out the package.
{{{
cd packages
svn co https://svn.openwrt.org/openwrt/packages/<package name>

cd ..
make menuconfig
make
}}}

The package should now show up somewhere in {{{make menuconfig}}}.  When selecting it, press "m" to ensure it's built as a package, not built into the image.  Some packages that only allow this, e.g. br2684ctl, require hitting <space> to show up as a package.

After {{{make}}} completes, the .ipk file will be in ./bin/package/<arch>/.

= Managing packages =
The opkg utility is a lightweight package manager used to download and install !OpenWrt packages from the internet. (GNU/Linux users familiar with {{{apt-get}}} will recognise the similarities)

The firmware itself is designed to occupy as little space as possible while still providing a reasonably friendly command line interface or web administration interface. With no packages installed, !OpenWrt will configure the network interfaces, setup a basic NAT firewall, a secure shell server, a DNS forwarder and DHCP server.

||'''Command''' ||'''Description''' ||
||opkg update ||Download a list of packages available ||
||opkg list ||View the list of packages ||
||opkg install dropbear ||Install the dropbear package ||
||opkg remove dropbear ||Remove the dropbear package ||

More options can be found via {{{opkg --help}}}.

== ipkg vs. opkg ==
Older versions of OpenWrt use ipkg, while recent versions use opkg.  The latter is essentially a drop in replacement that addresses [http://lists.openmoko.org/pipermail/devel/2008-July/000496.html a number of issues].  Documentation in the OpenWrt wiki is inconsistent, so almost all references of either simply mean "the package manager on the system."

== How to install packages ==
=== opkg.conf ===
{{{opkg.conf}}} was inspired by Debian's apt.conf.  Instead of installing individual packages manually with pre-downloaded files and URLs, packages from repositories listed in {{{/etc/opkg.conf}}} can be installed with a user-friendly command.

To use the official packages, add these lines to {{{/etc/opkg.conf}}} (older versions use {{{/etc/ipkg.conf}}}:

{{{
# This depends on your release and platform.  If you're using a custom build,
# hosting the bin directory on a local webserver can be very convenient.
src kamikaze-7.09 http://downloads.openwrt.org/kamikaze/7.09/brcm-2.4/packages/

# This depends on the architecture you're using.  These packages may be a bit
# dated, but the *generally* run on both older and more recent Kamikaze builds.
src packages http://downloads.openwrt.org/kamikaze/packages/mipsel/
}}}

'''TIP:''' If you copy & paste this into your {{{/etc/ipkg.conf}}} file, make sure that you don't get a trailing space. If you do, {{{ipkg update}}} will look like it's updating but files will not be created in {{{/usr/lib/ipkg/lists}}}.

Other lines can be added to {{{/etc/opkg.conf}}}, adding a third party repository to the package set, however, this is not recommended.

After changing {{{/etc/opkg.conf}}}, run {{{opkg update}}} to get the system to recognize the new packages.

=== Installation ===
To install a package is present in a repository (usually this is the case), do
{{{
opkg install wireless-tools
}}}

To install a package from a URL or downloaded file, do
{{{
opkg install <filename> | <URL>
}}}

In both cases, opkg will attempt to resolve dependencies with packages in the repositories.  If it cannot, it will report an error, and not install any of the packages.

Missing dependencies with third-party packages are probably available from the source of the package.  To ignore dependencies, pass the {{{-force-depends}}} flag to opkg.

== Listing installed packages ==
{{{
opkg list_installed
}}}

== Removing Packages ==
{{{
opkg remove <package name listed by list_installed>
}}}

== Upgrading ==
The process for upgrading a single package is the same as installing a package: {{{opkg install}}}.

To upgrade all packages, do
{{{
opkg upgrade
}}}

This is '''not''' recommended for most users, jffs2 and ext2 users excepted.  A typical OpenWrt system stores the base system in a read-only squashfs partition.  While the upgrade process works fine, it uses far more space than a default installation as the base packages are duplicated in the base squashfs partition and the user jffs2 partition.  Instead of upgrading, upgrading OpenWrt with a reflash is recommended.

== Out of space ==
When opkg runs out of space, it usually fails to elegantly recover.  If the lock was not removed,
{{{
Collected errors:
 * Could not obtain administrative lock
}}}
it can be deleted from {{{/usr/lib/opkg/lock}}}.

Additionally, opkg doesn't remove the files it was installing.  One way to do this is get a list of the files it was installing, then delete them.
{{{
mkdir /tmp/opkg_cleanup
cd /tmp/opkg_cleanup
opkg download <package>
gunzip -c *.ipk | tar -x
gunzip -c data.tar.gz | tar -x

find .
}}}

The files other than {{{control.tar.gz}}}, {{{data.tar.gz}}}, {{{debian-binary}}}, and {{{*.ipk}}} were (or would have been) added by opkg.
== External storage ==
If you have USB storage, or install packages to a destination other than root, the shell script {{{ipkg-link}}} will create automatic symlinks to the root filesystem for those packages. See the info on {{{ipkg-link}}} on the UsbStorageHowto.

== Proxy support ==
To use opkg through a proxy, add the following to {{{/etc/opkg.conf}}}

{{{
option http_proxy http://aaa.bbb.ccc.ddd:port/
option ftp_proxy ftp://aaa.bbb.ccc.ddd:port/
}}}

these are for if you need authentication

{{{
option proxy_username xxxx
option proxy_password xxxx
}}}

If the authentication with the above options in {{{/etc/opkg.conf}}} is not working, try the following format:

{{{
option http_proxy http://username:password@aaa.bbb.ccc.ddd:port/
option ftp_proxy http://username:password@aaa.bbb.ccc.ddd:port/
}}}
