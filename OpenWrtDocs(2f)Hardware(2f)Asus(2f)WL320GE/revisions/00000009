== Hardware Info ==
{{{
Bootloader: CPE
System-on-Chip: BCM5352
CPU Speed: 200MHz
Flash size: 4MB
RAM: 16MB
Wireless: Broadcom Corporation BCM4306 802.11b/g Wireless LAN Controller / Broadcom BCM4320 802.11 Wireless Controller 4.80.53.0
Antennas: 1 (WL-320gE) / 2 (WL-320gP)
Ethernet: 1 Ethernet port (but with integrated Broadcom switch, "ETHERNET" port is connected to port number 3)
USB: yes, but no external connector. Header can be soldered onto the PCB.
Serial: yes, header already present (at least on r1.50 boards)
JTAG: ?
802.3af Power over Ethernet: no (WL-320gE) / yes (WL-320gP)
GPIO: yes, header already present (at least on r1.50 boards)
}}}

=== lspci ===
{{{
00:00.0 FLASH memory: Broadcom Corporation Sentry5 Chipcommon I/O Controller
00:01.0 Ethernet controller: Broadcom Corporation Sentry5 Ethernet Controller
00:02.0 MIPS: Broadcom Corporation BCM3302 Sentry5 MIPS32 CPU
00:03.0 USB Controller: Broadcom Corporation BCM47xx Sentry5 USB Host Controller
00:04.0 RAM memory: Broadcom Corporation Sentry5 DDR/SDR RAM Controller
00:05.0 Network controller: Broadcom Corporation BCM4306 802.11b/g Wireless LAN Controller
00:06.0 Network controller: Broadcom Corporation Unknown device 4719
}}}

=== /proc/cpuinfo ===
{{{system type             : Broadcom BCM5352 chip rev 0
processor               : 0
cpu model               : BCM3302 V0.8
BogoMIPS                : 199.47
wait instruction        : no
microsecond timers      : yes
tlb_entries             : 32
extra interrupt vector  : no
hardware watchpoint     : no
VCED exceptions         : not available
VCEI exceptions         : not available
}}}

=== Switch configuration ===
The WL-320gE and WL-320gP have one LAN port only, however it seems to be connected internally as "switch port 3". So your switch configuration should look something like this:

{{{
config 'switch' 'eth0'
        option 'vlan0' '3 5*'
}}}

Note that unlike e.g. the WL-500g, you will have to leave the bridge setting at "eth0.0"! Using "eth0" instead will not work.

=== nvram show ===
Default: [http://sokrates.mimuw.edu.pl/~sebek/openwrt/wl320gE-nvram.txt]

The bare minimum of nvram variables required should be this (taken from a WL-320gE, HWRev 1.5):

{{{
aa0=1
boardflags=0x0658
boardnum=45
boardrev=0x10
boardtype=0x467
boot_wait=on
clkfreq=200
dl_ram_addr=a0001000
et0macaddr=xx:xx:xx:xx:xx:xx
et0mdcport=0
et0phyaddr=30
hardware_version=WL320G-01-02-01-00
lan_ipaddr=192.168.1.1
lan_netmask=255.255.255.0
opo=0x0
os_date=Jul 25 2007
os_flash_addr=bfc40000  
os_ram_addr=80001000
os_version=3.131.35.0
pmon_ver=CFE 3.91.23.0
scratch=a0180000
sdram_config=0x0032
sdram_init=0x2100
sdram_ncdl=0x2023f
sdram_refresh=0x0
sysDescr=ASUSTeK WL320g 1.9.8.0
watchdog=5000
wl0id=0x4320
}}}

Don't be stupid and try to "optimize" NVRAM - '''you can brick your router'''!

=== Versions Tested ===
 *  7.09, brcm-2.4-squashfs
 * Kamikaze r12712 as of 2008-09-26

== WL320gP ==
This is an identical model with Power over Ethernet.
