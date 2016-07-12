[[TableOfContents]]
== IP Interface Settings ==
In order to configure the IP interfaces on the system, a number of settings are grouped into "bundles" sharing the same prefix. The default bundles are called "lan", "wan" and "wifi", but those names have no special significance other than the fact that the startup script looks for bundles with these names. They might as well have been called "rod", "jane" and "freddy". In fact, let's demonstrate that:

{{{
freddy_ifname=vlan2
freddy_proto=static
freddy_ipaddr=192.168.100.100
freddy_netmask=255.255.255.0
freddy_gateway=192.168.100.1
}}}

In order to trigger the configuration of this interface, you'd type {{{ifup freddy}}}. This would configure the kernel IP interface {{{vlan2}}} with the given IP address and netmask, and also insert a defaultroute to 192.168.100.1 via this interface.

(Note: if you are perverse enough actually to want to call your IP interfaces "rod", "jane" and "freddy", you will have to modify {{{/etc/init.d/S40network}}} to call ifup appropriately. This is a useful thing to do if you want to configure extra IP interfaces on your system. You might want to separate off one of your ethernet ports and call it "dmz", for example)

So, let's be sensible and stick to the default "wan", "lan" and "wifi". The WRT54G requires LAN and WAN settings at least to boot properly. Since the "lan" bundle normally consists of the LAN ports bridged together with the wifi interface on the same subnet, most people should leave the wifi_* variables UNSET.

For each bundle you may set the following variables (ie lan_ifname, wan_ifname, wifi_ifname)

||'''Setting''' ||'''Meaning/Purpose''' ||
||'''*_ifname''' ||The name of the interface which will be used for this category ||
||'''*_ifnames''' ||If the _ifname is a bridge (br0) then _ifnames is the interfaces to be bridged ||
||'''*_proto''' ||''static'', ''dhcp'' or ''none''. Method used to configure the interface ||
||'''*_ipaddr''' ||IP address to use if _proto is static ||
||'''*_netmask''' ||netmask to use if _proto is static (X.X.X.X notation) ||
||'''*_gateway''' ||gateway to use if _proto is static (X.X.X.X notation) ||
||'''*_dns''' ||dns to use if _proto is static (X.X.X.X notation) ||
||'''*_stp''' ||Enable spanning tree if _ifname is a bridge (0 or 1) ||
||'''*_hwaddr''' ||MAC address of the interface if different from the factory default (xx:xx:xx:xx:xx:xx) ||


Don't set {{{*_gateway}}} more than once, or use {{{*_proto=dhcp}}} on more than one interface, or you'll find yourself with multiple default routes inserted which is probably not what you want.

After changing any of these settings, type {{{ifup foo}}} (where foo is one of lan, wan, wifi etc as appropriate)

== Bridging ==
You can create a layer 2 (ethernet) bridge between two or more interfaces by setting {{{foo_ifname=br0}}} and {{{foo_ifnames="iface1 iface2 iface3..."}}}. Typically you will see something similar to this in your default settings:

{{{
lan_ifname=br0
lan_ifnames="vlan0 eth1"
lan_ipaddr=192.168.1.1
lan_netmask=255.255.255.0
lan_proto=static
lan_stp=1
}}}

In this case, the IP address is assigned to the bridge device (br0), and the bridge device connects interfaces vlan0 and eth1, corresponding to LAN ports 1-4 and the wireless interface respectively.

Note: the [:OpenWrtDocs/Configuration#NetworkInterfaceNames:network interface names] corresponding to physical ports on the Wrt vary from one brand and model of router to another. Your particular device may use different settings to those shown above.

== VLAN Settings ==
Because of the way the interfaces are done in hardware (one interface, multiple ports), there are required ''vlan'' settings for the device. If these aren't set to the proper values, then the interfaces will not be assigned correctly. Note that if you're using ''admcfg'' or similar, this may not apply to you. (I'm not sure).

Be sure the NVRAM has settings for the following, and the recommended defaults:

||'''NVRAM Setting''' ||'''Recommended Value''' ||
||'''vlan0hwname''' ||et0 ||
||'''vlan0ports''' ||1 2 3 4 5* ||
||'''vlan1hwname''' ||et0 ||
||'''vlan1ports''' ||0 5 ||


In other words, an interface called "vlan0" is linked to ports 1-4 of the internal switch (typically labelled "LAN 1-4" on the box, although you may find that they are in reverse order),and an interface called "vlan1" is linked to port 0 of the internal switch (typically labelled "WAN" on the box). Port 5 of the internal switch carries all VLANs tagged (that's what the asterisk is for) to the real interface et(h)0.

{{{
PHYSICALLY:
                   tagged     +-------------------+
            eth0 ============ | 5      SWITCH     |
                              | 4   3   2   1   0 |
                              +-------------------+
                                |   |   |   |   |
                                ...LAN 1-4...  WAN

LOGICALLY:
            vlan0 ------------- LAN 1-4
            vlan1 ------------- WAN
}}}

If the NVRAM is set with those values, then the recommended values for '''wan_ifnames''' and '''lan_ifnames''' will be correct. Note that by changing the ports around, you are able to change which port is the WAN port and so on, but that isn't a very good idea in general.

Now let's say you want to syphon off the port labelled "LAN 1" as a DMZ port on a separate subnet. On an Asus router this is actually switch port 4. So you'd reconfigure as:

||'''vlan0hwname''' ||et0 ||
||'''vlan0ports''' ||1 2 3 5* ||
||'''vlan1hwname''' ||et0 ||
||'''vlan1ports''' ||0 5 ||
||'''vlan2hwname''' ||et0 ||
||'''vlan2ports''' ||4 5 ||


Once you've done this, you can configure interface {{{vlan2}}} with its own IP address on its own subnet, and Wrt will route between them.

{{{
dmz_ifname=vlan2
dmz_ipaddr=192.168.2.1
dmz_netmask=255.255.255.0
dmz_proto=static
}}}

Type {{{ifup dmz}}} to perform the configuration, and modify {{{/etc/init.d/S40network}}} so that this is done when your box is next rebooted too. See DemilitarizedZoneHowto for more details.

Another possibility is that if you don't need a separate WAN port, you could get rid of vlan1 and configure vlan0 so that all 5 ports are on the LAN subnet. Going to the other extreme, you could configure five separate vlans and have a five-port ethernet router.

== Wireless Configuration ==
Although the wifi_* variables can be used to configure the IP network settings of the wireless interface, the default setting is to include the wireless interface in lan_ifnames and leave the wifi_* variables unset. If you remove the wireless interface from the lan bridge (which you MUST do to use ad-hoc mode) configure the wifi_* variables according to the general settings above.

There are separate variables called wl0_* which configure the characteristics of the ''physical'' wireless interface - which are applicable whether or not the wifi interface is bridged or a separate IP network.

'''Note:''' There are wl_* and wl0_* variables; the wl_* variables are obsoleted and were replaced by wl0_*.

||'''NVRAM Setting''' ||'''Meaning''' ||
||'''wl0_ifname''' ||Set by wlconf to the name of the ethernet interface (eth1, eth2) ||
||'''wl0_hwaddr''' ||Set by wlconf, use il0macaddr to change the mac ||
||'''wl0_mode''' ||Either ''ap'', ''sta'' or ''wet'' for Access Point mode, station mode or wireless ethernet bridge ||
||'''wl0_ap_isolate''' ||(0/1) 0: allow clients to see each other  1: hide clients from each other ||
||'''wl0_infra''' ||Select operation mode for ''sta'' and ''wet'' (0=ad-hoc, 1=infrastructure) ||
||'''wl0_closed''' ||(0/1) 0: broadcast ssid 1: hide ssid ||
||'''wl0_country_code''' ||AU = Worldwide, TH = Thailand, IL = Israel, JO = Jordan, CN = China, JP = Japan, US = USA/Canada/New Zealand, DE = Europe, All = All channels ||
||'''wl0_macmode''' ||(disabled/allow/deny) used to (allow/deny) mac addresses listed in wl0_maclist ||
||'''wl0_maclist''' ||List of space separated mac addresses to allow/deny according to wl0_macmode. Addresses should be entered with colons, e.g.: 00:02:2D:08:E2:1D ||
||'''wl0_radio''' ||Enable / disable the radio (1=enable) ||
||'''wl0_channel''' ||The channel to use (default 6, 0=auto channel) ||
||||<style="text-align: center;">'''Note:'''Please take note of the appropriate range of channels for your country.  Many 802.11 client adapters can detect an AP on a channel that is not available in your country but will refuse to associate with it.  This can be very confusing and frustrating if you have set your OpenWRT radio to an channel which is not permitted in your region.  Permitted channel usage is as follows: Africa/Asia/Australia/Europe/South­ America: 1 - 13, Canada/United States: 1 - 11, France: 11 - 13, Israel: 5 - 7, Japan: 1 - 14, Mexico: 11 ||
||'''wl0_gmode''' ||Set 54g modes (0=Legacy B, 1=auto, 2=G only, 3=B deferred, 4=performance, 5=LRS, 6=afterburner) ||
||||<style="text-align: center;">'''Note:''' It may be necessary to use Legacy mode if you want older wireless devices to associate with a WRT access point.  If wl0_gmode is not set, the wireless adapter will operate as if it were set to 0. ||
||'''wl0_gmode_protection''' ||For situations where not all wifi stations hear each other ||
||'''wl0_rateset''' ||all ||
||'''wl0_plcphdr''' ||preamble. long: use long or short preamble, *: use short preamble ||
||'''wl0_rate''' ||Set rate in 500 Kbps units (0=auto) ||
||'''wl0_txpwr''' ||Set transmit power in miliwatts ||
||'''wl0_frag''' ||Set fragmentation threshold (default 2346) ||
||'''wl0_rts''' ||Set RTS threshold (256-2347 default 2347) ||
||'''wl0_dtim''' ||Set DTIM period (default 1) ||
||'''wl0_bcn''' ||Set beacon period (default 100) ||
||'''wl0_frameburst''' ||(on/off) enable/disable frameburst ||
||'''wl0_antdiv''' ||Select antenna (''-1=auto, 0=main''[near power jack]'', 1=aux''[near reset button]'', 3=diversity'') Starting with WRT54G v2.0 and WRT54GS V1.1 these are reversed 0=''[near reset button]'' and 1=''[near power jack]'' ||
||'''wl0_txant''' ||See wl -h||
||'''wl0_ssid''' ||Set the SSID of the Wrt54g ||
||'''wl0_distance''' || (per Whiterussian RC5) Adjusts timing for signal propagation time. Unit: [m] (one-way). Setting this variable overrules setting of shortslot/longslot timing. Setting this variable is only needed over distances greater than appr. 1.5 km. The need usually shows when communication throughput is very low although the ratio of signal strength to noise is good. ||
||'''wl0_wdstimeout''' ||if set, it will enable the WDS watchdog (e. g. wl0_wdstimeout=180, value is in seconds) ||


For WPA: (See ["OpenWrtDocs/Configuration"] on how to enable WPA on current snapshots)

||'''wl0_auth_mode''' ||obsolete, use '''wl0_akm''' NOTE: set to psk or radius because some configurations don't work without it. See http://www.bingner.com/openwrt/wpa.html, http://wiki.openwrt.org/OpenWrtDocs/Wpa2Enterprise or maybe you can use some other wpa supplicant instead of nas ||
||'''wl0_akm''' ||''open,wpa,psk,wpa2,psk2'' ||
||'''wl0_wpa_psk''' ||WPA pre-shared key ||
||'''wl0_wpa_gtk_rekey''' ||WPA GTK rekey interval ||
||'''wl0_radius_ipaddr''' || ||
||'''wl0_radius_key''' || ||
||'''wl0_radius_port''' ||Default value: ''1812'' ||


For WEP:

||'''wl0_wep''' ||enabled/disabled ||
||'''wl0_key1 ... wl0_key4''' ||WEP keys (example: ''wl0_key1=DEADBEEF12'')[[FootNote(64bit/128bit wep is autodetected based on key length. For 64bit use 5/10 chars and for 128bit 13/26 chars len keys)]] ||
||'''wl0_key''' ||primary key index: the wl0_key[1234] used (values: ''1'',''2'',''3'',''4'') ||
||'''wl0_auth''' || 1 (shared key) / 0 (open); the 'shared key' option is the most vulnerable WEP option as it most facilitates an intruder due to a fundamental security flaw in WEP. The 'open' setting will allow association but will make it an intruder more difficult to find the encryption key, needed for traffic. ||


For WDS:

||'''wl0_lazywds''' ||Set lazywds mode - dynamically grant WDS to anyone(''1=enable / 0=disable'') ||
||'''wl0_wds''' ||Space separated list of WDS member MAC addresses (xx:xx:xx:xx:xx:xx notation) ||


'''NOTE:''' if you want to use a wrt54gs as a WDS client with '''wl0_wds''' set, the '''wl0_gmode''' setting must not be in afterburner (6) mode (apparently no linksys speedboost is available for WDS clients).  Also, '''wl0_mode''' should be set to ''ap''.

Misc:

||'''wl0_phytypes''' ||Supported 802.11 modes, automatically set by wlconf ||
||'''wl0_phytype''' ||Attempt these 802.11 modes ||
||'''wl0_corerev''' ||Set by wlconf to the wireless revision, (4:v1.0 hardware, 7:v2,gs) ||


In summary, you could find the wifi interface known by three different identifiers: as {{{wl0_*}}} for the physical interface settings, as {{{wifi_*}}} for its IP settings if it's on a separate subnet, and as {{{eth1}}} or {{{eth2}}} to the kernel, depending on your hardware. Confused? :)

== Static Routes ==
Static routes are a bit uglier to maintain, but they are still maintainable. Until RC5 there is only one NVRAM setting for them: '''{{{static_route}}}'''. This contains all the static routes to be added upon boot-up. From RC6 there can be '''{{{<ifname>_static_route}}}''' NVRAM variables for each interface, e.g. '''{{{lan_static_route}}}'''.

The syntax of the {{{static_route}}} NVRAM variable is as follows:

{{{
  static_route=ip:netmask:gatewayip:metric:interface # until RC5
  interface_static_route=ip:netmask:gatewayip:metric # from RC6
}}}

So, for example, to set a static route to 10.1.2.0/255.255.255.0 via vlan1, use:

{{{
nvram set static_route=10.1.2.0:255.255.255.0:0.0.0.0:1:vlan1 # until RC5
nvram set lan_static_route=10.1.2.0:255.255.255.0:0.0.0.0:1 # from RC6
}}}

This will make 10.1.2.0 directly connected. To route via a router, use:

{{{
nvram set static_route=10.1.2.0:255.255.255.0:192.168.1.1:1:vlan1 # until RC5
nvram set lan_static_route=10.1.2.0:255.255.255.0:192.168.1.1:1 # from RC6
}}}

This will use vlan1 to send packets to 10.1.2.0 via router 192.168.1.1

As of the most recent CVS build, all values must be present. The networking script doesn't detect missing values, and will thererfore not create the route if the syntax is incorrect (things missing, etc.).

To add multiple routes, seperate each route formatted as above with a space. To avoid the shell truncating after the first space, you need to quote:

{{{
nvram set static_route="10.1.2.0:255.255.255.0:192.168.1.1:1:vlan1 10.1.3.0:255.255.255.0:192.168.1.1:1:vlan1" # until RC5
nvram set lan_static_route="10.1.2.0:255.255.255.0:192.168.1.1:1 10.1.3.0:255.255.255.0:192.168.1.1:1" # from RC6
}}}

To see if the new settings are working, try
{{{
  # ifup lan
}}}

If you need to debug this, 
{{{
  # DEBUG=echo ifup lan
}}}

This will list all the commands to be run.  You can then copy and paste the "route" command from the output, and run it by hand to see what's wrong.

== misc ==
DHCP Settings:

||'''NVRAM Setting''' ||'''Meaning''' ||
||'''dhcp_start''' ||The starting offset for DHCP assignments ||
||'''dhcp_num''' ||The number of addresses in DHCP pool ||


Unsetting these values will not stop the dhcp server from running; it will use default values of dhcp_start=100 and dhcp_num=150. To turn off the dhcp server, use {{{chmod -x /etc/init.d/S50dnsmasq}}} [jffs2 systems] or {{{rm /etc/init.d/S50dnsmasq}}} [squashfs systems]

NOTE: In the unlikely event you're using a lan_netmask other than 255.255.255.0, be aware that {{{dhcp_start}}} is an offset into your network segment, as described by {{{int2ip(ip2int(lan_ipaddr)&ip2int(lan_netmask))}}}.  Furthermore, the startup script S50dnsmasq does not allow for the possibility that you might want to run DHCP servers on multiple interfaces, or that you might want to run it on a different interface than lan_*

Hostname:

||'''wan_hostname''' ||The hostname of your router. ||


[[Anchor(NVRAMCommitting)]]
== NVRAM committing ==
When you set/get nvram settings, you are get/setting them in RAM. "nvram commit" writes them persistenly to the flash. But you don't have to commit in order to test, in fact it's safer not to because the flash memory has a limited write cycle life. (Don't be scared though, it's something like 1000-10.000 times; still better to only save it when really needed! NB In ["Faq"] it is however stated that this figure, according to manufacturers, can be in the range of 100,000 - 1,000,000) You can save your settings to RAM, check them out by ifdown/ifup'ing all your interfaces, and then "nvram commit" them if they are to your liking. If not, you can reboot and you're back to the last working configuration you had.

== Applying changes to wireless settings ==
To apply the changes made to the nvram settings that start with '''{{{wl0_}}}''' (e.g. to the {{{wl0_maclist}}} entry) run the '''{{{wifi}}}''' command (or '''{{{wl}}}''' if you have not installed the wificonf package) to reconfigure the Broadcom {{{wl.o}}} module in the kernel.
