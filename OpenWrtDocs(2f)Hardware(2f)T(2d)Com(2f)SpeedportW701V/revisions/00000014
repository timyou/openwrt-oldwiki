#pragma section-numbers off
[[TableOfContents]]

= T-Com Speedport W701V =

This page is Work In Progress, speak to Hydra on #openwrt and #ar7 on freenode for more info.

Others users known to have this device:  saftsack, Heini66

== Hardware Info ==

Uses TI AR7 chipset, onboard wireless lan, a very nice amount of ram (32MB) and flash (8MB) making it a great device to run OpenWRT on!

Being an AR7 device it also has a built-in ADSL Modem, the Speedport W701V also features as ISDN socket and two telephone sockets for VoIP use.

CPU: TNETD7200ZDW (AR7) @211Mhz 
Flash: 8 MB 
Ram: 32 MB 
WLan Chip: TNETW1350A
Ethernet Switch Chip: Infineon ADM6996LC 

It also has a single 3.3v serial port, the original T-Com firmware allows you shell access with no password to the device though the serial port.

== Bootloader ==

The bootloader is ADAM2 which provides a console on the serial port and allows flashing via FTP.  The W701V's bootloader's default IP address is 192.168.178.1, you should be able to ping it on that address a second or two after the device is rebooted.  If not reset the device back to it's defaults using the reset button on the back (see tcom's site for info on how to do this).  My router came with a very recent edition, v1.203, from February 2007.

=== Photos ===

http://www.hydraservices.com/files/t-com_speedport-w701v/pcb1.jpg

http://www.hydraservices.com/files/t-com_speedport-w701v/pcb2.jpg

=== Serial Port ===

It has a 3.3v serial port to the lower right of the CPU, near the crystal and the large capacitor.  The PCB on my router didn't have a pin header/pin strip attached to it so I bought a pin strip from Maplin Electronics for £0.79p and soldered it carefully to the back of the PCB  I then attached my serial port adaptor (see the Addontech ARM8100 page on this wiki for circuit diagram) to the pin header and to my pc.

The general location of the port and it's pin-out is as follows:

{{{
        Top right of PCB
_________________________
                         |
F     R A M              |
L                WIFI    |
A                CHIP    |
S        SoC             |
H        CPU  XTal       |
                 4  GND  |
                 3  TX   |
                 2  RX   |
                 1  VCC  |
                         |
              ADM6996    |
                         |
_________________________|
}}}

Serial port settings: 38400 8N1

== Original Firmware Info ==

=== Backing up original firmware ===

To backup the original firmware you'll need console access to the device, e.g. use a serial cable and minicom to access the root shell.

You can then dump each mtd block to a file and download them via the built in web browser as below.

{{{
mkdir /var/backup
cp /dev/mtd1 /var/backup/mtd1-rootfs.bin
cp /dev/mtd2 /var/backup/mtd2-kernel-and-rootfs.bin
cp /dev/mtd3 /var/backup/mtd3-bootloader.bin
cp /dev/mtd4 /var/backup/mtd4-nvram1.bin
cp /dev/mtd5 /var/backup/mtd5-nvram2.bin
kill `pidof websrv`
cd /var
rm html
ln -s backup html
websrv
}}}

You can then download the files by pointing your webbrowser at {{{http://<your router's ip>/mtd0-rootfs.bin}}} etc.

All being well you should have files like this

{{{
# ls -al
drwxr-xr-x    2 root     root            0 Jan  1 01:10 .
drwxrwxr-x    8 root     root            0 Jan  1 01:04 ..
-rw-r--r--    1 root     root      7158272 Jan  1 01:09 mtd1-rootfs.bin
-rw-r--r--    1 root     root      7798784 Jan  1 01:09 mtd2-kernel-and-rootfs.bin
-rw-r--r--    1 root     root        65536 Jan  1 01:09 mtd3-bootloader.bin
-rw-r--r--    1 root     root       262144 Jan  1 01:10 mtd4-nvram1.bin
-rw-r--r--    1 root     root       262144 Jan  1 01:10 mtd5-nvram2.bin
}}}

=== Restoring Original Firmware ===

==== Undoing changes to adam2 config ====

TODO: finish this section, here's some hints for now

{{{
setenv kernel_args idle=4
unsetenv mtd5
}}}

=== Boot log from old firmware ===

=== Output from various commands on the original firmware ===

When I logged in to the console for the first time it kindly dumped a bunch of info and kernel configuration values for me to see!
{{{
HWRevision='101'
HWRevision_ATA='1'
HWRevision_BitFileCount='1'
HWRevision_Reserved1='0'
ANNEX='B'
OEM='tcom'
OEM_DEFAULT_INDEX=''
OEM_tmp='tcom'
Language='de'
Country='049'
TZ='CET-1CEST,M3.5.0,M10.5.0'
CONFIG_AB_COUNT='2'
CONFIG_ANNEX='B'
CONFIG_ASSIST='y'
CONFIG_ATA='n'
CONFIG_ATA_FULL='n'
CONFIG_AUDIO='n'
CONFIG_AURA='n'
CONFIG_BLUETOOTH='n'
CONFIG_BLUETOOTH_CTP='n'
CONFIG_BUTTON='y'
CONFIG_CAPI='y'
CONFIG_CAPI_MIPS='n'
CONFIG_CAPI_NT='n'
CONFIG_CAPI_POTS='y'
CONFIG_CAPI_TE='y'
CONFIG_CAPI_UBIK='n'
CONFIG_CAPI_XILINX='y'
CONFIG_CDROM='n'
CONFIG_CDROM_FALLBACK='n'
CONFIG_DECT='n'
CONFIG_DSL='y'
CONFIG_ENVIRONMENT_PATH='/proc/sys/urlader'
CONFIG_ETH_COUNT='4'
CONFIG_FIRMWARE_URL='http://www.telekom.de/faq'
CONFIG_FON='y'
CONFIG_HOMEI2C='n'
CONFIG_HOSTNAME='speedport.ip'
CONFIG_I2C='n'
CONFIG_INSTALL_TYPE='ar7_8MB_xilinx_4eth_2ab_isdn_pots_wlan_13200'
CONFIG_JFFS2='n'
CONFIG_LED_NO_DSL_LED='n'
CONFIG_MAILER='n'
CONFIG_MEDIACLI='n'
CONFIG_MEDIASRV='n'
CONFIG_NAND='n'
CONFIG_NFS='n'
CONFIG_OEM_DEFAULT='tcom'
CONFIG_PRODUKT='Fritz_Box_SpeedportW701V'
CONFIG_PRODUKT_NAME='Speedport W 701V'
CONFIG_RAMSIZE='32'
CONFIG_ROMSIZE='8'
CONFIG_SERVICEPORTAL_URL='none'
CONFIG_STOREUSRCFG='n'
CONFIG_SUBVERSION=''
CONFIG_TAM='n'
CONFIG_TAM_MODE='0'
CONFIG_TR069='y'
CONFIG_UBIK2='n'
CONFIG_UPNP='n'
CONFIG_USB='n'
CONFIG_USB_HOST_AVM='n'
CONFIG_USB_HOST_TI='n'
CONFIG_USB_PRINT_SERV='n'
CONFIG_USB_STORAGE='n'
CONFIG_USB_WLAN_AUTH='n'
CONFIG_VDSL='n'
CONFIG_VERSION='04.26'
CONFIG_VERSION_MAJOR='33'
CONFIG_VLYNQ='y'
CONFIG_VLYNQ0='0'
CONFIG_VLYNQ1='0'
CONFIG_VPN='n'
CONFIG_WLAN='y'
CONFIG_WLAN_1130TNET='n'
CONFIG_WLAN_1350TNET='y'
CONFIG_WLAN_GREEN='n'
CONFIG_WLAN_WDS='y'
CONFIG_XILINX='y'
}}}

{{{
~ # ps ax
  PID  Uid     VmSize Stat Command
    1 root        336 S   init
    2 root            SWN [ksoftirqd/0]
    3 root            SW< [events/0]
    4 root            SW< [khelper]
    5 root            SW< [kthread]
    6 root            SW< [kblockd/0]
   24 root            SW< [pdflush]
   25 root            SW< [pdflush]
   27 root            SW< [aio/0]
   26 root            SW  [kswapd0]
   69 root            SW  [mtdblockd]
  128 root            SW  [tffsd_mtd_0]
  352 root            SW  [capitransp]
  411 root        456 S   wpa_authenticator
  424 root       1656 R N websrv
  428 root       1656 S N websrv
  429 root       1656 S N websrv
  430 root       1656 S N websrv
  435 root       1736 S   multid
  444 root       1920 S   dsld -i -n
  458 root        724 S   telefon a127.0.0.1
  463 root       2124 S < voipd
  470 root        160 S   /bin/run_clock -c /dev/tffs -d
  475 root        468 S   -sh
  561 root        312 R   ps ax

}}}

{{{

~ # free
              total         used         free       shared      buffers
  Mem:        30468        24024         6444            0         3040
 Swap:            0            0            0
Total:        30468        24024         6444

}}}

{{{

~ # ls proc
1                   428                 69                  execdomains         meminfo             sysrq-trigger
128                 429                 avalanche           filesystems         misc                sysvipc
2                   430                 buddyinfo           fs                  modules             tffs
24                  435                 bus                 interrupts          mounts              tty
25                  444                 capi                iomem               mtd                 uptime
26                  458                 clocks              ioports             net                 version
27                  463                 cmdline             irq                 partitions          vmstat
3                   470                 cpmac_sched_cpmac0  kallsyms            self                wlan
352                 475                 cpuinfo             kcore               slabinfo            zoneinfo
4                   5                   devices             kmsg                stat
411                 565                 diskstats           loadavg             sync-on-demand
424                 6                   driver              locks               sys

}}}

{{{

~ # cat /proc/cpuinfo
system type             : MIPS OHIO
processor               : 0
cpu model               : MIPS 4KEc V4.8
BogoMIPS                : 211.35
wait instruction        : yes
microsecond timers      : yes
tlb_entries             : 16
extra interrupt vector  : yes
hardware watchpoint     : yes
VCED exceptions         : not available
VCEI exceptions         : not available

}}}

{{{

~ # cat /proc/mtd
dev:    size   erasesize  name
mtd0: 00800000 00010000 "phys_mapped_flash"
mtd1: 006d3b00 00010000 "filesystem"
mtd2: 00770000 00010000 "kernel"
mtd3: 00010000 00010000 "bootloader"
mtd4: 00040000 00010000 "tffs (1)"
mtd5: 00040000 00010000 "tffs (2)"
mtd6: 00200000 00010000 "jffs2"
mtd7: 00570000 00010000 "Kernel without jffs2"

}}}

{{{

~ # cat /proc/avalanche/avsar_ver
ATM Driver version:[4.06.04.30]
DSL HAL version: [5.00.00.02]
DSP Datapump version: [1.35.73.01]
SAR HAL version: [01.07.2b]
PDSP Firmware version:[0.54]

}}}

{{{

~ # cat /proc/version
Linux version 2.6.13.1-ohio (jpluschke@EmbeddedVM) (gcc version 3.4.3) #3 Thu Feb 8 14:32:37 CET 2007

}}}

{{{

~ # cat /proc/meminfo
MemTotal:        30468 kB
MemFree:          6384 kB
Buffers:          3040 kB
Cached:          10232 kB
SwapCached:          0 kB
Active:           9600 kB
Inactive:         6676 kB
HighTotal:           0 kB
HighFree:            0 kB
LowTotal:        30468 kB
LowFree:          6384 kB
SwapTotal:           0 kB
SwapFree:            0 kB
Dirty:               0 kB
Writeback:           0 kB
Mapped:           5648 kB
Slab:             4868 kB
CommitLimit:     15232 kB
Committed_AS:     4428 kB
PageTables:        196 kB
VmallocTotal:  1048560 kB
VmallocUsed:      2636 kB
VmallocChunk:  1044964 kB

}}}

{{{

~ # cat /proc/kmsg
ify disable 0x940013f8 0x9419be18
<4>[ohio_set_clock_notify] avm_clock_id_cpu notify enable 0x940013f8 0x9419be18
<4>CPU frequency 211.97 MHz
<4>Using 105.984 MHz high precision timer.
<4>[setup_irq]: irq 127 irqaction->handler 0x94041a10 (no_action+0x0/0x8 )
<4>[register_console] enable commandline console 0
<4>Dentry cache hash table entries: 8192 (order: 3, 32768 bytes)
<4>Inode-cache hash table entries: 4096 (order: 2, 16384 bytes)
<6>Memory: 30324k/30676k available (1477k kernel code, 320k reserved, 342k data, 112k init, 0k highmem)
<6>totalram_pages= 7589
<4>Calibrating delay loop... 211.35 BogoMIPS (lpj=1056768)
<4>loops_per_jiffy=1056768
<4>Mount-cache hash table entries: 512
<4>Checking for 'wait' instruction... [speedup] idle_mode = 4
<4> with idle values available.
<7>Calling initcall 0x941d6414: helper_init+0x0/0x30()
<7>Calling initcall 0x941d6558: ksysfs_init+0x0/0x3c()
<7>Calling initcall 0x941d840c: filelock_init+0x0/0x48()
<7>Calling initcall 0x941d8c50: init_script_binfmt+0x0/0xc()
<7>Calling initcall 0x941d8c5c: init_elf_binfmt+0x0/0xc()
<7>Calling initcall 0x941dda7c: netlink_proto_init+0x0/0x2ac()
<6>NET: Registered protocol family 16
<7>Calling initcall 0x941d94cc: kobject_uevent_init+0x0/0x50()
<7>Calling initcall 0x941d9754: tty_class_init+0x0/0x34()
<7>Calling initcall 0x941cd57c: frame_info_init+0x0/0xb4()
<4>Can't analyze prologue code at 9416fc8c
<7>Calling initcall 0x941d80fc: init_bio+0x0/0x17c()
<7>Calling initcall 0x941d9e00: misc_init+0x0/0xc0()
<7>Calling initcall 0x941db814: genhd_device_init+0x0/0x44()
<7>Calling initcall 0x941dbf2c: init_mtd+0x0/0x48()
<7>Calling initcall 0x941dccf0: input_init+0x0/0x1e0()
<7>Calling initcall 0x941dd514: proto_init+0x0/0x48()
<7>Calling initcall 0x941dd6d8: net_dev_init+0x0/0x1dc()
<7>Calling initcall 0x941d8360: init_pipe_fs+0x0/0x6c()
<7>Calling initcall 0x941d95e4: chr_dev_init+0x0/0xb4()
<7>Calling initcall 0x941d5a94: create_proc_profile+0x0/0x64()
<7>Calling initcall 0x941d5b74: ioresources_init+0x0/0x6c()
<7>Calling initcall 0x941d5d28: uid_cache_init+0x0/0x88()
<7>Calling initcall 0x941d6104: param_sysfs_init+0x0/0x208()
<7>Calling initcall 0x941d630c: init_posix_timers+0x0/0x108()
<7>Calling initcall 0x941d6444: init_posix_cpu_timers+0x0/0xd4()
<7>Calling initcall 0x941d6518: kallsyms_init+0x0/0x40()
<7>Calling initcall 0x941d7794: init_per_zone_pages_min+0x0/0x64()
<7>Calling initcall 0x941d7bdc: pdflush_init+0x0/0x28()
<7>Calling initcall 0x941d7c04: cpucache_init+0x0/0x20()
<7>Calling initcall 0x941d7f50: kswapd_init+0x0/0x70()
<7>Calling initcall 0x941d8004: init_tmpfs+0x0/0x3c()
<7>Calling initcall 0x941d83cc: fasync_init+0x0/0x40()
<7>Calling initcall 0x941d8ad0: aio_setup+0x0/0x8c()
<7>Calling initcall 0x941d8b5c: inotify_setup+0x0/0xf4()
<7>Calling initcall 0x941d9194: init_devpts_fs+0x0/0x48()
<7>Calling initcall 0x941d91dc: init_squashfs_fs+0x0/0xe4()
<6>Squashfs 2.2-r2b (released 2006/02/23) (C) 2002-2005 Phillip Lougher
<7>Calling initcall 0x941d92c0: init_ramfs_fs+0x0/0xc()
<7>Calling initcall 0x941d92d8: ipc_init+0x0/0x30()
<7>Calling initcall 0x941d9698: rand_initialize+0x0/0x3c()
<7>Calling initcall 0x941d9788: tty_init+0x0/0x184()
<7>Calling initcall 0x941d990c: pty_init+0x0/0x4f4()
<7>Calling initcall 0x941d9ec0: avm_power_init+0x0/0x11c()
<7>Calling initcall 0x941d9fdc: avm_sammel_init+0x0/0x158()
<4>[avm] configured: watchdog eventled enable shift register enable direct gpio
<4>     gpio usage: reset=12 clock=13 store=10 data=9
<4>AR7WDT: Watchdog Driver for AR7 Hardware (Version 1.0, build: Feb  8 2007 14:30:44)
<7>Calling initcall 0x941dae60: serial8250_init+0x0/0x10c()
<6>Serial: 8250/16550 driver $Revision: 1.90 $ 1 ports, IRQ sharing disabled
<4>[uart_add_one_port]
<4>ttyS0 at MMIO 0x0 (irq = 15) is a OHIO_UART
<4>[uart_add_one_port] dont rigister console port->type = 16
<4>port->cons = 0x941a9680 port->cons->flags = 0x7
<4>[uart_add_one_port] sucess
<7>Calling initcall 0x941db858: noop_init+0x0/0xc()
<6>io scheduler noop registered
<7>Calling initcall 0x941db864: cpmac_main_probe+0x0/0xd8()
<7>Calling initcall 0x941db93c: cpphy_entry_probe+0x0/0xcc()
<7>Calling initcall 0x941dba08: cpphy_entry_probe+0x0/0xe8()
<4>(vor) REG_ADM_LC_PHY_CONTROL_PORT(0x200) = 0x3100
<4>(nach) REG_ADM_LC_PHY_CONTROL_PORT(0x200) = 0x3100
<4>(vor) REG_ADM_LC_PHY_CONTROL_PORT(0x220) = 0x3100
<4>(nach) REG_ADM_LC_PHY_CONTROL_PORT(0x220) = 0x3100
<4>(vor) REG_ADM_LC_PHY_CONTROL_PORT(0x240) = 0x3100
<4>(nach) REG_ADM_LC_PHY_CONTROL_PORT(0x240) = 0x3100
<4>(vor) REG_ADM_LC_PHY_CONTROL_PORT(0x260) = 0x3100
<4>(nach) REG_ADM_LC_PHY_CONTROL_PORT(0x260) = 0x3100
<4>(vor) REG_ADM_LC_PHY_CONTROL_PORT(0x280) = 0x3100
<4>(nach) REG_ADM_LC_PHY_CONTROL_PORT(0x280) = 0x3100
<3>cpmac_if_register, dev cpmac0 (phy_id 0) registered
<7>Calling initcall 0x941dbaf0: cpphy_entry_probe+0x0/0xcc()
<7>Calling initcall 0x941dbbbc: cpphy_entry_probe+0x0/0xe8()
<3>cpmac_if_register, phy_id 0 already registered
<7>Calling initcall 0x941dbd34: net_olddevs_init+0x0/0x100()
<7>Calling initcall 0x941dbe9c: tun_init+0x0/0x90()
<6>tun: Universal TUN/TAP device driver, 1.6
<6>tun: (C) 1999-2004 Max Krasnyansky <maxk@qualcomm.com>
<7>Calling initcall 0x941dbf74: cmdline_parser_init+0x0/0xc()
<7>Calling initcall 0x941dbf80: init_mtdchar+0x0/0xc0()
<7>Calling initcall 0x941dc040: init_mtdblock+0x0/0xc()
<7>Calling initcall 0x941dc04c: cfi_probe_init+0x0/0x24()
<7>Calling initcall 0x941dc070: cfi_amdstd_init+0x0/0x30()
<7>Calling initcall 0x941dc0a0: cfi_intelext_init+0x0/0x4c()
<7>Calling initcall 0x941dc0ec: jedec_probe_init+0x0/0x24()
<7>Calling initcall 0x941dc110: map_ram_init+0x0/0x24()
<7>Calling initcall 0x941dc134: init_physmap+0x0/0x170()
<5>physmap flash device: 400000 at 10000000
<6>phys_mapped_flash: Found 1 x16 devices at 0x0 in 16-bit bank
<4> Amd/Fujitsu Extended Query Table at 0x0040
<4>phys_mapped_flash: Swapping erase regions for broken CFI table.
<5>number of CFI chips: 1
<5>cfi_cmdset_0002: Disabling erase-suspend-program due to code brokenness.
<5>RedBoot partition parsing not available
<7>Calling initcall 0x941dc2a4: platram_init+0x0/0x30()
<4>Generic platform RAM MTD, (c) 2004 Simtec Electronics
<7>Calling initcall 0x941dc2d4: init_ohio_flash+0x0/0xa1c()
<5>Ohio flash driver (size->0x400000 mem->0x10000000)
<4>flash_size=0x800000
<6>Ohio flash memory: Found 1 x16 devices at 0x0 in 16-bit bank
<4> Amd/Fujitsu Extended Query Table at 0x0040
<4>Ohio flash memory: Swapping erase regions for broken CFI table.
<5>number of CFI chips: 1
<5>cfi_cmdset_0002: Disabling erase-suspend-program due to code brokenness.
<4>[mtd]: set to default: jffs2_size = 0x20 * 64KByte (0x200000 Bytes)
<4>[ohio_find_hidden_filesystem]: super block found: bytes_used: 0x36347f/3552383
<4>[init_ohio_flash] find hidden filesystem size=0x6d3b00 offset=0xac500
<4>[mtd] configure jffs2 partition
<4>[mtd] fs_size=0x400000 max=0x370000 is=0x200000 max jffs2_size value 55
<5>Creating 7 MTD partitions on "Ohio flash memory":
<5>0x000ac500-0x00780000 : "filesystem"
<5>     'nor-flash'
<4>     'Bits can be cleared (flash)'
<4>     'Has an erase function'
<4>mtd: partition "filesystem" doesn't start on an erase block boundary -- force read-only
<5>0x00010000-0x00780000 : "kernel"
<5>     'nor-flash'
<4>     'Bits can be cleared (flash)'
<4>     'Has an erase function'
<5>0x00000000-0x00010000 : "bootloader"
<5>     'nor-flash'
<4>     'Bits can be cleared (flash)'
<4>     'Has an erase function'
<4>     'Virtual blocks not allowed'
<5>0x00780000-0x007c0000 : "tffs (1)"
<5>     'nor-flash'
<4>     'Bits can be cleared (flash)'
<4>     'Has an erase function'
<4>     'Virtual blocks not allowed'
<5>0x007c0000-0x00800000 : "tffs (2)"
<5>     'nor-flash'
<4>     'Bits can be cleared (flash)'
<4>     'Has an erase function'
<4>     'Virtual blocks not allowed'
<5>0x00580000-0x00780000 : "jffs2"
<5>     'nor-flash'
<4>     'Bits can be cleared (flash)'
<4>     'Has an erase function'
<4>     'Virtual blocks not allowed'
<5>0x00010000-0x00580000 : "Kernel without jffs2"
<5>     'nor-flash'
<4>     'Bits can be cleared (flash)'
<4>     'Has an erase function'
<4>     'Virtual blocks not allowed'
<7>Calling initcall 0x941dced0: kcapi_init+0x0/0x9c()
<7>Calling initcall 0x941dd014: capi_init+0x0/0x324()
<5>capi20: Rev 1.1.2.7: started up with major 68 (middleware+capifs)
<7>Calling initcall 0x941dd338: capifs_init+0x0/0x108()
<5>capifs: Rev 1.1.2.3
<7>Calling initcall 0x941de72c: inet_init+0x0/0x504()
<6>NET: Registered protocol family 2
<4>IP route cache hash table entries: 512 (order: -1, 2048 bytes)
<4>TCP established hash table entries: 2048 (order: 2, 16384 bytes)
<4>TCP bind hash table entries: 2048 (order: 1, 8192 bytes)
<6>TCP: Hash tables configured (established 2048 bind 2048)
<6>TCP reno registered
<7>Calling initcall 0x941e1168: init+0x0/0x8()
<7>Calling initcall 0x941e1170: bictcp_register+0x0/0xc()
<6>TCP bic registered
<7>Calling initcall 0x941e117c: mcfw_init_module+0x0/0x88()
<6>mcfw_init: ok
<7>Calling initcall 0x941e1204: af_unix_init+0x0/0xa0()
<6>NET: Registered protocol family 1
<7>Calling initcall 0x941e12a4: packet_init+0x0/0x80()
<6>NET: Registered protocol family 17
<7>Calling initcall 0x941e1324: br_init+0x0/0x68()
<7>Calling initcall 0x941e13e0: atm_init+0x0/0xec()
<6>NET: Registered protocol family 8
<6>NET: Registered protocol family 20
<7>Calling initcall 0x941e1584: br2684_init+0x0/0x54()
<7>Calling initcall 0x941cc2a0: ohio_install_dummy_irq_functions+0x0/0x58()
<4>[setup_irq]: irq 1 irqaction->handler 0x94001664 (dummy_timer_irq+0x0/0x14 )
<4>[setup_irq]: irq 6 irqaction->handler 0x94001678 (dummy_system_irq_2+0x0/0x18 )
<7>Calling initcall 0x9400174c: ohio_late_init+0x0/0x3c()
<4>[ohio_late_init]
<4>[ohio_set_clock_notify] avm_clock_id_system notify disable 0x9400169c 0x94279e48
<4>[ohio_set_clock_notify] avm_clock_id_system notify enable 0x9400169c 0x94279e48
<7>Calling initcall 0x941cc3f8: ohio_clk_switch_init+0x0/0x60()
<7>Calling initcall 0x941cc6ac: speedup_init+0x0/0x2c()
<7>Calling initcall 0x941d96d4: seqgen_init+0x0/0x20()
<7>Calling initcall 0x940c5b18: avm_event_push_button_init+0x0/0x114()
<7>Calling initcall 0x941da610: tffs_init+0x0/0x2e4()
<6>[tffs] alloc_chrdev_region() param=mtd4
<6>[tffs] CONFIG_TFFS_MTD_DEVICE_0=4 CONFIG_TFFS_MTD_DEVICE_1=5
<6>[tffs] Character device init successfull
<4>TFFS: tiny flash file system driver. GPL (c) AVM Berlin (Version 2.0)
<4>      mount on mtd4 and mtd5 (double buffering)
<6>Adam2 environment variables API installed.
<7>Calling initcall 0x941db524: early_uart_console_switch+0x0/0xb8()
<7>Calling initcall 0x94113e38: net_random_reseed+0x0/0x34()
<7>Calling initcall 0x941dfc50: ip_auto_config+0x0/0x1140()
<4>[prepare_namespace] new mount root /dev/mtdblock1
<6>tffsd: wait for events
<4>use lzma compression
<4>VFS: Mounted root (squashfs filesystem) readonly.
<4>Freeing prom memory: 0kb freed
<6>Freeing unused kernel memory: 112k freed (7617 free)
<4>[setup_irq]: irq 15 irqaction->handler 0x940cf534 (serial8250_interrupt+0x0/0x128 )
<4>[setup_irq]: irq 15 irqaction->handler 0x940cf534 (serial8250_interrupt+0x0/0x128 )
<4>[setup_irq]: irq 15 irqaction->handler 0x940cf534 (serial8250_interrupt+0x0/0x128 )
<4>[setup_irq]: irq 15 irqaction->handler 0x940cf534 (serial8250_interrupt+0x0/0x128 )
<4>AR7WDT: System Init UEberwachung 120 Sekunden
<4>TFFS Name Table 8
<4>Piglet: module license '
<4>(C) Copyright 2005 by AVM
<4>' taints kernel.
<4>registered device TI Avalanche SAR
<4>tiatm driver (patch_annex=0xc00519ec)
<4>[tiatm] Set StrictPriority=0
<4>DSP binary filesize = 303784 bytes
<4>[setup_irq]: irq 23 irqaction->handler 0xc003920c (tn7atm_sar_irq+0x0/0x30 [tiatm] )
<4>[setup_irq]: irq 31 irqaction->handler 0xc003923c (tn7atm_dsl_irq+0x0/0x28 [tiatm] )
<4>[tiatm]: Powermanagment (States => 1,3,10) supported!
<4>Texas Instruments ATM driver: version:[4.06.04.30]
<4>ubik2 driver (ubik2 - 0x10=0xc00646b4)
<4>atm_dsp_register_ubik2: ubik2_ToMIPS_notify=0xc0055c00
<4>atm_dsp_register_ubik2: dsp mem pointer 0xa1c0f218
<3>ubik2_init_interface: DSP-Link Version v3 8480
<6>isdn_fbox: Loading...
<6>isdn_fbox: Driver 'isdn_fbox' attached to stack
<6>isdn_fbox: CAPI driver registered.
<4>isdn_fbox: AVM F!Box expected @ port 0x0000, irq 0
<4>isdn_fbox: Loading...
<6>isdn_fbox: Stack version 3.11-07
<6>isdn_fbox: D-channel 0: DSS1
<6>isdn_fbox: D-channel 1: DSS1
<6>isdn_fbox: D-channel 2: DSS1_N
<6>isdn_fbox: D-channel 3: POTS
<6>isdn_fbox: D-channel 4: SIP
<4>isdn_fbox: Loaded.
<6>kdsldmod: init start
<6>kdsld: cache_create(datapipe)
<6>kdsld: cache_create(datapipe_mod)
<6>kdsld: cache_create(ipaccessset)
<6>kdsld: cache_create(ipaccessrule)
<6>kdsld: cache_create(ipfragid)
<6>kdsld: cache_create(ipmasqentry)
<6>kdsld: cache_create(ipmasqfwinfo)
<6>kdsld: cache_create(ipmasqigdpm)
<6>kdsld: cache_create(ipmasqappldata)
<6>kdsld: cache_create(ipmasqmcgroup)
<6>kdsld: cache_create(dnsmasqentry)
<6>kdsld: cache_create(dnsstaticentry)
<6>kdsld: cache_create(pingerentry)
<6>kdsld: cache_create(pingerwaiter)
<6>kdsld: cache_create(iprouteset)
<6>kdsld: DATAPIPE: with header optimization
<6>kdsldmod: init done
<6>kdsld: PPP led: off (value=0)
<4>[speedup] disable
<4>429493936: Configuration succeeded !!!
<4>[ohio_vlynq_init] device 0
<4>[ohio_vlynq_startup_link]
<4>[setup_irq]: irq 29 irqaction->handler 0x94004f2c (vlynq_interrupt+0x0/0x34 )
<4>[setup_irq]: irq 79 irqaction->handler 0xc02d7a10 (whal_acxIntrHandler+0x0/0x1e8 [tiap] )
<4>429493943:
<4>429493966: WDRV_MAINSM: WLAN Driver initialized successfully
<4>
<4>429493966: FW Watchdog is Enabled
<6>dda: tiwlan0 in initializing Succeeded wireless extensions: ret = 0
<6>tiwlan0 device is activated
<6>wdsup0 device is activated
<6>wdsdw0 device is activated
<6>wdsdw1 device is activated
<6>wdsdw2 device is activated
<6>wdsdw3 device is activated
<4>[setup_irq]: irq 27 irqaction->handler 0x940e016c (cpmac_main_isr+0x0/0x78 )
<3>cpmac_main_ioctl, unknown ioctl 35142
<6>device eth0 entered promiscuous mode
<6>device cpmac0 entered promiscuous mode
<6>lan: port 1(eth0) entering learning state
<4>tiwlan_ddaDoIoctl : Unknown ioctl 35142
<6>device tiwlan0 entered promiscuous mode
<6>lan: port 2(tiwlan0) entering learning state
<4>tiwlan_ddaWdsDoIoctl : Unknown ioctl 35142
<6>device wdsup0 entered promiscuous mode
<6>lan: port 3(wdsup0) entering learning state
<4>tiwlan_ddaWdsDoIoctl : Unknown ioctl 35142
<6>device wdsdw0 entered promiscuous mode
<6>lan: port 4(wdsdw0) entering learning state
<4>tiwlan_ddaWdsDoIoctl : Unknown ioctl 35142
<6>device wdsdw1 entered promiscuous mode
<6>lan: port 5(wdsdw1) entering learning state
<4>tiwlan_ddaWdsDoIoctl : Unknown ioctl 35142
<6>device wdsdw2 entered promiscuous mode
<6>lan: port 6(wdsdw2) entering learning state
<4>tiwlan_ddaWdsDoIoctl : Unknown ioctl 35142
<6>device wdsdw3 entered promiscuous mode
<6>lan: port 7(wdsdw3) entering learning state
<6>kdsld: sync lost
<4>AR7WDT: System Init UEberwachung abgeschlossen (93030 ms noch verfuegbar)
<6>SysRq : Changing Loglevel
<4>Loglevel set to 4
<6>lan: topology change detected, propagating
<6>lan: port 1(eth0) entering forwarding state
<6>lan: topology change detected, propagating
<6>lan: port 2(tiwlan0) entering forwarding state
<6>lan: topology change detected, propagating
<6>lan: port 3(wdsup0) entering forwarding state
<6>lan: topology change detected, propagating
<6>lan: port 4(wdsdw0) entering forwarding state
<6>lan: topology change detected, propagating
<6>lan: port 5(wdsdw1) entering forwarding state
<6>lan: topology change detected, propagating
<6>lan: port 6(wdsdw2) entering forwarding state
<6>lan: topology change detected, propagating
<6>lan: port 7(wdsdw3) entering forwarding state
<6>mcfw_query_sent: tiwlan:0:0.0.0.0 1000
<6>mcfw_query_sent: tiwlan:0:0.0.0.0 1000
<6>mcfw_query_sent: tiwlan:0:0.0.0.0 1000
<6>mcfw_query_sent: tiwlan:0:0.0.0.0 1000
<6>mcfw_query_sent: tiwlan:0:0.0.0.0 1000
<6>mcfw_query_sent: tiwlan:0:0.0.0.0 1000
<6>mcfw_query_sent: tiwlan:0:0.0.0.0 1000
<6>mcfw_query_sent: tiwlan:0:0.0.0.0 1000
<6>mcfw_query_sent: tiwlan:0:0.0.0.0 1000
<6>mcfw_query_sent: tiwlan:0:0.0.0.0 1000
<6>mcfw_query_sent: tiwlan:0:0.0.0.0 1000
<6>mcfw_query_sent: tiwlan:0:0.0.0.0 1000
<4>[tiatm] DSL in training!
<6>mcfw_query_sent: tiwlan:0:0.0.0.0 1000
<6>mcfw_query_sent: tiwlan:0:0.0.0.0 1000
<4>[tiatm] DSL in training!
<6>mcfw_query_sent: tiwlan:0:0.0.0.0 1000
<6>mcfw_query_sent: tiwlan:0:0.0.0.0 1000
<6>mcfw_query_sent: tiwlan:0:0.0.0.0 1000

}}}

{{{

~ # cat /proc/iomem
14000000-1420afff : reserved
  14000000-141715d3 : Kernel code
  141715d4-141c70bf : Kernel data
1420b000-15ffffff : System RAM
a8610000-a86107ff : cpmac0

}}}

{{{

~ # cat /proc/devices
Character devices:
  1 mem
  2 pty
  3 ttyp
  4 ttyS
  5 /dev/tty
  5 /dev/console
  5 /dev/ptmx
 10 misc
 13 input
 68 capi20
 90 mtd
128 ptm
136 pts
191 capi
230 tiatm
240 tffs
241 avm_event
242 watchdog
243 kdsld
244 kdsldptrace
245 ubik2
246 debug
251 avm_led
252 avm_power

Block devices:
 31 mtdblock

}}}

{{{

~ # cat /proc/modules
tiap 880464 0 - Live 0xc02ab000
kdsldmod 515808 2 - Live 0xc022c000
isdn_fbox 931040 20 - Live 0xc0147000
ubik2 69104 1 isdn_fbox, Live 0xc0055000
tiatm 106560 1 ubik2, Live 0xc0039000
Piglet 7632 0 - Live 0xc000a000

}}}

{{{

~ # ifconfig
cpmac0    Link encap:Ethernet  HWaddr 00:1A:4F:CB:E2:D9
          UP BROADCAST MULTICAST  MTU:1500  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:256
          RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)

eth0      Link encap:Ethernet  HWaddr 00:1A:4F:CB:E2:D9
          UP BROADCAST RUNNING ALLMULTI MULTICAST  MTU:1500  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:19 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0
          RX bytes:0 (0.0 B)  TX bytes:1026 (1.0 KiB)

lan       Link encap:Ethernet  HWaddr 00:1A:4F:CB:E2:D9
          inet addr:192.168.2.1  Bcast:192.168.2.255  Mask:255.255.255.0
          UP BROADCAST RUNNING ALLMULTI MULTICAST  MTU:1500  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:21 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0
          RX bytes:0 (0.0 B)  TX bytes:1062 (1.0 KiB)

lan:0     Link encap:Ethernet  HWaddr 00:1A:4F:CB:E2:D9
          inet addr:192.168.2.254  Bcast:192.168.2.255  Mask:255.255.255.0
          UP BROADCAST RUNNING ALLMULTI MULTICAST  MTU:1500  Metric:1

lo        Link encap:Local Loopback
          inet addr:127.0.0.1  Mask:255.0.0.0
          UP LOOPBACK RUNNING  MTU:16436  Metric:1
          RX packets:270 errors:0 dropped:0 overruns:0 frame:0
          TX packets:270 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0
          RX bytes:32574 (31.8 KiB)  TX bytes:32574 (31.8 KiB)

tiwlan0   Link encap:Ethernet  HWaddr 00:1A:4F:90:5B:9E
          UP BROADCAST RUNNING ALLMULTI MULTICAST  MTU:1500  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:19 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:0 (0.0 B)  TX bytes:950 (950.0 B)

wdsdw0    Link encap:Ethernet  HWaddr 00:1A:4F:90:5B:9E
          UP BROADCAST RUNNING ALLMULTI MULTICAST  MTU:1500  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:19 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:0 (0.0 B)  TX bytes:950 (950.0 B)

wdsdw1    Link encap:Ethernet  HWaddr 00:1A:4F:90:5B:9E
          UP BROADCAST RUNNING ALLMULTI MULTICAST  MTU:1500  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:19 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:0 (0.0 B)  TX bytes:950 (950.0 B)

wdsdw2    Link encap:Ethernet  HWaddr 00:1A:4F:90:5B:9E
          UP BROADCAST RUNNING ALLMULTI MULTICAST  MTU:1500  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:19 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:0 (0.0 B)  TX bytes:950 (950.0 B)

wdsdw3    Link encap:Ethernet  HWaddr 00:1A:4F:90:5B:9E
          UP BROADCAST RUNNING ALLMULTI MULTICAST  MTU:1500  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:19 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:0 (0.0 B)  TX bytes:950 (950.0 B)

wdsup0    Link encap:Ethernet  HWaddr 00:1A:4F:90:5B:9E
          UP BROADCAST RUNNING ALLMULTI MULTICAST  MTU:1500  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:19 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:0 (0.0 B)  TX bytes:950 (950.0 B)
}}}

{{{
~ # cat /etc/avm_firmware_public_key1
00d153ab43f587bc891397f763ac18aff92b840cdfd5aeb773c995ae957cd3b992cd48eacc7ac940cb38e0849777010ed41189c986cfbe67b929121934654f3976b2748f8d16059d9a1e518617c4dcfba468ec865c2bae9269b
010001
}}}

{{{
~ # cat /etc/avm_firmware_public_key2
00e1519e966ee984cdf564825a34cc9beb3c14f720579781e8859eb51f963560979ef16caa6e279376dc9c60a35d67d2b32128ce8f8abb29b2c3aace92bc32607b0b2f09dfcc3c9258d1e6b1daff58fd1f29c410a31ef454e0b
010001
}}}

{{{

~ # cat /etc/led.conf
DEF error,0 = 1,128,0,all
DEF error,1 = 3,127,0,all
DOUBLE error,0 TO error,1
DEF power,0 = 0,7,0,power
DEF power,1 = 0,7,0,power
DEF tr69,0 = 2,6,1,tr69
DEF cpmac,3 = 99,0,2,lan4
DEF cpmac,2 = 99,1,3,lan3
DEF cpmac,1 = 99,2,4,lan2
DEF cpmac,0 = 99,3,5,lan
DEF wlan,0 = 2,5,6,wlan
DEF ab,1 = 2,4,7,festnetz
DEF ab,2 = 2,4,7,festnetz
DEF ab,3 = 2,4,7,festnetz
DEF voip_con,0 = 2,3,8,voip_con
DEF pppoe,0 = 2,2,9,dsl
DEF pppoe,1 = 2,2,9,dsl
DEF adsl,0 = 2,1,10,adsl
DEF adsl,1 = 2,1,10,adsl
DEF ata,0 = 2,0,11,ata
DEF usb,0 = 99,32,12,usb
DEF usb,1 = 99,32,12,usb
DEF blockring,0 = 99,32,13,blockring
DEF missedcall,0 = 99,32,14,missedcall
DEF budget,0 = 99,32,15,budget
DEF info,0 = 99,32,16,info
DEF info,1 = 99,32,16,info
DEF info,2 = 99,32,16,info
DEF info,3 = 99,32,16,info
DEF info,4 = 99,32,16,info
DEF internet,0 = 99,32,17,internet
DEF internet,1 = 99,32,17,internet
DEF isdn,0 = 99,32,18,isdn
DEF isdn,1 = 99,32,18,isdn
DEF isdn,2 = 99,32,18,isdn
DEF stick_surf,0 = 99,32,19,stick_surf
DEF stick_surf,1 = 99,32,19,stick_surf
DEF stick_surf,2 = 99,32,19,stick_surf
DEF stick_surf,3 = 99,32,19,stick_surf
DEF null,0 = 99,32,20,null_device
MAP budget,0 TO info,1
MAP ab,2 TO null,0
SET power,0 = 1

}}}

=== Output from various ADAM2 commands on original firmware ===

{{{

(AVM) EVA Revision: 1.203 Version: 1203
(C) Copyright 2005 AVM Date: Feb  7 2007 Time: 19:03:32 (3) 2 0-11111

[FLASH:] SPANSION Top-MirrorBit-Flash 8MB 32 Bytes WriteBuffer
[FLASH:](Eraseregion [0] 127 sectors a 64kB)
[FLASH:](Eraseregion [1] 8 sectors a 8kB)
[SYSTEM:] OHIO on 211MHz/125MHz

Eva_AVM >
       Commands   Description
       --------   -----------
           help   help
             dm   dump mem <addr> <range>
             cm   change mem <addr> <value>
          erase   Erase Flash <mtd>
       printenv   print Env. Variables
        restart   reboot Device
         setenv   set Env. variable <var> <value>
       unsetenv   unset Env. variable <var>
             go   load & start kernel from mtd1
         setmac   set mac addresses <addr> (like 12:23:40)
        memtest   test memory

Eva_AVM >printenv
HWRevision            101.1.1.0
ProductID             Fritz_Box_SpeedportW701V
SerialNumber          0000000000000000
annex                 B
autoload              yes
bootloaderVersion     1.203
bootserport           tty0
bluetooth
cpufrequency          211968000
firstfreeaddress      0x946B1D78
firmware_version      tcom
firmware_info         33.04.26
flashsize             0x00800000
kernel_args           idle=4
maca                  00:1A:4F:CB:E2:D9
macb                  00:1A:4F:CB:E2:DA
macwlan               00:1A:4F:90:5B:9E
macdsl                00:1A:4F:CB:E2:DB
memsize               0x02000000
modetty0              38400,n,8,1,hw
modetty1              38400,n,8,1,hw
mtd0                  0x90000000,0x90000000
mtd1                  0x90010000,0x90780000
mtd2                  0x90000000,0x90010000
mtd3                  0x90780000,0x907C0000
mtd4                  0x907C0000,0x90800000
my_ipaddress          192.168.178.1
prompt                Eva_AVM
ptest
reserved
req_fullrate_freq     125000000
sysfrequency          125000000
urlader-version       1203
usb_board_mac         00:1A:4F:CB:E2:DC
usb_rndis_mac         00:1A:4F:CB:E2:DD
usb_device_id         0x0000
usb_revision_id       0x0000
usb_device_name       USB DSL Device
usb_manufacturer_name  AVM
wlan_key              3577134058785966
wlan_cal              001C,03F2,000F,00D2,010A,00D2,010A,02E0,02DA
}}}

=== Original Flash Map ===

||'''partition''' ||'''start''' ||'''end''' ||'''size''' ||'''description''' ||
||mtd0 ||{{{0x90000000}}} ||{{{0x90000000}}} ||{{{0x000000}}} ||empty! ||
||mtd1 ||{{{0x90010000}}} ||{{{0x90780000}}} ||{{{0x770000}}} ||kernel+jffs2 (jffs starts at 0x00580000) ||
||mtd2 ||{{{0x90000000}}} ||{{{0x90010000}}} ||{{{0x010000}}} ||ADAM2/bootloader ||
||mtd3 ||{{{0x90780000}}} ||{{{0x907c0000}}} ||{{{0x040000}}} ||tffs (1) ? ||
||mtd4 ||{{{0x907c0000}}} ||{{{0x90800000}}} ||{{{0x040000}}} ||tffs (2) ? ||

Physical order of partitions on flash chip is:

mtd0,mtd2,mtd1,mtd3,mtd4

mtd0 is rather odd as it's 0 length!

== Installing OpenWrt ==

To install OpenWRT you need an OpenWRT Kamikaze image file, it's best to build your own if you have a Linux system around, the process is quite simple and well documented, there's just a few options that need to be changed from the build system's defaults.

=== Build Options ===

TODO

==== Watchdog Issues ====

Due to a problem with the current ar7 watchdog code (as of 22/03/2007) the watchdogs must be disabled.  Failure to do so will just result in a kernel that hangs when the watchdog driver is initialised.  See topic http://forum.openwrt.org/viewtopic.php?id=8052 for a similar problem.

{{{
vi target/linux/ar7-2.4/config/default
}}}

then set these options as follows:

{{{
CONFIG_AR7_WDT=n
CONFIG_SOFT_WATCHDOG=n
}}}

=== Flashing your OpenWRT image ===

The best way to do this is using the bootloaders built in FTP server.  I also prefer to have a serial cable attached so I can monitor the progress, but this optional.

To flash OpenWRT onto any device there must be an MTD Block that spans the main unused area of the flash rom.  The adam2 bootloader always boots from MTD1 (using the "go" command).  As it turns out the W701V's MTD block 1 (mtd1) is correct for the flashing operation as can be seen from this except from the original flash map table (above).

||'''partition''' ||'''start''' ||'''end''' ||'''size''' ||'''description''' ||
||mtd1 ||{{{0x90010000}}} ||{{{0x90780000}}} ||{{{0x770000}}} ||kernel+jffs2 (jffs starts at 0x00580000) ||

The W701V's default ip address is '192.168.178.1' - You can change the default adam2 address using the adam2 setenv commands to change the 'my_ipaddress' variable.
Give your PC an IP address of '192.168.178.10'.
Reboot the router an within 5 seconds connect to the ADAM2 ftp server on '192.168.178.1'.
If you have a serial cable you can also reboot the router and press a key to get the router to wait in the ADAM2 console so that you have more time to connect via ftp to it.
You should also be able to ping the device in the 5 second window or while the adam2 boot loader is paused, if not see the bootloader section of this document (above).

The login name and password for the ftp server is adam2 (lower case). 

Now you can flash with the firmware of your choice. I (Hydra) downloaded openwrt from the svn repos and built a stock flash image which was created by the build process as 'trunk/bin/openwrt-ar7-2.4-squashfs.bin'. The JFFS images were also created which can be also be used. The JFFS image to use would be the one with the 64k erase size, e.g. 'openwrt-ar7-2.4-jffs2-64k.bin'.

I flashed the firmware by issue the following commands:

{{{
binary
quote MEDIA FLSH
passiv
put /home/hydra/openwrt/svn/trunk/bin/openwrt-ar7-2.4-squashfs.bin "openwrt-ar7-2.4-squashfs.bin mtd1"
quote REBOOT
bye
}}}

Passiv mode must be used otherwise the device reports "501 Command Not Implemented" after issuing the "put" command.

The entire process looked like this:

{{{
hydra@hydra02:~$ ftp 192.168.178.1
Connected to 192.168.178.1.
220 ADAM2 FTP Server ready.
Name (192.168.178.1:hydra): adam2
331 Password required for adam2.
Password:
230 User adam2 successfully logged in.
Remote system type is UNIX.
ftp> binary
200 Type set to I.
ftp> quote MEDIA FLSH
200 Media set to FLSH.
ftp> passiv
Passive mode on.
ftp> put /home/hydra/openwrt/svn/trunk/bin/openwrt-ar7-2.4-squashfs.bin mtd1
local: /home/hydra/openwrt/svn/trunk/bin/openwrt-ar7-2.4-squashfs.bin remote: mtd1
200 Port command successful.
150 Opening BINARY mode data connection for file transfer.
226 Transfer complete.
1697713 bytes sent in 7.37 secs (225.0 kB/s)
ftp> quote REBOOT
221 Thank you for using the FTP service on ADAM2.
221 Goodbye.
ftp> quit
}}}

There is a pause before the file is transferred where the router erases the mtd1 block. If you have a serial cable attached you can see the output in the adam2 console.

After the file is transferred there is another pause while the image file is flashed to the chip, don't reboot your router during this time.

Some users have reported errors appearing in the serial console that complain about flashing problems.  It appears that the flash process sometimes retries and succeedes and other times it fails.  failure is not reported to the ftp so it's advised to always use a serial cable so you can monitor  the flash process, if it fails just "put" the image via ftp until it doesn't report a failure.


The entire log from the serial console was as follows:
{{{
TODO
}}}

Once the firmware is flashed you have to create an mtd block that spans the entire squashfs filesystem image on the flash.  I've not found a simple way round this yet but here's what i did:

1) open the squashfs image in a hex editor (khexedit / ultraedit) and do an ascii search for "hsqs", the hex editor should show the file offset (of the 'h' character) from the beginning of the file.  note this number
2) add the offset of the mtd1 block to the number you just noted down
3) create an mtd block using the adam2 setenv command starting from the new number and going to the end of the mtd1 block.  the last mtd block in the adam2 environment was mtd4 for me, so i used mtd5, and issued this command:

{{{
setenv mtd5 0x900868ff,0x90780000
}}}

Do to an issue where the kernel command line is not overridden we need to update the adam2 settings so the kernel command line (shown just after the kernel boots) is set correctly)

{{{
setenv kernel_args root=/dev/mtdblock2 rootfstype=squashfs,jffs2 init=/etc/preinit
}}}

Finally, boot the device!  - type either "restart" or "go" at the adam2 prompt on the serial port or power the box off and on again.

My boot log looked like this:
{{{
Eva_AVM >go
........done
start kernel
Launching kernel decompressor.
Kernel decompressor was successful ... launching kernel.

LINUX started...
CPU revision is: 00018448
Primary instruction cache 16kB, physically tagged, 4-way, linesize 16 bytes.
Primary data cache 8kB, 4-way, linesize 16 bytes.
Linux version 2.4.34 (hydra@hydra02) (gcc version 3.4.6 (OpenWrt-2.0)) #6 Thu Mar 22 21:33:14 GMT 2007
Determined physical RAM map:
 memory: 00020000 @ 14000000 (ROM data)
 memory: 01fe0000 @ 14020000 (usable)
On node 0 totalpages: 8192
zone(0): 8192 pages.
zone(1): 0 pages.
zone(2): 0 pages.
Kernel command line: root=/dev/mtdblock2 rootfstype=squashfs,jffs2 init=/etc/preinit root=/dev/mtdblock2 rootfstype=squashfs,jffs2 init=/etc/preinit console=ttyS0,38400
the pacing pre-scalar has been set as 600.
Using 75.000 MHz high precision timer.
Calibrating delay loop... 149.91 BogoMIPS
Memory: 30476k/32768k available (1383k kernel code, 2292k reserved, 92k data, 68k init, 0k highmem)
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
Registering mini_fo version $Id$
devfs: v1.12c (20020818) Richard Gooch (rgooch@atnf.csiro.au)
devfs: boot_options: 0x1
JFFS2 version 2.1. (C) 2001 Red Hat, Inc., designed by Axis Communications AB.
squashfs: version 3.0 (2006/03/15) Phillip Lougher
pty: 256 Unix98 ptys configured
Serial driver version 5.05c (2001-07-08) with no serial options enabled
ttyS00 at 0xa8610e00 (irq = 15) is a 16550A
Vlynq CONFIG_AR7_VLYNQ_PORTS=2
Vlynq Device vlynq0 registered with minor no 63 as misc device. Result=0
Vlynq instance:0 Link UP
Vlynq Device vlynq1 registered with minor no 62 as misc device. Result=0
VLYNQ 1 : init failed
ar7 flash device: 0x400000 at 0x10000000.
 Amd/Fujitsu Extended Query Table v1.3 at 0x0040
Physically mapped flash: Swapping erase regions for broken CFI table.
number of CFI chips: 1
cfi_cmdset_0002: Disabling fast programming due to code brokenness.
Parsing ADAM2 partition map...
Looking for mtd device :mtd0:
Found a mtd0 image (0x0), with size (0x0).
Assuming adam2 size of 0x0
Looking for mtd device :mtd1:
Found a mtd1 image (0x10000), with size (0x770000).
Looking for mtd device :mtd2:
Found a mtd2 image (0x0), with size (0x10000).
Assuming adam2 size of 0x10000
Looking for mtd device :mtd3:
Found a mtd3 image (0x780000), with size (0x40000).
Looking for mtd device :mtd4:
Found a mtd4 image (0x7c0000), with size (0x40000).
Setting new rootfs offset to 000868ff
Squashfs detected (size = 0xb0086973)
Creating 5 MTD partitions on "Physically mapped flash":
0x00000000-0x00010000 : "adam2"
0x00010000-0x00400000 : "linux"
0x000868ff-0x001b0000 : "rootfs"
mtd: partition "rootfs" doesn't start on an erase block boundary -- force read-only
0x00400000-0x00800000 : "config"
0x001b0000-0x00400000 : "rootfs_data"
Initializing Cryptographic API
NET4: Linux TCP/IP 1.0 for NET4.0
IP Protocols: ICMP, UDP, TCP, IGMP
IP: routing cache hash table of 512 buckets, 4Kbytes
TCP: Hash tables configured (established 2048 bind 4096)
ip_conntrack version 2.1 (5953 buckets, 5953 max) - 360 bytes per conntrack
p_tables: (C) 2000-2002 Netfilter core team
ET4: Unix domain sockets 1.0/SMP for Linux NET4.0.
NET4: Ethernet Bridge 008 for NET4.0
802.1Q VLAN Support v1.8 Ben Greear <greearb@candelatech.com>
All bugs added by David S. Miller <davem@redhat.com>
VFS: Mounted root (squashfs filesystem) readonly.
Mounted devfs on /dev
Can't preserve ADAM2 memory, firstfreeaddress = 946b1d78.
Freeing prom memory: 128kb freed
Freeing unused kernel memory: 68k freed
Algorithmics/MIPS FPU Emulator v1.5
mount: mounting none on /dev failed
Unlocking rootfs ...
Could not open mtd device: rootfs
switching to jffs2
mini_fo: using base directory: /
mini_fo: using storage directory: /jffs
init started:  BusyBox v1.4.1 (2007-03-20 22:57:20 GMT) multi-call binary

Please press Enter to activate this console. jffs2.bbc: SIZE compression mode activated.
Using the MAC with external PHY
Cpmac driver is allocating buffer memory at init time.
Using the MAC with external PHY
Cpmac driver Disable TX complete interrupt setting threshold to 20.
CSLIP: code copyright 1989 Regents of the University of California
PPP generic driver version 2.4.2
IPP2P v0.8.1_rc1 loading
registered device TI Avalanche SAR
Initializing DSL interface
}}}

TODO: it hung.. more diagnostic work to be done.

=== Getting the ADSL Working via PPPoA (Manually) ===

=== Getting the ADSL Working via PPPoA (using the Kamikaze init scripts) ===

=== Firmware images and configs ===

== References ==

There are loads of forum posts (in german) relating to the W701V here (use Suchen, top right, to search) http://www.ip-phone-forum.de/forumdisplay.php?f=560

----
 CategoryModel ["CategoryAR7Device"]
