This page describes how to throttle incoming connections.

You might want to do this if you are running a server on your OpenWRT box which is open to the internet. For example, if you have an SSH server you will find that your syslog is filled with this type of behaviour:

{{{12:45:40 dropbear[9840]: bad password attempt for 'root' from 212.180.4.152:36250   
12:45:41 dropbear[9840]: exit before auth (user 'root', 1 fails): Disconnect received   
12:45:41 dropbear[9843]: Child connection from 212.180.4.152:36444   
12:45:44 dropbear[9843]: bad password attempt for 'root' from 212.180.4.152:36444   
12:45:45 dropbear[9843]: exit before auth (user 'root', 1 fails): Disconnect received   
12:45:45 dropbear[9844]: Child connection from 212.180.4.152:36636}}}

Which is kindof annoying.

Here's how to use [http://snowman.net/projects/ipt_recent/ mod_recent] to restrict incoming connections to a certain number within a certain time. In the example below I'm going to assume you want to restrict incoming SSH connections to 5 connections per 180 seconds.

Firstly, install the kernel modules. You need:

{{{# ipkg install kmod-ipt-extra
# ipkg install iptables-mod-extra}}}

Install the module:

{{{# insmod ipt_recent.o}}}

You should also arrange to have this module loaded at startup, perhaps in your `firewall.user` file.

Now add the appropriate rules to your `firewall.user` file. Modify your existing rules for SSH connections. Ensure that the new filter rules replace the existing rule to ACCEPT connections.

{{{### Allow SSH from WAN
iptables -t nat -A prerouting_rule -i $WAN -p tcp --dport 22 -j ACCEPT
iptables -t filter -A input_rule -i $WAN -p TCP --dport 22 \
  -m recent --name SSH --update --hitcount 5 --seconds 180 -j DROP
iptables -t filter -A input_rule -i $WAN -p TCP --dport 22 \
  -m recent --name SSH --set -j ACCEPT}}}

Test it by logging in 5 times yourself:

{{{~ $ ssh wrt54gs

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

{{{~ $ ssh wrt54gs
[banner elided]
root@OpenWrt:~# ^D
Connection to wrt54gs closed.

~ $ ssh wrt54gs
ssh: connect to host wrt54gs port 22: Connection timed out
~ $}}}
