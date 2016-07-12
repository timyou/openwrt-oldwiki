#acl Known:read,write All:read
##
## Note: these pages document the firmware itself, not packages
##       questions/comments should be posted to the forum
##


[:OpenWrtDocs]
[[TableOfContents]]


= Failsafe mode =

If you've broken one of the startup scripts, firewalled yourself or corrupted
the JFFS2 partition, you can get back in by using !OpenWrt's failsafe mode. Full
failsafe mode is only working when you have installed one of the SquashFS images.

/!\ The act of switching between a normal boot and failsafe mode could change
your MAC address! This will invalidate the ARP cache of the workstation you're
using to access !OpenWrt with.  If you can't ping !OpenWrt at {{{192.168.1.1}}},
see the !OpenWrt [:Faq] to learn how to flush your ARP cache.


== How to get into failsafe mode ==

## TODO: The Faq article "How do I recover / boot in failsafe mode?" is redundant of this.  These need to be merged.

'''TIP:''' !OpenWrt ''itself'' uses the reset button to enter into failsafe mode, and for no other purpose.  In particular, it will ''not'' reset the NVRAM.  The ''bootloader'', however, may reset the NVRAM in response to the reset button.  Therefore, it's important to know what's running when you hold down the reset button.  One indicator is that !OpenWrt will light the DMZ LED (on systems that have one) from the time it begins until the time the bootup scripts complete.  If the DMZ LED has not yet lit up, you are still in the bootloader!

'''Linksys models'''

Plug in the router and wait for the DMZ
LED to light up.  Then immediately press and hold the reset button for 2 seconds. If
done right the DMZ LED will quickly flash 3 times every second.

/!\ Holding the reset button ''before'' the DMZ LED turns on (i.e. when the bootloader is still running) can reset the NVRAM.  Resetting the NVRAM will brick some models.

'''Non-Linksys models'''

Plug in the power, wait 2 secs, then press and hold the reset button for 10-15 seconds.

'''All Models (pre-RC5+)'''

Download and run recvudp utility.

Source code: [http://downloads.openwrt.org/people/nbd/recvudp.c recvudp.c]

Binaries:
[http://f.fainelli.free.fr/openwrt/recvudp-win32.zip Windows32]
[http://f.fainelli.free.fr/openwrt/recvudp-macosx.tar.gz MacOSX]
[http://openwrt.inf.fh-brs.de/~olli/recvudp (K)ubuntu]
[http://f.fainelli.free.fr/openwrt/recvudp-amd64.tar.gz AMD64-Linux]
[http://f.fainelli.free.fr/recvudp-linuxppc.tar.gz LinuxPPC]
[http://f.fainelli.free.fr/openwrt/recvudp-freebsd-i386.tar.gz FreeBSD]
[http://f.fainelli.free.fr/openwrt/recvudp-macosx-universal.tar.gz MacOSX-universal]

The recvudp program opens a blank window and listens on UDP port 4919.  Set the client to
a static IP in the failsafe subnet range. The router will come up as 192.168.1.1 so 192.168.1.10
for example is good. Plug in the router and wait for the go signal. Do NOT press reset before you
get this:

{{{
Msg from 192.168.1.1: Press reset now, to enter Failsafe!
}}}

Immediately press and hold the reset button for 2 seconds. If successful the following message appears:

{{{
Msg from 192.168.1.1: Entering Failsafe!
}}}

The router is now in failsafe mode.

If "Entering Failsafe!" message does not appear then you have missed the short time slot when OpenWrt can recognize the reset button (or not held down the reset button long enough).  If there are no messages (blank window) check the client's network and firewall settings to ensure that UDP port 4919 is open and accessible.

Note: This was originally followed in [https://dev.openwrt.org/ticket/255 Trac#255]

== What should I do in failsafe mode? ==

When in failsafe, the system will boot using only the files contained within
the firmware (the SquashFS partition) ignoring any changes made to the JFFS2
partition. Additionally, various network settings will be overridden forcing
the router to {{{192.168.1.1}}}. Telnet to this address will work without a 
password in this mode.

If you want to completely erase the JFFS2 partition, removing all packages, you can run {{{firstboot}}}.

If you want to attempt to fix the JFFS2 partition, mount it with the following
commands:

{{{
mtd unlock /dev/mtd/4
mount -t jffs2 /dev/mtdblock/4 /jffs
}}}

After the partition is mounted, you can edit the files in {{{/jffs}}}. If you run
firstboot with the JFFS2 partition mounted, it will not format the partition,
but it will overwrite files with symlinks. (Packages will be preserved, changes
to scripts will be lost)


= Resetting to defaults =

/!\ '''NOTE: Resetting NVRAM this way will actually cause more problems than it solves. For
example, Asus WL-500g and the Motorola WR850G bootloader will not recreate default values
and will not boot properly after being reset.
If you do this on a Siemens SE505 V1, your router will not be accessible to you anymore! You will have to reflash it with the stock firmware on ip address 192.168.1.1 (NOT 192.168.2.1 as the installation procedure says!!)'''

To clean the NVRAM variables the safe way see the !OpenWrt [:Faq].

If you're having trouble setting up some feature of your router (wireless, LAN
ports, etc) and for some reason all of the documentation here just isn't
working for you, it's sometimes best to start from scratch with a default
configuration. Sometimes the various firmwares you try will add conflicting
settings to NVRAM that will need to be flushed. Erasing NVRAM ensures there
aren't any errant settings confusing your poor confused router. Run this command
to restore your NVRAM to defaults:

{{{
mtd -r erase nvram
}}}

This will clear out the NVRAM partition and reboot ({{{-r}}}) the router, the
bootloader will create a new NVRAM partition with default settings after the
reboot. Remember to set {{{boot_wait}}} back on after you reboot your router --
trying to do it before rebooting will just write your old settings (cached in
memory) back to the flash.

To reset NVRAM settings on a Siemens SE505 V1 simply press reset after you plug it in and release as soon as one of the leds starts flashing very fast.


= Recovering from bad firmware =

See [:OpenWrtDocs/Installing] for generic installation instructions.


== Software based method ==

Reflash the unit using the TFTP method.


== Serial console ==

Important information about connecting a serial console can be found in [:OpenWrtDocs/Customizing].

Set {{{boot_wait=on}}} in CFE and then TFTP the firmware image.
To enter CFE hit {{{CTRL-C}}} right after power on.

{{{
CFE> nvram set boot_wait=on
*** command status = 0
CFE> nvram commit
*** command status = 0
CFE>
}}}

After this use the normal TFTP instructions found in [:OpenWrtDocs/Installing].

On Linksys models you can use another way too. Setup a local TFTP server on your
PC and then execute the following commands inside CFE

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

You still don't want to short any pins on your precious router. Thats nasty
disgusting behaviour. A lot better way to get a Flash into your wrecked piece
of hardware, is to build your own JTAG adaptor. It's easy, you can make it in a
jiffy using spare parts from the bottom of your messy drawer. You need:

 * 4 100R resistors
 * 1 male SUB-D 25 plug
 * If you want to do it right, a 12-way IDC-Connector plug (these are the ones
 who look like the HDD-Cables)
 * A 12-way ribbon cable for above (the JTAG cable should not exceed the length of 10 cm)
 * The boyfriend of that IDC-Connector for the PCB
 * !HairyDairyMaids [http://spacetoad.com/tmp/hairydairymaid_debrickv22.zip debrick utility]
 ([http://www.ranvik.net/prosjekter-privat/jtag_for_wrt54g_og_wrt54gs/ mirror]) or a more recent version from [http://downloads.openwrt.org/utils/ Downloads]
 and instructions how to connect everything together
 * A Linksys WRT54G/WRT54GS router with a broken flash and the desperate feeling
 that you can't make it any worse

It is basically like this:

'''NOTE:''' The diagram below is as if you were looking at your computer's
parallel port head on. If you are going to solder directly to a male connector,
pay close attention to the pin numbers as they will be in a different
orientation on the male connector. When looking at the back of the male
connector (where you solder wires to) pin 13 is on the far left, while 1 is on
the right.

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

Or a more [http://downloads.openwrt.org/inh/reference/JTAGschem.png modern version]
if you prefer.

Use the pin numbers on the parallel port connector, and the pin numbers on
the Linksys PCB, as they are all correct.

'''Note #1:''' Pin 12 is assumed to be grounded. If it is not grounded on your Linksys,
you may safely connect the wire indicated on pin 12 to any grounded even-numbered pin on
the Linksys JTAG connector.

'''Note #2:''' I had to enable ppdev in the kernel to use the program by hairydairymaid
with GNU/Linux. Working versions of the CFE can be found in
[http://downloads.openwrt.org/people/inh/cfe/ inh's] download directory, information about
changing the CFE are available at [:OpenWrtDocs/Customizing: OpenWrtDocs/Customizing].

'''Note #3:''' I had to disable i2c-parport support in my kernel - because I always got
the kernel message {{{all devices in use}}} when trying to access the parport.

Oh, and by the way, this cable is a good thing to have anyway, because many
embedded devices feature that JTAG interface e.g. HP's IPAQ has one as well, so
if you dare to open it, you can do lots of
[http://openwince.sourceforge.net/jtag/iPAQ-3600/ funky things with your IPAQ].

[http://openwince.sourceforge.net/jtag/ Openwince/JTAG] calls this cable as
"Xilinx DLC5 JTAG Parallel Cable III" but since this variant isn't buffered,
the length of this cable must not exceed 10 cm.


'''Siemens models '''

On Siemens SE505 v2 models the JTAG connector is labeled J7.
{{{
JTAG connector J7

   2   1
    o o
    o o-TDO
    o o-TDI
    o o-TCK
GND-o o-TMS
  10   9

}}}

= Problems going from JFFS2 to SquashFS or problems booting after reflashing =

/!\ '''IMPORTANT:'''  This section assumes you have taken care of backup - follow
this procedure without backing up properly first, and your JFFS2 files are
gone!

There are only two times when the JFFS2 partition gets formatted:

 * If you flash to a JFFS2 firmware, the JFFS2 partition is always formatted
 the first time the device boots (hence the extra reboot)
 * If you use SquashFS and {{{/sbin/mount_root}}} is unable to pivot the root to
 the JFFS2 filesystem

In all other instances (with the exception of failsafe), !OpenWrt will assume
that the JFFS2 partition is valid and attempt to use it. This creates a problem
when either the filesystem layout changes and the JFFS2 symlinks are invalid,
or when the JFFS2 partition has been overwritten due to a larger firmware.

There's two ways to avoid the above issue:

 * If you haven't yet reflashed, reflash using the command {{{mtd -e linux -r write openwrt-xxxx.trx linux}}}.
 The {{{-e linux}}} tells {{{mtd}}} to erase any existing data; !OpenWrt will be
 unable to find a JFFS2 partition at bootup  and the firstboot script will be
 called to create a JFFS2 partition.
 * If you have reflashed with SquashFS and the device is unbootable then what's
 happened is !OpenWrt has detected the JFFS2 partition and attempted to boot it
 and crashed. Booting into failsafe mode will allow you into the device where
 you can run {{{firstboot}}} manually.


= Getting help =

Still stuck? See [http://openwrt.org/support how to get help and support] for
information on where to get further help.
