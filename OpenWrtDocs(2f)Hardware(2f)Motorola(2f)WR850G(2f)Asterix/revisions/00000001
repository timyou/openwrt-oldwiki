= Asterix on the Motorola WR850G =

From the OpenWrt Forum.
http://forum.openwrt.org/viewtopic.php?id=5476

4 simple steps big_smile

1)
I think I used openwrt-wrt54g-squashfs.bin (squashfs of your right model and version)

2) (WARNING: THE FOLLOWING PACKAGE LIST HAS VARYING BASE PACKAGES DEPENDING RC4, RC5,.. )
root@OpenWrt:~# ipkg list_installed
asterisk - 1.0.10-1 - An open source PBX
base-files - 8 - OpenWrt filesystem structure and scripts
base-files-brcm - 2 - Board/architecture specific files
bridge - 1.0.6-1 - Ethernet bridging tools
busybox - 1.00-3 - Core utilities for embedded Linux systems
dnsmasq - 2.27-1 - A lightweight DNS and DHCP server
dropbear - 0.48.1-1 - a small SSH 2 server/client designed for small memory environments.
ez-ipupdate - 3.0.11b8-2 - a client for dynamic DNS services
haserl - 0.8.0-1 - a CGI wrapper to embed shell scripts in HTML documents
ip - 2.6.11-050330-1 - iproute2 routing control utility
ipkg - 0.99.149-2 - lightweight package management system
iptables - 1.3.3-2 - The netfilter firewalling software for IPv4
iwlib - 28.pre7-1 - Library for setting up WiFi cards using the Wireless Extension
kernel - 2.4.30-brcm-3 -
kmod-brcm-wl - 2.4.30-brcm-3 - Proprietary driver for Broadcom Wireless chipsets
kmod-diag - 2.4.30-brcm-3 - Driver for Router LEDs and Buttons
kmod-ppp - 2.4.30-brcm-3 - PPP support
kmod-pppoe - 2.4.30-brcm-3 - PPP over Ethernet support
kmod-sched - 2.4.30-brcm-3 - Kernel schedulers for IP traffic
kmod-switch - 2.4.30-brcm-1 - switch driver for robo/admtek switch
kmod-wlcompat - 2.4.30-brcm-3 - Compatibility module for using the Wireless Extension with broadcom's wl
libncurses - 5.2-7 - a terminal handling library and common terminal definitions
libpthread - 0.9.27-1 - POSIX threads library
mtd - 4 - Tool for modifying the flash chip
nvram - 1 - NVRAM utility and libraries for Broadcom hardware
ppp - 2.4.3-7 - a PPP (Point-to-Point Protocol) daemon (with MPPE/MPPC support)
ppp-mod-pppoe - 2.4.3-7 - a PPPoE (PPP over Ethernet) plugin for PPP
tc - 2.6.11-050330-1 - iproute2 traffic control utility
uclibc - 0.9.27-8 - Standard C library for embedded Linux systems
webif - 0.2-1 - A modular, extensible web interface for OpenWrt.
wificonf - 6 - Replacement utility for wlconf
wireless-tools - 28.pre7-1 - Tools for setting up WiFi cards using the Wireless Extension
wl - 3.90.37-1 - Proprietary Broadcom utility for setting wireless driver parameters
Successfully terminated.


3)
For QOS script you can download this file from my website
For DHCP connection
wget http://www.frozenmemoirs.com/S91qos_cable

OR for PPPOE connection
wget http://www.frozenmemoirs.com/S91qos_dsl

You may need to change the "DEV=" variable in the script if required. Also change "UPLINK=" to 80% of your max upload.

Put this script under /etc/init.d/, also chmod a+x the script

Make sure this script executes ./S91qos, coz it requres few modules to be loaded

root@OpenWrt:~# cat /etc/modules
wl
sch_htb
sch_sfq
cls_u32
cls_route
cls_tcindex
cls_fw


4) And finally check your quota, Voila!!! you still have around 20% of 2MB left smile
root@OpenWrt:~# df
Filesystem           1k-blocks      Used Available Use% Mounted on
/dev/root                 1024      1024         0 100% /rom
/dev/mtdblock/4           2240      1828       412  82% /
none                      7172        84      7088   1% /tmp
root@OpenWrt:~#

Last edited by LoneShadow (2006-05-01 00:28:32)
