'''Netgear WGT634U'''

The WGT634U is based on the Broadcom 5365 board. It has a 200MHz CPU, 8Mb flash and 32Mb RAM.
The wireless NIC is an Atheros mini-PCI, and it also has an USB2.0 controller.

== Status of OpenWrt ==

We now have a working Kernel 2.6.12.5 in CVS development tree. For trying a snapshot of OpenWrt you need
a serial connection.

You will find snapshots here (may be next week): http://downloads.openwrt.org/people/wbx/netgear/

If you compile on your own, please only use squashfs images. You can flash via tftp, you need to run a tftp server:<br>
ifconfig eth0 -addr=10.23.23.2 -mask=255.255.255.0; flash -noheader 10.23.23.29:openwrt-wgt634u-2.6-squashfs.bin flash0.os

ATTENTION: CVS jffs2 builds will brick your router (it will erase the NVRAM settings needed by CFE)

Use one of the bin files.


TODO:<br>
  integration of kernel 2.6 to buildsystem [done]<br>
  integration of kernel drivers, thx jolt [done]<br>
  LZMA Loader [done]<br>
  new Flash Map driver [partially]<br> 
  network driver [done]<br>
  OpenWrt startup scripts [not working, need to be fixed]<br>
  vlan configuration<br>
  wireless driver [partially]<br>
  usb driver<br>

== Other projects and information ==

More info in the forum: --> http://openwrt.org/forum/viewtopic.php?id=33

External developer's Wiki: http://wgt634u.nomis52.net/

OpenWGT project --> http://openwgt.informatik.hu-berlin.de/

Another firmware project --> http://router.4th.be/
