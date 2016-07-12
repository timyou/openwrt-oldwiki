= Prestige 660HW-61 =

The device is based on Texas Instruments [http://www.linux-mips.org/wiki/AR7 AR7], so you need the [:AR7Port] in OpenWrt trunk.
It uses [:Bootbase] as the bootloader. There are detailed guides how to flash the firmware available [http://www.adslayuda.com/Zyxel650-9.html here] (spanish) [http://www.stkaiser.de/anleitung/ here] (german) and [http://www.dslrouter-hilfe.de/forum/showpost.php?p=49041&postcount=36 here] (german).

== Status ==

[http://www.ixo.de/info/zyxel_uclinux/ Kolja Waschk] had success booting uClinux kernel on previous ZyXEL Prestige router series (100, 310, 314, 316) and others.

== Serial Console ==

You can build a serial cable using various mobile cables as shown [http://www.adslayuda.com/index.php?name=PNphpBB2&file=viewtopic&t=53480 in this forum post] (spanish) and [http://www.stkaiser.de/anleitung/data/01_usb.html on this page] (german).

This way, you don't need to buy a [http://www.adslayuda.com/ar03/img/rs232_zyxel_prestige_660hw-61.jpg MAX232 chip] plus capacitors to do the TTL level conversion.

I used a SIEMENS S55 slim lumberg [http://pinouts.ru/data/siemens_c55_pinout.shtml cable] to do the trick.

/!\ '''DO NOT try to connect your PC's serial port to the router directly !'''

=== Router startup through serial console ===

{{{
Bootbase Version: V1.06 | 04/01/2004 11:22:33
RAM: Size = 16384 Kbytes
DRAM POST: Testing: 16384K
OK
FLASH: Intel 16M *1

ZyNOS Version: V3.40(PE.7) | 09/29/2004  17:42:50

Press any key to enter debug mode within 3 seconds.
................<ENTER>
Enter Debug Mode
}}}

=== Enabling privileged commands ===

Thanks (again) to adslayuda for the [http://www.adslayuda.com/Zyxel650-9.html howto] on the password algorithm. The following code can be used to compute it:

{{{

/* ZyXEL prestige 660HW series password calculator by brainstorm <brainstorm at nopcode org>
 * Thanks to http://www.adslayuda.com/Zyxel650-9.html authors
 *
 * Example usage:
 *
 * Router:
 * ======
 *
 * ATSE
 * 0028D6DF1C03
 * OK
 *
 * Computer:
 * ========
 *
 * ./zyxel 0028D6DF1C03
 * ATEN 1,221E3111
 *
 * Router:
 * ======
 * ATEN 1,221E3111
 * OK
 *
 * "Dangerous" commands enabled :-)
 *
 * */

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define magic1  0x10F0A563L
#define magic2  7
#define atse_length 12  /* ATSE command, ZyNOS seed password length */

#define WORD_LENGTH (8*sizeof(value))
int ror(unsigned int value, int places)
{
  return (value>>places)|(value<<(WORD_LENGTH-places));
}


int main (int argc, char* argv[]) {

        char *seed, a[7], c[3];
        unsigned int b,d,e,password;

        if ( argc != 2 ) {
                printf("Only one argument is permitted: 00BDC8667E5B\n");
                exit(-1);

        } else if ( strlen(argv[1]) != atse_length ) {
                printf( "Incorrect parameter length, should be %d characters long\n", atse_length );
                exit (-2);
        }

        seed = argv[1];

        strncpy (a, seed , 6);  //a="ersten" 3Bytes vom seed
        e = strtol(a,NULL,16);  //e=a

        strncpy (c, seed + strlen(seed)-2, 2); //c= last 2 bytes of seed?
        d = strtol(c,NULL,16) & magic2; //d="last byte" AND 7
        b = e + magic1; //

        b = ror(b,d);
        password = b ^ e;
        printf("\nATEN 1,%X\n", password);

        return 0;
}


}}}

There is also a small windows tool called [http://www.adslayuda.com/descargas/routers/zyxel650/configuracion/ZynPass1.2.zip ZynPass] which calculates the password.


== Memory layout ==

Bootbase provides a powerful flashing/debugging console, for instance, the ATMP command shows us how is the memory allocated. Later on, you can use the ATDUx,y command to dump memory contents starting at x plus an y offset:

{{{
ATMP

ROMIO image start at b0010000
code version:
code start: 94008000
code length: 1C3D24
memMapTab: 14 entries, start = b0037000, checksum = A88D
$RAM Section:
  0: BootExt(RAMBOOT), start=94008000, len=38000
  1: HTPCode(RAMCODE), start=94020000, len=E0000
  2: RasCode(RAMCODE), start=94020000, len=FE0000
$ROM Section:
  3: BootBas(ROMIMG), start=b0000000, len=4000
  4: DbgArea(ROMIMG), start=b0004000, len=2000
  5: RomDir2(ROMDIR), start=b0006000, len=A000
  6: BootExt(ROMIMG), start=b0010030, len=17FD0
  7: HTPCode(ROMBIN), start=b0028000, len=F000
          (Compressed)
          Version: HTP_P660 V 0.05, start: b0028030
          Length: 17618, Checksum: 3B6A
          Compressed Length: 7F07, Checksum: 64E7
  8: MemMapT(ROMMAP), start=b0037000, len=C00
  9: termcap(ROMIMG), start=b0037c00, len=400
 10: tiadsl(ROMBIN), start=b0038000, len=24A00
          (Compressed)
          Version: ADSL ATU-R, start: b0038030
          Length: 40736, Checksum: 9761
          Compressed Length: 2242D, Checksum: 6E3D
 11: tiwlan(ROMBIN), start=b005ca00, len=1BC00
          (Compressed)
          Version: WLAN, start: b005ca30
          Length: 12894, Checksum: 539D
          Compressed Length: C1A0, Checksum: 4883
 12: RomDefa(ROMIMG), start=b0078600, len=A000
 13: RasCode(ROMBIN), start=b0082600, len=17DA00
          (Compressed)
          Version: P660HW-61 ATU-R, start: b0082630
          Length: 446098, Checksum: 321B
          Compressed Length: 151724, Checksum: 7D74
}}}

For instance, ATDU b0037c00,400 will produce the following output (refer to the "termcap" entry above for memory address and length):

{{{
B0037C00: 76 74 31 30 30 7C 64 65-63 2D 76 74 31 30 30 7C   vt100|dec-vt100|
B0037C10: 76 74 31 30 30 2D 61 6D-7C 76 74 31 30 30 61 6D   vt100-am|vt100am
B0037C20: 7C 64 65 63 20 76 74 31-30 30 3A 5C 0D 0A 09 3A   |dec vt100:\...:
B0037C30: 64 6F 3D 5E 4A 3A 63 6F-23 38 30 3A 6C 69 23 32   do=^J:co#80:li#2
B0037C40: 34 3A 63 6C 3D 35 30 5C-45 5B 3B 48 5C 45 5B 32   4:cl=50\E[;H\E[2
B0037C50: 4A 3A 73 66 3D 32 2A 5C-45 44 3A 5C 0D 0A 09 3A   J:sf=2*\ED:\...:
B0037C60: 6C 65 3D 5E 48 3A 62 73-3A 61 6D 3A 63 6D 3D 35   le=^H:bs:am:cm=5
B0037C70: 5C 45 5B 25 69 25 64 3B-25 64 48 3A 6E 64 3D 32   \E[%i%d;%dH:nd=2
B0037C80: 5C 45 5B 43 3A 75 70 3D-32 5C 45 5B 41 3A 5C 0D   \E[C:up=2\E[A:\.
B0037C90: 0A 09 3A 63 65 3D 33 5C-45 5B 4B 3A 63 64 3D 35   ..:ce=3\E[K:cd=5
B0037CA0: 30 5C 45 5B 4A 3A 73 6F-3D 32 5C 45 5B 37 6D 3A   0\E[J:so=2\E[7m:
B0037CB0: 73 65 3D 32 5C 45 5B 6D-3A 75 73 3D 32 5C 45 5B   se=2\E[m:us=2\E[
B0037CC0: 34 6D 3A 75 65 3D 32 5C-45 5B 6D 3A 5C 0D 0A 09   4m:ue=2\E[m:\...
B0037CD0: 3A 6D 64 3D 32 5C 45 5B-31 6D 3A 6D 72 3D 32 5C   :md=2\E[1m:mr=2\
B0037CE0: 45 5B 37 6D 3A 6D 62 3D-32 5C 45 5B 35 6D 3A 6D   E[7m:mb=2\E[5m:m
B0037CF0: 65 3D 32 5C 45 5B 6D 3A-69 73 3D 5C 45 5B 31 3B   e=2\E[m:is=\E[1;
< Press any key to Continue, ESC to Quit >
}}}

== Original Firmware files ==

[ftp://ftp.europe.zyxel.com/P660HW-61/firmware/P660HW-61_V3.40(PE.10)C0_Standard.zip Firmware] downloaded from official ZyXEL website:

'''340PE10C0.rom:''' Router configuration, coincides with "4: DbgArea" shown above. You can retrieve this file from your router using the ATTD [:BootBase] command.
'''340PE10C0.bin:''' Router firmware.

== Flashing BootBase ==

The following process rewrites the BootBase bootloader. It's just a translation from adslayuda mentioned earlier, thanks to "haypocos" for this procedure. This instructions may be
useful to these brave enough to flash a new bootloader on top of BootBase.

/!\ '''DO NOT try this unless you know what it's all about'''
/!\ '''Really, DON'T, it's gonna brick your router'''

ATEN stuff
ATBA4: Sets baudrate to 57.6k to speedup Xmodem download
ATDO BFC00000,6C5D0: Downloads the bootbase and extensions for backup purposes
<XMODEM transfer>
ATBT1: Block 0 unprotected, we are going to overwrite the bootloader
ATUX 0: Actual bootloader upload and writing
<XMODEM transfer>

----
CategoryModel ["CategoryAR7Device"]
