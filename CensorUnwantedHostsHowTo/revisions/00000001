This HOWTO describes how to block the access to unwanted hosts by
iptables and a transparent http-proxy.  These instructions were tested
on WRT54GL with Kamikaze 7.09.

[[TableOfContents]]

= Packages to install =

You have to install the following packages on the router:

{{{
ipkg install kmod-ipt-nat
ipkg install iptables-mod-nat
ipkg install tinyproxy
}}}

The package `crowdcontrol` provides an alternative of `tinyproxy`
which I have not tried.

= Setting up Tiniproxy =

Tinyproxy is a lightweight proxy server.  We are going to make it
receive all http-requests from the internal lan to Internet.  Then
Tinyproxy will redirect these requests to the real hosts.  All this
happens transparently for the clients in the lan.

== `tinyproxy.conf` ==

The configuration file of Tinyproxy is
`/etc/tinyproxy/tinyproxy.conf`.  We have to change some of the
settings there.

By default Tinyproxy will listen on port 8888.  Unfortunately there is
a nasty bug in Kamikaze which makes impossible to redirect the http
port 80 to 8888 if kernel 2.4 is used.  There is a discussion in the
forum: http://forum.openwrt.org/viewtopic.php?id=13533.

In order to circumvent this we are going to make Tinyproxy listen on
port 80.  First disable the http-server of OpenWrt as it also listens
on port 80:
{{{
/etc/init.d/httpd stop
/etc/init.d/httpd disable
}}}

Then change the port in `tinyproxy.conf`:
{{{
Port 80
}}}

Check that the "Allow" directives permit access to Tinyproxy both from
the router itself and from the internal lan.  If you comment out these
directives Tinyproxy will listen on all interfaces; in this case make
sure that your firewall protects Tinyproxy from the outside world.
{{{
#Allow 127.0.0.1
#Allow 192.168.1.0/25
}}}

In OpenWrt `/var` is in RAM-drive and by default Tinyproxy will use
`/var/log/tinyproxy.log` as a log file.  This is not a good idea for a
device with limited RAM.  Lets use Syslog instead:
{{{
# Logfile "/var/log/tinyproxy.log"
Syslog On
}}}

In order to address the limited resources of the router you can also
change some of the following directives in `tinyproxy.conf`:
{{{
LogLevel Error
Timeout 120
MaxClients 100
MinSpareServers 5
MaxSpareServers 20
StartServers 10
MaxRequestsPerChild 10000
}}}

Finally the filter.  Url-based filtering is more flexible, POSIX
extended regular expressions are more convenient.  Use case
insensitive matching:
{{{
Filter "/etc/tinyproxy/filter"
FilterURLs On
FilterExtended On
FilterCaseSensitive Off
}}}

== The filter file ==

The file `/etc/tinypfoxy/filter` is a list of regular expressions, one
per line.  Each of them is describes a set of URLs that will be
blocked.

If you don't know how to write regular expressions here is a short
tutorial: . (a dot) matches any symbol, .* matches any sequence of
symbols, (foo|bar|zoo) matches the strings "foo", "bar" and "zoo".
The question mark is a special symbol so use \? if you want to match
a question mark.

There are several blacklists you can download from Internet but they
are quiet big and not suited for a device with limited resources.  I
think it would be inappropriate and offencive to write here a real
filter list so use the following only as an example:
{{{
breasts
erotic
fashion
fitness
naked
porno
sexy
swimsuit
underwear
playboy.com:80
google.*:80/.*(porn|sex)
youtube.com:80/.*(porn|sex)
yahoo.com:80/.*sex
}}}

You can see that there are three different patterns in this example
filter.

A bare word such as "fitness" will block any web address that includes
this word.

A pattern such as "playboy.com:80" will block the access to the given
site (and its subdomains) on port 80.

And a pattern such as "yahoo.com:80/.*sex" will block all sex-related
directories and searches on yahoo.com.

Notice that it is not necessary to block the Google-search for
i.e. "erotic" because it is already blocked by the simple pattern
"erotic".  On the other hand the pattern "sexy" does not block the
Google-search for "sex" so it is explicitly blocked.  Notice also that
there is no pattern "sex" instead of "sexy" because it would block
some wanted addresses such as http://en.wikipedia.org/wiki/Sextant.

== Final tweaks ==

By default `/etc/resolv.conf` is a symbolic link to a file where the
external DNS servers are given priority.  In order to improve the
performance of Tinyproxy remove this symbolic link and replace it by a
file with the following contents:
{{{
search lan
nameserver 127.0.0.1
}}}

Alternatively apply the following patch to `/etc/init.d/dnsmasq`:
{{{
--- dnsmasq	2008-08-14 22:10:50.000000000 +0300
+++ dnsmasq.new	2008-08-18 20:13:48.576758328 +0300
@@ -240,7 +240,7 @@
 
 	/usr/sbin/dnsmasq $args && {
 		rm -f /tmp/resolv.conf
-		DNS_SERVERS="$DNS_SERVERS 127.0.0.1"
+		DNS_SERVERS="127.0.0.1 $DNS_SERVERS"
 		for DNS_SERVER in $DNS_SERVERS ; do
 			echo "nameserver $DNS_SERVER" >> /tmp/resolv.conf
 		done
}}}

Finally we are ready to enable and start Tinyproxy!
{{{
/etc/init.d/tinyproxy enable
/etc/init.d/tinyproxy start
}}}

Check that everything is OK:
{{{
ps
logread | tail
}}}

You can try whether Tinyproxy works if you configure your web browser
to use it as a http-proxy.  If you use Firefox go to Edit/Preferences,
then select the tab "Advanced" and the subtab "Network".  Press the
button "Settings..." and use "Manual proxy configuration", "HTTP
proxy: 192.168.1.1 Port: 80" (or whatever is appropriate).  If you
browser works but some sites are blocked this means Tinyproxy works.
Do not forget to remove the proxy settings in your browser.

= Transparent forwarding to Tinyproxy =

Now we want to configure the transparent forwarding to Tinyproxy.  Add
the following commands at the end of `/etc/firewall.user`:
{{{
iptables -t nat -N natcensor
iptables -t nat -I prerouting_rule -j natcensor
}}}
These commands will create a new chain "natcensor" in the table "nat"
which is for now empty.  All outgoing packages will be inspected by
this chain.

In order to populate this chain create a script `/etc/init.d/censor`.
The following code assumes that you have defined three local network
interfaces in `/etc/config/network`:

 1. lan - the main local network
 1. wifi - additional local network
 1. free - the clients connected through this interface will have unrestricted access to Internet.

If your network configuration is simpler, then simply remove all lines
containing the strings "WIFI" and "FREE".

{{{
#!/bin/sh /etc/rc.common

START=46

start () {
	. /etc/functions.sh
	include /lib/network
	scan_interfaces
	
	config_get LAN lan ifname
	config_get LANIP lan ipaddr
	config_get WIFI wifi ifname
	config_get WIFIIP wifi ipaddr
	config_get FREE free ifname
	config_get FREEIP free ipaddr
	
	iptables -t nat -F natcensor
	iptables -t nat -A natcensor -i $FREE -j RETURN
	iptables -t nat -A natcensor -i $LAN -p tcp --dport 80 -j DNAT --to $LANIP
	iptables -t nat -A natcensor -i $WIFI -p tcp --dport 80 -j DNAT --to $WIFIIP
}

stop () {
	iptables -t nat -F natcensor
}
}}}

Now enable this script:
{{{
/etc/init.d/censor enable
/etc/init.d/censor start
}}}

Test that everything works as it should in your browser.  In order to
stop temporarily the filtering use
{{{
/etc/init.d/censor stop
}}}

If your router doesn't use kernel 2.4 but rather 2.6 then you can use
port forwarding.  In this case you can configure Tinyproxy to listen
on port 8080 or 8888 and you can leave port 80 for httpd.  Instead of
all commands with "-j DNAT" in `/etc/init.d/censor` use the following
one (where 8080 is the port for Tinyproxy):
{{{
iptables -t nat -A natcensor -p tcp --dport 80 -j REDIRECT --to-port 8080
}}}

= Block some hosts by their IP-number =

You may want to block completely the access to some hosts by their
IP-numbers.  Create a file `/etc/forbidden` which lists these hosts -
one IP-number per line.

Add the following commands at the end of `/etc/firewall.user`:
iptables -N censor
iptables -I forwarding_rule -j censor
iptables -I output_rule -j censor

Modify the script `/etc/init.d/censor` as follows:
{{{
#!/bin/sh /etc/rc.common

START=46

start () {
	...
	...
	...
	iptables -F censor
	iptables -A censor -i $FREE -j RETURN
	cat /etc/forbidden |
	while read ip; do
		iptables -A censor -d $ip -j REJECT --reject-with icmp-host-prohibited
	done
}

stop () {
	...
	iptables -F censor
}
}}}
