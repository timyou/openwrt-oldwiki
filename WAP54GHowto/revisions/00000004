= This is a mini-howto for people who want to use OpenWRT on WAP54G. =

NOTE: If you brick your WAP54G, don't flame me. This works for me, but this doesn't mean that it'll work for you!

'''!!!WARNING!!!'''
I know two different WAP54G models. Look at the rear of your AP. If the reset button is near to the left antenna, your AP will accept OpenWRT.
If the reset button is near to the ethernet connector (left side of the ethernet connector), you'll brick your AP with OpenWRT. This version of WAP54G only works with the original Linksys firmwares (except 2.06) for me. If you install the Mustdie or Freya firmwares (based on 2.06), your LAN will not work, but WLAN will, so that you can upload a different firmware via WLAN. If you install OpenWRT, both LAN and WLAN will die.
'''!!!WARNING!!!'''

 1., Enable boot_wait. I did this by installing Sveasoft Freya firmware, enabling telnet on the web page, so that I got a prompt on the AP. telnet to the AP and issue the following two commands: ''nvram set boot_wait=on; nvram commit''. Before flashing openwrt, make sure the AP is in AP mode and you can connect it via wireless! Test it or you'll brick your AP!
 
 2., I could tftp (netkit-tftp doesn't work for me, but atftp does) openwrt-linux.trx (CVS version) to the AP.
 a., Using atftp:
||''atftp 192.168.1.245''||
||''atftp> trace''||
||''atftp> timeout 1''||
||''atftp> put openwrt-linux.trx''||
Before you press enter after the put command, power on the AP. Press enter as soon as possible once you've connected the power!
 
 3., After booting with openwrt, I could ping the AP, however telnet did not work from the LAN. telnet still worked via wireless. OpenWRT tries to configure the vlans like on WRT54G. This is bad on WAP54G. Connect to the AP via wireless, and telnet into it. Run ''firstboot''. Remove /etc/nvram.overrides, then copy it from /rom/etc (''cp /rom/etc/nvram.overrides /etc/''). Edit /etc/nvram.overrides, and comment out the following lines (thx to mbm for the tip):
||remap lan_ifname||
||remap lan_ifnames||
||remap wifi_ifname||
||remap wifi_ifnames||
||remap wan_ifname||
||remap wan_ifnames||
||remap pppoe_ifname||
It may not be necessary, but I've deleted /etc/init.d/S45firewall, in order to completely disable netfilter (iptables), to make the AP accept everything from both LAN and WLAN.

 4., Now you can install packages via ipkg like on a WRT54G unit. Note that WAP54G has only 1.8MB free space.

 5., If you have problems, send your comments to slapic@linux.co.hu.

 6., If you're familiar with WiKi, customize this page to look better.

