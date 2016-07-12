WAP54Howto [[TableOfContents]]

= This is a mini-howto for people who want to use OpenWRT on WAP54G. =
NOTE: If you brick your WAP54G, don't flame me. This works for me, but this doesn't mean that it'll work for you!

'''!!!WARNING!!!''' I know two different WAP54G models. Look at the rear of your AP. If the reset button is close to the left antenna, your AP will accept OpenWRT. If the reset button is next to the ethernet connector (left side of the ethernet connector), you'll brick your AP with OpenWRT (**unless using patches made by nbd**). If you install OpenWRT without these patches, both LAN and WLAN will die. See bottom section for v2 instructions and info. '''!!!WARNING!!!'''

 . 1., Enable boot_wait. I did this by installing Sveasoft Freya firmware and enabling telnet on the web page, so that I got a prompt on the AP. telnet to the AP and issue the following two commands: ''nvram set boot_wait=on; nvram commit''. Before flashing openwrt, make sure the AP is in AP mode and you can connect it via wireless! Test it or you'll brick your AP! 2., I could tftp (netkit-tftp doesn't work for me, but atftp does) openwrt-linux.trx (CVS version) to the AP. a., Using atftp:

||''atftp 192.168.1.245'' ||
||''atftp> trace'' ||
||''atftp> timeout 1'' ||
||''atftp> put openwrt-linux.trx'' ||


Before you press enter after the put command, power on the AP. Press enter as soon as possible once you've connected the power!

 . 3., After booting with openwrt, I could ping the AP, however telnet did not work from the LAN. telnet still worked via wireless. OpenWRT tries to configure the vlans like on WRT54G. This is bad on WAP54G. Connect to the AP via wireless, and telnet into it. Run ''firstboot''. Remove /etc/nvram.overrides, then copy it from /rom/etc (''cp /rom/etc/nvram.overrides /etc/''). Edit /etc/nvram.overrides, and comment out the following lines (thx to mbm for the tip):

||remap lan_ifname ||
||remap lan_ifnames ||
||remap wifi_ifname ||
||remap wifi_ifnames ||
||remap wan_ifname ||
||remap wan_ifnames ||
||remap pppoe_ifname ||


It may not be necessary, but I've deleted /etc/init.d/S45firewall, in order to completely disable netfilter (iptables), to make the AP accept everything from both LAN and WLAN.

 . 3.1, In the last experimental release the /rom/etc/nvram.overrides as removed!

This script set the basic nvram value copy all in a script and execute it!

||#!/bin/sh ||
||nvram set wifi_ifname=eth2 ||
||nvram set lan_ifname=br0 ||
||nvram set lan_ifnames=eth1 eth2 ||
||nvram set wl0_ifname=eth2 ||
||nvram set wan0_ifname=eth1 ||
||nvram set lan_hwnames=et1 wl0 ||
||nvram set wan_ifname=eth1 ||
||nvram set txpwr=84 ||
||nvram commit ||


This script is tested on a v.1 unit!

 . 4., Now you can install packages via ipkg like on a WRT54G unit. Note that WAP54G has only 1.8MB free space. 5., If you have problems, send your comments to slapic@linux.co.hu . 6., If you're familiar with Wiki, customize this page to look better.

== Warning: your WAP54G doesn't have much flash! (and can get stuck because of that) ==
With only 4Mo of flash, the WAP54G is limited to a jffs2 partition of less than 2Mo.

Some report only 2MB flash, but there are devices v1.0 with 4MB flash. Read ImageBuilderHowTo to build a custom smaller image.

'''There is bug in the OpenWRT firmware which prevents you from deleting, modifying and (obvioulsy) adding new files on the system when the jffs2 partition is full!'''

The error message you get (quite paradoxical if you aks me):

{{{
root@OpenWrt:/# rm /usr/man/man8/openvpn.8
rm: unable to remove `/usr/man/man8/openvpn.8': No space left on device
}}}

Alternatively you might be able to use the following:

{{{
root@OpenWrt:/# > /usr/man/man8/openvpn.8
}}}

That should make some space available so you can rm the files.

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

Run {{{firstboot}}} to regenerate your jffs2 partition if the system didn't do it automatically after the reboot. Obviously this

Information on flash layout and the 'mtd' command can be found in this post by mbm: http://forum.openwrt.org/viewtopic.php?pid=3123#p3123

PS: alternatively, you can fill up the flash of your WAP54G on purpose to lock it and be certain nobody is going to modify your configurations files without knowing this trick and formating the whole partition. This is called 'security through obscurity' and I do not advise it!

== Another experience (by AlexanderKostadinov) ==
I installed RC4 on 2 devices and RC5 on 2 devices. All with the reset button next to the ethernet connector. I observed 3 types of behavior.

=== Install original linksys 1.09.01 firmware (if yours is older) ===
=== Install HyperWAP 1.0 ===
You can use any trusted firmware to enable boot_wait (preferably Feya), because HyperWAP has no telnet and no way to modify manually nvram variables. In this howto I will share my own experience but in this point I want to tell a better way if someone is willing to take the risk of trying it. If you are not willing to try it on your own then skip to the next point! So if you use the Feya, issue in the telnet sessuon:

||nvram set boot_wait=on ||
||nvram set boardtype=bcm94710dev ||
||nvram set boardnum=2 ||
||nvram commit ||
||reboot ||


If you used HyperWAP then download the configuration as config.bin for example and edit it with an editor that don't modify some symbols on saving (hex editor,mcedit,...). It contains nulls then pairs "variable=value[null]", so I guess that it is possible to move boardtype and boardnum at the end, remove the "\r" as last simbol in the value and add the needed number of nulls to the end (must be 2 for 2 variables). Now restore the configuration to the devices.

Now you must be able to upgrade directly to RC5 with the micro image. As I said before '''this is untested'''. (actually I've tested it later and it is not working fine - to recover I installed RC4, cleaned nvram the safe way, set the variables again and installed RC5)


=== Test if boot_wait is working with RC4 ===
'''From this point first be sure to have wireless connection to the device/devices'''. RC4 firmware has a modified micro image for wap54G. You must upgrade first to it if you didn't modified boardtype and boardnum variables before. If you can upload it by TFTP, you are lucky, so telnet to the unit. '''Now skip one point.'''

=== workaround boot_wait problem ===
As I said before, you must have wireless connection to the device, so update to RC4 with the webif.  You may be able to access the device through lan ar maybe only through wireless port or maybe you just bricked your device. I installed only 4 devices and all are well working now, but you should be warned. So telnet to the device.

=== nvram variables ===
||nvram set boardtype=bcm94710dev ||
||nvram set boardnum=2 ||
||nvram commit ||
||reboot ||


This will tell RC5 firmware to use a workaround for v1.0 devices and not brick them.

=== install RC5 ===
I used [ImageBuilderHowTo] to make a customized RC5 image with iptables, dhcp and maybe something else removed, but I think that the micro image should work fine. All my devices have 4MB flash, but some maybe have only 2MB... Use brcm-2.4-squashfs.trx. If you have boot_wait working, go without fear with tftp and your box should be working. Else use mtd utility to upgrade. Now you should have RC5 working...

=== Some important notes ===
Board variables are needed to enable workarounds-see http://wiki.openwrt.org/OpenWrtDocs/Hardware/Linksys/WAP54Gv10.

Maybe some devices have only 2MB flash and not 4MB.

Somethimes boot_wait works, but PMON resets some variables to the default (boot_wait=off), because some other variable/variables are with some value (see http://forum.openwrt.org/viewtopic.php?pid=26835#p26835). I don't know how to solve this problem nor which variables make this mess. The unit is fully working, but you cannot use boot_wait.

This is why I recommend not using HyperWAP but Feya ot some other telnet capable firmware, where you can check these possibilities with dmesg and nvram utilities. This is to be sure in the success in 2 out of 3 possibilities.

If you have a working boot_wait, I'm sure (99%) that you will not brick your unit, but if boot_wait remains on after reboot, but tftp is not working then I recommend usind the hardware patch in http://wiki.openwrt.org/OpenWrtDocs/Hardware/Linksys/WAP54Gv10 to be insured.

=== Another note ===
Wap54G v1.0 is full of bugs, but if you are carefull and understand what you are doing, It is very likely to succeed installing OpenWRT.

I hope that I helped you in understanding the issues with these units although I have written the howto section in very limmited time so maybe ununderstandible.

If you have questions, suggestions or comments about '''this section''' of the howto, you can freely contact me via mail [AlexanderKostadinov]. You are free to correct any gramatical mistakes made by me :)

== Reviving a brick WAP54G v1 ==
After flashing a recent (mid december 2004) snapshot of openwrt-linux.trx into my WAP54G (v1) the device went dead, no WLAN nor LAN activity and both the power and diag LEDs permanently on. Yes, I ignored warnings like in this thread, stupid, stupid.  Did some more searching on the net and found the WRT54G trick to short pins 15 and 16 of the flash memory during power-on. But with my WAP54G this produced after appr. one second of pinging without reply on 192.168.1.1. indeed some ping responses but then the responses stop and nothing more can be done, regardless whether the short has been removed during the ping responses. The device does not enter a tftd wait state.  Then searched further on the net amd applied to the WAP54G a trick described for the WRT54G by Sveasoft. I applied from a windows system from a DOS window the command tftp -i 192.168.1.1 PUT <<PC-local path to a Linksys recent .trx for the WAP54G v1>> a fraction of a second after applying DC power to the device. A fraction being literally something around half a second. This worked !!!! Give the device time to re-install itself after the tftpd has announced a successful data transfer. Of course make sure that the PC has connectivity to the 192.168.1.x subnet. I was about to trash the device but am happy to have searched a little further on the net. By the way, also Sveasoft's Freya software was not functional on this device; the LAN was dead but the WLAN was not. Hence this could be easily restored from the Freya web interface by forcing a system reset (pressing the reset button some 5 seconds or so) and accessing the device and web interface from a client tuned to channel 6 with a 'linksys' ssid and all security turned off. Hope this can revive your WAP54G !! martin, portugal

***On my WAP54G v1.0 (which uses an AMD flash chip at U6), the pin short trick does work, but the pins to short are 16 and 17.  --HaveBlue

= This is a mini-howto for people who want to use OpenWRT on WAP54G v2 =
Update for Whiterussian RC5

The [http://downloads.openwrt.org/whiterussian/rc5/micro/openwrt-brcm-2.4-squashfs.trx micro] image of Whiterussian RC5 gives a full working system on WAP54Gv.2, no more read only file system!!

The following refer to Whiterussian RC4, I don't know if it should be erase.

As you can read on [http://forum.openwrt.org/viewtopic.php?id=3431 WAP54G v2 issues - "Read-only file system"] thread in the forum, Openwrt, specificaly:[[BR]] http://downloads.openwrt.org/whiterussian/rc4/default/openwrt-wap54g-squashfs.trx[[BR]] get installed fine on the WAP54G v2, but give you a read-only file system, so you won't be able to modify any configuration file, you can't even activate root passwd, so you can't use web interfase neither.

Just telnet and any configuration based on nvram.

This is my work around:

 * You have to follow [http://wiki.openwrt.org/ImageBuilderHowTo ImageBuilderHowTo], in order to create an image with modyfied /etc files.
 * Copy all /etc, from an already installed WAP54G, to the PC where you are going to create your images.
 * To activate ssh and access to the web interfase
  * Put a hash of you passwd on /etc/passwd
  * Put this line on /etc/httpd.conf
   . cgi-bin/webif:root:HASH
  * Create dss and rsa keys, and put it on /etc/dropbear. For this I use /etc/init.d/S50dropbear, but you have to modify it, in order to use /tmp/dropbear instead of /etc/dropbear, cause remember all you file system is read-only, except /tmp.
 * Make any other configuration (for example)
  * edit /etc/dnsmasq.conf to adjust the range[[BR]]
  * edit /etc/hosts and add your hosts[[BR]]
  * create /etc/resolv.conf and put your nameserver

If you have problems, send your comments to tuxerg@gmail.com , and/or post on [http://forum.openwrt.org/viewtopic.php?id=3431 WAP54G v2 issues - "Read-only file system"].

== Reviving a brick WAP54G v2 ==
After reading the above on v1, and seeing I had a v2... I knew there had to be a way ;-) Here's my (Curto) experiences..

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

= WAP54G v3 =
You can upload rc4 default wap54g build via  webinterface. Same limitations as above for v2.

crodler

== Reviving a brick WAP54G v3 ==
After flashing a wrong .trx, the v3 went dead completely, no WLAN / LAN anymore. I start listening via the serial, and it turned out to be a problem with pflash, which wasn't able to access the flash chip. The v3 version has NO intel flash chip anymore, instead a SST brand chip (namely SST39VF160-70-4c-eke) is used. Things got worse: Shortening pin15 / 16 on the flash chip (see above) did NOT work either. However, there's a workaround for that:

What you do when shortening the pins is nothing more than generating a checksum error during load (as wrong data is accessed while shortening the A18 address line). If this happens, the device starts to listen on its default IP for a new firmware image.

By comparing the intel / SST datasheets, you'll discover that both chips are not completely pin compatible. On the v3 PCB, Pin 15 simply has no connection, so you'll need to:

- Find a point to get GND on the v3 PCB. Many possibilities, e. g. the metal plating of the "easy secure" button, the outer rim of the TNC connector, etc ...

- Use some wire, connect a needle or something similar thin to the other end. Push it GENTLY on pin 16 of the flash chip. To find the pin, count to the right starting at the dot on the chip. Take your time here. If you're not sure you got it right, double check. Using a wrong pin may destroy the voltage regulator(s) and / or other circuitry on the PCB or cause other havoc.

- Turn on the power on the WAP54. Wait a brief period (>2 secs). Remove the pin16 short.

- Use a .trx file of your choice. I used http://downloads.openwrt.org/whiterussian/rc4/default/openwrt-wap54g-squashfs.trx[[BR]], which seems to work.

- (Windows related) Start a DOS prompt. Type "tftp -i 192.168.1.245 put <path and filename of your trx>. You may check if the WAP54 has entered the desired state by pinging 192.168.1.245. If you get replies, hit enter. Wait a brief period (>2 minutes) until programming has finished.

-> Steeve

Use the following interface names:

{{{
nvram set lan_ifname=eth1
nvram set wan_ifname=vlan0
nvram commit
}}}

=== Alternative Debricking ===
On my WAP54g ver.3 there is a intel flash chip and the instructions above did not work. I have a serial port setup on mine so I sent ctrl-c on boot to get the CFE> boot prompt. This gave me access to the nvram and let me fix a few variables. I just had myself locked out of my WAP54g on all interfaces. You can use this to set boot wait.

Another problem I've run into is that the wireless interface isn't starting up correctly on boot. I've installed the wl binary and this lets me shut the wireless down and bring it back up(wl up & wl down) after this the interface works fine. The only problem is that you need to set the lan interface to eth0 so you can telnet into the router.

-> Garak
