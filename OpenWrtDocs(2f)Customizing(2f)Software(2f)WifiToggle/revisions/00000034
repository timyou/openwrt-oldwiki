#pragma section-numbers off
||<tablebgcolor="#f1f1ed" tablewidth="40%" tablestyle="margin: 0pt 0pt 1em 1em; float: right; font-size: 0.9em;"style="padding: 0.5em;">[[TableOfContents]]||
## Do you know that WhiteRussian is obsolete?
## Whatever... I'll no longer play with Wikis.
= Intro =
New diag module. This is what controls the LEDs and the buttons; now LEDs are /proc/diag/led and buttons trigger hotplug scripts in /etc/hotplug.d/button. This really makes it easy to add a''' '''!WiFi toggle''' '''button.

With little modifications the script can be used to connect/disconnect your WAN connection.

= Installation =
Create a directory for the hotplug script

{{{
mkdir -p /etc/hotplug.d/button}}}

Download the hotplug script
{{{
wget -O /etc/hotplug.d/button/01-wifitoggle "http://wiki.openwrt.org/OpenWrtDocs/Customizing/Software/WifiToggle?action=AttachFile&do=get&target=wifitoggle.hotplug1"
}}}

Download the UCI configuration file
{{{
wget -O /etc/config/wifitoggle "http://wiki.openwrt.org/OpenWrtDocs/Customizing/Software/WifiToggle?action=AttachFile&do=get&target=wifitoggle.config1"}}}

= Configuration =
Change the button you like to use or leave the default (reset button).

{{{
uci set wifitoggle.cfg1.button=ses}}}
Description of the options in the !WiFi toggle configuration file (/etc/config/wifitoggle):
||<tablewidth="1171px" tableheight="77px">'''Option''' ||'''Value''' ||'''Default value''' ||'''Description''' ||
||button ||[reset|ses|aoss] ||reset ||The name of the button on the router which should be used to turn !WifFi on/off ||
||seen ||[0|1] ||0 ||No idea what this is for but without the value 1 for seen the Reset button on the Fonera is not working. ||

Commit your changes

{{{
uci commit wifitoggle}}}
Test it by pressing the button you configured above.


= Alternative Script =

This is another setup based upon the above script, and also the one at: http://wiki.openwrt.org/OpenWrtDocs/KamikazeConfiguration
There are a few reasons for this modified version.  First objective is to reuse the code to allow for easy wireless (with accompanying led) toggling within the shell too.  Second objective is to minimise the number of writes to the flash rom every time wireless is toggled.

Note: If you are using wireless encryption, nas and radius daemons will not be turned off during toggle and will continue to occupy cpu/memory. They should not consume too many resources with no client load though.  

== Generic Toggle Script ==
Create a file called {{{woggle}}} in {{{/sbin}}} and paste this into it:
{{{
#!/bin/sh

WIFI_RADIOSTATUS=$(uci show wireless.wl0.disabled | cut -d = -f 2)
case "$WIFI_RADIOSTATUS" in
1)
        uci set wireless.wl0.disabled=0
        wifi
        echo 1 > /proc/diag/led/ses_white ;;
0)
        uci set wireless.wl0.disabled=1
        wifi
        echo 0 > /proc/diag/led/ses_white
        echo 2 > /proc/diag/led/wlan
esac
}}}
Then set {{{ chmod +x /sbin/woggle }}}

== Hotplugging ==

Now to get hotplugging working, create a directory in {{{/etc/hotplug.d}}} called {{{button}}} and then create a file in {{{/etc/hotplug.d/button}}} called {{{01-radio-toggle}}} as in the original wifi toggle script (above).  Paste this into that file:
{{{
if [ "$BUTTON" = "ses" ] ; then
        if [ "$ACTION" = "pressed" ] ; then
                /sbin/woggle
        fi
fi
}}}
and set {{{ chmod +x 01-radio-toggle }}} to make the file executable.

Although some of the LED lines have been removed from here, the behaviour is pretty much the same as the original scripts.  If you wish to add original led lines back, just copy the lines from the original scripts back in, or substitute your own.

Now, every time you want to turn the wireless on or off, you can press the button on the router, or you can issue a {{{woggle}}} command from the openwrt shell.
