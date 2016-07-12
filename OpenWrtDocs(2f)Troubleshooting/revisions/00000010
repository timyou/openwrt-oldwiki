#acl Known:read,write All:read
##
## Note: these pages document the firmware itself, not packages
##       questions/comments should be posted to the forum
##
[:OpenWrtDocs]
[[TableOfContents]]
= Recovering from bad firmware (Alternate Software-based Method) =
Since shorting pins can be dangerous this method has been recommended:
 1. Disconnect your brick from everything
 1. Connect your PC to one of the LAN-Ports
 1. Setup your NIC to 10baseT-HD
    in Linux you can do this using the mii-tool:
    {{{
mii-tool -R -F 10baseT-HD eth0 }}}
 1. Set your NIC to 192.168.1.50
    Linux:
    {{{
ifconfig eth0 192.168.1.50 up }}}
 1. Connect power to your ''brick'' and press the Reset for 30 secs
 1. Ping to 192.168.1.1
 1. The power/diag light should blink if this worked.
The '''great''' advantage is that you don't have fool about with that warranty sticker.
[http://www.linksys.com/support/top10faqs/wrt54g/Red%20Diag%20or%20Power%20Light%20Blinking%20on%20the%20WRT54G.asp "Linksys support page"]

= Using a JTAG-adaptor =

You still don't want to short any pins on your precious router. Thats nasty disgusting behaviour. A lot better way to get a Flash into your wrecked piece of hardware, is to build your own JTAG-adaptor. It's easy and if you were me doesn't cost a jiffy because you already have this stuff floating around anyway. You need:
 1. 4 100R resistors
 1. 1 male SUB-D 25 plug
 1. If you want to do it right, a 12-way IDC-Connector plug (these are the ones who look like the HDD-Cables)
 1. A 12-way ribbon cable for above
 1. The girlfrind of that IDC-Connector for the PCB
 1. This [http://spacetoad.com/tmp/hairydairymaid_debrickv22.zip "zip-file"] with a utitlty and instructions how to connect everything together.
 1. A little bit of luck

It seems to me though that the GS variant has a different location of the flash. The size certainly differs ;-) you have to modify the source to this respect, or you have to wait till I have found out where this damn flash resides. I'll tell you as soon as i know more.


= Recovering from bad flash (Shorting Pins Method) =

If you've followed the instructions and warnings you should have boot_wait set to on. With boot_wait on, each time the router boots you will have roughly 3 seconds to send a new firmware using tftp. Use a standard tftp client to send the firmware in binary mode to 192.168.1.1. Due to limitations in the bootloader, this firmware will have to be under 3MB in size.

If you didn't set boot_wait, you'll have to open the router and short pins on the flash chip to recover.

||4M flash chip (WRT54G v1.0, v1.1, v2.0, v2.2?)||Use pins 15&16||
||8M flash chip (WRT54GS v1.0, v1.1)||Use pins 5&6||

/!\ Be very careful with the flash chip, short only the pins shown in the instructions and do not bend or break any pins

Open the router and locate the flash chip, while the router is off use a straight pin or small screwdriver to connect the pins shown and plug in the router. The bootloader will be unable to load the firmware and instead it will run a tftp server on 192.168.1.1 as described above. On a WRT54G/WRT54GS the power led will be flashing (diag led on a WRT54G v1.0) and all other leds will be normal, when you see this led pattern you can stop shorting the pins and tftp a firmware to 192.168.1.1.

= Fixing a broken script / Failsafe mode =
If you've broken one of the startup scripts, firewalled yourself or corrupted the jffs2 partition, you can get back in by using OpenWrt's failsafe mode. To get into failsafe, plug in the router and wait for the DMZ led to light then immediately press and hold the reset button for 2 seconds. If done right the DMZ led will quickly flash 3 times every second.

( /!\  holding the reset button before the DMZ led can reset NVRAM, see the NVRAM section below )


When in failsafe, the system will boot using only the files contained within the firmware (the squashfs partition) ignoring any changes made to the jffs2 partition. Additionally, various network settings will be overridden forcing the router to 192.168.1.1.

If you want to completely erase the jffs2 partition, removing all packages you can run firstboot.

If you want to attempt to fix the jffs2 partition, mount it with the following commands:
{{{
mtd unlock /dev/mtd/4
mount -t jffs2 /dev/mtdblock/4 /jffs
}}}
After the partition is mounted, you can edit the files in /jffs. If you run firstboot with the jffs2 partition mounted, it will not format the partition, but it will overwrite files with symlinks. (Packages will be preserved, changes to scripts will be lost)

= Fixing NVRAM =
If you've broken NVRAM, first try the failsafe routine described above; once in failsafe you can just use the nvram utility to alter the nvram settings. If you want to fully reset NVRAM, you can use the command "mtd erase nvram".

If you can't get in using failsafe you will have to erase NVRAM.

On the WRT54G v2.x or WRT54GS models, you can easily reset NVRAM by holding down the reset button while plugging in the router. If this does not work, try the method for WRT54G v1.x models.

On WRT54G v1.x models the process is much more difficult. Open the router and locate pins 2&3 on the flash chip -- Do not short them yet. Plug in the router, wait for all the switch ports to light up, when the ports are lit up, short pins 2&3 of the flash.

When the NVRAM is erased, all variables will be lost and only a few variables required for bootup will be created.

/!\ After NVRAM is erased, boot_wait will be OFF and should be turned back ON.

= WRT54G v2.2 / WRT54g v1.1 : Can't downgrade to this old firmware version =
See http://openwrt.org/forum/viewtopic.php?t=809
