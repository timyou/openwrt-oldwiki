= ALICE GATE VoIP 2 Plus Wi-Fi Business board AGPF-S0 =
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
Until I post some more information take a look at this  [http://forum.openwrt.org/viewtopic.php?pid=78247#p78247 thread]
