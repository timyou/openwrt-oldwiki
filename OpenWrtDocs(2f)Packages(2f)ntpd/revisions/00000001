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
Now, configure the server to listen on an interface by modifying /etc/ntp.conf
{{{
# use a random selection of 8 public stratum 2 servers
# see http://twiki.ntp.org/bin/view/Servers/NTPPoolServers

#restrict default nomodify notrap noquery
#restrict default noquery


restrict 127.0.0.1

driftfile  /etc/ntp.drift

server 0.pool.ntp.org iburst
server 1.pool.ntp.org iburst
server 2.pool.ntp.org iburst
server 3.pool.ntp.org iburst


# GPS(NMEA)+PPS
#server 127.127.20.0 minpoll 4 prefer
#fudge 127.127.20.0 flag3 1 flag2 0

# SMA PPS
#server 127.127.28.0 minpoll 4 prefer
#fudge 127.127.28.0 refid PPS flag3 1

#server 192.168.1.253

# 0.0.0.0 means all interfaces
'''listen on 0.0.0.0'''
}}}

3. Restart ntpd
{{{
/etc/init.d/ntpd restart
}}}

== Configuring ntp client ==
Todo:
----
CategoryPackage
