'''Linksys WRTSL54GS'''

[[TableOfContents]]
= Hardware versions =
There is only one version of the WRTSL54GS. It has a 266 MHz CPU, 8 MB flash and 32 MB RAM. Supported by whiterussian RC5 and later.

Note the antenna is *NOT* removable in this model

= port mapping =

There are 3 eth interfaces, unlike many WRT units so it is faster on WAN-LAN switching.

eth0=LAN
eth1=WAN
eth2=WiFi

Ports map like so:

||external-port# ||   internal#||
||4              ||           3||
||3              ||           2||
||2              ||           1||
||1              ||           0||
||(CPU)          ||           5||
||Internet       ||           4||

= Hack points =

== serial ports ==
2 serial ports in a 2x5 (10-pin) block near front of board, console on ttyS0 at 115,200 baud. Pins are arranged in exact configuration for addition of an IDC-10 ribbon-cable connector. Unfortunately Linksys did not put one there so you will have to add your own. These connectors were 59 cents at the Fry's Electronics in Sacramento, CA. Standard IDC-10 straight works here. The RF shield nearby, means a right-angle IDC-10 will not work if configured facing interior. Would work fine facing towards front if you cut a hole in front of router. Use a hacked Nokia DKU-5 cable or a MAX233 kit to get serial ports. No hardware flow control, use software.

||'''connector'''||'''1'''||'''2'''||'''3'''||'''4'''||'''5'''||
||JP4(ttyS0)||3.3v||TX||RX||NC||GND||
||JP3(ttyS1)||3.3v||TX||RX||NC||GND||

To check current serial port setting:
{{{
root@OpenWRT:~# cat /proc/tty/driver/serial
serinfo:1.0 driver:5.05c revision:2001-07-08
0: uart:16550A port:B8000300 irq:3 baud:114583 tx:5108 rx:129 RTS|DTR
1: uart:16550A port:B8000400 irq:3 baud:9593 tx:0 rx:0 CTS|DSR|CD
}}}

If you are going to work much with the serial ports, recommend to use the buildroot kit to build a firmware with BusyBox including the optional stty, getty, setserial, and maybe login programs.

== JTAG ==
No JTAG header is available.  However, all basic pins are present on test points: 
inline:wrtsl54gs_jtag.jpg

SRST and TRST haven't been identified, but ignoring them doesn't prevent JTAG to operate.

Be warned that soldering or probing on test points is fairly tricky.

Both Xilinx and Wiggler cables should work - see [http://wiki.openwrt.org/JTAG_Cables this] wiki entry.

HairyDairyMaid's debricker is working, but currently requires /skipdetect and instrlen:8 options since the 4704 isn't in the list of supported processors.  The 28F640J3 flash in the SL is in the known part list of the debricker.

A JTAG discussion thread is [http://www.linksysinfo.org/modules.php?name=Forums&file=viewtopic&t=14754 here].

== LED10 ==
The LED10 location at front of board contains no LED. Perhaps it is usable by GPIO functions for 1-Wire or similar.

= Board info and CPU model =
||'''Model'''||'''boardrev'''||'''boardtype'''||'''boardflags'''||'''boardnum'''||'''wl0_corerev'''||'''cpu  model'''||
||WRTSL54GS||0x10||0x042f||0x0018||42||9||BCM4704 rev8||

= More information =

Autopsy photos http://www.linksysinfo.org/modules.php?name=Content&pa=showpage&pid=36

Original exploration thread  http://www.linksysinfo.org/modules.php?name=Forums&file=viewtopic&t=12538

Spillover into OpenWRT  http://forum.openwrt.org/viewtopic.php?id=3529

You can get the MAX233 parts kit here:
http://www.compsys1.com/workbench/On_top_of_the_Bench/Max233_Adapter/max233_adapter.html
Recent information was, an extra $6 added to kit price on request for an assembled version.

= Firmware download =

Recommend to use WhiteRussian RC5 or later.
