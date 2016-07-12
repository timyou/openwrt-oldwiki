'''IO-DATA USL-5P'''


This is a NAS with 5 USB ports and 1 ethernet interface.

 * Bootloader: SH IPL+g with modifications from IO-DATA
 * CPU: SH7751R @ 240MHz (SH4)
 * Flash size:
 * RAM: 64MByte
 * Ethernet: Realtek RTL8139C+
 * Serial: yes, pinouts follow
 * CF slot: yes, the bootloader boots from a CF card
 * Other: Buzzer, RTC


=== Serial pinout ===


{{{
   o   o   o   o     [battery]
  GND RxD TxD 3.3V
}}}

Serial settings are 9600, 8n1.

=== Boot ===

The original firmware boots immediately after the bootloader initialization is complete, there is no way to abort it. Also there is no known way to login to it, so the only way to install OpenWrt on this device is to change the contents of the CF card.

NOTE: This wiki entry will be changing quickly as I'm playing around with OpenWrt to support this board.
