= Work in Progress =
Porting OpenWrt to the DSL-502T is a work in progress.

This page is to assist those working in that direction.

Thanks Strider for starting the page off for me.

Thank you nbd and all the OpenWRT developers for making this work-Z3r0 (not the z3r0 on IRC)

Thank you Mr Chandler for fixing some of the formatting.

Note, as of 17th May '07 I am no longer maintaining this page as I no longer have a DSL-502T, if you would like to update this page please feel free to. (Z3r0)

(I'm starting to update this page to reflect the current port status. -- OliverJowett)

== Specifications ==

 * ADSL modem with ADSL2/2+ support to 24Mbit/s+.
 * Single 100MBps LAN port.
 * Single USB-B port (default firmware uses this to provide USB-over-ethernet to a PC host only, it's not clear if this can actually be used as a USB host)
 * Flash chip: 4MBytes - Samsung K8D3216UBC a 32Mbit NOR-type Flash Memory organized as 4M x 8
 * SDRAM: 16Mbytes - Nanya NT5SV8M16DS-6K
 * CPU: TNETD7300GDU Texas Instruments AR7 MIPS based

== How to get OpenWRT onto the router: ==
'''Preamble/Disclaimer'''

It's possible (but unlikely) that you will 'brick' the router (e.g. if you manage to delete the bootloader or config space) such that it can't be booted at all. This needs a JTAG cable to recover from. They are around US$20 from eBay.

In most other situations, the worst that will happen is that you will have to power-cycle the router and flash known good firmware onto the router to recover it.

'''Get the source code'''

The sourcecode is held in a subversion repository and is updated continuously. Install the subversion package (e.g. using the synaptic package manager on ubuntu). To get the latest trunk code:
{{{
$ svn co https://svn.openwrt.org/openwrt/trunk
}}}

To get a specific revision:
{{{
$ svn -r6250 co https://svn.openwrt.org/openwrt/trunk
}}}

To update an existing checkout to the latest version (only the changes are downloaded):
{{{
$ svn update
}}}

'''Apply useful patches that aren't in subversion yet'''

These are patches that have tickets open but haven't made it into the subversion tree yet:

 * Front panel LED support: [https://dev.openwrt.org/ticket/2746]
 * Make LEDs blink on network activity: [https://dev.openwrt.org/ticket/2776]
 * Enable WAN (ADSL) interface automatically on boot: [https://dev.openwrt.org/ticket/2781]

In general they can be applied by downloading and saving the "original version" of the patchfile attached to the ticket, then {{{"cd openwrt/trunk; patch -p0 <name-of-patch-file"}}}

'''Download source code for optional extra packages'''

Browse [https://dev.openwrt.org/browser/packages] and see if there's anything you want. Then check out the relevant packages into the "package" directory the tree you previously checked out:
{{{
$ cd openwrt/trunk/package
$ svn co https://svn.openwrt.org/openwrt/packages/net/ntpclient
$ svn co https://svn.openwrt.org/openwrt/packages/net/tcpdump
}}}

''' Install prerequisites for compiling'''

For Ubuntu grab 'build essentials' 'flex' 'bison' 'autoconf' 'zlib1g-dev' 'libncurses5-dev', 'automake', 'g++'  i.e
{{{
$ apt-get install flex bison autoconf zlib1g-dev libncurses5-dev automake g++
}}}

'''Select firmware components'''

Enter into the folder and run make menuconfig. Select at least:
 * Target System -> TI AR7 [2.6]
 * Target Profile -> No Wifi
 * Target Images -> SquashFS
 * Base system -> br2684ctl (only needed by PPPoE)
 * Network -> ppp -> ppp-mod-pppoa and/or ppp-mod-pppoe, depending on your ADSL type
 * Kernel Modules -> Network Devices -> select either annex A or B depending on your ADSL type (B = Germany only?). The annex of your router is marked on the PCB if you don't mind opening the case.

Quit and save the config.

Run 'make' to download essential packages (approximately 100MByte) and compile the firmware. Go and get a coffee. Maybe a second coffee too.

The final firmware produced by the build is located in bin/openwrt-ar7-squashfs.bin.

'''Flash the new firmware'''

 * Download a copy of the standard D-Link firmware so you can revert to it if things go wrong! You need the "web upgrade" .BIN version of the firmware, not the .EXE version. D-Link firmware can be downloaded from (for example) [http://www.dlink.com.au/tech/]
 * Get [https://dev.openwrt.org/attachment/ticket/2780/adam2flash-502T.pl?format=raw adam2flash-502T.pl].
 * Configure your PC for a static IP address, I'd suggest 192.168.1.2 (or another address on that subnet)
 * Choose an IP address for your router. The OpenWrt firmware will use 192.168.1.1 after rebooting, so that's a sensible choice.
 * Turn off the router.
 * Run adam2flash-502T.pl, providing the router IP address you chose and the new firmware to upload. If you are changing between D-Link and OpenWrt firmware, you will also need to specify -setmtd1 (if you forget this, the script will tell you that you need it and exit)
 * Turn on the router.
 * Wait for the upload to complete. Here's a sample session:
{{{$ scripts/adam2flash-502T.pl 192.168.1.1 -setmtd1 bin/openwrt-ar7-squashfs.bin 
Looking for device: ..... found!
ADAM2 version 0.22.2 at 192.168.1.1 (192.168.1.1)
Firmware type: OpenWRT (little-endian)
logging into ADAM2 bootloader.. ok.
checking hardware.. AR7RD / DSL-502T.
checking MTD settings.. ok.
Firmware size: 0x00280004
Available flash space: 0x003e0000
Preparing to flash.. ok.
Erasing flash and establishing data connection (this may take a while): ok.
Writing firmware: ... (lots more dots) ... done.
Rebooting device.}}}
 * Watch the LEDs and wait for the router to reboot. After a while, you should be able to ping 192.168.1.1!

For more information on the firmware & memory layout of the DSL-502T, see the [https://dev.openwrt.org/attachment/ticket/2780/adam2flash-502T.pl comments in adam2flash-502T.pl]

You can also use adam2flash-502T.pl to restore the original D-Link firmware if needed - it recognizes D-Link firmware and adjusts MTD settings accordingly.

'''Connecting to ADAM2 manually'''

If you need to manually tweak firmware settings, you can do so by getting adam2flash to assign the bootloader an IP then doing a manual telnet to the FTP control port:
{{{
$ scripts/adam2flash-502T.pl 192.168.1.1 && telnet 192.168.1.1 21
}}}
Now you are connected to the bootloader FTP server. Log in with "USER adam2" and "PASS adam2".

'''Checking that it worked'''

If you applied the LED patches above, the router will go through three states while rebooting:

 1. "status" off - bootloader running
 2. "status" flashing rapidly - image loaded OK, kernel booted, OpenWrt initializing
    * "ADSL" should start flashing as the DSL line is brought up
    * "Ethernet" should turn on as the ethernet interface is brought up
    * If you've configured PPP (see below), "USB" should turn on as the PPP layer is brought up
 3. "status" pulsing in a heartbeat (pulse pulse - pause - pulse pulse - pause) - OpenWrt completed booting, normal operation

If you didn't apply the LED patches.. the only LED that will do anything is the ADSL LED.

Some time after rebooting, you should be able to ping or telnet to 192.168.1.1. If so -- congratulations!

You can reconfigure your PC for DHCP if you like, you should be given an IP in the 192.168.1.x range.

'''Password protect the router'''

Get a ssh client such as, well, "ssh"!. Under Window, try [http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html PuTTY].

Telnet to the router and type 'passwd' to set a password. Now telnet will be disabled, and you should log back in over ssh.

== Enabling ADSL ==
'''Set up modulation'''

Current firmware supports both ADSL1 (G.DMT, G.lite, T.1413, Multi-Mode) and ADSL2+.

The modulation can be changed via the adam2 prompt: "SETENV modulation,GDMT" or T1413/GLITE/MMODE. Or specify a hex bitmask of allowable modes. The NZ firmware has modulation=0xffff (allow all modes) and this appears to auto-negotiate ADSL1 and ADSL2 modes as appropriate.

 * G.DMT supports up to 8mbit/s.
 * T.1413 is an older version of G.DMT.
 * G.Lite is a lighter version of G.DMT that supports up to 1.5Mbit/s.
 * MMODE is Multi-Mode and negotiates the best mode that it can.

'''Check your line is in sync'''

If DSL is working, the ADSL LED should be solidly on. Check 'dmesg' for DSL log messages. You should see something like this:
{{{
registered device TI Avalanche SAR
Sangam detected
requesting firmware image "ar0700xx.bin"
avsar firmware released
tn7dsl_set_modulation : Setting mode to 0xffff
Creating new root folder avalanche in the proc for the driver stats 
Texas Instruments ATM driver: version:[7.02.01.00]
DSL in Sync
}}}

You can also do cat /proc/avalanche/avsar_modem_training and if it says "IDLE" that means you've probably set the wrong annex, if it says "INIT" that is good as the modem is negotiating a speed with the exchange, then it should say "SHOWTIME" when it is ready to work.

You can also do cat /proc/avalanche/avsar_modem_stats this is the best way of working out if you connection is initialised as it will show Upstream/Downstream sync speeds.

'''PPPoA configuration'''

Edit /etc/config/network. Add a section like this at the end:
{{{
config interface wan
        option ifname   ppp0
        option unit     0
        option proto    pppoa
        option encaps   vc
        option vpi      0
        option vci      100
        option username (your username here)
        option password (your password here)
        option keepalive 5,5
}}}

encaps should be "vc" or "llc".
vpi and vci are specific to your ISP.

'''PPPoE configuration'''

Previously, there was lots of manual setup info here, but it all seemed horribly out of date.
If someone has current experience with PPPoE, please fill in something up-to-date here.
I would guess that it is mostly similar to PPPoA with "proto pppoe" and perhaps "encaps llc".
-- OliverJowett

It's not that simple, for pppoe you have to bring up an ATM-bridge (you can uncomment the example in /etc/config/network)
But I never had enough information on how configuring the pppoe interface... I had tried all the conf in the links at the end of this document but no one worked for me.
In the end I have solved the issue by calling my ISP for changing from pppoe to pppoa.
-- War3333

'''Connect to your ISP directly using DHCP'''

Most people will be using PPPoE or PPPoA. However, if you are using DHCP, please read this thread: http://forum.openwrt.org/viewtopic.php?id=8019

'''Bring up the ADSL connection'''

{{{
ifup wan
/etc/init.d/firewall restart
/etc/init.d/ledsetup restart  # if you installed the LED patches
}}}

The firewall and ledsetup only needs to be restarted after making configuration changes, not every time.

Currently the ADSL connection will not start automatically on boot. See [https://dev.openwrt.org/ticket/2781] for a patch to fix this, or manually run 'ifup wan' after a reboot.

The "USB" LED should turn on (it's been hijacked to display PPP state, not USB state), and 'ifconfig' should show something like this:

{{{
ppp0      Link encap:Point-to-Point Protocol  
          inet addr:222.154.180.230  P-t-P:125.237.255.1  Mask:255.255.255.255
          UP POINTOPOINT RUNNING NOARP MULTICAST  MTU:1500  Metric:1
          RX packets:1742 errors:0 dropped:0 overruns:0 frame:0
          TX packets:1818 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:3 
          RX bytes:1313740 (1.2 MiB)  TX bytes:306881 (299.6 KiB)
}}}

'logread' should show some PPP connection messages:
{{{
Dec  1 06:17:42 OpenWrt daemon.info pppd[638]: Plugin pppoatm.so loaded.
Dec  1 06:17:42 OpenWrt daemon.notice pppd[639]: pppd 2.4.3 started by root, uid 0
Dec  1 06:17:42 OpenWrt daemon.info pppd[639]: Using interface ppp0
Dec  1 06:17:42 OpenWrt daemon.notice pppd[639]: Connect: ppp0 <--> 0.100
Dec  1 06:17:43 OpenWrt daemon.notice pppd[639]: PAP authentication succeeded
Dec  1 06:17:43 OpenWrt daemon.notice pppd[639]: PAP authentication succeeded
Dec  1 06:17:43 OpenWrt daemon.notice pppd[639]: local  IP address 222.154.81.8
Dec  1 06:17:43 OpenWrt daemon.notice pppd[639]: remote IP address 125.237.255.1
Dec  1 06:17:43 OpenWrt daemon.notice pppd[639]: primary   DNS address 202.27.158.40
Dec  1 06:17:43 OpenWrt daemon.notice pppd[639]: secondary DNS address 202.27.156.72
}}}

And you should now have internet access!

'''Set up port forwarding'''

For general port forwarding, edit /etc/config/firewall and follow the comments. Run '/etc/init.d/firewall restart' after configuration changes.

'''How to give interfaces fixed IP addresses'''

For port forwarding you need to have fixed IP addresses, just find out the MAC address of the ethernet card via the XP command prompt ipconfig /all or via linux ifconfig.

Then add an appropriate line to /etc/ethers matching the ethernet MAC address to an IP, e.g.
{{{
00:30:1B:B5:DC:D8 192.168.1.2
}}}

Finally, run '/etc/init.d/dnsmasq' to ensure that the DHCP server picks up the configuration change.

== Troubleshooting ==
'''WPNT834 Performance problem'''

Poor performance of the ADSL connection exists between the Netgear WPNT834 Rangemax 240 and D-Link DSL-502T, characterised by poor transfer speeds which may be asynchronous in nature, many retransmits and general packet loss in TCPdump and poor telnet access/webpage access to the DSL-502T, this is caused by poor ethernet performance between the two devices. This is possibly caused by a duplex mismatch or buggy 100FD/HD code on one of the devices.

The only way to solve this at present is to force the DSL-502T ethernet connection to Autonegotiate 10Mbit/s by changing one line of source code: see the last two posts here:

 . http://forum.openwrt.org/viewtopic.php?id=8117
== How to Debrick ==
You can generally use the methods on DLinks site or just change ur mtd0/1/4 variables back to defaults and upload the dlink firmware.

But if you've accidentally destroyed your mtd2 adam2 bootloader or mtd3 config file you will need a JTAG cable.

'''Instructions for debricking with a JTAG'''

'''How to get hold of a JTAG or make one '''

I grabbed one from ebay but you can make your own with 4/5 resistors, pin schematics are here:

http://wiki.openwrt.org/AR7Port http://wiki.openwrt.org/OpenWrtDocs/Customizing/Hardware/JTAG_Cable

The cable I purchased from Ebay was for the WRT54G, it had a 12 pin header, whereas my router had an already soldered 14 pin header, the WRT54G uses EJTAG 2.0 and the AR7 uses EJTAG 2.6, to make the JTAG cable work I simple connected pin 1 TRST with pin 8 VCC/VIO/VRED via a 100 ohm resistor (I didn't  bother soldering it on) and then placed the 12 pin JTAG on top squashing it into place, bending back the extra 2 pins.

My pins are numbered as so:

{{{
1 (TRST) - 14
2 - 13
3 - 12
4 - 11
5 - 10
6 - 9
7 - 8 (VIO/VCCC/VREF)
}}}
'''Bios settings'''

My BIOS settings for my printer port were: ECP+EPP, 0x378.

'''Using the Debrick utility to restore the bootloader and config'''

Once you do this you can use HairyDairyMaids debrick utility 4.8 Get it here:http://downloads.openwrt.org/utils/

Under Windows: load giveio.sys by running loaddrv.exe and adding 'giveio.sys' to the end of the line and clicking install+start.

Under Linux (Ubuntu): Get the build essentials package, compile the binary using 'make' from the folder you extracted the files to, then you need to do this to read the parallel port: rmmod lp, modprobe parport, mknod /dev/parport0 c 99 0

You can now do ./wrt54g -probeonly to test if the unit can be detected

Grab Olegs Adam2 bootloader: http://star.oai.pp.ru/jtag/adam2-oleg.zip

rename the adam2 file to CUSTOM.BIN then do:

./wrt54g -flash:custom  /noerase /nobreak /nodma /window:0x90000000 /start:0x90000000 /length:0x10000  /nocwd

Grab mtd3 config http://mcmcc.bat.ru/dlinkt/restore_mtd3_50xT.rar

rename this to CUSTOM.BIN then do:

./wrt54g -flash:custom  /noerase /nobreak /nodma /window:0x903f0000 /start:0x903f0000 /length:0x10000  /nocwd

You may not have to do /noerase /nobreak or /nocwd but /nodma is required

Once this is done, set you lan IP as 10.8.8.1 subnet 255.0.0.0 (on Linux u need to do ifconfig eth0 10.8.8.1 to set your IP) and then reboot the router, ftp into 10.8.8.8 21 using the command prompt FTP (not anything else) and you will see an adam2 prompt (gratz!).

ping 10.8.8.8 to see if adam2 is working

'''Uploading the original firmware'''

Now that ADAM2 is working, you can use adam2flash-502T.pl to install firmware of your choice, including the original D-Link firmware. See above.

== Further Information ==
Old threads that may be of some use:

How to debrick the DSL-502T: http://forum.openwrt.org/viewtopic.php?id=7742

How to bring up the ADSL interface: http://forum.openwrt.org/viewtopic.php?pid=35563

PPPoE on the DSL-502T: http://forum.openwrt.org/viewtopic.php?pid=35563

Script to bring up the ADSL interface on bootup: http://forum.openwrt.org/viewtopic.php?id=8342

How to change passwd:[http://forum.openwrt.org/viewtopic.php?id=8342 http://forum.openwrt.org/viewtopic.php?id=9093]

VCMUX/LLC howto: http://forum.openwrt.org/viewtopic.php?id=8700

WPNT834 with DSL-502T duplex mismatch bug: http://forum.openwrt.org/viewtopic.php?id=8117

Bridged DSL (not PPP): http://forum.openwrt.org/viewtopic.php?id=8019

Couldn't increase MTU to 1500: http://forum.openwrt.org/viewtopic.php?id=9281

----
 . ["CategoryAR7Device"]
