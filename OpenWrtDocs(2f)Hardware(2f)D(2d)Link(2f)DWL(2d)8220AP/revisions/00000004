= D-Link DWL-8220AP =


=== Hardware ===

{{{
OS : VxWorks
CPU : Atheros AR5312A
Flash : Macronix MX29LV160BTTC
Wi-Fi : 802.11a/b/g with AR2112A/AR5112A
RAM : 16 Mb
Switch : 2x IC+ IP101A
JTAG : yes
Serial : yes
}}}

=== Serial ===

The serial pinout is a bit tricky. To have VCC and GND here is what I did :

J1 header :

{{{
LED

    [] (GND)
    () ()
    () ()
    () ()
    () ()
    () ()
    () (VCC)
LED
}}}

JP2

{{{
LEDs (left side)
(TX) () () (RX)
}}}

Serial console is at 38400 8N1

=== Bootlog ===

{{{
AP Boot Loader version 16
Stage 1 boot code build 4.0.7.5_080805_0731__AP
access point startup

    Trapeze Networks AP Bootstrap 1.5 (01/xx/05)


GO 1 entry_addr 80400000 ....

AP Boot Loader version 16
Stage 1 boot code build 4.0.7.5_080805_0731__AP
access point startup
}}}

Here is a capture of the exchange between a bootstrapping access point and a machine acting as a DHCP server.

[http://f.fainelli.free.fr/openwrt/wiki/dwl8220ap-capture.pcap]
