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

Note that most of the issues that I faced were related to OpenWRT configuration, and not the fact that I was on the Linksys router.  I have tried to highlight some of the stickier points that I ran into while getting this to work.  Hopefully, this document can be helpful to users of other wireless routers as well.

== Where I Started ==
I have a LAN in my Home Office that connects a few machines, as well as a laptop that connects to the LAN with a WiFi card through a Netgear WNR854T Wireless Access Point.  The Netgear box replaced the Linksys router a while back.  My son got X-Box Live for his birthday, and therefore needed to connect his X-Box to the network.  There was no reasonable way to do that hard-wired, so I did some research and found OpenWRT.

It took me several days to get it to work, so I thought I'd create this page to remind me the next time I brick the thing!

The first time I tried loading and configuring OpenWRT, I bricked the WRT54G, so that is where I'll start.

== The Goal ==
The goal of this setup is to have a wired network on the Linksys side of a wireless bridge that can access the internet through the Netgear Access Point.  This is accomplished in this example by using a separate subnet on the Linksys side, and routing the traffic through the Netgear box.  Since I use the Access Point for other uses, I need WPA encryption used on the wireless connections.

== Before Starting ==
 * Download the __2.4__ kernel version of Kamikaze 7.09, found at http://downloads.openwrt.org/kamikaze/7.09/brcm-2.4/ .  '''Note: As of this writing (3/08), you can not use the 2.6 kernel version because Wifi is not reliably implemented.'''  (That was my first mistake...)
 * Download the Linksys FTP program, found at (ftp://ftp.linksys.com/pub/network/tftp.exe)  This FTP client is needed because the WRT54G has a password, and the failsafe booting requires it.  Other TFTP clients do not support this (that I am aware of).  This software is not needed if your WRT54G is not bricked.  Note that this client is a Windows program, so if you are running Linux, you will need to run this program using wine (http://winehq.org) or other method (VMware, a Windows PC, other?)

== Debricking the WRT54G ==
If your WRT54G is not bricked, you can use the normal Firmware Upgrade function found in the Web Interface of the router.  Use the ".bin" format firmware when upgrading this way.  If you are upgrading the firmware through the web interface, the IP address of the WRT54G will remain what it was prior to the upgrade.  This does not happen if the WRT54G is bricked.  If your router is not bricked, skip the rest of this section and use its configured IP address whenever the address {{{192.168.1.1}}} is used in subsequent sections.

'''NOTE:  FOLLOWING THE STEPS IN THE REST OF THIS SECTION VOIDS YOUR WRT54G WARRANTY!'''  If the router is bricked, you probably do not mind.  Loading OpenWRT onto the WRT54G also voids the warranty...

There are supposed to be several possible ways to get your bricked router to fall into "failsafe mode", where it listens on IP address 192.168.1.1 for a TFTP connection to load new firmware before booting up.  (See references below.)  After trying all of them, the only one that worked (and worked reliably every time) was the shorting of the Flash memory pins.  If you are not adventurous, this may not be for you.  However, I found it quite satisfying, since it was the only thing that worked.  :-)  The steps required to debrick the WRT54G are:
 * Unplug the WRT54G and remove all connections.
 * Remove the cover of the WRT54G.  This will require removing the antennae, then pulling the front off and removing the top.  On my WRT54G, there were no screws that needed removing.  attachment:LinkSysRouterDisassembled.jpg
 * Find the Flash memory chip.  Find pin 1 which will be in the corner with  an indentation or other obvious marking.  Count down to find pins 15, 16, and 17.  Note that the printed circuit board has a little white tick mark every 5 pins, which will help immensely when needing to locate the correct pins.  attachment:LinkSysRouterFlashChipCloseup.jpg
 * Connect the WRT54G to a PC (directly, or indirectly through a LAN).  The PC's network interface card (NIC) needs to be configured with IP 192.168.1.2, and a netmask of 255.255.255.0.
 * You will want to start a running ping so you can see when the brick comes back to life.  On Linux, that would be {{{ping 192.168.1.1}}} and on Windows it would be {{{ping -C 192.168.1.1}}}.
 * Start the Linksys TFTP client, and fill in the IP address (192.168.1.1) and last password that was used on the router.  Do NOT start the transfer yet.
 * Here's the "tricky" part:  __While plugging in the WRT54G__, use a sharp metallic object (paper clip, pointy screw driver, awl) and touch pins 15 and 16 simultaneously.  (Actually, on my WRT54G, I had to touch pins 16 and 17 simultaneously, but other references stated 15 and 16.)  '''Be careful not to remove any metal from the printed circuit board.'''  Be gentle!  Keep touching these pins and watch the running ping.  You should start to see a response to the pings.  Once this happens, you can remove the tool.  The WRT54G is now in failsafe mode, waiting for a TFTP of the firmware. 
 * Initiate the TFTP transfer with the Linksys client.  Use the ".bin" format firmware when upgrading this way.
 * Once the firmware is uploaded, unplug the WRT54G and reassemble it, and reconnect it to the PC you used to load the firmware.

As an aside, I would love to know exactly what is happening by shorting pins 16 and 17.  Although I do not know for sure, it is my belief that shorting the pins (which, if I found the correct pinout, are address lines 18 and 17 respectively) causes a checksum on the Flash memory to fail (because the wrong memory addresses are returned from the chip), which causes the router to enter failsafe mode.  If there's a EE out there who knows for sure, please update this paragraph.  

There is a lot of information on debricking a WRT54g on the net.  Some potentially helpful links are http://www.openwrt.org/OpenWrtDocs/Troubleshooting , http://forum.openwrt.org/viewtopic.php?id=580 and http://www.ranvik.net/prosjekter-privat/jtag_for_wrt54g_og_wrt54gs/HairyDairyMaid_WRT54G_v22.pdf 

== Configuring the WRT54G ==
The first time you connect to an OpenWRT router, you must use telnet:
 * {{{telnet 192.168.1.1}}}
 * Log on as {{{root}}} using the password used for the firmware upload.
 * Turn on BootWait, by typing the following at the # prompt:
   * {{{nvram set bootwait=on}}}
   * {{{nvram get bootwait      # to make sure it's on...}}}
   * {{{nvram commit}}}
 Bootwait causes the WRT54G to wait a few seconds before booting to see if firmware is trying to be uploaded via TFTP.  If it sees the TFTP, it will upload the firmware before booting.  This can save a LOT of headaches if you misconfigure something.  You won't have to rip the box apart to debrick it.  Just start up the TFTP client and power cycle the WRT54G.
 * Change the router's password by typing {{{passwd}}} at the # prompt.  Changing the password automatically disables telnet and enables ssh.
 * Sign off ({{{exit}}}) and reconnect using SSH.  (PuTTY also worked well for me on a Windows box.)
 * We will use DHCP on the Linksys side of the bridge for the X-Box to use.  Edit the file {{{/etc/config/dhcp}}} to make it read:
{{{
config dhcp
        option interface    lan
        option start        100
        option limit        150
        option leasetime    12h
        option ignore       0
config dhcp
        option interface    wan
        option ignore       1
}}}
 * Edit the file {{{/etc/config/network}}} to read:
{{{
config interface lan
        option type        bridge
        option ifname      "eth0.0"
        option proto       static
        option ipaddr      192.168.1.1
        option netmask     255.255.255.0
        # The following should be the IP address of your Access Point that you are using to get out to the internet.
        option gateway     10.0.0.1  
        # For the following, I used the IP address of the DNS servers provided by my ISP.
        option dns         "xx.xx.xx.xx yy.yy.yy.yy"  
config interface wan
        #  IMPORTANT: The following needs to be wl0 to gateway through the wireless adapter!
        option ifname      "wl0"   
        # The following will get the wireless IP address from the Access Point via DHCP
        option proto       dhcp     
}}}
 * Edit the file {{{/etc/config/wireless}}} to read:
{{{
config wifi-device wl0
        option type        broadcom
        #  For the following, use whatever channel you have your access point configured to use.  
        option channel     1  
        option disabled    0
config wifi-iface
        option device      wl0
        option network     wan
        option mode        sta
        # For the following, use the SSID of the Access Point
        option ssid        yourssid  
        option encryption  psk  
        # Note: I could not get a link using psk2, even though my access point supports it.
        # The following can only be alphanumeric.  Special characters do not seem to work.  
        # Quotes seem to frog it up as well.
        option key         EnterYourPSKEncryptionPasswordHereWithoutQuotes  
        option hidden      0
        option isolate     0
        option bgscan      0
        option wds         0
}}}

== Configuring the Access Point ==
The following configuration needs to be set up on the Access Point in order to support the above WRT54G configuration to make this all work:
 * To have the Access Point assign IP configuration to the WRT54G (matching the {{{option proto dhcp}}} line of the {{{config interface wan}}} section of {{{/etc/config/network}}} file), the Access Point needs to have its DHCP server enabled, serving IP addresses in the subnet of the Access Point.  For example, if the Access Point is in the 10.0.0.0/255.0.0.0 network, then its dhcp configuration should assign addresses starting with 10.*
 * To match the {{{option channel 1}}} line in {{{/etc/config/wireless}}}, the channel on the Access Point also needs to be set to 1.  (Obviously, you can use any channel that you wish, as long as the two settings match.)
 * To match the {{{option ssid yourssid}}} line in {{{/etc/config/wireless}}}, the SSID of the Access Point needs to match that used on the WRT54G.
 * To match the {{{option encryption psk}}} and {{{option key [whatever]}}} lines in {{{/etc/config/wireless}}}, the Access point needs to allow WPA encryption, and use the same key.

----
CategoryHowTo
