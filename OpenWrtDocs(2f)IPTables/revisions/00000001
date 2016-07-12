## Please edit system and help pages ONLY in the moinmaster wiki! For more
## information, please see MoinMaster:MoinPagesEditorGroup.
##acl MoinPagesEditorGroup:read,write,delete,revert All:read
##master-page:HelpTemplate
##master-date:Unknown-Date
#format wiki
#language en
OpenWrt's firewall configuration resides in two places:

 * ''/etc/firewall.user'' is where users place your custom rules
 * ''/etc/config/firewall'' is the "quick and easy" (but perhaps less flexible) method of opening ports, creating service redirections, etc
The''/etc/config/firewall''method may be discussed here at some future time (but now today).
The basic structure of the firewall is established by the firewall start-up script in''/etc/init.d''.  It is worthwhile to examine this file for educational purposes, but it is not intended that you modify it.  Its job is to establish the basic iptables framework.  You customize its behavior by adding rules to pre-defined, empty rules; your additions go in''/etc/firewall.user''.  The purpose of this document is to explain the structure of those pre-defined rules.
The following diagram is adapted from the IPTables tutorial, with detail added to explain where each firewall.user rule fits in.  Each one of the detail boxes describes the actions that take place in the /etc/init.d firewall start-up script.  At certain points this script invokes user-defined chains of rules; this is duly noted. http://wiki.autofrog.com/_media/openwrt/openwrtiptables.png
