= nas =

{{{nas}}} is the binary, Broadcom proprietary, tool that sets up security connection on wireless device.

The usage for nas is :
{{{
Usage: nas [options]
        -l    LAN interface name
        -i    Wireless interface name
        -k    Shared secret
        -m    0:Radius, 1:WPA, 2:WPA-PSK, default:Radius
        -g    WPA GTK rotation interval
        -h    RADIUS server IP address
        -p    RADIUS server UDP port
        -s    Service Set Identity
        -w    Cryptographic algorithm: 2:TKIP, 4:AES
        -P    
The -l <lan> option must be present first and then followed by -i <wl> ... options for each wireless interface

 -S|-A = Authenticator (NAS) or Supplicant
 -H UDP port on which to listen to requests
}}}

The ["OpenWrtFaq"] contains information on how to enable WPA.

== From experimental build 2005-05-25 (whiteRusian included) ==

Current versions (both HEAD and whiterussian branch) use a new wireless driver (3.90.23.0). These versions require two changes:

* needs nas binary from Linksys beta firmware (4.50.05/4.00.5)

* PSK option changed from "-m 2" to "-m 4"


The nas binary can be found at: http://openwrt.alphacore.net/experimental/nas_0.2-1_mipsel.ipk
Remaining questions:

* What do the new "-m" options do?

* How to enable WPA2?

* Is it possible to extract nas binary from Linksys firmware image? Method from the wiki does not work anymore with this version.

Edit: My impression is "wl0_wep" key is not needed. So either set it to "disabled" or remove it.

Last edited by Yogi (2005-06-26 12:33:33)

Here are option of command nas of LINKSYS WRT54GS ver 4.50.5

1. Security disable

nas -P /tmp/nas.lan.pid -l br0 -H 34954

2. Security WPA-PSK TKIP

nas -P /tmp/nas.lan.pid -l br0 -H 34954 -i eth1 -A -m 4 -k <share-key> -s linksys -w 2 -g 3600

3. Security WPA-PSK AES

nas -P /tmp/nas.lan.pid -l br0 -H 34954 -i eth1 -A -m 4 -k <share-key> -s linksys -w 4 -g 3600

4. Security WPA-PSK TKIP+AES

nas -P /tmp/nas.lan.pid -l br0 -H 34954 -i eth1 -A -m 4 -k <share-key> -s linksys -w 6 -g 3600

5. Security WPA -RADIUS - TKIP

nas -P /tmp/nas.lan.pid -l br0 -H 34954 -i eth1 -A -m 2 -r <share-key> -s linksys -w 2 -g 3600 -h <Radius server ip> -p 1812 -t 36000

6. Security WPA2-PSK-TKIP

nas -P /tmp/nas.lan.pid -l br0 -H 34954 -i eth1 -A -m 128 -k <share-key> -s linksys -w 2 -g 3600

7. Security WPA2-RADIUS-TKIP

nas -P /tmp/nas.lan.pid -l br0 -H 34954 -i eth1 -A -m 64 -r <share-key> -s linksys -w 2 -g 3600 -h <Radius IP> -p 1812 -t 36000

8. Security WPA2-RADIUS-AES

nas -P /tmp/nas.lan.pid -l br0 -H 34954 -i eth1 -A -m 64 -r <share-key> -s linksys -w 4 -g 3600 -h <Radius IP> -p 1812 -t 36000

9. Security WPA2-PSK-TKIP Mixed

nas -P /tmp/nas.lan.pid -l br0 -H 34954 -i eth1 -A -m 132 -k <share-key> -s linksys -w 2 -g 3600

10. Security WPA2-RADIUS-TKIP Mixed

nas -P /tmp/nas.lan.pid -l br0 -H 34954 -i eth1 -A -m 66 -r <share-key> -s linksys -w 2 -g 3600 -h <Radius IP> -p 1812 -t 36000

11. Security WEP64bit -RADIUS

nas -P /tmp/nas.lan.pid -l br0 -H 34954 -i eth1 -A -m 32 -r <Radius share-key> -s linksys -w 1 -I 1 -K <WEP share key> -h <Radius IP> -p 1812 -t 36000

12. Security WEP64bit (same as security disabled and nas daemon is not running)

nas -P /tmp/nas.lan.pid -l br0 -H 34954

For more detail please read forum post

http://forum.openwrt.org/viewtopic.php?id=1836
