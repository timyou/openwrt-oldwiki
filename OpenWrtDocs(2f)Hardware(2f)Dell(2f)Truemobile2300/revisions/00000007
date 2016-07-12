= Description =

The Dell !TrueMobile 2300 is based on the BCM4702KPB SoC, a BCM94306MP Mini-PCI
radio and a BCM5325MA2KQM switch.  In many respects it is similar to the
[:OpenWrtDocs/Hardware/Linksys/WRT54G: Linksys WRT54G] v1.  Like most
BCM4710-based platforms the stock firmware is Linux-based. The device
also contains the defacto standard of 4MiB Flash and 16MiB RAM.

= Installing OpenWrt =

The initial installation of OpenWrt is accomplished by uploading a
`.trx` image through the Dell firmware.  After OpenWrt is installed
it is a good idea to set the ''boot_wait'' NVRAM variable to ''on''.

When TFTPing to a router with ''boot_wait=on'' also use a `.trx` image.

= Serial port =

Because this is a BCM4702KPB-based model, the multi-use pins used by the serial port
are already in use by an Ethernet port.  It may however be possible to add a UART
(see [:OpenWrtDocs/Customizing]) if the header by the flash chip is an IO bus.
The other posibility is that this header is JTAG.

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

Most of these variables must not be changed or unset.
It should be safe to change the `lan_`* variables however.

Regardless of this, it is probably still unwise to use 'nvram reset' on this model. 

= LAN and WAN ports =

Out of the box, you may only be able to talk to a freshly converted openwrt Dell 2300 over wireless. Because of this, it's important to make sure you know the essid and any applicable WEP keys before flashing it. 

It's very easy to get the LAN and WAN ports working. Simply ssh in and configure the nvram arguments: 

{{{
nvram set lan_ifnames="eth0 eth2"
nvram set wan_ifname=eth1
nvram commit
}}}

= Power and Wireless LEDs =

Like some other non-linksys models, the 2300 has the Power and Wireless LEDs attached to GPIO pins, and does not use the 'diag' interface to control them. 

A freshly flashed openwrt 2300 will boot up never lighting the Power and Wireless LEDs. This, combined with the nonfunctional ethernet ports, leads many to believe that they have bricked their Dell. 

The wireless LED is on gpio pin 6, and the power LED is on gpio pin 7. 

The easy way to fiddle with these is the gpio utility found here: http://downloads.openwrt.org/utils/gpio.tar.gz

{{{
cd /tmp
wget http://downloads.openwrt.org/gpio.tar.gz
gzip -d gpio.tar.gz
tar xvf gpio.tar
mv gpio /usr/sbin
}}}

Unless you're a hardware engineer it seems counter-intuitive, but with the gpio utility, the led is lit by disabling the gpio pin, and darkened by enabling the gpio pin. 

Thus, to light the Power LED: 

{{{
gpio disable 7
}}} 

The manual method, as described by Oleg (of Asus firmware hacking fame) is as follows: 

{{{
The number stays for the bit number. The gpio port itself is accessible via /dev/gpio/*. You've to read outen, OR it with 0x40 (GPIO6) and write back - this should turn the led on. Then you will need to play with bit 6 in the /dev/gpio/out to change LED color.
}}}

fwiw, he was describing the Microsoft mn700 at the time. It is unclear how to change the LED color on the Dell 2300, and it doesn't appear to be possible with the gpio utility.  

The Restore button is likely connected to a gpio pin as well, but the author of this section hasn't bothered to figure out which one. 

----
CategoryModel
