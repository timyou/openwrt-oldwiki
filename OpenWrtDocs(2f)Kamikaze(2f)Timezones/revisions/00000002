= Timezones =
With the x-wrt webif^2, use System -> Settings page.

'''*The following information is probably out of date*'''
Otherwise, in /etc/config/timezone an example is (for info about other zones and DST rules, see OpenWrtDocs/Configuration and look for Timezone)

{{{
config timezone
        option posixtz  MST7MDT,M3.2.0,M11.1.0
        option zoneinfo 'America/Denver'
}}}
~-Note: The '''zoneinfo''' field is designed to contain the same information like the timezone setting in most current *nix implementations (the Olson's database). It will later enable to simply synchronize changes in the POSIX TZ strings.-~

Do the following on a *nix system to find out your timezone string:

{{{
cat /usr/share/zoneinfo/posix/continent/city
}}}
and look at the last line.

Next you either create the /etc/TZ file and copy the posixtz field to it or you can create a simple timezone init script which will handle all TZ changes and the creation of the /etc/TZ file:

{{{
#!/bin/sh /etc/rc.common
START=11
timezone_config() {
        local cfg="$1"
        local posixtz
        local etctz="/etc/TZ"
        config_get posixtz "$cfg" posixtz
        if [ ! -h $etctz ]; then
                ln -sf /tmp/TZ "$etctz"
        fi
        [ -n "$posixtz" ] && echo "$posixtz" > "$etctz" || echo "UTC+0" > "$etctz"
}
start() {
        config_load timezone
        config_foreach timezone_config timezone
}
restart() {
        start
}
}}}
and issue

{{{
/etc/init.d/timezone start
/etc/init.d/timezone enable
}}}

CategoryHowTo
