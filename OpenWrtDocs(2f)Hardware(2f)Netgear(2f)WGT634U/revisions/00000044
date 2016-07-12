'''Netgear WGT634U'''

The WGT634U is based on the Broadcom 5365P board. It has a 200 MHz CPU, 8 MB flash
and 32 MB RAM. The wireless NIC is an Atheros Mini-PCI, and it also has an USB 2.0
controller.


== Status of OpenWrt ==

We now have a working Kernel 2.6.12.5 in our development tree. For trying a snapshot
of OpenWrt you need a serial connection. You will find snapshots here:
[http://downloads.openwrt.org/people/wbx/netgear/]

You can flash the snapshots via TFTP. You need to run a TFTP server on your local PC
connected to the WAN port of the Netgear router. To get into the bootloader of the
router by holding down {{{CTRL+C}}} while power on. The following CFE command is used
to write the snapshots ({{{.bin}}} files) to the flash. Your PC is configured as
{{{192.168.1.2}}}.

{{{
ifconfig eth0 -addr=192.168.1.1 -mask=255.255.255.0
flash -noheader 192.168.1.2:openwrt-wgt634u-2.6-squashfs.bin flash0.os
}}}

Flashing may take over a minute. After that you can use {{{reboot}}} to start !OpenWrt.

Please only use these snapshots if you like to help to get this !OpenWrt port working.
There is still a lot of work. See the TODO list.

If you have any suggestions or patches, please send wbx (wbx@openwrt.org) an e-Mail.


== TODO ==

 * reset button driver [need to be ported to 2.6]
 * wireless driver [sometimes kernel oops if iwconfig is used]
 * USB driver [EHCI needs to be fixed]
  * EHCI driver is not working (writing to high speed devices freeze the USB stack) and
  gives the following error:
  {{{
root@OpenWrt:/# mount -t ext3 /dev/scsi/host0/bus0/target0/lun0/part1 /mnt
ioctl_internal_command: <0 0 0 0> return code = 8000002
   : Current: sense key=0x0
    ASC=0x0 ASCQ=0x0
  }}}
  * OHCI driver is working, try kmod-ohci
 * webupgrade from original firmware [need a CRC header]


== Configuration ==

The !OpenWrt port for Netgear WGT634U will '''not''' use any NVRAM configuration.
Everything is configured in {{{/etc}}}. For network configuration please modify
{{{/etc/config/network}}}. The NVRAM partition is your old config partition, so please
back it up. You eventually need it to restore your original firmware.


== Restoring original firmware ==

You can use TFTP for the original images:

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

Because it seems CFEs TFTP client will only read 4194304 bytes from the TFTP server, version
1.4.1.10 will not work using this method. It just happens that 1.4.1.9 doesn't have important
data in the unread area of the image.


== Serial console ==

Default parameters for the serial console are 115200 N81. You need a
[http://www.maxim-ic.com/quick_view2.cfm/qv_pk/1068 MAX3232] chip to get the console
working.

J6 (left from J7) looks like a second serial port, but has no header on it.

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

 * More info in the forum:
 [[BR]]- [http://openwrt.org/forum/viewtopic.php?id=33]

 * External developer's Wiki
 [[BR]]- [http://wgt634u.nomis52.net/]

 * OpenWGT project
 [[BR]]- [http://openwgt.informatik.hu-berlin.de/]

 * Another firmware project
 [[BR]]- [http://router.4th.be/]
