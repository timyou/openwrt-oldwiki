= Airlink AR335W/AR430W WIP =

Those two routers have almost identical hardware. Both are based on an Atheros System on Chip (SoC) and both have limited Redboot. 


[[ImageLink(AR335W,width=width[,height=height]])]]

= Hardware =
== Info ==
||<tablewidth="460px" tableheight="345px">'''Architecture''' ||MIPS 5KEc ? ||
||'''Vendor''' || ||
||'''Bootloader''' ||!RedBoot ||
||'''System-On-Chip''' ||Atheros AR2317/AR2318 ||
||'''CPU Speed''' ||182 MHz ||
||'''Flash size''' ||4 MB ||
||'''RAM''' ||16 MB ||
||'''Switch''' ||IC+ IP175C||
||'''Wireless''' ||Integrated Atheros 802.11b/g (*also Atheros™ Super G™: 108 Mbps on AR430W) ||
||'''Ethernet''' ||5x RJ45 (1x Wan , 4x Lan)||
||'''USB''' ||No ||
||'''Serial''' ||Yes ||
||'''JTAG''' ||No ||
 * 5V power supply
 * Antenna

= Installing Modified Redboot =
This is a copy-paste from DD-WRT website. You can download files you need from this page. http://www.dd-wrt.com/dd-wrtv2/down.php?path=downloads%2Fv24%2FAtheros+WiSoc%2FAirlink+101+AR430W/

Configure your local ip to 192.168.20.80
plugoff the power cord and replug it
now enter the redboot using telnet and ip 192.168.20.81 and port 9000. conside to connect your lan cable on the wan port. You might need several tries since its only available for 1 second after aprox. 5 sec. of booting.


IP: 192.168.20.81/255.255.255.0, Gateway: 0.0.0.0
Default server: 192.168.20.80


Now start a local tftp server on your computer and place ap61.ram as well as ap61.rom in the root dir of this server

Back to the redboot enter:
'''load ap61.ram'''
'''go'''

Now a new temporarily bootloader should start. It will display some warning. but you dont need to care about

Important! while doing the following steps. never plugoff the lan cable or the power cord
now type
Redboot> '''fconfig -i'''
for now use all settings from default and save the config finally


Redboot> '''fconfig bootp false'''
{{{
bootp: Setting to false
Update RedBoot non-volatile configuration - continue (y/n)? y
... Erase from 0xbffe0000-0xbfff0000: .
... Program from 0x80ff0000-0x81000000 at 0xbffe0000: .
}}}

Warning this step will erase firmware on your router!

Redboot> '''fis init'''
{{{
About to initialize [format] FLASH image system - continue (y/n)? y
*** Initialize FLASH Image System
... Erase from 0xbffe0000-0xbfff0000: .
... Program from 0x807f0000-0x80800000 at 0xbffe0000: .
}}}

Redboot> '''ip_address -l 192.168.20.81 -h 192.168.20.80'''
{{{
IP: 192.168.20.81/255.255.255.0, Gateway: 0.0.0.0
Default server: 192.168.20.80
}}}

Redboot> '''load -r -b %{FREEMEMLO} ap61.rom'''
{{{
Using default protocol (TFTP)
Raw file loaded 0x80080000-0x800a8717, assumed entry at 0x80080000
}}}

Redboot> '''fis create -l 0x30000 -e 0xbfc00000 RedBoot'''
{{{
An image named 'RedBoot' exists - continue (y/n)? y
... Erase from 0xbfc00000-0xbfc30000: ...
... Program from 0x80080000-0x800a8718 at 0xbfc00000: ...
... Erase from 0xbffe0000-0xbfff0000: .
... Program from 0x807f0000-0x80800000 at 0xbffe0000: .
}}}

Redboot> '''reset'''

'''You will need to change your static ip address to 192.168.1.23, because your router is now reachable at 192.168.1.1 port 9000'''

= Installing OpenWrt with RedBoot =
'''You will need to flash modified Redboot before you continue.'''

Once you have gained access to [:RedBoot:!RedBoot] either by telnet or the serial console you can install [:OpenWrt:!OpenWrt] with the following method.

You have to download two files (right click and save as).

 * [http://downloads.openwrt.org/kamikaze/7.09/atheros-2.6/openwrt-atheros-2.6-vmlinux.lzma openwrt-atheros-2.6-vmlinux.lzma]
 * [http://downloads.openwrt.org/kamikaze/7.09/atheros-2.6/openwrt-atheros-2.6-root.squashfs openwrt-atheros-2.6-root.squashfs]
Copy openwrt-atheros-2.6-vmlinux.lzma and openwrt-atheros-2.6-root.squashfs to /tftpboot/ and flash them like this:

{{{
^C
DD-WRT> load -r -b %{FREEMEMLO} openwrt-atheros-2.6-vmlinux.lzma
Using default protocol (TFTP)
Raw file loaded 0x80041000-0x800f0fff, assumed entry at 0x80041000
DD-WRT> fis init}}}
The values for the -e and -r switches in the 'fis create' !RedBoot command below is the Kernel entry point. Do not change this value.

{{{
RedBoot> fis create -e 0x80041000 -r 0x80041000 vmlinux.bin.l7
An image named 'vmlinux.bin.l7' exists - continue (y/n)? y
... Erase from 0xa8730000-0xa87e0000: ...........
... Program from 0x80041000-0x800f1000 at 0xa8730000: ...........
... Erase from 0xa87e0000-0xa87f0000: .
... Program from 0x80ff0000-0x81000000 at 0xa87e0000: .
}}}
"fis free" will print the first and last free block

{{{
DD-WRT> fis free
      0xA80F0000 .. 0xA87E0000
}}}
Now do the math (last - first, cause you need the difference)

{{{
server:~# bc
obase=16
ibase=16
A87E0000 - A80F0000
6F0000
}}}
Replace ''0xLENGTH'' with the value above (0x006F0000 in my case '''It's very important that you calculate value for your router, DO NOT TRY TO USE 0x006F0000, It will brick your router!''') and flash the the rootfs:

{{{
DD-WRT> load -r -b %{FREEMEMLO} openwrt-atheros-2.6-root.squashfs
Using default protocol (TFTP)
|
Raw file loaded 0x80041000-0x80200fff, assumed entry at 0x80041000
RedBoot> fis create -l 0xLENGTH rootfs
An image named 'rootfs' exists - continue (y/n)? y
... Erase from 0xa8030000-0xa8730000: ................................................................................................................
... Program from 0x80041000-0x80741000 at 0xa8030000: ..............................................................................................................
... Erase from 0xa87e0000-0xa87f0000: .
... Program from 0x80ff0000-0x81000000 at 0xa87e0000: .

now type '''fconfig''' and configure the bootscript to
Run script at boot: true 
Enter script, terminate with empty line 
>> fis load -l vmlinux.bin.l7
>> exec 
>><--- just press enter 
Boot script timeout (1000ms resolution): 5 
Use BOOTP for network configuration: false <--- just press enter 
Gateway IP address: <--- just press enter 
Local IP address: 192.168.1.1
Local IP address mask: 255.255.255.0 
Default server IP address: 192.168.1.254 
Console baud rate: 9600 
GDB connection port: 9000 
Force console for special debug messages: false  <--- just press enter 
Network debug at boot time: false  <--- just press enter 
Update RedBoot non-volatile configuration - continue (y/n)? y 
... Erase from 0xbffe0000-0xbfff0000: . 
... Program from 0x80ff0000-0x81000000 at 0xbffe0000: . 
DD-WRT>reset

}}}

If you did everything correctly then you should be able to telnet your router after it reboots.

= Using wireless =
Many users have had the wireless driver hang the AR430w with Kamikaze 7.09.

However, if you build entirely from trunk, with one small modification to the configuration, the wireless should work:

I have successfully gotten this router to work with almost stock openwrt trunk (I have used rev 12634).  The only necessary change in order to prevent a hung router upon boot is to modify the kernel config and turn off all the GPIO options.  From there it's just a "make" and then flashing it like above, but with the rootfs.squashfs and the kernel copied out of the "bin" directory once you are done:
{{{
Index: target/linux/atheros/config-2.6.26
===================================================================
--- target/linux/atheros/config-2.6.26  (revision 12634)
+++ target/linux/atheros/config-2.6.26  (working copy)
@@ -63,9 +63,9 @@
 CONFIG_GENERIC_CMOS_UPDATE=y
 # CONFIG_GENERIC_FIND_FIRST_BIT is not set
 CONFIG_GENERIC_FIND_NEXT_BIT=y
-CONFIG_GENERIC_GPIO=y
+# CONFIG_GENERIC_GPIO is not set
 # CONFIG_GENERIC_HARDIRQS_NO__DO_IRQ is not set
-CONFIG_GPIO_DEVICE=y
+# CONFIG_GPIO_DEVICE is not set
 CONFIG_HAS_DMA=y
 CONFIG_HAS_IOMEM=y
 CONFIG_HAS_IOPORT=y
@@ -92,7 +92,7 @@
 CONFIG_IRQ_CPU=y
 # CONFIG_IWLWIFI_LEDS is not set
 # CONFIG_LEDS_ALIX is not set
-CONFIG_LEDS_GPIO=y
+# CONFIG_LEDS_GPIO is not set
 # CONFIG_LEMOTE_FULONG is not set
 CONFIG_LZO_COMPRESS=m
 CONFIG_LZO_DECOMPRESS=m
}}}

The wireless does not seem to start configured upon boot.
To enable the wireless for testing from the command line, run:
{{{
wlanconfig ath0 create wlandev wifi0 wlanmode ap
ifconfig ath0 up
iwconfig ath0 essid "myaccesspoint"
}}}
and check that another computer can see the access point.

 . Category80211gDevices
 . CategorySupportedInKamikaze7_07
