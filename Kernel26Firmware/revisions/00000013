= Linux 2.6 Firmware Page =

This page is dedicated to the creation of an experimental 2.6 kernel release.

== Finished tasks ==

 * Kernel26 wiki page ;)

== TODO in order of priority ==

 * '''A linux userspace boot loader [MipsExec]'''

 It would be nice if we could do something like '''mipsexec params.txt''' (with kernelimage and initrd files) on the command prompt without the need for reflashing.

 * '''A kernel26 development tree in CVS'''

 In cooperation with [http://handhelds.org/cgi-bin/cvsweb.cgi/linux/kernel26/] or [http://www.linux-mips.org/cvsweb/linux/]

 * '''Setup of a basic structure for broadcom architecture [LinuxMipsCodingGuidelines]'''

 arch/mips/mips-boards/broadcom/platform-asus.c ...

 * '''Find out if we can use the SOC abstraction layer for Silicon Backplane'''

 Comments by andy (linux-mips mailing list):

 The Silicon Backplane bus actually came from another company, it wasn't
 defined by Broadcom; google knows all: [http://www.ocpip.org/socket/adoption/sonics]
 
 I think there are other OCP busses supported in the kernel; ISTR seeing
 some PPC SoC from IBM that uses OCP... so perhaps this should be brought
 up on l-k for general discussion.
 
 But it's challenging to come up with a useful abstraction that covers
 both the b44 scenario and the SoC scenario.

   - for b44, OCP is on the far side of the PCI bus, and is used only to
     access a single core (ethernet MAC).
 
   - for bcm947xx (and ppc SoC, I guess), OCP is the system bus, and is
     used to access everything from PCI to DRAM.
 
 grep grep grep... Take a look at include/asm-ppc/ocp.h and arch/ppc/platforms/*.c, it looks like the PowerPC people have already done a bunch of work here.

 Also of interest may be the new SOC abstraction on the hh.org branch, see [http://handhelds.org/cgi-bin/cvsweb.cgi/linux/kernel26/Documentation/soc.txt]


 * '''A 2.6 port of the ethernet/switch driver.'''

 This should be relatively straight forward considering we have the source for the '''et''' module.
 See: [http://funke.lo-res.org/linksys/]
 Probably for the ethernet part we could also copy or reuse the regular '''b44''' driver code.

 * '''A 2.6 port of the wlan driver.'''

 There is already a very promising Broadcom WLAN driver project at [http://sourceforge.net/projects/linux-bcom4301/], they document the chipsets specifications.
 The actual specifications can be found at [http://bcm-specs.sipsolutions.net] and the project which actually writes the driver at [http://bcm43xx.berlios.de/].

 * '''use some binary driver from broadcom 2.6 tree.'''
 ftp://ftp.gpl-devices.org/pub/vendors/Hitachi/AH4021/AH4021-firmware-v36.tar.gz is a 2.6.8 kernel with some broadcom binaries :
 {{{
bcmdrivers/broadcom/atm/impl1/blaadd96348GWV.o_save
bcmdrivers/broadcom/char/adsl/impl1/adsldd96348GWV.o_save
bcmdrivers/broadcom/char/atmapi/impl1/atmapi96348GWV.o_save
bcmdrivers/broadcom/char/bcmprocfs/impl1/bcmprocfs96348GWV.o_save
bcmdrivers/broadcom/net/enet/impl2/bcm_enet96348GWV.o_save
bcmdrivers/broadcom/net/usb/impl2/bcm_usb96348GWV.o_save
bcmdrivers/broadcom/net/wl/impl1/wl96348GWV.o_save
}}}

/!\ As there is no contact info here, I've put this here as a sidenote - check Jolt's 2.6 port - http://cvs.berlios.de/cgi-bin/viewcvs.cgi/tuxap/kernel/ - Kaloz

== A more specific TODO ==

The idea is here merge the Broadcom stuff with the linux-mips kernel. Here's a quick comparison, on file level, with some specific hints on how to migrate.

{{{
Files found in the openwrt distribution and not in the linux-mips-2.6 distro
with number of words containing broadcom...

These probably need some inspection when moving to 2.6

I don't pretend this is a complete list nor do I pretend all comments are
correct. So please feel free to fill in the blanks or make suggestions.


> ./arch/mips/mm/c-r4k.c:1
- Adapt: enable icaches & dcaches for BCM chips?

> ./arch/mips/kernel/cpu-probe.c:3
- Adapt: enable cpu-probe for broadcom chipsets

> ./arch/mips/brcm-boards/bcm947xx/sbpci.c:4
> ./arch/mips/brcm-boards/bcm947xx/sbmips.c:13
> ./arch/mips/brcm-boards/bcm947xx/setup.c:5
> ./arch/mips/brcm-boards/bcm947xx/perfcntr.c:4
> ./arch/mips/brcm-boards/bcm947xx/gpio.c:3
> ./arch/mips/brcm-boards/bcm947xx/prom.c:3
> ./arch/mips/brcm-boards/bcm947xx/time.c:3
> ./arch/mips/brcm-boards/bcm947xx/nvram.c:3
> ./arch/mips/brcm-boards/bcm947xx/pcibios.c:5
> ./arch/mips/brcm-boards/bcm947xx/sflash.c:4
> ./arch/mips/brcm-boards/bcm947xx/nvram_linux.c:3
> ./arch/mips/brcm-boards/generic/irq.c:4
> ./arch/mips/brcm-boards/generic/int-handler.S:4
> ./arch/mips/brcm-boards/generic/gdb_hook.c:3

- Migrate ...

> ./drivers/net/hnd/bcmutils.c:3
> ./drivers/net/hnd/hnddma.c:4
> ./drivers/net/hnd/bcmsrom.c:3
> ./drivers/net/hnd/sbutils.c:5
> ./drivers/net/hnd/linux_osl.c:3
> ./include/bcmutils.h:3
> ./include/hndmips.h:3
- Broadcom library routines like CRC functions these should probably be
 migrated to the corresponding linux functions. Or should be moved in the
 apecific architecture or driver folders.
 Also there's some code bloat that enables the inclusion in other OS's
 this should probably be removed.

> ./drivers/mtd/maps/bcm947xx-flash.c:3
- Migrate, How to handle this in 2.6?

> ./include/sflash.h:4
- Move to include/linux/mtd/ ?

> ./drivers/mtd/devices/sflash.c:5
- Migrate, "Silicon backplane" routines for flash access.

> ./drivers/pci/devlist.h:3
- Probably this is obsolete now.

> ./drivers/pcmcia/bcm4710_pcmcia.c:4
> ./drivers/pcmcia/bcm4710_generic.c:4
> ./drivers/pcmcia/bcm4710pcmcia.h:3
- Migrate

> ./include/bcmnvram.h:3
- Defines for nvram get/set functions (like sdram settings) a lot of these parameters should probably go to the board specific initialization code.
For example in arch/misp/xxxx/board-asus-500gx.c ../board-linksys-wrtxxx.c )

> ./include/osl.h:3
> ./include/proto/ethernet.h:6
> ./include/proto/802.11.h:3
> ./include/hnddma.h:4
> ./include/sbpci.h:3
> ./include/bcmenetmib.h:4
> ./include/bcmenetrxh.h:4
> ./include/sbmemc.h:3
> ./include/sbmips.h:5
> ./include/trxhdr.h:3
> ./include/bcmdevs.h:7
> ./include/sbsdram.h:3
> ./include/sbutils.h:4
> ./include/sbconfig.h:5
> ./include/bcmendian.h:3
> ./include/bcmenet47xx.h:4
> ./include/pcicfg.h:3
> ./include/bcmsrom.h:3
> ./include/sbextif.h:3
> ./include/typedefs.h:3
> ./include/bcm4710.h:3
> ./include/linuxver.h:3
> ./include/linux_osl.h:3
- TODO Probably allot of BCM specific code need to be moved in driver or
  the specific arch dir.
  Also there's some code bloat that enables the inclusion in other OS's

- TODO Probably allot of BCM specific code need to be moved in driver or
  the specific arch dir.
  Also there's some code bloat that enables the inclusion in other OS's
  this should probably be removed.

> ./include/asm-mips/bootinfo.h:2
- Update with BCM machine types...
}}}
