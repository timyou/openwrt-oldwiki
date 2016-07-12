= Description =

The Dell !TrueMobile 2300 is based on the BCM4702KPB SoC, a BCM94306MP Mini-PCI
radio and a BCM5325MA2KQM switch.  In many respects it is similar to the
[:OpenWrtDocs/Hardware/Linksys/WRT54G: Linksys WRT54G] v1.  Like most
BCM4710-based platforms the stock firmware is Linux-based. The device
also contains the defacto standard of 4MiB Flash and 16MiB RAM.

= Installing OpenWrt =

It looks like The Broadcom Mini-PCI is not compatible with Kamikaze, both Versions (2.4 and 2.6)
seem to have Problems with <= Kamikaze 7.09 out of the box, there is a work around shown below.

''' It is strongly recommended to flash whiterussian first before trying anything else, because boot_wait is not enabled by default! '''

The initial installation of OpenWrt is accomplished by uploading a
`.trx` image through the Dell firmware.  After OpenWrt is installed
it is a good idea to set the ''boot_wait'' NVRAM variable to ''on''.

When TFTPing to a router with ''boot_wait=on'' also use a `.trx` image.

= Installing OpenWrt - Kamikaze =
{{{
ifconfig eth0 up
vconfig add eth0 0
ifconfig eth0.0 192.168.1.10 up
telnet 192.168.1.1
}}}

{{{
alternative way:

TM2300 was trying to use vlan1 so I ended up doing the following on my linux box (via eth0) directly connected to the router with nothing else running.  At first, have the router powered off.

ifconfig eth0 192.168.1.10 up
vconfig add eth0 1
ifconfig eth0.1 192.168.1.10 up

I could not get the router to ever come up with 192.168.1.1  so instead I started a dhcp server on my linux box.  With  /etc/dhcpd.conf  having a   subnet defined for 192.168.1.0    range was from 1.1 to 1.5

Then 
dhcpd eth0.1

Started the router.   

It picked up an address of 192.168.1.4

Then I was able to telnet it  smile

Set the password, and then changed /etc/config/network to..

#### VLAN configuration
#config switch eth0   
#       option vlan0    "0 1 2 3 5*"
#       option vlan1    "4 5"       


#### Loopback configuration
config interface loopback 
        option ifname   "lo"
        option proto    static
        option ipaddr   127.0.0.1
        option netmask  255.0.0.0


#### LAN configuration
config interface lan 
        option type     bridge
#       option ifname   "eth0.0"
        option ifname   "eth0"
        option proto    static
        option ipaddr   192.168.1.1
        option netmask  255.255.255.0


#### WAN configuration
config interface        wan
#       option ifname   "eth0.1"
        option ifname   "eth1"
        option proto    dhcp

And power cycled just to be sure, and now it came back up properly as 192.168.1.1  and I got rid of my vlan on the linux box via

vconfig rem eth0.1
killall dhcpd

And got me a proper address via   
dhclient eth0
}}}


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

Like some other non-linksys models, the 2300 is not yet detected by the diag driver in rc6, and if you want the wifi and power LEDs to light, you'll have to do it manually. 

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

The Restore button is likely connected to a gpio pin as well, but the author of this section hasn't bothered to figure out which one. 

= JTAG =
''' WARNING ONLY TRY THIS IF IT IS YOUR LAST CHANCE TO REVIVE YOUR ROUTER!! '''

If there is no way to access the Router and BOOT_WAIT is disabled there is one last chance to revive your TM2300.
First you have to remove the mini-pci card, then you need to connect cables to the points marked in the image.
It is recommended to use hot glue to fixate the cables. Then you need one more cable connected to ground.

http://img158.imageshack.us/img158/1127/delljtagpinout163kl8.th.jpg

[http://img158.imageshack.us/my.php?image=delljtagpinout163kl8.jpg]

Connect these cables to a parallel port, you need 4x 100ohm resistors.

http://img337.imageshack.us/img337/1774/interface2by4.png

Then you have to download WRT-JTAG
[http://www.wlan-skynet.de/download/index.shtml]

{{{c:\wrt54g -erase:nvram /noemw /nocwd /noreset

   Reset the Router

c:\wrt54g -erase:kernel /noemw /nocwd /noreset

   Reset the Router
}}}

If there is a problem detecting the flash chip try adding an option to set the type of chip manual:

{{{
c:\wrt54g -erase:nvram /noemw /nocwd /noreset /fc:03
}}}

03 for example stands for AMD 29lv320DB flash chip

Activate your Network card with fixed IP for example 192.168.2.2
and try to ping the router (192.168.2.1) until you get response.
It is now possible to flash the router with tftp!

= Flashing CFE via JTAG =
On some routers it could happen that the flashing process stops after X%.
I found out that it helps if i skip the first 2000 bytes of code and flash the rest first. After i flashed the bytes 2000-40000
if flashed the first 2000 bytes to the Truemobile and that worked!!
I had to modify the sourcecode of wrt54g debrick tool so that i can add a fileoffset to the file i want to flash.

----
CategoryModel
