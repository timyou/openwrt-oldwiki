[[TableOfContents]]

== Realtek RTL8651B SoC ==
This is a SoC with a Lexra LX5280 32-bit MIPS core, with MMU and with a 6-port fast ethernet switch, used in routers. (For more specific details, see bottom of page.)

== Earlier generations ==
1. Realtek 8181

 * Lexra LX5280 core, up to 200MHz
 * no MMU
 * two ethernet MACs, WLAN
2. Realtek 8186

 * Lexra LX5280 core, up to 200MHz
 * no MMU
 * WLAN, two UARTs, two Ethernet MACs, 4xPCM audio channels, crypto engine
3. Realtek 8650/8651

 * Lexra LX4180 core, up to 96MHz
 * no MMU
 * two UARTs, 6-port fast ethernet switch, 2 PCI, PCMCIA, USB 1.1
== Devices ==
See TableOfHardware

 * Belkin !F5D8230-4
 * Linksys WRT54GX2, WRT54GX4, [:OpenWrtDocs/Hardware/Linksys/WRT54GX:WRT54GXv2], WRV200
 * [:OpenWrtDocs/Hardware/Netgear/WPNT834:Netgear WPNT834] [http://www.netgear.com/products/details/WPNT834.php product page] (has a crippled bootloader, can't netboot)
 * Canyon CN-WF514 (version as of 2006 spring, has firmware version 1.37) - RTL8186
 * Edimax BR-6204Wg (FW compatible with the above Canyon CN-WF514) - RTL8186
 * [:OpenWrtDocs/Hardware/Asus/WL566gM:Asus WL-566gM] - RTL8651B
 * D-Link DI-624M - RTL8651B
 * D-Link DI-634M - RTL8651B
== TODO ==
 * Make a working 2.6 kernel and netboot it.
 * Find a JTAG on any of the devices to be able to make a crash recovery
== Status ==
Currently only the diff-ing is done based on 2.4.26-uc0, integration into 2.6 is in progress.

== Detailed specifications ==
 * Lexra LX5280 core, up to 200MHz
 * MMU
 * two UARTs, 6-port fast ethernet switch, 4 PCI
 * switch traffic offload, crypto engine
