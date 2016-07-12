= Introduction =
These pages will describe building the hardware and software required to add an I2C bus and a Real-Time Clock to the Linksys WRT54GL router.
The I2C bus is very versatile and can interface with many components such as eeprom memory chips, GPS location detectors, solid-state compasses, LCD displays and of course the Real-Time clock chip described here.

Eventually more I2C projects will be documented here.

= Credits =
The information presented here was partially gathered from sources on the Internet
including the following:[[BR]][http://www.linksysinfo.org] and [http://openwrt.org]:

'''Firmware:''' !OpenWrt Whiterussian 0.9[[BR]]
'''Kernel driver:''' i2c-mips-gpio: from [http://forum.openwrt.org/viewtopic.php?id=7949][[BR]]
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

attachment:i2c-rtc-mounted.jpg

Mounted in the router together with the serial console adapter and 5v regulator.[[BR]]Although it doesn't look like it, there's about 10mm clearance above the main board.[[BR]]
Since the gpio pin for the Cisco button is used, I decided to shorten the length of the
buttons lever to avoid it getting pressed accidentally. This probably wouldn't cause any
problems but better to be safe.

attachment:shorten-cisco-button.jpg

= Software =
== Prerequisites ==
 *!OpenWrt Whiterussian 0.9 flashed to the router and running normally. Available from [http://downloads.openwrt.org/whiterussian/0.9/default/]
 *Microperl ipkg installed on the router. Available from [http://downloads.openwrt.org/backports/0.9/microperl_5.8.6-1_mipsel.ipk]
 *A Linux workstation if you plan on compiling the binaries.

== WRT54GL OS ==
Not much to be said here besides flash your router with Whiterussian 0.9 as stated in
the prerequisites. No other router or Whiterussian version has been tested although I can see no reason why it wouldn't work on other routers.

== Kernel Modules ==
These kernel modules were used:
 *i2c-core
 *i2c-algo-bit
 *i2c-proc
 *i2c-dev
 *i2c-mips-gpio (compiled separately from the regular kernel modules)

The first 4 can be obtained by rebuilding the kernel using "make menuconfig" in the kernel tree build_mipsel/linux and enabling the I2C bit-banging routines. After compilation, they can just be copied over to the router to the /lib/modules/2.4.30 directory.[[BR]]
The last kernel module needs to be compiled from the code mentioned in the credits section of this page or copied from here: [[BR]]

["/Source Code"]

Note that the code shows an alternate hardware schematic for the I2C bus which differs from the schematic presented in the Hardware section of this page.[[BR]]
The schematic presented in the Hardware section provides better signal buffering to and from the I2c devices.
After compiling the last module it too needs to be copied to th router and installed under /lib/modules/2.4.30 just like the previous modules.
If you want to get all the Modules precompiled, send a PM to !NekMech on the !OpenWrt forum.

== User Space programs and scripts ==
There are 3 binaries: i2cset, i2cread, i2cdump[[BR]]
And 3 scripts: i2c-load.sh, gethwclock.pl, S99i2c[[BR]]

Source code is available here: ["/Source Code"]

In all the examples below, the device used was the DS1307 I2C clock chip.
The clock chip is wired to I2C bus “0” (the only one), and has a device address of “104”
decimal or “68H” hex. These programs were all installed under /usr/share/i2c on the
router and are run from there besides S99i2c which is installed under /etc/init.d.

=== Binaries ===
 *i2cset – Sends any command over the i2c bus to any device.
 *i2cread – Reads any number of characters from any device on the i2c bus.
 *i2cdump – Provided as a diagnostic tool which can read all the available data from any i2c device.
=== Scripts ===
 *i2c-load.sh – bash script for loading the kernel modules in the correct order with “insmod”.
 *gethwclock.pl – microperl script which performs all the tasks of reading and writing to the clock chip. You will need the microperl ipkg installed as stated in the prerequisites.
 *S99i2c – bash script which is executed at boot to load the kernel modules, and update the system time from the hardware clock.

=== Using the scripts and binaries ===
'''i2cset''' - Used to send data/commands to an i2c device.[[BR]]
Running with no command line options displays an error message and help syntax as well as the available i2c busses.[[BR]]
{{{
Example:
root@OpenWrt:/usr/share/i2c# ./i2cset
Syntax: i2cset I2CBUS CHIP-ADDRESS VALUES
I2CBUS is an integer
Installed I2C busses:
i2c-0 i2c WRT54G GPIO Bit-shift algorithm
}}}
The gethwclock.pl script uses it to set the time, the control register and to move the
register pointer of the hardware clock to the correct position for reading the time.[[BR]]

'''i2cread''' - Used to read back data from an i2c device.[[BR]]
Running with no command line options, displays an error message and help syntax as well as the available i2c busses.
{{{
Example:
root@OpenWrt:/usr/share/i2c# ./i2cread
Syntax: i2cread I2CBUS CHIP-ADDRESS COUNT
I2CBUS is an integer
Installed I2C busses:
i2c-0 i2c WRT54G GPIO Bit-shift algorithm
}}}
The gethwclock.pl script uses it to read the hardware clock during boot (to set the
system clock) and any time requested manually.

'''i2cdump''' - Used as a general purpose diagnostic tool, it performs a dump of any i2c devices registers/memory.[[BR]]
Running with no command line options displays an error message and help syntax.
{{{
Example:
root@OpenWrt:/usr/share/i2c# ./i2cdump
Error: No i2c-bus specified!
Syntax: i2cdump I2CBUS ADDRESS [MODE] [BANK [BANKREG]]
MODE is 'b[yte]', 'w[ord]', 's[mbusblock], or 'i[2cblock]' (default b)
Append MODE with 'p' for PEC checking
I2CBUS is an integer
ADDRESS is an integer 0x00 - 0x7f
BANK and BANKREG are for byte and word accesses (default bank 0, reg 0x4e)
BANK is the command for smbusblock accesses (default 0)
Installed I2C busses:
i2c-0 i2c WRT54G GPIO Bit-shift algorithm
}}}

Running the utility with the bus number “0” and device address “104” will dump all the registers for the clock chip. Note that addresses 08H – 3FH are general purpose ram registers which can be used for anything you want. Do not use ram register 3FH since it will be overwritten when reading the date from the clock chip by the gethwclock.pl script.
{{{
Example:
root@OpenWrt:/usr/share/i2c# ./i2cdump 0 104
No size specified (using byte-data access)
WARNING! This program can confuse your I2C bus, cause data loss and worse!
I will probe file /dev/i2c/0, address 0x68, mode byte
You have five seconds to reconsider and press CTRL-C!

0 1 2 3 4 5 6 7 8 9 a b c d e f 0123456789abcdef
00: 04 48 16 01 09 04 07 10 10 10 6a 50 52 c3 4d 22 ?H????????jPR?M"
10: cb 6a 68 00 e2 7c 50 41 03 01 f9 55 12 0c 69 0c ?jh.?|PA???U??i?
20: 70 1e 02 42 a8 2c 02 2a bc 48 28 3e 80 2c b7 84 p??B?,?*?H(>?,??
30: 1f 00 68 42 c6 5e 34 d4 42 8a 20 28 c7 90 fe ff ?.hB?^4?B? (???.
40: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ................
50: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ................
60: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ................
70: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ................
80: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ................
90: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ................
a0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ................
b0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ................
c0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ................
d0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ................
e0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ................
f0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ................
}}}






Work in progress
