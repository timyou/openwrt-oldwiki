= Western Digital NetCenter =
Kamikaze is running on this device with 2.4 or 2.6 kernel (brcm 47xx).
The IDE HDD  can be mounted (so bootstrapping is possible, but not tested yet).

This device is simmilar to the ASUS WL-700g.

== Hardware ==
 * Broadcom 4780 @ 266MHz (BCM4780PKPBG) SoC with hardware encryption (crypto not currently supported)
 * 8MB FLASH (?) and 32MB DDR-SDRAM (?)
 * VIA USB 2.0 controller (VT6212L), 2 external USB connectors
 * Acard/Artop PATA controller (ATP865-B) and Western Digital Caviar SE harddisk (160GB/250GB/320GB versions).
 * TTL serial port with soldered socket on board (4-pin)

== GPIO ==
 * GPIO 0 = soft-power-button (0...pressed, 1...not pressed)
 * GPIO 1 = LED1
 * GPIO 2 = SDA
 * GPIO 3 = +5V line (0...on, 1...off)
 * GPIO 4 = LED4
 * GPIO 5 = SCL
 * GPIO 6 = +12V line (0...on, 1...off)
 * GPIO 7 = hard-reset (reset-button-press or setting this pin high forces a hard-reset)

After reset GPIO 2, GPIO 5 and GPIO 7 are 0, the rest is 1.
The harddisk needs the +12V and the +5V power supply (GPIO 3 and GPIO 6 set to 0).
There are 2 leds a red (or orange) one and a blue one.
The red led is lighting if (LED4 is 0) or (+5V and LED1 and LED4 are 1).
The blue led is lighting if +5V is 1 and not(LED1 is 1 and LED4 is 0).

== Links ==
 * ASUS WL-700g http://wiki.openwrt.org/OpenWrtDocs/Hardware/Asus/WL700gE
 * German net-center page on http://www.open-netcenter.de (with forum)
 * OpenMMS page for Maxtor Shared Storage (which has nearly the same hardware) http://openmss.org
