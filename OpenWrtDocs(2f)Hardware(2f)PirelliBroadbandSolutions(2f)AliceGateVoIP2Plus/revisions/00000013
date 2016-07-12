= ALICE GATE VoIP 2 Plus Wi-Fi Business =
The web page said board AGPF-S1, but the bootloader and the tag on the image refer to AGPF-S0.
== Hardware ==
|| CPU || [http://www.broadcom.com/products/DSL/xDSL-CPE-Solutions/BCM6358 BCM6358KFBG ] ||
|| Flash || 16 MByte SPANSION [http://www.spansion.com/datasheets/s29gl-p_00_a11_e.pdf S29GL128P] ||
|| SDRAM || 32 MByte NANYA [http://www.eu.nanya.com/NanyaAdmin/GetFiles.ashx?ID=116 NT5DS16M16CS ] ||
|| LAN MAC/PHY Switch || ? ||
|| Wi Fi Card || BCM94318MPG (Chipset BCM4318) ||

== Serial Console ==
The serial port is J10, on the left of the switch chip

|| 6 || GND || RX || 5 ||
|| 4 || GND || Vcc (3.3V) || 3 ||
|| 2 || GND || TX || 1 ||

Settings are 115200 8N1

== FLASH ==

|| CFE || 128KB || 0x00000 - 0x1FFFF ||
|| FIRST IMAGE || ~8MB || 0x020000 - 0x7FFFFF ||
|| SECOND IMAGE || ~8MB || 0x800000 - 0xFDFFFF ||
|| FACTORY SETTINGS || 128KB || 0xFE0000 - 0xFFFFFF ||
 
More detailed information came from the discuss prompt:
{{{
Section 00 Type BOOT       Range 0x00000000-0x00020000 MaxSize 0x00020000
        No more information.

Section 01 Type IMAGE      Range 0x00020000-0x007C0000 MaxSize 0x0079FF6C
        Size 0x0070BC38 Name 'IMAGE'
        Checksum 0x37FE2BDA Counter 0x00000002 Start Offset 0x00000000

Section 02 Type IMAGE      Range 0x00800000-0x00FA0000 MaxSize 0x0079FF6C
        Uninitialized.

Section 03 Type CONF       Range 0x00FA0000-0x00FC0000 MaxSize 0x0001FF6C
        Size 0x0000756B Name 'rg_conf'
        Checksum 0x003A4562 Counter 0x0000002D Start Offset 0x00000000

Section 04 Type CONF       Range 0x00FC0000-0x00FE0000 MaxSize 0x0001FF6C
        Size 0x0000756B Name 'rg_conf'
        Checksum 0x003A307D Counter 0x0000002E Start Offset 0x00000000

Section 05 Type FACTORY    Range 0x00FE0000-0x00FF0000 MaxSize 0x0000FF6C
        Size 0x00000506 Name 'rg_factory'
        Checksum 0x00011485 Counter 0x0000001A Start Offset 0x00000000

Section 06 Type UNKNOWN    Range 0x00FF0000-0x01000000 MaxSize 0x00010000
}}}

I don't understand the MaxSize value of some sections as they leave some space before the next section.

Note, when you flash from jtag the BASE ADDRESS is 0x1E000000

== JATG ==
Jtag port is J9 near the Soc and the minipci socket.

It seems to be a mips e-jtag 14 pin connector with columns swapped.

|| 14 || ? DINT || VREF || 13 ||
|| 12 || ? SRST_N || GND || 11 ||
|| 10 || ? TCK || GND || 9 ||
|| 8 || ? TMS || GND || 7 ||
|| 6 || ? TDO || GND || 5 ||
|| 4 || ? TDI || GND || 3 ||
|| 2 || ? TRST_N || GND || 1 ||

CPU Chip ID: 00000110001101011000000101111111 (0635817F)

I used the JTAG port with [http://urjtag.org urjtag], just use the svn version. Useful info on [http://www.neufbox4.org/wiki/index.php?title=Interface_JTAG "Neuf Box 4 JTAG" ]

== OpenWrt on the machine :-) ==

There are some work to be done but you can boot openwrt on the router without too much problems. Just be carefull and make a backup of the flash.
You can just download the image for AGPF-S0 from [http://downloads.openwrt.org/snapshots/brcm63xx/ here], skip the jffs2 with 64k erase block as the flash use 128k block, anyway using 64k should not give much problem, just some wasted space and some errors messages. Don't use image dated 15 march 2009.

== Picture with highlighted Serial and Jtag ==

attachment:alice_agpf.jpg
