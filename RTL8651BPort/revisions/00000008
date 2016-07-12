[[TableOfContents]]

== Realtek RTL8651B SoC ==
This is a SoC with a Lexra LX5280 32-bit MIPS core, with MMU and with a 6-port fast ethernet switch, used in routers. Alternatively, the 818x series incorporate features suitable for SoC wireless applications. (For more specific details, see bottom of page.)


== Earlier generations ==
1. Realtek 8650/8651

 * Lexra LX4180 core, up to 96MHz
 * no MMU
 * two UARTs, 2 PCI, PCMCIA, USB 1.1
 * 6-port fast ethernet switch

2. Realtek 8181

 * Lexra LX5280 core, up to 200MHz
 * no MMU
 * UART, two ethernet MACs
 * WLAN
 
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
Realtek 8651B

 * Lexra LX5280 core, up to 200MHz
 * MMU
 * two UARTs, 4 PCI
 * 6-port fast ethernet switch
 * switch traffic offload, crypto engine

Realtek 8186

 * Lexra LX5280 core, up to 200MHz
 * MMU
 * two Ethernet MACs
 * WLAN
 * crypto engine
 * UART (second available on TFBGA package)
 * PCI interface (TFBGA package only)
 * 4xPCM audio channels (TFBGA package only)

== Resources ==

 * Source for GPLed code in Linksys WRT54GX2, WRT54GX4, and WRV200 is available from [http://www.linksys.com/servlet/Satellite?c=L_Content_C1&childpagename=US%2FLayout&cid=1115416836002&pagename=Linksys%2FCommon%2FVisitorWrapper Linksys "GPL Code Center"]
