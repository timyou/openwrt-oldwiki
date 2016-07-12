= Timezones =
Kamikaze stores the Timezone in system.@system[0].timezone. If you prefer the LuCI WebUI, use System > System and select your Zonename and Timezone there.

To change the Timezone from the shell using UCI CLI do:

{{{
root@OpenWrt:~# uci set system.@system[0].zonename=<zonename>
root@OpenWrt:~# uci set system.@system[0].timezone=<your_timezone>
root@OpenWrt:~# uci commit system
root@OpenWrt:~# timezone=$(uci get system.@system[-1].timezone); [ -z "$timezone" ] && timezone=UTC; echo "$timezone" > /tmp/TZ
}}}
Timezones: http://luci.freifunk-halle.net/UserDocs/TimeZones

CategoryHowTo
