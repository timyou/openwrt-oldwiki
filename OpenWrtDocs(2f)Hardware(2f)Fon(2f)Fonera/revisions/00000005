[[TableOfContents]]

= Fonera =

the Fonera FON2100A is based on an Atheros System on a Chip (Soc). It got a MIPS 4KEc V6.4 processor. There is an ongoing process porting OpenWRT to this chip: AtherosPort

It's almost identical to the [http://meraki.net/mini.html Meraki Mini], who provide their own [http://www.meraki.net/linux/ openwrt fork]

== Case ==
to open the case, remove the two feet on the opposite site to the antenna jack, they'll reveal two crosspoint screws. 

== Serial ==

It got populated serial headers

    * VCC (3.3V) – red
    * GND – blue
    * RX – white
    * TX – orange

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

== Ressources ==
* [http://jauzsi.hu/2006/10/13/inside-of-the-fonera Picture of serial]
* [http://log.tigerbus.de/?p=89 unbricking]
