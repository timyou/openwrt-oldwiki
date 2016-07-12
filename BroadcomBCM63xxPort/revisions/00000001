[[TableOfContents]]
= Status of the Broadcom 63xx port of OpenWrt =

== What is this Broadcom 63xx stuff? ==

[http://www.broadcom.com/products/DSL/xDSL-CPE-Solutions/BCM6348 Broadcom63xx SoC] integrates ADSL/ADSL2+ features, routing, and external Wireless NIC.

== Finished tasks ==

The support for Broadcom 63xx is at this state :

   * Linux 2.6.16.7 kernel booting

== TODO ==

   * Fix MTD/Flash map driver (need special table for CFE and RedBoot devices)
   * Try to run binary drivers with CONFIG_VERSIONING set on

== Firmware/Bootloader ==

Some devices use RedBoot such as Inventel Liveboxes. Other run CFE with a built-in LZMA decompressor such as Siemens SE515, Free Freebox ...

= How to help =

   * Create valid firmware images. 

   * Test the currently merged kernel in order to see if it boots on CFE based boards. It currently does not receives the MTD map from RedBoot (maybe wrong sector number).
----
CategoryOpenWrtPort
