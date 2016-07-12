'''This page still under development!!!'''

Describe DDNSHowTo here.


[[TableOfContents]]


= About Dynamic DNS (DDNS) =

The DDNS service is for etablishing connections from computers on
the Internet to your computer. This is useful if you want to run
server software on your computer and only have a dynamic IP.

OpenWrt uses ez-ipupdate for providing DDNS service.


= Requirements =

A recent OpenWrt version. This howto was written for the
'White Russian RC3' release.


= Installation =

{{{
ipkg install ez-ipupdate
}}}


= Configuration =

ez-ipupdate can be used with the following services:

    * http://www.ez-ip.net
    * http://www.justlinux.com
    * http://www.dhs.org
    * http://www.dyndns.org
    * http://www.ods.org
    * http://gnudip.cheapnet.net (GNUDip)
    * http://www.dyn.ca (GNUDip)
    * http://www.tzo.com
    * http://www.easydns.com
    * http://www.dyns.cx
    * http://www.hn.org
    * http://www.zoneedit.com


== Creating the configuration file ==

Easiest way to use ez-ipupdate is creating a configuration file.
We call the file /etc/ez-ipupdate.conf. You can choose any other
name.

{{{
cat > /etc/ez-ipupdate.conf
}}}

{{{
service-type=zoneedit
user=myname:mypassword
interface=eth0
host=mydomain.com
cache-file=/tmp/ez-ipup
pid-file=/var/run/ez-ipupdate.pid
#notify-email=john.doe@mydomain.com
# other options:
#address=<ip address>
#daemon
#debug
#foreground
#host=<host>
#interface=<interface>
#mx=<mail exchanger>
#retrys=<number of trys>
#run-as-user=<user>
#run-as-euser=<user>
#server=<server name>
#timeout=<sec.millisec>
#max-interval=<time in seconds>
#notify-email=<email address>
#period=<time between update attempts>
#url=<url>
}}}

The list of allowed parameters in the configuration file are:

{{{
address                 usage: address=[ip address]
cache-file              usage: cache-file=[cache file]
cloak-title             usage: cloak-title=[title]
daemon                  usage: daemon=[command]
execute                 usage: execute=[shell command]
debug                   usage: debug
foreground              usage: foreground
pid-file                usage: pid-file=[file]
host                    usage: host=[host]
interface               usage: interface=[interface]
mx                      usage: mx=[mail exchanger]
max-interval            usage: max-interval=[number of seconds between updates]
notify-email            usage: notify-email=[address to email if bad things happen]
offline                 usage: offline
retrys                  usage: retrys=[number of trys]
server                  usage: server=[server name]
service-type            usage: service-type=[service type]
timeout                 usage: timeout=[sec.millisec]
resolv-period           usage: resolv-period=[time between failed resolve attempts]
period                  usage: period=[time between update attempts]
url                     usage: url=[url]
user                    usage: user=[user name][:password]
run-as-user             usage: run-as-user=[user]
run-as-euser            usage: run-as-euser=[user] (this is not secure)
wildcard                usage: wildcard
quiet                   usage: quiet
connection-type         usage: connection-type=[connection type]
request                 usage: request=[request uri]
partner                 usage: partner=[easydns partner]
}}}

The main configuration is done now.


= Starting DDNS =


== Manually via the command line ==

{{{
/usr/bin/ez-ipupdate -c /etc/ez-ipupdate.conf
}}}


== Via the /etc/ppp/ip-up script ==

This updateds your DDNS every time a PPP connection was etablished.
To get this working you need to have PPP installed and configured on your router.

{{{
test -d /etc/ppp || mkdir -p /etc/ppp
test -f /etc/ppp/ip-up || \
        echo -e "#/bin/sh\n\n/usr/bin/ez-ipupdate -c /etc/ez-ipupdate.conf &" \
        > /etc/ppp/ip-up
chmod a+x /etc/ppp/ip-up
}}}

[[BR]]

{{{
cat /etc/ppp/ip-up
}}}

{{{
#!/bin/sh

/usr/bin/ez-ipupdate -c /etc/ez-ipupdate.conf &
}}}

If /etc/ppp/ip-up does not look like the above one, you have to edit the file manually with the vi editor.


== Via a cronjob ==


== Debugging ==

To check if ez-ipupdate really updated your IP look at the contents of the
file /tmp/ez-ipup:

{{{
test -f /tmp/ez-ipup && cat /tmp/ez-ipup
}}}

The dump of my /tmp/ez-ipup file:

{{{
1127182459,aaa.bbb.ccc.ddd
}}}

The first number is a Unix timestamp. And aaa.bbb.ccc.ddd is your current
IP address. You can checkout your current IP address with
http://www.whatismyip.com/ or http://www.whatismyip.org/.


= Useful links =

For more details please have a look at the links below.

[[BR]]- http://en.wikipedia.org/wiki/Ddns
[[BR]]- http://www.ez-ipupdate.com/
