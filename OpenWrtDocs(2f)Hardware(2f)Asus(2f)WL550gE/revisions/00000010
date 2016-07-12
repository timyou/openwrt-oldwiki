The Asus WL-550gE is supported by OpenWrt rc6.

== Flo's user report ==

After uploading WhiteRussian RC5 file "openwrt-brcm-2.4-jffs2-4MB.trx" the router is no longer reachable via any network interface. Rescue mode does not seem to work eighter :(

If any developer would like to mess with this, let me know. I have a "virgin" second piece laying around here ;-)

== znerol's user report ==

I successfully flashed an Asus WL-550gE with openwrt-brcm-2.4-squashfs.trx (rc6) and openwrt-freifunk-1.4.5.trx. The device seems to work fine, however i did not test encryption yet.


== rob's user report ==

I flashed my Asus WL-550gE with openwrt-brcm-2.4-squashfs.trx (whiterussian-0.9). pppoe seems to stop receiving data after several hours and requires a reconnect to get it working again.. Everything else seems to work.

== AlexanderGraef's user report ==

Flashing my Asus WL-550gE with openwrt-brcm-2.4-squashfs.trx was easy:

 1. Connect to hub/switch
 2. Configure your computer as 192.168.1.123
 3. Issue "ping -t -w 10 192.168.1.1"
 4. Remove power cord from WL-550gE
 5. Hold down "RESTORE" button with pen
 6. Plug in power cord
 7. When the PWR-LED blinks slowly and you get answer from ping, issue:
   "tftp -i 192.168.1.1 PUT openwrt-brcm-2.4-squashfs.trx"
 8. Wait about 5 minutes, then power cycle WL-550gE
 9. Open browser with http://192.168.1.1 and see the OpenWRT admin GUI

I also added an internal USB memory stick, so I could install more software. The WL-550gE has two internal USB ports. You simply need to solder cables to GND, D+, D-, VCC. You also need to add one 15kOhm resistor between D+ and GND, and a second 15kOhm resistor between D- and GND. After installing usbcore, usb-ohci, scsi_mod, sd_mod, usb-storage and filesystem modules, you can access the memory stick.

== Skender's report ==

Works great for me. Did the same as AlexanderGraef.
