[[TableOfContents]]

= Linksys WAG354G v1 =
The Linksys WAG354G is an ADSL gateway with wireless  acccess point integrated.

== Specifications ==
ADSL2/2+ support up to 24Mbit/s+

4 port switch

Wireless 802.11b/g

The unit comes with an internal antenna. It's possible to add an external antenna via the R-SMA plug. There seems to be a mechanical switch that gets (de-)activated when you open the tap of the external antenna port.

=== Hardware ===
Platform: ''TI AR7WRD''

SoC: [http://www.cassy.de/fbox/tnetd7300.pdf TNETD7300AGDW]

Processor: ''MIPS 4KEc V4.8'' @ 150 MHz

4 port switch: ''Infineon ADM6996L''

Wireless chipset: ''TI TNETW1130''

Expansions: '''minipci slot''' for wireless card (connected to the processor via a VLYNQ bus)

Internal:

[http://www.hughe.co.uk/pub/pics/tech/openwrt/WAG354G_big.jpg Big size]

attachment:WAG354G_small.jpg

----
 . '''Serial console'''
Serial console can be plugged to JP5: connector lacks, it has to be soldered on the board.
-My board actually has the header already installed on JP5. -- RobertSiemer [[DateTime(2008-04-04T17:33:21Z)]]

Position on board and pinout:

{{{
                 |
                 |
         MiniPCI |
         Slot    |
        _________|



      |*|      |*|     leds    |*|   |*|   |*|   |*|


                --JP5--------------------
               | [1]  [2]  [3]  [4]  [5] |
                -------------------------
  _ _ _ ______________________________________________ _ _ _


Legend:
1  GND
2  NC
3  Rx
4  Tx
5  Vcc
}}}
'''Interface'''

You cannot plug directly those pins to your pc serial port. You need a RS232-TTL level adapter. Some examples:

 * Using a MAX232: [http://wiki.openwrt.org/OpenWrtDocs/Hardware/Linksys/WAG354G?action=AttachFile&do=get&target=serial-wag354G.png Serial Console Schematic]
 * Using a USB-Serial Converter cable based on the Prolific [http://www.prolific.com.tw/eng/downloads.asp?ID=23 PL2303 chipset]. Good if you have an Apple MAC.
 * Using an hacked mobile phone datacable (MBUS), both serial or USB. Ususally this cables are really cheap and implements one of the 2 above solutions.
Detailed instructions: http://www.nslu2-linux.org/wiki/HowTo/AddASerialPort''' '''

'''Terminal'''

Configuration:

{{{
 38400 bauds, 8 bits, no parity, 1 stop bit (38400 8N1) }}}
Software: [http://alioth.debian.org/projects/minicom/ Minicom]on Linux or MacOSX(via fink); [http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html Putty] on Windows

----
 . '''JTAG'''

Jtag pins are located in JP2, but the connector lacks. The pinout and specifications are the same of others AR7 devices that is 14 ping ejtag 2.6. 

With the router upside down, GND pins are located in the upper pin strip.

You can use Hairydairymaid Debrick Utility with a Xilinx cable.

----
 . '''GPIO'''
One gpio for the reset button. One gpio for switching between internal/external antenna.

to be written (& tested)...

----
 . '''Mods'''
Possible mods:

 * Minipci Wireless Card is not replaceable!! It uses the proprietary vlynq bus by T.I.

 * Add an SD card reader.
to be written (& tested)...

-----

=== Software ===
'''Bootloader'''

["PSPBoot"] 1.2 rev: 0.22.17

'''Code Patterns'''

''WA31'' for Annex A (ADSL over POTS) devices.

''WA32'' for Annex B devices.

----
 . '''Flash layout'''
{{{
0x900e0000,0x903d0000 fs (mtd0)
0x90020000,0x903d0000 kernel (mtd1)  (The end address is the same as fs...)
0x90000000,0x90020000 Bootloader (mtd2)
0x903d0000,0x903f0000 Lang partition (mtd4)
0x903f0000,0x90400000 NVRAM (mtd3)
_____________________________________
TOTAL = 4096K = 4M
}}}
----------


== Building Openwrt ==

The latest openwrt kamikaze has more recent ADSL drivers with support of ADSL2+, and a preliminary support for the wireless card, using the open soure drivers by the [http://acx100.sourceforge.net/ ACX100 project] .

Checkout the latest kamikaze trunk:
{{{
svn co https://svn.openwrt.org/openwrt/trunk/
}}}
As trunk is always changing it may happen something will not work as expected, both in compilation or use of the firmware.

Now you have to set up the configuration entering
{{{
make menuconfig
}}}
Choose as target platform '''AR7'''. Then in kernel configuration select [*] the Annex that matches your router.


== Running OpenWRT ==

'''The following configuration applies only to OpenWRT Kamikaze with 2.6 kernel version.'''

=== Network Configuration ===
'''NOTE:''' All the network interfaces can be configured via the '''/etc/config/network''' file. File structure is self-explicative, here I will just show you some examples.

'''eth0 (ethernet) interface'''

 * Static IP
{{{
config interface lan
        option ifname   eth0
        option proto    'static'
        option ipaddr   '192.168.1.1'
        option netmask  '255.255.255.0'
        option gateway  '192.168.1.254'
        option dns      '192.168.1.254'}}}
 * DHCP
{{{
config interface lan
        option ifname   eth0
        option proto    'dhcp' }}}
'''ppp0 (adsl) interface'''

 * PPPoA + VC
{{{
config interface wan
        option ifname   atm0
        option proto    pppoa
        option encaps   vc
        option vpi      8
        option vci      35
	option username "yourusername"
        option password "yourpassword"     }}}
 *  PPPoE ''' '''
'''wlan0 (wifi) interface'''

{{{
config interface wlan
        option ifname   wlan0
        option proto    'static'
        option ipaddr   '192.168.100.1'
        option netmask  '255.255.255.0'
        option gateway  ''
        option dns      ''  }}}
=== Enable Wireless in Access-Point mode ===
For this work you can both consider eth0 and wlan0 as 2 separate interfaces, or bridge them. I have choosen the first way.
 * The wireless chipset needs a firmware. You can download some firmwares for the ACX111 chipset [http://www.hauke-m.de/fileadmin/acx/fw.tar.bz2 here]. Choose one firmware binary (I used the last version) named ''tiacx111c16''  and upload it in the /lib/firmware/ folder of your router.
 * Edit the /etc/config/network file according to the section above.
 * Reboot your router. At this point wireless drivers should have been started in a sort of client mode. Just fyi, this is the output of console:
{{{
acx_i_timer: adev->status=1 (SCANNING)
continuing scan (1 sec)
acx_i_timer: adev->status=1 (SCANNING)
continuing scan (2 sec)
scan table: SSID="dd-wrt" CH=1 SIR=44 SNR=0
peer_cap 0x0511, needed_cap 0x0001
ESSID doesn't match! ('dd-wrt' station, 'STA1D2AE8' config)
no matching station found in range yet                               }}}
Entering''ifconfig wlan0 ''you should see an output according to your configuration.
 * Use '''iwconfig''' to configure the the wireless properties.
__Some examples
__{{{
iwconfig wlan0 mode Master essid openwrt channel 6 txpower 15}}}
This will create an open netword with ssid "openwrt", using channel 6 and with transmission power set to 15. Transmission power range is 10-15dbm.
{{{
iwconfig wlan0 mode Master essid openwrt key restricted 1234AAAABB channel 6 txpower 15}}}
Like the previous, but this time the network is protected with WEP (whoa!) with the hex key 1234AAAABB. If  you use a shorter key, it will be fullfilled with zero to reach the 10 symbols.
Refer to the[http://www.linuxcommand.org/man_pages/iwconfig8.html manual]for all the options. I observed that if I enter "ifdown wlan; iwconfig....;ifup wan" the router crashes. So dont enter ifdown before entering iwconfig.
 * Configure the natting. With the following script packets from wlan0 are sent to ppp0, that is Internet connection. Change EXTIF to eth0 if internet is reachable from the ethernet.
{{{
#!/bin/sh
INTIF=wlan0
LANIN=192.168.100.0/24
EXTIF=ppp0
iptables -A INPUT -i $INTIF -s $LANIN -j ACCEPT
iptables -A OUTPUT -o $INTIF -d $LANIN -j ACCEPT
iptables -A FORWARD -s $LANIN -d 0/0 -j ACCEPT
iptables -A FORWARD -m state --state ESTABLISHED,RELATED -d $LANIN -j ACCEPT
iptables -t nat -A POSTROUTING -o $EXTIF -s $LANIN -j MASQUERADE
iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
iptables -A OUTPUT -m state --state NEW,ESTABLISHED,RELATED -j ACCEPT}}}
 * Check the routing table using "route". If the default rule is wrong, delete it
{{{
route del default}}}
and enter the default for right one for your configuration. In this case:
{{{
route add default ppp0}}}
 * If you want the dhcp server on the wlan0 interface:
{{{
dnsmasq -i wlan0 --dhcp-range=192.168.100.50,192.168.100.150,12h}}}
=== Old notes ===
'''WARNING''' This page is a work in progress.  So far I (IanJackson) am just collecting information found in various other places (eg, IRC logs) together.

Known problems:

* `Crashes occasionally' for some people or with some devices.  Currently not known whether this is a hardware problem.

* Using the tftp procedure to upload an openwrt image seems for some people to disable the tftp facility in PSPBoot, so that future upgrades have to be done from within openwrt.  However this didn't happen to me -IanJackson.

= Linksys WAG354G v2 =

== Specifications ==
Same as the V1.

=== Hardware ===
Platform: ''TI AR7WRD''

SoC: [http://www.cassy.de/fbox/tnetd7300.pdf TNETD7300AGDW]

Processor: ''MIPS 4KEc V4.8'' @ 210 MHz

4 port switch: ''Infineon ADM6996LC''

Integrated on motherboard Wireless chipset: ''TI TNETW1350A''

----
 . '''Serial console'''
Serial console can be plugged to JP4: connector lacks, it has to be soldered on the board.

Pinout:

{{{
                                                   JP4_______                |
  |                                                [1]  [2]  [3]  [4]  [5]   |
  |                                                                          |
  |                                                                          |
  |___ _ ___|-|____|-|__leds___|-|_|-|_|-|_|-|_______________________________|
Legend:
1  GND
2  NC
3  Rx
4  Tx
5  Vcc
}}}

'''Terminal'''

Configuration:

{{{
 38400 bauds, 8 bits, no parity, 1 stop bit (38400 8N1) }}}


 *On my system, it only works with
{{{
 4800 bauds, 8 bits, no parity, 1 stop bit (4800 8N1) }}}, but the kernel is executed with :
{{{
 console=ttyS0,38400n8r }}}

----
 . ["CategoryAR7Device"]
