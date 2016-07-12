= Introduction =
These pages will describe building the hardware and software required to add an I2C bus and a Real-Time Clock to the Linksys WRT54GL router.
The I2C bus is very versatile and can interface with many components such as eeprom memory chips, GPS location detectors, solid-state compasses, LCD displays and of course the Real-Time clock chip described here.

Eventually more I2C projects will be documented here.

= Credits =
The information presented here was partially gathered from sources on the Internet
including the following:[[BR]][http://www.linksysinfo.org] and [http://openwrt.org]:

'''Firmware:''' `OpenWrt Whiterussian 0.9`[[BR]]
'''Kernel driver:''' i2c-mips-gpio:[[BR]]
Based on original i2c-mips-gpio by John Newbigin,[[BR]]
which in turn was based on i2c-philips-par.c by Simon G. Vogl.[[BR]]
Changed to sb_gpio-Interface by Torsten Landschoff.[[BR]]
4-wire logic and final version by niclas at datenritter dot de.[[BR]]
'''User space binaries''' are modified versions of utilities provided in the lm_sensors package: [http://www.lm-sensors.org][[BR]]
'''Schematics''' were created with gEDA: [http://www.geda.seul.org]

= Hardware =
=== Schematic ===

attachment:i2c_rtc.png

Basically, the circuit is comprised of 2 IC's and support components.
The 74LS05 buffer is open collector and requires pull up resistors on the outputs. All incoming and outgoing signals are buffered.
The DS1307 clock circuit is just the basic reference design specified in the data sheet and it's I2C signals are just connected to the I2C bus.
The SQW signal is just a square wave programmable as 1Hz, 4kHz, 8kHz, 32kHz or as a constant high or low output. Can be used for anything you want.[[BR]] [[BR]]
The battery backup mechanism of the clock chip ensures time is maintained also when
the router is powered off.[[BR]]
+5V power was obtained from a 7805 regulator circuit (added on a separate circuit) which is not described here.

=== GPIO pins ===
I2C GPIO signals used:[[BR]]
SDA_OUT : GPIO 4 (Cisco switch)[[BR]]
SDA_IN: GPIO 2 (White LED)[[BR]]
SCL_OUT: GPIO 7 (DMZ LED)[[BR]]
SCL_IN: GPIO 3 (Orange LED)[[BR]]

''Note:'' Because of the use of these GPIO pins which are also used by the MMC project, you won't be able to have both. Sorry.

=== Construction ===
The circuit was built on a small piece of perforated board.[[BR]][[BR]]
attachment:i2c-rtc-circuit.jpg

The upper right hand corner is for the I2C extension connector for additional I2C devices.[[BR]]
The 4 GPIO signals as you see are connected with the upper terminal block and +5V connected with the lower terminal block.



Work in progress
