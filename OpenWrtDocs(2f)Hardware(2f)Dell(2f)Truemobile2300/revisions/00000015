= Dell TrueMobile 2300 =
||<tablewidth="780px" tableheight="425px"> ||'''!TrueMobile 2300 v1 (Linksys WRT54G v1)''' ||'''!TrueMobile 2300 v2 (Linksys WRT54G v2)''' ||
||'''System-On-Chip''' ||BCM4702KPB ||BCM4712KPB ||
||'''CPU Speed''' ||125 MHz ||200 MHz ||
||'''Switch''' ||BCM5325MA2KQM ||ADM6996L ||
||'''Radio''' ||BCM94306MP Mini-PCI ||Integrated ||
||'''Flash Size''' ||4 MiB ||4 MiB ||
||'''RAM''' ||16 MiB ||16 MiB ||
||'''Boards''' || http://img76.imageshack.us/img76/2287/tm2300v1la3.th.jpg [http://img76.imageshack.us/my.php?image=tm2300v1la3.jpg] || http://img92.imageshack.us/img92/4941/tm2300v2ns1.th.jpg    [http://img92.imageshack.us/my.php?image=tm2300v2ns1.jpg] ||
= Installing OpenWrt =
It looks like the Broadcom Mini-PCI is not compatible with Kamikaze, both Versions (2.4 and 2.6) seem to have Problems with <= Kamikaze 7.09 out of the box, there is a work around shown below.

''' It is strongly recommended to flash WhiteRussian first before trying anything else, because boot_wait is not enabled by default! '''

The initial installation of OpenWrt is accomplished by uploading a {{{.trx}}} image through the Dell firmware.  After OpenWrt is installed it is a good idea to set the ''boot_wait'' NVRAM variable to ''on''.

When TFTPing to a router with ''boot_wait=on'' also use a {{{.trx}}} image.

= Installing OpenWrt - Kamikaze (This only applies to TrueMobile 2300 v1's) =
To install Kamikaze on the !TrueMobile 2300 v1 you have to do a little workaround. The problem is because the !TrueMobile 2300 v1 does not use VLAN tagging because it has a different interface for WAN and LAN (eth1,eth0). On other OpenWrt compatible Routers both interfaces are one physical device (eth0) and divided into 2 vlans (vlan0,vlan1). The switch then removes the VLAN tags and sends the data out to the correct port. Due to the fact that the !TrueMobile 2300 v1 does not use VLAN tags the switch does not remove the VLAN tags. So we have to add a VLAN on our local computer to access the Router.

'''normal way:'''

----
 . On my router i used Ubuntu 7.10 to do the trick (but it should work on any Linux or Unix distribution)
first i had to install VLAN support:

{{{
apt-get install vlan
}}}
then i added the VLAN 0 to eth0

{{{
ifconfig eth0 up
vconfig add eth0 0
}}}
now i had to assign an IP address to the new device (eth0.0)

{{{
ifconfig eth0.0 192.168.1.10 up
}}}
Finaly i was able to telnet the Router:

{{{
telnet 192.168.1.1
}}}
After i did the configuration i restored the network settings on my local computer: vconfig rem eth0.1 dhclient eth0

'''alternative way:'''

----
 . However some users report that they had to use vlan 1 instead of vlan 0, i do not know why and it makes no sense for me, because vlan1 is normally used for WAN and remote access via WAN is disabled by default.
But here is the Instruction:

{{{
ifconfig eth0 up
vconfig add eth0 1
ifconfig eth0.1 192.168.1.10 up
}}}
I could not get the router to ever come up with 192.168.1.1  so instead I started a dhcp server on my linux box.  With  /etc/dhcpd.conf  having a   subnet defined for 192.168.1.0    range was from 1.1 to 1.5

Then

{{{
dhcpd eth0.1
}}}
Started the router.

It picked up an address of 192.168.1.4 Then I was able to telnet it. After you have done the Configuration changes see below, you can get right of the vlan on your local computer with:

vconfig rem eth0.1 killall dhcpd dhclient eth0

= Configuration of Kamikaze after the successful Telnet access (This only applies to TrueMobile 2300 v1's) =
To get rid of the vlans edit the file

{{{
/etc/config/network
}}}
It should look like this:

{{{
#### VLAN configuration
#config switch eth0   ""
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
}}}
As you can see some of the vlan configuration commands are commented out with #

= Serial port =
Because the !TrueMobile 2300 v1 is a BCM4702KPB-based model, the multi-use pins used by the serial port are already in use by an Ethernet port.  It may however be possible to add a UART (see ["OpenWrtDocs/Customizing"]) if the header by the flash chip is an IO bus. The other possibility is that this header is JTAG.

= Sources =
Dell has released source code of the Dell !TrueMobile 2300 (Broadcom based) here:

http://linux.dell.com/files/truemobile/tm2300/Linux_source_code.tar.gz

= TrueMobile 2300 v1's bootloader default NVRAM settings =
Obtained by running {{{strings}}} on {{{/dev/mtd/0ro}}}

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

Most of these variables must not be changed or unset. It should be safe to change the {{{lan_}}}* variables however.

Regardless of this, it is probably still unwise to use 'nvram reset' on this model.

= LAN and WAN ports - WhiteRussian (This only applies to TrueMobile 2300 v1's) =
Out of the box, you may only be able to talk to a freshly converted OpenWrt !TrueMobile 2300 v1 over wireless. Because of this, it's important to make sure you know the essid and any applicable WEP keys before flashing it.

It's very easy to get the LAN and WAN ports working. Simply ssh in and configure the NVRAM arguments:

{{{
nvram set lan_ifnames="eth0 eth2"
nvram set wan_ifname=eth1
nvram commit
}}}
= Power and Wireless LEDs =
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

If there is no way to access the Router and BOOT_WAIT is disabled there is one last chance to revive your !TrueMobile 2300 v1. First you have to remove the mini-pci card, then you need to connect cables to the points marked in the image. It is recommended to use hot glue to fixate the cables. Then you need one more cable connected to ground.

http://img158.imageshack.us/img158/1127/delljtagpinout163kl8.th.jpg

[http://img158.imageshack.us/my.php?image=delljtagpinout163kl8.jpg]

Connect these cables to a parallel port, you need 4x 100ohm resistors.

http://img337.imageshack.us/img337/1774/interface2by4.png

Then you have to download WRT-JTAG http://www.wlan-skynet.de/download/index.shtml

{{{
c:\wrt54g -erase:nvram /noemw /nocwd /noreset
   Reset the Router
c:\wrt54g -erase:kernel /noemw /nocwd /noreset
   Reset the Router
}}}
If there is a problem detecting the flash chip try adding an option to set the type of chip manual:

{{{
c:\wrt54g -erase:nvram /noemw /nocwd /noreset /fc:03
}}}
03 for example stands for AMD 29lv320DB flash chip

Activate your Network card with fixed IP for example 192.168.2.2 and try to ping the router (192.168.2.1) until you get response. It is now possible to flash the router with tftp!

= Flashing CFE via JTAG =
On some routers it could happen that the flashing process stops after X%. I found out that it helps if i skip the first 2000 bytes of code and flash the rest first. After i flashed the bytes 2000-40000 if flashed the first 2000 bytes to the !TrueMobile and that worked!! I had to modify the sourcecode of wrt54g debrick tool so that i can add a fileoffset to the file i want to flash.

----
 . CategoryModel
