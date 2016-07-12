= Serial Console =
Serial ports allow you to do a myriad of things, including connect to your computer, connect to other devices such as LCDs and GPSes, etc... With a little programming, you could even connect a bunch of routers together. This mod doesn't '''add''' serial ports; those are already there. This just makes them much easier to use with just about any hardware you want.

For the developer, a serial port will also allow you to recover a bricked router when all other methods have failed (tftp, failsafe mode, shorting pins, etc.) This is something which typically cannot be done with just a USB-capable router and USB-serial adapter, as USB support is only available once the firmware has successfully loaded.

== TTL vs. RS-232 levels ==
Most OpenWrt compatible devices have one or two* serial ports on the router's PCB (printed circuit board). The problem is they operate on 3.3V, which means '''they will get fried if you connect them to your computer's serial port''', which operates at 12V.

=== USB TTL Serial ===
You could buy something like [http://www.sparkfun.com/commerce/product_info.php?products_id=718 this] or [http://www.sparkfun.com/commerce/product_info.php?products_id=199 this].
[http://www.ftdichip.com/Products/EvaluationKits/TTL-232R-3V3-AJ.htm This] is even simpler. (Scroll down on that page.)

A USB based data cable for a mobile cell phone is another possibility.

note: For the serial console on a WRT54G with a USB cell phone cable, the following pins are used: 4(tx), 6(rx), 10(gnd)

Compatible Radio Shack (Future Dial) "Mobile Phone Data Cables" using the Prolific 2303 USB-3.3vSerial converter chip:

 *LG Models 1200, VI5225, VX4500, VX4600, VX600
 *Audiovox Models 8200, 8500 and 8600
 *Nokia Models 3285 and 5185
 *Cable 22 (For Nokia 3100, 3200, 3585i, 3588 and others with Nokia 14-pin pop-port)
 *Cable 32 (For Motorola T720*, T722i, P280, 270c, V60*, V66, V70, V120*)

Ebay clone cables:
 *Datacable for Nokia 6210, 6250, 6310, 6310i, 7110

reference: http://www.nslu2-linux.org/wiki/HowTo/AddASerialPort

=== Home-made RS-232 kit ===
TTL-RS-232 level conversion is a fairly common problem, so there are a number of ICs on the market that convert between these voltage levels.   has made a few handy little ICs for us to use. The best (IMHO) is the , or more specifically, the MAX233a, which has a higher speed capacity and uses less power. This guide will tell you how to solder everything together to get a pc-compatible serial port on your OpenWrt router.

==== From scratch ====
First, you need an "RS232-TTL level converter chip."  RS232 refers to the standard defining what plugs into your computer, and TTL is a family of chips that use 0V and 0.8V as low and 2.2V and 5V as high.  They can be purchased new (the [http://www.maxim-ic.com Maxim IC] MAX233x line is popular).  Most vendors have large minimums, but some (e.g. [http://mouser.com/ Mouser Electronics]) sell components in small quantities.

The wiring is fairly simple, but it depends on the chip.  Generally, it involves connecting Vcc from the router to the chip's Vcc pin, both router and rs-232 grounds to the ground pin, and the TX and RX wires to the chip.  Remember that the router's TX will "connect" to the same level conversion bank as the computer's RX.  Additionally, some of these level converters require external capacitors, while some have them built in.  Much of this varies, so consult the chip's spec.

==== From a PDA or cell phone serial cable ====
Another great source for RS232-TTL converters is in cell phone serial cables. Most cell phones need this same circuit to level-up for connection to a PC's serial port. Many people already have such a cable laying around, or can buy one fairly cheap.  Using an existing cable is much easier than building one.  If you open up the cell phone cable's serial port casing and see a MAX### chip, it's probably the cable you need. One known chip is a MAX323 (yes, 323, the original MAX232 is a 5V device and we need 3.3V here).

If you've found a good cell phone cable to use, you merely need to determine which wires are the VCC, GND, TX, and RX connections. Usually the VCC is red and the GND is black, but the other colors may vary (though blue and orange are common). There should be no need to modify the PCB embedded in the cable.

==== MAX232 Kits ====
You can also search for MAX232 Kits. There are some kits available.

 * http://cgi.ebay.fr/RS232-to-TTL-level-Signal-Converter-Kit_W0QQitemZ9703039037QQcategoryZ41995QQssPageNameZWD2VQQrdZ1QQcmdZViewItem,
 * http://www.elv-downloads.de/service/manuals/TTLRS232-Umsetzer/38439-TTLRS232-Umsetzer.pdf
 * http://www.compsys1.com/workbench/On_top_of_the_Bench/Max233_Adapter/max233_adapter.html

==== Model-specific guides ====
These guides are somewhat model specific, but if you're struggling to build your own cable, they're filled with information that applies to that part of the process.
 * [http://jdc.parodius.com/wrt54g/serial.html WRT54G serial mod guide]
 * [http://www.nslu2-linux.org/wiki/HowTo/AddASerialPort NSLU2 serial guide]
 * [http://www.rwhitby.net/wrt54gs/serial.html WRT54GS serial guide]

=== Use your old PDA as a console ===
Since many older PDAs (e.g. Palm series) have TTL serial connections already, you can use them to get a direct serial connection to the router.  

Solder the RX, TX, and ground (but '''never''' Vcc) TTL-level connectors on the OpenWrt box to the PDA's TTL level serial connectors.

Example: Palm IIIc, [http://www.neophob.com/serendipity/index.php?url=archives/121-Reuse-your-old-Palm-as-Serial-Console.html].

== Terminal software ==
 * Hyperterm (comes with many versions of MS Windows)
 * Minicom (for POSIX systems)
 * [http://efault.net/npat/hacks/picocom/ picocom]
 * cu(1) (part of the Taylor UUCP package, for POSIX systems)
 * [http://www.chiark.greenend.org.uk/~sgtatham/putty/ Putty] v0.59 or newer (now with serial console support!)
 * Pocketterm  (for Palm PDAs)

== Serial port pinouts ==
Pinouts for your model can often be found on your model's page in CategoryModel.

== Finding Serial Console ==
First, check the OpenWRT wiki page describing your hardware and do a Google search. Most of the time, the serial port(s), if they exist, have already been documented by others.

=== Piezoelectric buzzer method ===
1. Use a Piezoelectric buzzer and attach its ground (usually black) wire to a ground point on the router; the back of the power regulators are usually good candidates, but check this with a multimeter/voltmeter.
2. Use the other wire to probe any of the header pins which may be pre-installed, or any of the component holes which look like they could have header pins installed into (typically in a row of 4 pins for a serial port).  Reset the router.  The bootloader/linux bootup messages will only happen for a few seconds, and after that, the serial console will be silent - so even if you have the right pin you will not hear anything.

3. Once you get the right pin, the Piezoelectric buzzer should make a screeching sound much like that of a 56kbps connection.

=== Logic analyzer/oscilloscope ===
A more accurate method would be to use either a logic analyzer or an oscilloscope, but these are expensive and for the basic task of locating a serial pin a little overkill. ;-)
