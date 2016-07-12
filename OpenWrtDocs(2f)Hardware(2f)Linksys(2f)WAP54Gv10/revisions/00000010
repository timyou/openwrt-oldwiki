'''WAP54G version 1.0'''

This info is relevant '''ONLY''' to the version 1.0 of WAP54G.

See also more general page ["OpenWrtDocs/Hardware/Linksys/WAP54G"]

== Problem of PCB design ==
There is missing weak pulldown on pin 5 ISO/RXER of AC101L PHY chip. PHY chip enters "isolate" mode after PHY reset.

It means that ethernet driver not aware of that problem can receive only. Transmitted packets get lost on MII interface and never go outside.

That is why some firmwares (even one version from LinkSys probably) do not work.

Not all v1.0 devices suffer from this problem because it is triggered by logic value read from floating CMOS input - and it can read mostly low, mostly high or random at all. I tested two MDG0048..... devices with the problem and recived reports about 3 working devices with S/N MDG003.......

I (AlexanderKostadinov) have one MDG0033... working and one MDG0037... not working.

=== Software workaround ===
Driver should reset "isolate" state of PHY chip.

et driver was patched in version kernel-source-et-0.13.tar.gz

b44 driver was patched in svn r2932.

OpenWrt White Russian RC5 is patched but workaround is not activated due to [#cr_in_nvram DOSish nvram defaults]. RC6 will hopefully sort it out. (Comment HansWernerHilse: In my case, RC5 answered to ARP queries. So the fix probably does work. However, RC5 bricked - temporarily - my V1.0., so I vote against it.)

=== PMON ===
PMON (version 5.3.22) on 3 devices I tested has the same problem. boot_wait do not work even if properly enabled. As device has no JTAG header I am no so brave to experiment with reflashing PMON.

I (AlexanderKostadinov) have at least 2 devices with working boot_wait and 2 with not working...

=== Hardware solution ===
'''!!!WARNING!!!''' If you are not experienced in soldering SMD or do not know how to protect against [http://en.wikipedia.org/wiki/Electrostatic_discharge ESD] do no try that. As usual everything is on your own risk '''!!!WARNING!!!'''

Add a resistor of value between 10 and 100 kohms from pin 5 of AC101L chip to the ground. Instead of tiny pin 5 use either side of SMD resistor R28. Use one side of R6 (far from AC101L) as ground.

==== Quick and dirty hack ====
 * Power off the device. Dismount.
 * Ground yourself electrically (touching metal shielding on miniPCI).
 * Keep touching shielding and firmly touch area around AC101L pin 5 (side of chip nearest to front of AP).
 * Keep touching and power on.
 * Keep touching until the initialization is done (3 seconds for PMON)
If boot_wait is on, ping and tftp should work now.

(Comment HansWernerHilse: Worked on first try. Note that my fingertip probably touched all adjacent resistors plus a whole set of pins of the AC101L, although I tried to press as lightly as possible. Note that I got the position to press upon from the description of the "Hardware Solution" above. My body was grounded during the whole procedure.)

(Comment [http://www.snowlark.com Snowlark]: This worked PERFECTLY! One additional upgrade, if you get a twisty-tie with a metal core and plastic outer, very similar to 24gauge wire, you can just strip the coating away on both ends, ground to the shield on the edge of the board, and then touch pin 5 - worked for me! First time was a charm. Then, I did a hard-reset [1 minute reset button hold down] just to be sure, then accessed the LinkSys config via the browser utilizing IP 192.168.1.245 with 'admin' password. ['''FYI''' - I'm an ex-USAF EE -- we use coated metal instead of human fingers -- things can get ugly sometimes!])

=== Blind TFTP ===
Fortunately TFTP protocol can be violated to transfer an image without any feedback from device. It is the only way how to use boot_wait without dismounting device or flashing PMON. See http://forum.openwrt.org/viewtopic.php?id=3591

[[Anchor(cr_in_nvram)]]

== DOSish NVRAM defaults ==
Most of NVRAM default values are stored with '\r' (CR) character appended. This can also make a big problem in firmware as the device is not identified correctly.

To go around, try setting manually with the same values nvram variables boardtype and boardnum.

TO DEVELOPERS: Take extra care when testing NVRAM values, especially boardtype and boardnum Command {{{nvram get}}} and {{{nvram show}}} is now patched to filter out apended '\r'. You have to filter out '\r' in C code using value returned by {{{nvram_get()}}}.
