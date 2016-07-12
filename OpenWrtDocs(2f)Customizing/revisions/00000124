[[TableOfContents]]
= Disclaimer =
The contents of this section of the wiki can have serious consequences. While every effort has been made to test and verify the items herein, if executed incorrectly, or if you just happen to have a bad day you '''COULD SERIOUSLY DAMAGE YOUR HARDWARE'''. Neither I (inh) nor anyone else will be held responsible for anything you do.


  * [:OpenWrtDocs/Customizing/Hardware/Serial_Console] Howto attach a serial console via usb or parallel port to your wrt
  * [:OpenWrtDocs/Customizing/Hardware/USB] USB is pretty powerfull, read about attaching webcams, harddisks etc via usb
  * [:OpenWrtDocs/Customizing/Hardware/UART] if you know what UART is you may want to read this
  * [:OpenWrtDocs/Customizing/Hardware/MMC] add a multimedia card or sd card to increase your storage volume
  * [:OpenWrtDocs/Customizing/Hardware/GPS] attach an GPS device if using the wrt for wardriving
  * [http://david.zope.nl/hardware/wl500g/wx200wl500g/] Adding a WX200 / WM918 / WMR918 / WMR968 Weather Station
  * [http://www.duff.dk/wrt54gs/pics/reuter_lcd.jpg picture] Adding an LCD 
  * [http://www.duff.dk/wrt54gs/pics/Complete_VGA_Setup.jpg picture] and [http://www.duff.dk/wrt54gs/pics/HW_VGA_Setup.jpg picture] Adding VGA Output
  * [http://yasha.okshtein.net/wrt54g/] How to Mobilize a WRT54g on a RC car
  * [http://www.byteclub.net/wiki/index.php?title=Wrt54g] Adding i2c bus
  * [:OpenWrtDocs/Customizing/Hardware/Power_over_Ethernet] Power Over Ethernet/Power Requirements
  * [http://www.frazer.net.nz/wrting/wrtprojects.htm] WRT Datalogger and Water tank Leve Monitor =
  * [:OpenWrtDocs/Customizing/Hardware/UMTS] Power Over Ethernet/Power Requirements


= Software =
== Things not to compile in ==
When you change things in the configs yourself, only active the following if you realy know what you are doing.

Busybox Configuration - General Configuration - Support NSA Security Enhanced Linux = N

Busybox Configuration - Init Utilities - halt = N

Busybox Configuration - Init Utilities - poweroff = N

Busybox Configuration - Networking Utilities - ifupdown = N


== Software Tools ==
=== Networking ===
||[http://www.hetos.de/bwlog.html WRTbwlog] ||A tool that shows internet traffic on all wired and wireless interfaces, as well as many other useful and related functions ||
||BandwithTestPage ||A simple CGI script for testing the instantaneous bandwidth to the wireless router. Just drop into /www/cgi-bin and chmod+x. ||


=== System ===
=== Wireless ===
||[http://wiviz.natetrue.com WiViz] ||A very nice wireless network visualization tool ||


== Software Guides ==
=== Wireless ===
==== Client Mode ====
See ClientModeHowto

=== System ===
==== LED System Load Monitor ====
Credit goes to SeRi for starting this mod. He had it use the wrt's white and amber LEDs (version 3 only) to show system load. I thought it was a very nifty mod, but I couldn't use it, as the white and amber LEDs are used for the read/write lines on the SD card mod. So what did I do? I modded the mod of course! Now anyone with a spare LED can use this mod. you just need to set the correct GPIO pin. For wrt54g's version 2-3, gpio 7 is for the DMZ LED, which is what I use. You can modify the source accordingly. This will flash the LED once per second under normal useage, twice per second under medium load, and when there is a high load on the system, the LED flashes 3 times per second.'' ''

'''NOTE: You will need to compile your kernel with the Busybox option for usleep enabled. This is what is used for the LED strobing'''

'''Installing Necessary Software'''

First of, grab the [http://downloads.openwrt.org/inh/programs/loadmon.sh loadmon.sh] script, and [mbm]'s [http://downloads.openwrt.org/gpio.tar.gz GPIO tool]. Then untar the gpio tool, and copy the files to your /usr/sbin directory. A typical way to do this on a jffs2 install would go as follows. If you are using squash fs, then you shoudl know what to do.

{{{
cd /tmp
wget http://downloads.openwrt.org/inh/programs/loadmon.sh
wget http://downloads.openwrt.org/gpio.tar.gz
gzip -d gpio.tar.gz
tar xvf gpio.tar
mv gpio /usr/sbin
mv loadmon.sh /usr/sbin
}}}

Now that everything is in place, you need to edit your configuration files to start up the script manually when the router boots. To do this, create a script in /etc/init.d to start loadmon.sh. Here's a simple way to do that:

{{{
echo "#!/bin/sh" > /etc/init.d/S60loadmon
echo "/usr/sbin/loadmon.sh &" >> /etc/init.d/S60loadmon
chmod +x /etc/init.d/S60loadmon
}}}

Now reboot and test it out :)

If you dont want to build your own firmware, and you own a router with the white and orange lights, you can try this script. It will show the white light if load is low, white and orange at medium load, and orange at high load:

{{{
#!/bin/sh

#Set GPIO to the GPIO of the LED you wish to use.
# Default is 7 for DMZ LED on most routers..
GPIOG=2
GPIOR=3
DELAY=2
HIGHLOAD="70"
MEDLOAD="30"

while sleep $DELAY; do
   load=$(cat /proc/loadavg | cut -d " " -f1 | tr -d ".")
   #echo $load

    if [ "$load" -gt "$HIGHLOAD" ]; then
        gpio enable $GPIOG
        gpio disable $GPIOR
    elif [ "$load" -gt "$MEDLOAD" ]; then
        gpio disable $GPIOG
        gpio disable $GPIOR
    else
        gpio disable $GPIOG
        gpio enable $GPIOR
    fi
done
}}}

==== Transparent Firewall ====
See TransparentFirewall

= Firmware =
== Changing CFE defaults ==
The following is a guide from http://wl500g.dyndns.org/wrt54g.html that I've copied here, with added commentary. I am not the original author, that credit goes to Oleg.'' ''

Copyright (c) 2005 Oleg I. Vdovikin IMPORTANT: This information provided AS IS, without any warranties. If in doubt leave this page now. This information applies to WRT54G hw rev 2.0, 2.2, 3.0. No other units were tested, but most likely WRT54GS units should be the same. WRT54G hw rev 1.x use different layout, so you need to adjust things accordingly.

The wrt54g v.2.2 unit was kindly donated to me by maxx, the member of the forum.chupa.nl forum. I would like to publically say thank you to him.

'''Extracting default values'''

Telnet/ssh to your router running your favorite firmware and type the following

{{{
dd if=/dev/mtdblock/0 bs=1 skip=4116 count=2048 | strings > /tmp/cfe.txt
dd if=/dev/mtdblock/0 of=/tmp/cfe.bin
}}}

Copy both cfe.bin and cfe.txt to your linux box (this is required).

To copy files from your router to your computer, make sure the Dropbear package is installed, and type:

{{{
scp root@<router ip>:/tmp/cfe.bin /directory/on/your/computer
scp root@<router ip>:/tmp/cfe.txt /directory/on/your/computer
}}}

''Check cfe.txt, it should look like this (this is from v.2.2): ''

{{{
boardtype=0x0708
boardnum=42
boardrev=0x10
boardflags=0x0118
boardflags2=0
sromrev=2
clkfreq=200
sdram_init=0x000b
sdram_config=0x0062
sdram_refresh=0x0000
sdram_ncdl=0x0
et0macaddr=00:90:4C:00:00:00
et0phyaddr=30
et0mdcport=0
gpio5=robo_reset
vlan0ports=1 2 3 4 5*
vlan0hwname=et0
vlan1ports=0 5
vlan1hwname=et0
wl0id=0x4320
il0macaddr=00:90:4C:00:00:00
aa0=3
ag0=255
pa0maxpwr=0x4e
pa0itssit=62
pa0b0=0x15eb
pa0b1=0xfa82
pa0b2=0xfe66
wl0gpio2=0
wl0gpio3=0
cctl=0
ccode=0
dl_ram_addr=a0001000
os_ram_addr=80001000
os_flash_addr=bfc40000
lan_ipaddr=192.168.1.1
lan_netmask=255.255.255.0
scratch=a0180000
boot_wait=off
watchdog=5000
bootnv_ver=2
}}}

'''Changing defaults'''

Open cfe.txt using text editor and change defaults in the way you like (but be extremely careful, as some changes could prevent device from booting and you will need to use JTAG cable to bring it back to life). For me I've decided to enable both Afterburner (Speedbooster) and set boot_wait to on by default, so reset to default no longer messes the things, so I've applied this pseudo-patch (please note, that I've added bit 0x200 to boardflags to enable afterburner):

{{{
-boardflags=0x0118
-boot_wait=off
+boardflags=0x0318
+boot_wait=on
}}}

To make life easier for me, I added "reset_gpio=6" to the cfe.txt file. This way, if I do set something wrong, like clkfreq, and the router just locks up, I wont have to try over and over again to hit a very slim window with the JTAG to erase the nvram. I can just hold reset when the router powers on, and it will use the default nvram values stored in the cfe.'' ''

If you do not understand some things in this file, do not try to edit it. This is also applies to afterburner. I've also tried to change default lan_ipaddr, but this does not work in the way I expect: CFE started to answer to ping request to new lan_ipaddr, but it does not accept tftp transfers...

'''Creating new CFE image'''

You will need a nvserial utility which comes with several GPL tarballs. Linksys supplies it in the wrt54g.1.42.3, wrt54g.1.42.2, wap55ag.1.07, wap54gv2.2.06. Launch nvserial in the way like this on your x86 linux box: You can get nvserial from http://downloads.openwrt.org/people/inh/programs/nvserial'' ''

{{{
nvserial -i cfe.bin -o cfe_new.bin -b 4096 -c 2048 cfe.txt
}}}

It works really slow, but it should finally create cfe_new.bin file for you, which has new embedded nvram.

'''Recompiling kernel with writable pmon partition'''

By default most firmwares has pmon partition write protected, i.e. you can't flash anything to this first 256k of flash. This is to prevent corrupting PMON/CFE. To remove this "lock" you will need to compile your own firmare with the following patch, you will need to copy the patch into "target/linux/linux-2.4/patches/brcm". (This patch works with WHITERUSSIAN RC3)

{{{
--- linux-2.4.30/arch/mips/bcm947xx/setup.c.orig        2005-09-21 11:24:09.000000000 -0400
+++ linux-2.4.30/arch/mips/bcm947xx/setup.c     2005-09-21 13:48:46.853425632 -0400
@@ -174,7 +174,7 @@
 #ifdef CONFIG_MTD_PARTITIONS

 static struct mtd_partition bcm947xx_parts[] = {
-       { name: "pmon", offset: 0, size: 0, mask_flags: MTD_WRITEABLE, },
+       { name: "pmon", offset: 0, size: 0 /*, mask_flags: MTD_WRITEABLE,*/ },
        { name: "linux", offset: 0, size: 0, },
        { name: "rootfs", offset: 0, size: 0, },
        { name: "nvram", offset: 0, size: 0, },
}}}

'''Flashing new CFE image'''

So, once you've recompiled and flashed your new firmware you need you upgrade CFE. This process is dangerous, as flash failure during it will prevent your unit from booting. Copy cfe_new.bin to your wrt54g and flash it. The exact commands are dependent on the firmware. With OpenWrt I've used the following:

{{{
mtd unlock pmon
mtd write -f /tmp/cfe_new.bin pmon
}}}

I recommend using the JTAG cable method for re-flashing your CFE. If something were to go wrong, you would end up needing the JTAG cable anyways. It's really cheap and easy to build, and makes it possible to recover from almost any error you make when writing to the flash. Check out http://openwrt.org/OpenWrtDocs/Troubleshooting '''' '''

Checking it''' '''

Embedded nvram is only used, when real nvram is either corrupted or empty (CRC/magic checks fails), so you will need to erase nvram or to reset to defaults. With OpenWrt type this:

{{{
mtd erase nvram
}}}

Then cross your fingers and reboot your unit. And remember - I'm not responsible for any damage to your unit, as this information is provided AS IS for my own pleasure. oleg@cs.msu.su Posted: 2005-04-03

== Customizing Firmware Image ==
It is relatively easy to create a custom firmware image which is pre-loaded with particular software packages and your own files. Please use the !OpenWrt [:ImageBuilderHowTo:Image Builder].

----
 . CategoryHowTo CategoryHowTo      
