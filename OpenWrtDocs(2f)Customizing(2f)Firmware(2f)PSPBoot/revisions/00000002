[[TableOfContents]]
= PSPBoot =
PSPBoot is the bootloader used on the LinkSys WAG354G, WRTP54G and [http://www.linux-mips.org/wiki/ADSL2MUE ADSL2MUE]. It is similar to the ["ADAM2"] loader.

== Startup sequence ==
{{{
free space start: 0xb0020000
free space end: 0xb0400000

Minimal POST completed...     Success.
Last reset cause: Hardware reset (Power-on reset)

PSPBoot1.2 rev: 0.22.17
(c) Copyright 2002-2004 Texas Instruments, Inc. All Rights Reserved.
FlashType:

mac_init(): Find mac [00:13:10:F9:E2:CE] in location 0
Find mac [00:13:10:F9:E2:CE] in location 0
mac_value: 00:13:10:F9:E2:CE

Press ESC for monitor... 1
(psbl)
}}}

== Available commands ==
{{{
(psbl) help
reboot            version           info              fa
printenv          setenv            unsetenv          defragenv
fmt               boot              dm                oclk
help
}}}

== Information on commands ==
{{{
(psbl) help reboot
reboot: Warm reboot the system
(psbl) help version
version: Dump build information and optional modules supported
(psbl) help info
info: Gives SoC specific information.
(psbl) help fa
fa: Displays flash allocation information
(psbl) help printenv
printenv: Print all configured system environment variables.
Usage: printenv [envlist]
(psbl) help setenv
setenv: Set a system environment variable
(psbl) help unsetenv
unsetenv: Delete a system environment variable
(psbl) help defragenv
defragenv: Defragment the system environment space
(psbl) help fmt
fmt: Erase a given area on Flash memory
Usage: fmt -a <start_address,end_address>
       fmt <env_var>

(psbl) help boot
boot: Boot the OS image according to settings in 'BOOTCFG'
(psbl) help dm
dm: Dump memory from a given address
Usage: dm [<Hex address> [num words]]
(psbl) help oclk
oclk: Configure/Dump the frequencies for CPU and System}}}

== Version ==
{{{
(psbl) version

PSPBoot 1.2.1.5
Compiled gcc rev: 2.95.3 20010315 (release/MontaVista) [May 17 2005 18:36:51]
Built for AR7WRD board in Little Endian mode.

Optional modules included (+) or not (-):
 +tibinary -elf -gzip -ffs -tftp -ftp -dhcp -pcapp
(psbl) boot
boot order: f
boot file: mtd1
}}}

== Info ==
{{{
(psbl) info

CHIP ID: TNETD73XX (0x5), REV: 0x21

MIPS Processor   : 4KEc rev: 2.2.0
Cache mode       : write-back, write-allocate.
Instruction cache: Associativity: 4, Line size: 16, Total size: 16KB
Data cache       : Associativity: 4, Line size: 16, Total size: 16KB

Last reset cause: Software reset (memory controller also reset)

EMIF is running at the same speed of the processor.
Processor running in little endian mode.
Processor clock is asynchronous to internal bus clock.
}}}

== Environment ==
{{{
(psbl) printenv

bootloaderVersion       1.2.1.5
ProductID       AR7WRD
HWRevision      Unknown
SerialNumber    none
IPA             192.168.1.1
MAC_PORT        1
SwRev           0.22.17
MEMSZ           0x1000000
FLASHSZ         0x400000
MODETTY0        38400,n,8,1,hw
MODETTY1        38400,n,8,1,hw
CPUFREQ         150000000
SYSFREQ         125000000
PROMPT          (psbl)
mtd0            0x900e0000,0x903f0000
mtd1            0x90020000,0x903f0000
mtd2            0x90000000,0x90020000
mtd3            0x903f0000,0x90400000
mtd4            0x90020000,0x903f0000
pair_selection  0
HWA_0           00:13:10:F9:E2:CE
BOOTCFG         m:f:mtd1
}}}

== Flash Allocation ==
{{{
(psbl) fa
Current Flash Allocation:

section :   PSBL, base : 0xb0000000, size :      51616 bytes
section :    ENV, base : 0xb0010000, size :      65536 bytes

unallocated Space Start: 0xb0020000
unallocated Space End  : 0xb0400000
}}}

== TFTP flashing ==
PSPBoot accepts a TFTP upload of a new firmware while beeing in command line mode or during the boot wait. The boot wait is 3 seconds by default. This creates a very narrow windows for uploading. TFTP is possible at about 2 seconds after powerup for about 1 second. With a serial console attached, it is also possible to stop the boot process by pressing ESC. The bootloader will then continue to accept uploads. The uploaded file has to be called upgrade_code.bin .

Without serial console, this procedure was successful on wag354g:

-unplug the router
-set static a configuration to the nic, with ip 192.168.1.xx(2-254) and netmask 255.255.255.0
-launch tftp:
        tftp> verbose (for debugging purpose)
        tftp> trace   ( "     "       "     )
        tftp> binary
        tftp> connect 192.168.1.1
        tftp> put upgrade_code.bin
-wait ~ 1sec.
-plug the power to the router

If transfer starts, the tftp output is like this:
....
sent DATA <block=6666, 512 bytes> 
		received ACK <block=6666> 
...

-wait until router reboots
