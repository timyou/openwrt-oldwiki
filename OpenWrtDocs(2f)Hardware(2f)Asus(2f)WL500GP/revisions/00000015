The Asus WL-500g Premium seems to be supported by OpenWrt.

Here are some links to forum threads related to the WL-500gP:

 * [http://forum.openwrt.org/viewtopic.php?id=6090 Problems with WLAN encryption]
 * [http://forum.openwrt.org/viewtopic.php?id=6071 CPU Power]
 * [http://forum.openwrt.org/viewtopic.php?id=5688 Some more compatiblity information]
 * [http://wl500g.info/forumdisplay.php?f=61 wl500g.info]
 * [http://forum.bsr-clan.de/viewtopic.php?t=8813&highlight=500 Does anyone know what exactly are the 8 (2x4) pins near the bigger capacitor on the PCB?]

=== Few problems with the WL-500gP ===
The reset button does not work (due largely to mis-mapped /proc/sys/reset)

[wiki:WikiPedia:GPIO gpio] 0 = RESTORE button (reset) (00 = unpressed, 01 = pressed)

gpio 1 = Power LED (enable = off, disable = on)

gpio 4 = EZ SETUP button (similar to linksys "button"?) (00 = unpressed, 01 = pressed)

 . It seams as tho the only method of flashing this router (at the moment) is to use a tftp client & upload firmware when the router is in diag mode. To put the router in diag mode, unplug the router & push & hold the RESTORE button then plug the router in. Wait for a slow blinking power light & presto you're in diag mode. Then tftp the image to the router. After a few minutes, unplug/plug the router. I've (thecompwiz) had to do this twice before the firmware took... but it definately works. After firmware is installed, you should be able to log into the router via telnet. Set the root password & you need to make a few nvram setting changes.... Since this router was not in the "supported" category when RC5 was released... there are a few things to change:
  . nvram set lan_ifnames="vlan0 eth2" nvram set wlan_ifname=eth2

(don't forget to commit WikiPedia:nvram changes)

 * ***WARNING*** I cannot guarentee this will always work, or that it will work in your case... nor will I ever guarentee anything you do. That being said, the WL-500gP is supposed to have 32mb RAM... and if you poke arround, you may notice that you are only seeing 16mb ram... there are a few nvram settings that need to be changed:
  . nvram set sdram_init=0x0009 nvram set sdram_ncdl=0

(don't forget to commit/reboot)

''''''

=== More info of WL-500gP ===
FCC ID: MSQWL500GP [https://gullfoss2.fcc.gov/prod/oet/forms/blobs/retrieve.cgi?attachment_id=640814&native_or_pdf=pdf FCC pictures]

HardwareAcceleratedCrypto

----
VespaTS: Couldn't get [wiki:WikiPedia:PPPoE PPPOE] to work. To get pppoe running I had to change again some settings:

wan_device=eth0 (it was set to vlan1)

Could an experienced WL-500gP user update [:OpenWrtDocs/Configuration#NetworkInterfaceNames:this table]?

***Caution** I've (thecompwiz)been having troubles if I set wan_proto=none It appears as if it breaks the vlan0.

== Trunc with Kernel 2.6 * ==
'''P:''' The line ''b44: eth1: BUG! Timeout waiting for bit 80000000 of register 428 to clear.'' may appear in log.

'''S:''' As writen in http://forum.openwrt.org/viewtopic.php?pid=29017 this can be fixed by editing /etc/init.d/S10boot

----
CategoryModel
