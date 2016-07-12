[[TableOfContents]]

= Linksys WAG54G2 v1.0 =
NOTE: The Linksys WAG54G2 is NOT version 2 of the WAG54G, it's totally different hardware.

WAG54G2 is an ADSL gateway router with 4 (available) port 10/100 ethernet switch, ADSL 2+ modem, 802.11g Wireless access point.

OpenWRT doesn't support this platform yet, but i'm going to have a go at getting it running. So, for now, this page is preliminary info.

== Hardware ==
Based on the Conexant CX94610 ADSL2plus chipset, which is a SoC with an ARM1026EJ core. Ethernet switch is an IC+ IP175 5 port, 4 ports are available on the back panel. WLAN: unknown Conexant, WLAN chips are covered by an aluminium screen on the board 16 MB SDRAM 4 MB Flash

== Serial Console ==
''will add photo later''


Serial Console is available as a header on board (mine was covered with soldermask which needed scraping before I could solder it).

It's connector J2, at one of the corners of the board, which is 4 pins (pin 4 is marked with a "4":-

Pin 1: GND
Pin 2: TXD
Pin 3: VCC
Pin 4: RXD



The board runs at 3.3V, but I had success with the serial console with a Maxim MAX232CPE (which is nominally 5V rated). Connect at 38,400 8N1 with no flow control.

= Software =
The linksys software is based on kernel 2.6.11 with plenty of patching. GPL code is available from linksys [ftp://ftp.linksys.com/opensourcecode/wag54g2/1.00.10/WAG54G2_GPL_v1.00.10_AnnexA.tgz here].

You can get root from the serial console just by pressing enter- no login needed.

== Boot Loader ==
The boot loaded is 'PP Boot' - conexant specific. Have a look ["OpenWrtDocs/Bootloaders/PP Boot"]

== Boot Log ==

{{{ FSB v0.06 PLL w ln p08 zi

Solos 461x PP boot v1.5

SDRAM size = 0x1000000
Processor clock speed 264.0MHz
Flash is Mirror_BIT device!
mac addr : 
00 21 29 7c 3c c3 
Flash is Mirror_BIT device!
Finding flashfs partition...done.

Image 'image' is a Linux kernel
Trying to load initrd...none found
Calling Configure_NVS_FromFile.

Flash is Mirror_BIT device!
Invalid Linux kernel command line support status. Using default info 
LZMA 4.05
00bXLinux version 2.6.11.12 (fred@localhost.localdomain) (gcc version 4.0.1) #52 Tue Jul 29 15:08:29 CST 2008
CPU: ARM1026EJ-Sid(wb)B [4106a262] revision 2 (ARMv5TEJ)
CPU0: D VIVT write-back cache
CPU0: I cache: 16384 bytes, associativity 4, 32 byte lines, 128 sets
CPU0: D cache: 8192 bytes, associativity 4, 32 byte lines, 64 sets
Machine: Solos CX46xx, unknown variant
Memory policy: ECC disabled, Data cache writeback
Built 1 zonelists
Kernel command line: console=ttyS0 root=31:2 mem=15M rw mtdparts=phys_mapped_flash:128k(boot),640k(kernel),3264k(fs),-(nvram) rootfstype=squashfs
init_dma not supported 
PID hash table entries: 64 (order: 6, 1024 bytes)
Dentry cache hash table entries: 2048 (order: 1, 8192 bytes)
Inode-cache hash table entries: 1024 (order: 0, 4096 bytes)
Memory: 15MB = 15MB total
Memory: 13032KB available (1545K code, 492K data, 84K init)
Mount-cache hash table entries: 512 (order: 0, 4096 bytes)
CPU: Testing write buffer coherency: ok
NET: Registered protocol family 16
Generic PHY: Registered new driver
NetWinder Floating Point Emulator V0.97 (double precision)
squashfs: version 3.2-r2 (2007/01/15) Phillip Lougher
squashfs: LZMA suppport for slax.org by jro
Initializing Cryptographic API
Solos on-chip UART init.
ttyS0 at I/O 0x0 (irq = 29) is a Solos UART
io scheduler noop registered
RAMDISK driver initialized: 1 RAM disks of 11268K size 1024 blocksize
IP175: Registered new driver
RTL18305SC: Registered new driver
PPP generic driver version 2.4.2
NET: Registered protocol family 24
physmap flash device: 400000 at 38000000
phys_mapped_flash: Found 1 x16 devices at 0x0 in 8-bit bank
 Amd/Fujitsu Extended Query Table at 0x0040
number of CFI chips: 1
cfi_cmdset_0002: Disabling erase-suspend-program due to code brokenness.
4 cmdlinepart partitions found on MTD device phys_mapped_flash
Creating 4 MTD partitions on "phys_mapped_flash":
0x00000000-0x00020000 : "boot"
0x00020000-0x000c0000 : "kernel"
0x000c0000-0x003f0000 : "fs"
0x003f0000-0x00400000 : "nvram"
u32 classifier
    OLD policer on 
NET: Registered protocol family 2
IP: routing cache hash table of 512 buckets, 4Kbytes
TCP established hash table entries: 512 (order: 0, 4096 bytes)
TCP bind hash table entries: 512 (order: -1, 2048 bytes)
TCP: Hash tables configured (established 512 bind 512)
GRE over IPv4 tunneling driver
ip_conntrack version 2.1 (120 buckets, 960 max) - 272 bytes per conntrack
ip_conntrack_rtsp v0.6.21 loading
ip_nat_rtsp v0.6.21 loading
ip_tables: (C) 2000-2002 Netfilter core team
ipt_random match loaded
ip_conntrack_pptp version 3.0 loaded
ip_nat_pptp version 3.0 loaded
Initializing IPsec netlink socket
NET: Registered protocol family 1
NET: Registered protocol family 17
NET: Registered protocol family 15
NET: Registered protocol family 8
NET: Registered protocol family 20
802.1Q VLAN Support v1.8 Ben Greear <greearb@candelatech.com>
All bugs added by David S. Miller <davem@redhat.com>
VFS: Mounted root (squashfs filesystem) readonly.
Freeing init memory: 84K

init started:  BusyBox v1.00 (2008.07.29-07:03+0000) multi-call binary

init started:  BusyBox v1.00 (2008.07.29-07:03+0000) multi-call binary

new_init_action:action=1

Starting pid 14, console /dev/ttyS0: '/etc/rcS'
mkdir: Cannot create directory `/etc/dnrd': Unknown error 30
led: module license 'Proprietary' taints kernel.
will read pda file
found header
count=3586
dump_to_file
 Loading ether driver ...
solos_eth_mii: probed
 Loading Conexant BSP...
BASE MAC ADDRESS 00:c0:02:12:35:88

Starting Conexant drivers
.
Quantum v1.01
 msc16 loaded 

Conexant drivers started
starting task turbo_WhipTask
DSL MSC16 imem 4096, dmem 2048

DSL MSC16 version 1.3
 Loading Wireless ...
 Reading True PDA ...
DRIVER VERSION: 3.0 
addressof start is c08f4000 
got cyan buf size_H2S 00000050, size_S2H 00000c80
sm_drv_tell_to_radio,shared_dgb_htos=c08f4000
sm_drv_tell_to_radio,shared_dgb_stoh=c08f4058
Returning Status: [0].
UART InitializedReceived the MAC Address trap
MY INIT Called 
init...
download uses obsolete (PF_INET,SOCK_PACKET)
received link state trap: [108]
bridge: can't decode speed from eth0: 0
device eth0 entered promiscuous mode
received link state trap: [108]
device br0 already exists; can't create bridge with the same name
device eth0 is already a member of a bridge; can't enslave it to bridge br0.
wsc_enalbe=1
SIOCSIFHWADDR: Unknown error 16
killall: rssid: no process killed
killall: wsccmd: no process killed
Simple config inital steps
 led cmd="l1
 wlan_on=1
LAN_MAC:0x0021297c3cc3killall: syslogd: no process killed
killall: paed: no process killed
Start WiFi Protected Setup / Simple Config
/etc/rcS: 135: cannot create /proc/sys/vm/pagetable_cache: Directory nonexistent
killall: igd_upnpd: no process killed
init[178] : find an unknown option,ignor it
init[178] : find an unknown option,ignor it
init[178] : find an unknown option,ignor it
init[178] : find an unknown option,ignor it
init[178] : find an unknown option,ignor it
init[178] : find an unknown option,ignor it
init[178] : find an unknown option,ignor it
init[178] : find an unknown option,ignor it
init[178] : find an unknown option,ignor it
init[178] : find an unknown option,ignor it
init[178] : find an unknown option,ignor it
read root xml mod
new_init_action:action=4

Please press Enter to activate this console.  }}}

== /etc/rcS ==
{{{ 
# cat rcS[J
#!/bin/sh
export PATH=/sbin:/bin:/usr/sbin:/usr/bin:/usr/sbin/scripts

UTC=yes

mount -n -t proc proc /proc
mount -n -t ramfs ramfs /tmp
mount -n -t ramfs ramfs /var

# build var directories 
/bin/mkdir -m 0777 /tmp/var
/bin/mkdir -m 0777 /var/lock
/bin/mkdir -m 0777 /var/log
/bin/mkdir -m 0777 /var/run
/bin/mkdir -m 0777 /var/tmp
/bin/mkdir -m 0777 /tmp/etc
/bin/mkdir -m 0777 /tmp/etc/ppp
/bin/mkdir -m 0755 /etc/dnrd
/bin/mkdir -m 0777 /var/lib
/bin/mkdir -m 0777 /var/cache
/bin/mkdir -m 0777 /var/lib/dhcp-fwd
/bin/mkdir -m 0777 /var/pda
/bin/mkdir -m 0777 /var/etc
/bin/mkdir -m 0777 /var/paed
#/bin/ln -sf /isfs/truepda.bin /var/pda/truepda.bin
/bin/cp /etc/wsc_config.txt /var/paed/wsc_config.txt
/bin/cp -rf /usr/etc/ppp/* /tmp/etc/ppp/
/bin/ln -sf /usr/sbin/setup.cgi /tmp/etc/setup.cgi
/bin/ln -sf /usr/sbin/restore_config.cgi /tmp/etc/restore_config.cgi
/bin/ln -sf /tmp/upgrade_flash.cgi /tmp/etc/upgrade_flash.cgi

/sbin/insmod /lib/modules/led.ko
#/sbin/insmod /lib/modules/push_button.ko
/bin/echo "b1" > /proc/led

#Kenneth
/bin/read-truepda 
#if [ -f /var/pda/truepda.bin ];
#then /bin/ln -sf /isfs/truepda.bin /var/pda/truepda.bin;
#fi;
#Kenneth
if [ ! -e /var/pda/truepda.bin ] ; then
  busybox echo "NO PDA in flash, copying default PDA"
  busybox cp /isfs/pda.bin /var/pda/truepda.bin
fi

# insert modules
#/bin/startbsp
busybox echo " Loading ether driver ..."
busybox insmod /lib/solos_ethernet.ko
busybox echo " Loading Conexant BSP..."
busybox insmod /lib/hsl_mod_gpl.o
busybox sleep 2
busybox insmod /lib/cnxt_fiq.o
busybox sleep 2
busybox insmod /lib/cnxt_drv.o
busybox sleep 2
busybox echo "Aa1" >> /proc/quantum/drv_ctl
#Wireless  Module
busybox echo " Loading Wireless ..."
busybox echo " Reading True PDA ..."
#Kenneth remark begin...
busybox sleep 1
busybox insmod /lib/stun_ahb.ko
busybox sleep 4
setoid wlan0 0x10000002 ssid "SolosW_AP"
setoid wlan0 0xd long 0
#paed &
/sbin/insmod /lib/wlan_wsc.ko
#Kenneth remark end!
#busybox echo "PSa1:AnnexAFastRetrain:Disable" >> /proc/quantum/drv_ctl
#enable Learning mode,otherwise switch will forward all packet to every lan port
/usr/sbin/ethtool -L eth0 Learning enable
#enable sercomm download
/usr/sbin/download
# start services
/usr/sbin/rc_server
/usr/sbin/server_daemon&
sleep 2
/usr/sbin/rc setwmac start
#busybox ifconfig wlan0 up
#busybox ifconfig eth0 up
/bin/brctl addbr br0
/bin/brctl stp br0 no
#/usr/sbin/brctl addif br0 wlan0
/bin/brctl addif br0 eth0
/bin/brctl setfd br0 0

# stamp lan start time
/bin/cp /proc/uptime /tmp/lan_uptime
/bin/cp /usr/sbin/upgrade_flash.cgi /tmp/upgrade_flash.cgi
/bin/cp /usr/sbin/mini_httpd /tmp/mini_httpd

# increase lan interface waiting queue length
/sbin/ifconfig br0 txqueuelen 100

ifconfig lo 127.0.0.1
route add -net 127.0.0.0 netmask 255.255.0.0 lo

/sbin/klogd&
#/usr/sbin/pb_ap&

#/bin/echo "" > /var/first_start_wan

/usr/sbin/rc adsl start
/usr/sbin/rc printk start
/usr/sbin/rc lan start
#/bin/echo f7 > /proc/led 
#Kenneth remark begin...
/usr/sbin/rc wlan start
#Kenneth remark end!
/usr/sbin/lld2 br0 wlan0& 
/usr/sbin/rc syslogd start
/usr/sbin/rc httpd start
/usr/sbin/rc dhcpd start
#/usr/sbin/rc ntp start
# start pb for test, will be removed later
/usr/sbin/server pb start
/usr/sbin/server ntp start
/usr/sbin/rc route start
/usr/sbin/rc ripd start
#/usr/sbin/rc snmp start

#/usr/sbin/crond &
/usr/sbin/server crond start
#/usr/sbin/scfgmgr
/usr/sbin/server scfgmgr start
#/usr/sbin/atm_monitor &
/usr/sbin/server atm_monitor start
#/usr/sbin/cmd_agent_ap
/usr/sbin/server cmd_agent start
#/usr/sbin/wizd&
#/usr/sbin/server wizd start

echo "0 0" > /proc/sys/vm/pagetable_cache
#Add for force IGMP v2
echo "2" > /proc/sys/net/ipv4/conf/all/force_igmp_version
# router
echo 1 > /proc/sys/net/ipv4/ip_forward
# pppox
echo 1 > /proc/sys/net/ipv4/ip_dynaddr

# add more conntrack 
# increase route cache max_size 
echo 4096 > /proc/sys/net/ipv4/route/max_size 

##echo 2048 > /proc/sys/net/ipv4/netfilter/ip_conntrack_max
echo 3072 > /proc/sys/net/ipv4/ip_conntrack_max
# disable log
##echo 0 > /proc/sys/net/ipv4/netfilter/ip_conntrack_tcp_log_invalid

# for debug, should be removed in formal released firmware
echo 0 > /proc/cpu/alignment
# ignore_all not yet used: this should be satisfactory
echo 1 > /proc/sys/net/ipv4/icmp_echo_ignore_broadcasts
# drop spoofed addr: turn this off when rip is on ?
echo 1 > /proc/sys/net/ipv4/conf/default/rp_filter
echo 1 > /proc/sys/net/ipv4/conf/all/rp_filter
# do not honor source route flags
echo 0 > /proc/sys/net/ipv4/conf/default/accept_source_route
echo 0 > /proc/sys/net/ipv4/conf/all/accept_source_route
# this needs proper sampling on av_blog to determine optimal value
# for now just observe softnet_stats to see # time was throttled
# historical value was 300
echo 100 > /proc/sys/net/core/netdev_max_backlog
##echo 60 > /proc/sys/net/ipv4/netfilter/ip_conntrack_udp_timeout
# For voice 
##echo 600 > /proc/sys/net/ipv4/netfilter/ip_conntrack_udp_timeout_stream
#telnetd&
#sleep 3
/usr/sbin/rc printk start 
/usr/sbin/rc upnp start
/bin/cp /proc/uptime /tmp/hnap_devready
#insatll netfilter module for firewall
/sbin/insmod lib/modules/ipt_LOG.ko
/sbin/insmod lib/modules/ipt_DLOG.ko
/sbin/insmod lib/modules/ipt_http_string.ko
/sbin/insmod lib/modules/ipt_multi_match.ko
/sbin/insmod lib/modules/ipt_psd.ko
/sbin/insmod lib/modules/ipt_string.ko
#/sbin/insmod lib/modules/ipt_webstr.ko
/sbin/insmod lib/modules/ipt_stringGET.ko
/sbin/insmod lib/modules/ipt_stringHEAD.ko
/sbin/insmod lib/modules/ipt_stringHOST.ko

#set led status to READY
/bin/echo "b2" > /proc/led

# }}}
