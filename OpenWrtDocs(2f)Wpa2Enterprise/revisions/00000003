One success story with Openwrt / WPA2 / Freeradius / Mac OSX follows. 

== NVRAM Settings ==
I combined possibly outdated docs and got a setup working. Here's what I had to change in NVRAM:

{{{
wl0_akm=wpa wpa2
wl0_auth_mode=radius
wl0_crypto=aes+tkip
wl0_radius_ipaddr=127.0.0.1
wl0_radius_key=myVeryLongSecretString
wl0_radius_port=1812
wl0_ssid=myNetworksSSID
wl0_wep=aes+tkip
}}}

Two mysteries here:
1. Although the [:OpenWrtDocs/Configuration#WPA] docs say that `wl0_auth_mode` is deprecated, [http://www.bingner.com/openwrt/wpa.html this page] linked from the forums suggested it should be either `psk` or `radius`.  It didn't seem to hurt anything, and I didn't get it working until I set it to radius, so perhaps there's something there.
2. My device has both `wl_` and `wl0_` prefix variables; I set both of them out of superstition but only list the wl0_ ones above.  Anyone know why this is so?

Don't forget to `nvram commit` ! 

== FreeRadius ==
Using ipkg, get all the freeradius-* packages. You'll need to edit four files: clients.conf, eap.conf, radiusd.conf and users, plus configure certificates properly (handled under the eap.conf section below).

=== clients.conf ===
This just needs to match the value for wl0_radius_key:
{{{
client 127.0.0.1 {
        secret          = myVeryLongSecretString
        shortname       = localhost
        nastype     = other     # localhost isn't usually a NAS...
}
}}}
=== eap.conf ===
This file is included by radiusd.conf. Here's mine, stripped of all comments and blanks.
{{{
       eap {
                default_eap_type = tls
                timer_expire     = 60
                ignore_unknown_eap_types = no
                cisco_accounting_username_bug = no
                md5 {
                }
                tls {
                        private_key_password = seekritpassword
                        private_key_file = ${raddbdir}/certs/14.key
                        certificate_file = ${raddbdir}/certs/14.pem
                        CA_file = ${raddbdir}/certs/my-cacert.pem
                        dh_file = ${raddbdir}/certs/dh
                        random_file = ${raddbdir}/certs/random
                        fragment_size = 1024
                }
                ttls {
                        default_eap_type = md5
                        copy_request_to_tunnel = no
                        use_tunneled_reply = no

                }
                 peap {
                        default_eap_type = mschapv2
                }
                mschapv2 {
                }

        }
}}}
The freeradius-samplecerts ipkg will install some 'snakeoil' certificates that you can use if you want; I already had a CA set up at work using the excellent [http://devel.it.su.se/pub/jsp/polopoly.jsp?d=1026&a=3290 CSP package] so I just generated a new one for my server. Although the comments in the distributed file suggest not using MD5 as an EAP type, pre-WinXP-SP2 machines only know how to do MD5 (reference: [http://www.freeradius.org/doc/EAP-MD5.html freeradius.org doc]), so I've enabled it. 

=== radiusd.conf ===
Huge file as distributed. I've massively cut mine down to save space and cut out things that the freeradius ipkg doesn't support (all the backends, proxying, neato logging, etc do not work). It's still quite long, but here are JUST THE IMPORTANT PARTS. I'll attach the real file to this wiki page for downloading.

{{{
thread pool {
        start_servers = 1
        max_servers = 4
        min_spare_servers = 1
        max_spare_servers = 3
        max_requests_per_server = 0
}
$INCLUDE  ${confdir}/clients.conf
modules {

        pap {
                encryption_scheme = clear
        }
        chap {
                authtype = CHAP
        }
        mschap {
                authtype = MS-CHAP
                with_ntdomain_hack = yes
        }

        mschapv2 {
        }
        $INCLUDE ${confdir}/eap.conf
        files {
                usersfile = ${confdir}/users
                compat = no
        }
}
authorize {

        files
        eap
}
authenticate {
        eap
}
}}}
Basically we've cut it down from being enterprise-ready (10 simultaneous processes!) down to something that'll work on the embedded OS/device in openwrt, and disabled everything except what's necessary for EAP.

=== users ===
Once again -- huge file, completely unnecessary for our purposes. Here is all you really need:

{{{
DEFAULT Group == "disabled", Auth-Type := Reject
                Reply-Message = "Your account has been disabled."
mysername    User-Password == "mySeekritPassword"
}}}

== Client Configuration ==
For my MacBook Pro, I had to pick the 802.1X type manually in System Preferences - Network - AirPort - Edit (SSID). I Picked ""Wireless Security"": WPA2 Enterprise, put username and password, and picked ""802.1X Configuration"": TTLS - PAP.  This forced it to use the cleartext password in the users file.

== Debugging ==
Run radiusd in full-monty debug mode: `/usr/sbin/radiusd -X -A` and you'll see each packet come in and each step of the transaction. Very helpful because the WRT doesn't tell you nuffin' !
