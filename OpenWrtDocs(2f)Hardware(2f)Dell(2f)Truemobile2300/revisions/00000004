= Description =

The Dell !TrueMobile 2300 is based on the BCM4702KPB SoC, a Mini-PCI BCM94306MP
radio and a BCM5325MA2KQM switch.  In many respects it is similar to the
[:OpenWrtDocs/Hardware/Linksys/WRT54G: Linksys WRT54G] v1.  Like most
BCM4710-based platforms the stock firmware is Linux-based. The device
also contains the defacto standard of 4MiB Flash and 16MiB RAM.

= Installing OpenWrt =

The initial installation of OpenWrt is accomplished by uploading a
.trx image through the Dell firmware.  Once OpenWrt is installed
it is a good idea to set the ''boot_wait'' NVRAM variable to ''on''.

= Serial port? =

It is unknown if a serial header exists on this model.  There is an
unpopulated header near the Flash IC that may contain JTAG and/or
serial lines.  Further investigation will be required.

= Sources =

Dell has released source code of the Dell !TrueMobile 2300 (Broadcom based) here:

http://linux.dell.com/files/truemobile/tm2300/Linux_source_code.tar.gz

= Bootloader's default NVRAM settings =

Obtained by running `strings` on `/dev/mtd/0ro`

{{{
boardtype=bcm94710ap
boardnum=44
clkfreq=125
sdram_init=0x0419
sdram_config=0x0000
sdram_refresh=0x8040
et0macaddr=00:90:4c:49:00:2c
et0phyaddr=30
et0mdcport=0
et1macaddr=00:90:4c:4a:00:2c
et1phyaddr=1
et1mdcport=1
dl_ram_addr=a0001000
os_ram_addr=80001000
os_flash_addr=bfc40000
lan_ipaddr=192.168.2.1
tftp_ipaddr=192.168.2.1
lan_netmask=255.255.255.0
scratch=a0180000
boot_wait=on
watchdog=1000
}}}

Your NVRAM will be set to this if the firmware finds the NVRAM partition corrupt.
Also, these variables are likely essential to the boards functioning,
so it's a good idea not to unset them.

----
CategoryModel
