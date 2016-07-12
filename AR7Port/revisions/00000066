[[TableOfContents]]
= Status of the AR7 port of OpenWrt =

== What is this AR7 stuff? ==

[http://focus.ti.com/pdfs/bcg/ar7wi_fact_sheet.pdf AR7]  is a router platform by Texas Instruments, which is used for routers and ADSL gateways, including
 * [http://www.seattlewireless.net/index.cgi/ActiontecGT701 Actiontec GT-701]
 * [http://www.aztech.com/DSL-600EW.htm Aztech DSL 600EW] (has USB)
 * [http://www.wehavemorefun.de/fritzbox/ AVM Fritz!Box] (German language)
 * [http://www.seattlewireless.net/index.cgi/DlinkDslG604t D-Link DSL-G604T] (and DSL-300T, DSL-302T, DSL-500T, DSL-502T, DSL-G664T)
 * !LevelOne 4-port 10/100 Mbps ADSL Router [http://www.level1.com/products3.php?sklop=12&id=560156 FBR-1416A] and [http://www.level1.com/products3.php?sklop=12&id=560157 FBR-1416B]
 * !LevelOne Wireless ADSL Router [http://www.level1.com/products3.php?sklop=12&id=540548 WBR-3407A] and [http://www.level1.com/products3.php?sklop=12&id=540549 WBR-3407B] , GPL Sourcecode for [ftp://ftp.level1.com/gpl/WBR-3407A%28GPL%29_2004-07-28.zip WBR-3407A] and [ftp://ftp.level1.com/gpl/WBR-3407B%28GPL%29_2004-07-28.zip WBR-3407B] 
 * Linksys WAG54G v2 (Note: v1 '''DOES NOT''' run Linux and is therefor unsupported)
 * Linksys [http://www.linux-mips.org/wiki/ADSL2MUE ADSL2MUE]
 * Linksys WRTP54G
 * Netcomm NB5 (Aztech DSL600EW)
 * [http://www.seattlewireless.net/index.cgi/NetgearDG834G Netgear DG834G]
 * Siemens [http://bs.netgaroo.com/sx541/ SX541] (uses realtime OS (SOHO.BIN) and BRN Boot Loader from the Broad Net Technology, Inc.)
 * Sitecom [http://www.trasduzione.com/WL-108 WL-108]
 * TCOM [http://ar7-firmware.berlios.de Sinus 154 DSL Basic SE] (uses realtime OS (SOHO.BIN) and BRN Boot Loader from the Broad Net Technology, Inc.)
 * TCOM [http://ar7-firmware.berlios.de Sinus 154 DSL Basic 3] (uses realtime OS (SOHO.BIN) and BRN Boot Loader from the Broad Net Technology, Inc.)
 * [http://www.zyxel.com/product/model.php?indexcate=1079416368&indexcate1=1021877946&indexFlagvalue=1021873638 Zyxel Prestige 660HW] (and possibly the whole 600 series)

and many more.

http://www.linux-mips.org/wiki/AR7

See [:OpenWrtDocs/InstallingAR7] if you are brave enough to test it.

== Finished tasks ==

Our Kernel support for AR7 is in SVN trunk and disabled by default.
Here's what we have integrated so far:

   * A kernel that boots up to the part where it tries to mount the root filesystem
   * A simple mtd flash map driver that uses the boot loader's partition map
   * Running a shell with a modified OpenWrt rootfs works!
   * We have working (and free) drivers for Ethernet and ADSL in SVN!
   * The flash map driver is working, but needs more testing
   * We have the source for the TI WLAN driver
   * With the new stuff in SVN, it now sets up the networking stuff, so you can log in via telnet on 192.168.1.1 (or whatever you configured in menuconfig). That can be changed in /etc/config/network
   * The VLYNQ bus works
   * The LZMA loader works and is integrated
   * Support for WAG354G is integrated, still needs testing...
   * ADSL works! New init scripts for PPPoE are integrated.
   * Scripts for flashing DSL-G664T and G604T

== Bugs / Ugly-Hacks ==

I would like to keep a list of the bugs and ugly-hacks used to make the ar7 work, so that they can be removed.

   * '''arch/mips/ar7/reset.c''': the functions are empty. Please impliment this '''without''' using the tnetd code, if possible. (reboot works now, shutdown/halt does not yet.) -- nbd: for halt, you probably only need {{{ __cli() + while(1); }}} z3ro: there are some tnetd functions for halt... hopefully we can use the code from these without needing all of the tnetd code. enrik: I have some improvements for the code including a jump back to ADAM2 on halt. Will send patch soon.

   * '''arch/mips/kernel/setup.c''': We have some #ifdef CONFIG_AR7 ... #else ... #endif because of the memory offset, we should use the generics here and modify the functions in mm/bootmem.c (this will kill some #ifdef CONFIG_AR7's in other files, too.)
   * '''arch/mips/mm/init.c''': These #ifdef CONFIG_AR7's are related to not having the proper code in mm/bootmem.c, see previous list item. enrik: I have generalized the arch/mips/kernel and .../setup code to always use the more general bootmem-functions and done some initialization cleanup, too. Will send patch soon.

   * LED/pin driver is in a mess. Proc entry is named /proc/led/led instead of /proc/led_mod/led as was in original 2.4.17_mvl21-malta-mips_fp_le kernel, writing to in does nonthing, reading leads to "Unable to handle kernel paging request" exception. Entry /proc/led_mod/ar7reset, that was present in original kernel and was reading state of "reset" pin in back of device, is completely missing.

   * Please document any more bugs/ugly-hacks found.

== TODO ==

   * Complete the init scripts, remove nvram dependencies where they are still present...
   * Test WAG354G support
   * Fix the wireless driver
   * Generalize scripts/dlink.pl so that it works with other ADAM2 versions as well (like FritzBox)

== Firmware/Bootloader ==

There are at least 3 variants

 * Telogy Networks, Inc ["ADAM2"] + Linux - most AR7 devices
 * TI PSP bootloader ["PSPBoot"] + Linux - WAG354G, WRTP54G, ADSL2MUE, maybe others?
 * Broad Net Technology, Inc. BRN bootloader and realtime OS (SOHO.BIN)

There are also at least two variants of ADAM2. My version (0.22.06) allows flashing of each mtdblock by ftp, others have reported they must flash a complete image via '''t'''ftp
TFTP is probably specific to CyberTAN-based stuff (almost exclusively Linksys). All other vendors seem to use FTP

There are two ADAM2 environment controlling boot process:

 * autoload = 0|1
 * autoload_timeout = N sec.


= How to help =

If you want to help and got some basic kernel hacking knowledge, you should start by familiarizing yourself with the OpenWrt build system. It now has support for building images for non-broadcom hardware.
All the kernel and image stuff is in the target/ subdirectory.

AR7-specific kernel patches go into {{{target/linux/linux-2.4/patches/ar7}}}. The build system part that constructs the firmware images for AR7 based routers is in {{{target/linux/image/ar7}}}. You can also find the kernel loader there.

If you'd like to help out and maybe have a patch or two, please talk to one of the developers working on this via IRC in the OpenWrt channel. Some people working on this are: nbd, wbx, wickus, z3ro, ralf, mache, and ydef.


= Other stuff =


== WAG54G Serial Console ==

{{{
|
|    __
|   |  |        <--- Pin 1: GND
|    --
|   |  |        <--- Pin 2: Not Connected
|    --
|   |  |        <--- Pin 3: Router's Serial RX
|    --
|   |  |        <--- Pin 4: Router's Serial TX
|    --
|   |  |        <--- Pin 5: VCC
|    --
|
|
 \__led__led__led__led____________________
                Front of WAG54G
}}}


The method used to find the serial port was suggested to me on irc; use a piezo buzzer and attach it's ground (usually black) wire to a ground point on the router - the back of the power regulators are usually good candidates, but check this with a multimeter/voltmeter... Use the other wire to probe any of the header pins which may be pre-installed, or any of the component holes which look like they could have header pins installed into. Once you get the right pin, the piezo should make a screeching sound much like that of a 56kbps connection.

Make sure you reset the router after probing each pin. The bootloader/linux bootup messages will only happen for a few seconds, after that the serial console will be silent - so even if you have the right pin you will not hear anything.

A more accurate method would be to use either a logic analyzer or an oscilloscope, but these are expensive and for the basic task of locating a serial pin a little overkill. ;)

Pin 5 (VCC) supports you with 3.3 V in case your serial cable needs it.[[BR]]
Terminal Settings should be: 38400 8N1, no hard- or software flow control.


== WRTP54G Serial Console ==
  

{{{________________________________________
|                                         |
|                                         led
|                   Pin 1: GND   ---> @   |
|                                         led
|         Pin 2: Not Connected   ---> @   |
|                                         led
|                   Pin 3: RX   ----> @   |                 Front of WRTP54G
|                                         led
|                   Pin 4: TX   ----> @   |
|                                         |
|                   Pin 5: VCC  ----> @   led
|                                         |
|                                         |
|                                         |
 \________________________________________|
}}}
The WRTP54G is *almost* a photo replica of the wag54gv2 hence the fccid of wag54gv2m.  The board layout differs slightly, although enough that the serial and jtag headers are positioned parallel to the front of the unit as opposed to the perpendicular alignment on the wag54gv2


== WRTP54G JTAG Pinout ==

{{{__________________________________________
|                     J3                  |
|                                         led
| Pin 1: TRST  ----> @   @ <-- Pin 2:GND  |
|                                         led
| Pin 3: TDI   ----> @   @ <-- Pin 4:GND  |
|                                         led
| Pin 5: TDO   ----> @   @ <-- Pin 6:GND  |
|                                         led
| Pin 7: TMS   ----> @   @ <-- Pin 8:GND  |   Front of WRTP54G
|                                         |
| Pin 9: TCK   ----> @   @ <-- Pin 10:GND led
|                                         |
| Pin 11:RST   ----> @   @ <-- Pin 12:NC  |
|                                         |
| Pin 13:DINT  ----> @   @ <-- Pin 14:VIO*|
 \________________________________________|

    *voltage reference @ 3.3 volts
}}}

The ar7 is based on ejtag version 2.6.

This ejtag layout should support all ar7 based boards with a 14 pin jtag pinout.  The same cable as used for the standard wrt54g (based on the xilinx III/dlc-5) as demonstrated by HairyDairyMaid can be constructed and is well documented.  Debug INT pin 13 is optional and pin 14 can be left unhooked for passive cabling.

Since DMA Routines do NOT exist for this ejtag version (compared to ejtag v2.0 supported on the wrt54g) interfacing requires a rewrite utilizng prAcc routines of the v2.6 standard.

[http://www.dlinkpedia.net/index.php/Jtag_su_30xT JTAG for D-Link DSL-30xT], [http://www.dlinkpedia.net/index.php/Interfaccia_JTAG JTAGInterface] (Italian!)

== ADSL2MUE Serial Console ==
  

{{{________________________________________
|                                         |
|                    Pin 4: GND   ----> @ |
|                    Pin 3: TX    ----> @ |
|                    Pin 2: RX    ----> @ |
|             Pin 1: + 3.3 volts  ----> @ |
|                                         |              Front of ADSL2MUE
|                                         |
|                                         led
|                                         led
|                                         led
|                                         led
|                                         led
 \________________________________________|
}}}
The console is located on the same edge that the leds are, that is, front-right side of the board. It is labeled J1 and an arrow points to pin 1 on the left, that is, the closest pin to the leds.
Voltage reference is 3.3 volts and it is set by default at 38400,8,N,1.
Mine already had a connector soldered just like to ones we usually see on computer boards as CPU/NB fan connector.


== D-Link DSL-G300T/302T/500T Serial Console ==


{{{  ___________________________________
|         Pin 1: RX      ----> []   |
|         Pin 2: GND     ----> ()   |
|         Pin 3: + 3.3 v ----> ()   |
|         Pin 4: GND     ----> ()   |
|         Pin 5: TX      ----> ()   led     Front of G300T/302T/500T
|                             JP2   |
|                                   led
|                                   |
|                                   led
|                                   led
|___________________________________|
}}}
The console is located in upper right corner, if you hold board with components to you, ethernet to left and leds to right, it's JP2, the only 5-pin 2,54mm-step connector. Usualy it is already soldered-in. Voltage reference is 3.3 volts and it is set by default at 38400,8,N,1.


== D-Link DSL-G504T/604T/664T Serial Console ==


{{{  ______________________________________
|                                      \
|                                       led
|                                       led
| Pin 5: TX      ----> ()               led
| Pin 4: GND     ----> ()               led
| Pin 3: + 3.3 v ----> ()               |
| Pin 2: GND     ----> ()               |
| Pin 1: RX      ----> []               led     Front of G504T/604T/664T
|                     JP5               |
|                                       led
|                                       |
|                                       led
|                                       led
|______________________________________/
}}}
The console is located aproximately in center of a board, it's JP5, the only 5-pin 2,54mm-step connector. Usualy it is already soldered-in. Voltage reference is 3.3 volts and it is set by default at 38400,8,N,1.


== Netgear DG834G v2 Serial Console ==


{{{ 

|                                       led
|         Pin 4: RX      ----> ()       |
|         Pin 3: NC      ----> ()       |
|         Pin 2: TX      ----> ()       |
|         Pin 1: GND     ----> []  tick led     Front of DG834G
|                           JP603       |
|                                 power led
|                                       |
|______________________________________/
}}}
The console is located roughly behind the tick led on the front left of the board, just off the edge of the MiniPCI connector. It was half hidden by the MAC
address sticker on my unit. It's the only header I could find; only 4 pins and wasn't soldered up at all. I took a voltage tap of an adjacent 74xx chip to power my MAX232. Settings are 115200,8,N,1.

== ALLNet ALL0277DSLv2 Serial Console ==

{{{

|                                                              |
|                 U2 (MAX3232?)                                |
|                                                              |
|                 === 1     16 === +3.3V                       |
|                 === 2     15 === GND                         |
|                 === 3     14 ===                             |
|                 === 4     13 ===                             |
|                 === 5     12 === CPU's RxD                   |
|                 === 6     11 === CPU's TxD                   |
|                 === 7     10 ===                             |
|                 === 8      9 ===                             |
|                                                              |
|                                                              |
|                                                              |
\___l__________________l_l_l_l__________l______l_______________/
    e                  e e e e          e      e
    d                  d d d d          d      d
}}}

Obviously, the board is prepared to be assembled with a MAX3232 or similar. The pads can either be used to directly connect a 3.3V serial cable or the missing parts (MAX3232, capacitors, resistors; have a look at the datasheet) could be soldered on the board. I chose to connect a cable directly using the pads as described above. Settings are 115200,8,N,1.
