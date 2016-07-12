'''Linksys WRT54GS'''


[[TableOfContents]]


=== Hardware versions ===

There are six versions of the WRT54GS. All of them are based on the 4712 board. They
have a 200 MHz CPU, 8 MB flash and 32 MB RAM (except v4). You can get the version number
from the sticker on the bottom of the device. All revisions are supported by OpenWrt 1.0
(White Russian) and later.


===== Identification by S/N =====

Useful for identifying shrinkwrapped units. The '''S/N''' can be found on
the box, below the UPC barcode.
||||<tablestyle="width 50%"> (!) '''Please contribute to this list.''' (!) ||||'''!OpenWrt'''||
||'''Model'''||<:> '''S/N'''||<:>  '''Stable[[BR]]White Russian'''||<:>  '''Unstable[[BR]]development'''||
||<(|2>WRT54GS v1.0||<:> CGN0||<:|2> (./) ||<:|2> (./) ||
||<:> CGN1||
||WRT54GS v1.1||<:> CGN2||<:> (./) ||<:> (./) ||
||WRT54GS v2.0||<:> CDF3||<:> (./) ||<:> (./) ||
||WRT54GS v2.1||<:> CDF4||<:> (./) ||<:> (./) ||
||WRT54GS v3.0||<:> CDF5||<:> (./) ||<:> (./) ||
||WRT54GS v4.0||<:> CDF6||<:> (./) ||<:> (./) ||


==== WRT54GS v1.0 ====

The WRT54GS v1.0 uses an ADM6996 switch and SDRAM.


==== WRT54GS v1.1 ====

The WRT54GS v1.1 uses a BCM5325 switch and DDR-SDRAM.


==== WRT54GS v2.0 ====

The WRT54GS v2.0 uses a BCM5325EKQM switch and a BCM4712LKFB processor.


==== WRT54GS v2.1 ====

The WRT54GS v2.1 also uses a BCM5325EKQM switch and a BCM4712LKFB processor.


==== WRT54GS v3.0 ====

The WRT54GS v3.0 uses a Broadcom 5352 CPU with integrated Switch.


==== WRT54GS v4.0 ====

'''NOTE:''' v4.0 only has 4 MB Flash and 16 MB RAM. Half of prior versions.
Some WRT54GS v4 has 8 MB flash and 32 MB RAM, only first relase of WRT54GS v4
had 4MB/16MB.


=== Detailed hardware info ===

==== Motherboard photos ====

Nice hardware info with precise [http://wiki.version6.net/WRT54GS pictures].


==== Power requirements ====

The following tests were conducted on a Linksys WRT54GS v2.0 hardware platform,
hooked up to a lab PSU. All measurements are accurate +/-0.01 A


===== Normal operation =====

In idle mode, radio off: 0.36 A
In idle mode, radio on: 0.45 A

('''NOTE:''' this also means one can follow the boot process nicely from the current
draw... perhaps this could be usefull in debugging? Morse error messages on the amp
meter, I think I'm getting carried away).

Inserting or retracting a networking cable gives a ~2 s peak of 0.02 A

When one lowers the input voltage, the current draw increases so the total power is
always arround 5.3 W (+/-0.1 W) At arround 4 volt the router stops responding. This
was tested running lots of md5sums on a file (should show memory and CPU problems).
Presumably, the internal DC-DC converter can't up the voltage enough anymore at that
level.

If anyone is willing to risk his router for a high-voltage measurement, let me know.
(email to joris in the v5.be domain)

A WRT54GS1.1 uses AD1509 voltage regulators for the 5 V and 3.3 V rails. These have a
maximum operating input voltage of 22 V so theoretically, anything below that should be
ok.


===== Battery tests =====

The measurements above show the wrt should behave exellent on batteries.

Why don't we try that in a real life test :)

I'm hooking up the wrt to a new, fully charged, 12V lead-acid car battery, rated 42 AH
(skinny geeks shouldn't carry arround those kind of batteries).
... 5 days later: the Wrt behaved exellent! It remained up and running for 4 days and
13 hours on the battery.
It should be noted that I measured the voltage only regularly during the first 3 days,
during wich it dropped only arround 0.8 V. Presumably, the battery used is rather good
at keeping the voltage...

We have run a Wrt for 6 weeks on a lead-acid battery, charger, generator combination
with no problems. Power was cut due to legal problems concerning the site the AP was on.
The only time the unit was down was when we had power restored.
