= This is a mini-howto for people who wants to use OpenWRT on WAP54G. =

NOTE: If you brick your WAP54G, don't flame me. This works for me, but this doesn't mean that it'll work for you!

'''!!!WARNING!!!'''
I know two different WAP54G models. Look at the rear of your AP. If the reset button is near to the left antenna, your AP will accept OpenWRT.
If the reset button is near to the ethernet connector (left side of the ethernet connector), you'll brick your AP with OpenWRT. This version of WAP54G only works with the original Linksys firmwares (except 2.06) for me. If you install the Mustdie or Freya firmwares (based on 2.06), your LAN will not work, but WLAN will, so that you can upload a different firmware via WLAN. If you install OpenWRT, both LAN and WLAN will die.
'''!!!WARNING!!!'''

 1., Enabled boot_wait. I could do this with installing Sveasoft Freya firmware, enabled telnet on the web page, so that I got a prompt on the AP.telnet to the AP and issue the following two commands: ''nvram set boot_wait=on; nvram commit''. Before flasing openwrt, make sure the AP is in AP mode and you can connect it via wireless! Test it or you'll brick your AP!
 
 2., I could tftp (netkit-tftp doesn't work for me, but atftp does) openwrt-linux.trx (CVS version) to the AP.
 a., Using atftp:
||''atftp 192.168.1.245''||
||''atftp> trace''||
||''atftp> timeout 1''||
||''atftp> put openwrt-linux.trx''||
Before you push enter after the put command, power on the AP. Press enter asap when you've connected the power!
 
 3., After booting with openwrt, I could ping the AP, however telnet does not work from the lan. I had to connect via wireless and telnet works. OpenWRT tries to configure the vlans like in WRT54G. This is bad on WAP54G. Connect to the AP via wireless, and telnet into it. Runs ''firstboot''. Remove /etc/nvram.overrides, than copy it from /rom/etc (''cp /rom/etc/nvram.overrides /etc/''). Edit /etc/nvram.overrides, and comment out the following lines (thx to mbm for the tip):
||remap lan_ifname||
||remap lan_ifnames||
||remap wifi_ifname||
||remap wifi_ifnames||
||remap wan_ifname||
||remap wan_ifnames||
||remap pppoe_ifname||
Maybe it isn't required, but I've deleted /etc/init.d/S45firewall, so that I've completly disabled netfilter (iptables), and the AP will accept everything both via LAN and WLAN.

 4., Now you can install packages via ipkg like on a WRT54G unit. Note that WAP54G has only 1.8MB free space.

 5., If you have problems, send your comments to slapic@linux.co.hu.

 6., If you're familiar with WiKi, customize this page to look better.

