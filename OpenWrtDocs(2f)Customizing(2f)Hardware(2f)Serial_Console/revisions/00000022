= Serial Console =

Many people get along without a serial console for their device because they are able to flash working firmware the first time or are able to apply various recovery methods and do all their communicating with the device over a network.  However, due to characteristics of their bootloaders or because they are not yet fully supported, for some devices it can be quite handy to have a compatible serial console available.

Most devices that are supported by OpenWrt include a serial port.  These serial ports typically provide a console to the bootloader and, when the firmware has booted, a console to the running system.  Typically, a console to the bootloader will allow you to configure a network, fetch and flash a new firmware, which can be a life-saver when the firmware is broken.  A console to the running system will let you correct a misconfigured network.

== Connectors ==

Sometimes, the device's serial port is available at a 9-pin D connector accessible from the exterior of the case, sometimes they are found on pin headers on the printed circuit board (PCB), and sometimes they exist as unpopulated holes in the PCB.  

If the serial port is not readily accesssible from the exterior of the device enclosure, you have some choices:

 * modify the enclosure, either to allow passage of a cable or to attach a convenient connector, e.g.:
  * a 9-pin D connector (this is a good choice if you are going to build a level-shifter into the interior of the enclosure, so as to provide a standard +/- 12V interface externally);
  * a 1/8-inch stereo headphone jack (this is a good choice if you are simply bringing the lines to the exterior)
 * open the case to attach to header pins or holes, as needed, this is a good choice if:
  * opening the enclosure is easy; 
  * access to the serial port is needed only very occasionally; and/or
  * you have many devices you would rather not modify.

== Logic Levels ==

Some devices have standard [http://en.wikipedia.org/wiki/RS-232 RS232] +/- 12V serial ports, but in many OpenWrt-supported devices the serial ports operate at TTL voltage (sometimes 5V, but more often 3.3V) levels.  In order for the serial console to work, the logic levels on the wires should match those expected by your device.  The first step therefore is to determine which voltage levels are required.  Often, you can find this documented on the OpenWrt wiki or elsewhere.

== Talking and Listening ==

In order to interact with your device over its serial port, you need a minimum of three wires connected: a ground (GND); transmit (TX); and receive (RX).  It is possible to get useful information about what is happening with only GND and RX, but in order to fix a problem you will usually also need TX.  Your computer's TX should be connected to the device's RX, and your computer's RX should be connected to the device's TX.  The computer's GND should connect the the device's GND.  That way, what you say will get heard by the device and what the device says will get heard by your computer.  This is often called a "null-modem" configuration.

You will also need a terminal emulation program on your computer, such as minicom, hyperterminal, etc.  The terminal emulation program needs to be configured to be compatible with your device, in particular, with regard to baud rate and flow control.  If you are using only three wires (GND, TX, and RX) then hardware flow control should be turned off; you aren't using the pins (RTS and CTS) necessary for it to work.  Rarely, the baud rate that the device expects ''might'' be different in the bootloader and the running firmware; if so, you'll need to modify the baud rate settings in your terminal emulator after the firmware boots up.

== Considerations ==

Some things to consider:

 * If your computer has a serial port, you can use a level-shifter (as necessary) and a "null-modem cable".
 * If your computer has a USB port, then:
  * if your device uses standard RS232 logic levels, you can use a standard USB-serial converter along with a standard "null-modem cable"
  * if your device uses TTL logic levels, you can use a USB-serial device that uses the right serial voltage TTL and a connector suitably wired to connect to your device.
 * If your computer has neither a serial port or a USB port, you are in trouble!

These days, computer manufacturers are dropping RS232 serial ports, while USB ports are increasingly ubiquitous.  Particularly if you need to TTL logic levels, USB is probably the way to go since you can get the right logic levels integrated in the USB-serial converter.

=== USB ===

==== Prebuilt Cables ====

Standard RS232 levels, for example:
 * [http://www.zonetusa.com/DispProduct.asp?ProductID=119 Zonet ZUC3100] uses pl2303 chip, well-supported in Linux

TTL 5V, for example:
 * [http://www.mouser.com/Search/ProductDetail.aspx?qs=OMDV80DKjRorBEBwmlJ4Pg%3d%3d FTDI TTL-232R-5V]
 * [http://apple.clickandbuild.com/cnb/shop/ftdichip?productID=49&op=catalogue-product_info-null&prodCategoryID=47 FTDI TTL-232R-5V (£)]
 * [http://apple.clickandbuild.com/cnb/shop/ftdichip?productID=69&op=catalogue-product_info-null&prodCategoryID=47 FTDI TTL-232R-AJ (£)]
 * [http://apple.clickandbuild.com/cnb/shop/ftdichip?productID=67&op=catalogue-product_info-null&prodCategoryID=47 FTDI TTL-232R-WE (£)]

TTL 3.3V, for example:
 * [http://www.mouser.com/Search/ProductDetail.aspx?R=TTL-232R-3V3virtualkey62130000virtualkey895-TTL-232R-3V3 FTDI TTL-232R-3V3]
 * [http://apple.clickandbuild.com/cnb/shop/ftdichip?productID=53&op=catalogue-product_info-null&prodCategoryID=47 FTDI TTL-232R-3V3 (£)]
 * [http://apple.clickandbuild.com/cnb/shop/ftdichip?productID=70&op=catalogue-product_info-null&prodCategoryID=47 FTDI TTL-232R-3V3-AJ (£)]
 * [http://apple.clickandbuild.com/cnb/shop/ftdichip?productID=68&op=catalogue-product_info-null&prodCategoryID=47 FTDI TTL-232R-3V3-WE (£)]

You may need to rewire the terminals of the TTL cables to match your device pinout.

==== USB-serial parts ====

If you want to solder:
 * [http://www.sparkfun.com/commerce/product_info.php?products_id=718 Breakout Board for FT232RL USB to Serial]
 * [http://www.sparkfun.com/commerce/product_info.php?products_id=199 Breakout Board for CP2103 USB to Serial w/ GPIOs].
 * [http://apple.clickandbuild.com/cnb/shop/ftdichip?productID=71&op=catalogue-product_info-null&prodCategoryID=47 FTDI TTL-232R-PCB (£)]
 * [http://apple.clickandbuild.com/cnb/shop/ftdichip?productID=72&op=catalogue-product_info-null&prodCategoryID=47 FTDI TTL-232R-3V3-PCB (£)]

==== Cellphone Data Cables ====

A USB based data cable for a mobile cell phone is another possibility.

Compatible Radio Shack (Future Dial) "Mobile Phone Data Cables" using the Prolific 2303 USB-3.3vSerial converter chip:

 *LG Models 1200, VI5225, VX4500, VX4600, VX600
 *Audiovox Models 8200, 8500 and 8600
 *Nokia Models 3285 and 5185
 *Cable 22 (For Nokia 3100, 3200, 3585i, 3588 and others with Nokia 14-pin pop-port)
 *Cable 32 (For Motorola T720*, T722i, P280, 270c, V60*, V66, V70, V120*)

Ebay clone cables:
 *Datacable for Nokia 6210, 6250, 6310, 6310i, 7110

reference: http://www.nslu2-linux.org/wiki/HowTo/AddASerialPort

=== Level conversion ===

TTL-RS-232 level conversion is a fairly common problem, so there are a number of ICs on the market that convert between these voltage levels.  [http://www.maxim-ic.com Maxim IC] has made a few handy little ICs for us to use. The best (IMHO) is the , or more specifically, the MAX233a, which has a higher speed capacity and uses less power. This guide will tell you how to solder everything together to get a pc-compatible serial port on your OpenWrt router.

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
