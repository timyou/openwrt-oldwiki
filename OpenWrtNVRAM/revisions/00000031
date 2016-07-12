[[TableOfContents]]

== General Settings ==
The WRT54G requires LAN and WAN settings at the least to properly boot. The specific settings/names are listed below, but this a bit of an overview:

There are 3 categories of interfaces, lan, wan and wifi[[FootNote(The wifi_* NVRAM variables are NONSTANDARD, intended to be used when lan_ifnames doesn't bridge lan and wireless. Most people should leave the wifi_* variables unset)]]. For each one of these categories you may set the following variables (ie lan_ifname, wan_ifname, wifi_ifname)

||'''Setting'''||'''Meaning/Purpose'''||
||'''*_ifname'''||The name of the interface which will be used for this category||
||'''*_ifnames'''||If the _ifname is a bridge (br0) then _ifnames is the interfaces to be bridged||
||'''*_proto'''||''static'', ''dhcp'' or ''none''. Method used to configure the interface||
||'''*_ipaddr'''||IP address to use if _proto is static||
||'''*_netmask'''||netmask to use if _proto is static (X.X.X.X notation)||
||'''*_gateway'''||gateway to use if _proto is static (X.X.X.X notation)||
||'''*_dns'''||dns to use if _proto is static (X.X.X.X notation)||
||'''*_stp'''||Enable spanning tree if _ifname is a bridge (0 or 1)||

== misc ==
DHCP Settings:
||'''NVRAM Setting'''||'''Meaning'''||
||'''dhcp_start'''||The starting IP address for DHCP assignments||
||'''dhcp_num'''||The number of addresses in DHCP pool||

Hostname:
||'''wan_hostname'''||The hostname of your router.||

== Wireless Configuration ==
Although the wifi_* variables can be used to configure the network settings of the wireless interface, the default setting is to include the wireless interface in lan_ifnames and leave the wifi_* variables unset. If you remove the wireless interface from the lan bridge (which you MUST do to use ad-hoc mode) configure the wifi_* variables according to the general settings above.

'''Note:''' There are wl_* and wl0_* variables; the wl_* variables are obsoleted and were replaced by wl0_*.

||'''NVRAM Setting'''||'''Meaning'''||
||'''wl0_ifname'''||Set by wlconf to the name of the ethernet interface (eth1, eth2)||
||'''wl0_hwaddr'''||Set by wlconf, use il0macaddr to change the mac||
||'''wl0_mode'''||Either ''ap'', ''sta'' or ''wet'' for Access Point mode, station mode or wireless ethernet bridge ||
||'''wl0_ap_isolate'''||(0/1) 0: allow clients to see each other  1: hide clients from each other ||
||'''wl0_infra'''||Select operation mode for ''sta'' and ''wet'' (0=ad-hoc, 1=infrastructure)||
||'''wl0_closed'''||(0/1) 0: broadcast ssid 1: hide ssid||
||'''wl0_country_code'''||AU = Worldwide, TH = Thailand, IL = Israel, JO = Jordan, CN = China, JP = Japan, US = USA/Canada/New Zealand, DE = Europe, All = All channels||
||'''wl0_macmode'''||(disabled/allow/deny) used to (allow/deny) mac addresses listed in wl0_maclist||
||'''wl0_maclist'''||List of space separated mac addresses to allow/deny according to wl0_macmode. Addresses should be entered with colons, e.g.: 00:02:2D:08:E2:1D ||
||'''wl0_radio'''||Enable / disable the radio (1=enable)||
||'''wl0_channel'''||The channel to use (1-13 worldwide, 1-11 USA/Canada, default 6, 0=auto channel)||
||||'''Note:''' Please take note of the appropriate range of channels for your country.  Many 802.11 client adapters can detect an AP on a channel that is not available in your country but will refuse to associate with it.  This can be very confusing and frustrating if you have set your OpenWRT radio to an channel which is not permitted in your region!||
||'''wl0_gmode'''||Set 54g modes (0=Legacy B, 1=auto, 2=G only, 3=B deferred, 4=performance, 5=LRS, 6=afterburner)||
||||'''Note:''' It may be necessary to use Legacy mode if you want older wireless devices to associate with a WRT access point.||
||'''wl0_gmode_protection'''|| ||
||'''wl0_rateset'''||all||
||'''wl0_plcphdr'''||preamble. long: use long or short preamble, *: use short preamble||
||'''wl0_rate'''||Set rate in 500 Kbps units (0=auto)||
||'''wl0_frag'''||Set fragmentation threshold (default 2346)||
||'''wl0_rts'''||Set RTS threshold (default 2347)||
||'''wl0_dtim'''||Set DTIM period (default 1)||
||'''wl0_bcn'''||Set beacon period (default 100)||
||'''wl0_frameburst'''||(on/off) enable/disable frameburst||
||'''wl0_antdiv'''||Select antenna (''-1=auto, 0=main''[near power jack]'', 1=aux''[near reset button]'', 3=diversity'') In WRT54G v2.0 and WRT54GS V1.1 is reversed 0=''[near reset button]'' and 1=''[near power jack]''||
||'''wl0_ssid'''||Set the SSID of the Wrt54g||

For WPA:
(See ["OpenWrtDocs/Configuration"] on how to enable WPA on current snapshots)
||'''wl0_auth_mode'''||obsolete, use '''wl0_akm'''||
||'''wl0_akm'''||''open,wpa,psk,wpa2,psk2''||
||'''wl0_wpa_psk'''||WPA pre-shared key||
||'''wl0_wpa_gtk_rekey'''||WPA GTK rekey interval||
||'''wl0_radius_ipaddr'''|| ||
||'''wl0_radius_key'''|| ||
||'''wl0_radius_port'''||Default value: ''1812''||


For WEP:
||'''wl0_wep'''||enabled/disabled||
||'''wl0_key1 ... wl0_key4'''||WEP keys (example: ''wl0_key1=DEADBEEF12'')[[FootNote(64bit/128bit wep is autodetected based on key length. For 64bit use 5/10 chars and for 128bit 13/26 chars len keys)]]||
||'''wl0_key'''||primary key index: the wl0_key[1234] used (values: ''1'',''2'',''3'',''4'')||

For WDS:
||'''wl0_lazywds'''||Set lazywds mode - dynamically grant WDS to anyone(''1=enable / 0=disable'')||
||'''wl0_wds'''||Space separated list of WDS member MAC addresses (xx:xx:xx:xx:xx:xx notation)||
'''NOTE:''' if you want to use a wrt54gs as a WDS client with '''wl0_wds''' set, the '''wl0_gmode''' setting must not be in afterburner (6) mode (apparently no linksys speedboost is available for WDS clients).  Also, '''wl0_mode''' should be set to ''ap''.

Misc:
||'''wl0_phytypes'''||Supported 802.11 modes, automatically set by wlconf||
||'''wl0_phytype'''||Attempt these 802.11 modes||
||'''wl0_corerev'''||Set by wlconf to the wireless revision, (4:v1.0 hardware, 7:v2,gs)||

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
nvram set static_route=10.1.2.0:255.255.255.0:0.0.0.0:1:vlan1
}}}

This will make 10.1.2.0 directly connected. To route via a router, use:

{{{
nvram set static_route=10.1.2.0:255.255.255.0:192.168.1.1:1:vlan1
}}}

This will use vlan1 to send packets to 10.1.2.0 via router 192.168.1.1

As of the most recent CVS build, all values must be present. The networking script doesn't detect missing values, and will thererfore not create the route if the syntax is incorrect (things missing, etc.).


== NVRAM committing ==

When you set/get nvram settings, you are get/setting them in RAM. "nvram commit" writes them persistenly to the flash. But you don't have to commit in order to test, in fact it's safer not to. You can save your settings to RAM, check them out by ifdown/ifup'ing all your interfaces, and then "nvram commit" them if they are to your liking. If not, you can reboot and you're back to the last working configuration you had.


== Applying changes to wireless settings ==

To apply the changes made to the nvram settings that start with '''`wl0_`''' (e.g. to the `wl0_maclist` entry) run the '''`wifi`''' command (or '''`wl`''' if you have not installed the wificonf package) to reconfigure the Broadcom `wl.o` module in the kernel.
