#acl Known:read,write All:read
##
## Note: these pages document the firmware itself, not packages
##       questions/comments should be posted to the forum
##
##
##
##
## PLEASE POST ALL QUESTIONS ABOUT THE DOCUMENTATION ON THE FORUM.
## I DO NOT WANT TO HAVE TO LOCK DOWN EDITS ON THESE PAGES
## - mbm
##
## (no, don't reply here, use the forum)
##
##
##
##
##
##
##
##
##
##
##
##
##

OpenWrtDocs [[TableOfContents]]

= Wireless problems =
If you have WPA encryption enabled, you need to install nas before wireless will connect.

{{{
ipkg install nas; reboot
}}}

= Failsafe mode =
If you've broken one of the startup scripts, firewalled yourself or corrupted the JFFS2 partition, you can get back in by using !OpenWrt's failsafe mode. Full failsafe mode is only working when you have installed one of the SquashFS images.

== How to get into failsafe mode ==
!OpenWrt'' itself ''uses the reset button to enter into failsafe mode, and for no other purpose.  In particular, it will'' not ''reset the NVRAM.  The ''boot loader'', however, may reset the NVRAM in response to the reset button.  Therefore, it's important to know what's running when you hold down the reset button.  One indicator is that !OpenWrt will light the DMZ LED (on systems that have one) from the time it begins until the time the bootup scripts complete.  If the DMZ LED has not yet lit up, you are still in the bootloader!

=== All Models (RC5+) ===
When OpenWrt boots, it will broadcast a UDP packet to port 4919 of network 192.168.1.x containing the message:
{{{
Press reset now, to enter Failsafe!
}}}

You can use the recvudp utility provided below, or a network monitor/sniffer to view the messages, for example `nc -l  -p 4919 -u`. Remember, your PC must be set to have an address like 192.168.1.2 When the above message appears, press and hold the reset button for 2 seconds. You should now get the message:
{{{
Entering Failsafe!
}}}

===  Older releases / model specific ===
==== Linksys models ====
Plug in the router and wait for the DMZ LED to light up.  Then immediately press and hold the reset button for 2 seconds. If done right the DMZ LED will quickly flash 3 times every second.

/!\ Holding the reset button ''before'' the DMZ LED turns on (i.e. when the bootloader is still running) can reset the NVRAM.  Resetting the NVRAM will brick some models.

==== Non-Linksys models ====
Plug in the power, wait 2 secs, then press and hold the reset button for 10-15 seconds.

== What should I do in failsafe mode? ==
Once in failsafe mode, the router will ignore the configuration and use the ip address 192.168.1.1 and will boot directly into a telnet server, bypassing normal boot up. There will be no DHCP server, and the JFFS2 partition won't be mounted.

/!\ Tips:
 * Recover root, for example using FreyFunk WEB interface you can change the password becouse not need authentication.
 * Your router will listen on the LAN port(s) only.  You will not be able to connect via the WAN port in failsafe mode.
 * Failsafe has no DHCP, make sure you set a static IP address.
 * The act of switching between a normal boot and failsafe mode could change your MAC address! This will invalidate the ARP cache of the workstation you're using to access !OpenWrt with.  If you can't ping !OpenWrt at {{{192.168.1.1}}} flush your ARP cache:

{{{
arp -d *
}}}

If you want to COMPLETELY ERASE the JFFS2 partition, removing all packages, you can run:
{{{
firstboot
}}}

to begin erasing, and then:

{{{
sync
}}}

to make sure that the Linux kernel actually commits this erasure to flash.

If you want to attempt to fix the JFFS2 partition, mount it with the following command:
{{{
/sbin/mount_root
}}}

= Resetting to defaults =
/!\ '''NOTE: Resetting NVRAM this way will actually cause more problems than it solves. For example, Asus WL-500g and the Motorola WR850G bootloader will not recreate default values and will not boot properly after being reset. If you do this on a Siemens SE505 V1, your router will not be accessible to you anymore! You will have to reflash it with the stock firmware on ip address 192.168.1.1 (NOT 192.168.2.1 as the installation procedure says!!)'''

To clean the NVRAM variables the safe way see the !OpenWrt ["Faq"].

If you're having trouble setting up some feature of your router (wireless, LAN ports, etc) and for some reason all of the documentation here just isn't working for you, it's sometimes best to start from scratch with a default configuration. Sometimes the various firmwares you try will add conflicting settings to NVRAM that will need to be flushed. Erasing NVRAM ensures there aren't any errant settings confusing your poor confused router. Run this command to restore your NVRAM to defaults:

{{{
mtd -r erase nvram
}}}
This will clear out the NVRAM partition and reboot ({{{-r}}}) the router, the bootloader will create a new NVRAM partition with default settings after the reboot. Remember to set {{{boot_wait}}} back on after you reboot your router -- trying to do it before rebooting will just write your old settings (cached in memory) back to the flash.

To reset NVRAM settings on a Siemens SE505 V1 simply press reset after you plug it in and release as soon as one of the leds starts flashing very fast.

= Recovering from bad firmware =
See ["OpenWrtDocs/Installing"] for generic installation instructions.

== Software based method ==
Reflash the unit using the [:OpenWrtViaTftp:TFTP] method.

== Serial console ==
Important information about connecting a serial console can be found in ["OpenWrtDocs/Customizing/Hardware/Serial Console"], Information about CFE can be found in ["OpenWrtDocs/Customizing/Firmware/CFE"].

Set {{{boot_wait=on}}} in CFE and then TFTP the firmware image. To enter CFE hit {{{CTRL-C}}} right after power on.

{{{
CFE> nvram set boot_wait=on
*** command status = 0
CFE> nvram commit
*** command status = 0
CFE>
}}}
After this use the normal TFTP instructions found in ["OpenWrtDocs/Installing"].

On Linksys models you can use another way too. Setup a local TFTP server on your PC and then execute the following commands inside CFE

{{{
CFE> ifconfig eth0 -addr=192.168.1.1 -mask=255.255.255.0
CFE> et up
CFE> flash -noheader 192.168.1.2:/openwrt-brcm-2.4-squashfs.trx flash1.trx
}}}
A simpler method is to have the CFE go into a voluntary boot_wait TFTP reception in this manner:

{{{
CFE> ifconfig eth0 -addr=192.168.1.1 -mask=255.255.255.0
CFE> et up
CFE> flash -noheader : flash1.trx
}}}
The CFE will enter TFTP receptive mode after that command.

== JTAG adaptor method ==
/!\ '''WARNING:''' You are now leaving the safe grounds of warranty coverage.

'''Linksys models'''

 * refer to ["OpenWrtDocs/Customizing/Hardware/JTAG Cable"] howto create a JTAG cable
 * get !HairyDairyMaids [http://www.ranvik.net/prosjekter-privat/jtag_for_wrt54g_og_wrt54gs/ debrick utility] or a more recent version from [http://downloads.openwrt.org/utils/ Downloads] and instructions how to connect everything together
 * turn the router off, attach the jtag cable
 * turn it on, and issue one command
 * don't hurry, sometimes you'll need to wait a bit
 * BACKUP BEFORE MAKING ANY CHANGES

{{{
wrt54g -backup:cfe
}}}
will backup the CFE bootloader; you will need this later.

{{{
wrt54g -erase:nvram
}}}
will delete the nvram, if you just borked the nvram, you will be done here.

{{{
wrt54g -erase:kernel
}}}
if you've borken the kernel, you have to delete the kernel, in order to flash a new one

{{{
wrt54g -erase:cfe
}}}
if you managed to crap the cfe, you can delete it

{{{
wrt54g -flash:cfe
}}}
if you have the appropriate CFE.BIN image for your router in the same dir as the debrick utility, this will flash the router with the new cfe. Once you've flashed a CFE with boot_wait enabled, you can use tftp to upload a new kernel.

On Linux, don't forget to unload 'lp' module and load 'ppdev'.

= Getting help =
Still stuck? See [http://openwrt.org/support how to get help and support] for information on where to get further help.
