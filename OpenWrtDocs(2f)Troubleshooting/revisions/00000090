#acl Known:read,write All:read
##
## Note: these pages document the firmware itself, not packages
##       questions/comments should be posted to the forum
##


/!\ ''' This page is currently in a clean up and reorganization process (I update it to
be more recent and more generic)''' /!\


[:OpenWrtDocs]
[[TableOfContents]]


= Failsafe mode =

If you've broken one of the startup scripts, firewalled yourself or corrupted
the JFFS2 partition, you can get back in by using !OpenWrt's failsafe mode. Remember
failsafe mode is only working when you have installed one of the SquashFS images.

/!\ The act of switching between a normal boot and failsafe mode could change
your MAC address! This will invalidate the ARP cache of the workstation you're
using to access !OpenWrt with.  If you can't ping !OpenWrt at {{{192.168.1.1}}},
see the !OpenWrt [:Faq] howto delete your ARP cache.


== Howto get into failsafe mode ==

'''Linksys models'''

To get into failsafe on Linksys models, plug in the router and wait for the DMZ
LED to light then immediately press and hold the reset button for 2 seconds. If
done right the DMZ LED will quickly flash 3 times every second.

Holding the reset button before the DMZ LED can reset NVRAM.

'''Other non-Linksys models'''

Plug in the power, wait 2 secs. Then start pressing reset button for 10-15 seconds.


== What should I do in failsafe mode? ==

When in failsafe, the system will boot using only the files contained within
the firmware (the SquashFS partition) ignoring any changes made to the JFFS2
partition. Additionally, various network settings will be overridden forcing
the router to {{{192.168.1.1}}}.

If you want to completely erase the JFFS2 partition, removing all packages you
can run {{{firstboot}}}.

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

/!\ '''NOTE:''' Resetting the NVRAM is not a good idea on every model, for
example Asus WL-500g and the Motorola WR850G bootloader will not recreate
default values, avoid deleting NVRAM.

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


= Recovering from bad firmware =

== Software based method ==

See [:OpenWrtDocs/Installing] generic installation instructions.

'''Linksys models'''

If you've followed the instructions and warnings you should have {{{boot_wait}}}
set to on. With {{{boot_wait}}} on, each time the router boots you will have
roughly 3 seconds to send a new firmware using TFTP. Use a standard TFTP client
to send the firmware in binary mode to {{{192.168.1.1}}}. Due to limitations in
the bootloader, this firmware will have to be under 3 MB in size.

'''Asus models'''

The Asus models does not have a DMZ LED. Press the reset button for 2 seconds just
after the AIR LED lights, or maybe the LAN LED. At some point it works, anyway.

Asus WL-500g units seem to respond only on the WAN port when booted in failsafe
mode. Asus WL-300g responds only on the LAN port in failsafe mode.

You can use the Asus software restoration Windows tool from the CD which comes with
the router to flash !OpenWrt TRX firmware images or restore the original firmware.

'''Motorola models'''

The Motorola WR850G may wait for an image on {{{192.168.10.1}}}.


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
 * A 12-way ribbon cable for above
 * The boyfriend of that IDC-Connector for the PCB
 * HairyD''''''airyMaids
 [http://spacetoad.com/tmp/hairydairymaid_debrickv22.zip "zip-file"] with a
 debrick utility and instructions how to connect everything together
 ([http://www.ranvik.net/prosjekter-privat/jtag_for_wrt54g_og_wrt54gs/ mirror]).
 * A Linksys WRT54G/WRT54GS router with a broken flash and the desperate feeling
 that you can't make it any worse.

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
