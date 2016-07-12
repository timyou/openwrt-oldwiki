#pragma section-numbers off
||<tablebgcolor="#f1f1ed" tablewidth="40%" tablestyle="margin: 0pt 0pt 1em 1em; float: right; font-size: 0.9em;"style="padding: 0.5em;">[[TableOfContents]]||
= Configure WiFi encryption =
To generate a random password for you key you can use the pwgen program. Pwgen is available for most Linux distributions and is also packaged for !OpenWrt Kamikaze. E.g. pwgen 13 1

== WPA encryption ==
=== Broadcom WiFi ===
For Broadcom wireless chips you have to install the nas package.

{{{
ipkg install nas}}}
=== Atheros WiFi ===
For Atheros wireless chips install the hostapd package if your run in AP mode.

{{{
ipkg install hostapd}}}
'''TIP:''' If you only need WPA (PSK) encryption you can install the hostapd-mini package which does not depend on the zlib and libopenssl packages.

If you have a Atheros wireless and run it in client-mode you have to install the wpa-supplicant package instead of hostapd.

{{{
ipkg install wpa-supplicant}}}
=== Configure WPA (PSK) ===
Configure WPA (PSK) encryption using UCI.

{{{
uci set wireless.cfg2.encryption=psk
uci set wireless.cfg2.key=<password>
uci commit wireless && wifi}}}
'''Note: '''For the key only letters (upper and lower case) and numbers are allowed. The length must be between 8 and 63 characters.

=== Configure WPA2 (PSK) ===
Configure WPA2 (PSK) encryption using UCI.

{{{
uci set wireless.cfg2.encryption=psk2
uci set wireless.cfg2.key=<password>
uci commit wireless && wifi}}}
'''Note: '''For the key only letters (upper and lower case) and numbers are allowed. The length must be between 8 and 63 characters.

== WEP encryption (not recommended) ==
Some notes for the WEP key format:

 * The format for the WEP key for the key1 option is HEX
 * The length of a 64bit WEP key must be exact 5 characters
 * The length of a 128bit WEP key must be exact 13 characters
 * Allowed characters are letters (upper and lower case) and numbers
Generate a 64bit WEP key:

{{{
echo -n 'awerf' | hexdump -e '5/1 "%02x" "\n"' | cut -d ':' -f 1-5
6177657266
}}}
Generate a128bit WEP key:

{{{
echo -n 'xdhdkkewioddd' | hexdump -e '13/1 "%02x" "\n"' | cut -d ':' -f 1-13
786468646b6b6577696f646464}}}
The above commands generate a 64bit and a 128bit WEP key in hex format.

Now use UCI to configure WEP encryption with the hex key you just generated.

{{{
uci set wireless.cfg2.encryption=wep
uci set wireless.cfg2.key1=<WEP_key_in_hex_format>
uci set wireless.cfg2.key=1
uci commit wireless && wifi}}}
You can configure up to four WEP keys.
