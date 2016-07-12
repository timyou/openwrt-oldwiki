= Linux 2.6 Firmware Page =

This page is dedicated to the creation of an experimental 2.6 kernel release.

== Finished tasks ==

 * Kernel26 wiki page ;)

== TODO in order of priority ==

 * '''A linux userspace boot loader [MipsExec]'''

 It would be nice if we could do something like '''mipsexec params.txt''' (with kernelimage and initrd files) on the command prompt without the need for reflashing.

 * '''A kernel26 development tree in CVS'''

 In cooperation with [http://handhelds.org/cgi-bin/cvsweb.cgi/linux/kernel26/] or [http://www.linux-mips.org/cvsweb/linux/]

 * '''Setup of a basic stucture for broadcom architecture [LinuxMipsCodingGuidelines]'''

 arch/mips/mips-boards/broadcom/platform-asus.c ...

 * '''A 2.6 port of the ethernet/switch driver.'''

 This should be relatively straight forward considering we have the source for the '''et''' module.
 See: [http://funke.lo-res.org/linksys/]
 Probably for the ethernet part we could also copy or reuse the regular '''b44''' driver code.

 * '''A 2.6 port of the wlan driver.'''

 There is already a very promising Broadcom Wlan driver project at [http://sourceforge.net/projects/linux-bcom4301/].

== A more specific TODO ==

The idea is here merge the Broadcom stuff with the linux-mips kernel. Here's a quick comparison with some specific hints on how to migrate.

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

- Migrate: Should we cluster this with the sibyte stuf? Probably
there's some shared code....

   so migrate dir structure from:
        arch/mips/sibyte/cfe
        arch/mips/sibyte/swarm
        arch/mips/sibyte/sb1250
   to:
        arch/mips/broadcom/cfe
                           sb1
                           swarm
                           sb1250
                           bcm947xx
                           generic


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

Silicon BackplaneeEthernet driver/API:
 It looks like most broadcom drivers (even the b44) use a broadcom specific
 bus. Maybe we could generalise this in a specific SiliconBackplane api.


Ethernet driver and switch chip:
 see: [http://funke.lo-res.org/linksys/]
 Probably the ethernet part could be integrated or forked off using the regular
 b44 driver.

Wlan driver:
 see: [http://cvs.sourceforge.net/viewcvs.py/linux-bcom4301/src/]

}}}
