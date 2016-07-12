The Asus WL-500g Premium seems to be supported by OpenWrt.

== Installation ==
It's possible (and really easy) to use manufacturers own web interface (at 192.168.1.1) to download OpenWrt into the WL-500gP box. This way at least [http://downloads.openwrt.org/whiterussian/rc5/bin/openwrt-brcm-2.4-jffs2-4MB.trx this image] (Whiterussian-rc5, jffs2, 4MB) is working.

( Alright ... but on my wl500gp I had to use tftp and above definitely didnot work. )

==== Network ====
For information on the internal network architecture and how physical ports map to vlans and bridges, see [:OpenWrtDocs/NetworkInterfaces:NetworkInterfaces]

==== Missing some RAM ====
If you look at "dmesg", for example, there's only 16MB of RAM. Specs says there should be 32MB.

 . This is how you get all 32MB for use:
{{{
root@OpenWrt:~/# nvram set sdram_init=0x0009
root@OpenWrt:~/# nvram set sdram_ncdl=0
root@OpenWrt:~/# nvram commit
root@OpenWrt:~/# reboot
}}}
== Few problems with the WL-500gP ==
The reset button does not work (due largely to mis-mapped /proc/sys/reset)

[wiki:WikiPedia:GPIO gpio] 0 = RESTORE button (reset) (00 = unpressed, 01 = pressed)

gpio 1 = Power LED (enable = off, disable = on)

gpio 4 = EZ SETUP button (similar to linksys "button"?) (00 = unpressed, 01 = pressed)

 . It seams as tho the only method of flashing this router (at the moment) is to use a tftp client & upload firmware when the router is in diag mode. To put the router in diag mode, unplug the router & push & hold the RESTORE button then plug the router in. Wait for a slow blinking power light & presto you're in diag mode. Then tftp the image to the router. After a few minutes, unplug/plug the router. I've (thecompwiz) had to do this twice before the firmware took... but it definately works. After firmware is installed, you should be able to log into the router via telnet. Set the root password & you need to make a few nvram setting changes.... Since this router was not in the "supported" category when RC5 was released... there are a few things to change:
  . {{{
nvram set lan_ifnames="vlan0 eth2"
nvram set wlan_ifname=eth2
nvram set br0_ifnames="vlan0 eth1"
nvram set wan0_ifname=eth0
nvram set wan_ifnames=eth0
nvram set wl0_ifname=eth2
nvram set lan_ifname=br0
nvram set wifi_ifname=eth2
nvram set wan_ifname=vlan1
nvram set wan0_ifnames=eth0
nvram set primary_ifname=eth0}}}

(don't forget to commit WikiPedia:nvram changes)

{{{
nvram commit
}}}

----
 . VespaTS: Couldn't get [wiki:WikiPedia:PPPoE PPPOE] to work. To get pppoe running I had to change again some settings:
wan_device=eth0 (it was set to vlan1)

Could an experienced WL-500gP user update [:OpenWrtDocs/Configuration#NetworkInterfaceNames:this table]?

***Caution** I've (thecompwiz)been having troubles if I set wan_proto=none It appears as if it breaks the vlan0.

=== Wrong vlan ports ===
I was unable to ping my ADSL modem (some Alcatel) connected to the WAN port. The problem was the vlan configuration. `nvram get vlan1ports` showed `"0 5u"` (could anyone describe what this means?). I changed it to `"0 5*"` (like the config of vlan0) and this solved my problem.

''''''

Use the following settings in order to get the dedicated WAN port working in case of troubles:

{{{nvram set wan_ifname=vlan1
nvram set vlan1ports="0 5*"
nvram set vlan0ports="1 2 3 4 5*" }}}

Maybe you also need to change the wifi settings:

{{{nvram set wifi_ifname=eth2
nvram commit}}}

=== DHCP server & client settings ===

To act as a DHCP-client towards WAN set the following:

{{{nvram set wan0_proto=dhcp
nvram set wan_proto=dhcp
nvram commit}}}

To act as a DHCP-server towards LAN set the following:

{{{nvram set default_lan_proto=dhcp_server
nvram set lan_dhcp=1
nvram set dhcp_enable_x=1
nvram commit}}}

These settings are optional and not necessary for dhcp to function:

{{{nvram set dhcp1_start=192.168.2.222
nvram set dhcp_start=222 # will cause to set DHCP IP address pool begin at 192.168.x.222
nvram set dhcp1_end=192.168.2.254
nvram set dhcp_end=254 # will cause to set DHCP IP address pool end at 192.168.x.254
nvram set dhcp_lease=86400 # DHCP lease time 86400 hours
nvram commit}}}

To act as a DHCP-server towards WIFI set the following:
{{{nvram set wifi_proto=dhcp
nvram commit}}}

== WL-500gP info ==
FCC ID: MSQWL500GP [https://gullfoss2.fcc.gov/prod/oet/forms/blobs/retrieve.cgi?attachment_id=640814&native_or_pdf=pdf FCC pictures]

HardwareAcceleratedCrypto

----
 . Here are some links to forum threads related to the WL-500gP:
 * [http://forum.openwrt.org/viewtopic.php?id=6090 Problems with WLAN encryption]
 * [http://forum.openwrt.org/viewtopic.php?id=6071 CPU Power]
 * [http://forum.openwrt.org/viewtopic.php?id=5688 Some more compatiblity information]
 * [http://wl500g.info/forumdisplay.php?f=61 wl500g.info]
 * [http://forum.bsr-clan.de/viewtopic.php?t=8813&highlight=500 Does anyone know what exactly are the 8 (2x4) pins near the bigger capacitor on the PCB?]
 * [http://forum.openwrt.org/viewtopic.php?id=6362 configure WAN-interface]

== Trunc with Kernel 2.6 ==
'''P:''' The line ''b44: eth1: BUG! Timeout waiting for bit 80000000 of register 428 to clear.'' may appear in log.

'''S:''' As writen in http://forum.openwrt.org/viewtopic.php?pid=29017 this can be fixed by editing /etc/init.d/S10boot

----
 . CategoryModel
