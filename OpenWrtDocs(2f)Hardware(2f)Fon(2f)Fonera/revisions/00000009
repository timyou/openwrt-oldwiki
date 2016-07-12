[[TableOfContents]]

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


== Case ==
to open the case, remove the two feet on the opposite site to the antenna jack, they'll reveal two crosspoint screws.

== Serial ==

It got populated serial headers

    * VCC (3.3V) ? red
    * GND ? blue
    * RX ? white
    * TX ? orange

If the ethernet jack is in front of you, it looks like
{{{
b . o w .
r . . . .

 O    O
}}}


Serial settings are 9600-8-N-1

I have to power the fonera up wait for a few seconds before connecting the serial cable, otherwise it doesn't boot.


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

== Updating / Unbricking via redboot ==

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
RedBoot> load -r -b 0x80041000 kernel.lzma
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


== OpenWrt ==

[https://dev.openwrt.org/changeset/5898 SVN] trunk supports this atheros SOC. thank you, nbd!


After you build a kamikaze image with svn trunk for the atheros-2.6 target, you get the following files in your ./bin/ directory:

{{{
openwrt-atheros-2.6-root.jffs2-128k
openwrt-atheros-2.6-vmlinux.elf
openwrt-atheros-2.6-vmlinux.lzma
openwrt-atheros-2.6-root.jffs2-64k
openwrt-atheros-2.6-vmlinux.gz
packages/
}}}

It's important to use the files in ./bin/ and NOT ./build_mips/linux-2.6-atheros/vmlinux.bin.l7
It took me quite some time to figure out why this vmlinux.bin.l7 doesn't work.

The magic is, that ./target/linux/atheros-2.6/image/Makefile converts the image with:
{{{
dd if=$(KDIR)/vmlinux.bin.l7 of=$(BIN_DIR)/openwrt-$(BOARD)-$(KERNEL)-vmlinux.lzma bs=65536 conv=sync
}}}
where conv=sync pads every input block with NULs to ibs-size, which is needed!


Copy openwrt-atheros-2.6-vmlinux.lzma and openwrt-atheros-2.6-root.jffs2-64k to /tftpboot/ and flash them like this:
{{{
^C
RedBoot> ip_address -l 192.168.5.75/24 -h 192.168.5.2
IP: 192.168.5.75/255.255.255.0, Gateway: 0.0.0.0
Default server: 192.168.5.2
RedBoot> load -r -b 0x80041000 openwrt-atheros-2.6-vmlinux.lzma
Using default protocol (TFTP)
Raw file loaded 0x80041000-0x800f0fff, assumed entry at 0x80041000
RedBoot> fis create -r 0x80041000 -e 0x80041000 vmlinux.bin.l7
An image named 'vmlinux.bin.l7' exists - continue (y/n)? y
... Erase from 0xa8730000-0xa87e0000: ...........
... Program from 0x80041000-0x800f1000 at 0xa8730000: ...........
... Erase from 0xa87e0000-0xa87f0000: .
... Program from 0x80ff0000-0x81000000 at 0xa87e0000: .
RedBoot>  load -r -v -b 0x80041000 openwrt-atheros-2.6-root.jffs2-64k
Using default protocol (TFTP)
|
Raw file loaded 0x80041000-0x80200fff, assumed entry at 0x80041000
RedBoot> fis create -b 0x80041000 -f 0xA8030000 -l 0x00700000 -e 0x00000000 rootfs
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


== Telnet into Redboot ==

You can change the redboot configuration, so you can later telnet into this bootmanager in order to reflash this device from there, without having serial access.

To do this, run fconfig like this from the redboot prompt:

{{{
RedBoot> fconfig
Run script at boot: true
Boot script:
.. fis load -l vmlinux.bin.l7
.. exec
Enter script, terminate with empty line
>> fis load -l vmlinux.bin.l7
>> exec
>>
Boot script timeout (1000ms resolution): 10
Use BOOTP for network configuration: false
Gateway IP address:
Local IP address: 192.168.5.22
Local IP address mask: 255.255.255.0
Default server IP address: 192.168.5.2
Console baud rate: 9600
GDB connection port: 9000
Force console for special debug messages: false
Network debug at boot time: false
Update RedBoot non-volatile configuration - continue (y/n)? y
... Erase from 0xa87e0000-0xa87f0000: .
... Program from 0x80ff0000-0x81000000 at 0xa87e0000: .
RedBoot>
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

Actually I had problems with my old BSD telnet on slackware 11 to send a proper ctrl-c to the redboot gdb console.
I circumvented the problem with this small trick:

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

The boot process is somehow signalled via the leds, first only the power led is on, then the internet led starts blinking, and when this internet led is solid green, it's the right time to connect to the gdb console.

This is the point, where I disconnected the serial cable and closed the case. If the kernel is booting and ssh working, I don't need any debug-stuff in between. It's possible to unbrick the fonera with this redboot gdb console, as I can always reflash to a working firmware.

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

This should be possible (but is untested right now and my really brick your fonera!) like this:
{{{
root@OpenWrt:~# mtd write /tmp/redboot_config "RedBoot config"
}}}


You can find some informations about the openwrt development on this device [http://forum.openwrt.org/viewtopic.php?pid=39251#p39251 here].

== Ressources ==
* [http://jauzsi.hu/2006/10/13/inside-of-the-fonera Picture of serial]
* [http://log.tigerbus.de/?p=89 unbricking]
