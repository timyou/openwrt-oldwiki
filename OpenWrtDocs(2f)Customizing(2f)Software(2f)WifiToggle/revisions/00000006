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
wget -P /etc/hotplug.d/button -O 01-wifitoggle http://...
wget -P /etc/config -O wifitoggle http://...}}}
= Configuration =
Change the button you like to use to ses.

{{{
uci set wifitoggle.cfg1.button=ses}}}
Description of the options in the p910nd config file (/etc/config/p910nd):
||<tablewidth="1171px" tableheight="77px">'''Option''' ||'''Value''' ||'''Default value''' ||'''Description''' ||
||button ||[reset|ses|aoss] ||reset ||The name of the button on the router which should be used to turn WifFi on/off ||


Commit your changes

{{{
uci commit wifitoggle}}}
Test it by pressing the button you configured above.

----
 . In the new'''!OpenWrt !WhiteRussian RC6'''the release notes indicated that there's a new diag module which adds control of the leds and the buttons in'''/proc'''.Snip of release note :'' New diag module This is what controlls the leds and the buttons; now leds are /proc/diag/led and buttons trigger hotplug scripts in /etc/hotplug.d/button. (Now you can also press any button at startup to enter failsafe mode) ''This really makes it to easy to add a''' !WifiToggle '''button to the Linksys WRT54GL loaded with RC6.
Step 1 : As written in the release notes create a directory named '''button''' in '''/etc/hotplug.d/'''

Step 2 : Use you're favorite editor to create a file name '''/etc/hotplug.d/button/01-wifitoggle''' and insert the code below :

{{{
if [ "$BUTTON" = "ses" ] ; then
  if [ "$ACTION" = "pressed" ] ; then
  WIFI_RADIOSTATUS=$(nvram get wl0_radio)
  case "$WIFI_RADIOSTATUS" in
  0) nvram set wl0_radio=1
  wifi
   echo 1 > /proc/diag/led/ses_orange  ;;
  1) nvram set wl0_radio=0
    wifi
   echo 0 > /proc/diag/led/ses_orange ;;
  esac
 fi
fi
}}}
Step 3 : test it by pressing the button on the front of the WRT54GL:-)

Done.

''Note : the lines containing the '''echo''' can be dismist when not needed but I like (better visible then the small '''wlan''' led). ''
