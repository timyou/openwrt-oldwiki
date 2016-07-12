'''Linksys WRTSL54GS'''

[[TableOfContents]]
= Hardware versions =

These models have a 266 MHz CPU.  There are 2 variants:

||serial||flash||RAM  || firmware ||
||CJK0  ||8 MB ||32 MB|| WhiteRussian RC5 and later works.||
||CJK1  ||8 MB ||32 MB|| WhiteRussian RC5 and later works.||

The antenna is *NOT* removable. Well not without some soldering work.

= Interface diagram (per mbm) =

{{{
                     .-OpenWrt--------------------.
                     | .-----.                    |
                     | | br0 |--------------.     |
                     | '-----'              |     |
                     |    |                 |     |
                     | .------. .------. .------. |
                     '-| eth0 |-| eth1 |-| eth2 |-'
                       '------' '------' '------'
                          |        |        |
                          |        '---.    |
    .-switch--------------|----------. |    |
    | .-vlan0-------------|--.       | |    |
    | |                .--|--+-vlan1 | |    |
    | |[0] [1] [2] [3] | [5] | [4] | | |    |
    | '-|---|---|---|--+-----'     | | |    |
    |   |   |   |   |  '-----------' | |    |
    '---|---|---|---|----------------' |    |
        |   |   |   |      .-----------'    |
        |   |   |   |      |       .--------'
        |   |   |   |      |       |
    .---|---|---|---|------|-------|----.
    |  [1] [2] [3] [4]   [wan]   [wifi] |
    '-case------------------------------'
}}}

Note switch port 4 is not externally available. This design is different from many units which use a single interface to handle both LAN & WAN traffic, so performance should be better.

= Hack points =

== serial ports ==
2 serial ports in a 2x5 (10-pin) block near front of board, console on ttyS0 at 115,200 baud. No hardware flow control available.  Pins are arranged in exact configuration for addition of an IDC-10 ribbon-cable connector. Unfortunately Linksys did not put one there so you will have to add your own.  The signal from the WRT board is 3.3 Volt TTL however, so you cannot simply wire to a standard RS-232 connector as they operate at 12 Volts. You will need a circuit to convert the 3.3 Volt signal to a level that is usable by a host. 

||'''connector'''||'''1'''||'''2'''||'''3'''||'''4'''||'''5'''||'''defaults'''||'''usage'''||
||JP4(ttyS0)||3.3v||TX||RX||NC||GND||115,200 baud, 8-n-1, none||console root shell||
||JP3(ttyS1)||3.3v||TX||RX||NC||GND||9,600   baud, 8-n-1, none||     unused       ||

NC=not connected, this pin is not used.

To check current serial port setting:
{{{
root@OpenWRT:~# cat /proc/tty/driver/serial
serinfo:1.0 driver:5.05c revision:2001-07-08
0: uart:16550A port:B8000300 irq:3 baud:114583 tx:5108 rx:129 RTS|DTR
1: uart:16550A port:B8000400 irq:3 baud:9593 tx:0 rx:0 CTS|DSR|CD
}}}

If you are going to work much with the serial ports, recommend to use the buildroot kit to build a firmware with BusyBox including the optional stty, getty, setserial, and maybe login programs.

=== MAX233 kit console ===
inline:wrtsl54gs_serial_IDC10.jpg

Above are 2 common IDC-10 sockets. On the left is a straight IDC-10 socket which would be useful for internal hookups, or running a ribbon to a convenient mounting point for an external connector.  The type on the right is a "right-angle" socket and is the one installed on the SL above it.  These sockets cost less than one dollar/euro and fit relatively easily onto the PCB.

inline:wrtsl54gs_serial_complete.jpg

Here's one complete serial-console setup, using a MAX233 kit with ribbon-cable connectors. This makes it easy to move among multiple routers assuming they are fitted with an IDC-10 socket.

=== TTL-232R-3V3-AJ USB console ===

Another good choice is using a USB device that natively supports the 3.3V TTL signal levels. One such product:

http://www.ftdichip.com/Products/EvaluationKits/TTL-232R-3V3-AJ.htm

There is a tiny PCB in the host-end of the USB cable that is doing the signal conversion. Since the circuit is powered from the USB port, only 3 wires need to be soldered instead of the 4 needed in the MAX233 design.  You need to hook up TX, RX, and GND pins and a convenient choice for external interface port is a stereo jack.  It's a clean and elegant setup. Thanks to JimWright, here's how it can look installed:

inline:wrt_jack_cable.jpg

inline:Serial_hack.jpg

== JTAG ==

inline:wrtsl54gs_jtag.jpg

No JTAG header is available.  However, all basic pins are present on test points.

SRST and TRST haven't been identified, but ignoring them doesn't prevent JTAG from operating.

Be warned that soldering or probing on test points is fairly tricky.

Both Xilinx and Wiggler cables should work - see [http://wiki.openwrt.org/OpenWrtDocs/Customizing/Hardware/JTAG_Cable this] wiki entry.

HairyDairyMaid's debricker is working, but currently requires /skipdetect and instrlen:8 options since the 4704 isn't in the list of supported processors.  The 28F640J3 flash in the SL is in the known part list of the debricker.

== LED10 ==
The LED10 location at front of board contains no LED. Perhaps it is usable by GPIO functions for 1-Wire or similar.

= Board info and CPU model =
||'''Model'''||'''boardrev'''||'''boardtype'''||'''boardflags'''||'''boardnum'''||'''wl0_corerev'''||'''cpu  model'''||
||WRTSL54GS||0x10||0x042f||0x0018||42||9||BCM4704 rev8||

= More information =

Autopsy photos http://www.linksysinfo.org/forums/showthread.php?t=47389

64 meg RAM upgrade: http://www.linksysinfo.org/forums/showthread.php?t=46673

Original exploration thread http://www.linksysinfo.org/forums/showthread.php?t=43413&highlight=wrtsl54gs

Spillover into OpenWRT  http://forum.openwrt.org/viewtopic.php?id=3529

You can get the MAX233 parts kit here:
http://www.compsys1.com/workbench/On_top_of_the_Bench/Max233_Adapter/max233_adapter.html
Recent information was, an extra $6 added to kit price on request for an assembled version.

Another USB TTL convertor device:
http://www.compsys1.com/html/usb_rs232.html

= Firmware download =

Recommend to use WhiteRussian RC5 or later.
