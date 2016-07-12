'''Compex WP54G'''

(This page is at an early stage of development. Please feel free to update)

The Compex WP54G is a small, well-made device with two ethernet ports and Atheros wireless. It can be powered via a separate 24V DC PSU, a proprietary 24V DC PoE injector or real 802.3af PoE.

The manufacturer's home site is http://www.compex.com.sg/

The European distributor is [http://www.compexshop.eu/ Tomorrows CZ] and they have their own [http://www.cpx.cz/dls/WP54G_linux/ downloads page]

The Compex-supplied firmware is actually quite powerful; version 2.xx has multi-SSID access point and a number of other operating modes. However they also [http://www.compex.com.sg/home/OEM/Open_wrt.htm support OpenWrt] on this unit.

'''Default settings'''

The Compex comes up by default as 192.168.168.1/24. You can login to it using a web browser, the default password is "password"

Via the web interface you can enable telnet and ssh, and create user accounts to access it through these methods. You can set each account to be "Read Only" or "Read Write". When you login you get a very crippled busybox environment.

{{{
$ ssh admin@192.168.168.1
admin@192.168.168.1's password:


BusyBox v1.00 (2006.10.11-08:51+0000) Built-in shell (ash)
Enter 'help' for a list of built-in commands.

# nvram
-sh: nvram: not found
# ls
you can't use the command!
# echo
you can't use the command!
# help
config radio and virtual VAP:
config <[wlan <unit>] | [vap <index>]>
Available parameters:
brinfo              brmacinfo           buttonpwdreset      ddns
dhcp                dhcpstartip         dhcpendip           dnsmasq
factory             ipaddr              ipmask              macstats
routeshow           satd                snmp                snmpcommunity
snmpsetcommunity    ssh                 sshport             telnet
telnetport          upgrade             upnp                userlist
webserver           restart

# 
}}}

'''Firmware format'''

The web interface has an option to upgrade the firmware. However the file format of Compex's standard firmware is not the same as OpenWrt's trx file. Here are the first few bytes of WP54G_MSSID_V203_B1013.IMG

{{{
00000000  00 4d 59 4c 90 46 32 d2  00 00 00 00 00 00 00 00  |.MYL.F2.........|
00000010  f6 11 15 05 f6 11 15 05  00 00 00 00 00 00 02 00  |................|
00000020  00 00 02 00 03 00 00 00  01 00 00 00 00 00 01 00  |................|
00000030  90 00 00 00 00 00 01 00  01 00 00 00 00 00 02 00  |................|
...
}}}

Therefore it looks unlikely that you can upload an OpenWrt image through the standard web interface.

'''OpenWRT support'''

WP54G support is not yet integrated into the main OpenWrt repository.

From the Compex site you can download their [http://www.compex.com.sg/home/OEM/Downloads/Open-WRT_Codes.rar OpenWrt code bundle]. This is a RAR file (use 'unrar' to extract) which contains:

{{{
-rw-r--r--  1 root  root    252608 Aug 16 09:09 cfe.bin
-rw-r--r--  1 root  root  10593655 Apr 25  2006 openwrt-trunk-20060425.tgz
-rw-r--r--  1 root  root   1622016 Jun  2 17:12 openwrt-wp54g-2.4-squashfs.trx
-rw-r--r--  1 root  root     80105 Jun  2 17:19 openwrt-wp54g-20060602.tgz
-rw-r--r--  1 root  root       167 Jun  2 11:23 wp54gcmd
}}}

The file openwrt-wp54g-2.4-squashfs.trx appears to be a standard OpenWrt TRX-format file:

{{{
00000000  48 44 52 30 00 c0 18 00  31 2f ef 1f 00 00 01 00  |HDR0....1/......|
00000010  1c 00 00 00 54 09 00 00  00 00 08 00 1f 8b 08 00  |....T...........|
00000020  00 00 00 00 02 03 a5 57  5f 6c 5b 57 19 ff f9 dc  |.......W_l[W....|
00000030  9b c4 4d 53 73 e3 b8 91  5b aa 71 4f 7d e2 58 cd  |..MSs...[.qO}.X.|
...
}}}

The file 'wp54gcmd' contains just the following line:

{{{
flash -noheader 192.168.0.1:openwrt-wp54g-2.4-squashfs.trx flash1.trx;nvram set STARTUP="load -z -raw -max=8000 -addr=0x80001000 flash1.trx:0x1c;go";nvram commit;reset
}}}

However it's not clear how you use it.

If you download the [http://www.compex.com.sg/home/OEM/Downloads/JTAG_Programmer.rar JTAG programmer codes bundle] it's another RAR file containing:

{{{
-rw-r--r--  1 root  root    1887 Aug 22 13:34 JTAG_Programmer_ReadMe.txt
-rw-r--r--  1 root  root  435679 Aug  2 19:00 myloram.s19
-rw-r--r--  1 root  root  180084 Aug  2 18:50 myloram.srec
-rw-r--r--  1 root  root     875 Jun  8 09:57 wp18.mac
-rw-r--r--  1 root  root    1358 May 30 17:04 wp54g.mac
}}}

The !ReadMe.txt file talks about using "Wiggler" as the JTAG interface, to upload one of the .mac files which is a RAM version of their loader. Once you have done this you can use tftp to upload cfe.bin

TO DO: Document the actual process to convert a WP54G to OpenWrt

TO DO: Document the actual process to revert a WP54G to standard Compex firmware

'''Inside the box'''

Opening the unit is done by prising off the four rubber feet and removing the small cross-point screws underneath. The board is remarkably boring; there is a single chip under a heatsink, a wireless miniPCI card, and the rest is just capacitors and analogue support chips. Warning: after opening the box, it's quite hard to get the LED light guide back into place properly.

The board appears to be the same as the one in [http://www.compex.com.sg/home/OEM/Downloads/OpenWRT_WP54_1B_Bareboard_DSv2.1.pdf this photo]

There is an unpopulated 2x7 jumper (JP1) and another 2x5 jumper (J1). I guess these are JTAG and serial, but are not labelled as such.

'''Other links'''

 * [http://www.linux-mips.org/wiki/Adm5120 Linux-MIPS Adm5120 page]
 * [http://www.seattlewireless.net/Atheros Seattle Wireless Atheros page]
