The Optware collection ports approximately 600 application packages to embedded Linux; this collection originally was part of the nslu2-linux.org 'slug' project. 

As the packages are rather large, they are best suited for a USB-capable device with external storage (see UsbStorageHowto) or SD/MMC card flash.

Before beginning installation, mount a writeable partition (flash or hard disc) as /opt - if you have a hard disc, you may also want to create a swap partition.

=== Installation for Whiterussian ===

Once this is ready, download the ipkg-opt installer using:
{{{
 wget http://pastebin.ca/raw/328107  -O - | tr -d '\r' > /tmp/optware-install.sh;
 sh /tmp/optware-install.sh
}}}

Upon successful install, you should be able to download a list of packages with:
{{{
 ipkg-opt update
}}}

The installation of individual packages from the collection is then done using a similar procedure to standard ipkg installation, but using ipkg-opt. 

The created /opt/etc/ipkg.conf contains:
{{{
 src/gz optware http://ipkg.nslu2-linux.org/feeds/optware/ddwrt/cross/stable
 dest /opt/ /
}}}

This ensures that ipkg-opt downloaded packages will be placed under /opt/bin, /opt/lib, /opt/sbin instead of in the root filesystem.

The Optware packages appear to be mostly compatible with OpenWRT Whiterussian installations, although problems occasionally will occur with differences in library files between the various distributions.

You may also want to update /etc/profile to add :/opt/bin:/opt/usr/bin:/opt/sbin to your $PATH variable.

=== Installation for Kamikaze ===
Packages designed for use under the 2.4 kernel (OpenWRT/Whiterussian) may not be compatible with newer versions of the operating environment.

There are some packages available for the current Kamikaze release here:
{{{
src Optware http://ipkg.nslu2-linux.org/feeds/openwrt/kamikaze-7.09
}}}

Note: Not all platforms are supported yet under Kamikaze.

----
CategoryPackage
