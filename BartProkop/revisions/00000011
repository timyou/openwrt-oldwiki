##master-page:HomepageTemplate
#format wiki
== Bart Prokop ==

Email: [[MailTo(bart AT SPAMFREE tt-soft DOT com)]]
Web: [[(http://bart.prokop.name)]
All coments, amedments, corrections are warmly welcome.

Real world examples.

I created this page to contribute to this project by step by step describing Open WRT instalations running in real word. I created those instalations mostly to implement advanced router features. My intention is to provide step by step log of commands and settings necessary to achieve certain configuration.

== Multi subnet small IT company router ==
=== Router requested features ===
This is the very first advanced configuration with Open WRT I want to describe. The requirements were as follow:
 1. The embeded device shall provide Internet access to all conected computers with different policy for some groups of users.
 2. The embeded device will replace the existing routing capabilities of Linux server. I do not want to route via Linux server anymore as it has many many other things to do and is under haavy reconfiguration process.
 3. List of features on embeded devices:
  * service MORE than one separate LAN conected to embeded device
  * slave DNS server (to existing Linux server)
  * PPTP server (take this feature from Linux server)
  * QoS
 4.

==== Network topology ====
The ISP providea a DLS connection terminated by SpeedStream modem. We are provided with 5 usable IP addresses (Mask of 255.255.255.248):
 * 80.55.248.80 - net address
 * 80.55.248.81 - ADSL modem IP address
 * 80.55.248.82 - free
 * 80.55.248.83 - free (we will install our OpenWRT router here)
 * 80.55.248.84 - free
 * 80.55.248.85 - Linux company server
 * 80.55.248.86 - free
 * 80.55.248.87 - broadcast address
 
=== Implementation ===
==== Hardware and firmware upgrade ====
I decided to purchase Linksys WRT54GL v 1.1 model. Its serial number is CL7B1FB39805. The first step was replace vendor firmware with OpenWRT. It is very trivial task. You had to download a firmware from [[http://downloads.openwrt.org/whiterussian/newest/default/]]. In my case it was file named openwrt-wrt54g-squashfs.bin. Before flashing your device I strongly recommend to compare MD5SUMs of downloaded file to those avaiable at download pages. I used vendor firmware for upgrading the firmware. After flashing, the device will boot. Please then use telnet (not ssh as it will not work) to log into your embeded device and set root password. Setting root password allows you to log in via SSH. The command to issue are:

{{{
telnet 192.168.1.1 (from your PC of course, log in as root with empty password)
passwd (after it you type and re-type your root password)
reboot (to restart device)
}}}

At this point you should be able to ssh to your router and be able to enjoy embeded linux. I also decided to clean NVRAM, as my device could have strange settings from previous firmware. To do so just type ('''please double check if it is SAFE with your hardware!!!'''):
{{{
mtd -r erase nvram
}}}
In my case it reduced variable count to 30% of this what I had originally set with vendor firmware. After ersing nvram, I strongly recommend to set up a boot_wait to on. It will really help if I cause the router to stop working by misconfiguring it.
{{{
nvram set boot_wait=on
nvram commit
}}}
==== Basic network settings ====
I changed SSID to reflect company domain:
{{{
nvram set wl0_ssid="www.tt-soft.com"
nvram commit
}}}
We need to configure our WAN port to 80.55.248.83. As we know our static IP, configuration is very simple:
{{{
nvram set wan_proto=static
nvram set wan_ipaddr=80.55.248.83
nvram set wan_netmask=255.255.255.248
nvram set wan_gateway=80.55.248.81
nvram set wan_dns=80.55.248.85
nvram commit
}}}
Now lets enable SSH on WAN port. It is disabled by default and we need it open as we want external access to our device. It is very easy. Just edit a file /etc/firewall.user, locate lines which looks like those below and uncomment last two lines:
{{{
### Open port to WAN
## -- This allows port 22 to be answered by (dropbear on) the router
# iptables -t nat -A prerouting_wan -p tcp --dport 22 -j ACCEPT
# iptables        -A input_wan      -p tcp --dport 22 -j ACCEPT
}}}

...

----
CategoryHomepage
