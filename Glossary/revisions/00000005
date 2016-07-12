## Please don't attempt to explain every NVRAM setting on this page -- use OpenWrtNVRAM


[[TableOfContents]]


===== Afterburner (aka SpeedBooster) =====

The Broadcom enhancement that claims faster
802.11 speeds. On most routers it breaks WDS. It's unsupported in !OpenWrt.


===== failsafe =====

A special recovery mode in !OpenWrt triggered by holding the reset button for ~2
seconds immediately after the DMZ LED lights up during boot. While in failsafe,
!OpenWrt will ignore files in the JFFS2 partition and will override the LAN IP address with
{{{192.168.1.1}}}.


===== firstboot =====

A script which initializes the JFFS2 partition. It is normally run automatically
the first time !OpenWrt is booted, but can be run manually to reset the JFFS2 partition.


===== JFFS2 =====

[wiki:WikiPedia:JFFS2 The Journalling Flash File System (version 2)], a writable file system for use in flash memory devices such as routers.  It is used as the root partition in !OpenWrt.


===== NVRAM =====

[wiki:WikiPedia:NVRAM Non-Volatile RAM].
A partition, occupying the last 64K of the flash chip, used for storing various configuration information in a `name=value` format.  See [:OpenWrtNVRAM] for a list of variable names that !OpenWrt uses.

Also can refer to the `nvram` utility, which is used to manage NVRAM, such as to get/set/unset variables.


===== SquashFS =====

[wiki:WikiPedia:SquashFS The Squash File System], a compressed, read-only filesystem for Linux, mounted as {{{/rom}}} in `-squashfs` builds of !OpenWrt.


===== Wrt =====

Generic term used to describe the !OpenWrt-compatible routers.

Wrt is also the name of the bot used on the IRC channel to display news.
