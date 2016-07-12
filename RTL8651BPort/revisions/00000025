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

 * [:OpenWrtDocs/Hardware/Asus/WL566gM:Asus WL-566gM] - RTL8651B
 * Belkin !F5D8230-4
 * Canyon CN-WF514 (version as of 2006 spring, has firmware version 1.37) - RTL8186
 * D-Link DI-524UP - RTL8650B [http://www.dlink.ca/products/?pid=316 product description] [ftp://ftp.dlink.co.uk/GPL/DI-524UP_GPL.tar.gz Firmware source code] [http://ossfans.org/DI524UP/ Firmware investigation project]
 * D-Link DI-624M - RTL8651B
 * D-Link DI-624S - RTL8651B [ftp://ftp.dlink.com/GPL/DI-624S/DI-624s_v100036.tgz Firmware source code GPL]
 * D-Link DI-634M - RTL8651B
 * Edimax BR-6204Wg (FW compatible with the above Canyon CN-WF514) - RTL8186
 * Edimax IC-1500 - RTL8651B [http://www.edimax.com/en/produce_detail.php?pd_id=54&pl1_id=8&pl2_id=35 product description] [http://www.edimax.com/images/Image/OpenSourceCode/Wireless/IPCamera/IC-1500wg/IC1500_RTL865X.tar.gz Firmware source code] (IP Web-camera)
 * Linksys WRT54GX2, WRT54GX4, [:OpenWrtDocs/Hardware/Linksys/WRT54GX:WRT54GXv2], WRV200
 * [:OpenWrtDocs/Hardware/Netgear/WPNT834:Netgear WPNT834] [http://www.netgear.com/products/details/WPNT834.php product page] (has a crippled bootloader, can't netboot)

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

In many cases the manufacturers have based their firmware on ucLinux.  Any binary-only drivers meant for ucLinux are not compatible with any OpenWRT kernel.  This creates a serious barrier to porting OpenWRT to these platforms.  The main technical advantage of ucLinux is not requiring an MMU but these platforms do have an MMU (as outlined above).

Source Code for Manufacturers' Firmware is available from:

 * [:OpenWrtDocs/Hardware/Asus/WL566gM:Asus WL-566gM] [http://dlsvr01.asus.com/pub/ASUS/wireless/WL-566gM/GPL_WL566gM_1018.zip]
 * Belkin F5D8230-4 [http://www.belkin.com/support/gpl.asp]
 * Canyon [http://www1.canyon-tech.com/products/show.cfm/Networking/Net/Wireless_Products_IEEE_802.11g/CN-WF514/Down CN-WF514]
 * D-Link DI-524UP - RTL8650B [ftp://ftp.dlink.co.uk/GPL/DI-524UP_GPL.tar.gz]
 * D-Link DI-624M [http://support.dlink.com/faq/print.asp?productid=2081]
 * D-Link DI-624S (Rev B1) [http://www.dlink.com.au/Products.aspx?Sec=1&Sub1=2&Sub2=5&PID=64] [ftp://ftp.dlink.com/GPL/DI-624S/DI-624s_v100036.tgz Firmware source code GPL]
 * D-Link DI-634M [http://www.dlink.com.au/tech/Download/download.aspx?product=DI-634M&revision=REV_A&filetype=Firmware]
 * Edimax BR-6204Wg [http://www.edimax.com.tw/html/english/frames/b-download.htm]
 * Edimax IC-1500 [http://www.edimax.com/images/Image/Firmware/Wire/IPCamera/IC-1500/IC-1500_1.28.zip]
 * Linksys WRT54GX2, WRT54GX4, and WRV200 [http://www.linksys.com/servlet/Satellite?c=L_Content_C1&childpagename=US%2FLayout&cid=1115416836002&pagename=Linksys%2FCommon%2FVisitorWrapper Linksys "GPL Code Center"]
 * Netgear WPNT834 & KWGR614 [http://kbserver.netgear.com/kb_web_files/n101238.asp Netgear "Open Source Code for Programmers"]

Working(?) free firmware : http://inbox.eu.org/

Info at [http://www.linux-mips.org www.linux-mips.org]:
 * [http://www.linux-mips.org/wiki/Lexra Lexra]
 * [http://www.linux-mips.org/wiki/Realtek_SOC Raltek SOCs]

Investigation of DI-524UP: http://ossfans.org/DI524UP/
