[[TableOfContents]]
= D-Link DWL-2100AP =

[http://www.dlink.com/products/?pid=292 AirPlus XtremeG Wireless Access Point]

== Hardware ==

Based on an A2 version.

 * Atheros AR2313A SoC
 * Atheros AR2112A RF
 * [http://web.icsi.com.tw/domino/packinfo.nsf/WebDSProcNum/(798C2B999CBCD0EA3FDA31D07F57CC19)?OpenDocument IC42S16800-7T] 16MB RAM
 * [http://www.amd.com/us-en/assets/content_type/white_papers_and_tech_docs/23579c6.pdf AMD AM29LV320DB] 4MB Flash
 * [http://www.icplus.com.tw/pp-IP101A.html IC+ IP101A] Ethernet transceiver
 * External antenna on RP-SMA connector
 * Internal antenna

== Interfaces ==

=== Serial ===

JP1 (12-pin, without headers) is the serial port.  It's wired very similarly to the serial port in the [:OpenWrtDocs/Hardware/Netgear/WPN824: Netgear WPN824] (also AR2313) and 
[:OpenWrtDocs/Hardware/Netgear/WGT624: Netgear WGT624] (AR231'''2''') 

{{{
       1    JP1
 VCC - [] () - VCC
  RX - () ()
       () ()
       () ()
  TX - () ()
GND? - () () - GND?
}}}

Some resistors (R264, R273, R275) are missing, so the serial port won't work.  I've bridged them with solder (since I don't have access to SMT equipment), and it seems like it's working.

=== JTAG ===

J1 (14-pin, without headers) seems to be the JTAG port.  Probably standard EJTAG 2.6 layout.

== Software ==

The AP ships with VxWorks.  Bootup is as follows:

{{{
ar531x rev 0x00005850 firmware startup...
SDRAM TEST...PASSED



  WAP-G02A  Boot Procedure                       V1.0
---------------------------------------------------------
  Start ..Boot.B12..

Atheros AR5001AP default version 3.0.0.43A


 0
auto-booting...

Attaching to TFFS... done.
Loading /fl/APIMG1...

  Please wait, loading  image ...

  image check ok!!!

/fl/  - Volume is OK
Reading Configuration File "/fl/apcfg".
Configuration file checksum: 6c9d89 is good
Attaching interface lo0...done
vxWorksTftpPackageInit: init. finish & success!
wireless access point starting...
wlan1 Ready
Ready
}}}

The boot loader can be interrupted by pressing Esc.  Initial boot settings are:

{{{
[Boot]: p

boot device          : tffs:
unit number          : 0
processor number     : 0
file name            : /fl/APIMG1
inet on ethernet (e) : 192.168.1.20:0xffffff00
flags (f)            : 0x0
other (o)            : ae
}}}
