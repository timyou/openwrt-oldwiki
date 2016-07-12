= Serial Console =
Serial ports allow you to do a myriad of things, including connect to your computer, connect to other devices such as LCDs and GPSes, etc... With a little programming, you could even connect a bunch of routers together. This mod doesn't '''add''' serial ports; those are already there. This just makes them much easier to use with just about any hardware you want.

For the developer, a serial port will also allow you to recover a bricked router when all other methods have failed (tftp, failsafe mode, shorting pins, etc.) This is something which typically cannot be done with just a USB-capable router and USB-serial adapter, as USB support is only available once the firmware has successfully loaded.

== Serial port pinouts ==
Pinouts for your model can often be found on your model's page in CategoryModel.

== USB Kit ==
You could buy something like [http://www.sparkfun.com/commerce/product_info.php?products_id=718 this] or [http://www.sparkfun.com/commerce/product_info.php?products_id=199 this].

A USB based data cable for a mobile cell phone is another possibility.

note: For the serial console on a WRT54G with a USB cell phone cable, the following pins are used: 4(tx), 6(rx), 10(gnd)

Compatible Radio Shack (Future Dial) "Mobile Phone Data Cables":

 . - LG Models 1200, VI5225, VX4500, VX4600, VX600 - Audiovox Models 8200, 8500 and 8600 - Nokia Models 3285 and 5185 - Cable 22 (For Nokia 3100, 3200, 3585i, 3588 and others with Nokia 14-pin pop-port)

goobay

 . - Datacable for Nokia 6210, 6250, 6310, 6310i, 7110

reference: http://www.nslu2-linux.org/wiki/HowTo/AddASerialPort

== Home-made RS-232 kit ==
'''Background'''

Most OpenWrt compatible devices have one or two* serial ports on the router's PCB (printed circuit board). The problem is they operate on 3.3V, which means '''they will get fried if you connect them to your computer's serial port''', which operates at 12V. Luckily, this is more common a thing than you would think, and as such, Maxim (no, not the magazine) has made a few handy little ICs for us to use. The best (IMHO) is the MAX233, or more specifically, the MAX233a, which has a higher speed capacity and uses less power. This guide will tell you how to solder everything together to get a pc-compatible serial port on your OpenWrt router.

http://jdc.parodius.com/wrt54g/serial.html

http://www.nslu2-linux.org/wiki/HowTo/AddASerialPort

http://www.rwhitby.net/wrt54gs/serial.html

This electronic adaptator is call RS232-TTL converter. You can find it at many places whith this name.

A great source for RS232-TTL convertors is in cell phone serial cables. Most cell phones need this same circuit to level-up for connection to a PC's serial port. Many people already have such a cable laying around, or can buy one fairly cheap. It is much easier than building the necessary circuit yourself.

If you open up the cell phone cable's serial port casing and see a MAX### chip, it's probably the cable you need. One known chip is a MAX323 (yes, 323, the original MAX232 is a 5V device and we need 3.3V here).

If you've found a good cell phone cable to use, you merely need to determine which wires are the VCC, GND, TX, and RX connections. Usually the VCC is red and the GND is black, but the other colors may vary (though blue and orange are common). There should be no need to modify the PCB embedded in the cable.

You can also search for MAX232 Kits. There are some kits available.

 * http://cgi.ebay.fr/RS232-to-TTL-level-Signal-Converter-Kit_W0QQitemZ9703039037QQcategoryZ41995QQssPageNameZWD2VQQrdZ1QQcmdZViewItem,
 * http://www.elv-downloads.de/service/manuals/TTLRS232-Umsetzer/38439-TTLRS232-Umsetzer.pdf
 * http://www.compsys1.com/workbench/On_top_of_the_Bench/Max233_Adapter/max233_adapter.html

*'''Note: '''The WRT54G/GS CFE only emit messages on TTSY0. This is the serial port that uses even numbered pins, therefore starting at pin 2.

== Terminal software ==
 * Hyperterm (comes with many versions of MS Windows)
 * Minicom (for POSIX systems)
 * [http://efault.net/npat/hacks/picocom/ picocom]
 * cu(1) (part of the Taylor UUCP package, for POSIX systems)
 * [http://www.chiark.greenend.org.uk/~sgtatham/putty/ Putty] v0.59 or newer (now with serial console support!)

== Finding Serial Console ==
First, check the OpenWRT wiki page describing your hardware and do a Google search. Most of the time, the serial port(s), if they exist, have already been documented by others.

(stolen from the ["AR7Port"] page) This method used to find the serial port was suggested to me on irc; use a piezo buzzer and attach its ground (usually black) wire to a ground point on the router - the back of the power regulators are usually good candidates, but check this with a multimeter/voltmeter... Use the other wire to probe any of the header pins which may be pre-installed, or any of the component holes which look like they could have header pins installed into. Once you get the right pin, the piezo should make a screeching sound much like that of a 56kbps connection.

Make sure you reset the router after probing each pin. The bootloader/linux bootup messages will only happen for a few seconds, after that the serial console will be silent - so even if you have the right pin you will not hear anything.

A more accurate method would be to use either a logic analyzer or an oscilloscope, but these are expensive and for the basic task of locating a serial pin a little overkill. ;-)

== Use your old PDA as console ==
When you own an old PDA (for example Palm series) you may solder your rx/tx level signals from the openwrt box to the pda ttl level serial connectors. I made this with an Palm IIIc, [http://www.neophob.com/serendipity/index.php?url=archives/121-Reuse-your-old-Palm-as-Serial-Console.html].
