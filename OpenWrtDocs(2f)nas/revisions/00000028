= nas =

'''nas''' is the proprietary binary tool that sets up dynamic encryption (WEP/WPA) on the wireless device.

''note:'' normally '''nas''' is called by the S41wpa script in /etc/init.d. This Script composes the command by reading the corresponding nvram variables (wl0_ssid, wl0_akm, wl0_crypto,...).

''note:'' '''nas''' is not used in client bridging mode (i.e. the wireless interface is a client to a remote access point and it is bridged to the LAN port). This mode is configured by `wl0_mode=wet`. In this case the chipset driver's built-in supplicant is used, configured by `/sbin/wifi` from the wificonfig package. It reads the nvram variables itself.

== Where to get the nas binary? ==

The nas binary can be found at: http://downloads.openwrt.org/whiterussian/packages/non-free
If you use old version of firmware, please upgrade.

== How to configure? ==

If you installed the nas binary using the package indicated above, an install script is automatically added to the router. You can use the nvram to configure the nas options.

For a working Freeradius configuration for use with the Radius-enabled modes, see [:OpenWrtDocs/Wpa2Enterprise]

||'''Setting'''||'''nvram'''||'''Description'''||
||Wireless mode||wl0_mode||Using 'sta' will put the device in supplicant mode (client), otherwise it will be an authenticator (server).||
||SSID||wl0_ssid||The SSID configured for the wireless||
||WPA rekey||wl0_wpa_gtk_rekey||Rekeying interval in seconds. Defaults to 3600.||
||Authentication mode||wl0_akm||'wpa', 'wpa wpa2', 'wpa2', 'psk', 'psk psk2', 'psk2'.||
||Encryption mode for WPA||wl0_crypto||'tkip', 'aes', 'aes+tkip'.||
||Preshared key||wl0_wpa_psk||Specifies the preshared key. Only for psk/psk2||
||Radius Server IP||wl0_radius_ipaddr||Radius server IP address. Only for wpa/wpa2.||
||Radius Server Port||wl0_radius_port||Radius server port. Defaults to 1812. Only for wpa/wpa2.||
||Radius Server Shared Secret||wl0_radius_key||The shared secret with the Radius server. Only for wpa/wpa2.||

Please note, not all client cards/drivers/OSes support wpa/wpa2 or psk/psk2.  Try all combinations of wl0_akm before giving up on nas.

== nas command line options ==

=== Security disable ===
{{{
nas -P /tmp/nas.lan.pid -l br0 -H 34954
}}}

=== Security WPA-PSK TKIP ===
{{{
nas -P /tmp/nas.lan.pid -l br0 -H 34954 -i eth1 -A -m 4 -k <share-key> -s linksys -w 2 -g 3600
}}}

=== Security WPA-PSK AES ===
{{{
nas -P /tmp/nas.lan.pid -l br0 -H 34954 -i eth1 -A -m 4 -k <share-key> -s linksys -w 4 -g 3600
}}}

=== Security WPA-PSK TKIP+AES ===
{{{
nas -P /tmp/nas.lan.pid -l br0 -H 34954 -i eth1 -A -m 4 -k <share-key> -s linksys -w 6 -g 3600
}}}

=== Security WPA -RADIUS - TKIP ===
{{{
nas -P /tmp/nas.lan.pid -l br0 -H 34954 -i eth1 -A -m 2 -r <share-key> -s linksys -w 2 -g 3600 -h <Radius server ip> -p 1812 -t 36000
}}}

=== Security WPA2-PSK-TKIP ===
{{{
nas -P /tmp/nas.lan.pid -l br0 -H 34954 -i eth1 -A -m 128 -k <share-key> -s linksys -w 2 -g 3600
}}}

=== Security WPA2-RADIUS-TKIP ===
{{{
nas -P /tmp/nas.lan.pid -l br0 -H 34954 -i eth1 -A -m 64 -r <share-key> -s linksys -w 2 -g 3600 -h <Radius IP> -p 1812 -t 36000
}}}

=== Security WPA2-RADIUS-AES ===
{{{
nas -P /tmp/nas.lan.pid -l br0 -H 34954 -i eth1 -A -m 64 -r <share-key> -s linksys -w 4 -g 3600 -h <Radius IP> -p 1812 -t 36000
}}}

=== Security WPA2-PSK-TKIP Mixed ===
{{{
nas -P /tmp/nas.lan.pid -l br0 -H 34954 -i eth1 -A -m 132 -k <share-key> -s linksys -w 2 -g 3600
}}}

=== Security WPA2-RADIUS-TKIP Mixed ===
{{{
nas -P /tmp/nas.lan.pid -l br0 -H 34954 -i eth1 -A -m 66 -r <share-key> -s linksys -w 2 -g 3600 -h <Radius IP> -p 1812 -t 36000
}}}

=== Security WEP64bit -RADIUS ===
{{{
nas -P /tmp/nas.lan.pid -l br0 -H 34954 -i eth1 -A -m 32 -r <Radius share-key> -s linksys -w 1 -I 1 -K <WEP share key> -h <Radius IP> -p 1812 -t 36000
}}}

=== Security WEP64bit (same as security disabled and nas daemon is not running) ===
{{{
nas -P /tmp/nas.lan.pid -l br0 -H 34954
}}}

=== nas command options ===

The usage for nas is :
{{{
Usage: nas [options]
        -l    LAN interface name
        -i    Wireless interface name
        -k    WPA share-key
        -m    2 - WPA
              4 - PSK
              32 - 802.1X
              64 - WPA2
              66 - WPA WPA2
              128 - PSK2
              132 - PSK PSK2             
        -g    WPA GTK rotation interval
        -h    RADIUS server IP address
        -r    RADIUS secret
        -p    RADIUS server authentication UDP port
        -s    SSID
        -w    1 - WEP
              2 - TKIP
              4 - AES
              6 - AES+TKIP
        -P    nas pid file
        -I    WEP key index
        -K    WEP share key
        -H    UDP port on which to listen to requests
        -t    ??????

The -l <lan> option must be present first and then followed by -i <wl> ... options for each wireless interface

On "Supplicant"/"Client" side -l <lan> option can't be used. 

 -S|-A = Authenticator (NAS) or Supplicant

}}}


== More info ==

For more detail please read forum post

http://forum.openwrt.org/viewtopic.php?id=1836

For more detail about "Supplicant"/"Client" mode see http://forum.openwrt.org/viewtopic.php?pid=10703
