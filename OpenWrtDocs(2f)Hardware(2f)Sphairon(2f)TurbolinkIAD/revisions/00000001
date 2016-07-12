#pragma section-numbers off
[[TableOfContents]]

= Turbolink IAD =
The Sphairon Turbolink IAD is a ADSL2+ CPE featuring 16MB RAM, 8MB flash, 4-port switch and 2 analogue and 1 S0 (with two phone connectors) phone lines.

== Status ==


== Hardware Info ==

The hardware seems to be centered around Infineons reference design for an xDSL gateway (see page 9 of http://solution.eccn.com/pdf/Infineon_063141w.pdf)

=== Photos ===


=== Disassembly notes ===

There are four clips on the sides. Once they are removed, the two halves of the case can be taken apart easily.

=== Major components ===

==== mainboard ====

 * Infineon PSB50505
  * AMAZON Family highly integrated single-chip solution for ADSL2/2+ Modems
  * 32-bit MIPS 4KEc RISC processor running at 235 MHz
  * no public documentation 
 * 2x Infineon PEB 3322 HL V1.4
  * VINETIC-2VIP Voice over IP Processor for CPE
  * Integrated voice compression Codecs: G.728, G.723.1, G.729 A/B/E, G.726 ADPCM (32, 16, 24, 40 kbit/s)
  * Line Echo Cancellation (LEC): near and far-end-echo; up to 128 ms tail; exceeding G.165/G.168/G.168-2000
  * ATM AAL2 and RTP packet processing
  * T.38 fax relay support
  * Fully programmable 2-, 4- and 8-channel CODEC
  * Specification acc. to ITU-T Q.552, G.712, LSSGR
  * AC and DC characteristic software programmable
  * Internal programmable balanced ringing up to 100 VRMS and 50 VRMS unbalanced ringing 
  * http://www.sacg.com.tw/sacweb/marcom/epaper/images/VINETIC_2VIP_ds1_v14PrelDatasheet.pdf 
 * Infineon ADM6996I
  * 6port 10/100Mb/s single chip ethernet switch controller 
 * VOGT V4  513 40 914 00
  * magnetics for ethernet 
 * 1x ESMT M12L128324A
  * 1M x 32Bit x 4 Banks SDRAM
  * http://www.elitemt.com.tw/DB/manager/upload/M12L128324A.pdf
 * 1x ST Microelectronics M29W640FB 
  * 64M 3V Supply Flash Memory
  * 8Mb x 8Bit or 4Mb x 16Bit
  * http://www.datasheet4u.com/download.php?id=548435
 * 1x Infineon PEB3086F ISAC-SX V1.4
  * ISDN subscriber access controller
  * http://www.ortodoxism.ro/datasheets/infineon/1-issx_13d.pdf 
 * 2x Infineon PEF4264 T V1.2
  * ringing SLIC with DC/DC converter 
  * http://www.infineon.com/cms/en/product/channel.html?channel=ff80808112ab681d0112ab696f5f0203

==== miniPCI slot ====

 * no miniPCI socket soldered

=== Serial Port ===
Serial Console

At connector P1:
{{{
 1   2   3   4
xxx TxD RxD GND
}}}
running at 3.3 Volt; 115200 Baud, 8N1

=== JTAG AMAZON ===

8 Pol. on left side of device:
{{{
8   7   6   5   4   3   2   1

}}}

=== JTAG VINETIC ===

There is a single pin centered on the top of the device next flash and PEB3322. This is the TD0 of the VINETIC. 
 

== PCB Photographs ==


== Bootloader ==

should be u-boot


== Firmware ==

=== Original ===

no firmware found

=== Source ===

http://www.sphairon.com/media/download/software/gpl/hansenet_2_08_1_18_tar.bz2

http://www.sphairon.com/media/download/software/gpl/uclibc_mips_toolchain_tar.bz2


== Links ==

Original information on Sphairons homepage:

http://www.sphairon.com/fld3530/fld2820/e_serv_turbolink_iad_03.html
----
 . CategoryModel 
