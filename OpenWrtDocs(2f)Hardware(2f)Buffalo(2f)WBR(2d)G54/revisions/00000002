= Buffalo WBR-G54 =

== Installation ==

Used the same TFTP method as for the WBR2-G54 : the only difference is that the TTL during the bootloader is 128 and not 100.

== Wireless config ==

The old Buffalo 2.20 firmware (newest available for the WBR-G54) uses the older wl*_ nvram settings convention. My wireless config took a lot of fiddling to get working for some reason, so I was keen to preserve it.

I dumped the wl*_ settings, edited them to be wl0_* istead, and scripted them back into the nvram. One "wifi" later, hey presto, working wireless.

== Restoring Buffalo firmware ==

As per the manual except that 34 bytes not 32 need to be trimmed from the front of the file WBR-G54_2.20_1.16 which is obtained from Buffalo's website.
