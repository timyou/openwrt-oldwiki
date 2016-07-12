The Asus WL-500g Premium seems to work with OpenWrt.

== Installation ==
Looks like most people won't be able to install OpenWrt using the Asus web interface. You can try the web interface in case it works, or skip directly to the tftp part (which works for sure).  From Asus Firmware 1.9.7.0 the webinterface doesn't work to upgrade to OpenWRT (bin or micro, 4Mb or 8Mb).  If the tftp part fails, you can try the installation with the Asus "firmware restoration" tool (works like a charm, but windows only).

=== Via Asus web interface ===
/!\ '''For some people upgrading via the web interface works, for some it doesn't. Trying won't break the router, the web interface just might not accept the OpenWrt firmware image.''' /!\

It might be possible to use manufacturers own web interface to download OpenWrt into the router. It has been reported that [http://downloads.openwrt.org/whiterussian/rc5/bin/openwrt-brcm-2.4-jffs2-4MB.trx this image] (Whiterussian-rc5, jffs2, 4MB) was accepted by the web interface.  ~-Comment: From which webinterface, from asus fw version 1.9.6.9?-~

=== Using diag mode and tftp ===
/!\ '''After tftp upload is complete, DON'T reboot (replug) too early! It might brick your router.''' /!\

Netkit's tftp doesn't work quit often, use atftp.

It is possible to install OpenWrt using a tftp client when the router is in "diag" mode. To put the router in diag mode, do this:

 * Unplug the power cord.
 * Push the RESTORE button using a pen or such, and keep the button pushed down.
 * Plug the power on while keeping the RESTORE button pushed for few seconds.
 * If you see a slowly blinking power light, you're in diag mode. Now the router should accept an image via tftp. See OpenWrtViaTftp for more instructions on upgrading via tftp.
 * After the tftp upload is complete, wait at least 6 minutes. Get a cup of coffee or something in the meanwhile.
 * Asus WL-500gP doesn't seem to reboot automatically after the upgrade is complete. You need to plug off the power, and plug it back on to make the router alive again.
 * You're done! You should be able to telnet to your router and start configuring.
=== Using the Asus firmware restoration tool (windows only) ===
 * you can try the installation with the Asus "firmware restoration" tool, it's on the cd.
 * Browse the .trx file ( bin/openwrt-brcm-2.4-jffs2-4MB.trx works great).
 * Press Upload. The router will reboot itself.
 * You can find the router on it's previous ip address (otherwise 192.168.1.1)
== WL-500gP specific configuration ==
=== Interfaces ===
/!\ ''' Some people have been having troubles by setting wan_proto=none. It appears as if it breaks the vlan0.''' /!\

Before reading further, please read about the internal network architecture and how physical ports map to vlans unless you're already familiar with it. See OpenWrtDocs/NetworkInterfaces if you feel like you could refresh your memory.

When WhiteRussian RC5 was released, this router was not in the "Supported" category yet. The WAN interface for example won't work with the default settings.

You need to make a few nvram changes before the network settings are similar as in most other routers (such as WRT54GL):

 . {{{
nvram set vlan1ports="0 5*"
nvram set wan_ifname=vlan1
nvram set lan_ifnames="vlan0 eth2"
nvram set lan_ifname=br0
}}}
This will configure LAN and WIFI to be bridged (br0) and WAN to vlan1.

Save the settings with:

{{{
nvram commit
}}}
/!\ '''Note: the {{{nvram commit}}} command will erase and rewrite a 64kB part of the flash memory. Don't do this too often since flash memories only have limited number of erase/rewrite-cycles!''' (see [http://wiki.openwrt.org/OpenWrtNVRAM#NVRAMCommitting nvram commit warning]) /!\

You should be able to configure the rest of the network configuration using OpenWrt webif.

Note: new vlan settings will be applied on reboot, or by some program such as RoboCfg (which isn't used by default).

=== Enabling all RAM ===
If you look at "dmesg" or "free" command's output, you will probably see that there's only 16MB of RAM. Specs says there should be 32MB.

 . This is how you enable the rest of RAM:
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

----
=== PPPOE ===
VespaTS: Couldn't get [wiki:WikiPedia:PPPoE PPPOE] to work. To get pppoe running I had to change again some settings:

wan_device=eth0 (it was set to vlan1)

Could an experienced WL-500gP user update [:OpenWrtDocs/Configuration#NetworkInterfaceNames:this table]?



The above does not work for me (on a clean OpenWRT squashfs firmware), I've to use these setting after configure in the web ui:

/!\ '''Note:''' You may want to do a 'ifdown wan' first, to suppress pppd messages.

{{{
nvram set wan_ifname=ppp0
nvram set pppoe_ifname=vlan1
nvram set wan_device=vlan1}}}
=== DHCP server & client settings ===
To act as a DHCP-client towards WAN set the following:

{{{
nvram set wan0_proto=dhcp
nvram set wan_proto=dhcp
nvram commit}}}
To act as a DHCP-server towards LAN set the following:

{{{
nvram set default_lan_proto=dhcp_server
nvram set lan_dhcp=1
nvram set dhcp_enable_x=1
nvram commit}}}
These settings are optional and not necessary for dhcp to function:

{{{
# to set DHCP IP address pool begin at 192.168.1.222
nvram set dhcp1_start=192.168.1.222
nvram set dhcp_start=222
# to set DHCP IP address pool end at 192.168.1.254
nvram set dhcp1_end=192.168.1.254
nvram set dhcp_end=254
nvram set dhcp_lease=86400 # DHCP lease time 86400 hours
nvram commit}}}
To act as a DHCP-server towards WIFI set the following:

{{{
nvram set wifi_proto=dhcp
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
 * [http://forum.bsr-clan.de/viewtopic.php?t=8813&highlight=500 Does anyone know what exactly are the 8 (2x4) pins near the bigger capacitor on the PCB?] They are 2 serial connections
 * [http://forum.openwrt.org/viewtopic.php?id=6362 configure WAN-interface]
== Trunc with Kernel 2.6 ==
'''P:''' The line ''b44: eth1: BUG! Timeout waiting for bit 80000000 of register 428 to clear.'' may appear in log. ''' '''

'''S:''' As writen in http://forum.openwrt.org/viewtopic.php?pid=29017 this can be fixed by editing /etc/init.d/S10boot

'''P:''' USB 1.1 devices are not recognized, USB 2.0 devices like harddrives etc. work perfectly. How comes? ''' '''

'''S:''' The WL-500gP ehci-hcd module handles all USB2 transfer well, but the external ports use uhci-hcd for usb1. To make it even worse, the current trunk version has issues with this module to load but it can be fixed like mentioned in the forum http://forum.openwrt.org/viewtopic.php?id=7149. The broadcom chip seems to have a "buried" ohci controller that can not be used with the external connectors.

----
 . CategoryModel
