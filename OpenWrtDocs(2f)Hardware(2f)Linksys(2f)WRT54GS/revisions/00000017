'''Linksys WRT54GS'''

=== Hardware versions ===
There are three versions of the WRT54GS. All of them are based on the 4712 board. They have a 200MHz CPU, 8Mb Flash and 32Mb RAM. You can get the version number from the sticker on the bottom of the device. If you are unsure about the version number, just give it a try, the file upload will automatically be cancelled if your device is not supported.

==== WRT54GS v1.0 ====
The WRT54GS v1.0 uses an ADM6996 switch and SDRAM. These units are fully supported by OpenWrt.
The device can be identified by ModelName WRT54GS or WRT54GS-XX, where XX should be a 
country toplevel domain code (EU, DE, ...).

==== WRT54GS v1.1 ====
The WRT54GS v1.1 uses a BCM5325 switch and DDR-SDRAM. These units are supported in the EXPERIMENTAL branch of OpenWrt.

==== WRT54GS v2.0 ====
We have no information about the internals of these units, yet. As noone saw a v2.0, yet we can't be sure, but it should work with the EXPERIMENTAL branch of OpenWrt.


=== Detailed hardware info ===

==== Motherboard photos ====
Nice hardwer info with precise picture http://wiki.version6.net/WRT54GS

==== Power requirements ====
The following tests were conducted on a linksys wrt54GS v2.0 hardware platform, hooked up to a lab psu.
All measurements are accurate +/-0.01A

===== Normal operation =====
In idle mode, radio off: 0.36A
In idle mode, radio on: 0.45A

(note: this also means one can follow the boot process nicely from the current draw... perhaps this could be usefull in debugging? Morse error messages on the amp meter, I think I'm getting carried away)

Inserting or retracting a networking cable gives a ~2s peak of 0.02A

When one lowers the input voltage, the current draw increases so the total power is always arround 5.3W (+/-0.1W)
At arround 4V the wrt stops responding. This was tested running lots of md5sums on a file (should show memory and cpu problems).
Presumably, the internal DC-DC converter can't up the voltage enough anymore at that level.

If anyone is willing to risk his wrt for a high-voltage measurement, let me know. (email to joris in the v5.be domain)

===== Battery tests =====

The measurements above show the wrt should behave exellent on batteries.

Why don't we try that in a real life test :)

I'm hooking up the wrt to a new, fully charged, 12V lead-acid car battery, rated 42AH (skinny geeks shouldn't carry arround those kind of batteries).
... 5 days later: the wrt behaved exellent! It remained up and running for 4 days and 13 hours on the battery.
It should be noted that I measured the voltage only regularly during the first 3 days, during wich it dropped only arround 0.8V. Presumably, the battery used is rather good at keeping the voltage...



We have run a WRT for 6 weeks on a Lead Acid battery, charger, generator combination with no problems. Power was cut due to legal problems concerning the site the AP was on. The only time the unit was down was when we had power restored.
