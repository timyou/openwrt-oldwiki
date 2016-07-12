= Netgear WGT634U =

The WGT634U is based on the Broadcom 5365P board. It has a 200 MHz CPU, 8 MB flash
and 32 MB RAM. The wireless NIC is an Atheros Mini-PCI capable of 802.11b/g, and it
also has an USB 2.0 controller.


== Status of OpenWrt ==

The kernel boots on the system, we have drivers for the ethernet interface (b44). 
We are working on including a new switch driver (robocfg will be obsolete). We have 
drivers for the wireless radio (madwifi). Recently we updated to 2.6.15rc5 to play with 2.6 
on Linksys hardware. The OpenWrt port is still unusable for users!

If you want to help with development, attach a serial console and build an image from
subversion. Choose brcm-2.6 in make menuconfig.

Images can be flashed via TFTP. You need to run a TFTP server on your local PC
connected to the WAN port of the Netgear router. To get into the bootloader of the
router by holding down {{{CTRL+C}}} while power on. The following CFE command is used
to write the snapshots ({{{.bin}}} files) to the flash. Your PC is configured as
{{{192.168.1.2}}}.

{{{
ifconfig eth0 -addr=192.168.1.1 -mask=255.255.255.0
flash -noheader 192.168.1.2:openwrt-wgt634u-2.6-squashfs.bin flash0.os
}}}

Flashing may take over a minute. After that you can use {{{reboot}}} to start !OpenWrt.

== TODO ==
 
 * add new switch drivers and test on 2.4/2.6
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
 * fix networking by getting hotplug system to work on non-nvram systems
 * reset button driver [need to be ported to 2.6]
 * webupgrade from original firmware [need a CRC header]


== Configuration ==

The !OpenWrt port for Netgear WGT634U will '''not''' use any NVRAM configuration.
Everything is configured in {{{/etc}}}. For network configuration please modify
{{{/etc/config/network}}}. The NVRAM partition is your old config partition, so please
back it up. You eventually need it to restore your original firmware.

=== This Works For Me ===

 I have successfully flashed the experimental kamikaze tree to the WGT.  Here is the method that I used (if your method is better, please replace this --RussellSenior):

  * attach a serial console cable to the wgt634u
  * attach ethernet to the WAN port (next to the USB socket)
  * hold down Ctrl-C while inserting power to enter CFE
  * configure ethernet from CFE (I have a dhcp server that does the work for me):

  {{{CFE> ifconfig eth0 -auto
Device eth0:  hwaddr 00-0F-B5-97-1C-3D, ipaddr 192.168.0.200, mask 255.255.255.0
        gateway 192.168.0.1, nameserver 192.168.0.1, domain foo.com
*** command status = 0}}}

  * on the host machine, construct an erasing image in two parts, sized to be TFTP-able:

  {{{$ dd bs=128k if=/dev/zero count=30 | tr '\000' '\377' > wipe-1.img
$ dd bs=128k if=/dev/zero count=29 | tr '\000' '\377' > wipe-2.img}}}

  * put the wipe-1.img and wipe-2.img into the right place.  I used tftpd-hpa, which on Debian uses /var/lib/tftpboot/ by default.  I put the wipe-*.img files and the buildroot's bin/openwrt-wgt634u-2.6-squashfs.bin in /var/lib/tftpboot/wgt634u/.  My tftp server is at 192.168.0.3.

  * from CFE, flash the wipe images in turn:

  {{{CFE> flash -noheader 192.168.0.3:wgt634u/wipe-1.img flash0.os
Reading 192.168.0.3:wgt634u/wipe-1.img: Done. 3932160 bytes read
Programming...done. 3932160 bytes written
*** command status = 0
CFE> flash -noheader -offset=3932160 192.168.0.3:wgt634u/wipe-2.img flash0.os
Reading 192.168.0.3:wgt634u/wipe-2.img: Done. 3801088 bytes read
Programming...done. 3801088 bytes written
*** command status = 0}}}

  * then, flash the new squashfs.bin image:

  {{{CFE> flash -noheader 192.168.0.3:wgt634u/openwrt-wgt634u-2.6-squashfs.bin flash0.os
Reading 192.168.0.3:wgt634u/openwrt-wgt634u-2.6-squashfs.bin: Done. 1892352 bytes read
Programming...done. 1892352 bytes written
*** command status = 0}}}

  * reboot:

  {{{CFE> reboot}}}

  * NOTE: r2794 booted for me; r2836 kernel panic'd with "Kernel panic - not syncing: Attempted to kill init!"

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

Because it seems CFEs TFTP client will only read 4194304 bytes from the TFTP server, version 1.4.1.10 will not work using this method.  To get around the 4MB limit, we can split larger images into smaller chunks and then use the -offset flag to flash the parts.  E.g. 

{{{
CFE> flash -noheader tftp_host:foo.img.1 flash0.os
Reading tftp_host:foo.img.1: Done. 3932160 bytes read
Programming...done. 3932160 bytes written
*** command status = 0
CFE> flash -noheader -offset=3932160 tftp_host:foo.img.2 flash0.os
Reading tftp_host:foo.img.2: Done. 786256 bytes read
Programming...done. 786256 bytes written
*** command status = 0
}}}

== Serial console ==

Default parameters for the serial console on J7 are 115200 N81. You need a [http://www.maxim-ic.com/quick_view2.cfm/qv_pk/1068 MAX3232] chip (or one of the alternatives, such as cell phone data cables) to get the console working.

J6 (left from J7) is a second serial port, but has no header on it. It has the same pinout as J7.

{{{
------------------------------------------
| |     |    LAN-Ports   |          |    |
|       ------------------               |
|                                        |
|        USB                             |
|                         VCC .  VCC .   |
|  WiFi                    TX .  TX  .   |
|                 CPU      RX .  RX  .   |
|         RAM             GND .  GND .   |
|                             J6     J7  |
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
----
CategoryModel
