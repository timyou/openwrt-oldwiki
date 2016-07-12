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
wget -O /etc/hotplug.d/button/01-wifitoggle "http://wiki.openwrt.org/OpenWrtDocs/Customizing/Software/WifiToggle?action=AttachFile&do=get&target=wifitoggle.hotplug"
}}}

Download the UCI configuration file
{{{
wget -O /etc/config/wifitoggle "http://wiki.openwrt.org/OpenWrtDocs/Customizing/Software/WifiToggle?action=AttachFile&do=get&target=wifitoggle.config"}}}
[http://wiki.openwrt.org/OpenWrtDocs/Customizing/Software/WifiToggle?action=AttachFile Show attachments] (Please fix the long URLs. Thanks)

= Configuration =
Change the button you like to use or leave the default (reset button).

{{{
uci set wifitoggle.cfg1.button=ses}}}
Description of the options in the !WiFi toggle configuration file (/etc/config/wifitoggle):
||<tablewidth="1171px" tableheight="77px">'''Option''' ||'''Value''' ||'''Default value''' ||'''Description''' ||
||button ||[reset|ses|aoss] ||reset ||The name of the button on the router which should be used to turn !WifFi on/off ||


Commit your changes

{{{
uci commit wifitoggle}}}
Test it by pressing the button you configured above.
