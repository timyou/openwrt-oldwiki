{{{
RedBoot> fis init
About to initialize [format] FLASH image system - continue (y/n)? y
*** Initialize FLASH Image System
    Warning: device contents not erased, some blocks may not be usable
... Unlock from 0x50fe0000-0x51000000: .
... Erase from 0x50fe0000-0x51000000: .
... Program from 0x03fdf000-0x03fff000 at 0x50fe0000: .
... Lock from 0x50fe0000-0x51000000: .
RedBoot> fis list
Name              FLASH addr  Mem addr    Length      Entry point
RedBoot           0x50000000  0x50000000  0x00040000  0x00000000
RedBoot config    0x50FC0000  0x50FC0000  0x00001000  0x00000000
FIS directory     0x50FE0000  0x50FE0000  0x00020000  0x00000000
}}}

{{{
RedBoot> load -r -b %{FREEMEMLO} -m ymodem
Raw file loaded 0x0001c800-0x0002815f, assumed entry at 0x0001c800
xyzModem - CRC mode, 373(SOH)/0(STX)/0(CAN) packets, 3 retries
RedBoot> fis create -b %{FREEMEMLO} -l 0x2000 -f 0x50fa0000 -e %{FREEMEMLO} -r %{FREEMEMLO} apex
argc is 13
... Erase from 0x50fa0000-0x50fc0000: .
... Program from 0x0001c800-0x0001e800 at 0x50fa0000: .
... Unlock from 0x50fe0000-0x51000000: .
... Erase from 0x50fe0000-0x51000000: .
... Program from 0x03fdf000-0x03fff000 at 0x50fe0000: .
... Lock from 0x50fe0000-0x51000000: .
RedBoot> fis load apex
RedBoot> go
Ans

APEX Boot Loader 1.5.14 -- Copyright (c) 2004,2005,2006,2007 Marc Singer
  compiled for SlugOS NAS100D/BE on 2009.Jan.13-06:05:26

    APEX comes with ABSOLUTELY NO WARRANTY.  It is free software and
    you are welcome to redistribute it under certain circumstances.
    For details, refer to the file COPYING in the program source.

  apex => mem:0x00200000+0xb960   (47456 bytes)
  env  => nor:0xfbc000+15k        (empty)

    Use the command 'help help' to get started.

# sdram-init
 1 bank of 2 256Mib chips
# memscan -u 0+256m
 0x0 0x04000000 (64 MiB)
# copy $kernelsrc $bootaddr
# copy fis://kernel 0x00400000
Unable to open 'fis://kernel'
Error -14 (partition not found)
apex> 
}}}



CategoryModel
CategoryIXP4xxDevice
