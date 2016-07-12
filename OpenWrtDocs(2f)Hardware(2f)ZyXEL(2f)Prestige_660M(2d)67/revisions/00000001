= Prestige 660HW-61 =

This device is very similar to the Prestige 660HW-61, please see that entry for a lot of info that also applies to this model.

== Status ==

The AR7 port of OpenWRT won't start on my 660HW. I finally got so far that it no longer threw an exception on startup, it just fails silently :( I guess that BootBase sets up memory management and the caches in a way that trips the kernel up.

== Experiments ==

I tried Sun Juns barebone MIPS serial code (thanks to the guys on #openwrt for the help), but this wouldn't run either. I stripped it down to the absolute minimum, and this finally works:

{{{
loop:
      lui      v1,0x2E2E  # an ascii '.'
      li       v1,0x2E2E  # in the lower nibble too
      li      v0, 0x0000  # clear v0, just in case
      lui     v0,0xa861   
      ori     v0,v0,0xe00 # 0xa8610e00 is the location of the uart out IO
      sw      v1,(v0)     # dump the . in there

      j       loop        # and loop indefenitely
}}}

I don't know if the stack setup, cache setup or something completely different b0rks Sun's demo code.

== BootBase info ==

Zyxel apparently decided to put the AR7 CPU into big endian mode, not in little endian like with other AR7 based routers. I tried to analyze the environment BootBase offers the code it jumps to. These programs do the following:

 1. invalidate primary data and instruction cache indizes ?
 2. setting ERL, EXL and BEV in the CP0 status register - does this set the CPU into kernel mode?
 3. write 0xFFFFFFFF into the Avalanche INTC registers 0x2430 and 0x2434 (in segment 0xA861).
 4. write first 0x7777, then 0xCCCC into the watchdog reg at 0x0B10, then 0x0001 into 0x0B14
 5. Set the CP0 cause reg to 0x80
 6. Copy a bunch of stuff around
 7. Enable ints, set the IRQ mask to 00011100 and enable COPRO3 (?) through the CP0 status reg.

Does any of this make sense? Maybe an experienced AR7 veteran could help me with some of this.
