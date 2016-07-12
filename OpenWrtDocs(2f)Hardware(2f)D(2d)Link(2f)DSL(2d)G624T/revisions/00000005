= Work in Progress =
Porting OpenWrt to the [http://www.d-link.co.uk/?go=gNTyP9CgrdFOIC4AStFCF834mptYKO9ZTdvhLPG3yV3oVo5+hKltbNlwaaFp6DQoHDrszSBF9oUJBtnv DSL-G624T] is a work in progress.

== Specifications ==
Wireless 4-Port ADSL Router with Firewall/QoS Control (ADSL 2/2+ Compliant)

CPU: Texas Instruments AR7 MIPS-based, [http://focus.ti.com/general/docs/bcg/bcggencontent.tsp?templateId=6116&navigationId=11917&path=templatedata/cm/general/data/bcgmiddl/ar7_cpe TNETD73000AZDW]

Flash chip: 4Mbytes, SAMSUNG, [http://www.samsung.com/Products/Semiconductor/NORFlash/32Mbit/K8D3216UBC/K8D3216UBC.htm K8D3216UBC], 32Mbit NOR-type Flash Memory organized as 4M x 8

SDRAM: 16Mbytes, ESMT, [http://www.esmt.com.tw/english/products_de.asp?CLASS_L1=7&CLASS_L2=54&CLASS_L3=62&CLASS_L4=0#62 M12L128168A-7T], 3.3V at 143MHz organised as 8M x 16

Switch: Infineon, [http://www.infineon.com/cgi-bin/ifx/portal/ep/channelView.do?channelId=-65146&channelPage=/ep/channel/productOverview.jsp&pageTypeId=17099 ADM6996M]

Wireless NIC: Texas Instruments, TI ACX111 (["VLYNQ"])

4x-ethernet-port transformer: YCL, [http://www.ycl.com.tw/ycl_products?kind=pf&catid=116 PH402466AG]

Boot loader: ["ADAM2"]

A picture of the inside is available as well: [http://luca.pca.it/projects/dlink/hpim1913.jpg hpim1913.jpg]

== How to get OpenWRT onto the router ==

Refer to the general OpenWRT build documentation ([http://downloads.openwrt.org/kamikaze/docs/openwrt.html#x1-320002.1 here]), this section is only about specific procedures and options you'll need.

First of all the latest SVN snapshot with a 2.6.22 kernel (r9234) is recommended, since 2.6.23 isn't stable yet. So don't download the head SVN but type this instead :
{{{
svn -r 9234 checkout https://svn.openwrt.org/openwrt/trunk
}}}

Be sure you know the ADAM2 IP address before proceeding as explained [wiki:OpenWrtDocs/TroubleshootingAR7 here].

'''menuconfig options'''

Those are the changes you need to make to the default configuration, so if options aren't in the following, '''that doesn't mean you have to untick them''', only untick an option if you cross an "empty" < > or [ ].
I can however suggest you to customize the configuration according to your needs, and for this matter I put some suggestions in the second quote.

Mandatory options:
{{{
Target System (TI AR7 [2.6])
Target Profile (Texas Instruments WiFi (default))
Base system
   <*> br2684ctl                                 (for PPPoE)
   busybox
      Configuration
         Networking Utilities
            [ ] udhcp Client (udhcpc)            (useless since the WAN is PPP)
Network
   <*> hostapd-mini
   ppp
      <*> ppp-mod-pppoa                          (for PPPoA)
   <*> wpa-supplicant
Kernel modules
   Network Devices
      <*> kmod-sangam-atm-annex-a
      <*> kmod-sangam-atm-annex-b                (actually you'll barely use both of them in your lifetime..)
}}}

Some suggestions:
{{{
Base system
   busybox
      Configuration
         Networking Utilities
            [ ] httpd                            (you most likely don't need a HTTP server)
   <*> qos-scripts
Utilities
   <*> dropbearconvert
}}}

I recommend also to include some third-party packages :
{{{
updatedd      (DDNS client)
miniupnpd     (lightweight UPnP IGD server)
}}}

'''Upload the firmware'''

Once the firwmare is compiled, you need to upload it to the router.  For this, you can use the adam2flash.pl script present in the scripts/ folder.  First of all, be sure that you can connect to the ADAM2 bootloader.  Using an ethernet cable (during the booting process the wireless isn't available), configure your network card in the same IP range as ADAM2 and then switch the router on.  After 2 seconds you can connect to it (substitute 192.168.1.1 with your ADAM2 IP address):

{{{
$ telnet 192.168.1.1 21
Trying 192.168.1.1...
Connected to 192.168.1.1.
Escape character is '^]'.
220 ADAM2 FTP Server ready.
USER adam2
331 Password required for adam2.
PASS adam2
230 User adam2 successfully logged in.
GETENV mtd0
mtd0                  0x900a1000,0x903f0000
200 GETENV command successful
GETENV mtd1
mtd1                  0x90010090,0x900a1000
200 GETENV command successful
GETENV mtd2
mtd2                  0x90000000,0x90010000
200 GETENV command successful
GETENV mtd3
mtd3                  0x903f0000,0x90400000
200 GETENV command successful
GETENV mtd4
mtd4                  0x90010000,0x903f0000
200 GETENV command successful
^]
telnet> quit
Connection closed.
}}}
Then, choose which compiled firwmare you want to upload from the ones available in the bin/ folder:

{{{
$ scripts/adam2flash.pl 192.168.1.1 bin/openwrt-ar7-2.6-squashfs.bin
Looking for device: .... found!
ADAM2 version 0.22.2 at 192.168.1.1 (192.168.1.1)
Available flash space: 0x003dff70 (0x00090f70 + 0x0034f000)
Writing to mtd1...
can't open data connection
}}}
On IRC, nbd advised me to try to write to mtd4 because of the strange mtd1 memory mapping.  I'll report back here as soon as I'd have tested it.

Sam Liddicott could not update mtd1 or mtd0 using adam2flash.pl or the ftp instructions at [":OpenWrtDocs/Hardware/D-Link/DSL-502T"], getting this ftp error:
{{{
550 Flash erase failed
}}}
but he could update mtd4 using the manual ftp instructions.  As far as he could tell the linux image never booted and he had to restore his mtd settings and the dlink image which worked; and strangely had all of his dlink settings intact. He wonders if the open wrt erase+flash even did anything at all - maybe the mtd boundary changes stopped it booting and openwrt was never there at all?



== Informations from the D-Link firmware ==
Firmware: [ftp://ftp.d-link.de/dsl/dsl-g624t/driver_software V3.02B01T02.EU-A.20061124]

{{{
# cat /proc/cpuinfo
processor               : 0
cpu model               : MIPS 4KEc V4.8
BogoMIPS                : 149.91
wait instruction        : no
microsecond timers      : yes
extra interrupt vector  : yes
hardware watchpoint     : yes
VCED exceptions         : not available
VCEI exceptions         : not available}}}
{{{
# cat /proc/meminfo
        total:    used:    free:  shared: buffers:  cached:
Mem:  14528512 13832192   696320        0  1769472  3592192
Swap:        0        0        0
MemTotal:        14188 kB
MemFree:           680 kB
MemShared:           0 kB
Buffers:          1728 kB
Cached:           3508 kB
SwapCached:          0 kB
Active:           5684 kB
Inactive:         1644 kB
HighTotal:           0 kB
HighFree:            0 kB
LowTotal:        14188 kB
LowFree:           680 kB
SwapTotal:           0 kB
SwapFree:            0 kB}}}
{{{
# cat /proc/mounts
/dev/mtdblock/0 / squashfs ro 0 0
none /dev devfs rw 0 0
proc /proc proc rw 0 0
ramfs /var ramfs rw 0 0}}}
{{{
# cat /proc/mtd
dev:    size   erasesize  name
mtd0: 0034f000 00010000 "mtd0"
mtd1: 00090f70 00010000 "mtd1"
mtd2: 00010000 00002000 "mtd2"
mtd3: 00010000 00010000 "mtd3"
mtd4: 003e0000 00010000 "mtd4"}}}
{{{
# cat /proc/version
Linux version 2.4.17_mvl21-malta-mips_fp_le (jenny@FD5) (gcc version
2.95.3 20010315 (release/MontaVista)) #1 Fri Nov 24 10:35:39 CST 2006}}}
{{{
# cat /proc/tty/driver/serial
serinfo:1.0 driver:5.05c revision:2001-07-08
0: uart:16550A port:A8610E00 irq:15 baud:2258 tx:40645 rx:0 RTS|DTR
1: uart:16550A port:A8610F00 irq:16 tx:0 rx:0 RTS|DTR}}}
{{{
# cat /proc/ticfg/env
memsize 0x01000000
flashsize       0x00400000
modetty0        38400,n,8,1,hw
modetty1        38400,n,8,1,hw
bootserport     tty0
cpufrequency    150000000
sysfrequency    125000000
bootloaderVersion       0.22.02
Adam2_Release   0.22.02_b04_Mar 10 2005
ProductID       AR7RD
HWRevision      Unknown
SerialNumber    00:11:22:33:44:55
my_ipaddress    192.168.1.1
prompt  Adam2_AR7RD
firstfreeaddress        0x9401d888
req_fullrate_freq       125000000
maca    00:11:22:33:44:55
mtd0    0x900a1000,0x903f0000
mtd1    0x90010090,0x900a1000
mtd2    0x90000000,0x90010000
mtd3    0x903f0000,0x90400000
mtd4    0x90010000,0x903f0000
autoload        1
autoload_timeout        7
StaticBuffer    120
SW_FEATURES     0X8000
vcc_encaps0     0.0
vcc_encaps1     0.0
vcc_encaps2     0.0
vcc_encaps3     0.0
vcc_encaps4     0.0
vcc_encaps5     0.0
vcc_encaps6     0.0
vcc_encaps7     0.0
modulation      0xffff
eoc_vendor_id   DLink
enable_margin_retrain   1
eoc_vendor_serialnum    00:11:22:33:44:55
invntry_vernum  2006053000000000
eoc_vendor_revision     20060208
HWA_0   00:11:22:33:44:55
mac_ap  00:11:22:33:44:55
usb_vid 0x0
usb_pid 0x0
usb_man N/A
usb_prod        N/A}}}

----
 . ["CategoryAR7Device"]
----
["CategoryAR7Device"]
