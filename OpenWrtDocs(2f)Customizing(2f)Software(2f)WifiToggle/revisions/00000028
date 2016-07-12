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
First objective is to reuse the code to allow for easy wireless (with accompanying led) toggling within the shell too.  Second objective is to minimise the number of writes to the flash rom every time wireless is toggled.

First, make sure
{{{ option disabled 0 }}}
is set in the {{{/etc/config/wireless}}} (Kamikaze) for your interface.  This will mean the wireless will go up every time the router is powered up.  

== Bringing Wireless Offline After Boot ==
To bring wireless down at boot(only if you want) after it's brought up by regular network scripts, create a file called {{{wifidown}}} in {{{/etc/init.d}}} and copy and paste this in:
{{{ #!/bin/sh
/usr/sbin/woggle
}}}
Set {{{ chmod +x /etc/init.d/wifidown }}}
Then, you need it to load during boot, so type
{{{ ln -s /etc/init.d/wifidown /etc/rc.d/S99wifidown }}}
This will make sure it is one of the last scripts to be loaded after boot (to give the network scripts a chance to load first).

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

== Generic Toggle Script ==
Create a file called {{{woggle}}} in {{{/sbin}}} and paste this into it:
{{{
#!/bin/sh

WIFI_RADIOSTATUS=$(wlc radio)
case "$WIFI_RADIOSTATUS" in
0)
        wlc radio 1
        echo 1 > /proc/diag/led/ses_white ;;
1)
        wlc radio 0
        echo 0 > /proc/diag/led/ses_white
        echo 2 > /proc/diag/led/wlan
esac
}}}
Then set {{{ chmod +x /sbin/woggle }}}

Although some of the LED lines have been removed from here, the behaviour is pretty much the same as the original scripts.  If you wish to add original led lines back, just copy the lines from the original scripts back in, or substitute your own.

Now, every time you want to turn the wireless on or off, you can press the button on the router, or you can issue a {{{woggle}}} command from the openwrt shell.

---- /!\ '''End of edit conflict''' ----
