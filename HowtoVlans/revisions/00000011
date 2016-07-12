= Howto: VLANS on the WRT54G =

'''Request for help!''' I have been searching for a copy of the admcfg source, and have yet to find it. The only documentation I found was in google's cache, unfortunately google doesn't seem to cache tgz files. Please email be if you know where I can get a copy: bhook(at)kssb(dot)net.

'''Answer:''' admcfg is obsolete and not portable across the various different hardware types. Please see [:OpenWrtDocs/Configuration#head-cdceb01bb26cc4c59c558d91f7d76c37c5318626: OpenWrtDocs/Configuration] for proper vlan setup. [:TableOfHardware: Devices] with BCM5325 can be configured using robocfg.

'''Response to Answer:''' admcfg may be obsolete, and is buggy (the ARP bug is annoying), but the vlanxxxx variables don't provide all of the needed configuration options for the ADM switch in a WRT54G. For example, I have found no way to make port 0 (the WAN port) a TAGGED port. At first I thought that the * used in the vlanXports variables might help, but it simply defines the default PVID for a port that exists in multiple vlans. In single AP networks, there probably would never be a need to configure tagged vlans, but if you are trying to use multiple APs and want to segment your WiFi, and still use the ethernet ports, then as best I can tell admcfg is the only way to go. And lastly, the vlanxxxx variables don't do anything until you reset the router, which means you could easily brick your wrt (only cracking open the case can save it then).
'''Remark to Response to Answer:''' On ASUS-500GX is possible make external port tagged in this way 'nvram set vlan0ports="1t 2 5*"'. This is syntax like robocfg tool. Tested on WhiteRussianRC2, may be possible on all BCM5325 HWs

== Intro ==
The author of this Howto had a need to use VLAN support to keep wifi and wired traffic separate on his network. There are other, more reliable ways of achieving this, but none came anywhere close in cost to using a WRT. Even a small name-brand switch that supports VLANs will run you a fairly high price.

== What are you trying to do here? ==
In order for people to understand the goal I am trying to achieve, consider this illustration:

We have two LinkSys WRT54G routers. Each has 5 ethernet jacks on the back of it, one of these ports is a CrossOver port (labeled "WAN" in software, or "Internet" on the back of the device). The other 4 are regular ports. Now, don't ask me WHY anyone would want to do the following, but just rest assured that it is a valid example that will demonstrate what this howto attempts to achieve. What we are going to do is create 5 VLANs, one for each regular port on the router, plus one for the WiFi interface. We then want to used a TaggedTrunk to connect the two routers together via their "Internet" port (NOTE: these ports should be connected with a StraightThrough cable). When all is said and done, port 1 of router A should be able to see port 1 of router B, port 2 on router A should see port 2 on router B, etc.

== So, how do we do it? ==

Well, that's what I'm working on, and also asking for help here. If anyone has suggestions or information that could be helpful, please add it here or email it to me via bhook(at)coder7(dot)com or bhook(at)kssb(dot)net.

== Initial Info ==

This will likely require the use of the admcfg package, which allows us to configure the switch that controls the 5 (really it's 6) ethernet ports on the WRT54G. And just for the benefit of others that may be searching, here is what I found for documentation on the admcfg utility:

USAGE:
admcfg [<port> [option]]

      port is in the form of "portX"

      option is one of:

            ENABLED, DISABLED - enable/disable port

            100Mbps, 10Mbps - port speed

            FD, HD - full duplex/half duplex

            FLOW, NOFLOW - 802.3 flow control

            TAG, UNTAG - output vlan tagging

            TOS, VLAN - priority given to TOS/VLAN

            PRIO, NOPRIO - port based priority

            PVID:X - set the primary vlan id

            vlanX - set the vlan mappings 


So, in theory, a command like `admcfg port0 TAG` should enable VLAN tagging on our trunk, then it would just be a matter of resetting some nvram values, or, as a safer alternative, using the admcfg utility to set which ports are members of which vlans (a power cycle will flush the setting from admcfg).

When using admcfg in startup scripts, I read a rather good suggestion of setting a delay of 1 minute before making changes. This way, if you typo or put in some really odd config (or forget your config), you can powercycle your wrt and attempt to salvage it in the first 60 seconds.

== First success ==

Okay, I grabbed two WRTs and loaded openwrt (snapshot-20050202). I got them configured to access the internet (via yet another wrt, running stock firmware) and ran ipkg to get admcfg and dropbear (I prefer ssh... even though it is completely unneccessary at this point). Just for those that need step by step (you'll have to figure out how to get connected on your own):

  `rm /etc/ipkg.conf`

  `cp /rom/etc/ipkg.conf /etc/ipkg.conf`

  `vim /etc/ipkg.conf #you need to add the line 'src rop http://www.xs4all.nl/~rop/openwrt' to this file`

  `ipkg update`

  `ipkg install admcfg`

  `ipkg install dropbear #optional, and you will be asked to assign a password`


Now, I ssh into one of my WRTs on any of ports 1-4 to issue the following commands (note: if you really want you can jack with vlan0/1 and pvid0/1, but these could end up disconnecting you from your WRT):

  `ifconfig br0 down`

  `brctl delbr br0`

  `insmod adm.o`


  `admcfg port0 vlan0 vlan1 vlan2 vlan3 vlan4 vlan5 vlan6 vlan7 vlan8 vlan9 vlan10 vlan11 vlan12 vlan13 vlan14 vlan15 PVID:2 TAG`

  `vconfig add eth0 2`

  `ifconfig vlan2 10.0.0.1 netmask 255.0.0.0 up`


Now, do the same exact thing on the second router, except you want to change that last command to:

  `ifconfig vlan2 10.1.0.1 netmask 255.0.0.0 up`


Hook the "Internet" ports of both routers together with a StraightThrough cable, then issue the following command on the first router:

  `arping -I vlan2 10.1.0.1`

If you are getting back replies, then things seem to be working.


== Second Success ==

 Router A:

  `admcfg port3 vlan3 PVID:3`

  `admcfg port4 vlan4 PVID:4`

  `vconfig add eth0 3`

  `vconfig add eth0 4`

  `ifconfig vlan3 10.0.3.1 netmask 255.0.0.0 up`

  `ifconfig vlan4 10.0.4.1 netmask 255.0.0.0 up`

 Router B:

  `admcfg port3 vlan3 PVID:3`

  `admcfg port4 vlan4 PVID:4`

  `vconfig add eth0 3`

  `vconfig add eth0 4`

  `ifconfig vlan3 10.1.3.1 netmask 255.0.0.0 up`

  `ifconfig vlan4 10.1.4.1 netmask 255.0.0.0 up`

NOTE: The IPs are different in these two blocks, that is the only difference.

Now, this builds on the section above, so if you haven't got that working (namely tagging on port0), then this most certainly will not work either. However, if you have done things right, then a normal machine plugged into port 3 of either switch should be able to ARP both router's and their IP addresses. Unfortunately, there seems to be a glitch somewhere, because you can now ARP all of the IP address active on both devices. I have read somewhere that there is a glitch in admcfg that creates the ARP bridging, though I haven't confirmed this.

== Problems ==
 *it seems that busybox and possibly some other apps on these devices wont pick up the additional interfaces and IPs, hence not being able to just use `ping` as a sure way to verify things (it works sometimes).
 *I can't seem to make certain vlans go away on certain ports. I haven't figured out WHY it's like this, and it is very inconsistent.

== Notes ==
 *Keep in mind that the WRT uses an internal 6 port switch, with port 0 being the WAN/Internet port, 1-4 being exactly what you expect (ie, ports 1-4), and port 5 being an internal connection to the WRT itself. You probably DO NOT want to jack with the vlan settings for port 5, ever.
 *90% of the commands you type are actually executing busybox through a symlink. This can cause some issues, since busybox isn't intended to be a full-featured version of the commands it replaces. For example, you can't force the interface to send pings from.
 *I haven't figured out what exactly to do with the WIFI yet. I know that eth1 is the physical interface, but I'm not quite sure how to bridge it onto port 0 with an actual VLAN assigned to it. My best guess at this point is to set the PVID for port 5 to something other than 0, but as mentioned above I have no clue what will happen when you start screwing with port 5.
 *About speed: I tested it here with two PCs (both with eepro1000) and a wrt54gs between. Both PCs had an own VLAN. The Speed for FTP was around 3.7 M/s and the load on the Linksys was arount 0.7.

== A little help ==
 *A script which may help some people. Create a file `vi /etc/init.d/S41network` and copy this:

`#!/bin/sh`

`ifconfig br0 down #disables default bridge br0`

`brctl delbr br0     #deletes default bridge br0`

`#`

`insmod adm.o    #loads admcfg module`

`#`
 
`admcfg port0 PVID:1 vlan1   #sets port0 (internet) #leave that as vlan1.`

`admcfg port1 PVID:0 vlan0   #sets port1 as vlan0`

`admcfg port2 PVID:2 vlan2   #sets port2 as vlan2`

`admcfg port3 PVID:3 vlan3   #sets port3 as vlan3`

`admcfg port4 PVID:4 vlan4   #sets port4 as vlan4`

`#`
 
`vconfig add eth0 0  #creates vlans`

`vconfig add eth0 1`

`vconfig add eth0 2`

`vconfig add eth0 3`

`vconfig add eth0 4`

`#`
 
`#assign ip addresses`

`ifconfig vlan1 192.168.2.1 netmask 255.255.255.0 broadcast 192.168.2.255 up #iport labeled internet`

`ifconfig vlan0 192.168.1.1 netmask 255.255.255.0 broadcast 192.168.1.255 up #port labeled port1`

`ifconfig vlan2 192.168.3.1 netmask 255.255.255.0 broadcast 192.168.3.255 up #port labeled port2`

`ifconfig vlan3 192.168.4.1 netmask 255.255.255.0 broadcast 192.168.4.255 up #port labeled port3`

`ifconfig vlan4 192.168.5.1 netmask 255.255.255.0  broadcast 192.168.5.255 up #port labeled port4`

`#` 

`ifconfig eth1 192.168.6.1 netmask 255.255.255.0 broadcast 192.168.6.255 up #wireless port`

Then save the file and don't forget to `chmod +x /etc/init.d/S41network`
Now the only thing you have to do is alter the IPs, netmasks and broadcasts.
