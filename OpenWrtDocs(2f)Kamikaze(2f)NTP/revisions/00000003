= NTP Client =
To use ntp install the ntpclient package, and in modify /etc/config/ntpclient to your needs:

{{{
root@OpenWrt:~# opkg install ntpclient
}}}

Change the default NTP server using UCI. By default there are four NTP servers configured. To change the first NTP server run the following UCI command:
{{{
root@OpenWrt:~# uci set ntpclient.@ntpserver[0].hostname=pool.ntp.org
}}}
To change the second NTP server do:
{{{
root@OpenWrt:~# uci set ntpclient.@ntpserver[0].hostname=ntp.ubuntu.com
}}}
Save the changes with:
{{{
root@OpenWrt:~# uci commit ntpclient
}}}

Of course there are even more alternatives, e.g. feel free to substitute your local ntp server for pool.ntp.org.

Run
{{{
root@OpenWrt:~# root@OpenWrt:~# ACTION=ifup INTERFACE=wan /sbin/hotplug-call iface
}}}
or restart the network to update the time.

CategoryHowTo CategoryPackage
