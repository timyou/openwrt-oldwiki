'''Netgear WGT634U'''

The WGT634U is based on the Broadcom 5365P board. It has a 200MHz CPU, 8Mb flash and 32Mb RAM.
The wireless NIC is an Atheros mini-PCI, and it also has an USB2.0 controller.

== Status of OpenWrt ==

We now have a working Kernel 2.6.12.5 in CVS development tree. For trying a snapshot of OpenWrt you need
a serial connection. You will find snapshots here: http://downloads.openwrt.org/people/wbx/netgear/

You can flash the snapshots via tftp. You need to run a tftp server on your local PC connected to the wan port of the Netgear router.
To get into the bootloader of the router by holding down Control-C while power on. The following CFE command is used to write the snapshots (.bin files)
to the flash. Your PC is configured as 192.168.1.2.

ifconfig eth0 -addr=192.168.1.1 -mask=255.255.255.0; flash -noheader 192.168.1.2:openwrt-wgt634u-2.6-squashfs.bin flash0.os

After that you can use "reboot" to start OpenWrt.

Please only use these snapshots if you like to help to get this OpenWrt port working. There is still a lot of work. See the TODO list.
If you have any suggestions or patches for CVS HEAD, please send wbx (wbx@openwrt.org) an e-Mail.

TODO:
 * integration of kernel 2.6 to buildsystem [done]
 * integration of kernel drivers, thx jolt [done]
 * LZMA Loader [done]
 * new Flash Map driver [done]
 * network driver [done]
 * OpenWrt startup scripts [done]
 * pppoe [done]
 * update with mtd and trx files [done]
 * vlan configuration [done] 
 * reset button driver [need to be ported to 2.6]
 * wireless driver [need to be tested, sometimes kernel oops if iwconfig is used, need new wificonf in HEAD, -> nbd ]
 * usb driver [need to be tested]
 * webupgrade from original firmware [need a crc header]


== Configuration ==

The OpenWrt port for Netgear WGT634U will not use any nvram configuration. Everything is configured in /etc. For network configuration please modify /etc/config/network.
The nvram partition is your old config partition, so please back it up. You eventually need it to restore your original firmware.

== Restoring original firmware ==

You can use tftp for the original images:

{{{
CFE> setenv -p kernel_args "console=ttyS1,115200 root=/dev/ram0 init=linuxrc rw syst_size=8M"
*** command status = 0
CFE> ifconfig eth0 -addr=192.168.1.1 -mask=255.255.255.0;
Device eth0:  hwaddr 00-0F-B5-0E-49-D6, ipaddr 192.168.1.1, mask 255.255.255.0
        gateway not set, nameserver not set
*** command status = 0
CFE> flash -noheader 192.168.1.2:wgt634u_1_4_1_9.img flash0.os
Reading 192.168.1.2:wgt634u_1_4_1_9.img: Done. 4194304 bytes read
Programming...done. 4194304 bytes written
*** command status = 0
CFE> reset
}}}

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
