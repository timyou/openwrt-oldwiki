## Please edit system and help pages ONLY in the moinmaster wiki! For more
## information, please see MoinMaster:MoinPagesEditorGroup.
### Unfortunately, I do not know what the above means...  This is my first wiki page!
##acl MoinPagesEditorGroup:read,write,delete,revert All:read
##master-page:HelpTemplate
##master-date:Unknown-Date
#format wiki
#language en
== WRT54G - From Brick to Bridge using Kamikaze ==
This page describes how I got my Linksys WRT54G v1.1 from the bricked state to a working bridge using OpenWRT Kamikaze 7.09.

Note that most of the issues that I faced were related to OpenWRT configuration, and not the fact that I was on the Linksys router.  Hopefully, this document can be helpful to users of other wireless routers as well.

== Where I Started ==
I have a LAN in my Home Office that connects a few machines, as well as a laptop that connects to the LAN with a WiFi card through a Netgear WNR854T Wireless Access Point.  The Netgear box replaced the Linksys router a while back.  My son got X-Box Live for his birthday, and therefore needed to connect his X-Box to the network.  There was no reasonable way to do that hard-wired, so I did some research and found OpenWRT.

It took me several days to get it to work, so I thought I'd create this page to remind me the next time I brick the thing!

The first time I tried loading and configuring OpenWRT, I bricked the WRT54G, so that is where I'll start.

== The Goal ==
The goal of this setup is to have a wired network on the Linksys side of a wireless bridge that can access the internet through the Netgear Access Point.  This is accomplished in this example by using a separate subnet on the Linksys side, and routing the traffic through the Netgear box.  Since I use the Access Point for other uses, I need WPA encryption used on the wireless connections.

== Before Starting ==
* Download the __2.4__ kernel version of Kamikaze 7.09, found at http://downloads.openwrt.org/kamikaze/7.09/brcm-2.4/ .  '''Note: As of this writing (3/08), you can not use the 2.6 kernel version because Wifi is not reliably implemented.'''  (That was my first mistake...)
* Download the Linksys FTP program, found at (URL needed - can't seem to find it right now...)  This FTP client is needed because the WRT54G has a password, and the failsafe booting requires it.  Other TFTP clients do not support this.  This software is not needed if your WRT54G is not bricked.  Note that this client is a Windows program, so if you are running Linux, you will need to run this program using wine (http://winehq.org) or other method (VMware, a Windows PC, other?)

'''NOTE:  FOLLOWING THESE STEPS VOIDS YOUR WRT54G WARRANTY!'''  If the router is bricked, you probably do not mind this.

== Debricking the WRT54G ==
If your WRT54G is not bricked, you can use the normal Firmware Upgrade function found in the Web Interface of the router.  Use the ".bin" format firmware when upgrading this way.  If you are upgrading the firmware through the web interface, the IP address of the WRT54G will remain what it was prior to the upgrade.  THis does not happen if the WRT54G is bricked.  If your router is not bricked, use its configured IP address whenever the address {{{192.168.1.1}}} is used below.

There are supposed to be several possible ways to get your bricked router to fall into "failsafe mode", where it listens on IP address 192.168.1.1 for a TFTP connection to load new firmware before booting up.  After trying all of them, the only one that worked (and worked reliably every time) was the shorting of the Flash memory pins.  If you are not adventurous, this may not be for you.  However, I found it quite satisfying, since it was the only thing that worked.  :-)  The steps required to debrick the WRT54G are:
* Unplug the WRT54G and remove all connections.
* Remove the cover of the WRT54G.  This will require removing the antennae, then pulling the front off.  On my WRT54G, there were no screws that needed removing.
* Find the Flash memory chip.  Find pin 1 which will be in the corner with  an indentation or other obvious marking.  Count down to find pins 15, 16, and 17.  Note that the printed circuit board has a little white tick mark every 5 pins, which will help immensely when needing to locate the correct pins.  (I have pictures, but do not know how to add them to the wiki...)
* Connect the WRT54G to a PC (directly or indirectly).  The PC's network needs to be configured with IP 192.168.1.2, and a netmask of 255.255.255.0.
* You may want to start a running ping so you can see when the brick comes back to life.  On Linux, that would be {{{ping 192.168.1.1}}} and on Windows it would be {{{ping -C 192.168.1.1}}}.
* Start the Linksys TFTP client, and fill in the IP address as last password that was used on the router.  Do NOT start the TFTP yet.
* Here's the "tricky" part:  __While plugging in the WRT54G__, use a sharp metallic object (paper clip, pointy screw driver, awl) and touch pins 15 and 16 simultaneously.  (Actually, on my WRT54G, I had to touch pins 16 and 17 simultaneously.)  '''Be careful not to remove any metal from the printed circuit board.'''  Be gentle!  Keep touching these pins and watch the running ping.  You should start to see a response to the pings.  Once this happens, you can remove the tool.  The WRT54G is now in failsafe mode, waiting for a TFTP of the firmware.
* Initiate the TFTP transfer with the Linksys TFTP client.  Use the ".bin" format firmware when upgrading this way.
* Once the firmware is uploaded, unplug the WRT54G and reassemble it, and re-connect it to the PC you used to load the firmware.

As an aside, I would love to know exactly what is happening by shorting pins 16 and 17.  Although I do not know for sure, it is my belief that shorting the pins (which if I found the correct pinout, are address lines 18 and 17 respectively) causes a checksum on the Flash memory to fail (because the wrong memory addresses are returned from the chip), which causes the router to enter failsafe mode.  If there's a EE out there who knows for sure, please update this paragraph.  

== Configuring the WRT54G ==
The first time you connect to an OpenWRT router, you must use telnet:
* {{{telnet 192.168.1.1}}}
* Log on as {{{root}}} using the password used for the firmware upload.
* Change the router's password by typing {{{passwd}}} at the # prompt.  Changing the password automatically disables telnet and enables ssh.
* Sign off ({{{exit}}}) and re-connect using SSH.  (PuTTY also worked well for me on a Windows box.)
* Edit the file {{{/etc/config/dhcp}}} to make it read:
{{{
config dhcp
 option interface lan
 option start 100
 option limit 150
 option leasetime 12h
 option ignore 0
config dhcp
 option interfact wan
 option ignore 1
}}}
* Edit the file {{{/etc/config/network}}} to read:
{{{
config interface lan
 option type bridge
 option ifname "eth0.0"
 option proto static
 option ipaddr 192.168.1.1
 option netmask 255.255.255.0
 option gateway 10.0.0.1  # This should be the IP address of your Access Point that you are using to get out to the internet.
 option dns "xx.xx.xx.xx yy.yy.yy.yy"  # I used the IP address of the DNS servers provided by my ISP.
config interface wan
 option ifname "wl0"   #  '''IMPORTANT: This needs to be wl0 to gateway through the wireless adapter!'''
 option proto dhcp     # Will get the wireless IP address from the Access Pointvia DHCP
}}}
* Edit the file {{{/etc/config/wireless}}} to read:
{{{
config wifi-device wl0
 option type broadcom
 option channel 1  #  Use whatever channel you have your access point configured to use.
 option disabled 0
config wifi-iface
 option device wl0
 option network wan
 option mode sta
 option ssid yourssid  # use the SSID of the Access Point
 option encryption psk  # Note: I could not get a link using psk2, even though my access point supports it.
 option key EnterYourPSKEncryptionPasswordHereWithoutQuotes  # This can only be alphanumeric.  Special characters do not seem to work.  Quotes seem to frog it up as well.
 option hidden 0
 option isolate 0
 option bgscan 0
 option wds 0
}}}

== Configuring the Access Point ==
(to do)
----
CategoryHowTo
