## page was renamed from OpenWrtDocs/Hardware/Ubiquit/LiteStation5
'''!LiteStation5'''

{{{
Bootloader: RedBoot
CPU: Atheros AR2313
CPU Speed: 180 Mhz
Flash size: 4 MB
RAM: 16 MB
Wireless: Atheros 802.11a/b/g (in CPU, 400mW)
Ethernet: 1 port connected to the CPU
USB: none
Serial: yes
JTAG: ?
}}}
=== OpenWrt support ===
OpenWrt doesn't support the LS5, yet. If you are interested in OpenWrt support for this unit, please contact ["Kaloz"].

Using the firmware builder from Ubiquiti: http://www.ubnt.com/downloads/mkfwimage-1.2.tar.gz a bootable OpenWRT fireware can be built.  However, as of r7880, MADWIFI does not recognize the radio as a supported hardware version.

=== Serial Port ===
According to Ubiquiti the serial port is 3.3v and uses the following pins:

pin1,2   -- 3.3V
pin3     -- SIN
pin5     -- CTS
pin7     -- RTS
pin9     -- SOUT
pin11,12 -- GND

However, with this pin connection to my MAX3232 chip no data ever appeared to my serial console.
