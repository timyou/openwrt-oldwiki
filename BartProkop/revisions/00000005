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

 
=== Implementation ===
==== Hardware and firmware upgrade ====

I decided to purchase Linksys WRT54GL v 1.1 model. Its serial number is CL7B1FB39805. The first step was replace vendor firmware with OpenWRT. It is very trivial task. You had to download a firmware from [[http://downloads.openwrt.org/whiterussian/newest/default/]]. In my case it was file named openwrt-wrt54g-squashfs.bin. Before flashing your device I strongly recommend to compare MD5SUMs of downloaded file to those avaiable at download pages. I used vendor firmware for upgrading the firmware. After flashing, the device will boot. Please then use telnet (not ssh as it will not work) to log into your embeded device and set root password. Setting root password allows you to log in via SSH. The command to issue are:

{{{
telnet 192.168.1.1 (from your PC of course, log in as root with empty password)
passwd (after it you type and re-type your root password)
reboot (to restart device)
}}}



...

----
CategoryHomepage
