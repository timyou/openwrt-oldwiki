THIS IS WORK IN PROGRESS.

If correctly following the instructions in this tutorial you will get a hotspot with captive portal and user management running stand alone on Kamikaze 7.06. No external server or persistency mechanism will be required.

For much hardware this will be quite a suite of deamons to handle and might very well run out of space halfway this tuturial. On the authors WRT54GL with clean 2.4 kamikaze 7.06 flash there was 60K available for website and userdatabse on jffs after install using ipkg. 800K free when building firmware with all applications in squashfs.

[[TableOfContents]]


= Chillispot =

[Chillispot http://www.chillispot.org/] is a fully loaded user network connection management suit.

Using ipfilter it ensures that only authenticated connections have access to the network. All unauthenticated http/https connections are captured and sent to a login script. This is known as a captive portal.

Traffic from clients is routed from the interface (in this case {{{wl0}}}) via a tunnel (here known as {{{tun0}}}) in wich per user shaping and filters can be applied. These settings, and all user meta data, is stored in a RADIUS. In this tutorial I will use FreeRADIUS and its plain text file database module.

= Installing =

{{{
root@OpenWRT:/# ipkg install chillispot
}}}

This will install a minimal Chillispot distribution.

By default it sets up the client network 192.168.182.0/24 on {{{tun0}}}. Do not attempt to change this to the same range as your internal LAN. The first two IP-addresses in the range is reserved (.1 is the client gateway, your WRT) and will not be leased out by Chillispots built in DHCP.

It comes with a huge chilli.conf. You can replace it with something like this:

/etc/chilli.conf
{{{
root@master:/# cat /etc/chilli.conf
radiusserver1 127.0.0.1
radiusserver2 127.0.0.1
radiussecret testing123
dhcpif wl0
dns1 192.168.182.1
dns1 192.168.182.2
uamanydns
uamsecret testing123
uamserver https://192.168.182.1/cgi-bin/hotspotlogin.cgi
}}}


The tunneled interface must not be bridged to the network. Simply comment out {{{out option net lan}}} in your configutation file for the hotspot interface.

/etc/config/wireless
{{{
config wifi-device  wl0
        option type     broadcom
        option channel  8

config wifi-iface
        option device   wl0
#       option network  lan
        option mode     ap
        option ssid     OpenWRT
        option hidden   0
        option encryption none
}}}

This is in most cases all the Chillispot configuration you need to bother about. However, Chillispot have a few package dependencies you need to set up and tweak in order for everthing to run smooth of your WRT.


= Prerequisites to start =

== mini-httpd-ssl ==

 * SSL for hotspotlogin.cgi
 * create new PEM-cert
 * index.html

== microperl ==

 * hotspotlogin.cgi is perl
 * hotspotlogin.cgi needs to be patched iwth MD5:Digest code
 * microperl does not come integer.pw, get this from your own perl an put it in cgi-bin.

== freeradius ==

 * ipkg install freeradius
 * radiusd.conf - auth not needed when radiusd and chilli is on same machine
 * users - managemnt
