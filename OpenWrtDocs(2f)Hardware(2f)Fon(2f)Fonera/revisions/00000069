#pragma section-numbers off
||<tablebgcolor="#f1f1ed" tablewidth="40%" tablestyle="margin: 0pt 0pt 1em 1em; float: right; font-size: 0.9em;"style="padding: 0.5em;">[[TableOfContents]]||

= Fonera =
the Fonera FON2100A is based on an Atheros System on a Chip (Soc). It got a MIPS 4KEc V6.4 processor. There is an ongoing process porting OpenWRT to this chip: AtherosPort

It's almost identical to the [http://meraki.net/mini.html Meraki Mini], who provide their own [http://www.meraki.net/linux/ openwrt fork]

 * 5V power supply
 * 1x ethernet jack
 * antenna
 * serial
 * 16MB RAM
 * 8MB Flash
 * SPI-Bus
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

According to OpenWRT, the output-power is set to 18dBm, in contrast to the FCC-RF-tests where an output power of almost 25dBm (actually 24.89dBm on channel 6 in 802.11g mode) is measured. Question here is, if further versions will provide an adjustable TX-Power up to that level. Is the information provided by OpenWRT of 18dBm just a hypothetical value??? I found no reference in Kamikaze yet, how to adjust it.

Another interessting issue is the possible frequency range, as specified by Atheros itself at http://www.atheros.com/pt/bulletins/AR5006AP_GBulletin.pdf - where the available band ranges from 2.300GHz to 2.500GHz. Question here is, if there will be an option to use further frequencies than the international standardized 14 Channels. In particular, there might be a very high interest e.g. from the amateur-radio community!

Irregular updates of bleeding edge kamikaze Firmware along with pre-compiled packages and beta webinterface can be found at http://mobileaccess.de/fonera/bin and http://mobileaccess.de/fonera/bin/packages respectively. Simply add this URL to your ipkg configuration at /etc/ipkg.conf 


== Case ==
to open the case, remove the two feet on the opposite site to the antenna jack, they'll reveal two crosspoint screws.

== Serial ==
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

I have to power the fonera up wait for a few seconds before connecting the serial cable, otherwise it doesn't boot.

Another way might be to push the reset button located on the underside of the router.

== CPU ==
{{{
root@(none):/# cat /proc/cpuinfo
system type             : Atheros AR531X_COBRA
processor               : 0
cpu model               : MIPS 4KEc V6.4
BogoMIPS                : 183.50
wait instruction        : yes
microsecond timers      : yes
tlb_entries             : 16
extra interrupt vector  : yes
hardware watchpoint     : no
VCED exceptions         : not available
VCEI exceptions         : not available
}}}
== JTAG ==
There seems to be a 14 pin unpopulated jtag, but it's not that important as the redboot boatloader doesn't seem to be crippled.

== Original software ==
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
=== Flash layout ===
{{{
RedBoot> fis list
Name              FLASH addr  Mem addr    Length      Entry point
RedBoot           0xA8000000  0xA8000000  0x00030000  0x00000000
rootfs            0xA8030000  0xA8030000  0x00700000  0x00000000
vmlinux.bin.l7    0xA8730000  0x80041000  0x000B0000  0x80041000
FIS directory     0xA87E0000  0xA87E0000  0x0000F000  0x00000000
RedBoot config    0xA87EF000  0xA87EF000  0x00001000  0x00000000
}}}
As you can see, the vmlinux.bin.l7 partition is of B0000, ergo 720896 bytes length. That means, that the kernel size should not exceed 720kb, but if it's smaller, everthing will be fine. Like wise the rootfs partition has a size of 0x700000 or 7340032 bytes. You've got 7.3 mb space.

== Unbricking the Fonera ==
This is taken from [http://fon.freddy.eu.org/fonera/howto-factory-reset.txt here]

Some people asked me how to recover a fonera, here are some methods:

=== Method 1 - Button Reset ===
 . Press the reset button for > 15 seconds This requires a working Fonera, and it should be on for a while.
=== Method 2 - Erase ===
 . Run "rm -R /jffs/*" and pull the plug It should result in a reseted fonera
=== Method 3 - MTD Trick ===
 . If everything fails and you killed your shell on the serial console: As soon as you see "Please press Enter to activate this console." press Enter Now you have to hurry up! Paste "cat /proc/mtd" and press Enter (even if you don't see your pasted line) You should see this list:
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
 . Search for the "rootfs1" line and take the number of the beginning of the line (mtdX) Now you have to reboot again Press Enter again but now paste this line:
{{{
        echo -ne '\xde\xad\xc0\xde' > "/dev/mtdblock/2"
}}}
 . Make sure you're using "/dev/mtdblock/X" (the mtdX number) Now reset it again and you should receive this message:
  . Please press Enter to activate this console. jffs2_scan_eraseblock(): End of file system marker found at 0x0 jffs2_build_filesystem(): unlocking the mtd device... done. jffs2_build_filesystem(): erasing all blocks after the end marker...
 This takes some time but you should have a fresh fonera again.

This Method will work only if the enter message will show up. If not the endmarker can be written directly in the RedBoot Environment.
{{{
         mfill -b 0x80041000 -l 4 -p 0xdeadc0de -4
         fis write -b 0x80041000 -f 0xa81b0000 -l 0x00000004
}}}
0xa81b0000 is the start of mtd2 (0xA8030000 + 0x00180000 kernel size)

=== Method 4 - TFTP/HTTP/Xmodem Recover ===
A way to recover it with Xmodem, a TFTP or HTTP server and RedBoot is [
http://www.easy2design.de/bla/?page_id=98 here]. If this doesn't work you probably have to use a JTAG cable.

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
=== Updating / Unbricking via redboot ===

['''NOTE''': Word on IRC is that the instructions down in the "Flashing OpenWRT" section are the ones you should use. Specifying all those parameters to "fis create" is said to be no good idea. Yet, I'll leave this section until further confirmation. -Fatus]

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
On your fonera

Enable networking (I don't have to remind you to plug your network cable in, do it? ;-)

{{{
RedBoot> ip_address -l 192.168.5.75/24 -h 192.168.5.2
IP: 192.168.5.75/255.255.255.0, Gateway: 0.0.0.0
Default server: 192.168.5.2
}}}
Load the kernel to the ramdisk

{{{
RedBoot> load -r -v -b 0x80041000 kernel.lzma
Using default protocol (TFTP)
Raw file loaded 0x80041000-0x800c0fff, assumed entry at 0x80041000
}}}
the kernel is now stored in the ramdisk at address 0x80041000, we can now write the file from the ramdisk to the flash

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
== Flashing OpenWrt ==
[https://dev.openwrt.org/changeset/5898 SVN] trunk supports this atheros SOC. thank you, nbd!

After you build a kamikaze image with svn trunk for the atheros-2.6 target (or visited http://downloads.openwrt.org/kamikaze), you get the following files in your ./bin/ directory:

{{{
openwrt-atheros-2.6-root.jffs2-128k
openwrt-atheros-2.6-root.jffs2-256k
openwrt-atheros-2.6-root.jffs2-64k
openwrt-atheros-2.6-root.squashfs
openwrt-atheros-2.6-vmlinux.elf
openwrt-atheros-2.6-vmlinux.gz
openwrt-atheros-2.6-vmlinux.lzma
packages
}}}

Copy openwrt-atheros-2.6-vmlinux.lzma and openwrt-atheros-2.6-root.squashfs to /tftpboot/ and flash them like this:

{{{
^C
RedBoot> ip_address -l 192.168.5.75/24 -h 192.168.5.2
IP: 192.168.5.75/255.255.255.0, Gateway: 0.0.0.0
Default server: 192.168.5.2

RedBoot> lo -r -b %{FREEMEMLO} openwrt-atheros-2.6-vmlinux.lzma
Using default protocol (TFTP)
Raw file loaded 0x80041000-0x800f0fff, assumed entry at 0x80041000

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
Replace ''0xCHANGEME'' with the value above (0x006F0000 in my case) and flash the the rootfs:
{{{
RedBoot> lo -r -b %{FREEMEMLO} openwrt-atheros-2.6-root.squashfs
Using default protocol (TFTP)
|
Raw file loaded 0x80041000-0x80200fff, assumed entry at 0x80041000

RedBoot> fi cr -l 0xCHANGEME rootfs
An image named 'rootfs' exists - continue (y/n)? y
... Erase from 0xa8030000-0xa8730000: ................................................................................................................
... Program from 0x80041000-0x80741000 at 0xa8030000: ..............................................................................................................
... Erase from 0xa87e0000-0xa87f0000: .
... Program from 0x80ff0000-0x81000000 at 0xa87e0000: .

RedBoot> reset
}}}

If everything is okay, then it'll now look like this:

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

'''NOTE''': if you changed RedBoot's baud rate to something different than 9600bps, revert that change unless your terminal program does auto baud detection -- OpenWRT logs to its serial console with 9600bps, so having the same baud rate in RedBoot is a good idea.

Furthermore, it's important to use the files in ./bin/ and NOT ./build_mips/linux-2.6-atheros/vmlinux.bin.l7 It took me quite some time to figure out why this vmlinux.bin.l7 doesn't work.

The magic is, that ./target/linux/atheros-2.6/image/Makefile converts the image with:

{{{
dd if=$(KDIR)/vmlinux.bin.l7 of=$(BIN_DIR)/openwrt-$(BOARD)-$(KERNEL)-vmlinux.lzma bs=65536 conv=sync
}}}
where conv=sync pads every input block with NULs to ibs-size, which is needed!

== Telnet into Redboot ==
You can change the redboot configuration, so you can later telnet into this bootmanager in order to reflash this device from there, without having serial access.

The default form of the fconfig command will force you to enter the data, change and confirm every initialized variable. To avoid reentering the '''Boot script''' data and harming unnecessary variables, run the fconfig list command first to look at variable names and values:
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

Next change only necessary variables (using their names from the previous listing) and update the RedBoot non-volatile configuration after the last change:
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
''Note: The configuration is only in the RAM until you update the RedBoot non-volatile configuration. If you reset the device without updating, the configuration will not be changed. You can use changes without the update for temporary settings.''

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

I specified a 10 second timeout here, so I have this 10 second time frame to telnet into redboot. If you are not able to hit the enter-key within 10 seconds after powering up, go for a larger time frame.

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
Actually I had problems with my old BSD telnet on slackware 11 to send a proper ctrl-c to the redboot gdb console. I circumvented the problem with this small trick:

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
I have to ctrl-c abort netcat.

The ctrl-c problem seems to be caused by a disabled TELNET LINEMODE option. When you enable this option by creating a file ~/.telnetrc with the following contents:
{{{
192.168.5.22 9000
        mode line
}}}
you can interrupt redboot with ctrl-c:
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

The boot process is somehow signalled via the leds, first only the power led is on, then the internet led starts blinking, and when this internet led is solid green, it's the right time to connect to the gdb console.

This is the point, where I disconnected the serial cable and closed the case. If the kernel is booting and ssh working, I don't need any debug-stuff in between. It's possible to unbrick the fonera with this redboot gdb console, as I can always reflash to a working firmware.

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
== Reflash the RedBoot Config from SSH... ==
...in order to get the access to Redboot through an ethernet cable instead of the serial console

As we can see via 'dmesg' there is a mtd for the redboot config:

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
It should be possible to use such a file to reflash other foneras in order to gain redboot access without ever opening the case. As long as someone can gain shell access to the fonera, he could enable redboot telnet access to his fonera and fiddle around with it. With this redboot gdb console, you can always restore the original firmware, even if your fonera doesn't boot your latest linux experiment.

This would be nice, but doesn't work, as the "RedBoot config" mtd partion isn't writable.

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
So you have to reflash the kernel with a kernel image, that allows writing to the redboot config partition and then reflash that config partition in order to gain access to the Redboot console.

Please note that they were not writeable for a reason. Writing "Redboot config" is probably going to reset the FIS directory because it is on the same "erase sector". This is not a major problem since with Redboot we can easily recreate them using the command ""fis init"" and to install Openwrt we must do this anyway.

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
== basic wpa config ==
It's a bit harder to find the documentation for kamikaze, as the config system changed. So here's a list of config entries to use the fonera as a wpa-psk accesspoint-bridge. You can take it with your laptop and use it as a mobile ap whereever you find a rj45 plug.

Edit your ipkg.conf using vi.

/etc/ipkg.conf
{{{
src snapshots http://ipkg.k1k2.de/packages
dest root /
dest ram /tmp
}}}


Now update your application list and install 'hostapd' and 'wpa-supplicant'.
{{{
root@OpenWrt:~ ipkg update
root@OpenWrt:~ ipkg install hostapd
root@OpenWrt:~ ipkg install wpa-supplicant
}}}


Edit your network settings using vi.

/etc/config/network
{{{
# Copyright (C) 2006 OpenWrt.org
config interface loopback
        option ifname   lo
        option proto    static
        option ipaddr   127.0.0.1
        option netmask  255.0.0.0
config interface lan
        option type     bridge
        option ifname   eth0
        option proto    dhcp
        option hostname Freefonera
}}}


Edit your wireless settings using vi.

/etc/config/wireless
{{{
config wifi-device  wifi0
        option type     atheros
        option channel  5

config wifi-iface
        option device   wifi0
        option network  lan
        option mode     ap
        option ssid     Fonerafree
        option hidden   0
        option encryption psk2
        option key <Your secret password>
}}}


and finally edit your firewall settings using vi.

/etc/config/firewall
{{{
iptables -A INPUT -i br-lan -j ACCEPT
iptables -A INPUT -o br-lan -j ACCEPT
}}}
then reboot and everthing should be working.

== Correcting antenna settings under Kamikaze ==
According to [http://wiki.freifunk-hannover.de/Fonera_mit_OLSR this german Wiki entry] by default Kamikaze utilizes antenna diversity on the Fonera.
It also uses the wrong antenna :(

To change that put the following at the end of /etc/sysctl.conf:
{{{
dev.wifi0.diversity=0
dev.wifi0.rxantenna=1
dev.wifi0.txantenna=1
}}}

If you are using the Fonera to create a link over long distances, these
settings might help:

{{{
dev.wifi0.ctstimeout = 25
dev.wifi0.acktimeout = 25
dev.wifi0.slottime = 11
}}}

The tool athctrl sets values for specific distances in meters with the -d option, i.e. athctrl -d 300 sets madwifi up for a 300m link

== Resources ==
 * [http://tech.am/2006/10/06/autopsy-of-a-fonera/ Autopsy of a Fonera]
 * [http://blog.blase16.de/index.php?url=2006/11/28/Hacking-Fonera Get the SSH access to the Fonera]
 * [http://stefans.datenbruch.de/lafonera/ Hacking the La Fonera]
 * [http://forum.openwrt.org/viewtopic.php?pid=39251#p39251 Openwrt development]
 * [http://jauzsi.hu/2006/10/13/inside-of-the-fonera Picture of serial]
 * [http://www.easy2design.de/bla/?page_id=98 Debricking and more]
 * [http://www.dd-wrt.com/phpBB2/viewtopic.php?t=9011 How to get the access to Redboot without the Serial Console]
 * [http://coppercore.net/~kevin/fon/ Files to get the access to Redboot without the Serial Console]
 * [http://olsrexperiment.de/sven-ola/fonera/readme.txt Packet for Fonera by sven-ola. NOTE: If you use -ipkg remove- on the Fonera orig firmware, it will BRICK it]
 * [http://fon.rogue.be/lafonera/ Some ipkgs for the Fonera ORGINAL firmware]
 * [http://olsrexperiment.de/sven-ola/fonera/ Other ipkgs for the Fonera ORGINAL firmware]
 * [http://ecos.sourceware.org/docs-latest/redboot/redboot-guide.html Redboot userguide]
 * [http://wiki.ninux.org/moin.cgi/La_Fonera Misc Links (Italian language)]
 * [http://www.tldp.org/LDP/lkmpg/ The Linux Kernel Module Programming Guide]
 * [http://ipkg.k1k2.de/packages/ Package Repository] and Images for La Fonera (see [http://www.fonboard.de/fonera-|-anderes-betriebssystem-draufflashen-t1358-s60.html#9813 Discussion] (german))
 * [http://mobileaccess.de/fonera/bin Precompiled OpenWRT, Package Repository] and precomiled webif (ready to install) (see [http://mobileaccess.de/wlan/index.html?go=forum&action=read&msgid=10033 simple howto] for web interface installation in german)
 * [http://karman.homelinux.net/blog/ Blog about Fonera] (Spanish)
 * [http://mrmuh.blogspot.com/2007/01/codename-kolofonium-realease-date.html Blog about Hacking the 0.7.1r2 firmware] 
 * [http://blog.extreme-networking.com/ OpenWRT installation guide (Italian) and misc] 
 * [http://wiki.freifunk-hannover.de/Fonera_mit_OLSR The Fonera in the Freifunk project, german] [http://wiki.freifunk.net/Fonera_with_OLSR_(English) english]: comprehensive guide to flashing la fonera with kamikaze.
