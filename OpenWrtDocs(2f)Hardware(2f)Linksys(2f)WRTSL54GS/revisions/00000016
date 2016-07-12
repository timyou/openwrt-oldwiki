'''Linksys WRTSL54GS'''

[[TableOfContents]]
= Hardware versions =
There is only one version of the WRTSL54GS. They have a 266 MHz CPU, 8 MB flash and 32 MB RAM. It's supported by OpenWrt whiterussian pre-RC5 and later.

Note is the antenna is **not** detachable.

= port mapping =

There are 3 eth interfaces, and ports map like so:

||external-port# ||   internal#||
||4              ||           3||
||3              ||           2||
||2              ||           1||
||1              ||           0||
||(CPU)          ||           5||
||Internet       ||           4||

= Hack points =

== serial ports ==
2 serial ports in a 2x5 (10-pin) block near front of board, console on ttyS0 at 115,200 baud. Pins are arranged in exact configuration for addition of an IDC-10 ribbon-cable connector. Unfortunately Linksys did not put one there so you will have to add your own. Standard IDC-10 straight works here. The RF shield nearby, means a right-angle IDC-10 will not work if configured facing interior. Would work fine facing towards front if you cut a hole in front of router. Use a hacked Nokia DKU-5 cable or a MAX233 kit to get serial ports. No hardware flow control, use software.

||'''connector'''||'''1'''||'''2'''||'''3'''||'''4'''||'''5'''||
||JP4||3.3v||TX||RX||?||GND||
||JP3||3.3v||TX||RX||?||GND||

== JTAG ==
2 locations on back of board with JTAG markings, but does not account for all pins needed. Hypothesis of user bbarrett at DSLreports.com was that Linksys uses a "bed of nail" test fixture and the contact points are scattered and not all labelled.

== LED10 ==
The LED10 location at front of board contains no LED. Usable by GPIO functions for 1-Wire or similar.

= Board info and CPU model =
||'''Model'''||'''boardrev'''||'''boardtype'''||'''boardflags'''||'''boardnum'''||'''wl0_corerev'''||'''cpu  model'''||
||WRTSL54GS||0x10||0x042f||0x0018||42||9||BCM4704 rev8||

= More information =
forum posts:

Original exploration thread  http://www.linksysinfo.org/modules.php?name=Forums&file=viewtopic&t=12538

Spillover into OpenWRT  http://forum.openwrt.org/viewtopic.php?id=3529


= Firmware download =

March 8 or later pre-RC5 builds work fine. Until RC5 is released, use SVN or a snapshot from
 * nbd: http://downloads.openwrt.org/people/nbd/whiterussian/
