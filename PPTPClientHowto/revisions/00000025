#format wiki
#language en
[[TableOfContents]]
== OpenWrt PPTP Client ==

How to configure your router as a PPTP client to connect to a PPTP server such as MS VPN.

/!\ If your service provider needs you to use PPTP for internet access, see the simpler [:Faq] answer ''How do I configure PPTP for internet access?''

== Requirements ==

=== Packages ===
Install the ''pptp'', ''kmod-mppe'' and ''kmod-crypto'' package:
{{{
ipkg install pptp kmod-mppe kmod-crypto}}}

:-) While the ''pptp'' package is installed already if you are using the White Russian RC5 ''pptp'' build of !OpenWrt, you still need to install ''kmod-mppe'' and ''kmod-crypto'' for encryption and compression support.

## valid as of RC5, for build micro and bin ipkg pulls in pptp, kmod-mppe, kmod-crypto, kmod-gre, kmod-ppp, and ppp, for build pptp ipkg pulls in only kmod-mppe and kmod-crypto.

=== Modules ===

||'''Feature'''||'''Required Modules'''||
||Minimum PPTP support||slhc ppp_generic ppp_async||
||Encryption or compression||sha1 arc4 ppp_mppe_mppc||

## valid as of RC5

At minimum, add the following lines to ''/etc/modules'':
{{{
slhc
ppp_generic
ppp_async}}}

If you need to use encryption or compression, add the following lines to ''/etc/modules'':
{{{
ppp_mppe_mppc
arc4
sha1}}}

then either reboot or load the modules this once:
{{{
insmod slhc
insmod ppp_generic
insmod ppp_async
insmod ppp_mppe_mppc
insmod arc4
insmod sha1}}}

See ticket [https://dev.openwrt.org/ticket/412 #412].

## valid as of RC5

== Configuring a Tunnel ==

=== /etc/ppp/options.pptp ===

This file is provided by the ''pptp'' package, and works as-is.  It sets the options for all tunnels initiated from your router.

## valid as of RC5

There's no need to change the file now, but there are several options you can change later if you like, see the manual page for ''pppd'':
||'''Option'''||'''Purpose'''||
||''lcp-echo-failure'' n||keep-alive, maximum number of echo attempts before considering the link to be dead||
||''lcp-echo-interval'' n||keep-alive, time between each echo attempt in seconds||
||''idle'' n||terminated tunnel after ''n'' seconds of inactivity, set to 0 to disable||
||''refuse-eap''||refuse to authenticate using EAP, needed with some recent servers, try it if you see EAP responses in debug log||
||''persist''||do not exit after a connection is terminated; instead try to reopen the connection||
||''mppe required,no40,no56''||forces 128-bit encryption||

=== /etc/ppp/peers/peer_name ===

Make the ''/etc/ppp/peers directory'' and create a file named after the peer:
{{{
mkdir -p /etc/ppp/peers
cd /etc/ppp/peers
touch peer_name
chmod 600 peer_name}}}
Substitute ''peer_name'' above with a descriptive one for the link you are trying to establish.

## valid as of RC5, the /etc/ppp/peers directory does not exist until created, and doesn't need group or other access

The file created defines the link with the VPN server and there are a few necessary options. Edit and add the following to your peer-file:
{{{
pty "pptp hostnameOrIp --nolaunchpppd"}}}
Here we instruct ''pppd'' to launch ''pptp'' to communicate with the VPN server. Substitute ''hostnameOrIp'' with the DNS hostname or IP-address of the VPN server you want to connect to.

{{{
mppe required,stateless}}}
Require that the connection be encrypted, using stateless encryption.  Most tunnel servers require encryption, so try this first, and if you get a warning suggesting that the server doesn't want MPPE, then remove this line.

{{{
name DOMAIN\\Username}}}
Define the username for the VPN-connection (the password is stored in ''chap-secrets'', see below). Substitute ''DOMAIN'' with the Windows Domain your user belongs to or remove ''DOMAIN\\'' if none is required. Also substitute ''Username'' above with the user you want to use to connect with the VPN server.

{{{
remotename peer_name}}}
Add this to properly specify the account and password in ''chap-secrets'' (see below).

{{{
file /etc/ppp/options.pptp}}}
Instruct ''pppd'' to load the generic options provided by the ''pptp'' package.

{{{
replacedefaultroute}}}
You need to add this line in case you use PPTP to access the Internet.

{{{
ipparam name}}}
This is optional.  Substitute ''name'' with the one chosen for the peer-file. This is used as a parameter to the ''ip-up'' and ''ip-down'' script executed upon connection and tear down of the link. Hence, you can write that script to behave differently depending on which peer we are connecting to or disconnecting from.

Any other ''pppd''/''pptp'' options not considered generic (usable by all PPTP connections) should go below the above options in the peer-file. To enable on demand "dialling" for example; add ''persist'', ''demand'' and ''idle 3600'', to make the router disconnect after one hour of inactivity and bring it back up again once the link is required.

=== /etc/ppp/chap-secrets ===

The ''/etc/ppp/chap-secrets'' file contains a list of usernames and passwords for use by ''pppd''.

/!\ For the ''bin'' and ''pptp'' builds of !OpenWrt, the file will start out being a symbolic link to a template in ''/rom'', so remove the link, copy the template, and make sure it is ''chmod 600''.

Add the following to the ''/etc/ppp/chap-secrets'' file:
{{{
DOMAIN\\Username peer_name Password *}}}

There are four fields separated by spaces:

 * substitute ''DOMAIN\\Username''. It is important that this match the ''name'' in the ''/etc/ppp/peers/peer_name'' file above. So, if no ''DOMAIN\\'' was used, do not enter one here either.

 * substitute ''peer_name'' with whatever you used for ''remotename'' in the ''/etc/ppp/peers/peer_name'' file.

 * substitute ''Password'' with the password given to you by the owner of the PPTP server.  If the password contains blanks or special characters, enclose it in double-quotes, "like this".

 * the asterisk tells ''pppd'' that this tunnel may use any IP address.  Normally the PPTP server determines the address.

Anyway, in many cases this is still not enough to get PPTP-internet work. Due to critical bug in ''pppd'', it create route to your pptp-server through self-established interface (ppp0). This way it gets not route to the VPN server (loop) and breaks the connection in some minutes. To prevent this, you have to delete this route upon the connection (see ip-up). If your VPN-server lies behind your default gateway (not in your subnet), you also MUST add additional route to VPN-server. This case quite common and very few routers have an ability to define a route to VPN-server.

So for this mentioned to work, you need to add following lines to your /etc/ppp/ip-up:

{{{
DG=10.188.0.17 #this is your default gateway
/sbin/route del -host $5 dev ppp0 #we delete "stupid" pppd route
/sbin/route add -host $5 gw $DG dev vlan1 #we add route to vpn-server in case you need it}}}


== Testing a Tunnel ==

The ''pppd'' command is used to start a tunnel. The syntax is ''pppd call peername'', where ''peername'' is one of the peer files in ''/etc/ppp/peers'':
{{{
pppd call peername updetach}}}

||'''Option'''||'''Purpose'''||
||''call'' name||obtain options from file ''/etc/ppp/peers/''name||
||''updetach''||wait until the connection is made and then detach process from terminal||

To stop the tunnel, kill the ''pppd'' process:
{{{
killall pppd}}}

To test a tunnel and send debug output to the console, enter from the command prompt:
{{{
pppd call peername debug dump nodetach}}}

||'''Option'''||'''Purpose'''||
||''debug''||display what is happening during negotation||
||''dump''||display the ''pppd'' options and where they came from||
||''nodetach''||do not detach the process from terminal once link is started||

The output of a successful connection may look as follows:
{{{
root@ap1:~# pppd call peername debug nodetach
using channel 2
Using interface ppp1
Connect: ppp1 <--> /dev/pts/2
sent [LCP ConfReq id=0x1 <mru 1490> <asyncmap 0x0> <magic 0xeae657f6>]
rcvd [LCP ConfReq id=0x0 <mru 1400> <auth eap> <magic 0x71251209> <pcomp> <accomp> <callback CBCP> <mrru 1614> <endpoint 13 17 01 42 a0 b2 3b 4f 73 48 02 8b d7 bd 18 49 9f a0 e4 00 00 00 00> < 17 04 00 c6>]
sent [LCP ConfRej id=0x0 <pcomp> <accomp> <callback CBCP> <mrru 1614> < 17 04 00 c6>]
rcvd [LCP ConfAck id=0x1 <mru 1490> <asyncmap 0x0> <magic 0xeae657f6>]
rcvd [LCP ConfReq id=0x1 <mru 1400> <auth eap> <magic 0x71251209> <endpoint 13 17 01 42 a0 b2 3b 4f 73 48 02 8b d7 bd 18 49 9f a0 e4 00 00 00 00>]
sent [LCP ConfNak id=0x1 <auth chap MD5>]
rcvd [LCP ConfReq id=0x2 <mru 1400> <auth chap MS-v2> <magic 0x71251209> <endpoint 13 17 01 42 a0 b2 3b 4f 73 48 02 8b d7 bd 18 49 9f a0 e4 00 00 00 00>]
sent [LCP ConfAck id=0x2 <mru 1400> <auth chap MS-v2> <magic 0x71251209> <endpoint 13 17 01 42 a0 b2 3b 4f 73 48 02 8b d7 bd 18 49 9f a0 e4 00 00 00 00>]
sent [LCP EchoReq id=0x0 magic=0xeae657f6]
rcvd [CHAP Challenge id=0x0 <54b2c702f64e0e27b48294cb4a08e55f>, name = "VPNSERVER"]
sent [CHAP Response id=0x0 <a9a840a6c0ba05641229e26a1ba65b370000000000000000dd7fcf6db46cdfe29ae19fcfa01de5268256a3521dffc2e300>, name = "DOMAIN\\Username"]
rcvd [LCP EchoRep id=0x0 magic=0x71251209]
rcvd [CHAP Success id=0x0 "S=09F4D2BD2B89C41308C4853687110838FB1D1DE3"]
sent [CCP ConfReq id=0x1 <mppe -H -M -S -L -D +C>]
sent [IPCP ConfReq id=0x1 <compress VJ 0f 01> <addr 192.168.255.1>]
rcvd [CCP ConfReq id=0x4 <mppe +H -M +S -L -D +C>]
sent [CCP ConfNak id=0x4 <mppe -H -M +S -L -D +C>]
rcvd [IPCP ConfReq id=0x5 <addr 192.168.0.1>]
sent [IPCP ConfAck id=0x5 <addr 192.168.0.1>]
rcvd [CCP ConfNak id=0x1 <mppe -H -M +S -L -D +C>]
sent [CCP ConfReq id=0x2 <mppe -H -M +S -L -D +C>]
rcvd [IPCP ConfRej id=0x1 <compress VJ 0f 01>]
sent [IPCP ConfReq id=0x2 <addr 192.168.255.1>]
rcvd [CCP ConfReq id=0x6 <mppe -H -M +S -L -D +C>]
sent [CCP ConfAck id=0x6 <mppe -H -M +S -L -D +C>]
rcvd [CCP ConfAck id=0x2 <mppe -H -M +S -L -D +C>]
MPPC/MPPE 128-bit stateful compression enabled
rcvd [IPCP ConfNak id=0x2 <addr 192.168.0.2>]
sent [IPCP ConfReq id=0x3 <addr 192.168.0.2>]
rcvd [IPCP ConfAck id=0x3 <addr 192.168.0.2>]
local IP address 192.168.0.2
remote IP address 192.168.0.1
Script /etc/ppp/ip-up started (pid 872)
Script /etc/ppp/ip-up finished (pid 872), status = 0x0}}}

If problems arise, from here search the ''pppd'' and ''pptp'' documentation and forums, since there is already tons of information available.

== Configuring Routing ==

=== /etc/ppp/ip-up and /etc/ppp/ip-down ===

The file ''/etc/ppp/ip-up'' is a shell script which is executed when the tunnel is started.. It is nice to be able to configure ''iptables'' or routing once the tunnel is up and remove that configuration once the tunnel is taken down.

Create the files and set execute permission if they do not already exist:
{{{
touch /etc/ppp/ip-up
chmod 755 /etc/ppp/ip-up
touch /etc/ppp/ip-down
chmod 755 /etc/ppp/ip-down}}}

Edit the files and add the following preamble. ''#!/bin/sh'' is required as the first line, to enable execution of the script. The other text, is good as a reminder of the parameters used when pppd calls these scripts.
{{{
#!/bin/sh
# parameters
# $1 the interface name used by pppd (e.g. ppp3)
# $2 the tty device name
# $3 the tty device speed
# $4 the local IP address for the interface
# $5 the remote IP address
# $6 the parameter specified by the 'ipparam' option to pppd}}}

It is the sixth parameter which is defined by ''ipparam'' in the peer-file above. It is a useful parameter to distinguish the scripts behaviour depending on which tunnel or PPP connection we are bringing up or down.

A generic structure for the ip-up and ip-down script shall check the ''$6'' parameter to match with an appropriate code section through a ''case'' branch as follows:
{{{
case "$6" in
 peer-name1)
  <commands here>
  ;;
 peer-name2)
  <commands here>
  ;;
 *)
esac
exit 0
}}}
Substitute ''peer-name1'', with the value given to ''ipparam'' above in the peer-file. Since we are configuring the first VPN link, you probably do not ''peer-name2'', it is included here as a template when adding another link. For now, remove it. Also, remove ''<commands here>>'', these will be replaced with actual commands below.

When you use commands in these scripts, be sure to either use their full path or add `/usr/sbin` and `/sbin` to the ''PATH'' first.  pppd intentionally restricts the ''PATH'' available to the scripts for security reasons.

=== iptables (firewall) rules ===
To update your firewall rules when the tunnel is brought up or torn down, we need to add a few commands to the ip-up and ip-down scripts created above. Also note, all these commands you can add to something like /etc/init.d/S70routes (create it). Though you have no ppp0 interface upon ''S70routes'' execution, it will work nevetherless. In this case you also do not need to remove these rules in ip-down. You can just add these lines to your S70routes:

{{{
iptables -A FORWARD -t filter -i br0 -m state --state NEW,ESTABLISHED,RELATED -j ACCEPT
iptables -A FORWARD -t filter -i ppp0 -m state --state ESTABLISHED,RELATED -j ACCEPT
iptables -t nat -A POSTROUTING -o ppp0 -s 192.168.168.0/24 -d 0/0 -j MASQUERADE}}}

Where 192.168.168.0/24 is your internal subnet (LAN). This, though not delicate, works for common case.


To allow outgoing communication with the tunnel add the following to ''ip-up'':
{{{
iptables -A forwarding_rule -o $1 -j ACCEPT}}}

Likewise, if we want to allow incoming traffic from the tunnel add to ''ip-up'':
{{{
iptables -A forwarding_rule -i $1 -j ACCEPT}}}

To enable masquerading (NAT) to the network beyond the tunnel add to ip-up:
{{{
iptables -t nat -A postrouting_rule -o $1 -j MASQUERADE}}}

Masquerading does not require {{{iptables -A forwarding_rule -i $1 -j ACCEPT}}} as described above. It is only required if the other end of the tunnel will send traffic to our network. Incoming traffic requires the other end of the tunnel to know about our local network topology either through static routes or by other means (routing protocols such as RIP and OSPF).

When adding (inserting) into the ''iptables'' ruleset, we need a corresponding removal in ''ip-down'' when the tunnel is taken down. Simply add the same command as above into ip-down substituting ''-A'' with ''-D'':
{{{
iptables -D forwarding_rule -o $1 -j ACCEPT
iptables -D forwarding_rule -i $1 -j ACCEPT
iptables -t nat -D postrouting_rule -o $1 -j MASQUERADE}}}

=== static routing ===
This howto assumes you will not use the tunnel as a default route. Instead each relevant network will be added to the static routing table of the OpenWrt router. Other means, such as routing protocols could likely be used. Please update this Wiki if you have any good ideas regarding this.

To add a network to the routing table for the tunnel we again go to the ''ip-up'' script and add the route. The general syntax is:
{{{
route add -net <network-address> netmask <network-netmask> $1}}}
Subsititue ''<network-address>'' with one you want to reach through the VPN-link. Also, ''<network-netmask>'' should be replaced with the appropriate value.

For example, to make network 192.168.0.0 with a netmask of 255.255.255.0 reachable, add:
{{{
route add -net 192.168.0.0 netmask 255.255.255.0 $1}}}

Again, a corresponding route ''delete'' command should be added to the ''ip-down'' script. To delete a network from the routing table, replace ''add'' with ''del'' and also remove ''$1'' at the end of the command, since it is not needed.

To continue the example above, deleting the route added by ''ip-up'' for the 192.168.0.0/255.255.255.0 network:
{{{
route del -net 192.168.0.0 netmask 255.255.255.0}}}
If entered in ''ip-down'' for the appropriate link, the 192.168.0.0/24-network will be removed from the static routing table when the link is taken down.

=== static routing for all packets ===

(It should be possible to direct all packets into the tunnel, if that's what you want. But be careful; if you direct the tunnel's packets as well, you'll end up with a routing loop and nothing will work.  To avoid this, add a static route for your tunnel server using the network interface.  Then add a default route that directs everything else to the tunnel network interface. The static host route takes priority over the default route, avoiding the  loop.  -- JamesCameron, PPTP Linux maintainer.)

== Connecting on startup ==
To connect instantly as the router boots, add the ''pppd call peername'' command to a start script in {{{/etc/init.d/}}}. If a connection cannot be made with the VPN-server as the WAN link may not be active yet, either experiment with a sleep prior to calling ''pppd'' or come up with a better solution (see on demand dial below as well).

== On demand "dial" ==
''pppd'' supports bringing a link up when it is needed. This requires that the static routes are already in place, prior to establishing the connection. Hence, it wont help adding them to ''ip-up''. Instead these routes need to be entered in the start script.

Edit the start script in {{{/etc/init.d/}}} and add the required networks through route add for the link in question.

Consider the example, where we have a peer defined in {{{/etc/ppp/peers}}} called peer1. Then, when establishing the link in demand dial mode, we sleep for a bit, then add the static routes in question.
{{{
pppd call peer1 persist demand idle 3600
sleep 2
route add -net 192.168.0.0 netmask 255.255.255.0 ppp0
}}}
Here we can not use a parameter for the link (normally $1 in the ip-up and ip-down scripts). We have to make sure the routes are entered for the correct link, since we are in a start script we can be quite certain no other ppp-links have been brought up. Type ''ifconfig'' in a console to ensure that the correct interface is used. When using PPPoE it is likely a ppp0 interface already exists. Then, the ''pppd call'' command will bring up the next one, ppp1 in this case. Hence, update the start script to reflect the correct interface name.

Once an IP packet is sent to the router destined for the VPN ppp interface, the link is brought up. After 3600 (the idle option above) seconds of inactivity, the link is brought down anew and it will revert to the behaviour of waiting for a packet to arrive destined for the VPN link.

== Routing back ==
If you want the other end of the VPN-connection to be able to route packets back to the local (OpenWrt) network you will have to add the appropriate static routes to the VPN-server or use a better solution such as a routing protocol.

To add static routes to a pppd server, use the ip-up and ip-down scripts on the server.

In Windows, you can define static routes for a VPN connection by administering the VPN-user in question. Choose the ''Dial-in'' tab and tick the checkbox next to ''Apply Static Routes''. Click the ''Static Routes ...'' button to add the necessary routes for traffic to flow in the opposite direction.

=== Quagga ===
The OSPF, RIP and other routing protocols are provided by Quagga.  The OSPF and RIP protocols are commonly implemented and also by Microsoft Windows(r).  The routing protocol can be made responsible to handle the routing table updates when a pptp link is brought up or taken down.  Please see the relevant documentation for Quagga or other routing daemons you may need to use.

== Troubleshooting ==
if you cannot connect, and you get some error like:

{{{
rcvd [CCP ConfReq id=0x1 <mppe +H -M +S -L -D -C>]
sent [CCP ConfNak id=0x1 <mppe -H -M +S -L -D -C>]
rcvd [LCP TermReq id=0x3 "MPPE required but peer negotiation failed"]
LCP terminated by peer (MPPE required but peer negotiation failed)
}}}

you have to add a line in the ''/etc/ppp/options.pptp''
{{{
mppe required,no40,no56,stateless
}}}


== Example Scripts ==

These example scripts show how to configure ''iptables'' rules when a tunnel comes up or goes down.

Several things to note about the scripts:
 1. the ''iptables'' and ''route'' commands were entered in full path format, if this isn't done the scripts silently fail with a 127 exit code reported by ''pppd'',
 1. logging is done to to `/var/log/ppp` using ''echo'',
 1. incoming connections aren't enabled, add ''iptables'' rules if you need them,
 1. change the 10.0.0.0/8 remote subnet according to your needs.

Improvements are welcome.

=== /etc/ppp/ip-up ===
{{{
#!/bin/sh
# parameters
# $1 the interface name used by pppd (e.g. ppp3)
# $2 the tty device name
# $3 the tty device speed
# $4 the local IP address for the interface
# $5 the remote IP address
# $6 the parameter specified by the 'ipparam' option to pppd

logfile=/var/log/ppp
echo "`date` $0 $1 $2 $3 $4 $5 $6" >> $logfile

case "$6" in
 peer-name1)
  A="/usr/sbin/iptables -t filter -I FORWARD -o $1 -j ACCEPT"
  B="/usr/sbin/iptables -t nat -A POSTROUTING -o $1 -j MASQUERADE"
  C="/sbin/route add -net 10.0.0.0 netmask 255.0.0.0 $1"
  $A
  echo " $? $A" >> $logfile
  $B
  echo " $? $B" >> $logfile
  $C
  echo " $? $C" >> $logfile
  ;;
 *)
esac
exit 0
}}}

=== /etc/ppp/ip-down ===
{{{
#!/bin/sh
# parameters
# $1 the interface name used by pppd (e.g. ppp3)
# $2 the tty device name
# $3 the tty device speed
# $4 the local IP address for the interface
# $5 the remote IP address
# $6 the parameter specified by the 'ipparam' option to pppd

logfile=/var/log/ppp
echo "`date` $0 $1 $2 $3 $4 $5 $6" >> $logfile

case "$6" in
 peer-name1)
   A="/usr/sbin/iptables -t filter -D FORWARD -o $1 -j ACCEPT"
   B="/usr/sbin/iptables -t nat -D POSTROUTING -o $1 -j MASQUERADE"
   C="/sbin/route del -net 10.0.0.0 netmask 255.0.0.0 $1"
   $A
   echo " $? $A" >> $logfile
   $B
   echo " $? $B" >> $logfile
   $C
   echo " $? $C" >> $logfile
   ;;
 *)
esac
exit 0
}}}
