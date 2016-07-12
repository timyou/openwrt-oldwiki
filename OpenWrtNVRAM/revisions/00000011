[[TableOfContents]]

== General Settings ==
The WRT54G requires LAN and WAN settings at the least to properly boot. The specific settings/names are listed below, but this a bit of an overview:

There are 3 categories of interfaces, lan, wan and wifi[[FootNote(The wifi_* NVRAM variables are NONSTANDARD, intended to be used when lan_ifnames doesn't bridge lan and wireless. Most people should leave the wifi_* variables unset)]]. For each one of these categories you may set the following variables (ie lan_ifname, wan_ifname, wifi_ifname)
||'''Setting'''||'''Meaning/Purpose'''||
||'''*_ifname'''||The name of the interface which will be used for this category||
||'''*_ifnames'''||If the _ifname is a bridge (br0) then _ifnames is the interfaces to be bridged||
||'''*_proto'''||''static'' or ''dhcp'', method used to configure the interface||
||'''*_ipaddr'''||IP address to use if _proto is static||
||'''*_netmask'''||netmask to use if _proto is static (X.X.X.X notation)||
||'''*_stp'''||Enable spanning tree if _ifname is a bridge (0 or 1)||

== LAN Configuration ==
The LAN settings used are:

||'''NVRAM Setting'''||'''Meaning'''||
||'''lan_ifname'''||The interface name to assign to the LAN segments (wireless and switch ports). This should be ''br0''||
||'''lan_ifnames'''||This is set to the interfaces you wish to bridge together into one LAN (recommend ''vlan0 eth1 eth2 eth3'')(use  ''vlan2 eth1 eth2 eth3'' with rev.1.1 routers)||
||'''lan_hwnames'''||The hardware driver names for this interface||
||'''lan_proto'''||How to assign the LAN address. (This will be forced to ''static'' by networking.sh[[FootNote(Often lan_proto is incorrectly set to ''dhcp'' but configured as static, networking.sh compensates by forcing lan_proto=static, edit networking.sh if you wish to use dhcp)]])||
||'''lan_ipaddr'''||LAN IP Address to be used for the 4 port switch and the wireless. This is the internal IP of the router.||
||'''lan_netmask'''||The Netmask (255.255.255.0 format) for the LAN IP you have assigned.||
||'''lan_stp'''||Whether or not to enable Spanning Tree Protocol on the bridge device (bridging the wireless and LAN segments) (0 (default) or 1)||
||'''lan_gateway''||The IP address of the LAN gateway.||

== WAN Configuration ==
The WAN settings used are:

||'''NVRAM Setting'''||'''Meaning'''||
||'''wan_ifname'''||The interface name to assign to the WAN. This should be ''vlan1''||
||'''wan_ifnames'''||Ignored since wan_ifname isn't a bridge device||
||'''wan_proto'''||How to assign the WAN address. This should be ''static'' or ''dhcp'' (The Linksys firmware also uses pppoe and disabled)||
||'''wan_ipaddr'''||Public IP address to be assigned to the router. This is the external IP of the router, and the IP which masquerading/NAT will use. (wan_proto=static only)||
||'''wan_netmask'''||The Netmask (255.255.255.0 format) for the WAN IP you have assigned. (wan_proto=static only)||
||'''wan_gateway'''||The default gateway to setup via the WAN port. (wan_proto=static only)||
||'''wan_dns'''||The DNS server to use on the WAN interface. (wan_proto=static only)||
||'''wan_hostname'''||The hostname of your router.||

== Wireless Configuration ==
Although the wifi_* variables can be used to configure the network settings of the wireless interface, the default setting is to include the wireless interface in lan_ifnames and leave the wifi_* variables unset. If you remove the wireless interface from the lan bridge you can use the following settings:
||'''wifi_ifname'''||The wireless interface (eth1 or eth2 depending on hardware revision)||
||'''wifi_proto'''||''static'' or ''dhcp'', method used to configure the interface||
||'''wifi_ipaddr'''||IP address to use if wifi_proto is static||
||'''wifi_netmask'''||netmask to use if wifi_proto is static (X.X.X.X notation)||

||'''NVRAM Setting'''||'''Meaning'''||
||'''wl0_ifname'''||Set by wlconf to the name of the ethernet interface (eth1, eth2)||
||'''wl0_hwaddr'''||Set by wlconf, use il0macaddr to change the mac||
||'''wl0_mode'''||Either ''ap'', ''sta'' or ''wet'' for Access Point mode, station mode or wireless ethernet bridge ||
||'''wl0_infra'''||Select operation mode for ''sta'' and ''wet'' (0=ad-hoc, 1=infrastructure)||
||'''wl0_closed'''||(0/1) 0: broadcast ssid 1: hide ssid||
||'''wl0_country_code'''||AU = Worldwide, TH = Thailand, IL = Israel, JO = Jordan, CN = China, JP = Japan, US = USA/Canada/New Zealand, DE = Europe, All = All channels||
||'''wl0_macmode'''||(disabled/allow/deny) used to (allow/deny) mac addresses listed in wl0_maclist||
||'''wl0_maclist'''||List of space separated mac addresses to allow/deny according to wl0_macmode. Addresses should be entered with colons, e.g.: 00:02:2D:08:E2:1D ||
||'''wl0_radio'''||Enable / disable the radio (1=enable)||
||'''wl0_phytypes'''||Supported 802.11 modes, automatically set by wlconf||
||'''wl0_phytype'''||Attempt these 802.11 modes||
||'''wl0_corerev'''||Set by wlconf to the wireless revision, (4:v1.0 hardware, 7:v2,gs)||
||'''wl0_channel'''||The channel to use (1-13 worldwide, 1-11 USA/Canada, default 6, 0=auto channel)||
||'''wl0_gmode'''||Set 54g modes (0=Legacy B, 1=auto, 2=G only, 3=B deferred, 4=performance, 5=LRS, 6=afterburner)||
||'''wl0_gmode_protection'''|| ||
||'''wl0_rateset'''||all||
||'''wl0_plcphdr'''||preamble. long: use long or short preamble, *: use short preamble||
||'''wl0_rate'''||Set rate in 500 Kbps units (0=auto)||
||'''wl0_frag'''||Set fragmentation threshold (default 2346)||
||'''wl0_rts'''||Set RTS threshold (default 2347)||
||'''wl0_dtim'''||Set DTIM period (default 1)||
||'''wl0_bcn'''||Set beacon period (default 100)||
||'''wl0_frameburst'''||(on/off) enable/disable frameburst||
||'''wl0_antdiv'''||Select antenna (-1=auto, 0=main, 1=aux, 3=diversify)||
||'''wl0_ssid'''||Set the SSID of the Wrt54g||

For WPA:
(See ["OpenWrtFaq"] on how to enable WPA on current snapshots)
||'''security_mode'''||disabled,radius,wpa,psk,wep||
||'''wl0_auth_mode'''||radius,wpa,psk||
||'''wl_wpa_psk'''||WPA pre-shared key||
||'''wl_wpa_gtk_rekey'''||WPA GTK rekey interval||
(Broken?, unsupported?... But in the Linksys code!)
||'''wl_radius_ipaddr'''|| ||
||'''wl_radius_key'''|| ||
||'''wl_radius_port'''||Default value: 1812||


For WEP:
||'''wl0_wep'''||on/off (At least for the WRT54G (v2.2) the wl0_wep parameter has to be to disabled/enabled, not to on/off...)||
||'''wl0_key1 ... wl0_key4'''||WEP keys (example: wl0_key1=DEADBEEF12)[[FootNote(64bit/128bit wep is autodetected by ''wlconf'' based on key length. For 64bit use 5/10 chars and for 128bit 13/26 chars len keys)]]||
||'''wl0_key'''||primary key index||


For WDS:
||'''wl0_lazywds'''||Set lazywds mode - dynamically grant WDS to anyone(1=enable / 0=disable)||
||'''wl0_wds'''||Space separated list of WDS member MAC addresses (xx:xx:xx:xx:xx:xx notation)||
'''NOTE:''' if you want to use a wrt54gs as a WDS client with '''wl0_wds''' set, the '''wl0_gmode''' setting must not be in afterburner (6) mode (apparently no linksys speedboost is available for WDS clients).  Also, '''wl0_mode''' should be set to ap.

See [wlconf] for more information on the settings used by the ["wlconf"]/wifi commands
== VLAN Settings ==
Because of the way the interfaces are done in hardware (one interface, multiple ports), there are required ''vlan settings for the device. If these aren't set to the proper values, then the interfaces will not be assigned correctly. Note that if you're using ''admcfg'' or similar, this may not apply to you. (I'm not sure).

Be sure the NVRAM has settings for the following, and the recommended defaults:

||'''NVRAM Setting'''||'''Recommended Value'''||
||'''vlan0hwname'''||et0||
||'''vlan0ports'''||1 2 3 4 5*||
||'''vlan1hwname'''||et0||
||'''vlan1ports'''||0 5||

If the NVRAM is set with those values, then the recommended values for '''wan_ifnames''' and '''lan_ifnames''' will be correct. Note that by changing the ports around, you are able to change which port is the WAN port and so on, but that isn't a very good idea in general.

== Static Routes ==
Static routes are a bit uglier to maintain, but they are still maintainable. There is only one NVRAM setting for them: '''`static_route`'''. This contains all the static routes to be added upon boot-up.

The syntax of the `static_route` NVRAM variable is as follows:

`static_route=ip:netmask:gatewayip:metric:interface`

So, for example, to set a static route to 10.1.2.0/255.255.255.0 via vlan1, use:

{{{
@OpenWrt:/# nvram set static_route=10.1.2.0:255.255.255.0:0.0.0.0:1:vlan1
}}}

This will make 10.1.2.0 directly connected. To route via a router, use:

{{{
@OpenWrt:/# nvram set static_route=10.1.2.0:255.255.255.0:192.168.1.1:1:vlan1
}}}

This will use vlan1 to send packets to 10.1.2.0 via router 192.168.1.1

As of the most recent CVS build, all values must be present. The networking script doesn't detect missing values, and will thererfore not create the route if the syntax is incorrect (things missing, etc.).


== NVRAM committing ==

When you set/get nvram settings, you are get/setting them in RAM. "nvram commit" writes them persistenly to the flash. But you don't have to commit in order to test, in fact it's safer not to. You can save your settings to RAM, check them out by ifdown/ifup'ing all your interfaces, and then "nvram commit" them if they are to your liking. If not, you can reboot and you're back to the last working configuration you had.
