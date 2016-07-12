= ntpd: the ISC NTP Daemon =
If you just want a lightweight ntp client, either the [:OpenWrtDocs/Packages/ntpclient:ntpclient] package or the build-in {{{rdate}}} command might be a better choice.

== Installation ==
Package installation instructions are at [:OpenWrtDocs/Packages:Packages], but generally, just do this:
{{{
opkg install ntpd
}}}

== Configuring ntp server ==
1. Configure ntpd as a service
The installer should configure the ntp server as a service, but if it didn't, add this line to {{{/etc/services}}}
{{{
ntp             123/udp     # Network Time Protocol
}}}

2. Set the listen interface
Some versions require the listen interface to set in /etc/ntpd.conf.  To see if yours does, precede to start the server, then try using ntpdate or ntpclient on another computer to get the time:

{{{
# -d instructs ntpdate to not set the date
ntpdate -d <host>

# lack of -s instructs ntplcient to just check the date
ntpclient -c 1 -h <host>
}}}

If it doesn't work, create {{{/etc/ntpd.conf}}} with this:
{{{
servers openwrt.pool.ntp.org

# 0.0.0.0 means all interfaces
listen on 0.0.0.0
}}}

3. Restart ntpd
{{{
/etc/init.d/ntpd restart
}}}

4. Firewall setup
If this service will be offered to non-local computers, you might have to open UDP port 123 for ntpd.
See also: [OpenWrtDocs/Kamikaze/FirewallConfiguration]
== Configuring ntp client ==
Todo:
----
CategoryPackage
