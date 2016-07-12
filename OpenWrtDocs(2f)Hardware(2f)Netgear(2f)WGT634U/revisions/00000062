= Netgear WGT634U =

The WGT634U is based on the Broadcom 5365P board. It has a 200 MHz CPU, 8 MB flash
and 32 MB RAM. The wireless NIC is an Atheros Mini-PCI capable of 802.11b/g, and it
also has an USB 2.0 controller.


== Status of OpenWrt ==

The kernel boots on the system, we have drivers for the ethernet interface (b44) and
the new switch driver is integrated (robocfg will be obsolete). We have drivers for the
wireless radio (madwifi). Recently we updated to 2.6.15 to play with 2.6 on Linksys
hardware. 

If you want to help with development, attach a serial console and build an image from
Subversion (Kamikaze). Choose "Broadcom BCM47xx/53xx [2.6]" in make menuconfig.


== Upgrading using the web interface ==

If you want to upgrade to OpenWrt using the web interface, you need to download a special
config file and upload it to your router using the '''Backup Settings''' option.

The file is available here: http://downloads.openwrt.org/utils/wgt634u-upgrade.cfg

After that, clear your browser cache, give the router some time to reboot, and then you should
find a new entry in the menu bar, called '''Upgrade to OpenWrt'''. Use this function to upload
the OpenWrt WGT634U image to the router. After a while it should be reachable under the default
IP {{{192.168.1.1}}}


== Upgrading using the serial console ==

Images smaller than 4MB can be flashed via TFTP. You need to run a TFTP server on your
local PC.

  * attach a serial console cable to the wgt634u
  * attach ethernet to the WAN port (next to the USB socket)
  * hold down {{{CTRL-C}}} while inserting power to enter CFE
  * configure ethernet from CFE (e.g. with a local DHCP server):

  {{{CFE> ifconfig eth0 -auto
Device eth0:  hwaddr 00-0F-B5-97-1C-3D, ipaddr 192.168.0.200, mask 255.255.255.0
        gateway 192.168.0.1, nameserver 192.168.0.1, domain foo.com
*** command status = 0}}}

  * for manual configuration use something like this:

  {{{
ifconfig eth0 -addr=192.168.1.250 -mask=255.255.255.0
}}}

  * then, flash the new squashfs.bin image:

  {{{CFE> flash -noheader 192.168.0.3:wgt634u/openwrt-wgt634u-2.6-squashfs.bin flash0.os
Reading 192.168.0.3:wgt634u/openwrt-wgt634u-2.6-squashfs.bin: Done. 1892352 bytes read
Programming...done. 1892352 bytes written
*** command status = 0}}}

  * reboot with

  {{{
CFE> reboot
}}}


Flashing may take over a minute. After that you can use {{{reboot}}} to start !OpenWrt.

Please always use the newest subversion code. 

Report any bugs via the https://dev.openwrt.org

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


== Configuration ==

The !OpenWrt port for Netgear WGT634U will '''not''' use any NVRAM configuration.
Everything is configured in {{{/etc}}}. For network configuration please modify
{{{/etc/config/network}}}. The NVRAM partition is your old config partition, so please
back it up. You eventually need it to restore your original firmware.


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
