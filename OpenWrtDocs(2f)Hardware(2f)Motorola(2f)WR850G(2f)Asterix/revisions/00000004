= Asterisk on the Motorola WR850G =

From the !OpenWrt Forum. [[BR]]
http://forum.openwrt.org/viewtopic.php?id=5476

4 simple steps big_smile

1)
I think I used openwrt-wrt54g-squashfs.bin (squashfs of your right model and version)

2) (WARNING: THE FOLLOWING PACKAGE LIST HAS VARYING BASE PACKAGES DEPENDING RC4, RC5,.. ) [[BR]]
root@OpenWrt:~# '''ipkg list_installed''' [[BR]]
asterisk - 1.0.10-1 - An open source PBX [[BR]]
base-files - 8 - OpenWrt filesystem structure and scripts [[BR]]
base-files-brcm - 2 - Board/architecture specific files [[BR]]
bridge - 1.0.6-1 - Ethernet bridging tools [[BR]]
busybox - 1.00-3 - Core utilities for embedded Linux systems [[BR]]
dnsmasq - 2.27-1 - A lightweight DNS and DHCP server [[BR]]
dropbear - 0.48.1-1 - a small SSH 2 server/client designed for small memory environments. [[BR]]
ez-ipupdate - 3.0.11b8-2 - a client for dynamic DNS services [[BR]]
haserl - 0.8.0-1 - a CGI wrapper to embed shell scripts in HTML documents [[BR]]
ip - 2.6.11-050330-1 - iproute2 routing control utility [[BR]]
ipkg - 0.99.149-2 - lightweight package management system [[BR]]
iptables - 1.3.3-2 - The netfilter firewalling software for IPv4 [[BR]]
iwlib - 28.pre7-1 - Library for setting up WiFi cards using the Wireless Extension [[BR]]
kernel - 2.4.30-brcm-3 - [[BR]]
kmod-brcm-wl - 2.4.30-brcm-3 - Proprietary driver for Broadcom Wireless chipsets [[BR]]
kmod-diag - 2.4.30-brcm-3 - Driver for Router LEDs and Buttons [[BR]]
kmod-ppp - 2.4.30-brcm-3 - PPP support [[BR]]
kmod-pppoe - 2.4.30-brcm-3 - PPP over Ethernet support [[BR]]
kmod-sched - 2.4.30-brcm-3 - Kernel schedulers for IP traffic [[BR]]
kmod-switch - 2.4.30-brcm-1 - switch driver for robo/admtek switch [[BR]]
kmod-wlcompat - 2.4.30-brcm-3 - Compatibility module for using the Wireless Extension with broadcom's wl [[BR]]
libncurses - 5.2-7 - a terminal handling library and common terminal definitions [[BR]]
libpthread - 0.9.27-1 - POSIX threads library [[BR]]
mtd - 4 - Tool for modifying the flash chip [[BR]]
nvram - 1 - NVRAM utility and libraries for Broadcom hardware [[BR]]
ppp - 2.4.3-7 - a PPP (Point-to-Point Protocol) daemon (with MPPE/MPPC support) [[BR]]
ppp-mod-pppoe - 2.4.3-7 - a PPPoE (PPP over Ethernet) plugin for PPP [[BR]]
tc - 2.6.11-050330-1 - iproute2 traffic control utility [[BR]]
uclibc - 0.9.27-8 - Standard C library for embedded Linux systems [[BR]]
webif - 0.2-1 - A modular, extensible web interface for OpenWrt. [[BR]]
wificonf - 6 - Replacement utility for wlconf [[BR]]
wireless-tools - 28.pre7-1 - Tools for setting up WiFi cards using the Wireless Extension [[BR]]
wl - 3.90.37-1 - Proprietary Broadcom utility for setting wireless driver parameters  [[BR]]
Successfully terminated. [[BR]]


3)
For QOS script you can download this file [[BR]]
Local copies [[BR]]
 * ["/qos_cable"] [[BR]]
 * ["/qos_dsl"][[BR]]
Original Source website [[BR]]
For DHCP connection http://www.frozenmemoirs.com/S91qos_cable [[BR]]
For PPPOE connection http://www.frozenmemoirs.com/S91qos_dsl

You may need to change the "DEV=" variable in the script if required. [[BR]]
Also change "UPLINK=" to 80% of your max upload.[[BR]]
Put this script under /etc/init.d/, also chmod a+x the script[[BR]]
Make sure this script executes ./S91qos, coz it requres few modules to be loaded
 root@OpenWrt:~# '''cat /etc/modules''' [[BR]]
 wl [[BR]]
 sch_htb [[BR]]
 sch_sfq [[BR]]
 cls_u32 [[BR]]
 cls_route [[BR]]
 cls_tcindex [[BR]]
 cls_fw [[BR]]

4) And finally check your quota, Voila!!! you still have around 20% of 2MB left smile [[BR]]
root@OpenWrt:~# '''df''' [[BR]]
Filesystem           1k-blocks      Used Available Use% Mounted on [[BR]]
/dev/root                 1024      1024         0 100% /rom [[BR]]
/dev/mtdblock/4           2240      1828       412  82% / [[BR]]
none                      7172        84      7088   1% /tmp [[BR]]

Last edited by LoneShadow (2006-05-01 00:28:32)
