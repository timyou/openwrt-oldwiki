'''WAP54G version 1.0'''

This info is relevant '''ONLY''' to the version 1.0 of WAP54G.

See also more general page [:OpenWrtDocs/Hardware/Linksys/WAP54G]

== Problem of PCB design ==

There is missing weak pulldown on pin 5 ISO/RXER of AC101L PHY chip.
PHY chip enters "isolate" mode after PHY reset.

It means that ethernet driver not aware of that problem can receive only. Transmitted packets get lost on MII interface and never go outside.

That is why some firmwares (even one version from LinkSys probably) do not work.

=== Software workaround ===

Driver should reset "isolate" state of PHY chip.

et driver was patched in version kernel-source-et-0.13.tar.gz

b44 driver was patched in svn r2932.

OpenWrt White Russian RC5 will hopefully include the patch.

=== PMON ===

PMON (version 5.3.22) on 3 devices I tested has the same problem.
boot_wait do not work even if properly enabled. As device has no JTAG header I am no so brave to experiment with reflashing PMON.

If you have version 1.0 with working boot_wait, please report here.

=== Hardware solution ===

'''!!!WARNING!!!''' If you are not experienced in soldering SMD or do not know how to protect against [http://en.wikipedia.org/wiki/Electrostatic_discharge ESD] do no try that. As usual everything is on your own risk '''!!!WARNING!!!'''

Add a resistor of value between 10 and 100 kohms from pin 5 of AC101L chip to the ground.
Instead of tiny pin 5 use either side of SMD resistor R28. Use one side of R6 (far from AC101L) as ground.

==== Quick and dirty hack ====

 * Power off the device. Dismount.
 * Ground yourself electrically (touching metal shielding on miniPCI).
 * Keep touching shielding and firmly touch area around AC101L pin 5 (side of chip nearest to front of AP).
 * Keep touching and power on.
 * Keep touching until eth initialization is done (3 seconds for PMON)

If boot_wait is on, ping and tftp should work now.

=== Blind TFTP ===

Fortunately TFTP protocol can be violated to transfer an image without any feedback from device.
It is the only way how to use boot_wait without dismounting device or flashing PMON.
See http://forum.openwrt.org/viewtopic.php?id=3591


== DOSish NVRAM defaults ==

Most of NVRAM default values are stored with '\r' (CR) character appended.
This can also make a big problem in firmware as the device is not identified correctly.

TO DEVELOPERS:
Take extra care when testing NVRAM values, especially boardtype and boardnum
Command nvram get and nvram show is now patched to filter out apended '\r'.
You have to filter out '\r' in C code using value returned by nvram_get().
