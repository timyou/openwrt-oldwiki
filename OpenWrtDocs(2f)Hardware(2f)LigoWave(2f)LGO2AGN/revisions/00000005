#pragma section-numbers off

||<tablebgcolor="#f1f1ed" tablewidth="40%" tablestyle="margin: 0pt 0pt 1em 1em; float: right; font-size: 0.9em;"style="padding: 0.5em;">[[TableOfContents]]||

= LigoWave LGO2AGN =

I obtained the bare PCB from Titan Wireless (http://www.titanwirelessonline.com/ProductDetails.asp?ProductCode=TW-266-2), but it came with LigoWave firmware installed, and has a Deliberant DLB200 sticker on the PCB.

The MAC addresses have a Deliberant OUI (00193B = Deliberant LLC).

= Hardware =

== Info ==

||<tablewidth="460px" tableheight="345px">'''Architecture''' ||XScale IXP42x ||
||'''Vendor''' ||!LigoWave ||
||'''Bootloader''' ||!RedBoot ||
||'''System-On-Chip''' ||Intel IXP420 ||
||'''CPU Speed''' ||266 MHz ||
||'''Flash size''' ||16 MiB ||
||'''RAM''' ||64 MiB ||
||'''Wireless''' ||2x miniPCI ||
||'''Ethernet''' ||2x RJ45 10/100 ||
||'''USB''' ||No ||
||'''Serial''' ||Yes (RJ11) ||
||'''JTAG''' ||Yes (20pin ARM) ||
||'''Power''' ||48V POE ||

== Serial Port ==

You will need a serial cable adapter with RJ11-Male and RS-232 DB9-Female ends.
The wiring diagram is as follows:

{{{
          1 2 3 4 RJ11
       
          | | | |
          | | +-+
          | |   | 5 GROUND
          | 3
          |       RS232 DB9
          2
 
      
        RJ11 pin1    <--> DB9 pin2
        RJ11 pin2    <--> DB9 pin3
        RJ11 pin3&4  <--> DB9 pin5
}}}

The terminal settings for the connection:

115200 / 8 data bits / no parity / 1 stop bit / no flow control

== Photos ==

http://www.titanwirelessonline.com/v/vspfiles/photos/TW-266-2-2.jpg

== JTAG ==

There seems to be a 20 pin JTAG, but it is not that important as the !RedBoot boatloader does not seem to be crippled.

= Original software =
{{{
+Ethernet eth1: MAC address 00:01:af:00:20:ec
IP: 192.168.2.99/255.255.255.0, Gateway: 0.0.0.0
Default server: 192.168.2.100, DNS server IP: 0.0.0.0

RedBoot(tm) bootstrap and debug environment [ROM]
Red Hat certified release, version 1.92 - built 21:10:32, Dec 16 2003

Platform: IXDP425 Development Platform (XScale)
Copyright (C) 2000, 2001, 2002, Red Hat, Inc.

RAM: 0x00000000-0x10000000, 0x0001f880-0x0ffd1000 available
FLASH: 0x50000000 - 0x51000000, 128 blocks of 0x00020000 bytes each.
== Executing boot script in 1.000 seconds - enter ^C to abort
RedBoot> fis load kernel1
RedBoot> exec -c "root=/dev/mtdblock2 init=/linuxrc ro"
Using base address 0x01600000 and length 0x00100000
Uncompressing Linux................................................................ done, booting the kernel.
[17179569.184000] Linux version 2.6.18.8 (buildd2@builder) (gcc version 4.1.2 20061007 (prerelease)) #1 Tue Dec 11 23:12:10 EET 2007
[17179569.184000] CPU: XScale-IXP42x Family [690541f2] revision 2 (ARMv5TE), cr=000039ff
[17179569.184000] Machine: Intel IXDP425 Development Platform
[17179569.184000] Memory policy: ECC disabled, Data cache writeback
[17179569.184000] CPU0: D VIVT undefined 5 cache
[17179569.184000] CPU0: I cache: 32768 bytes, associativity 32, 32 byte lines, 32 sets
[17179569.184000] CPU0: D cache: 32768 bytes, associativity 32, 32 byte lines, 32 sets
[17179569.184000] Built 1 zonelists.  Total pages: 16384
[17179569.184000] Kernel command line: root=/dev/mtdblock2 console=ttyS0,115200 ro init=/linuxrc root=/dev/mtdblock2 init=/linuxrc ro
[17179569.184000] PID hash table entries: 512 (order: 9, 2048 bytes)
[17179569.184000] Dentry cache hash table entries: 8192 (order: 3, 32768 bytes)
[17179569.184000] Inode-cache hash table entries: 4096 (order: 2, 16384 bytes)
[17179569.192000] Memory: 64MB = 64MB total
[17179569.192000] Memory: 62860KB available (1588K code, 327K data, 88K init)
[17179569.288000] Mount-cache hash table entries: 512
[17179569.288000] CPU: Testing write buffer coherency: ok
[17179569.292000] NET: Registered protocol family 16
[17179569.292000] IXP4xx: Using 16MiB expansion bus window size
[17179569.292000] PCI: IXP4xx is host
[17179569.292000] PCI: IXP4xx Using direct access for memory space
[17179569.292000] PCI: bus0: Fast back to back transfers enabled
[17179569.292000] dmabounce: registered device 0000:00:01.0 on pci bus
[17179569.292000] dmabounce: registered device 0000:00:03.0 on pci bus
[17179569.296000] NET: Registered protocol family 2
[17179569.332000] IP route cache hash table entries: 512 (order: -1, 2048 bytes)
[17179569.332000] TCP established hash table entries: 2048 (order: 1, 8192 bytes)
[17179569.332000] TCP bind hash table entries: 1024 (order: 0, 4096 bytes)
[17179569.332000] TCP: Hash tables configured (established 2048 bind 1024)
[17179569.332000] TCP reno registered
[17179569.332000] NetWinder Floating Point Emulator V0.97 (double precision)
[17179569.332000] squashfs: version 3.2-r2 (2007/01/15) Phillip Lougher
[17179569.332000] squashfs: LZMA suppport for slax.org by jro
[17179569.332000] JFFS2 version 2.2. (NAND) (C) 2001-2006 Red Hat, Inc.
[17179569.336000] Initializing Cryptographic API
[17179569.336000] io scheduler noop registered (default)
[17179569.496000] IXP4xx Watchdog Timer: heartbeat 60 sec
[17179569.496000] ixp425_gpio: IXP425 GPIO driver loaded
[17179569.496000] Serial: 8250/16550 driver $Revision: 1.90 $ 4 ports, IRQ sharing disabled
[17179569.500000] serial8250.0: ttyS0 at MMIO 0xc8000000 (irq = 15) is a XScale
[17179569.744000] serial8250.0: ttyS1 at MMIO 0xc8001000 (irq = 13) is a XScale
[17179569.752000] PPP generic driver version 2.4.2
[17179569.756000] PPP Deflate Compression module registered
[17179569.760000] PPP BSD Compression module registered
[17179569.768000] NET: Registered protocol family 24
[17179569.772000] IXP4XX-Flash.0: Found 1 x16 devices at 0x0 in 16-bit bank
[17179569.780000]  Intel/Sharp Extended Query Table at 0x0031
[17179569.784000] Using buffer write method
[17179569.788000] cfi_cmdset_0001: Erase suspend on write enabled
[17179569.796000] Searching for RedBoot partition table in IXP4XX-Flash.0 at offset 0xfe0000
[17179569.924000] drivers/mtd/redboot.c: adjusted dev mtd1 size from 4096 to 131072 bytes
[17179569.932000] 9 RedBoot partitions found on MTD device IXP4XX-Flash.0
[17179569.940000] Creating 9 MTD partitions on "IXP4XX-Flash.0":
[17179569.948000] 0x00000000-0x00040000 : "RedBoot"
[17179569.952000] 0x00040000-0x00140000 : "kernel1"
[17179569.956000] 0x00140000-0x00640000 : "cramfs1"
[17179569.960000] 0x00640000-0x00740000 : "kernel2"
[17179569.964000] 0x00740000-0x00c40000 : "cramfs2"
[17179569.972000] 0x00c40000-0x00cc0000 : "cfg"
[17179569.976000] 0x00ce0000-0x00fc0000 : "etc"
[17179569.980000] 0x00fc0000-0x00fe0000 : "RedBoot config"
[17179569.984000] 0x00fe0000-0x01000000 : "FIS directory"
[17179569.992000] TCP bic registered
[17179569.996000] NET: Registered protocol family 1
[17179570.008000] VFS: Mounted root (squashfs filesystem) readonly.
[17179570.016000] Freeing init memory: 88K
Populating '/etc/' directory structure ... done.
Linking '/usr/etc/*' files under '/etc' ... done
Starting /sbin/init ...
init started: BusyBox v1.5.0 (2007-12-11 23:06:30 EET) multi-call binary
starting pid 77, tty '': '/etc/rc.d/rc.sysinit'
[17179573.484000] ixp400: module license 'unspecified' taints kernel.
[17179574.024000] ixp400_eth: Initializing IXP400 NPE Ethernet driver software v. 1.6
[17179574.032000] ixp400_eth: CPU clock speed (approx) = 265 MHz
[17179574.556000] [message] ixEthMiiPhyScan, Mii 1: Mii PHY ID 00008201
[17179575.060000] [message] ixEthMiiPhyScan, Mii 3: Mii PHY ID 00008201
[17179575.264000] ixp400_eth: ixp0 is using NPEB and the PHY at address 1
[17179575.268000] ixp400_eth: ixp1 is using NPEC and the PHY at address 2
[17179575.280000] ixp400_eth: Use default MAC address 00:02:b3:01:01:01 for port 0
[17179575.288000] ixp400_eth: Use default MAC address 00:02:b3:02:02:02 for port 1
[17179575.576000] ath_hal: 0.9.18.0 (AR5210, AR5211, AR5212, RF5111, RF5112, RF2413, RF5413, REGOPS_FUNC)
[17179575.964000] wlan: 0.8.4.2 (svn r18123)
[17179576.164000] wlan: mac acl policy registered
modprobe: module ath_rate_minstrel not found
modprobe: failed to load module ath_rate_minstrel
[17179576.568000] ath_rate_sample: 1.2 (svn r18123)
[17179576.808000] ath_pci: 0.9.4.5 (svn r18123)
[17179576.812000] PCI: enabling device 0000:00:01.0 (0340 -> 0342)
[17179577.348000] ath_find_eeprom: macaddr location in hal found at c02ba6a8 offset from last chan 6844
[17179577.356000] ath_print_eeprom: mac: 00:0b:6b:85:b9:97, version 0x4008, regdomain 0x0 A/B/G=1/1/1
[17179577.364000] ath_print_eeprom: antennaGain= 0x1/0x1
[17179577.368000] ath_print_eeprom: cntls:0x10:0x13:0x11:0x12:0x14:0x40:0x30:0x31:0x32:0x34:0x0:0x0:0x0:0x0:0x0:0x0:0x0:0x0:0x0:0x0:0x0:0x0:0x0:0x0:0x0:0x0:0x0:0x0:0x0:0x0:0x0:0x0
[17179577.388000] wifi0: 11a rates: 6Mbps 9Mbps 12Mbps 18Mbps 24Mbps 36Mbps 48Mbps 54Mbps
[17179577.396000] wifi0: 11b rates: 1Mbps 2Mbps 5.5Mbps 11Mbps
[17179577.400000] wifi0: 11g rates: 1Mbps 2Mbps 5.5Mbps 11Mbps 6Mbps 9Mbps 12Mbps 18Mbps 24Mbps 36Mbps 48Mbps 54Mbps
[17179577.412000] wifi0: turboA rates: 6Mbps 9Mbps 12Mbps 18Mbps 24Mbps 36Mbps 48Mbps 54Mbps
[17179577.420000] wifi0: turboG rates: 6Mbps 12Mbps 18Mbps 24Mbps 36Mbps 48Mbps 54Mbps
[17179577.428000] wifi0: H/W encryption support: WEP AES AES_CCM TKIP
[17179577.432000] wifi0: mac 5.9 phy 4.3 radio 3.6
[17179577.440000] wifi0: Use hw queue 1 for WME_AC_BE traffic
[17179577.444000] wifi0: Use hw queue 0 for WME_AC_BK traffic
[17179577.448000] wifi0: Use hw queue 2 for WME_AC_VI traffic
[17179577.456000] wifi0: Use hw queue 3 for WME_AC_VO traffic
[17179577.460000] wifi0: Use hw queue 8 for CAB traffic
[17179577.464000] wifi0: Use hw queue 9 for beacons
[17179577.468000] wifi0: TX99 support enabled
[17179577.476000] wifi0: Atheros 5212: mem=0x48000000, irq=28
[17179577.480000] PCI: enabling device 0000:00:03.0 (0340 -> 0342)
[17179578.012000] ath_find_eeprom: macaddr location in hal found at c346a6a8 offset from last chan 6844
[17179578.024000] ath_print_eeprom: mac: 00:0b:6b:85:bb:59, version 0x4008, regdomain 0x0 A/B/G=1/1/1
[17179578.032000] ath_print_eeprom: antennaGain= 0x1/0x1
[17179578.036000] ath_print_eeprom: cntls:0x10:0x13:0x11:0x12:0x14:0x40:0x30:0x31:0x32:0x34:0x0:0x0:0x0:0x0:0x0:0x0:0x0:0x0:0x0:0x0:0x0:0x0:0x0:0x0:0x0:0x0:0x0:0x0:0x0:0x0:0x0:0x0
[17179578.056000] wifi1: 11a rates: 6Mbps 9Mbps 12Mbps 18Mbps 24Mbps 36Mbps 48Mbps 54Mbps
[17179578.064000] wifi1: 11b rates: 1Mbps 2Mbps 5.5Mbps 11Mbps
[17179578.068000] wifi1: 11g rates: 1Mbps 2Mbps 5.5Mbps 11Mbps 6Mbps 9Mbps 12Mbps 18Mbps 24Mbps 36Mbps 48Mbps 54Mbps
[17179578.080000] wifi1: turboA rates: 6Mbps 9Mbps 12Mbps 18Mbps 24Mbps 36Mbps 48Mbps 54Mbps
[17179578.088000] wifi1: turboG rates: 6Mbps 12Mbps 18Mbps 24Mbps 36Mbps 48Mbps 54Mbps
[17179578.096000] wifi1: H/W encryption support: WEP AES AES_CCM TKIP
[17179578.100000] wifi1: mac 5.9 phy 4.3 radio 3.6
[17179578.104000] wifi1: Use hw queue 1 for WME_AC_BE traffic
[17179578.112000] wifi1: Use hw queue 0 for WME_AC_BK traffic
[17179578.116000] wifi1: Use hw queue 2 for WME_AC_VI traffic
[17179578.124000] wifi1: Use hw queue 3 for WME_AC_VO traffic
[17179578.128000] wifi1: Use hw queue 8 for CAB traffic
[17179578.132000] wifi1: Use hw queue 9 for beacons
[17179578.136000] wifi1: TX99 support enabled
[17179578.140000] wifi1: Atheros 5212: mem=0x48010000, irq=26
RedBoot config checksum OK
ixp0: 00 19 3B 00 03 D7
ixp1: 00 19 3B 00 03 D8
[17179578.548000] NET: Registered protocol family 17
Waiting for reset to factory defaults packet.....
starting pid 147, tty '': '/usr/etc/rc.d/rc-bg'
starting pid 151, tty '/dev/ttyS0': '/sbin/getty'
ath0
ath1

WILIBOX login: [17179585.588000] ip_tables: (C) 2000-2006 Netfilter Core Team
[17179585.880000] ip_conntrack version 2.4 (512 buckets, 4096 max) - 212 bytes per conntrack
[17179587.164000] Bridge firewalling registered
[17179587.300000] device ath0 entered promiscuous mode
[17179587.388000] device ath1 entered promiscuous mode
/usr/etc/init.d/plugin: line 98: ethtool: not found
[17179587.476000] br0: port 2(ath1) entering learning state
[17179587.480000] br0: port 1(ath0) entering learning state
/usr/etc/init.d/plugin: line 98: ethtool: not found
/usr/etc/init.d/plugin: line 98: ethtool: not found
/usr/etc/init.d/plugin: line 98: ethtool: not found
00:00:18 [I] Launched 'sshd' successfully in respawning mode.
ls: /etc/persistent/skins/*.tgz: No such file or directory
[17179588.480000] br0: topology change detected, propagating
[17179588.484000] br0: port 2(ath1) entering forwarding state
[17179588.488000] br0: topology change detected, propagating
[17179588.496000] br0: port 1(ath0) entering forwarding state
00:00:19 [I] Launched 'httpd' successfully in respawning mode.
00:00:19 [I] Launched 'udhcpcixp1' successfully in respawning mode.
RTNETLINK answers: File exists
00:00:22 [I] Launched 'dnsmasq' successfully in respawning mode.
Reconfiguring syslogged...
00:00:22 [I] Launched 'discoveryd' successfully in respawning mode.
00:00:23 [I] Launched 'syslog' successfully in respawning mode.
admin: Boot finished. Ready to serve ...
}}}
== Flash layout ==
{{{
RedBoot> fis list
Name              FLASH addr  Mem addr    Length      Entry point
RedBoot           0x50000000  0x50000000  0x00040000  0x00000000
RedBoot config    0x50FC0000  0x50FC0000  0x00001000  0x00000000
FIS directory     0x50FE0000  0x50FE0000  0x00020000  0x00000000
kernel1           0x50040000  0x01600000  0x00100000  0x01600000
cramfs1           0x50140000  0x00800000  0x00500000  0x00800000
kernel2           0x50640000  0x01600000  0x00100000  0x00800000
cramfs2           0x50740000  0x00800000  0x00500000  0x00800000
cfg               0x50C40000  0x00800000  0x00080000  0x00800000
etc               0x50CE0000  0x00800000  0x002E0000  0x00800000
RedBoot>
}}}

= Telnet into RedBoot =
You can change the !RedBoot configuration, so you can later telnet into this bootloader in order to reflash this device from there, without having serial access.

The default form of the fconfig command will force you to enter the data, change and confirm every initialized variable. To avoid reentering the '''Boot script''' data and harming unnecessary variables, run the "fconfig list" command first to look at variable names and values:

{{{
RedBoot> fconfig -l -n
boot_script: true
boot_script_data:
.. fis load kernel1
.. exec -c "root=/dev/mtdblock2 init=/linuxrc ro"

boot_script_timeout: 1
bootp: false
bootp_my_gateway_ip: 0.0.0.0
bootp_my_ip: 192.168.2.99
bootp_my_ip_mask: 255.255.255.0
bootp_server_ip: 192.168.2.100
console_baud_rate: 115200
dns_ip: 0.0.0.0
gdb_port: 9000
info_console_force: false
net_debug: false
net_device: npe_eth1
npe_eth0_esa: 0x00:0x19:0x3B:0x00:0x03:0xD7
npe_eth1_esa: 0x00:0x19:0x3B:0x00:0x03:0xD8
device_type: LGO2AGN
}}}
Next change only necessary variables (using their names from the previous listing) and update the !RedBoot non-volatile configuration after the last change:

{{{
RedBoot> fconfig boot_script_timeout 10
boot_script_timeout: Setting to 10
Update RedBoot non-volatile configuration - continue (y/n)? n
RedBoot> fconfig bootp_my_ip 192.168.1.10
bootp_my_ip: Setting to 192.168.1.10
Update RedBoot non-volatile configuration - continue (y/n)? n
RedBoot> fconfig bootp_my_gateway_ip 192.168.1.254
bootp_my_gateway_ip: Setting to 192.168.1.254
Update RedBoot non-volatile configuration - continue (y/n)? n
RedBoot> fconfig dns_ip 192.168.1.254
dns_ip: Setting to 192.168.1.254
Update RedBoot non-volatile configuration - continue (y/n)? n
RedBoot> fconfig bootp_server_ip 192.168.1.254
bootp_server_ip: Setting to 192.168.1.254
Update RedBoot non-volatile configuration - continue (y/n)? y
... Unlock from 0x50fc0000-0x50fc1000: .
... Erase from 0x50fc0000-0x50fc1000: .
... Program from 0x0ffd2000-0x0ffd3000 at 0x50fc0000: .
... Lock from 0x50fc0000-0x50fc1000: .
}}}
'''Note:''''' ''The configuration is only in the RAM until you update'' ''the !RedBoot non-volatile configuration. If you reset the device without updating, the configuration will not be changed. You can use changes without the update for temporary settings.

Verify the configuration by listing the aliases this time:

{{{
RedBoot> fconfig -l
Run script at boot: true
Boot script:
.. fis load kernel1
.. exec -c "root=/dev/mtdblock2 init=/linuxrc ro"

Boot script timeout (1000ms resolution): 10
Use BOOTP for network configuration: false
Gateway IP address: 192.168.1.254
Local IP address: 192.168.1.10
Local IP address mask: 255.255.255.0
Default server IP address: 192.168.1.254
Console baud rate: 115200
DNS server IP address: 192.168.1.254
GDB connection port: 9000
Force console for special debug messages: false
Network debug at boot time: false
Default network device: npe_eth1
npe_eth0_esa: 0x00:0x19:0x3B:0x00:0x03:0xD7
npe_eth1_esa: 0x00:0x19:0x3B:0x00:0x03:0xD8
device_type: LGO2AGN
}}}
I specified a 10 second timeout here, so I have this 10 second time frame to telnet into !RedBoot. If you are not able to hit the enter-key within 10 seconds after powering up, go for a larger time frame.

{{{
$ arping -qf 192.168.1.10 ; telnet 192.168.1.10 9000
WARNING: interface is ignored: Operation not permitted
Trying 192.168.1.10...
?Invalid command
Connected to 192.168.1.10.
Escape character is '^]'.
== Executing boot script in 9.940 seconds - enter ^C to abort
^C
RedBoot>
}}}

= Resources =
 * [http://www.ligowave.com/landing/specs/LGO2AGN.pdf Data Sheet]
 * [http://support.ligowave.com/files/folders/427/download.aspx Original Firmware Image]
 * [http://support.ligowave.com/files/folders/339/download.aspx Original Firmware Manual]

----
["CategoryIXP4xxDevice"]
