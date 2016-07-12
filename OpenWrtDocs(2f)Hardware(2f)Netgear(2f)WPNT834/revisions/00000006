== Netgear WPNT834 ==

This is an RTL8651B-based router with an Airgo mini-PCI card, 4Mb flash and 32Mb memory.

== Specs ==

 * SoC: Realtek RTL8651B
 * Flash: 4MB (MX 29LV320ABTC-90G)
 * Memory: 32MB (2x V54C3128164VBI7)
 * Wireless card: Airgo AGN303BB-00 (PCI ID: 17cb:0002)
 * Switch: integrated into SoC
 * 2 integrated antennas, 1 RP-SMA connector
 * Power supply: 12V, 1A

== Serial ==

Settings: 38400, 8N1

{{{

  o   o   o   o              (no voltage)
 VCC  RX  TX GND     J3  o o o o o o o o o o
                         o o o o o o o o o o
                               * GND *
                         (possible JTAG connector)

}}}

== man wpnt834 ==

The firmware supplied by Netgear is rather crappy, though this is associated with the crappy Airgo driver for sure (we're talking about 1.0.34). Strange hickups in the connection, bad performance even with Netgear's own WPNT511 card...

GPL tarball is available at ftp://downloads.netgear.com/files/GPL/wpnt834_1.0_34.tar.gz, pictures of the device and the board at http://trash.uid0.hu/openwrt/wpnt834.

Googleing on 'ROME bootloader' resulted in the homepage of an embedded operating system (http://rome.sf.net), however, its author stated that he has no connection with the bootloader on the WPNT834.

== /boot ==

{{{
Project ROME LOADER
Version 00.00.01 (Jul 29 2005 11:27:06)
Protect:in boot c_entry
go to move.bin
In C_Entry of move.bin 0xBD013000=eab01000
after copy code 
after Decode()
************************************
Powered by Realtek RTL8651B SoC, rev 1
************************************
SDRAM size: 32MB
CPU revision is: 0000ff00
Init MMU (16 entries)
Primary instruction cache 0kB, linesize 0 bytes.
Primary data cache 0kB, linesize 0 bytes.
Linux version 2.4.26-uc0 (root@localhost.localdomain) (gcc version 3.2) #3 Mon N
ov 14 19:10:17 CST 2005
Determined physical RAM map:
 memory: 02000000 @ 00000000 (usable)
NOFS reserved @ 0x802e1e90
On node 0 totalpages: 8192
zone(0): 8192 pages.
zone(1): 0 pages.
zone(2): 0 pages.
Kernel command line: root=/dev/mtdblock4
IRR(0)=c0000000
Calibrating delay loop... 178.99 BogoMIPS
Memory: 29456k/32768k available (2077k kernel code, 3312k reserved, 100k data, 9
2k init, 0k highmem)
Dentry cache hash table entries: 4096 (order: 3, 32768 bytes)
Inode cache hash table entries: 2048 (order: 2, 16384 bytes)
Mount cache hash table entries: 512 (order: 0, 4096 bytes)
Buffer cache hash table entries: 1024 (order: 0, 4096 bytes)
Page-cache hash table entries: 8192 (order: 3, 32768 bytes)
Checking for 'wait' instruction...  unavailable.
POSIX conformance testing by UNIFIX
NEW PCI Driver...isLinuxCompliantEndianMode=False(Big Endian)
[PCI] Reset Bridge ..... Finish!
Memory Space 0 data=0xfffe0000 size=0x20000
Memory Space 1 data=0xfff80000 size=0x80000
PCI device exists: slot 0 function 0 VendorID 17cb DeviceID 2 bbd40000
memory mapping BAnum=0 slot=0 func=0
memory mapping BAnum=1 slot=0 func=0
assign mem base 1bf00000~1bf7ffff at bbd40014 size=524288
assign mem base 1bf80000~1bf9ffff at bbd40010 size=131072
Find Total 1 PCI functions
Found 00:00 [17cb/0002] 000200 00
Linux NET4.0 for Linux 2.4
Based upon Swansea University Computer Society NET3.039
Initializing RT netlink socket
Starting kswapd
Squashfs 2.1-r2 (released 2004/12/15) (C) 2002-2004 Phillip Lougher
pty: 256 Unix98 ptys configured
Serial driver version 5.05c (2001-07-08) with MANY_PORTS SERIAL_PCI enabled
Probing RTL8651 home gateway controller...
chip name: 8651B, chip revid: 1
===> Request IRQ 6 for eth0, ret=0
PPP generic driver version 2.4.2
PPP BSD Compression module registered
flash device: 3c0000 at be000000
 Amd/Fujitsu Extended Query Table v1.1 at 0x0040
number of CFI chips: 1
cfi_cmdset_0002: Disabling fast programming due to code brokenness.
Creating 5 MTD partitions on "Physically mapped flash":
0x00000000-0x0000ffb0 : "boot1"
0x00008000-0x00010000 : "boot2"
0x00010000-0x00020000 : "boot3"
0x00040000-0x00140000 : "kernel"
0x00140000-0x00400000 : "rootfs"
NET4: Linux TCP/IP 1.0 for NET4.0
IP Protocols: ICMP, UDP, TCP, IGMP
IP: routing cache hash table of 512 buckets, 4Kbytes
TCP: Hash tables configured (established 2048 bind 4096)
GRE over IPv4 tunneling driver
NET4: Unix domain sockets 1.0/SMP for Linux NET4.0.
emulate opcode 0x25 at 800f3b54 
VFS: Mounted root (squashfs filesystem) readonly.
Freeing unused kernel memory: 92k freed
emulate opcode 0x25 at 800f3b54 
IRR(4)=c0c40000
===> Request IRQ 4 for serial, ret=0
cp: /etc/airgo/wsmChlListDefaults: No such file or directory
cp: /etc/upnp_xml/ipcfg.xml: No such file or directory
cp: /etc/upnp_xml/gateway.mod: No such file or directory
cp: /etc/upnp_xml/cmnicfg.xml: No such file or directory
cp: /etc/upnp_xml/osinfo.xml: No such file or directory
Using ccd
Warning: loading ccd will taint the kernel: no license
  See http://www.tux.org/lkml/#export-tainted for information about tainted modu
les
cfgmgr init rst:0LoadsercCfgFile: LoadsercCfgFile.filelen=3345
Using wns_mod
Warning: loading wns_mod will taint the kernel: no license
  See http://www.tux.org/lkml/#export-tainted for information about tainted modu
les
LoadsercCfgFile: LoadsercCfgFile.filelen=0
Using pol_nosdram.o
rtl8651_user_pid set to 19
Warning: loading pol_nosdram will taint the kernel: no license
  See http://www.tux.org/lkml/#export-tainted for information about tainted modu
les

Set IGMP Default Upstream interface (eth0) ... SUCCESS!!
info, client (v0.9.9-pre) started
CPU: LX5280@ 1798889 cycles/jiffies
plm probe (plm_dump_buf @ C001F060)
np->hif_regs->bus_slave.hif_ctrl.val 00000000
np->hif_regs->bus_slave.hif_ctrl.val 000000C0
wlan0: PCI Revision = 1, Slot Name[00:00.0], Slot#[0]
wlan0: at BAR0 = 0xbbf80000, BAR1 = 0xbbf00000, IRQ 5.
IRR(5)=c0c40000
===> Request IRQ 5 for wlan0, ret=0
Register shadow 18
ccd_msg_handler_shadow 18 2 C00204C0
PPPoE Passthru disabled.
Drop Unknown PPPoE PADT disabled.
IPv6 Passthru disabled.
IPX Passthru disabled.
NETBIOS Passthru disabled.
target 239.0.0.0
SIOCDELRT: No such process
killall: routed: no process killed
cfgmgr init rst:0Result code 48: Failed to send request to radio mgt module(WSM)


BusyBox v1.00-pre2 (2005.11.14-09:56+0000) Built-in shell (msh)
Enter 'help' for a list of built-in commands.

# halPhyGetChanelListWithPower: dev_ind->numChan = 13
Starting MAC FW module...radioID = 0 NUM_RADIO 1 - param_addr = 0x813f72f4 start
 at C0030C10
Register External Device (wlan0) vid (9) extPortNum (6)
Reserve port 6 for peripheral device use. (0x40)
Total WLAN/WDS links: 1
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
[0][10][3][1] initFixedState : STA 0
[0][10][3][1] Setting #TX to 2 temporarily
[0][10][2][1] limresumeactivityntf is sent from hal
[0][10][2][1] halProcessStartEvent: Completed HAL/CFG/HAL init; State 3!
[0][10][2][1] halProcessStartEvent: Done:- Hal State 3
[0][12][2][1] Received RESUME_NTF in State 2 on Role 0
[0][12][3][1] The TITAN related global CFG's are: ccMode - 0 ccBitmap - 0, cpMod
e - 0 cpBitmap - 0, cbMode - 0 cbState - 0, rfcsState - 0
[0][12][3][1] The TITAN related global CFG's are: ccMode - 0 ccBitmap - 0, cpMod
e - 0 cpBitmap - 0, cbMode - 0 cbState - 0, rfcsState - 0
[0][12][3][1] The TITAN related global CFG's are: ccMode - 0 ccBitmap - 0, cpMod
e - 0 cpBitmap - 0, cbMode - 0 cbState - 0, rfcsState - 0
[0][12][3][1] The TITAN related global CFG's are: ccMode - 0 ccBitmap - 0, cpMod
e - 0 cpBitmap - 0, cbMode - 0 cbState - 0, rfcsState - 0
[0][12][3][1] The TITAN related global CFG's are: ccMode - 0 ccBitmap - 0, cpMod
e - 0 cpBitmap - 0, cbMode - 0 cbState - 0, rfcsState - 0
[0][12][3][1] The TITAN related global CFG's are: ccMode - 0 ccBitmap - 0, cpMod
e - 0 cpBitmap - 0, cbMode - 0 cbState - 0, rfcsState - 0
halPhyGetChanelListWithPower: dev_ind->numChan = 13
Applied reset-to-defaults
Apply commit-all global settings to take effect
[0][14][2][20] Cfg param 190 indication not handled
[0][14][2][20] Cfg param 191 indication not handled
[0][12][3][20] The TITAN related global CFG's are: ccMode - 1 ccBitmap - 255, cp
Mode - 0 cpBitmap - 0, cbMode - 0 cbState - 0, rfcsState - 0
[0][12][3][20] The TITAN related global CFG's are: ccMode - 1 ccBitmap - 255, cp
Mode - 0 cpBitmap - 0, cbMode - 0 cbState - 0, rfcsState - 0
[0][12][3][20] The TITAN related global CFG's are: ccMode - 1 ccBitmap - 255, cp
Mode - 0 cpBitmap - 0, cbMode - 1 cbState - 3, rfcsState - 0
[0][12][3][20] The TITAN related global CFG's are: ccMode - 1 ccBitmap - 255, cp
Mode - 0 cpBitmap - 0, cbMode - 1 cbState - 3, rfcsState - 0
[0][14][2][20] Cfg param 49 indication not handled
[0][12][3][25] Going to parse numSSID  in the START_BSS_REQ, len=9
[0][10][3][25] initFixedState : STA 1
[0][10][3][25] halUpdateConfig: set Proximity = 0
WSM radio 0 reset completed.
Applied commit-all globaWSM radio 0 reset started.
l se[0][12][3][150] RECEIVED STOP_BSS_REQ with reason code=0
[0][12][3][150] Triggering RESET_REQ
[0][10][2][150] halSysResetReq: Reason Code = 0x7
ttings
IRR(5)=c0c40000
Delete port 0 from peripheral port set. (0x40)
Unregister Extension device with LinkID 1 -- (wlan0)
Total WLAN/WDS links: 0
IRR(5)=c0c40000
halPhyGetChanelListWithPower: dev_ind->numChan = 13
mac_mod_exit: Cleaning MAC FW module: radio Id 0
Starting MAC FW module...radioID = 0 NUM_RADIO 1 - param_addr = 0x813f72f4 start
 at C0030C10
Register External Device (wlan0) vid (9) extPortNum (6)
Reserve port 6 for peripheral device use. (0x40)
Total WLAN/WDS links: 1
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
[0][10][3][1] initFixedState : STA 0
[0][10][3][1] Setting #TX to 2 temporarily
[0][10][2][1] limresumeactivityntf is sent from hal
[0][10][2][1] halProcessStartEvent: Completed HAL/CFG/HAL init; State 3!
[0][10][2][1] halProcessStartEvent: Done:- Hal State 3
[0][12][2][1] Received RESUME_NTF in State 2 on Role 0
[0][12][3][1] The TITAN related global CFG's are: ccMode - 0 ccBitmap - 0, cpMod
e - 0 cpBitmap - 0, cbMode - 0 cbState - 0, rfcsState - 0
[0][12][3][1] The TITAN related global CFG's are: ccMode - 0 ccBitmap - 0, cpMod
e - 0 cpBitmap - 0, cbMode - 0 cbState - 0, rfcsState - 0
[0][12][3][1] The TITAN related global CFG's are: ccMode - 0 ccBitmap - 0, cpMod
e - 0 cpBitmap - 0, cbMode - 0 cbState - 0, rfcsState - 0
[0][12][3][1] The TITAN related global CFG's are: ccMode - 0 ccBitmap - 0, cpMod
e - 0 cpBitmap - 0, cbMode - 0 cbState - 0, rfcsState - 0
[0][12][3][1] The TITAN related global CFG's are: ccMode - 0 ccBitmap - 0, cpMod
e - 0 cpBitmap - 0, cbMode - 0 cbState - 0, rfcsState - 0
[0][12][3][1] The TITAN related global CFG's are: ccMode - 0 ccBitmap - 0, cpMod
e - 0 cpBitmap - 0, cbMode - 0 cbState - 0, rfcsState - 0
halPhyGetChanelListWithPower: dev_ind->numChan = 13
[0][14][2][14] Cfg param 190 indication not handled
[0][14][2][14] Cfg param 191 indication not handled
[0][12][3][14] The TITAN related global CFG's are: ccMode - 1 ccBitmap - 255, cp
Mode - 0 cpBitmap - 0, cbMode - 0 cbState - 0, rfcsState - 0
[0][12][3][14] The TITAN related global CFG's are: ccMode - 1 ccBitmap - 255, cp
Mode - 0 cpBitmap - 0, cbMode - 0 cbState - 0, rfcsState - 0
[0][12][3][14] The TITAN related global CFG's are: ccMode - 1 ccBitmap - 255, cp
Mode - 0 cpBitmap - 0, cbMode - 1 cbState - 3, rfcsState - 0
[0][12][3][14] The TITAN related global CFG's are: ccMode - 1 ccBitmap - 255, cp
Mode - 0 cpBitmap - 0, cbMode - 1 cbState - 3, rfcsState - 0
[0][14][2][14] Cfg param 49 indication not handled
[0][12][3][50] Going to parse numSSID  in the START_BSS_REQ, len=9
[0][10][3][50] initFixedState : STA 1
[0][10][3][50] halUpdateConfig: set Proximity = 0
WSM radio 0 reset completed.
WSM radio 0 reset started.
[0][12][3][156] RECEIVED STOP_BSS_REQ with reason code=911
[0][12][3][156] Triggering RESET_REQ
[0][10][2][156] halSysResetReq: Reason Code = 0x7
Applied commit-all global settings
IRR(5)=c0c40000
Delete port 0 from peripheral port set. (0x40)
Unregister Extension device with LinkID 1 -- (wlan0)
Total WLAN/WDS links: 0
IRR(5)=c0c40000
halPhyGetChanelListWithPower: dev_ind->numChan = 13
mac_mod_exit: Cleaning MAC FW module: radio Id 0
Starting MAC FW module...radioID = 0 NUM_RADIO 1 - param_addr = 0x813f72f4 start
 at C0030C10
Register External Device (wlan0) vid (9) extPortNum (6)
Reserve port 6 for peripheral device use. (0x40)
Total WLAN/WDS links: 1
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
[0][10][3][1] initFixedState : STA 0
[0][10][3][1] Setting #TX to 2 temporarily
[0][10][2][1] limresumeactivityntf is sent from hal
[0][10][2][1] halProcessStartEvent: Completed HAL/CFG/HAL init; State 3!
[0][10][2][1] halProcessStartEvent: Done:- Hal State 3
[0][12][2][1] Received RESUME_NTF in State 2 on Role 0
[0][12][3][1] The TITAN related global CFG's are: ccMode - 0 ccBitmap - 0, cpMod
e - 0 cpBitmap - 0, cbMode - 0 cbState - 0, rfcsState - 0
[0][12][3][1] The TITAN related global CFG's are: ccMode - 0 ccBitmap - 0, cpMod
e - 0 cpBitmap - 0, cbMode - 0 cbState - 0, rfcsState - 0
[0][12][3][1] The TITAN related global CFG's are: ccMode - 0 ccBitmap - 0, cpMod
e - 0 cpBitmap - 0, cbMode - 0 cbState - 0, rfcsState - 0
[0][12][3][1] The TITAN related global CFG's are: ccMode - 0 ccBitmap - 0, cpMod
e - 0 cpBitmap - 0, cbMode - 0 cbState - 0, rfcsState - 0
[0][12][3][1] The TITAN related global CFG's are: ccMode - 0 ccBitmap - 0, cpMod
e - 0 cpBitmap - 0, cbMode - 0 cbState - 0, rfcsState - 0
[0][12][3][1] The TITAN related global CFG's are: ccMode - 0 ccBitmap - 0, cpMod
e - 0 cpBitmap - 0, cbMode - 0 cbState - 0, rfcsState - 0
WSM radio 0 reset started.
[0][12][2][1] received unexpected SME_STOP_BSS_REQ in state 0, for role 0
[0][12][2][1] eLIM_SME_OFFLINE_STATE
IRR(5)=c0c40000
mac_mod_exit: Cleaning MAC FW module: radio Id 0
halPhyGetChanelListWithPower: dev_ind->numChan = 13
Starting MAC FW module...radioID = 0 NUM_RADIO 1 - param_addr = 0x813f72f4 start
 at C0030C10
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
[0][10][3][1] initFixedState : STA 0
[0][10][3][1] Setting #TX to 2 temporarily
[0][10][2][1] limresumeactivityntf is sent from hal
[0][10][2][1] halProcessStartEvent: Completed HAL/CFG/HAL init; State 3!
[0][10][2][1] halProcessStartEvent: Done:- Hal State 3
[0][12][2][1] Received RESUME_NTF in State 2 on Role 0
[0][12][3][1] The TITAN related global CFG's are: ccMode - 0 ccBitmap - 0, cpMod
e - 0 cpBitmap - 0, cbMode - 0 cbState - 0, rfcsState - 0
[0][12][3][1] The TITAN related global CFG's are: ccMode - 0 ccBitmap - 0, cpMod
e - 0 cpBitmap - 0, cbMode - 0 cbState - 0, rfcsState - 0
[0][12][3][1] The TITAN related global CFG's are: ccMode - 0 ccBitmap - 0, cpMod
e - 0 cpBitmap - 0, cbMode - 0 cbState - 0, rfcsState - 0
[0][12][3][1] The TITAN related global CFG's are: ccMode - 0 ccBitmap - 0, cpMod
e - 0 cpBitmap - 0, cbMode - 0 cbState - 0, rfcsState - 0
[0][12][3][1] The TITAN related global CFG's are: ccMode - 0 ccBitmap - 0, cpMod
e - 0 cpBitmap - 0, cbMode - 0 cbState - 0, rfcsState - 0
[0][12][3][1] The TITAN related global CFG's are: ccMode - 0 ccBitmap - 0, cpMod
e - 0 cpBitmap - 0, cbMode - 0 cbState - 0, rfcsState - 0
halPhyGetChanelListWithPower: dev_ind->numChan = 13
[0][14][2][13] Cfg param 190 indication not handled
[0][14][2][13] Cfg param 191 indication not handled
[0][12][3][13] The TITAN related global CFG's are: ccMode - 1 ccBitmap - 255, cp
Mode - 0 cpBitmap - 0, cbMode - 0 cbState - 0, rfcsState - 0
[0][12][3][13] The TITAN related global CFG's are: ccMode - 1 ccBitmap - 255, cp
Mode - 0 cpBitmap - 0, cbMode - 0 cbState - 0, rfcsState - 0
[0][12][3][13] The TITAN related global CFG's are: ccMode - 1 ccBitmap - 255, cp
Mode - 0 cpBitmap - 0, cbMode - 1 cbState - 3, rfcsState - 0
[0][12][3][13] The TITAN related global CFG's are: ccMode - 1 ccBitmap - 255, cp
Mode - 0 cpBitmap - 0, cbMode - 1 cbState - 3, rfcsState - 0
[0][14][2][13] Cfg param 49 indication not handled
[0][12][3][49] Going to parse numSSID  in the START_BSS_REQ, len=9
[0][10][3][49] initFixedState : STA 1
[0][10][3][49] halUpdateConfig: set Proximity = 0
WSM radio 0 reset completed.

}}}

== Porting OpenWrt ==

The stock firmware seems to be uClinux based, which makes it hard to use as a base for OpenWrt.
See http://forum.openwrt.org/viewtopic.php?id=4001&p=2 for more information.
