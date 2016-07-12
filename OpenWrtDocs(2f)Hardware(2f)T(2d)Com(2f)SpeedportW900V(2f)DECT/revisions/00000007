#pragma section-numbers off
[[TableOfContents]]

= T-Com Speedport W900V DECT Module =

== Hardware ==

The DECT module of the Speedport W900V contains:

 * a [http://www.datasheetcatalog.org/datasheet2/4/091co1c2k8pgu96f8lzgjly4ef7y.pdf Sitel SC14428], the DECT baseband processor.
 * a [http://pdf1.alldatasheet.com/datasheet-pdf/view/28521/TI/LC126A.html TI SN74LVC126A], quad bus buffer with 3-state outputs.
 * a [http://www.st.com/stonline/products/literature/ds/4578/m24128-bw.pdf ST 4128BWP], 128 KBit I2C EEPROM.
 * a [http://elinux.org/upload/7/74/SST39VF400.pdf SST39VF400A], NOR flash of 256K x 16bit.
 * a radio module on a separate PCB, containing Philips UAA3546 und 3595.

The NOR and i2c flash and the bus buffer IC are supplied with a Vcc of 3.3V (which implies that we have a SC14428 without internal flash).

=== PCB Traces ===

I couldn't find the pinout of the SC14428 in 128TQFP in the net.

||'''SC14428 Pins'''||'''connected to'''||
||14 || SDA of i2c eeprom||
||21 || XTAL (10.368 MHz) ||
||22 || condensator to the XTAL||
||30 || A15 of NOR flash||
||47 || via 330 Ohm to testpin 1 of the bottom side of the PCB (see picture below)||
||48 || via 330 Ohm to testpin 2||
||67 || SCL of i2c eeprom||
||68-75||DQ0,DQ8,DQ1,DQ9,DQ2,DQ10,DQ3,DQ11 of the NOR flash||
||85-92||DQ4,DQ12,DQ5,DQ13,DQ6,DQ14,DQ7,DQ15 of the NOR flash||


=== Pictures ===

components side ([http://s10b.directupload.net/file/d/1718/qoab25ry_jpg.htm high-res picture])

http://s1b.directupload.net/images/090227/qc3c4cuo.jpg

bottom side (These may be test points to the SC14428):

http://s8b.directupload.net/images/090306/y3bx84jt.jpg
