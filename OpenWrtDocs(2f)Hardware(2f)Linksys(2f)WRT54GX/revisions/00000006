'''Linksys WRT54GX'''

There are two versions of the WRT54GX.

'''WRT54GX v1'''
{{{
Bootloader: CFE
CPU: Broadcom BCM4704
CPU Speed: 266 Mhz
Flash size: 4 MB
RAM: 16 MB
Wireless: Airgo mini-PCI
Serial: yes
JTAG: ?
}}}

'''WRT54GX v2'''

{{{
Bootloader: ROME
CPU: Realtek 8651B
CPU Speed: 200 Mhz
Flash size: 8 MB
RAM: 32 MB
Wireless: Airgo mini-PCI
Serial: yes
JTAG: ?
}}}

Serial port (JP1, 38400bps):
{{{
RX   o
TX   o
GND  o
VCC  o

LEDS
}}}

The ROME bootloader seems to want gzip'ed images. Unfortunately, it looks like images produced by the uClinux-dist are not accepted yet. Maybe it just returns the same error message.

Bootlog :

{{{
(c)Copyright Realtek, Inc. 2003
Project ROME LOADER
Version 00.00.18(uClinux) (Apr  1 2005 21:24:55)
LDR version 1.00.03 for identification
[865xB] CPU Clock Rate: 200MHz, Memory Clock Rate: 130MHz
AMD/Fujitsu Standard CFI Query Table v1.3 at 0x0040
Detected flash size: total 8MB.
SDRAM size: 32MB
+TFTP +Auto UART +Bank1:ROM
Here we try to capture the default reset button:  None.

--== Loader Menu ==--
'r' to update run image
'a' to change config
'l' to update loader
'g' to load run image without updating Flash
'o' to update flash with ROM file
's' to test SDRAM memory
't' to test flash memory
'e' to erase flash memory


Loading runtime image ...

Unzip image from address: 0xbe020000

Unexpected end of file

Start runtime image at 80000400.

************************************
Powered by Realtek RTL8651B SoC, rev 1
************************************
SDRAM size: 32MB
CPU revision is: 0000ff00
Init MMU (16 entries)
Primary instruction cache 0kB, linesize 0 bytes.
Primary data cache 0kB, linesize 0 bytes.
Linux version 2.4.26-uc0 (kevin@compile-server) (gcc version 3.3.3) #830 Sat May 28 12:44:50 CST 2005
Determined physical RAM map:
 memory: 02000000 @ 00000000 (usable)
NOFS reserved @ 0x802dabc0
On node 0 totalpages: 8192
zone(0): 8192 pages.
zone(1): 0 pages.
zone(2): 0 pages.
Kernel command line: root=/dev/mtdblock4
IRR(0)=c0000000
Calibrating delay loop... 199.06 BogoMIPS
Memory: 29484k/32768k available (2370k kernel code, 3284k reserved, 108k data, 104k init, 0k highmem)
Dentry cache hash table entries: 4096 (order: 3, 32768 bytes)
Inode cache hash table entries: 2048 (order: 2, 16384 bytes)
Mount cache hash table entries: 512 (order: 0, 4096 bytes)
Buffer cache hash table entries: 1024 (order: 0, 4096 bytes)
Page-cache hash table entries: 8192 (order: 3, 32768 bytes)
Checking for 'wait' instruction...  unavailable.
POSIX conformance testing by UNIFIX
NEW PCI Driver...isLinuxCompliantEndianMode=False(Big Endian)
Found Airgo PCI, function=0!
Memory Space 0 data=0xfffe0000 size=0x20000
Memory Space 1 data=0xfff80000 size=0x80000
PCI device exists: slot 0 function 0 VendorID 17cb DeviceID 1 bbd40000
Found Airgo PCI, function=1!
Found Airgo PCI, function=2!
Found Airgo PCI, function=3!
Found Airgo PCI, function=4!
Found Airgo PCI, function=5!
Found Airgo PCI, function=6!
Found Airgo PCI, function=7!
memory mapping BAnum=0 slot=0 func=0
memory mapping BAnum=1 slot=0 func=0
assign mem base 1bf00000~1bf7ffff at bbd40014 size=524288
assign mem base 1bf80000~1bf9ffff at bbd40010 size=131072
Find Total 1 PCI functions
Found 00:00 [17cb/0001] 000200 00
Linux NET4.0 for Linux 2.4
Based upon Swansea University Computer Society NET3.039
Initializing RT netlink socket
Starting kswapd
devfs: v1.12c (20020818) Richard Gooch (rgooch@atnf.csiro.au)
devfs: boot_options: 0x0
pty: 256 Unix98 ptys configured
Serial driver version 5.05c (2001-07-08) with MANY_PORTS SERIAL_PCI enabled
Probing RTL8651 home gateway controller...
Initialize RTL865x ASIC and driver
   Initialize mbuf...
   creating default 2 interfaces...eth0 IRR(6)=c0040000
===> Request IRQ 6 for eth0, ret=0
eth1 ...OK
PPP generic driver version 2.4.2
PPP BSD Compression module registered
flash device: 7e0000 at be000000
AMD/Fujitsu Standard CFI Query Table v1.3 at 0x0040
 Amd/Fujitsu Extended Query Table v1.3 at 0x0040
number of CFI chips: 1
cfi_cmdset_0002: Disabling fast programming due to code brokenness.
Creating 5 MTD partitions on "Physically mapped flash":
0x00000000-0x00006000 : "boot1"
0x00010000-0x00020000 : "boot2"
0x00000000-0x00800000 : "boot3"
0x00020000-0x00120000 : "kernel"
0x00120000-0x00800000 : "rootfs"
NET4: Linux TCP/IP 1.0 for NET4.0
IP Protocols: ICMP, UDP, TCP, IGMP
IP: routing cache hash table of 512 buckets, 4Kbytes
TCP: Hash tables configured (established 2048 bind 4096)
GRE over IPv4 tunneling driver
ip_conntrack version 2.1 (256 buckets, 2048 max) - 344 bytes per conntrack
ip_conntrack_pptp version $Revision: 1.1.1.1 $ loaded
ip_nat_pptp version $Revision: 1.1.1.1 $ loaded
ip_tables: (C) 2000-2002 Netfilter core team
NET4: Unix domain sockets 1.0/SMP for Linux NET4.0.
VFS: Mounted root (cramfs filesystem) readonly.
Freeing unused kernel memory: 104k freed
Bad boy: serial (at 0x8009d9fc) called us without a dev_id!
IRR(4)=c0c40000
===> Request IRQ 4 for serial, ret=0
Shell invoked to run file: /etc/rc
Command: mount -t proc proc /proc
Command: mount -t ramfs ramfs  /var
Command: mkdir /var/tmp
Command: mkdir /var/ppp/
Command: mkdir /var/log
Command: mkdir /var/run
Command: mkdir /var/lock
Command: mkdir /var/spool
Command: mkdir /var/spool/cron
Command: mkdir /var/spool/cron/crontabs
Command:
Command:
Command: #iwcontrol is required for RTL8185 Wireless driver
Command: #busybox insmod /lib/modules/2.4.26-uc0/kernel/drivers/net/wireless/rtl8185.o
Command: #iwcontrol auth  &
Command:
Command: #busybox insmod /lib/modules/2.4.26-uc0/kernel/drivers/usb/quickcam.o
Command: cd www
Command: /bin/webs start&
[18]
Command: cd /
Command:
Execution Finished, Exiting

Sash command shell (version 1.1.1)
/> System initializing...AMD/Fujitsu Standard CFI Query Table v1.3 at 0x0040

cfgmgr_integrityCheck: ok
cfgmgr_init: romeCfgParam size: 24224(0x5ea0)
cfgmgr_init: pRomeCfgParam addr: 715853824(0x2aab1000)
rtl8651_user_pid set to 18
Bring up ext  port 6..
Rx shift=10002
AMD/Fujitsu Standard CFI Query Table v1.3 at 0x0040
cfg wan to AMD/Fujitsu Standard CFI Query Table v1.3 at 0x0040
dhcp client ...

Set IGMP Default Upstream interface (eth0) ... SUCCESS!!
info, client (v0.9.9-pre) started
dhcpc client deconfig
ifCfgParam[0].ipAddr: 0.0.0.0
ifCfgParam[0].ipMask: 0.0.0.0
ifCfgParam[0].gwAddr: 0.0.0.0
ifCfgParam[0].dnsPrimaryAddr: 0.0.0.0
ifCfgParam[0].dnsSecondaryAddr: 0.0.0.0
ifCfgParam[0].winsPrimaryAddr: 0.0.0.0
ifCfgParam[0].winsSecondaryAddr: 0.0.0.0
rtl8651_delNaptMapping: ret -6
rtl8651_delRoute(default): ret -3
rtl8651_delIpIntf: ret -2710
target 239.0.0.0
SIOCDELRT: No such process
Using /lib/modules/2.4.26-uc0/kernel/drivers/net/led/led.o
PPPoE Passthru disabled.
Drop Unknown PPPoE PADT disabled.
IPv6 Passthru disabled.
Using /lib/modules/2.4.26-uc0/kernel/drivers/net/askey/airgo/ccd.o
Using /lib/modules/2.4.26-uc0/kernel/drivers/net/askey/airgo/wns_mod.o
Using /lib/modules/2.4.26-uc0/kernel/drivers/net/askey/airgo/pol_nosdram.o
debug, Sending discover...
# MAC Monitoring Register = 0x00000000
# Setup System Clock Rate for Watch Dog
plm probe (plm_dump_buf @ C0029100)
&bdh 817F4170 bdh A17E0000
np->hif_regs->bus_slave.hif_ctrl.val 00000000
np->hif_regs->bus_slave.hif_ctrl.val 000000C0
wlan0: PCI Revision = 3, Slot Name[00:00.0], Slot#[0]
wlan0: at BAR0 = 0xbbf80000, BAR1 = 0xbbf00000, IRQ 5.
IRR(5)=c0c40000
===> Request IRQ 5 for wlan0, ret=0
wlan0: request_irq, err = 0
wlan0: plm_reg_init Succeeded
wlan0: MAC:00:13:10:b7:98:c9
wlan0: plm_get_radio_eeprominfo(), err = 0
wlan0: OFFSET of dev->priv[0x6C]
wlan0: OFFSET of np->hif_regs[0x1060]
wlan0: OFFSET of np->stats_mac_td_ring_flush_cnt[0xD40]
wlan0: OFFSET of np->stats_mac_td_cnt[0xD2C]
Register shadow 18
ccd_msg_handler_shadow 18 2 C002A534
debug, Sending discover...
find_pid_by_name(): 0
ssid=linksys
[38]
debug, Sending discover...
[41]
Starting MAC FW module...radioID = 0 NUM_RADIO 1 - param_addr = 0x817f50a8 start at C003B400
[0][1a][3][982] bg = 1, nTx = 1, nRx = 2, cb=0, ap=1, mpci=0
[0][11][3][1] Sending CFG_DNLD_REQ
Reserve port 6 for peripheral device use. (0x40)
Total WLAN/WDS links: 1
[0][11][3][1] CFG size 3252 bytes MAGIC dword is 0xdeaddead
[0][11][3][1] CFG hdr totParams 187 intParams 144 strBufSize 756/1596
[0][10][3][1] CFG RDET MIN PULSE WIDTH = 100
[0][10][3][1] CFG RDET MAX PULSE WIDTH = 100
[0][10][3][1] CFG RDET PULSE WIDTH MARGIN = 4
[0][10][3][1] CFG RDET PULSE TR CNT1 = 3
[0][10][3][1] CFG RDET PULSE TR CNT2 = 3
[0][10][3][1] CFG RDET PULSE TR CNT3 = 5
[0][10][3][1] CFG RDET RSSI TH = 60
[0][10][3][1] CFG RDET MIN IAT = 5000
[0][10][3][1] CFG RDET MAX IAT = 65535
[0][10][3][1] CFG RDET MEAS DEL  = 77
Applied commit-all global setti[0][14][2][11] Cfg param 177 indication not handled
[0][14][2][11] Cfg param 178 indication not handled
[0][10][3][11] CFG RDET FLAG  = 0
ngs
[0][12][2][18] received unexpected SME_STOP_BSS_REQ in state 0, for role 0
[0][12][2][18] eLIM_SME_OFFLINE_STATE
wlan0: Rcvd a eWSM_DRV_RADIO_DISABLE_REQ for radio[0]
Delete port 0 from peripheral port set. (0x40)
Total WLAN/WDS links: 0
mac_mod_exit: Cleaning MAC FW module: radio Id 0
Starting MAC FW module...radioID = 0 NUM_RADIO 1 - param_addr = 0x817f50a8 start at C003B400
[0][1a][3][1052] bg = 1, nTx = 1, nRx = 2, cb=0, ap=1, mpci=0
[0][11][3][1] Sending CFG_DNLD_REQ
Reserve port 6 for peripheral device use. (0x40)
Total WLAN/WDS links: 1
[0][11][3][1] CFG size 3252 bytes MAGIC dword is 0xdeaddead
[0][11][3][1] CFG hdr totParams 187 intParams 144 strBufSize 756/1596
[0][10][3][1] CFG RDET MIN PULSE WIDTH = 100
[0][10][3][1] CFG RDET MAX PULSE WIDTH = 100
[0][10][3][1] CFG RDET PULSE WIDTH MARGIN = 4
[0][10][3][1] CFG RDET PULSE TR CNT1 = 3
[0][10][3][1] CFG RDET PULSE TR CNT2 = 3
[0][10][3][1] CFG RDET PULSE TR CNT3 = 5
[0][10][3][1] CFG RDET RSSI TH = 60
[0][10][3][1] CFG RDET MIN IAT = 5000
[0][10][3][1] CFG RDET MAX IAT = 65535
[0][10][3][1] CFG RDET MEAS DEL  = 77
[0][14][2][9] Cfg param 177 indication not handled
[0][14][2][9] Cfg param 178 indication not handled
[0][10][3][9] CFG RDET FLAG  = 0
info, server (v0.9.9-pre) started
error, max_leases value (254) not sane, setting to 50 instead
error, Unable to open /var/udhcpd.leases for reading
[0][12][3][316] Going to parse numSSID  in the START_BSS_REQ, len=9
}}}
