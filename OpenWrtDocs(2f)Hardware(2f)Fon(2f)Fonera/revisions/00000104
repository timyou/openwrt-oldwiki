#pragma section-numbers off
||<tablebgcolor="#f1f1ed" tablewidth="40%" tablestyle="margin: 0pt 0pt 1em 1em; float: right; font-size: 0.9em;"style="padding: 0.5em;">[[TableOfContents]]||
= Fonera =
The Fonera FON2100A is based on an Atheros System on Chip (SoC). It got a MIPS 4KEc V6.4 processor. There is an ongoing process porting !OpenWrt to this chip: AtherosPort.

It's almost identical to the [http://meraki.net/mini.html Meraki Mini], who provide their own [http://www.meraki.net/linux/ OpenWrt fork].

== Additional Comments ==
Detailed Information may be found in the FCC database: Doing a search on Fonera's FCC-ID reveals, that this device is actually made by Accton/SMC (http://www.accton.com.tw/).

A look at the varius test reports and external photos shows, that this device is provided also under the Trade(Model) Names

 * ACCTON MR3201A
 * FON FON2100A,B,C and F
 * Edge-Core WA3101
 * Philips SNR6500
 * SMC WEBT-G
 * Siemens Gigaset Wlan repeater 108
Copies of the mentioned FCC-documents may also be found at http://mobileaccess.de/fonera/

According to !OpenWrt, the output-power is set to 18dBm, in contrast to the FCC-RF-tests where an output power of almost 25dBm (actually 24.89dBm on channel 6 in 802.11g mode) is measured. Question here is, if further versions will provide an adjustable TX-Power up to that level. Is the information provided by !OpenWrt of 18dBm just a hypothetical value??? I found no reference in Kamikaze yet, how to adjust it.

Another interessting issue is the possible frequency range, as specified by Atheros itself at http://www.atheros.com/pt/bulletins/AR5006AP_GBulletin.pdf - where the available band ranges from 2.300GHz to 2.500GHz. Question here is, if there will be an option to use further frequencies than the international standardized 14 Channels. In particular, there might be a very high interest e.g. from the amateur-radio community!

= Hardware =
== Info ==
||<tablewidth="460px" tableheight="345px">'''Architecture''' ||MIPS 4KEc ||
||'''Vendor''' || ||
||'''Bootloader''' ||!RedBoot ||
||'''System-On-Chip''' ||Atheros AR2315 ||
||'''CPU Speed''' ||183 MHz ||
||'''Flash size''' ||8 MiB ||
||'''RAM''' ||16 MiB ||
||'''Wireless''' ||Integrated Atheros 802.11b/g ||
||'''Ethernet''' ||1x RJ45 ||
||'''USB''' ||No ||
||'''Serial''' ||Yes ||
||'''JTAG''' ||No ||
 * 5V power supply
 * Antenna
 * SPI-Bus
== Serial Port ==
If the ethernet jack is in front of you, it looks like (RXD and TXD directions are from the computer side, i.e. swapped with respect to Fonera board side)

{{{
+-------------------+
|GND| . |RXD|TXD| . |
|VCC| . | . | . | . |
+-------------------+
+-----+ +--------+    +---+
|Power| |Ethernet|    |Ant|
}}}
RXD and TXD are lowlevel (3.3V) signals. NOT RS232 levels.

{{{
VCC (3.3V) -> red
GND        -> blue
RX         -> white
TX         -> orange
b . o w .
r . . . .
}}}
[http://jauzsi.hu/img/others/fonera_serial.jpg Here] the picture.

Serial settings are 9600-8-N-1

== Case ==
To open the case, remove the two rubber feet on the opposite site to the antenna jack, they will reveal two crosspoint screws.

== Photos ==
== JTAG ==
There seems to be a 14 pin unpopulated JTAG, but it is not that important as the !RedBoot boatloader does not seem to be crippled.

= Original software =
{{{
+PHY ID is 0022:5521
Ethernet eth0: MAC address xx:xx:xx:xx:xx
IP: 0.0.0.0/255.255.255.255, Gateway: 0.0.0.0
Default server: 0.0.0.0
RedBoot(tm) bootstrap and debug environment [ROMRAM]
Non-certified release, version v1.3.0 - built 16:57:58, Aug  7 2006
Copyright (C) 2000, 2001, 2002, 2003, 2004 Red Hat, Inc.
Board: ap51
RAM: 0x80000000-0x81000000, [0x80040450-0x80fe1000] available
FLASH: 0xa8000000 - 0xa87f0000, 128 blocks of 0x00010000 bytes each.
== Executing boot script in 1.000 seconds - enter ^C to abort
^C
RedBoot>
}}}
== Flash layout ==
{{{
RedBoot> fis list
Name              FLASH addr  Mem addr    Length      Entry point
RedBoot           0xA8000000  0xA8000000  0x00030000  0x00000000
rootfs            0xA8030000  0xA8030000  0x00700000  0x00000000
vmlinux.bin.l7    0xA8730000  0x80041000  0x000B0000  0x80041000
FIS directory     0xA87E0000  0xA87E0000  0x0000F000  0x00000000
RedBoot config    0xA87EF000  0xA87EF000  0x00001000  0x00000000
}}}
As you can see, the vmlinux.bin.l7 partition is of B0000, ergo 720896 bytes length. That means, that the kernel size should not exceed 720kb, but if it is smaller, everthing will be fine. Like wise the rootfs partition has a size of 0x700000 or 7340032 bytes. You've got 7.3 MiB space.

== Backup your Fonera's flash ==
After gaining the SSH access use these commands:

{{{
cd /dev/mdtblock
httpd -p 9090
}}}
Connect to the Fonera through the private network. Now you can download the mtd partiotions using the addresses:

{{{
http://192.168.10.1:9090/0ro
http://192.168.10.1:9090/1ro
http://192.168.10.1:9090/2ro
http://192.168.10.1:9090/3ro
http://192.168.10.1:9090/4ro
http://192.168.10.1:9090/5ro
http://192.168.10.1:9090/6ro
http://192.168.10.1:9090/7ro
}}}
Also take note of the output of the command

{{{
cat /proc/mtd
}}}
That should be:

{{{
dev:    size   erasesize  name
mtd0: 00030000 00010000 "RedBoot"
mtd1: 006f0000 00010000 "rootfs"
mtd2: 00560000 00010000 "rootfs1"
mtd3: 00010000 00010000 "config"
mtd4: 000b0000 00010000 "vmlinux.bin.l7"
mtd5: 0000f000 00010000 "FIS directory"
mtd6: 00001000 00010000 "RedBoot config"
mtd7: 00010000 00010000 "board_config"
}}}
== Restore the original firmware ==
== Unbricking the Fonera ==
This is taken from [http://fon.freddy.eu.org/fonera/howto-factory-reset.txt here]. Some people asked me how to recover a Fonera, here are some methods:

=== Method 1 - Button Reset ===
Press the reset button for > 15 seconds This requires a working Fonera, and it should be on for a while.

=== Method 2 - Erase ===
Run "rm -R /jffs/*" and pull the plug. It should result in a reseted Fonera.

=== Method 3 - MTD Trick ===
If everything fails and you killed your shell on the serial console: As soon as you see "Please press Enter to activate this console." press Enter Now you have to hurry up! Paste "cat /proc/mtd" and press Enter (even if you don't see your pasted line) You should see this list:

{{{
dev:    size   erasesize  name
mtd0: 00030000 00010000 "RedBoot"
mtd1: 006f0000 00010000 "rootfs"
mtd2: 00560000 00010000 "rootfs1"
mtd3: 00010000 00010000 "config"
mtd4: 000b0000 00010000 "vmlinux.bin.l7"
mtd5: 0000f000 00010000 "FIS directory"
mtd6: 00001000 00010000 "RedBoot config"
mtd7: 00010000 00010000 "board_config" }}}
Search for the "rootfs1" line and take the number of the beginning of the line (mtdX) Now you have to reboot again Press Enter again but now paste this line:

{{{
echo -ne '\xde\xad\xc0\xde' > "/dev/mtdblock/2"
}}}
Make sure you're using "/dev/mtdblock/X" (the mtdX number) Now reset it again and you should receive this message: Please press Enter to activate this console. jffs2_scan_eraseblock(): End of file system marker found at 0x0 jffs2_build_filesystem(): unlocking the mtd device... done. jffs2_build_filesystem(): erasing all blocks after the end marker... This takes some time but you should have a fresh Fonera again. This Method will work only if the enter message will show up. If not the endmarker can be written directly in the !RedBoot Environment.

{{{
mfill -b 0x80041000 -l 4 -p 0xdeadc0de -4
fis write -b 0x80041000 -f 0xa81b0000 -l 0x00000004
}}}
0xa81b0000 is the start of mtd2 (0xA8030000 + 0x00180000 kernel size)

=== Method 4 - TFTP/HTTP/Xmodem Recover ===
A way to recover it with Xmodem, a TFTP or HTTP server and !RedBoot is http://www.easy2design.de/bla/?page_id=98.

=== Method 5 - Custumer Care ===
 1. Double click the Local Area Connection icon to show the connection's Status dialog box.
 1. Double click Internet Protocol (TCP/IP)
 1. Click Start>Connect to>Show all connections,
 1. Click the Use the following IP address option button and type:
  a. IP address: 169.254.255.2
  a. Subnet mask: 255.255.255.0
  a. Default gateway: (leave blank)
  a. Preferred DNS server: (leave blank)
  a. Alternate DNS server: (leave blank)
 1. Open your browser and type any URL (http://169.254.255.1).
 1. You will be asked for the Username and Password. The default values are Username=admin, Password=admin.
 1. Configure La Fonera
 1. Turn La Fonera off and connect it to your router so you can continue working normally.
 1. Remember to change again the values of your Local Area Network.
=== Updating / Unbricking via RedBoot ===
'''NOTE''': Word on IRC is that the instructions down in the "Flashing !OpenWrt" section are the ones you should use. Specifying all those parameters to "fis create" is said to be no good idea. Yet, I will leave this section until further confirmation. - Fatus

On your computer:

{{{
$ wget -q -O - http://downloads.fon.com/firmware/current/fonera_0.7.1.1.fon | tail -c +520 - | tar xvfz -
upgrade
rootfs.squashfs
kernel.lzma
hotfix
$ cp kernel.lzma /tftp/
$ cp rootfs.squashfs /tftp/
# in.tftpd -vvv -l -s /tftp/ -r blksize
}}}
On your Fonera

Enable networking (I do not have to remind you to plug your network cable in, do it? ;-)

{{{
RedBoot> ip_address -l 192.168.5.75/24 -h 192.168.5.2
IP: 192.168.5.75/255.255.255.0, Gateway: 0.0.0.0
Default server: 192.168.5.2
}}}
Load the Kernel to the ramdisk

{{{
RedBoot> load -r -v -b 0x80041000 kernel.lzma
Using default protocol (TFTP)
Raw file loaded 0x80041000-0x800c0fff, assumed entry at 0x80041000
}}}
The Kernel is now stored in the ramdisk at address 0x80041000, we can now write the file from the ramdisk to the flash

{{{
RedBoot> fis create -r 0x80041000 -e 0x80041000 vmlinux.bin.l7
An image named 'vmlinux.bin.l7' exists - continue (y/n)? y
... Erase from 0xa8730000-0xa87e0000: ...........
... Program from 0x80041000-0x800c1000 at 0xa8730000: ........
... Erase from 0xa87e0000-0xa87f0000: .
... Program from 0x80ff0000-0x81000000 at 0xa87e0000: .
}}}
And now the same for the rootfs:

{{{
RedBoot> load -r -v -b 0x80041000 rootfs.squashfs
Using default protocol (TFTP)
Raw file loaded 0x80041000-0x801c0fff, assumed entry at 0x80041000
}}}
And now write it to the flash:

{{{
RedBoot> fis create -b 0x80041000 -f 0xA8030000 -l 0x00700000 -e 0x00000000 rootfs
An image named 'rootfs' exists - continue (y/n)? y
... Erase from 0xa8030000-0xa8730000: ..........................................................................................................
... Program from 0x80041000-0x80741000 at 0xa8030000: ..........................................................................................
... Erase from 0xa87e0000-0xa87f0000: .
... Program from 0x80ff0000-0x81000000 at 0xa87e0000: .
}}}
This basically says, that it should write the content from the ramdisk at address 0x80041000 to the already existing flash image vmlinux.bin.l7 with the very same entry point for starting the kernel.

*Those last steps did not really work for me, had an overlapping error so I did it in reverse order and another args when creating vmlinux fis, check below. //QoS

{{{
RedBoot> load -r -v -b 0x80041000 rootfs.squashfs
RedBoot> fis create -b 0x80041000 -f 0xA8030000 -l 0x00700000 -e 0x00000000 rootfs
RedBoot> load -r -v -b 0x80041000 kernel.lzma
RedBoot> fis create -r 0x80041000 -f 0xA8730000 -l 0x000B0000 -e 0x80041000 vmlinux.bin.l7
RedBoot> fis list
Name              FLASH addr  Mem addr    Length      Entry point
RedBoot           0xA8000000  0xA8000000  0x00030000  0x00000000
rootfs            0xA8030000  0xA8030000  0x00700000  0x00000000
vmlinux.bin.l7    0xA8730000  0x80041000  0x000B0000  0x80041000
FIS directory     0xA87E0000  0xA87E0000  0x0000F000  0x00000000
RedBoot config    0xA87EF000  0xA87EF000  0x00001000  0x00000000
}}}
= Flashing OpenWrt =
You have to download two files (right click and save as).

 * [http://downloads.openwrt.org/kamikaze/7.07/atheros-2.6/openwrt-atheros-2.6-vmlinux.lzma openwrt-atheros-2.6-vmlinux.lzma]
 * [http://downloads.openwrt.org/kamikaze/7.07/atheros-2.6/openwrt-atheros-2.6-root.squashfs openwrt-atheros-2.6-root.squashfs]
Copy openwrt-atheros-2.6-vmlinux.lzma and openwrt-atheros-2.6-root.squashfs to /tftpboot/ and flash them like this:

{{{
^C
RedBoot> ip_address -l 192.168.5.75/24 -h 192.168.5.2
IP: 192.168.5.75/255.255.255.0, Gateway: 0.0.0.0
Default server: 192.168.5.2
RedBoot> lo -r -b %{FREEMEMLO} openwrt-atheros-2.6-vmlinux.lzma
Using default protocol (TFTP)
Raw file loaded 0x80041000-0x800f0fff, assumed entry at 0x80041000
RedBoot> fi init}}}
The values for the -e and -r switches in the 'fi cr' !RedBoot command below is the Kernel entry point. Do not change this value.

{{{
RedBoot> fi cr -e 0x80041000 -r 0x80041000 vmlinux.bin.l7
An image named 'vmlinux.bin.l7' exists - continue (y/n)? y
... Erase from 0xa8730000-0xa87e0000: ...........
... Program from 0x80041000-0x800f1000 at 0xa8730000: ...........
... Erase from 0xa87e0000-0xa87f0000: .
... Program from 0x80ff0000-0x81000000 at 0xa87e0000: .
}}}
"fis free" will print the first and last free block

{{{
RedBoot> fis free
      0xA80F0000 .. 0xA87E0000
}}}
now do the math (last - first, cause you need the difference)

{{{
server:~# bc
obase=16
ibase=16
A87E0000 - A80F0000
6F0000
}}}
Replace ''0xLENGTH'' with the value above (0x006F0000 in my case) and flash the the rootfs:

{{{
RedBoot> lo -r -b %{FREEMEMLO} openwrt-atheros-2.6-root.squashfs
Using default protocol (TFTP)
|
Raw file loaded 0x80041000-0x80200fff, assumed entry at 0x80041000
RedBoot> fi cr -l 0xLENGTH rootfs
An image named 'rootfs' exists - continue (y/n)? y
... Erase from 0xa8030000-0xa8730000: ................................................................................................................
... Program from 0x80041000-0x80741000 at 0xa8030000: ..............................................................................................................
... Erase from 0xa87e0000-0xa87f0000: .
... Program from 0x80ff0000-0x81000000 at 0xa87e0000: .
RedBoot> reset
}}}
If everything is okay, then it will now look like this:

{{{
+PHY ID is 0022:5521
...
== Executing boot script in 1.000 seconds - enter ^C to abort
RedBoot> fis load -l vmlinux.bin.l7
Image loaded from 0x80041000-0x8028e086
RedBoot> exec
Now booting linux kernel:
 Base address 0x80030000 Entry 0x80041000
 Cmdline :
Linux version 2.6.19.1 (nobody@dummy) (gcc version 3.4.6 (OpenWrt-2.0)) #1 Mon Dec 25 15:45:45 CET 2006
CPU revision is: 00019064
Determined physical RAM map:
 memory: 01000000 @ 00000000 (usable)
Initrd not found or empty - disabling initrd
Built 1 zonelists.  Total pages: 4064
Kernel command line: console=ttyS0,9600 rootfstype=squashfs,jffs2
...
Please press Enter to activate this console.
BusyBox v1.2.1 (2006.12.25-14:36+0000) Built-in shell (ash)
Enter 'help' for a list of built-in commands.
  _______                     ________        __
 |       |.-----.-----.-----.|  |  |  |.----.|  |_
 |   -   ||  _  |  -__|     ||  |  |  ||   _||   _|
 |_______||   __|_____|__|__||________||__|  |____|
          |__| W I R E L E S S   F R E E D O M
 KAMIKAZE (bleeding edge, r5899) -------------------
}}}
'''NOTE''': If you changed !RedBoot's baud rate to something different than 9600bps, revert that change unless your terminal program does auto baud detection -- !OpenWrt logs to its serial console with 9600bps, so having the same baud rate in !RedBoot is a good idea.

= Telnet into RedBoot =
You can change the !RedBoot configuration, so you can later telnet into this bootloader in order to reflash this device from there, without having serial access.

The default form of the fconfig command will force you to enter the data, change and confirm every initialized variable. To avoid reentering the '''Boot script''' data and harming unnecessary variables, run the "fconfig list" command first to look at variable names and values:

{{{
RedBoot> fconfig -l -n
boot_script: true
boot_script_data:
.. fis load -l vmlinux.bin.l7
.. exec
boot_script_timeout: 1
bootp: false
bootp_my_gateway_ip: 0.0.0.0
bootp_my_ip: 0.0.0.0
bootp_my_ip_mask: 255.255.255.255
bootp_server_ip: 0.0.0.0
console_baud_rate: 9600
gdb_port: 9000
info_console_force: false
net_debug: false
}}}
Next change only necessary variables (using their names from the previous listing) and update the !RedBoot non-volatile configuration after the last change:

{{{
RedBoot> fconfig boot_script_timeout 10
boot_script_timeout: Setting to 10
Update RedBoot non-volatile configuration - continue (y/n)? n
RedBoot> fconfig bootp_my_ip 192.168.5.22
Update RedBoot non-volatile configuration - continue (y/n)? n
RedBoot> fconfig bootp_my_ip_mask 255.255.255.0
Update RedBoot non-volatile configuration - continue (y/n)? n
RedBoot> fconfig bootp_server_ip 192.168.5.2
Update RedBoot non-volatile configuration - continue (y/n)? y
... Erase from 0xa87e0000-0xa87f0000: .
... Program from 0x80ff0000-0x81000000 at 0xa87e0000: .
}}}
'''Note:''''' ''The configuration is only in the RAM until you update'' ''the !RedBoot non-volatile configuration. If you reset the device without updating, the configuration will not be changed. You can use changes without the update for temporary settings.

Verify the configuration by listing the aliases this time:

{{{
RedBoot> fconfig -l
Run script at boot: true
Boot script:
.. fis load -l vmlinux.bin.l7
.. exec
Boot script timeout (1000ms resolution): 10
Use BOOTP for network configuration: false
Gateway IP address: 0.0.0.0
Local IP address: 192.168.5.22
Local IP address mask: 255.255.255.0
Default server IP address: 192.168.5.2
Console baud rate: 9600
GDB connection port: 9000
Force console for special debug messages: false
Network debug at boot time: false
}}}
I specified a 10 second timeout here, so I have this 10 second time frame to telnet into !RedBoot. If you are not able to hit the enter-key within 10 seconds after powering up, go for a larger time frame.

{{{
+PHY ID is 0022:5521
Ethernet eth0: MAC address xx:xx:xx:xx:xx:xx
IP: 192.168.5.22/255.255.255.0, Gateway: 0.0.0.0
Default server: 192.168.5.2
RedBoot(tm) bootstrap and debug environment [ROMRAM]
Non-certified release, version v1.3.0 - built 16:57:58, Aug  7 2006
Copyright (C) 2000, 2001, 2002, 2003, 2004 Red Hat, Inc.
Board: ap51
RAM: 0x80000000-0x81000000, [0x80040450-0x80fe1000] available
FLASH: 0xa8000000 - 0xa87f0000, 128 blocks of 0x00010000 bytes each.
== Executing boot script in 10.000 seconds - enter ^C to abort
}}}
Actually I had problems with my old BSD telnet on Slackware 11 to send a proper CTRL-C to the !RedBoot console. I circumvented the problem with this small trick:

{{{
$ echo -e "\0377\0364\0377\0375\0006" > break
$ nc -vvv 192.168.5.22 9000 < break ; telnet 192.168.5.22 9000
Warning: Inverse name lookup failed for `192.168.5.22'
192.168.5.22 9000 open
== Executing boot script in 7.420 seconds - enter ^C to abort
ÿü^C
RedBoot> ÿüExiting.
Total received bytes: 82
Total sent bytes: 6
Trying 192.168.5.22...
Connected to 192.168.5.22.
Escape character is '^]'.
RedBoot>
}}}
I have to CTRL-C abort netcat.

The CTRL-C problem seems to be caused by a disabled TELNET LINEMODE option. When you enable this option by creating a file ~/.telnetrc with the following contents:

{{{
192.168.5.22 9000
        mode line
}}}
You can interrupt redboot with CTRL-C:

{{{
$ arping -qf 192.168.5.22 ; telnet 192.168.5.22 9000
WARNING: interface is ignored: Operation not permitted
Trying 192.168.5.22...
?Invalid command
Connected to 192.168.5.22.
Escape character is '^]'.
== Executing boot script in 9.940 seconds - enter ^C to abort
^C
RedBoot>
}}}
The boot process is somehow signalled via the LEDs, first only the power LED is on, then the internet LED starts blinking, and when this internet LED is solid green, it is the right time to connect to the !RedBoot console.

This is the point, where I disconnected the serial cable and closed the case. If the kernel is booting and SSH working, I do not need any debug-stuff in between. It is possible to unbrick the fonera with this !RedBoot console, as I can always reflash to a working firmware.

= Reflash the RedBoot Config from SSH... =
In order to get the access to !RedBoot through an ethernet cable instead of the serial console.

As we can see via 'dmesg' there is a mtd for the !RedBoot config:

{{{
<5>Creating 6 MTD partitions on "spiflash":
<5>0x00000000-0x00030000 : "RedBoot"
<5>0x00030000-0x00720000 : "rootfs"
<5>0x00730000-0x007e0000 : "vmlinux.bin.l7"
<5>0x007e0000-0x007ef000 : "FIS directory"
<5>0x007ef000-0x007f0000 : "RedBoot config"
<5>0x007f0000-0x00800000 : "board_config"
}}}
We can even dump that mtd content with

{{{
root@OpenWrt:~# cat /dev/mtd/4ro > /tmp/redboot_config
root@OpenWrt:~# strings /tmp/redboot_config
boot_script
boot_script_data
boot_script
fis load -l vmlinux.bin.l7
exec
boot_script_timeout
boot_script
bootp
bootp_my_gateway_ip
bootp
bootp_my_ip
bootp
bootp_my_ip_mask
bootp
bootp_server_ip
console_baud_rate
gdb_port
info_console_force
info_console_number
info_console_force
net_debug
}}}
It should be possible to use such a file to reflash other foneras in order to gain !RedBoot access without ever opening the case. As long as someone can gain shell access to the Fonera, he could enable !RedBoot telnet access to his Fonera and fiddle around with it. With this !RedBoot GDB console, you can always restore the original firmware, even if your fonera does not boot your latest Linux experiment.

This would be nice, but does not work, as the "!RedBoot config" mtd partion is not writable.

{{{
root@OpenWrt:~# mtd write /tmp/redboot_config "RedBoot config"
}}}
According to this [http://www.dd-wrt.com/phpBB2/viewtopic.php?p=49585#49585 post], you can make this partition writable, if you add in kernel/driver/mtd/mtdpart.c after line 435

{{{
                        if (!(slave->mtd.flags & MTD_WRITEABLE)){
                        slave->mtd.flags |= MTD_WRITEABLE;
                        printk ("mtd: partition \"%s\" was read-only -- force writable -- CAMICIA HACK\n",
                                parts[i].name);
                        }
}}}
So you have to reflash the Kernel with a Kernel image, that allows writing to the !RedBoot config partition and then reflash that config partition in order to gain access to the !RedBoot console.

Please note that they were not writeable for a reason. Writing "!RedBoot config" is probably going to reset the FIS directory because it is on the same "erase sector". This is not a major problem since with !RedBoot we can easily recreate them using the command "fis init" and to install !OpenWrt we must do this anyway.

This whole procedure is described [http://www.dd-wrt.com/phpBB2/viewtopic.php?t=9011 here].

The basic steps are:

{{{
root@OpenWrt:~# cd /tmp
root@OpenWrt:~# wget http://coppercore.net/~kevin/fon/openwrt-ar531x-2.4-vmlinux-CAMICIA.lzma
Connecting to coppercore.net[64.27.5.164]:80
openwrt-ar531x-2.4-v 100% |*****************************| 512 KB 00:00 ETA
root@OpenWrt:~# mtd -e vmlinux.bin.l7 write openwrt-ar531x-2.4-vmlinux-CAMICIA.lzma vmlinux.bin.l7
Unlocking vmlinux.bin.l7 ...
Erasing vmlinux.bin.l7 ...
Writing from openwrt-ar531x-2.4-vmlinux-CAMICIA.lzma to vmlinux.bin.l7 ... [w]
root@OpenWrt:~# reboot
... wait ...
root@OpenWrt:~# cd /tmp
root@OpenWrt:~# wget http://coppercore.net/~kevin/fon/out.hex
Connecting to coppercore.net[64.27.5.164]:80
out.hex 100% |*******************************| 4096 00:00 ETA
root@OpenWrt:~# mtd -e "RedBoot config" write out.hex "RedBoot config"
Unlocking RedBoot config ...
Erasing RedBoot config ...
Writing from out.hex to RedBoot config ... [w]
root@OpenWrt:~# reboot
...wait...
$ telnet 192.168.1.254 9000
RedBoot> fis init
}}}
= Basic configuration =
== Use LAN as WAN port ==
== PPPoE ==
With Kamikaze 7.07 PPPoE works out-of-the-box. All required packages are already installed in the default image.To configure PPPoE with UCI, do this:

{{{
uci set network.wan.proto=pppoe
uci set network.wan.username=<pppoe_psername>
uci set network.wan.password=<pppoe_password>
uci commit network && ifup wan}}}
== QoS ==
Install the qos-scripts package

{{{
ipkg install qos-scripts
}}}
Basic QoS configuration using UCI:

{{{
uci set qos.wan.upload=192            # Upload speed in KB
uci set qos.wan.download=2048         # Download speed in KB
uci commit qos}}}
Start QoS and enable on next boot

{{{
/etc/init.d/qos start
/etc/init.d/qos enable
}}}
== Dynamic DNS ==
Please see [:DDNSHowTo:Dynamic DNS].

== WiFi ==
This describes the !WiFi configuration with the Fonera acting in plain AP mode.

=== Enable WiFi ===
{{{
uci set wireless.wifi0.disabled=0
uci commit wireless && wifi}}}
[[Anchor(wpa)]] [[Anchor(WPA)]]

=== WiFi encryption ===
To generate a random password for you key you can use the pwgen program. Pwgen is available for most Linux distributions and is also packaged for !OpenWrt Kamikaze. E.g. pwgen 5 1 to generate a random 5 characters password.

==== WEP encryption (not recommended) ====
Some notes for the WEP key format:

 * The format for the WEP key for the key1 option is HEX
 * The length of a 64bit WEP key must be exact 5 characters
 * The length of a 128bit WEP key must be exact 13 characters
 * Allowed characters are letters (upper and lower case) and numbers
Generate a 64bit WEP key:

{{{
echo -n 'awerf' | hexdump -e '5/1 "%02x" "\n"' | cut -d ':' -f 1-5
6177657266
}}}
Generate a128bit WEP key:

{{{
echo -n 'xdhdkkewioddd' | hexdump -e '13/1 "%02x" "\n"' | cut -d ':' -f 1-13
786468646b6b6577696f646464}}}
The above commands generate a 64bit and a 128bit WEP key in hex format.

Now use UCI to configure WEP encryption with the hex key you just generated.

{{{
uci set wireless.cfg2.encryption=wep
uci set wireless.cfg2.key1=<WEP_key_in_hex_format>
uci commit wireless && wifi}}}
==== WPA encryption ====
Install the hostapd package.

{{{
ipkg install hostapd}}}
'''TIP:''' If you only need WPA (PSK) encryption you can install the hostapd-mini package which does not depend on the zlib and libopenssl packages.

===== Configure WPA (PSK) =====
Configure WPA (PSK) encryption using UCI.

{{{
uci set wireless.cfg2.encryption=psk
uci set wireless.cfg2.key=<password>
uci commit wireless && wifi}}}
'''Note: '''For the key only letters (upper and lower case) and numbers are allowed. The length must be between 8 and 63 characters.

===== Configure WPA2 (PSK) =====
Configure WPA2 (PSK) encryption using UCI.

{{{
uci set wireless.cfg2.encryption=psk2
uci set wireless.cfg2.key=<password>
uci commit wireless && wifi}}}
'''Note: '''For the key only letters (upper and lower case) and numbers are allowed. The length must be between 8 and 63 characters.

 . [[Anchor(WiFi toggle)]]
  . [[Anchor(wifitoggle)]]
=== List connected clients ===
{{{
wlanconfig ath0 list}}}
= Correcting antenna settings under Kamikaze =
According to [http://wiki.freifunk-hannover.de/Fonera_mit_OLSR this german Wiki entry] by default Kamikaze utilizes antenna diversity on the Fonera. It also uses the wrong antenna :(

To change that put the following in the "wifi-device" section of /etc/

To change that put the following in the "wifi-device" section of /etc/config/wireless (see the example above):

{{{
option diversity 0
option txantenna 1
option rxantenna 1
}}}
If you are using the Fonera to create a link over long distances, the distance setting might help too:

{{{
option distance <distance>
}}}
Where <distance> is the distance between the ap and the furthest client in meters

It is possible to add a second antenna and use diversity between them. See the "Resources" section below.

= Hardware Hacks =
As with most routers, the Fonera has some gpio pins that extra hardware can be connected to. Here are 2 interesting hardware hacks :

 * [http://www.phrozen.org/fonera.html Adding a MMC card to the Fonera]
 * [http://wiki.openwrt.org/OpenWrtDocs/Hardware/Fon/FoneraMP3 Turning the Foneras into a hardware mp3 client]
= Resources =
 * [http://tech.am/2006/10/06/autopsy-of-a-fonera/ Autopsy of a Fonera]
 * [http://blog.blase16.de/index.php?url=2006/11/28/Hacking-Fonera Get the SSH access to the Fonera]
 * [http://stefans.datenbruch.de/lafonera/ Hacking the La Fonera]
 * [http://forum.openwrt.org/viewtopic.php?pid=39251#p39251 OpenWrt development]
 * [http://jauzsi.hu/2006/10/13/inside-of-the-fonera Picture of serial]
 * [http://www.easy2design.de/bla/?page_id=98 Debricking and more]
 * [http://www.dd-wrt.com/phpBB2/viewtopic.php?t=9011 How to get the access to RedBoot without the Serial Console]
 * [http://coppercore.net/~kevin/fon/ Files to get the access to RedBoot without the Serial Console]
 * [http://ecos.sourceware.org/docs-latest/redboot/redboot-guide.html RedBoot userguide]
 * [http://wiki.ninux.org/moin.cgi/La_Fonera Misc Links (Italian language)]
 * [http://www.tldp.org/LDP/lkmpg/ The Linux Kernel Module Programming Guide]
 * [http://karman.homelinux.net/blog/ Blog about Fonera] (Spanish)
 * [http://mrmuh.blogspot.com/2007/01/codename-kolofonium-realease-date.html Blog about Hacking the 0.7.1r2 firmware]
 * [http://blog.extreme-networking.com/ OpenWrt installation guide (Italian) and misc]
 * [http://wiki.freifunk-hannover.de/Fonera_mit_OLSR The Fonera in the Freifunk project, German] [http://wiki.freifunk.net/Fonera_with_OLSR_(English) English]: comprehensive guide to flashing la fonera with Kamikaze.
 * [http://www.dd-wrt.com/wiki/index.php/LaFonera_Hardware_Second-Antenna LaFonera Hardware Second-Antenna] Hardware hack of how to add a second antenna (and diversity)
