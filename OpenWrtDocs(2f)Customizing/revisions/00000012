[:OpenWrtDocs]
[[TableOfContents]]
= Disclaimer =
The contents of this section of the wiki can have serious consequences. While every effory has been made to test and verify the items herin, if executed incorrectly, or if you just happen to have a bad daym you COULD SERIOUSLY DAMAGE YOUR HARDWARE. I (inh) nor anyone else, will be help responsible for anything you do.

= Hardware =
== Adding Dual Serial Ports ==
''Serial ports allow you to do a myriad of things, inlcuding connect to your computer, connect to other deviced such as LCDs and GPSes, etc... With a lil programming, you could even connect a bunch of routers together.. This mod doesn't *add* serial ports.. those are already there.. this just makes them much easier to use with just about any hardware you want''

== Adding an MMC/SD Card ==
*Mod already done. Will update soon*
== Adding an LCD ==
*Awaiting hardware for writeup*
== Adding a GPS ==
*Almost done

== Adding a Weather Station ==
== Adding an LCD ==
[http://www.duff.dk/wrt54gs/pics/reuter_lcd.jpg]
== Adding VGA Output ==
[http://www.duff.dk/wrt54gs/pics/Complete_VGA_Setup.jpg]
[http://www.duff.dk/wrt54gs/pics/HW_VGA_Setup.jpg]
== Adding Secod Reset Button (v2.2 only) ==
[http://www.duff.dk/wrt54gs/pics/02_Covox_Top.jpg]
== Adding Sound Output ==
[http://www.duff.dk/wrt54gs/pics/07_Finished_product.jpg]

= Software =
= Firmware =
== Overclocking ==
''Overclocking the WRT has been a very sought-after mod. Many people overclock thier home PCs, and now I will tell you how to overclock your OpenWrt router. ''

'''Background Info'''

Many people know that by setting the nvram variable clkfreq, you can overclock your router. Many people also know that Linksys actually released a beta firmware, changing clkfreq to 216 to fix stability issues. That quick fix actually works quite well, as many people can tell you. Linksys also released a lesser-known beta firmware that set clkfreq to 240. This also well. But there are a few lesser known, and as far as I know, a few things discovered by [mbm] and I. First off, you can NOT set clkfreq to any number you want. It is very selective, and only certain values work. Also, there are 2 clocks you can adjust. This was previously unknown (read: another OpenWrt first.)

'''Simple Overclocking'''

As stated earlier, Linksys released firmware that made thier routers run at 216 mHz instead of 200 to fix stability issues. You too can do this simple overclock to make your router run much more solidly. Here is all you have to do.

At the OpenWrt prompt, type:
{{{
nvram set clkfreq=216
nvram commit
}}}

Thats it! Reboot your router by either unplugging it and plugging it back in, or by typing:
{{{
reboot
}}}
Simple enough! If your router was unstable with high traffic loads before, you should be much more stable now :)

'''Moderate Overclocking'''

While a 16mHz increase doesnt seem like much, it works wonders for the router. But what if you want to go faster? Setting clkfreq to 220 locks up the router, and then you are stuck with having to use the JTAG method to de-brick. That is, of course,  assuming you didnt change the default values in the CFE file, in which case all you have to do is reboot with the reset button held in... see the 'changing cfe defaults' guide)

Anyways, back on topic.. More speed! 
The trick with making it run faster is setting the right clkfreq values. The wrong ones turn your router into a brick. Here is a list of values that are known to work: 192,200,216,228,240,252,264,272,280,288,300

I've personally tested all of them on my wrt54g version 3, and they all worked. There is one caveat howerver; values above 264 seem to have no change. By checking the cpuinfo, it still reports the BogoMIPS as 264, even if clkfreq is set above that. To check your cpuinfo, type:
{{{
cat /proc/cpuinfo
}}}

Try the values, test your performance, or just bask in all your overclocking glory :)

'''Advanced Overclocking'''

This is the good stuff, especially if you have done the MMC/SD card mod, as it boosts the read/write speeds from 200 kilobytes a second to over 330 :D

In addition to setting clkfreq to a higher number, there is also another clock that can be controlled. This is called the sb clock, and is beleived to be the clock that controlls the speed of the data transfer between different areas of the Broadcom CPU. To set it, you set clkfreq like this:
{{{
nvram set clkfreq=MIPSclock,SBclock
}}}

For example, the following does the same as if you were to set clkfreq to 264:
{{{
nvram set clkfreq=264,132
}}}

MIPSclock is the standard clock you change when setting clkfreq with one value. The second number you set it to is the aformentioned SBclock. The SBclock, just like the MIPSclock, only has certain values that can be used, or it will brick your router. Here's a table:

||MIPSclock||||SBclock||
||||||||
||192||||96||
||200||||100||
||216||||108||
||228||||101333333||
||228||||114||
||240||||120||
||252||||126||
||264||||132||
||272||||116571428||
||280||||120||
||288||||123428571||
||300||||120||

Those are all values known to work. You can either set just the MIPSclock by using that value, or set both MIPS and SB clocks by using:
{{{
nvram set clkfreq=MIPSclock,sbclock
}}}

You can also mix and match values. I've personally found that setting MIPSclock to 300 and SBclock to 96, I get much better performance.

'''Conclusion'''

The clock seems to still remain somewhat of a mystery. With the recently discovered SBclock, and table of useable values, overclocking is a much more feasible and safe mod than it used to be. 

'''Troubleshooting'''

Setting an invalid clkfreq value can have a very undesireable effect: complete router lockup, aka 'bricking.' Normally bricking isn't that bad of a thing. YOu can simply use the [http://openwrt.org/OpenWrtDocs/Troubleshooting#head-d1e14acb3488c8f4b91727d72dce9f59583f9d65 JTAG method] to de-brick. When setting clkfreq values, however, you must take extra care. If you set an invalid window, you have a VERY VERY small time frame to get the jtag to erase the nvram before the CPU locks up. Rough estimates give a window of 1/2 second. If you have ever had to do this, it is a very big annoyance. A better solution is to add the nvram value reset_gpio to the default nvram stored in the cfe. By setting the right value to reset_gpio, and flashing the modified cfe back on to your router, if you do set a wrong clkfreq value, all you have to do is reset with the reset button held in, and everything will reset back to defaults. Details on  this method can be found [http://openwrt.org/OpenWrtDocs/Customizing#head-50e9ee3f70e5d5229aeade4c624b965b24de5967 here].

== Changing CFE defaults ==
''The following is a guide from http://wl500g.dyndns.org/wrt54g.html that I've copied here, with added commentary. I am not the original author, that credit goes to Oleg.''

Copyright (c) 2005 Oleg I. Vdovikin
IMPORTANT: This information provided AS IS, without any warranties. If in doubt leave this page now. This information applies to WRT54G hw rev 2.0, 2.2, 3.0. No other units were tested, but most likely WRT54GS units should be the same. WRT54G hw rev 1.x use different layout, so you need to adjust things accordingly.

The wrt54g v.2.2 unit was kindly donated to me by maxx, the member of the forum.chupa.nl forum. I would like to publically say thank you to him.

'''Extracting default values'''

Telnet/ssh to your router running your favorite firmware and type the following
{{{
dd if=/dev/mtdblock/0 bs=1 skip=4116 count=2048 | strings > /tmp/cfe.txt
dd if=/dev/mtdblock/0 of=/tmp/cfe.bin
}}}

Copy both cfe.bin and cfe.txt to your linux box (this is required).

''To copy files from your router to your computer, make sure the Dropbear package is installed, and type:
{{{
scp root@<router ip>:/tmp/cfe.bin /directory/on/your/computer
scp root@<router ip>:/tmp/cfe.txt /directory/on/your/computer
}}}
''
Check cfe.txt, it should look like this (this is from v.2.2):
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

Open cfe.txt using text editor and change defaults in the way you like (but be extremelly careful, as some changes could prevent device from booting and you will need to use JTAG cable to bring it back to life). For me I've decided to enable both Afterburner (Speedbooster) and set boot_wait to on by default, so reset to default no longer messes the things, so I've applied this pseudo-patch (please note, that I've added bit 0x200 to boardflags to enable afterburner):
{{{
-boardflags=0x0118
-boot_wait=off
+boardflags=0x0318
+boot_wait=on
}}}

''To make life easier for me, I added "reset_gpio=6" to the cfe.txt file. This way, if I do set something wrong, like clkfreq, and the router just locks up, I wont have to try over and over again to hit a very slim window with the JTAG to erase the nvram. I can just hold reset when the router powers on, and it will use teh default nvram values stored in the cfe.''

If you do not understand some things in this file, do not try to edit it. This is also applies to afterburner. I've also tried to change default lan_ipaddr, but this does not work in the way I expect: CFE started to answer to ping request to new lan_ipaddr, but it does not accept tftp transfers...

'''Creating new CFE image'''

You will need a nvserial utility which comes with several GPL tarballs. Linksys supplies it in the wrt54g.1.42.3, wrt54g.1.42.2, wap55ag.1.07, wap54gv2.2.06. Launch nvserial in the way like this on your x86 linux box:
''You can get nvserial from http://downloads.openwrt.org/inh/nvserial''
{{{
nvserial -i cfe.bin -o cfe_new.bin -b 4096 -c 2048 cfe.txt
}}}
It works really slow, but it should finally create cfe_new.bin file for you, which has new embedded nvram.

'''Recompiling kernel with writable pmon partition'''

By default most firmwares has pmon partition write protected, i.e. you can't flash anything to this first 256k of flash. This is to prevent corrupting PMON/CFE. To remove this "lock" you will need to apply this patch to the kernel and recompile your firmware:
{{{
--- linux/arch/mips/brcm-boards/bcm947xx/setup.c.orig   2005-01-23 19:29:05.000000000 +0300
+++ linux/arch/mips/brcm-boards/bcm947xx/setup.c        2005-03-26 15:13:33.000000000 +0300
@@ -179,7 +179,7 @@
 #ifdef CONFIG_MTD_PARTITIONS

 static struct mtd_partition bcm947xx_parts[] = {
-       { name: "pmon", offset: 0, size: 0, mask_flags: MTD_WRITEABLE, },
+       { name: "pmon", offset: 0, size: 0 /*, mask_flags: MTD_WRITEABLE,*/ },
        { name: "linux", offset: 0, size: 0, },
        { name: "rootfs", offset: 0, size: 0, mask_flags: MTD_WRITEABLE, },
        { name: "nvram", offset: 0, size: 0, },
}}}

'''Flashing new CFE image'''

So, once you've recompiled and flashed your new firmware you need yo upgrade CFE. This process is dangerous, as flash failure during it will prevent your unit from booting. Copy cfe_new.bin to your wrt54g and flash it. The exact commands are dependent on the firmware. With OpenWrt I've used the folowing:

{{{
mtd unlock pmon
mtd write /tmp/cfe_new.bin pmon
}}}

''I recommend using the JTAG cable method for reflashing your CFE. If somethign were to go wrong, you would end up needing the JTAG cable anyways. It's really cheap and easy to build, and makes it possible to recover from almost any error you make when writing to the flash. Check out http://openwrt.org/OpenWrtDocs/Troubleshooting ''

'''Checking it'''

Embedded nvram is only used, when real nvram is either corrupted or empty (CRC/magic checks fails), so you will need to erase nvram or to reset to defaults. With OpenWrt type this:
{{{
mtd erase nvram
}}}
Then cross your fingers and reboot your unit. And remember - I'm not responsible for any damage to your unit, as this information is provided AS IS for my own pleasure. oleg@cs.msu.su
Posted: 2005-04-03

= Downloads =
== Programs ==

Nvserial - Utility to build modified CFE images - http://downloads.openwrt.org/inh/nvserial
== Firmware images, CFE images, etc... ==
'''Please see the [http://downloads.openwrt.org/inh/cfe/README README] file regarding MAC addresses'''

=== Linksys wrt54gs v1.0 ===
||[http://downloads.openwrt.org/inh/cfe/cfe.bin-gs1.0 Stock CFE.bin]||Standard CFE that ships with the v1.0||
||[http://downloads.openwrt.org/inh/cfe/cfe.bin-gs1.0.Modified CFE.bin]||boot_wait enabled by default in the cfe nvram||
||[http://downloads.openwrt.org/inh/cfe/cfe.txt-gs1.0 Modified CFE NVRAM values]||The nvram values used in the modified cfe.bin||
=== Linksys wrt54gs v1.1 ===
||[http://downloads.openwrt.org/inh/cfe/cfe.bin-gs1.1 Stock CFE.bin]||Standard CFE that ships with the v1.1||
||[http://downloads.openwrt.org/inh/cfe/cfe.bin-gs1.1.Modified CFE.bin]||boot_wait enabled by default in the cfe nvram||
||[http://downloads.openwrt.org/inh/cfe/cfe.txt-gs1.1 Modified CFE NVRAM values]||The nvram values used in the modified cfe.bin||
=== Linksys wrt54g v2.2 and v3 ===
||[http://downloads.openwrt.org/inh/cfe/cfe.bin-g3.0 Stock CFE.bin]||Standard CFE that ships with the v2.2 and 3||
||[http://downloads.openwrt.org/inh/cfe/cfe.bin-g3.0 Modified CFE.bin]||boot_wait enabled, and will load nvram values stored in the cfe if reset is held while rebooting||
||[http://downloads.openwrt.org/inh/cfe/cfe.txt-g3.0 Modified CFE NVRAM values]||The nvram values used in the modified cfe.bin||
=== Linksys wrt54gx v1.0 ===
||[http://downloads.openwrt.org/inh/cfe/cfe.bin-gx1.0 Stock CFE.bin]||Standard CFE that ships with the v1.0 (compressed)||
||[http://downloads.openwrt.org/inh/cfe/cfe.bin-gx1.0 Decompressed Stock CFE.bin]||Standard CFE that ships with the v1.0 (de-compressed)||

Modified cfe.txt file accompanying the above .bin file - http://downloads.openwrt.org/inh/cfe.txt
