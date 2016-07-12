#pragma section-numbers off
||<tablebgcolor="#f1f1ed" tablewidth="40%" tablestyle="margin: 0pt 0pt 1em 1em; float: right; font-size: 0.9em;"style="padding: 0.5em;">[[TableOfContents]]||
= Intro =
New diag module. This is what controls the LEDs and the buttons; now LEDs are /proc/diag/led and buttons trigger hotplug scripts in /etc/hotplug.d/button. This really makes it easy to add a''' '''!WiFi toggle''' '''button.

With little modifications the script can be used to connect/disconnect your WAN connection.

= Installation =
Create a directory for the hotplug script

{{{
mkdir -p /etc/hotplug.d/button}}}
Download the hotplug script and the UCI configuration file

{{{
wget -P /etc/hotplug.d/button -O 01-wifitoggle http://... (fix URL to link to attachment on this page)
wget -P /etc/config -O wifitoggle http://... (fix URL to link to attachment on this page)}}}

[http://wiki.openwrt.org/OpenWrtDocs/Customizing/Software/WifiToggle?action=AttachFile Show attachments]
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
