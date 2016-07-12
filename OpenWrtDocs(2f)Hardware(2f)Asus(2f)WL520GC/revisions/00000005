= Asus WL-520GC =

{{{
SoC: BCM5354
SDRAM: 16MB
Flash: 2MB
Wi-Fi: in SoC
}}}

== Serial pinout ==

{{{
[x] GND
[x] TX
[x] RX
[x] VCC


LED
}}}

== Flashing OpenWrt ==

You can flash the '''openwrt-brcm-2.4-squashfs.trx''' file to your Asus WL-520GC device. The device has 192.168.4.1 as the default IP address.

It seems like the 2.4 version has some troubles accessing the flash and this will actually make the board hang after a while.

brcm47xx-2.6 does not have the same issue and works fine on this device. b43 will make the board reboot as soon as it is loaded.
