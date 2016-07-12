#pragma section-numbers off

= SMC WBR14-G2 =

The [http://www.smc.com SMC] [http://www.smc.com/index.cfm?event=viewProduct&localeCode=EN_USA&cid=5&scid=26&pid=1535 WBR14T-G] is an Atheros 2317-based device. (for more information look at ["AtherosPort"])

This device runs Atheros's own bootloader, and VxWorks proprietary OS, which doesn't have network (ethernet) firmware uploading/downloading support, so no boot_wait either. It supports uploads/downloads via serial console (XMODEM).
It also seems that SMC removed the atheros board configuration data from the flash ROM, so it has to be reprogrammed.


== Hardware Info ==

CPU: Atheros AR2317 WiSoC @ 240 Mhz

RAM: PSC A2V64S4OCTP (8MB)

Flash: ST 25P16V6P (2MB)

Ethernet: 5x 10/100 RJ45 Ports (ICPlus PHY)

Wireless: Atheros AR2317 integrated

Other: Reset button, 8 led's, serial and jtag port

=== Serial Console ===

A TTL/RS232 converter is needed to access the serial console of the bootloader.
Default baudrate: 115200 8N1
Pinout: (the first pin is marked with a white arrow on the PCB):
||'''Pin''' ||'''Function''' ||
|| #1 || VCC (+3.3V) ||
|| #2 || TxD ||
|| #3 || RxD ||
|| #4 || Ground (GND) ||
|| #5 || Not connected ||

=== JTAG ===

The JTAG connector (MIPS EJTAG v2.5 compliant) can be found next to the serial connector.
Pinout:
||'''Function''' ||'''Pin''' ||'''Pin''' ||'''Function''' ||
|| TRST_N || #1 || #8 || GND ||
|| TDI || #2 || #9 || GND ||
|| TDO || #3 || #10 || GND ||
|| TMS || #4 || #11 || GND ||
|| TCK || #5 || #12 || GND ||
|| SRST_N || #6 || #13 || Unused ||
|| Unused || #7 || #14 || VCC ||

The unbuffered Xilinx-type cable works perfectly.
For more information see ["OpenWrtDocs/Customizing/Hardware/JTAG_Cable"].

Notice: JTAG might not work "out of the box", if JTAG SPI flash programmers like tjtagspi fail to recognise the CPU (CPU Chip ID: 11111111111111111111111111111111 (FFFFFF)), then it may help to short the VCC and TRST_N pins on the JTAG interface. Doing this is DANGEROUS and may cause permanent damage to your board, so do it at your own risk.



----
 CategoryModel ["CategoryAtherosDevice"]
