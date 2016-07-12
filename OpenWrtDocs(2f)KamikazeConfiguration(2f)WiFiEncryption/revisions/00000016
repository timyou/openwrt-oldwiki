#pragma section-numbers off
||<tablebgcolor="#f1f1ed" tablewidth="40%" tablestyle="margin: 0pt 0pt 1em 1em; float: right; font-size: 0.9em;"style="padding: 0.5em;">[[TableOfContents]]||
= Configure WiFi encryption =
Howto setup wireless encryption with !OpenWrt Kamikaze. You can do the same from within the [http://luci.freifunk-halle.net/ LuCI WebUI] (Network > Wifi) if you prefer a GUI.

== Key generation ==
To generate a random password for your key you can use the {{{pwgen}}} program. pwgen is available for most Linux distributions and is also packaged for !OpenWrt Kamikaze. Run it with e.g. {{{pwgen --secret 13 1}}} (meaning: generate 1 password with a length of 13 letters/numbers).  On Debian Etch, use {{{pwgen --secure 13 1}}}.

== WPA encryption ==
=== Broadcom WiFi ===
For Broadcom wireless chips you have to install the nas package.

{{{
root@OpenWrt:~# opkg install nas}}}
=== Atheros WiFi ===
For Atheros wireless chips install the hostapd package if your run in AP mode.

{{{
root@OpenWrt:~# opkg install hostapd}}}
'''TIP:''' If you only need WPA (PSK) encryption you can install the hostapd-mini package which does not depend on the zlib and libopenssl packages.

If you have a Atheros wireless and run it in client-mode you have to install the wpa-supplicant package instead of hostapd.

{{{
root@OpenWrt:~# opkg install wpa-supplicant}}}
=== Configure WPA (PSK) ===
Configure WPA (PSK) encryption using UCI.

{{{
root@OpenWrt:~# uci set wireless.@wifi-iface[0].encryption=psk
root@OpenWrt:~# uci set wireless.@wifi-iface[0].key=<password>
root@OpenWrt:~# uci commit wireless
root@OpenWrt:~# wifi}}}
'''Note: '''For the key only letters (upper and lower case) and numbers are allowed. The length must be between 8 and 63 characters.

=== Configure WPA2 (PSK) ===
Configure WPA2 (PSK) encryption using UCI.

{{{
root@OpenWrt:~# uci set wireless.@wifi-iface[0].encryption=psk2
root@OpenWrt:~# uci set wireless.@wifi-iface[0].key=<password>
root@OpenWrt:~# uci commit wireless
root@OpenWrt:~# wifi}}}
'''Note: '''For the key only letters (upper and lower case) and numbers are allowed. The length must be between 8 and 63 characters.

-----

Configuration is also possible via direct editing of {{{/etc/config/wireless}}}:

{{{
	option encryption   psk
	option key	    "your_password"
}}}

-----

== WEP encryption (not recommended) ==
Some notes for the WEP key format:

 * The format for the WEP key for the key1 option is HEX
If you wish to use raw hex keys then you can skip to the UCI commands paragraph below.  Raw hex keys have 10 hex 'digits' (0..9, a..f) for 64-bit WEP keys and 26 hex 'digits' for 128-bit WEB keys.

If you do not wish to use raw hex keys then:

 * The length of a 64bit WEP key must be exact 5 characters
 * The length of a 128bit WEP key must be exact 13 characters
 * Allowed characters are letters (upper and lower case) and numbers
Generate a 64bit WEP key:

{{{
root@OpenWrt:~# echo -n 'awerf' | hexdump -e '5/1 "%02x" "\n"' | cut -d ':' -f 1-5
6177657266
}}}
Generate a128bit WEP key:

{{{
root@OpenWrt:~# echo -n 'xdhdkkewioddd' | hexdump -e '13/1 "%02x" "\n"' | cut -d ':' -f 1-13
786468646b6b6577696f646464}}}
The above commands generate a 64bit and a 128bit WEP key in hex format.

Now use UCI to configure WEP encryption with the hex key you just generated.

{{{
root@OpenWrt:~# uci set wireless.@wifi-iface[0].encryption=wep
root@OpenWrt:~# uci set wireless.@wifi-iface[0].key1=<WEP_key_in_hex_format>
root@OpenWrt:~# uci set wireless.@wifi-iface[0].key=1
root@OpenWrt:~# uci commit wireless
root@OpenWrt:~# wifi}}}
You can configure up to four WEP keys.
