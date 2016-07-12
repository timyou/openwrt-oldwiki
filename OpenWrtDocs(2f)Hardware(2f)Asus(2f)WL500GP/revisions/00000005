The Asus WL-500g Premium seems to be supported by OpenWrt.

Here are some links to forum threads related to the WL-500gP:

 * [http://forum.openwrt.org/viewtopic.php?id=6090 Problems with WLAN encryption]
 * [http://forum.openwrt.org/viewtopic.php?id=6071 CPU Power]
 * [http://forum.openwrt.org/viewtopic.php?id=5688 Some more compatiblity information]

 So far, very few problems with the wl-500gP

the reset button does not work (due largely to mis-mapped /proc/sys/reset)

gpio 0 = RESTORE button (reset) (00 = unpressed, 01 = pressed)

gpio 1 = Power LED (enable = off, disable = on)

gpio 4 = EZ SETUP button (similar to linksys "button"?) (00 = unpressed, 01 = pressed)


  It seams as tho the only method of flashing this router (at the moment) is to use a tftp client & upload firmware when the router is in diag mode.  To put the router in diag mode, unplug the router & push & hold the RESTORE button then plug the router in.  Wait for a slow blinking power light & presto you're in diag mode.  Then tftp the image to the router.  After a few minutes, unplug/plug the router.  I've (thecompwiz) had to do this twice before the firmware took... but it definately works.

  After firmware is installed, you should be able to log into the router via telnet.  Set the root password & you need to make a few nvram setting changes....

  Since this router was not in the "supported" category when RC5 was released... there are a few things to change:

   nvram set lan_ifnames="vlan0 eth2"

   nvram set wlan_ifname=eth2
  
(don't forget to commit nvram changes)
  ****WARNING***  I cannot guarentee this will always work, or that it will work in your case... nor will I ever guarentee anything you do.  That being said, the WL500gP is supposed to have 32mb RAM... and if you poke arround, you may notice that you are only seeing 16mb ram... there are a few nvram settings that need to be changed:

   nvram set sdram_init=0x0009 

   nvram set sdram_ncdl=0

(don't forget to commit/reboot)

'''Please write some more info on the WL-500gP!'''



VespaTS:
Couldn't get PPPOE to work. To get pppoe running I had to change again some settings:

wan_device=eth0      (it was set to vlan1)
