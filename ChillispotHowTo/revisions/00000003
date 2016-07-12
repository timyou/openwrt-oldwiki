THIS IS JUST A TEMPLATE - will finnish through out this week.

If following the instructions in this document you will get a hotspot with captive portal and user management running stand alone on Kamikaze 7.06.

[[TableOfContents]]


= About Chillispot =

 * has its own dhcp
 * sets a a new iprange for hotspot clients.

== Captive portal ==

== tun0 ==

 * breaking up the bridge to run hotspot on wl0 only

= Installing =

 * ipkg install chillispot
 * chillid.conf example
 * explain some about ipranges, dns, uamsecret and so in a paragraph

= Software prerequisites =

If you build your own firmware with these packages in the squashfs it will end up 2.5MB, leaving some 800KB free on my WRT54GL when all configuation was in place.

== mini-httpd-ssl ==

 * SSL for hotspotlogin.cgi
 * create new PEM-cert
 * index.html

== microperl ==

 * hotspotlogin.cgi is perl, needs some modifications

=== integer.pw ===

microperl does not come integer, get this from your own perl an put it in cgi-bin.

== freeradius ==

 * ipkg install freeradius
 * radiusd.conf - auth not needed when radiusd and chilli is on same machine
 * users - managemnt


= Problems you might encounter =

 * dont try to get chilli to use the same iprange as your br-lan
 * all the other stuff ive written down on peices of paper
