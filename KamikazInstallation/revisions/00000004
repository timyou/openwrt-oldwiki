''This is a work in progress. it is being ported over from the excellent post http://forum.openwrt.org/viewtopic.php?id=11451 posted by ''[http://forum.openwrt.org/profile.php?id=5640 GLP]. Expected done date of this page is 3/8/08

'''Installation on a WRT54G '''The most common installation

Getting Kamikaze installed is not that difficult, and it only takes a little editing to make it perform basic duties as home router. The following will hopefully be able to help a new-commer to OpenWrt Kamikaze with the setup of a basic functional system. This howto is based on the use of a Linksys WRT54G version 3.1, which is fully supported by OpenWrt Kamikaze - if you have another device please check [http://toh.openwrt.org/ http://toh.openwrt.org] to see if it is supported. It is assumend that the WRT has either the original firmware installed, or as in this case an older version of OpenWrt White Russian with the original OpenWrt webif. The following process consists of three parts:

1. Installation

2. Gettting access

3. Configuration

######################
1. Installation There are several ways to install Kamikaze, but this will only cover the very basic procedure based on using the firmware upgrade function of the webinterface (webif). Thsi means in praxis, that all which is needed to be done is to download the precompiled Kamikaze image and then simply upgrade the device. Kamikaze supports a rather large number of different platforms (https://dev.openwrt.org/wiki/platforms) so it is required to download the correct image from http://downloads.openwrt.org/kamikaze/7.06/ In the case of the WRT54G the correct image recides in the brcm-2.4/ directory - in this directory the correct file to download would have the name: openwrt-wrt54g-2.4-squashfs.bin It should be noted that there are two different brcm directories (brcm-2.4/ and brcm47xx-2.6) in the Kamikaze directory - these refer to images based on either 2.4 or 2.6 kernel. But, the 2.6 kernel does presently not support broadcom wireless, and installing the 2.6 image would leave the wireless interface of the WRT54G non-functional. When the correct image is downloaded, then it is just needed to login to the router (enter the ip-adress of your router in a browser and press return) followed by pointing the firmware upgrade function at the correct image and the pressing of the 'upgrade button'. *It is always recommended to use a cable connection between router and pc/laptop. The wireless connection can fluctuate and this might result in loss of data during the transfer, which again would leave the router with a non-functional system after reboot.

######################
2. Getting access Getting the first access to the new Kamikaze system requires that you login to the router via telnet (http://en.wikipedia.org/wiki/Telnet) and set a new login password (on windows you would need to install something like Putty (http://www.chiark.greenend.org.uk/~sgtatham/putty/). The default ip-adress of the router is 192.168.1.1, so you would have to check that your pc/laptop has acquired a correct corresponding ip-adress from the router (which should be the case if you'r still connected via ethernet cable). If the ip-adress is not correct, then try to force a re-new of the ip-adress. The complete login and password setting procedure looks like this -->

----
 . telnet 192.168.1.1 Trying 192.168.1.1... Connected to 192.168.1.1. Escape character is '^]'.
 . === IMPORTANT ============================
  . Use 'passwd' to set your login password this will disable telnet and enable SSH
----------
 . BusyBox v1.4.2 (2007-06-01 15:48:27 CEST) Built-in shell (ash) Enter 'help' for a list of built-in commands.
  . |__| W I R E L E S S   F R E E D O M __
 KAMIKAZE (7.06)
----------
 * 10 oz Vodka       Shake well with ice and strain
 * 10 oz Triple sec  mixture into 10 shot glasses.
 * 10 oz lime juice  Salute!
 .
----------
 . root@OpenWrt:/# passwd Changing password for root New password: Retype password: Password for root changed by root root@OpenWrt:/#
----
 . Hereafter it is needed to logout, to close the telnet connection (which is insecure), and instead use the ssh service for the future (http://en.wikipedia.org/wiki/Secure_Shell). Ths is done like this -->
----
 . root@OpenWrt:/# exit Connection closed by foreign host. ssh root@192.168.1.1 The authenticity of host '192.168.1.1 (192.168.1.1)' can't be established. RSA key fingerprint is 43:6d:51:fc:83:f0:c9:67:67:ac:26:f4:7f:bb:b1:8f. Are you sure you want to continue connecting (yes/no)? yes Warning: Permanently added '192.168.1.1' (RSA) to the list of known hosts. root@192.168.1.1 's password: BusyBox v1.4.2 (2007-06-01 15:48:27 CEST) Built-in shell (ash) Enter 'help' for a list of built-in commands.
 . _____                     ________        __ __
 . |       |.
-----
 .
-----
 .
-----
 . |  |  |  |.
----
 . |  |_
 . |   -   ||  _  |  -|     ||  |  |  ||   _||   _| |_______||   __|_____|__|__||________||__|  |____| __
  . __|__| W I R E L E S S   F R E E D O M
 KAMIKAZE (7.06)
----------
 * 10 oz Vodka       Shake well with ice and strain
 * 10 oz Triple sec  mixture into 10 shot glasses.
 * 10 oz lime juice  Salute!
 .
----------
 . root@OpenWrt:~#
----
 . The first time you login to the router the ssh service asks you if the 'fingerprint' of the router should be added to the list of known hosts on your local system. The list of known hosts is a small text file, and should you encounter problems with 'fingerprints' belonging to devices with similar ip-adresses (like: 192.168.1.1) then its a simple task to solve login problems with editing the file by simply removing the entry which results in problems.
######################
3. Configuration The default configuration of Kamikaze differs at least in two significant aspects: 1. There is no build-in webinterface. 2. The wireless interface is disabled. This means that the user has to learn how to edit "manually" and in this way enable the wireless interface. The files which needs to be edited recide in the /etc/config directory - and they are named 'network' and 'wireless' The following will first show how to find the correct files on the Kamikaze system and then how to edit the same files (beginning with login to the system and showing the steps needed + what the content of the different directories are) -->

----
 . ssh root@192.168.33.1 root@192.168.33.1 's password: BusyBox v1.4.2 (2007-06-01 15:48:27 CEST) Built-in shell (ash) Enter 'help' for a list of built-in commands.
 . _______                     ________        __
 . |       |.
-----
 .
-----
 .
-----
 . |  |  |  |.
----
 . |  |_
 . |   -   ||  _  |  -__|     ||  |  |  ||   _||   _| |_______||   __|_____|__|__||________||__|  |____|
  . |__| W I R E L E S S   F R E E D O M __
 KAMIKAZE (7.06)
----------
 * 10 oz Vodka       Shake well with ice and strain
 * 10 oz Triple sec  mixture into 10 shot glasses.
 * 10 oz lime juice  Salute!
 .
----------
 . root@OpenWrt:~# root@OpenWrt:~# pwd /tmp root@OpenWrt:~# ls dhcp.leases       log               resolv.conf       run lock              preinit.log       resolv.conf.auto  spool
----
 . As you can see the default "login position" is in the /tmp directory of the system - the files which needs to be edited are, as mentioned above, in /etc/config so you will need to change directory -->
----
 . root@OpenWrt:~# cd /etc/ root@OpenWrt:/etc# ls banner           firewall.user    inittab          passwd-          rc.common config           functions.sh     ipkg.conf        ppp              rc.d crontabs         group            modules.d        preinit          resolv.conf diag.sh          hosts            mtab             preinit.arch     shells dnsmasq.conf     hotplug.d        openwrt_version  profile          sysctl.conf dropbear         init.d           passwd           protocols        uci-defaults root@OpenWrt:/etc# cd config/ root@OpenWrt:/etc/config# ls dhcp      dropbear  firewall  network   system    wireless
----
 . The default editor on Kamikaze is 'vi'. This editor is not particular "user-friendly", and you need to know the following commands: To "open" file:                        vi <name of file> To make changes in text:        (press key) i Leaving text-change mode:     (press key) esc To save and quit:                   :wq If you just need to look at the content of a file it is more "safe" to use 'less' with these commands: To "open" file:                        less <name of file> To "close" file:                        (press key) q The editing process shoudl then look like this -->
----
 . root@OpenWrt:/etc# cd /etc/config/ root@OpenWrt:/etc/config# ls dhcp      dropbear  firewall  network   system    wireless root@OpenWrt:/etc/config# vi wireless config wifi-device  wl0
 . option type     broadcom option channel  5
# disable radio to prevent an open ap after reflashing:

 . option disabled 1
config wifi-iface

 . option device   wl0 option network  lan option mode     ap
 option ssid     OpenWrt option hidden   0 option encryption none
~ ~ - wireless 1/14 7%

----
 . As it says in the file it is needed to comment (add a '#') the line: option disabled 1 And, when your at it, it is easy to change the wireless ssid to something more personal than OpenWrt, by editing the line: option ssid   OpenWrt
-----
 . (here you press 'i' and change the file to something like the following) config wifi-device  wl0
 . option type     broadcom option channel  5
# disable radio to prevent an open ap after reflashing: #       option disabled 1 config wifi-iface

 . option device   wl0 option network  lan option mode     ap option ssid     Flopper option hidden   0 option encryption none
~ ~ - wireless 1/14 7% (the editing is followed by pressing the 'esc' key - and then typing the following command which will write the changes to file and quit vi) :wq

----
 . The wireless interface is now enabled and if you reboot the router and thereafter scan for active wireless networks the ssid of the router is now visible. Though the network file needs a little editing before the wireless part of the LAN is fully functional -->
----
 . root@OpenWrt:/etc/config# ls dhcp      dropbear  firewall  network   system    wireless root@OpenWrt:/etc/config# vi network
#### VLAN configuration
config switch eth0

 . option vlan0    "1 2 3 4 5*" option vlan1    "0 5"
#### Loopback configuration
config interface loopback

 . option ifname   "lo" option proto    static option ipaddr   127.0.0.1 option netmask  255.0.0.0
#### LAN configuration
config interface lan

 . option type     bridge option ifname   "eth0.0" option proto    static option ipaddr   192.168.1.1 option netmask  255.255.255.0
#### WAN configuration
config interface        wan

 . option ifname   "eth0.1" option proto    dhcp
~ ~ network

----
 . It is needed to add two additional option to the LAN configuration section of the file before everything will work as expected, it is respectively: - option gateway - option dns which needs to be added -->
----
 . (so press 'i' and change the LAN configuration section in the following way)
#### LAN configuration
config interface lan

 . option type     bridge option ifname   "eth0.0" option proto    static option ipaddr   192.168.33.1 option netmask  255.255.255.0 option gateway  192.168.1.254 option dns      192.168.1.254
(then press the 'esc' key, and the again type) :wq

----
 . To finalize this very basic installation and configuration of your new OpenWrt Kamikaze system you just need to reboot - and enjoy
References:KamikazeConfiguration
