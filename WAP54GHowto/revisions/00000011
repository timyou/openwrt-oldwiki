= This is a mini-howto for people who want to use OpenWRT on WAP54G. =

NOTE: If you brick your WAP54G, don't flame me. This works for me, but this doesn't mean that it'll work for you!

'''!!!WARNING!!!'''
I know two different WAP54G models. Look at the rear of your AP. If the reset button is close to the left antenna, your AP will accept OpenWRT.
If the reset button is next to the ethernet connector (left side of the ethernet connector), you'll brick your AP with OpenWRT (**unless using patches made by nbd**). If you install OpenWRT without these patches, both LAN and WLAN will die. See bottom section for v2 instructions and info.
'''!!!WARNING!!!'''

 1., Enable boot_wait. I did this by installing Sveasoft Freya firmware and enabling telnet on the web page, so that I got a prompt on the AP. telnet to the AP and issue the following two commands: ''nvram set boot_wait=on; nvram commit''. Before flashing openwrt, make sure the AP is in AP mode and you can connect it via wireless! Test it or you'll brick your AP!
 
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
 
 3.1, In the last experimental release the /rom/etc/nvram.overrides as removed!
This script set the basic nvram value copy all in a script and execute it!
||#!/bin/sh||
||nvram set wifi_ifname=eth2||
||nvram set lan_ifname=br0||
||nvram set lan_ifnames=eth1 eth2||
||nvram set wl0_ifname=eth2||
||nvram set wan0_ifname=eth1||
||nvram set lan_hwnames=et1 wl0||
||nvram set wan_ifname=eth1||
||nvram set txpwr=84||
||nvram commit||

This script is tested on a v.1 unit!
 
 4., Now you can install packages via ipkg like on a WRT54G unit. Note that WAP54G has only 1.8MB free space.

 5., If you have problems, send your comments to slapic@linux.co.hu.

 6., If you're familiar with Wiki, customize this page to look better.


== Warning: your WAP54G doesn't have much flash! (and can get stuck because of that) ==
With only 4Mo of flash, the WAP54G is limited to a jffs2 partition of less than 2Mo.

'''There is bug in the OpenWRT firmware which prevents you from deleting, modifying and (obvioulsy) adding new files on the system when the jffs2 partition is full!'''

The error message you get (quite paradoxical if you aks me):
{{{
root@OpenWrt:/# rm /usr/man/man8/openvpn.8
rm: unable to remove `/usr/man/man8/openvpn.8': No space left on device
}}}
As far as I know, the system should still work (you should be able to telnet/SSH it) but you won't be able to change any of its configuration but the nvram variables.

If you can tftp with boot_wait on, you should be able to install a new openWRT image, but I don't know if new install will reformat the jffs2 partition.

The solution which worked for me was erase the jffs2 partition. You will lose all your installed packages along with your personalised configuration files, so save everything you need first. However this is better than having a 'stuck' access point. To erase the jffs2 partition you can use the 'mtd' command:

{{{
mtd erase OpenWrt
}}}

you may need (I didn't have to do that) to first do a 

{{{
mtd unlock OpenWrt
}}}

Run `firstboot` to regenerate your jffs2 partition if the system didn't do it automatically after the reboot. Obviously this

Information on flash layout and the 'mtd' command can be found in this post by mbm: http://forum.openwrt.org/viewtopic.php?pid=3123#p3123

PS: alternatively, you can fill up the flash of your WAP54G on purpose to lock it and be certain nobody is going to modify your configurations files without knowing this trick and formating the whole partition. This is called 'security through obscurity' and I do not advise it!

== Reviving a brick WAP54G v1 ==
After flashing a recent (mid december 2004) snapshot of openwrt-linux.trx into my WAP54G (v1) the device went dead, no WLAN nor LAN activity and both the power and diag LEDs permanently on. Yes, I ignored warnings like in this thread, stupid, stupid. 
Did some more searching on the net and found the WRT54G trick to short pins 15 and 16 of the flash memory during power-on. But with my WAP54G this produced after appr. one second of pinging without reply on 192.168.1.1. indeed some ping responses but then the responses stop and nothing more can be done, regardless whether the short has been removed during the ping responses. The device does not enter a tftd wait state. 
Then searched further on the net amd applied to the WAP54G a trick described for the WRT54G by Sveasoft.
I applied from a windows system from a DOS window the command
tftp -i 192.168.1.1 PUT <<PC-local path to a Linksys recent .trx for the WAP54G v1>> a fraction of a second after applying DC power to the device. A fraction being literally something around half a second. This worked !!!! Give the device time to re-install itself after the tftpd has announced a successful data transfer.
Of course make sure that the PC has connectivity to the 192.168.1.x subnet.
I was about to trash the device but am happy to have searched a little further on the net.
By the way, also Sveasoft's Freya software was not functional on this device; the LAN was dead but the WLAN was not. Hence this could be easily restored from the Freya web interface by forcing a system reset (pressing the reset button some 5 seconds or so) and accessing the device and web interface from a client tuned to channel 6 with a 'linksys' ssid and all security turned off.
Hope this can revive your WAP54G !!
martin, portugal

== WAP54G v2 ==
After reading the above on v1, and seeing I had a v2... I knew there had to be a way ;) Here's my (Curto) experiences..

I was running mustdie based on 2.07, but obviously wanted more control.
I updated to linksys 2.08 (2.07 does not have http://router/fw-conf.asp ... so this update is required).
I then proceeded to attempt to flash with rc3 of white russian (brcm build)... which bricked my AP. The lights seemed to randomly flash, the connection would appear to go up and down every second or so (watching the connection from my windows xp laptop) and it could not be pinged, tftp'd, or telnet'd to.
******WARNING****** THIS STEP IS NOT GUARANTEED TO WORK AND COULD FRY YOUR UNIT ******WARNING******
I had read about shorting pins on the flash chip, so while it was turned on, I started a tftp transfer of the stock 2.08 firmware and shorted pins 15 & 16 on the flash chip (intel chip on the underside of the board)... and it worked! The transfer went through.
However, the unit still would not ping... so I did this procedure a second time... this time it worked.
I then downloaded the 2.08 source from linksys and tinkered with for a bit before nbd informed me he had a patch for kmod-diag to make it work on the v2 WAP54G.
I obtained he binary release, and flashed it via the web interface... and it worked perfect.
I have since downloaded his customized image builder kit and made by own firmware (with cif, ext2, and loop support so I can have a remotely hosted filesystem... which will be in another document).
His files are available from http://downloads.openwrt.org/people/nbd/whiterussian/
