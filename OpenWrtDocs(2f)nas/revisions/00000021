= nas =

'''nas''' is the binary, Broadcom proprietary, tool that sets up security connection on wireless device.

''note:'' normally nas is called by the S41wpa script in /etc/init.d. This Script composes the command by reading the corresponding nvram variables (wl0_ssid, wl0_akm, wl0_crypto,...).


== Which nas to use? ==

From experimental build 2005-05-25 and whiterussian, OpenWRT use a new wireless driver (3.90.23.0). These versions require nas binary from Linksys beta firmware (4.50.05/4.00.5).

The nas binary can be found at: http://downloads.openwrt.org/whiterussian/packages/non-free

If you use old version of firmware, pleas upgrade. Please check forum for right version of nas for old firmware.

== How to configure? ==

If you installed the nas binary using the package indicated above, an install script is automatically added to the router. You can use the nvram to configure the nas options.

||'''Setting'''||'''nvram'''||'''Description'''||
||Wireless mode||wl0_mode||Using 'sta' will put the device in supplicant mode (client), otherwise it will be an authenticator (server).||
||Wireless device||wifi_ifname, lan_ifname||Wireless interface, the script will take the wifi_ifname by default. It if doesn't exist is will use lan_ifname. It will fallback to 'br0' if both dont' exist.||
||Real wireless device||wl0_ifname||Probably also correct too||
||SSID||wl0_ssid||The SSID configured for the wireless||
||WPA rekey||wl0_wpa_gtk_rekey||Rekeying interval in seconds. Defaults to 3600.||
||Authentication mode||wl0_akm||'wpa', 'wpa wpa2', 'wpa2', 'psk', 'psk psk2', 'psk2'.||
||Encryption mode for WPA||wl0_crypto||'tkip', 'aes', 'aes+tkip'.||
||Preshared key||wl0_wpa_psk||Specifies the preshared key. Only for psk/psk2||
||Radius Server IP||wl0_radius_ipaddr||Radius server IP address. Only for wpa/wpa2.||
||Radius Server Port||wl0_radius_port||Radius server port. Defaults to 1812. Only for wpa/wpa2.||
||Radius Server Shared Secret||wl0_radius_key||The shared secret with the Radius server. Only for wpa/wpa2.||

== nas options ==

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
              64 - WPA2
              66 - WPA WPA2
              4 - PSK
              128 - PSK2
              132 - PSK PSK2             
        -g    WPA GTK rotation interval
        -h    RADIUS server IP address
        -r    RADIUS secret
        -p    RADIUS server authentication UDP port
        -s    SSID
        -w    2 - TKIP
              4 - AES
              6 - AES+TKIP
        -P    nas pid file
        -I    WEP key index
        -K    WEP share key
        -H    UDP port on which to listen to requests
        -t    ??????

The -l <lan> option must be present first and then followed by -i <wl> ... options for each wireless interface

On "Supplicant" side -l <lan> option can't be used. see http://forum.openwrt.org/viewtopic.php?pid=10703

 -S|-A = Authenticator (NAS) or Supplicant

}}}


== More info ==

For more detail please read forum post

http://forum.openwrt.org/viewtopic.php?id=1836
