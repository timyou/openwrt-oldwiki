= Work in Progress =
Porting OpenWrt to the DSL-320T is a work in progress.

This page is to assist those working in that direction.

== Specifications ==
ADSL modem with ADSL2/2+ support to 24Mbit/s+, it has port 1 LAN port.

Flash chip: 2MBytes

SDRAM: 8Mbytes

CPU: Texas Instruments AR7 MIPS based

== Original settings ==


The Flash memory is divided into blocks:
||||||||<style="text-align: center;">'''Default memory mappings''' ||
||Name ||Start ||End ||Description ||
||mtd0 ||0x900a1000 ||0x90200000 ||Filesystem ||
||mtd1 ||0x90020090 ||0x900a1000 ||Kernel ||
||mtd2 ||0x90000000 ||0x90010000 ||Bootloader ||
||mtd3 ||0x90010000 ||0x90020000 ||Configuration ||
||mtd4 ||0x90020000 ||0x90200000 ||Filesystem + Kernel ||

----
 . ["CategoryAR7Device"]
