#pragma section-numbers off
#pragma keywords Linksys, WRT54GS
#pragma description This page contains information on the Linksys WRT54GS model router.
= Linksys WRT54GS =
There are many versions of the WRT54GS. Models up to and including version 2.1 are based on the 4712 board; they have a 200 MHz CPU, 8 MB flash and 32 MB RAM. Version 3.0 and later models use the 5352 board; these have varying amounts of flash (see the Linksys WRT54GS entries in TableOfHardware). You can get the version number from the sticker on the bottom of the device. Revisions up to 4.0 are supported by OpenWrt 1.0 (White Russian) and later. boot_wait is '''off''' by default on these routers, so you should turn it on, see OpenWrtDocs/BootWait.

== Identification by S/N ==
Useful for identifying shrinkwrapped units. The '''S/N''' can be found on the box, below the UPC barcode.
||||<style="text-align: center;"> (!) '''Please contribute to this list.''' (!) ||||||<style="text-align: center;">'''!OpenWrt''' ||
||'''Model''' ||<style="text-align: center;"> '''S/N''' ||<style="text-align: center;">'''Stable[[BR]]White Russian''' ||<style="text-align: center;">  '''Development[[BR]]Kamikaze''' ||
||<style="text-align: center;" |2>WRT54GS v1.0 ||<style="text-align: center;"> CGN0 ||<style="text-align: center;" |2> (./) ||<style="text-align: center;" |2> (./) ||
||<style="text-align: center;"> CGN1 ||
||WRT54GS v1.1 ||<style="text-align: center;"> CGN2 ||<style="text-align: center;"> (./) ||<style="text-align: center;"> (./) ||
||WRT54GS v2.0 ||<style="text-align: center;"> CGN3 ||<style="text-align: center;"> (./) ||<style="text-align: center;"> (./) ||
||WRT54GS v2.1 ||<style="text-align: center;"> CGN4 ||<style="text-align: center;"> (./) ||<style="text-align: center;"> (./) ||
||WRT54GS v3.0 ||<style="text-align: center;"> CGN5 ||<style="text-align: center;"> (./) ||<style="text-align: center;"> (./) ||
||WRT54GS v4.0 ||<style="text-align: center;"> CGN6 ||<style="text-align: center;"> (./) ||<style="text-align: center;"> (./) ||
||WRT54GS v5 ||<style="text-align: center;"> CGN7 ||<style="text-align: center;"> (./) (partial) ||<style="text-align: center;"> {X} ||
||WRT54GS v5.1 ||<style="text-align: center;"> CGN8 ||<style="text-align: center;"> (./) (partial) ||<style="text-align: center;"> {X} ||


The WRT54GS-CA is identical to the WRT54GS, but it has packaging and documentation for the Canadian market.  This serial number information applies to the WRT54GS-CA.

=== WRT54GS v1.0 ===
The WRT54GS v1.0 uses an ADM6996 switch and SDRAM.

{{{
System-On-Chip : Broadcom 4712KPB
Flash size     : 8 MB Intel
RAM            : 32 MB (2 x EtronTech EM639165TS-7, PC133/CL3 8M x 16bits SDRAM)
Wireless       : Integrated Broadcom BCM2050KML
Switch         : ADMtek ADM6996L 5 port 10/100 switch
USB            : None
Serial         : yes
JTAG           : yes
}}}
Resetting to factory defaults via reset button or mtd erase nvram is '''safe''' on this unit.

=== WRT54GS v1.1 ===
The WRT54GS v1.1 uses a BCM5325 switch and DDR-SDRAM. Resetting to factory defaults via reset button or mtd erase nvram is '''safe''' on this unit.

=== WRT54GS v2.0 ===
The WRT54GS v2.0 uses a BCM5325EKQM switch and a BCM4712LKFB processor. Resetting to factory defaults via reset button or mtd erase nvram is '''not safe''' on this unit.

=== WRT54GS v2.1 ===
The WRT54GS v2.1 also uses a BCM5325EKQM switch and a BCM4712LKFB processor. Resetting to factory defaults via reset button or mtd erase nvram is '''not safe''' on this unit.

=== WRT54GS v3.0 ===
The WRT54GS v3.0 uses a Broadcom 5352 CPU with integrated switch. Resetting to factory defaults via reset button or mtd erase nvram is '''not safe''' on this unit.

=== WRT54GS v4.0 ===
The WRT54GS v4.0 uses a Broadcom 5352 CPU with integrated switch.

{{{
Bootloader     : CFE version 1.0.37 for BCM947XX (32bit,SP,LE)
System-On-Chip : Broadcom 5352EKPB
CPU Speed      : 200 MHz
Flash size     : 4 MB (Intel TE28F320)
RAM            : 16 MB (Hynix HY5DU281622ET)
Wireless       : Integrated Broadcom BCM2050KML
Switch         : Built-in
USB            : None
Serial         : yes (JP2)
JTAG           : assumed on JP1
}}}
'''NOTE:''' v4.0 only has 4 MB Flash and 16 MB RAM. Half of prior versions. Some WRT54GS v4 has 8 MB flash and 32 MB RAM, only first relase of WRT54GS v4 had 4MB/16MB. Resetting to factory defaults via reset button or mtd erase nvram is '''safe''' on this unit.

=== WRT54GS v5 & v5.1 ===
This version has switched to a proprietary non-Linux OS (WikiPedia:VxWorks). It has less flash (2 MB) and less RAM (16 MB). The WRT54GS V5 is not officially supported, but a flashing procedure has been developed that will allow you to load a micro OpenWrt installation onto this device. For it to be of much use, packages must be pre-included in the squashfs filesystem image. For more information, see:[http://www.bitsum.com/openwiking/owbase/ow.asp?WRT54G5_CFE http://www.bitsum.com/openwiking/owbase/ow.asp?WRT54G5%5FCFE].

The flashing procedure linked to above utilizes the capability of the VxWorks boot loader to flash over itself to upload a proper CFE on this unit that then allows flashing a 'normal' TRX firmware image. The new boot loader does support all 16MB of the RAM available on GS units.

== Internal Photos ==
Hardware info with detailed pictures.

http://wiki.version6.net/WRT54GS

[http://www.linksysinfo.org/portal/forums/showthread.php?t=47124 Autopsy: Linksys WRT54G and WRT54GS Hardware Versions Under the Knife]

== Power Consumption ==
The following tests were conducted on a Linksys WRT54GS v2.0 hardware platform, hooked up to a lab PSU. All measurements are accurate +/-0.01 A

=== Normal Operation ===
In idle mode, radio off: 0.36 A In idle mode, radio on: 0.45 A

('''NOTE:''' this also means one can follow the boot process nicely from the current draw... perhaps this could be usefull in debugging? Morse error messages on the Ammeter, I think I'm getting carried away).

Inserting or retracting a networking cable gives a ~2 s peak of 0.02 A

When one lowers the input voltage, the current draw increases so the total power is always arround 5.3 W (+/-0.1 W) At arround 4 volt the router stops responding. This was tested running lots of md5sums on a file (should show memory and CPU problems). Presumably, the internal DC-DC converter can't up the voltage enough anymore at that level.

If anyone is willing to risk his router for a high-voltage measurement, let me know. (email to joris in the v5.be domain)

A WRT54GS1.1 uses AD1509 voltage regulators for the 5 V and 3.3 V rails. These have a maximum operating input voltage of 22 V so theoretically, anything below that should be ok.

=== Battery Tests ===
The measurements above show the wrt should behave exellent on batteries.

Why don't we try that in a real life test :)

I'm hooking up the wrt to a new, fully charged, 12V lead-acid car battery, rated 42 AH (skinny geeks shouldn't carry arround those kind of batteries). ... 5 days later: the Wrt behaved exellent! It remained up and running for 4 days and 13 hours on the battery. It should be noted that I measured the voltage only regularly during the first 3 days, during wich it dropped only arround 0.8 V. Presumably, the battery used is rather good at keeping the voltage...

We have run a Wrt for 6 weeks on a lead-acid battery, charger, generator combination with no problems. Power was cut due to legal problems concerning the site the AP was on. The only time the unit was down was when we had power restored.

----
 . CategoryModel
