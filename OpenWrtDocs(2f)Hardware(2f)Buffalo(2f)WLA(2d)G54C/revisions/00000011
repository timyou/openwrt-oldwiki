Buffalo WLA-G54C AirStation 54Mbps Wireless Compact Repeater Bridge-g

Internally it has a Mini-PCI card (Part # WLI-MPCI-G54). The PCI card has a Broadcom BCM4306KFB chip on it. Main CPU is BCM4702KPB Memory looks like a pair of DYNACHIPS D98SD6416AH-6.

There are a couple of other chips under the Mini-PCI card.

The wireless is hooked up to 2 antennas. One in vertical polarity the other in horizontal polarity. The antenna on the top of the unit can be bypassed and connected to an external antenna. The socket is hidden under a little rubber plug on the back of the unit.

2 LED's. Oddly enough, they are labeled LED2 (Wireless) and LED3 (Ethernet).

Unit also has a pushbutton switch labeled INIT

Another important note is that there is room for a 20-pin header on the board. It is labeled J25. There are no pins, but a header would be easily mounted, as the holes are already drilled through the PCB. There is a ground wire from the Mini-PCI card already soldered into one of the holes. Don't know if this could be used for JTAG and/or serial, but it defintely has traces from some of the 'pins' to other components on the board. However, those components are under the Mini-PCI card.

Fllowing is the room for 20-pin header, it connect to the 4M Byte flash directly,but only address line of A0 TO A3 is connected. "NC" is means that it cann't be measured.

GND      CE      QD7     QD6    QD5   QD4   QD3    QD2    QD1     QD0                     

1        2         3      4      5     6      7     8       9      10                     

11       12       13      14     15   16     17    18      19      20                     

||GND      NC       NC      WE     OE    NC    A3     A2     A1       A0                    

Who can make suggestions to repair WLA-G54C through this 20-pin heater.


Some Addon From Ben:
------------------------------------------------------
I've tried to install White Russian Firmware on it by using TFTP server as suggested, no lucky at all, it seems this ap cannot handle it well, but it's possible to install latest firmware by using default buffalo httpd configuration tool. BIN file doesn't need to be encrypted, so you can create your own distribution and easily put on it, here's what i've done (you need an HEX editor to do this):
- Download Buffalo latest firmware from their web site, keep first 35 byte from it
- Append compiled White Russian firmware to these 35 bytes and save your own firmware file everywhere on the pc
- Check file length, subtract 35 and put this number inside string filelen="xxx" found it first 35 bytes. Example: file size=1552390, write "filelen=1552355" string (without quotes..) where needed in its first 35 bytes and you're set, now you have your own firmware for WLA-G54C
- Upload your new bin file with Buffalo Web Interface, it's easy to do
- Reboot and follow OpenWRT documentation

Have fun
i've enjoyed so much this distro and i'd like to contribute for a piece of hardware i can control

Andrea (Ben) Benini
