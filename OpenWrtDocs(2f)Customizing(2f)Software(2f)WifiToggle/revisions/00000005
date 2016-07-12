If you are looking for a better Kamikaze solution look here: http://forum.openwrt.org/viewtopic.php?pid=53246#p53246

In the new '''OpenWrt WhiteRussian RC6''' the release notes indicated that there's a new diag module which adds control of the leds and the buttons in '''/proc'''.

Snip of release note :  '' New diag module This is what controlls the leds and the buttons; now leds are /proc/diag/led and buttons trigger hotplug scripts in /etc/hotplug.d/button. (Now you can also press any button at startup to enter failsafe mode) ''

This really makes it to easy to add a''' WifiToggle '''button to the Linksys WRT54GL loaded with RC6.

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
