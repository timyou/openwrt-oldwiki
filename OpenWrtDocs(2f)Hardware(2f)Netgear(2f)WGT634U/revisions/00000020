'''Netgear WGT634U'''

The WGT634U is based on the Broadcom 5365 board. It has a 200MHz CPU, 8Mb flash and 32Mb RAM.
The wireless NIC is an Atheros mini-PCI, and it also has an USB2.0 controller.

== Status of OpenWrt ==

We now have a working Kernel 2.6.12.5 in CVS development tree. For trying a snapshot of OpenWrt you need
a serial connection. You will find snapshots here: http://downloads.openwrt.org/people/wbx/netgear/

You can flash via tftp, you need to run a tftp server (connect the wan port to the tftp system):

ifconfig eth0 -addr=10.23.23.2 -mask=255.255.255.0; flash -noheader 10.23.23.29:openwrt-wgt634u-2.6-squashfs.bin flash0.os

Use one of the bin files. Please only use these snapshots if you like to help to get this OpenWrt port working. There is still a lot of work. See the TODO list.
If you have any suggestions or patches for CVS HEAD, please send wbx (wbx@openwrt.org) an e-Mail.

TODO:
 * integration of kernel 2.6 to buildsystem [done]
 * integration of kernel drivers, thx jolt [done]
 * LZMA Loader [done]
 * new Flash Map driver [done]
 * network driver [done]
 * OpenWrt startup scripts [done]
 * vlan configuration [need to be tested, robocfg fails]
 * wireless driver [need to be tested, kernel oops if iwconfig is used]
 * usb driver [need to be tested]
 * led driver [partially]
 * update with mtd [works]
 * installation via webupgrade from original firmware [need to be tested]

== Serial console ==

Default parameters for the serial console are: 115200, N, 8, 1

[[BR]]You need a MAX3232 chip to get the console working.

[[BR]]J6 (left from J7) looks like a second serial port, but has no header on it.

{{{
------------------------------------------
| |     |    LAN-Ports   |          |    |
|       ------------------               |
|                                        |
|                                        |
|                                VCC .   |
|                                TX  .   |
|                                RX  .   |
|                                GND .   |
|                                    J7  |
|                           FLASH        |
|                                        |
------------------------------------------
   |    |     |     |     |     |     |
}}}

== Other projects and information ==

More info in the forum: --> http://openwrt.org/forum/viewtopic.php?id=33

External developer's Wiki: http://wgt634u.nomis52.net/

OpenWGT project --> http://openwgt.informatik.hu-berlin.de/

Another firmware project --> http://router.4th.be/
