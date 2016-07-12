= General Information =
The Speedport W500V is a Broadband Router with integrated DSL Modem, WLan Module and ISDN + Analog PBX capability for VoIP. Manufactured by Hitachi High Technologies and OEM'ed primarily through the T-Com in germany.

The device is also sold by Lidl under the name Targa WR 500 VoIP.

What makes the Speedport W500V a quite atttractive device is the PBX part. It can route incoming calls from either landline and VoIP onto the connected analog phones. Comparable to what the AVM FritzBox FON Routers can do. For outgoing rules can be set to either route the call into landline or over a VoIP SIP Provider.

= Hardware =
'''1) Connections '''
||||<style="text-align: center;">'''Connection Types''' ||
||Amount ||Type ||
||1 ||WAN ||
||1 ||LAN ||
||1 ||Landline Phone ||
||2 ||TAE ||


'''2) LEDs'''
||||<style="text-align: center;">'''Power''' ||
||off ||device is of ||
||green ||device is ready ||
||red ||error during bootup / selftest ||
||||<style="text-align: center;">'''DSL''' ||
||off ||device is off ||
||green (static) ||synchronised with DSLAM ||
||green (blinking) ||synchronising with DSLAM ||
||red ||connection error / not synchronished with DSLAM ||
||||<style="text-align: center;">'''Online''' ||
||off ||no connection established ||
||orange (static) ||PPPoE connection to ISP established ||
||||<style="text-align: center;">'''WLAN''' ||
||off ||WLAN deactivated ||
||green (static) ||WLAN active ||
||green (blinking) ||sending/receiving data ||
||||<style="text-align: center;">'''LAN''' ||
||off ||no active LAN device connected ||
||green (static) ||WLAN active ||
||green (blinking) ||sending/receiving data ||
||||<style="text-align: center;">'''Landline''' ||
||off ||no active phone call over landline ||
||orange ||active phone call over landline ||
||||<style="text-align: center;">'''Internet / VoIP''' ||
||off ||no active phone call over landline ||
||orange ||active phone call over landline ||


'''3) Power Supply'''

Uses a 16V DC, 900mA PSU

'''4) Hardware Specs '''

::: still collecting data :::

'''5) Serial '''

Possible Serial connection at two different points.

'''6) JTAG'''

No research done into JTAG yet. To recover this device from a bad firmware flash or similar JTAG is unnecessary as the device comes with a tiny secondary firmware (safe mode) that can be used for recovery. To get into safe mode simply hold the reset button for at least 8 seconds while turning on the powerswitch. After about 8 seconds the powerled will turn red and a webinterface is available on [http://192.168.1.1 192.168.1.1]. Follow the instructions listed there to flash a working firmware.

'''7) Pictures'''

This is a picture of the top side view of the board. As you can see there is a populated 4 pin connection under the daughter board. This is serial (see below for details).

http://blueflubberball.de/SpeedPort_W500V/DSCF2177.JPG

The layout of the serial connection is pointed out on the next picture:

http://home.arcor.de/irc-stuff/pics/serial_mod.jpg

Look[http://www.wehavemorefun.de/fritzbox/Serielle_Konsole here], on how to build an appropriate serial cable (unfortunately german only, but this device is sold mostly in Germany anyway). Remember: the Pinout on the linked page is a little different (Rx and Tx are switched). They have some nice ideas how to recycle old mobile phone cables. Login via serial does not work by default. Probably this is because ttyS0 (the serial device) is not mentioned in /etc/securetty). Appropriate settings for terminal programs are: 115200, 8n1.

= System Information =
'''1) cat /proc/version'''

{{{
Linux version 2.6.8.1 (root@colinux) (gcc version 3.4.2) #1 Thu Nov 9 07:52:55 EST 2006
}}}
'''2) cat /proc/cpuinfo'''

{{{
system type             : 96348GW
processor               : 0
cpu model               : BCM6348 V0.7
BogoMIPS                : 253.44
wait instruction        : no
microsecond timers      : yes
tlb_entries             : 32
extra interrupt vector  : yes
hardware watchpoint     : no
VCED exceptions         : not available
VCEI exceptions         : not available}}}
'''3) cat /proc/meminfo'''

{{{
MemTotal:        14240 kB
MemFree:           720 kB
Buffers:           452 kB
Cached:           5560 kB
SwapCached:          0 kB
Active:           5312 kB
Inactive:         2528 kB
HighTotal:           0 kB
HighFree:            0 kB
LowTotal:        14240 kB
LowFree:           720 kB
SwapTotal:           0 kB
SwapFree:            0 kB
Dirty:               0 kB
Writeback:           0 kB
Mapped:           4924 kB
Slab:             2448 kB
Committed_AS:     5220 kB
PageTables:        280 kB
VmallocTotal:  1048560 kB
VmallocUsed:      2428 kB
VmallocChunk:  1044824 kB
}}}
'''4) cat /proc/iomem'''

{{{
00000000-00f9ffff : System RAM
  00010000-0014dcc3 : Kernel code
  0014dcc4-0017f0bf : Kernel data
08000000-08ffffff : bcm96348 pci memory space
  08000000-0800ffff : 0000:00:01.0
}}}
'''5) cat /proc/interrupts'''

{{{
           CPU0
  5:         30            MIPS  brcm_5
  7:     738711            MIPS  timer
 10:          0            MIPS  brcm_10
 12:       2995            MIPS  brcm_12
 13:          0            MIPS  brcm_13
 28:       2012            MIPS  brcm_28
 32:      14901            MIPS  brcm_32
ERR:          0
}}}
'''6) cat /proc/modules'''

{{{
ipt_state 544 1 - Live 0xc00a0000
ipt_mark 416 0 - Live 0xc009e000
ipt_limit 896 5 - Live 0xc009c000
ipt_TCPMSS 2240 2 - Live 0xc0096000
ipt_REDIRECT 768 0 - Live 0xc0098000
ipt_MASQUERADE 1504 1 - Live 0xc0092000
ipt_MARK 704 0 - Live 0xc0094000
ipt_LOG 4064 10 - Live 0xc008d000
ip_traffic 1840 0 - Live 0xc0090000
ip_queue 5632 0 - Live 0xc003a000
ip_nat_tftp 1888 0 - Live 0xc008b000
ip_nat_pptp 1824 0 - Live 0xc0089000
ip_nat_irc 2304 0 - Live 0xc0087000
ip_nat_h323 2112 0 - Live 0xc0085000
ip_nat_gre 1408 0 - Live 0xc0083000
ip_nat_ftp 2944 0 - Live 0xc0081000
ip_conntrack_tftp 1824 0 - Live 0xc007f000
ip_conntrack_pptp 2416 0 - Live 0xc007d000
ip_conntrack_irc 68864 1 ip_nat_irc, Live 0xc006b000
ip_conntrack_h323 2256 0 - Live 0xc004b000
ip_conntrack_gre 1968 2 ip_nat_pptp,ip_conntrack_pptp, Live 0xc0049000
ip_conntrack_ftp 20576 1 ip_nat_ftp, Live 0xc0042000
iptable_mangle 960 0 - Live 0xc0006000
iptable_nat 15184 9 ipt_REDIRECT,ipt_MASQUERADE,ip_nat_tftp,ip_nat_pptp,ip_nat_irc,ip_nat_h323,ip_nat_gre,ip_nat_ftp, Live 0xc003d000
ip_conntrack 24720 16 ipt_state,ipt_REDIRECT,ipt_MASQUERADE,ip_traffic,ip_nat_tftp,ip_nat_pptp,ip_nat_irc,ip_nat_h323,ip_nat_ftp,
ip_conntrack_tftp,ip_conntrack_pptp,ip_conntrack_irc,ip_conntrack_h323,ip_conntrack_gre,ip_conntrack_ftp,
iptable_nat, Live 0xc0012000
iptable_filter 928 1 - Live 0xc0010000
ip_tables 13984 11 ipt_state,ipt_mark,ipt_limit,ipt_TCPMSS,ipt_REDIRECT,ipt_MASQUERADE,ipt_MARK,ipt_LOG,iptable_mangle,
iptable_nat,iptable_filter, Live 0xc002d000
endpointdd 1265472 0 - Live 0xc0270000
wl 522288 0 - Live 0xc0115000
bcm_enet 18192 0 - Live 0xc0027000
bcmprocfs 13872 2 ip_traffic,ip_conntrack, Live 0xc000b000
adsldd 114592 0 - Live 0xc004e000
blaadd 5872 0 - Live 0xc0008000
atmapi 47504 2 adsldd,blaadd, Live 0xc001a000
}}}
'''7) cat /proc/devices'''

{{{
Character devices:
  1 mem
  2 pty
  3 ttyp
  4 ttyS
  5 /dev/tty
  5 /dev/console
 10 misc
108 ppp
205 atmapi
206 bcrmboard
208 adsl
209 endpoint
212 bcm
Block devices:
 31 mtdblock
}}}
'''8) cat /proc/pci'''

{{{
cat: /proc/pci: No such file or directory
}}}
'''9) dmesg'''

{{{
dmesg
Linux version 2.6.8.1 (root@colinux) (gcc version 3.4.2) #1 Thu Nov 9 07:52:55 EST 2006
Total Flash size: 4096K with 71 sectors
96348GW prom init
CPU revision is: 00029107
mpi: No Card is in the PCMCIA slot
Determined physical RAM map:
 memory: 00fa0000 @ 00000000 (usable)
On node 0 totalpages: 4000
  DMA zone: 4000 pages, LIFO batch:1
  Normal zone: 0 pages, LIFO batch:1
  HighMem zone: 0 pages, LIFO batch:1
Built 1 zonelists
Kernel command line: root=31:0 ro noinitrd
brcm mips: enabling icache and dcache...
Primary instruction cache 16kB, physically tagged, 2-way, linesize 16 bytes.
Primary data cache 8kB 2-way, linesize 16 bytes.
PID hash table entries: 64 (order 6: 512 bytes)
Using 128.000 MHz high precision timer.
Dentry cache hash table entries: 4096 (order: 2, 16384 bytes)
Inode-cache hash table entries: 2048 (order: 1, 8192 bytes)
Memory: 14148k/16000k available (1271k kernel code, 1832k reserved, 196k data, 72k init, 0k highmem)
Calibrating delay loop... 253.44 BogoMIPS
Mount-cache hash table entries: 512 (order: 0, 4096 bytes)
Checking for 'wait' instruction...  unavailable.
NET: Registered protocol family 16
Can't analyze prologue code at 8014c4fc
PPP generic driver version 2.4.2
NET: Registered protocol family 24
Using noop io scheduler
bcm963xx_mtd driver v1.0
brcmboard: brcm_board_init entry
bcm963xx_serial driver v2.0
NET: Registered protocol family 2
IP: routing cache hash table of 512 buckets, 4Kbytes
TCP: Hash tables configured (established 512 bind 1024)
NET: Registered protocol family 1
NET: Registered protocol family 17
Ebtables v2.0 registered
NET: Registered protocol family 8
NET: Registered protocol family 20
VFS: Mounted root (squashfs filesystem) readonly.
Freeing unused kernel memory: 72k freed
Algorithmics/MIPS FPU Emulator v1.5
atmapi: module license 'Proprietary' taints kernel.
blaadd: blaa_detect entry
adsl: adsl_init entry
Broadcom BCMPROCFS v1.0 initialized
Broadcom BCM6348A2 Ethernet Network Device v0.3 May 30 2006 11:50:04
Config Internal PHY Through MDIO
BCM63xx_ENET: 100 MB Full-Duplex (auto-neg)
eth0: MAC Address: 00:16:38:6A:96:C0
PCI: Setting latency timer of device 0000:00:01.0 to 64
PCI: Enabling device 0000:00:01.0 (0004 -> 0006)
wl: srom not detected, using main memory mapped srom info (wombo board)
wl0: wlc_attach: using main board MAC address base in NVRAM (wombo board)
wl0 MAC Address: 00:16:38:6A:96:C1
wl0: Broadcom BCM4318 802.11 Wireless Controller 3.131.35.0.cpe0.1dt
Endpoint: endpoint_init entry
BOS: Enter bosInit
BOS: Enter bosAppInit
BOS: Exit bosAppInit
BOS: Exit bosInit
Endpoint: endpoint_init COMPLETED
BcmAdsl_Initialize=0xC004F2A8, g_pFnNotifyCallback=0xC0062414
AdslCoreHwReset: AdslOemDataAddr = 0xA0FED8E0
ip_tables: (C) 2000-2002 Netfilter core team
ip_conntrack version 2.1 (125 buckets, 0 max) - 368 bytes per conntrack
device eth0 entered promiscuous mode
br0: port 1(eth0) entering learning state
br0: topology change detected, propagating
br0: port 1(eth0) entering forwarding state
eth0 Link UP.
device wl0 entered promiscuous mode
br0: port 2(wl0) entering learning state
br0: topology change detected, propagating
br0: port 2(wl0) entering forwarding state
device nas_1_32 entered promiscuous mode
br0: port 3(nas_1_32) entering learning state
br0: topology change detected, propagating
br0: port 3(nas_1_32) entering forwarding state
kernel::endpoint_open
kernel::endpoint_open COMPLETED
BOS: Enter bosStartApp
BOS: bosAppRootTask() - Is it morning already? Spawning app task (epoch #0)...
BOS: Enter TaskCreate aoAP
BOS: TaskCreate - spawn new task aoAP
bcmOsTaskCreate:
 TASK NAME      = aoAP
 TASK_PRIORITY  = 1
BOS: Exit TaskCreate
BOS: AppResetDetectionEnable() - Enabled reset detection.
bcmOsTaskCreate:
 TASK NAME      = aoRT
 TASK_PRIORITY  = 1
BOS: Exit bosStartApp
Reseting the 3341
voipResetGpio = 6
PASS: mmr
PASS: chipCtl
PASS: mspi
PASS: scratchSram
PASS: apmregs
PASS: apm0
PASS: apm1
PASS: hvg
PASS: slic
PASS: vpm
PASS: mbox
3341 diagnostics passed!
Reseting the 3341
voipResetGpio = 6
Initializing 3341 drivers
-------------- TDM DMA setup strt --------------
SAMPLESIZE = 8
DESCRIPTORP = 0xb7fe6300 INGRESSP = 0xb7fe6310 EGRESSP = 0xb7fe6330
Initializing Memory: 8 (16-bit locations)
Priming TX FIFO....
Completed TDM3341 init!!!!
MSPI driver init SUCCESSFUL
MSPI driver registers update SUCCESSFUL
BOARDHAL Enabling relays
Loading 3341 Zsp with Hausware app.
Loading 3341 overlay to 0xb7fc0000.
Verifying overlay...
Done verifying overlay.
BOS: Enter TaskCreate 3341_ASSERT_IST
BOS: TaskCreate - spawn new task 3341_ASSERT_IST
bcmOsTaskCreate:
 TASK NAME      = 3341_ASSERT_IST
 TASK_PRIORITY  = 1
BOS: Exit TaskCreate
DSP Handshake.  Hausware ZSP app initialized properly.
bosMsgQCreate: Created message queue VRGEVQ at address 0x0
BOS: Enter TaskCreate VRGEVPR
BOS: TaskCreate - spawn new task VRGEVPR
bcmOsTaskCreate:
 TASK NAME      = VRGEVPR
 TASK_PRIORITY  = 1
BOS: Exit TaskCreate
BOS: Enter TaskCreate HCAS
BOS: TaskCreate - spawn new task HCAS
bcmOsTaskCreate:
 TASK NAME      = HCAS
 TASK_PRIORITY  = 1
BOS: Exit TaskCreate
ENDPT: Creating hausware task
BOS: Enter TaskCreate HTSK
BOS: TaskCreate - spawn new task HTSK
bcmOsTaskCreate:
 TASK NAME      = HTSK
 TASK_PRIORITY  = 1
BOS: Exit TaskCreate
DAA DBG: MSPI Hdl = 0x500
DAA DBG: GPIO Hdl = 0xb
     DAA DBG: Successful READ!!!! count = 0
 DAA DBG: ISOCAP lock count = 0
Si3050 SLAC Initialised, Line side device = Si: 3019 (0x3)
System dev rev: 0x4, Line dev rev: 0x3
Line dev status: FDT:0x1, LCS: 0x0
DAA Device Init completed
DAA init successful
ENDPT: 'HAPI_RM_OPEN_VHD_EVT' (0x80c1), hdl:0x30, op1:0x50, op2:0x1
ENDPT: hdspVhdOpen Secondary Connection VHD success. VHD (0x50) of type: 0x0
ENDPT: 'HAPI_RM_OPEN_VHD_EVT' (0x80c1), hdl:0x30, op1:0x51, op2:0x1
ENDPT: hdspVhdOpen Secondary Connection VHD success. VHD (0x51) of type: 0x0
bosMsgQCreate: Created message queue PSTN_CTL_EVQ at address 0x8001
BOS: Enter TaskCreate PSTN
BOS: TaskCreate - spawn new task PSTN
bcmOsTaskCreate:
 TASK NAME      = PSTN
 TASK_PRIORITY  = 0
BOS: Exit TaskCreate
pstnCtlInit successful
vrgendptCreate: capabilities.endptType = 0
ENDPT: 'HAPI_RM_OPEN_VHD_EVT' (0x80c1), hdl:0x30, op1:0x52, op2:0x1
ENDPT: hdspVhdOpen Endpt VHD success. VHD (0x52) of type: 0x2
ENDPT: TX Gain set to 1000
ENDPT: RX Gain set to 1000
ENDPT: 'HAPI_ECAN_STATE_EVT' (0x3ac0), hdl:0x0, op1:0x7, op2:0x0
boardHalCasGetDriver: chan = 0
Default value for provItemId '41' did not exist
ENDPT: Initialization completed successfully for endpt 0
vrgendptCreate: capabilities.endptType = 0
ENDPT: 'HAPI_RM_OPEN_VHD_EVT' (0x80c1), hdl:0x30, op1:0x53, op2:0x1
ENDPT: hdspVhdOpen Endpt VHD success. VHD (0x53) of type: 0x2
ENDPT: TX Gain set to 1000
ENDPT: RX Gain set to 1000
ENDPT: 'HAPI_ECAN_STATE_EVT' (0x3ac0), hdl:0x1, op1:0x7, op2:0x0
boardHalCasGetDriver: chan = 1
Default value for provItemId '41' did not exist
ENDPT: Initialization completed successfully for endpt 1
vrgendptCreate: capabilities.endptType = 1
ENDPT: 'HAPI_RM_OPEN_VHD_EVT' (0x80c1), hdl:0x30, op1:0x54, op2:0x1
ENDPT: hdspVhdOpen PSTN VHD success. VHD (0x54) of type: 0x6
ENDPT: TX Gain set to 1000
ENDPT: RX Gain set to 1000
ENDPT: 'HAPI_ECAN_STATE_EVT' (0x3ac0), hdl:0x2, op1:0x7, op2:0x0
Default value for provItemId '41' did not exist
ENDPT: Initialization completed successfully for endpt 2
DAA: Going OnHook
DAA: Enable on-hook Caller ID receive.
DAA: Going OnHook
DAA: Enable on-hook Caller ID receive.
TCM_GetFXOState, generate cas event = "18"
}}}
'''10) df'''

{{{
Filesystem           1k-blocks      Used Available Use% Mounted on
/dev/mtdblock0            2880      2880         0 100% /
tmpfs                      256       160        96  63% /var}}}
'''11) ifconfig -a'''

{{{
atm0            Link encap:UNSPEC  HWaddr 00-28-00-00-00-00-00-42-00-00-00-00-00-00-00-00
                [NO FLAGS]  MTU:0  Metric:1
                RX packets:0 errors:0 dropped:0 overruns:0 frame:0
                TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
                collisions:0 txqueuelen:0
                RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)
br0             Link encap:Ethernet  HWaddr 00:16:38:6A:96:C0
                inet addr:192.168.0.4  Bcast:192.168.0.255  Mask:255.255.255.0
                UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
                RX packets:1072 errors:0 dropped:0 overruns:0 frame:0
                TX packets:771 errors:0 dropped:0 overruns:0 carrier:0
                collisions:0 txqueuelen:0
                RX bytes:80368 (78.4 KiB)  TX bytes:482768 (471.4 KiB)
cpcs0           Link encap:UNSPEC  HWaddr A7-80-FF-FF-FF-00-00-00-00-00-00-00-00-00-00-00
                [NO FLAGS]  MTU:65535  Metric:1
                RX packets:0 errors:0 dropped:0 overruns:0 frame:0
                TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
                collisions:0 txqueuelen:0
                RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)
dsl0            Link encap:UNSPEC  HWaddr A7-80-00-00-00-00-00-00-00-00-00-00-00-00-00-00
                [NO FLAGS]  MTU:0  Metric:1
                RX packets:0 errors:0 dropped:0 overruns:0 frame:0
                TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
                collisions:0 txqueuelen:0
                RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)
eth0            Link encap:Ethernet  HWaddr 00:16:38:6A:96:C0
                UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
                RX packets:1075 errors:0 dropped:0 overruns:0 frame:0
                TX packets:772 errors:0 dropped:0 overruns:0 carrier:0
                collisions:0 txqueuelen:1000
                RX bytes:100201 (97.8 KiB)  TX bytes:487085 (475.6 KiB)
                Interrupt:28 Base address:0x6000
lo              Link encap:Local Loopback
                inet addr:127.0.0.1  Mask:255.0.0.0
                UP LOOPBACK RUNNING  MTU:16436  Metric:1
                RX packets:1 errors:0 dropped:0 overruns:0 frame:0
                TX packets:1 errors:0 dropped:0 overruns:0 carrier:0
                collisions:0 txqueuelen:0
                RX bytes:29 (29.0 B)  TX bytes:29 (29.0 B)
nas_1_32        Link encap:Ethernet  HWaddr 00:16:38:6A:96:C2
                UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
                RX packets:0 errors:0 dropped:0 overruns:0 frame:0
                TX packets:0 errors:0 dropped:413 overruns:0 carrier:0
                collisions:0 txqueuelen:1000
                RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)
wl0             Link encap:Ethernet  HWaddr 00:16:38:6A:96:C1
                UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
                RX packets:0 errors:0 dropped:0 overruns:0 frame:471
                TX packets:390 errors:25 dropped:0 overruns:0 carrier:0
                collisions:0 txqueuelen:1000
                RX bytes:0 (0.0 B)  TX bytes:34637 (33.8 KiB)
                Interrupt:32
}}}
'''12)  nvram show | sort '''

{{{
nvram: not found
sort: not found
}}}
'''13) Webinterface'''

{{{
Factory Settings set the IP of the SpeedPOrt W500V LAN Interface to: 192.168.2.1
Webinterface: http://192.168.2.1}}}
= Firmware and Firmware Hacks =
'''Original Firmware'''

The Original Firmware Sources with the Tollchains is released by Hitachi High Technologies.

It can be grabbed from their website. http://www.hht-eu.com/pls/hht/wt_show.text_page?p_text_id=7705. It's an 82MB download.

The latest T-Com Firmware Version 1.3 and sources can be grabbed from their website.

Firmware: http://www.telekom.de/dtag/downloads/f/fw_speedport_w500v_v1.30.zip

Sources: http://www.telekom.de/dtag/downloads/b/bcm963xx_SpeedportW500V.01.2.01L.300L01.V27_cons_rel.tar.gz

'''Custom Firmware:'''

There is an alternative Firmware available tested with the SpeedPort W500V and the Targa WR 500 Voip.
It is called BitSwitcher.http://bitswitcher.sourceforge.net
It enables nvram, telnet, ssh, dnsmasq, stproxy etc. and offers a new Web-Interface.
There is a second Firmware Mod Project on Sourceforge available for the SpeedPort W500V.

It's called mod500. http://sourceforge.net/projects/mod500/

It enables telnet on the SpeedPort W500V.

 . User: root
 Password: ''<webinterface password>'' (Factory Password = 0000)
With the mod500 Firmware flashed you can now use the DMT Program to read out system and DSL information.

http://blueflubberball.de/SpeedPort_W500V/DMT.JPG

= Recovery =
If the Firmware Update failed and the router is bricked Firmware wise, during boot time you have the chance to reflash the stock firmware via an emergency Webinterface reachable under 192.168.1.1.

1) Unplug the Power for 3 - 5 seconds

2) Hold the reset button

3) Re-plug the power still holding the reset button

The router will now go into safe mode where the stock firmware can be reflashed.

= Links and Downloads =
Hitachi High Technologies Firmware Sources + Toolchain: http://www.hht-eu.com/pls/hht/wt_show.text_page?p_text_id=7705

T-Com Firmware Sources: http://www.telekom.de/dtag/downloads/b/bcm963xx_SpeedportW500V.01.2.01L.300L01.V27_cons_rel.tar.gz

T-Com Firmware Changelog in German: http://www.telekom.de/dtag/downloads/S/SpeedportW500V_firmwareaenderungen_V1_30.txt

T-Com Firmware GPL Public License: http://www.telekom.de/dtag/downloads/s/Statement.doc

T-Com Firmware Release 1.3: http://www.telekom.de/dtag/downloads/f/fw_speedport_w500v_v1.30.zip

BitSwitcher Firmware: http://bitswitcher.sourceforge.net

mod500 Firmware split from T-Com Stock Rev. 1.3:[http://sourceforge.net/projects/mod500/DMT http://sourceforge.net/projects/mod500/]

DMT Program: http://dmt.mhilfe.de/

= Misc =
To contact me: stacato [at] gmail [DOT] com

CategoryModel ["CategoryBCM63xx"]
