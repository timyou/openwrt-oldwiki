#acl Known:read,write All:read
##
## Note: these pages document the firmware itself, not packages
##       questions/comments should be posted to the forum
##
[:OpenWrtDocs]
[[TableOfContents]]
= Failsafe mode =
If you've broken one of the startup scripts, firewalled yourself or corrupted the jffs2 partition, you can get back in by using OpenWrt's failsafe mode. To get into failsafe, plug in the router and wait for the DMZ led to light then immediately press and hold the reset button for 2 seconds. If done right the DMZ led will quickly flash 3 times every second.

( /!\  The act of switching between a normal boot and failsafe mode could change your mac address!  This will invalidate the arp cache of the workstation you're using to access OpenWRT with.  If you can't ping OpenWRT at 192.168.1.1, check the cache with 'arp -a' and delete it with 'arp -d 192.168.1.1'. )

( /!\  holding the reset button before the DMZ led can reset NVRAM )

( /!\  the ASUS WL-300G does not have a DMZ led : press the reset button for 2 seconds just after the AIR led lights, or maybe the LAN led. At some point it works, anyway. )


When in failsafe, the system will boot using only the files contained within the firmware (the squashfs partition) ignoring any changes made to the jffs2 partition. Additionally, various network settings will be overridden forcing the router to 192.168.1.1.

If you want to completely erase the jffs2 partition, removing all packages you can run firstboot.

If you want to attempt to fix the jffs2 partition, mount it with the following commands:
{{{
mtd unlock /dev/mtd/4
mount -t jffs2 /dev/mtdblock/4 /jffs
}}}
After the partition is mounted, you can edit the files in /jffs. If you run firstboot with the jffs2 partition mounted, it will not format the partition, but it will overwrite files with symlinks. (Packages will be preserved, changes to scripts will be lost)

Note: if you cannot figure out how to put your device into failsafe mode then remember that you can always modify the boot scripts in the source. So if you want to boot failsafe mode, you might edit your buildroot/build_mipsel/root/etc/preinit to something like this:
{{{
#!/bin/sh
mount none /proc -t proc              
mount none /tmp -t ramfs
export FAILSAFE=true                  
exec /sbin/init         
}}}
Build a new image by typing make in the buildroot directory, install the modified firmware and boot the device. This forces your device to boot in FAILSAFE every time. So in order to boot in normal mode, you'll have to undo the changes you've made to the preinit file.

ASUS WL-500G units seem to respond only on the WAN port when booted in failsafe mode. ASUS WL-300G responds only on the LAN port in failsafe mode.


= Resetting to defaults =

( /!\  resetting the NVRAM is not a good idea on every model, for example wl500g bootloader will not recreate default values, avoid deleting nvram )

If you're having trouble setting up some feature of your router (wireless, lan ports, etc) and for some reason all of the documentation here just isn't working for you, it's sometimes best to start from scratch with a default configuration.  Sometimes the various firmwares you try will add conflicting settings to NVRAM that will need to be flushed.  Erasing NVRAM ensures there aren't any errant settings confusing your poor confused router. Run this command to restore your NVRAM to defaults:
{{{
mtd erase nvram
reboot
}}}
This will clear out the NVRAM partition and reboot the router, the bootloader will create a new NVRAM partition with default settings after the reboot. Remember to set boot_wait back on after you reboot your router -- trying to do it before rebooting will just write your old settings (cached in memory) back to the flash.

To reset changes you've made to the OpenWRT filesystem, run
{{{
firstboot
}}}
If firstboot is run while the jffs2 filesystem is mounted (eg. non-failsafe mode) it will skip formatting and only reset changed files to their defaults. (Files are overwritten with symlinks to their original copy in /rom; extra files and packages are left intact)

After these two steps, you'll have a router with a pristine unchanged configuration.  Everything should work now.

= Recovering from bad firmware =
== Software based method ==
If you've followed the instructions and warnings you should have boot_wait set to on. With boot_wait on, each time the router boots you will have roughly 3 seconds to send a new firmware using tftp. Use a standard tftp client to send the firmware in binary mode to 192.168.1.1. Due to limitations in the bootloader, this firmware will have to be under 3MB in size.

See ["OpenWrtDocs/Installing"][[BR]]
[:OpenWrtDocs/Installing#head-f56e06c42cb97a7aace9a5b503d0d288697d98d9:"3.2. Using boot_wait to upload the firmware"]

/!\  The Motorola [:OpenWrtDocs/Hardware/Motorola/WR850G:WR850G] may wait for an image on 192.168.10.1

/!\  the ASUS WL-300G does not have a DMZ led : press the reset button for 2 seconds just after the AIR led lights, or maybe the LAN led. At some point it works, anyway.

== JTAG-adaptor Method ==
'''you are now leaving the safe grounds of warranty coverage'''

You still don't want to short any pins on your precious router. Thats nasty disgusting behaviour. A lot better way to get a Flash into your wrecked piece of hardware, is to build your own JTAG-adaptor. It's easy, you can make it in a jiffy using spare parts from the bottom of your messy drawer. You need:
 1. 4 100R resistors
 1. 1 male SUB-D 25 plug
 1. If you want to do it right, a 12-way IDC-Connector plug (these are the ones who look like the HDD-Cables)
 1. A 12-way ribbon cable for above
 1. The boyfriend of that IDC-Connector for the PCB
 1. HairyD''''''airyMaids [http://spacetoad.com/tmp/hairydairymaid_debrickv22.zip "zip-file"] with a debrick utility and instructions how to connect everything together.
 1. A Linksys WRT54G with a broken flash and the desperate feeling that you can't make it any worse.

It is basically like this:

/!\ '''NOTE: The diagram below is as if you were looking at your computer's parallel port head on. If you are going to solder directly to a male connector, pay close attention to the pin numbers as they will be in a different orientation on the male connector. When looking at the back of the male connector (where you solder wires to) pin 13 is on the far left, while 1 is on the right.'''

{{{
Parport
 1                          13
  o o o o o o o o o o o o o
14 o|o|o|o o o o o o o o o|25
    | | |          |_____||
    | | |             |   |
    ^ ^ ^             |   ^
    1 1 1             |   1
    0 0 0             \___0___
    0 0 0                 0   |
    v v v                 v   |
    | | |_____            |   |
    | |___    |           |   |
    |     |   |           |   |
    |     |   |           |   |
    |     |   |           |   |
 1  |     |   |11         |   |
  o o o o o o |           |   |
      | |_____|           |   |
      |___________________|   |
  o-o-o-o-o-o_________________|
 2            12
JTAG
}}}
Or a more modern version if you prefer:

http://downloads.openwrt.org/inh/reference/JTAGschem.png

''Use the pin numbers on the parallel port connector, and the pin numbers on the WRT pcb, as they are all correct.
Note: Pin 12 is assumed to be grounded.  If it is not grounded on your WRT, you may safely connect the wire indicated on Pin 12 to any grounded even-numbered pin on the WRT's JTAG connector.''

''Oh, and by the way, this cable is a good thing to have anyway, because many embedded devices feature that JTAG-interface e.g. HP's IPAQ has one as well, so if you dare to open it, you can do lots of [http://openwince.sourceforge.net/jtag/iPAQ-3600/ "funky things with your IPAQ"]''

Since the JTAG adaptor gives you full access to your Flash, I wonder if that nasty thing about shorting pins shouldn't be removed altogether.

Note: I had to enable ppdev in the kernel to use the program by hairydairymaid with linux. Working versions of the CFE can be found at [http://downloads.openwrt.org/people/inh/cfe/], information about changing the CFE are available at [http://wiki.openwrt.org/OpenWrtDocs/Customizing].

Note2: I had to disable i2c-parport support in my kernel - because i always got the kernel message "all devices in use" when trying to access the parport.

== Shorting Pins Method ==

If you didn't set boot_wait and don't build a JTAG, you'll have to resort to opening the router and shorting pins on the flash chip to recover.

||4M flash chip (WRT54G v1.0, v1.1, v2.0)||Use pins 15&16||
||4M flash chip (WRT54G v2.2)||Use pins 16&17||
||4M flash chip (Motorola W!R850Gv2)||Use pins 5&6||
||8M flash chip (WRT54GS v1.0, v1.1)||Use pins 5&6||

''' /!\ Be very careful with the flash chip, short only the pins shown in the instructions and do not bend or break any pins; shorting the wrong pins can cause serious damage.'''

Open the router and locate the flash chip, while the router is off use a straight pin or small screwdriver to connect the pins shown and plug in the router. The bootloader will be unable to load the firmware and instead it will run a tftp server on 192.168.1.1 as described above. On a WRT54G/WRT54GS the power led will be flashing (diag led on a WRT54G v1.0) and all other leds will be normal, when you see this led pattern you can stop shorting the pins and tftp a firmware to 192.168.1.1.

See http://voidmain.is-a-geek.net/redhat/wrt54g_revival.html

Note1: With my 1.1 wrt54g device, there was no way to make it work with atftp, tftp or even windows tftp..
I was about to trash the device when I managed to put back linksys official firmware using the short pin and the official uploader tool and then puted back the openwrt using the administration web upgrade tool.. Ouf!

Note2: Observed on a WRT54GS V1.0: it is *sometimes* necessary to hit the reset button **AFTER** having shorted the pins and letting the lights come to their steady-state as mentioned above.  This has been observed multiple times by at least two OpenWRT users, but no obvious pattern has emerged as to why it sometimes works as advertised above, while other times requires the reset button to be hit.  If you're stuck here, it can't hurt to try this.

/!\  The Motorola [:OpenWrtDocs/Hardware/Motorola/WR850G:WR850G] may wait for an image on 192.168.10.1

'''What the hell does shorting the pins do / how do you know what pins?'''

The pins listed are address lines, if you grab the datasheet for any of the flash chips they'll be shown as a0, a1, a2 ...

Each address line represents 1 bit -- Suppose you wanted the 12th byte off the chip, 12 translates to 1100 in binary which means you'd need 4 address lines and they'd be set on or off (voltage, no voltage) depending on if the bit is 1 or 0.

If you short the pins, that changes the address the chip sees as requested. Continuing with the earlier example, suppose of those 4 address lines, the middle two were shorted:

-XX-

The requested address, 1100 gets seen as 1110; a request for address 12 got turned into a request for address 14. Likewise 3 (0011) becomes 7 (0111), 4 (0100) becomes 6 (0110) .. etc.

Result: It's actually impossible to read the value at 12 in this case, and it's likely that address 14 holds a different value. If this were a firmware, the bootloader would attempt to verify the firmware on bootup with a CRC check, mangling the addresses would change the data read and the CRC wouldn't match.

In the end, there's nothing really magical about pins 15-16; you can pick any address lines and short them and ''something'' will happen; if you didn't short the addresses of the bootloader there's a good chance it'll boot up and wait for a firmware. 

= Using the system logs for additional troubleshooting =

Modern versions of OpenWRT use S10boot to start a syslogd.  If a daemon is misbehaving and you can't figure out why use the ''logread'' tool to access the messages sent to syslog.  Often the solution makes itself evident.

= Some routers have screws =

At least Linksys WRT54GS v2.0 and Linksys WAG54G have screws hidden under the two front feet! 

If you're having trouble popping open your router to get at the internals, it's probably because there are screws hidden under the the two front feet in the blue part of the case. DO NOT apply extra force to open these models without checking for the prescence of screws!

Gently use your nails or a flat object to pry all the edges of the front feet up, then simply remove them. The feet are plugs, not just a thin rubber covering, so careful removal will not harm the feet.

From there you will have access to two small Phillips-head screws. Remove and enjoy.

= Problems going from jffs2 to squashfs or from squashfs to jffs2 =

''Important note!  This section assumes you have taken care of backup - follow this procedure without backing up properly first, and your jffs2 files are gone!''

Please use mtd to upgrade your router:
mtd -e linux -r write openwrt-xxx-yyy.trx linux

This will first erase your old system, including your rootfs and then write the new image and reboot your router. If you switch between the different root filesystems, cleaning up old stuff is mandatory, otherwise your router may not boot.

If the damage has already happened, eg. you flashed with an image, and now the router is cycling during boot, you simply flash with whatever your router had before.  (Eg. if you were going from jffs2 to squashfs, you simply flash it with jffs2 again, and the router will boot again).  Now you can follow the above procedure.

Another way to make the change, (for instance, if you don't understand how to do the above), is to log into your router with telnet or ssh. You make sure boot_wait is like you want it, then you erase everything using the command:

mtd -r erase

The router will reboot, and you can flash it with the image you want.

= Problems accessing the wireless interface =

After clearing you nvram and rebooting, the wireless interface has disappeared. In fact, the wl.o kernel module does not load anymore, due to the lack of some nvram variables, and you will find this message in your log :
{{{
eth%d: 3.90.37.0 driver failed with code 23
}}}
If you have a WRT54GS v1.1, you may try to add the following variables :
{{{
wl0id=0x4320 
wl0gpio2=0 
wl0gpio3=0
}}}
and try to load the wl.o module :
{{{
insmod wl.o
}}}

Another way to fix this problem should be to flash a "working" linksys firmware, configure your router and revert to openwrt.

= Source port mismatch with atftp =

If you get 'source port mismatch, check bypassedtimeout: retrying...' error when trying to upload firmware, there is probably something wrong with your arp table. First try clearing it by using 'arp -d 192.168.1.1' and retry. You can check which mac address your computer sees with 'arp -a'. If clearing didn't help, you can also try setting MAC address (under MAC address clone in basic setup) to mac address that your computer sees. Upload should work afterwards. I had this problem with wrt54gs.

= Getting help =
Still stuck? see [http://openwrt.org/support] for information on where to get help.
