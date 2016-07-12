''' attachment:logo3.gif ''''''''COMPEX WP54'''''

{*} {*} {*} {*} {*}

 . (This page is at an early stage of development. Please feel free to update)
The Compex WP54 is a small, well-made device with two ethernet ports and Atheros wireless.

There are several different models available of WP54, but only WP54 with part number including "WRT" runs any variant of OpenWRT currently. E.g. WP54-WRT and WP54-WRT6E ''(New Version)''

'''NOTE:''' These units run Compex's own fork of OpenWRT. There is '''''no''''' support for the Compex WP54 in either White Russian or the current Kamikaze tree.

''' <:( Compex WP54 THAT ''DO NOT'' SUPPORT WRT.'''

 * '''WP54 1A''' = Standard Wireless device that able to run in 7Modes(AP,Client, P to P,Gateway, P to multiple P,WL Routing Client and WL Adapter)
 * '''WP54 1B''' =''' '''can be powered either by 5V DC Supply or 802.3af PoE, using a jumper selection available on the board.
 * '''WP54 1C''' = Wireless Device that support AccessPoint Mode and Client mode only.
 * '''WP54 1D''' = can be powered either via a separate 24V DC PSU or a proprietary 24V DC PoE injector or real 802.3af PoE.
 * '''WP54 6D''' = It is [wiki:ALife:http://en.wikipedia.org/wiki/ROHS ROHS] Standard and able able to run in IEEE802.3af standard PoE and Compex PoE Plus.
''' {OK} Compex WP54 ''WITH'' WRT.'''

 * '''WP54-WRT''' is the same as WP54 1B board, but it has an additional hardware protection chip on the board [FIXME: What is this "hardware protection chip"? What does it do? Why can OpenWrt not run without it?].
 * '''WP54 6E''' = This is the latest OpenWRT version from Compex that able to run in IEEE802.3af standard PoE and Compex PoE Plus.It is also [http://en.wikipedia.org/wiki/ROHS ROHS] standard. This model come with 2 version, Compex and WRT version.
''' (./) OpenWRT Packets Information'''

''There are 2 Type Of Compex OpenWRT Packages available.''
||<tablewidth="665px" tablestyle="WIDTH: 665px; HEIGHT: 238px">'''Package ''' ||'''Content''' ||
||<style="TEXT-ALIGN: center">'''P-WR-WP54 Board''' ||WP54 WRT Bare-board (Pre-loaded with Open-WRT) ||
||<style="TEXT-ALIGN: center" |6>'''P-WR-WP54AG WRT ''''''Development Kit''' ||• WP54 WRT6E Bareboard (Pre-loaded with Open-WRT) ||
||• Wireless AG mini-PCI (Compex WLM54AG) ||
||• PoE+ Injector (Compex PoE+1A4815) ||
||• JTAG Programmer (Cable from PC to JTAG Programmer included) ||
||• Serial Converter (Cable from PC to Serial Converter included) ||
||• 24V DC Power Supply ||


'''Other Information about Compex '''OpenWrt''' Bareboard''' B-)

 * Open-WRT is preloaded on the board before shipping to customers.
 * Serial Ports is soldered onto the board.
 * JTAG Ports is soldered onto the board.
 * JTAG Programmer and Serial Converter is available if you purchase the development kit.
'''''Related Link''''' {i}

[http://www.compex.com.sg/ Homepage] =The manufacturer's Website

[http://compex.com.sg/home/OEM/Downloads/OpenWRT_WP54_6E_Bareboard_DSv2.7.pdf DataSheet] = Provide Technical Specification and Ordering Information.

[http://compex.com.sg/home/OEM/index.htm.%20 OEM Solution] = It is about Company OEM Solution.

[http://compex.com.sg/home/OEM/Downloads/WP54_Board_Product_Manual_Rev1.4.pdf Hardware Manual] = Its all about what you need to know about hardware. GPIO bit mapping, Serial Port, Serial Console Setting, Jtag Port, Power Supply Jumper Setting, and so on.

[http://compex.com.sg/home/OEM/Downloads/Open-WRT_Codes.rar OpenWRT Codes] = Its a .Rar file that contain Open WRT Code.

[http://compex.com.sg/home/OEM/Downloads/JTAG_Programmer.rar JTAG Programmer Codes] = Like the name, Contain the JTAG Programmer codes

'''''For Europe'''''

The European distributor is [http://www.compexshop.eu/ Tomorrows CZ] and they have their own [http://www.cpx.cz/dls/WP54G_linux/ downloads page]

'''''Other links'' '''

 * [http://www.linux-mips.org/wiki/Adm5120 Linux-MIPS Adm5120 page]
 * [http://www.seattlewireless.net/Atheros Seattle Wireless Atheros page]
Picture below show how to set the jumper to use PoE and DC Supply.

attachment:PoEJumper.JPG

and this picture is about and which pin to be used in serial converter.

attachment:SerialJumper.JPG

Hope these pictures will help you :) I will try to get more information regarding this product.

''''''

''''''

'''''Default settings'''''

''[These notes refer to the Compex firmware in WP54G, not WP54-WRT]''

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

The web interface has an option to upgrade the firmware. However the file format of Compex's standard firmware is not the same as OpenWrt's trx file. Here are the first few bytes of WP54G_MSSID_V203_B1013.IMG (The latest firmware Should be "WP54G_MSSID_V206_B1229.IMG ")

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
This appears to be a CFE command line, which presumes you have a TFTP server running on 192.168.0.1

If you download the [http://www.compex.com.sg/home/OEM/Downloads/JTAG_Programmer.rar JTAG programmer codes bundle] it's another RAR file containing:

{{{
-rw-r--r--  1 root  root    1887 Aug 22 13:34 JTAG_Programmer_ReadMe.txt
-rw-r--r--  1 root  root  435679 Aug  2 19:00 myloram.s19
-rw-r--r--  1 root  root  180084 Aug  2 18:50 myloram.srec
-rw-r--r--  1 root  root     875 Jun  8 09:57 wp18.mac
-rw-r--r--  1 root  root    1358 May 30 17:04 wp54g.mac
}}}
The !ReadMe.txt file talks about using [http://macraigor.com Macraigor] [http://macraigor.com/ocd_cmd.htm OCD Commander] to download and run RAM version of their loader via the E-JTAG interface using a [http://macraigor.com/wiggler.htm Wiggler] device. The .mac files contains commands for OCD Commander to initialize onboard memory devices, then download the loader and execute it. Once you have done this you can use tftp to upload cfe.bin

You can update the bootloader from within MyLoader itself.

'''Inside the box'''

Opening the unit is done by prising off the four rubber feet and removing the small cross-point screws underneath. The board is remarkably boring; there is a single chip under a heatsink, a wireless miniPCI card, and the rest is just capacitors and analogue support chips. Warning: after opening the box, it's quite hard to get the LED light guide back into place properly.

CategoryModel ["CategoryADM5120Device"]
