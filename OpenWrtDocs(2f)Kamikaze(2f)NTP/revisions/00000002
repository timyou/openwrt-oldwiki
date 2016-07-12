= NTP Client =
To use ntp install the ntpclient package, and in modify /etc/config/ntpclient to your needs:

{{{
config ntpclient
        option hostname 'pool.ntp.org'
        option port     '123'
        option count    '1'
config ntpclient
        option hostname 'ntp.ubuntu.com'
        option port     '123'
        option count    '1'
}}}
OpenWrt will soon advertise its [http://www.pool.ntp.org/vendors.html NTP Vendor Zone] with appropriate entries in all relevant packages. A [http://lists.openwrt.org/pipermail/openwrt-devel/2008-January/001524.html patch] for fixing this in ntpclient has these additional timeservers:

{{{
config ntpclient
        option hostname '0.openwrt.pool.ntp.org'
        option port     '123'
        option count    '1'
config ntpclient
        option hostname '1.openwrt.pool.ntp.org'
        option port     '123'
        option count    '1'
config ntpclient
        option hostname '2.openwrt.pool.ntp.org'
        option port     '123'
        option count    '1'
config ntpclient
        option hostname '3.openwrt.pool.ntp.org'
        option port     '123'
        option count    '1'
}}}
Of course there are even more alternatives, e.g. feel free to substitute your local ntp server for pool.ntp.org.

Run
{{{
ACTION=ifup /etc/hotplug.d/iface/20-ntpclient
}}}
or restart the network to update the time.

CategoryHowTo CategoryPackage
