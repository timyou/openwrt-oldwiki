#format wiki
#language en
[[TableOfContents]]
= OpenWrt Multiple PPTP VPN Passthrough =

How to configure your router to passthrough multiple VPN connections to a PPTP server such as MS VPN.

== Background ==

The standard WhiteRussian 5 binaries support only one PPTP VPN passthrough session at a time.  For example, lets say I have 2 Windows XP client computers connected to the Internet through a WRT54GL running WhiteRussian 5.  On Vthe first client computer I make a VPN connection to a Microsoft VPN server somewhere out there on the Net.  This connections works fine.  Now lets say a 2nd user tries to make a VPN connection on the 2nd client computer.  Their connection attempt will fail.

The reason the 2nd VPN connection won't work is simply that the ports used by the underlying protocols can only handle a single session without special connection tracking.

The good news is that there is already an OpenWrt package available that provides this connection tracking.

== Procedure ==

 * Connect to your WhiteRussian 5 shell.

 * Assuming you have ipkg configured and the package list updated, install the kmod-ipt-nat-extra package:
    root@OpenWrt:~# ipkg install kmod-ipt-nat-extra

 * Mark the newly installed 

chmod +x /etc/modules.d/40-ipt-nat-extra
