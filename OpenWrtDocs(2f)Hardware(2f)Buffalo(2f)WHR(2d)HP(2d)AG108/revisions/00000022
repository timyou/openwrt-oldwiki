= WHR-HP-AG108 =
attachment:WHR-HP-AG108.jpg

The WHR-HP-AG108 has a Atheros WiSoC CPU running at 220 MHz. It has 4 MB flash and 32 MB RAM as well as '''two wireless devices onboard''' (one a/b/g, one b/g) which allows '''simultaneous a and g''' wireless networks using the Buffalo or OpenWrt firmware. There is a serial port and most possibly the soldering points are for JTAG (didn't tried it jet).

Packaging suggest that my unit is a WHR-HP-AG108-4 (EU-Version), so it seems there are some different versions out there.

'''Flashing OpenWrt to a WHR-HP-AG108 is not trivial.''' The precompiled images from OpenWrt won't work with the WHR so you'll have to compile your own or download a custom firmware (available below). To flash the WHR from it's original firmware you must gain debug access to the router, activate telnet access, change the RedBoot configuration, use the Redboot interface to flash the operating system and file system files, and enable the boot script. It's not easy but the process is detailed below.

== Prepare firmware image ==
Get yourself a copy of Kamikaze from the SVN repository: svn co https://svn.openwrt.org/openwrt/trunk/ kamikaze {for the latest, bleeding edge, trunk release} I was unsuccessful with this release, but I did compile and flash the following stable tag svn: svn co https://svn.openwrt.org/openwrt/tags/kamikaze_7.09 kamikazestable

Edit ''package/madwifi/Makefile''. Change the line containing ''HAL_TARGET'' so that it reads

{{{
HAL_TARGET:=ap30
}}}
after that it's time for ''make menuconfig; make'' and have some fun and watching a short film while it compiles.

I tested it with Kamikaze 7.06 so if you're unsure you may use that version. It also works with the stable release of 7.09 as of 10 March 08.

'''If you can't compile the firmware image yourself you can download my pre-compiled OpenWrt Kamikaze 7.09 tag image for the WHR-HP-AG108 here: '''http://robrobinette.com/etc/Rob-WHR-HP-AG108.zip
The image is very stable and has Webif^2 built in so you will be able to access the router using your web browser at http://192.168.1.1 after you flash it.

== Buffalo debug interface ==
{{{
http://192.168.11.1/cgi-bin/cgi?req=frm&frm=py-db/55debug.html
user: bufpy
password: "otdpopy+your root password (empty by default)" e.g.: otdpopy1234
}}}

== Accessing RedBoot via ethernet ==
  * Start Buffalo debug interface
  * Activate telnet
  * Connect via telnet to the router
  * Download [attachment:RedBoot_config_gdb.rom Holgi’s redboot configuration]
  {{{
cd /tmp
wget ftp://[remote server address]/RedBoot_config_gdb.rom
}}}
  * Flash it
  {{{
dd if=/tmp/RedBoot_config_gdb.rom of=/dev/mtdblock/4
}}}
  * Confirm "128+0 records" in and out
  * Power cycle the router
  * Just after it starts, while the red diagnostic led is flashing, connect via telnet on port 9000
  . you should see
  {{{
Executing boot script in...
}}}
  interrupt it with CTRL-C
  * You should be at the !RedBoot prompt
  {{{
RedBoot>
}}}

== Loading OpenWrt ==
'''Always make a backup of your old firmware. If something goes wrong - I told you!'''

If you're using a '''serial console''' configure it with:

{{{
screen -c /dev/null -m /dev/ttyUSB0 9600 8N1
}}}
If you're using '''ethernet''', make sure your network cable is plugged into port 1! It's the one closest to the antenna. I tried port 4 before and didn't got a network connection with that.

Now you may power up your router and hit Ctrl-C when it asks for it. '''Once in !RedBoot''' you should set your network config

{{{
ip_address -l [router ip address] -h [ftp server address]
}}}
After that it's time to format the flash, copy the firmware from tftp to your router, write firmware to flash and configure bootloader to make it all work.

{{{
fis init -f
load -r -b %{FREEMEMLO} openwrt-atheros-2.6-vmlinux.gz
fis create -r 0x80041000 -e 0x80041000 vmlinux.gz
load -r -b %{FREEMEMLO} openwrt-atheros-2.6-root.squashfs
fis create -l 0x280000 rootfs
fconfig -d
}}}
Set ''execute boot script true'' and use

{{{
fis load -d vmlinux.gz
exec
}}}
as bootscript.

... done. Now it's time to restart your router with the 'reset' command and watch it boot up into !OpenWrt.

Here's the RedBoot commands I used to flash my router with the pre-compiled OpenWrt Kamikaze 7.09 tag image for the WHR-HP-AG108 downloaded here: http://robrobinette.com/etc/Rob-WHR-HP-AG108.zip

{{{
RedBoot> fis init -f    (will erase everything but the Redboot info from the WHR's flash memory)
fis free      (confirm you get the same free memory numbers below, if they are different the flash may not work)
  0xBE050000 .. 0xBE3D0000
  0xBE3E0000 .. 0xBE3F0000
= %{FREEMEMLO}   (confirm you get the same number below)
0X80000400
load -r -v -b %{FREEMEMLO} RobKamikaze709WHR.vmlinux.gz
fis create -r 0x80041000 -e 0x80041000 vmlinux.gz
load -r -v -b %{FREEMEMLO} RobKamikaze709WHR.squashfs
fis free  (again confirm you get the same numbers below)
  0xBE150000 .. 0xBE3D0000    (0xBE3D0000 - 0xBE150000 = 280000 (hex math))
  0xBE3E0000 .. 0xBE3F0000
(I get 280000 free space so  it's:)
fis create -l 0x280000 rootfs
fis list   (confirm you get the same numbers, they may be listed in a different order)
Name              FLASH addr  Mem addr    Length      Entry point
RedBoot           0xBE000000  0xBE000000  0x00050000  0x00000000
vmlinux.gz        0xBE050000  0x80041000  0x00100000  0x80041000
rootfs            0xBE150000  0x80000400  0x00280000  0x80000400
FIS directory     0xBE3D0000  0xBE3D0000  0x0000F000  0x00000000
RedBoot config    0xBE3DF000  0xBE3DF000  0x00001000  0x00000000
fis free
  0xBE270000 .. 0xBE3D0000
  0xBE3E0000 .. 0xBE3F0000
fconfig  
(when it asks you for your init script you put following lines)
fis load -d vmlinux.gz
exec
}}}
And that's it, use the 'reset' command to reboot into Kamikaze. Webif^2 is built into the image so the router will be available through your browser at 192.168.1.1



I telnetted into the router using port 9000 and set a password using the 'passwd' command, then accessed the router usng the Webif^2 web interface and used the System/File Editor to change the /etc/config/wireless file to:

{{{
config wifi-device  wifi0
        option type     atheros
        option channel  '44'
        option diversity        '0'
        option txantenna        '0'
        option rxantenna        '0'
        option mode     '11a'

        # REMOVE THE FOLLOWING LINE TO ENABLE WIFI:
#       option disabled 1 (This line is commented out)

config wifi-iface
        option device   wifi0
        option network  lan
        option mode     ap
        option ssid     RobRobinetteA
        option encryption       wep
        option key1     your_wep_code_here
        option key      1
        option hidden   '0'
        option isolate  '0'
        option txpower  '13'
        option bgscan   '0'
        option wds      '0'

config wifi-device  wifi1
        option type     atheros
        option channel  '11'
        option diversity        '0'
        option txantenna        '0'
        option rxantenna        '0'
        option mode     '11bg'

        # REMOVE THIS LINE TO ENABLE WIFI:
        option disabled 0

config wifi-iface
        option device   wifi1
        option network  lan
        option mode     ap
        option ssid     RobRobinetteG
        option encryption       wep
        option key1     your_wep_code_here
        option key      1
        option hidden   '0'
        option isolate  '0'
        option txpower  '15'
        option bgscan   '0'
        option wds      '0'
}}}
I confirmed that both wifi interfaces were working simultaneously with this setup. I found that the max transmit power of 13 worked for 802.11a and 15 for 802.11b/g. I loaded webif^2 and the web interface works great. The transmit power and signal-to-noise ratio of the WHR is a little weak. My Asus WL500gP puts out a stronger signal and consistantly tests much faster than the WHR.

== Troubles ==
Said this I'm still very unsatisfied with the wireless performance because compared to my wrt54gl the wireless range just sucks. Maybe it's because I can't set txpower to levels higher than 13 dBm, but I'm unsure about that because of the built in amplifier.

== Serial pinout (JP2) ==
{{{
3.3V, GND, RX, TX
Board on this side
}}}

== RedBoot factory defaults ==
{{{
RedBoot> fis list
Name              FLASH addr  Mem addr    Length      Entry point
RedBoot           0xBE000000  0xBE000000  0x00050000  0x00000000
RedBoot config    0xBE3DF000  0xBE3DF000  0x00001000  0x00000000
FIS directory     0xBE3D0000  0xBE3D0000  0x0000F000  0x00000000
vmlinux.bin.gz    0xBE050000  0x80002000  0x000B4B98  0x80182398
rootfs            0xBE120000  0xBE120000  0x002A0000  0x00000000
user.property     0xBE3E0000  0xBE3E0000  0x00010000  0x00000000
Radio.Config      0xBE3F0000  0xBE3F0000  0x00010000  0x00000000
}}}
{{{
RedBoot> fconfig -l
Run script at boot: false
Use BOOTP for network configuration: true
Console baud rate: 9600
DNS server IP address: 0.0.0.0
GDB connection port: 9000
Force console for special debug messages: false
Network debug at boot time: false
}}}
== Bootlog (original Buffalo firmware, MAC changed) ==
{{{
BusyBox v1.00 (2006.09.05-08:55+0000) Built-in shell (msh)
Enter 'help' for a list of built-in commands.

# reboot
umount: ramfs busy - remounted read-only
umount: none busy - remounted read-only
The system is going down NOW !!
Sending SIGTERM to all processes.
Jan  1 00:01:19 2006 (none) syslog.info System log daemon exiting.
Dec 31 23:01:19 udhcpd: Unable to open /tmp/udhcpd.lease for writing
Dec 31 23:01:19 udhcpd: Received a SIGTERM
Dec 31 23:01:19 dhcpcd: del resolve
Terminated
Please stand by while rebooting the system.
Restarting system.
+
*** Memory check:
 -> 0xA0FFFFFF
  success!! -> size : 16777216 bytes
FLASH configuration checksum error or invalid key
Ethernet eth0: MAC address 00:16:01:34:ff:ff
IP: 0.0.0.0/255.255.255.0, Gateway: 0.0.0.0
Default server: 0.0.0.0, DNS server IP: 0.0.0.0

RedBoot(tm) bootstrap and debug environment [ROM]
Non-certified release, version v2_0 - built 17:04:25, Jan 13 2006
Buffalo Version: 1.00.1.00

Copyright (C) 2000, 2001, 2002, Red Hat, Inc.

RAM: 0x80000400-0x81000000, 0x80000400-0x80fe1000 available
FLASH: 0xbe000000 - 0xbe3f0000, 63 blocks of 0x00010000 bytes each.
== Executing boot script in 3.000 seconds - enter ^C to abort

*** Flash check:
 -> check 'RedBoot'
 -> check 'vmlinux.bin.gz'
 -> check 'rootfs'
 -> check 'Radio.Config'
  success!!
*** go_script!
    System boot!!
Image loaded from 0x80002000-0x801af000
Now booting linux kernel:
 Base address 0x80080000 Entry 0x80182398
 Cmdline : root=/dev/mtdblock3
CPU revision is: 00018009
Primary instruction cache 16kB, physically tagged, 4-way, linesize 16 bytes.
Primary data cache 16kB 4-way, linesize 16 bytes.
Linux version 2.4.25 (vc03021@mkitec_vc03021) (gcc version 3.3.3) #1 2006年 9月 5日 火曜日 17:48:30 JST
Determined physical RAM map:
 memory: 02000000 @ 00000000 (usable)
On node 0 totalpages: 8192
zone(0): 8192 pages.
zone(1): 0 pages.
zone(2): 0 pages.
Kernel command line: console=ttyS0,9600  root=/dev/mtdblock3 panic=1
Using 110.000 MHz high precision timer.
Calibrating delay loop... 219.54 BogoMIPS
Memory: 30500k/32768k available (1523k kernel code, 2268k reserved, 96k data, 76k init, 0k highmem)
Dentry cache hash table entries: 4096 (order: 3, 32768 bytes)
Inode cache hash table entries: 2048 (order: 2, 16384 bytes)
Mount cache hash table entries: 512 (order: 0, 4096 bytes)
Buffer cache hash table entries: 1024 (order: 0, 4096 bytes)
Page-cache hash table entries: 8192 (order: 3, 32768 bytes)
Checking for 'wait' instruction...  available.
POSIX conformance testing by UNIFIX
Linux NET4.0 for Linux 2.4
Based upon Swansea University Computer Society NET3.039
Initializing RT netlink socket
Starting kswapd
devfs: v1.12c (20020818) Richard Gooch (rgooch@atnf.csiro.au)
devfs: boot_options: 0x1
pty: 256 Unix98 ptys configured
BUFFALO SWICH&LED DRIVER ver 1.00
Serial driver version 5.05c (2001-07-08) with no serial options enabled

ttyS00 at 0xbc000003 (irq = 37) is a 16550A
HDLC line discipline: version $Revision: #1 $, maxframe=4096
N_HDLC line discipline registered.
Generic MIPS RTC Driver v1.0
SLIP: version 0.8.4-NET3.019-NEWTTY (dynamic channels, max=256).
PPP generic driver version 2.4.2
PPP Deflate Compression module registered
PPP BSD Compression module registered
Buffalo WER-SERIES Board flash device mapping: 400000 at be000000
get_mtd_chip_driver:42: flag <jedec_probe>
get_mtd_chip_driver:42: flag <jedec>
get_mtd_chip_driver:42: flag <cfi_probe>
 Amd/Fujitsu Extended Query Table v1.3 at 0x0040
 This flash is supporting buffer-write-mode.
  (buffer size 32 bytes / write time 128-4096 us)
 Enable buffer-write-mode!!
Physically mapped flash: Swapping erase regions for broken CFI table.
number of CFI chips: 1
Using physmap partition definition
Creating 7 MTD partitions on "Physically mapped flash":
0x00000000-0x00050000 : "RedBoot"
0x00050000-0x00120000 : "vmlinux"
0x00120000-0x003d0000 : "rootfs"
0x003d0000-0x003e0000 : "RedBoot_config"
0x003e0000-0x003f0000 : "user_property"
0x003f0000-0x00400000 : "Boardinfo"
0x003f0000-0x00400000 : "Wlaninfo"
NET4: Linux TCP/IP 1.0 for NET4.0
IP Protocols: ICMP, UDP, TCP
IP: routing cache hash table of 512 buckets, 4Kbytes
TCP: Hash tables configured (established 2048 bind 4096)
ip_conntrack version 2.1 (256 buckets, 2048 max) - 344 bytes per conntrack
ip_conntrack_pptp version 1.9 loaded
ip_nat_pptp version 1.5 loaded
ip_tables: (C) 2000-2002 Netfilter core team
ipt_time loading
NET4: Unix domain sockets 1.0/SMP for Linux NET4.0.
NET4: Ethernet Bridge 008 for NET4.0
VFS: Mounted root (cramfs filesystem) readonly.
Mounted devfs on /dev
Freeing unused kernel memory: 76k freed
Algorithmics/MIPS FPU Emulator v1.5
MidLayer.c(1898) ML_Initialize :***** Please push init button if you want to init_reboot ******
Using /lib/modules/2.4.25/net/ae531x.o
Warning:AE531X: Atheros AR5312 integrated Ethernet controller Ver.1.0.6-atheros/20041015
 loading ae531x eth0: MACBASE:b8100000, PHYBASE=b8100000, DMABASE=b8101000
will taint the kernel: non-GPL license - Atheros
  See http://www.tux.org/lkml/#export-tainted for information eth1: MACBASE:b8200000, PHYBASE=b8200000, DMABASE=b8201000
about tainted modules
Using /lib/modules/2.4.25/net/ar5kap.o

Please press Enter to activate this console. Detected device id = 0057
ar5kap: Set wlan0 radio frequency 5180
802.11 a/b/g WLAN AP driver 3.3.0-145-Linux/AP Rel1.00-pl9-20050330 loaded
  Copyright (c) 2000-2004 Atheros Communications, Inc.
  Copyright (c) 2003,2004 NEC Informatec Systems Ltd.
  Copyright (c) 2004 Buffalo Inc.
wlan0: ar5kap at 0xb8000000, 00:16:01:34:ab:4a, IRQ 2
wlan0: revisions: mac 5.7 phy 4.2 analog 3.6
Detected device id = 0057
wlan1: ar5kap at 0xb8500000, 00:16:01:34:ab:4b, IRQ 5
wlan1: revisions: mac 5.7 phy 4.2 analog 4.6
et0: LAN port 4 link up
wireless access point starting...
etsiFeaturesEnable! 0
Radar scan beginning on all eligible channels
wlanFindChannel : buffalo_auto_channel = 1
InitSingleScan -- 5200, 2410  ofdm 5 passive scan
Auto Channel Scan selected 5200 MHz, channel 40
wlan0 Ready
Ready
wlan0: AP service started.
  TurboG:on DynamicTurbo:off Compression:off FastFrame:off Burst:off XR:off
wireless access point starting...
wlan1 Ready
Ready
wlan1: AP service started.
  TurboG:on DynamicTurbo:off Compression:off FastFrame:off Burst:off XR:off
Calling phyVportDeReg
wlan1: AP service stopped.
wireless access point starting...
wlan1 Ready
Ready
wlan1: AP service started.
  TurboG:on DynamicTurbo:off Compression:off FastFrame:off Burst:off XR:off
}}}
