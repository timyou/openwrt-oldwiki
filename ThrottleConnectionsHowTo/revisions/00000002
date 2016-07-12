This page describes how to throttle incoming connections. (Updated to White Russian 0.9 on 2007-04-23)

You might want to do this if you are running a server on your OpenWRT box which is open to the internet. For example, if you have a SSH server you will find that your syslog is filled with this type of behaviour:

{{{
12:45:40 dropbear[9840]: bad password attempt for 'root' from 212.180.4.152:36250
12:45:41 dropbear[9840]: exit before auth (user 'root', 1 fails): Disconnect received
12:45:41 dropbear[9843]: Child connection from 212.180.4.152:36444
12:45:44 dropbear[9843]: bad password attempt for 'root' from 212.180.4.152:36444
12:45:45 dropbear[9843]: exit before auth (user 'root', 1 fails): Disconnect received
12:45:45 dropbear[9844]: Child connection from 212.180.4.152:36636}}}
Which is kind of annoying.

Here's how to use [http://snowman.net/projects/ipt_recent/ mod_recent] to restrict incoming connections to a certain number within a certain time. The example below assumes you want to restrict incoming SSH connections to 5 connections per 180 seconds.
This document is based on the information of the document ["OpenWrtDocs/IPTables"] and the FAQs at http://netfilter.org/.

Firstly, install the kernel packages. You need:

{{{
# ipkg install kmod-ipt-extra
# ipkg install iptables-mod-extra}}}
The module "ipt_recent" must be loaded at every startup, so make sure that the line {{{ipt_recent}}} is in {{{/etc/modules}}}. Otherwise add it via

{{{
# echo "ipt_recent" >> /etc/modules
}}}
To start it manually without rebooting use

{{{
# insmod ipt_recent.o
}}}
Now add the appropriate rules to the file {{{/etc/firewall.user}}}. Modify your existing rules for SSH connections. Ensure that the new filter rules replace the existing rule to ACCEPT connections.

{{{
### SSH (Dropbear running on port 22)
## SSH: Rules for new incoming connections on tcp-22
iptables -t nat -A prerouting_wan -p tcp --dport 22  -m state --state NEW \
  -m recent --name ATTACKER_SSH --rsource --update --seconds 180 --hitcount 5 -j DROP
iptables -t nat -A prerouting_wan -p tcp --dport 22  -m state --state NEW \
  -m recent --name ATTACKER_SSH --rsource --set
## SSH
iptables        -A input_wan      -p tcp --dport 22  -m state --state NEW -j ACCEPT}}}

Test it by logging in 5 times yourself:

{{{
~ $ ssh wrt54gs
BusyBox v1.00 (2005.09.14-15:55+0000) Built-in shell (ash)
Enter 'help' for a list of built-in commands.
  _______                     ________        __
 |       |.-----.-----.-----.|  |  |  |.----.|  |_
 |   -   ||  _  |  -__|     ||  |  |  ||   _||   _|
 |_______||   __|_____|__|__||________||__|  |____|
          |__| W I R E L E S S   F R E E D O M
 WHITE RUSSIAN (RC3) -------------------------------
  * 2 oz Vodka   Mix the Vodka and Kahlua together
  * 1 oz Kahlua  over ice, then float the cream or
  * 1/2oz cream  milk on the top.
 ---------------------------------------------------
root@OpenWrt:~# ^D
Connection to wrt54gs closed.
}}}
[... four more...]

{{{
~ $ ssh wrt54gs
[banner elided]
root@OpenWrt:~# ^D
Connection to wrt54gs closed.
~ $ ssh wrt54gs
ssh: connect to host wrt54gs port 22: Connection timed out
~ $}}}

Also have a look at [http://forum.openwrt.org/viewtopic.php?id=7493 this forum thread] where the use of ipt_recent is discussed. It also provides an example how to access SSH via a non-standard port (e.g. 443 for restrictive firewalls) although SSH is still running on the standard port 22.
