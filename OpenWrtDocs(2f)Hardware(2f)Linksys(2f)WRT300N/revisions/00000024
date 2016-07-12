## Please add only OpenWrt and WRT300N related things to this page! Thanks.
'''Linksys WRT300N'''

'''Identification by S/N'''

Useful for identifying shrinkwrapped units. The '''S/N''' can be found on the box, below the UPC barcode.
||||<style="text-align: center;"> (!) '''Please contribute to this list.''' (!) ||||<style="text-align: center;">'''!OpenWrt''' ||
||'''Model''' ||<style="text-align: center;"> '''S/N''' ||<style="text-align: center;">  '''Stable[[BR]]White Russian''' ||<style="text-align: center;">  '''Development[[BR]]Kamikaze''' ||
||WRT300N v1.0 ||<style="text-align: center;"> CNP01 || ( ) || ( ) ||
||WRT300N v2.0 ||<style="text-align: center;"> SNP00 || ( ) || (X) ||


'''WRT300N v1.0'''

The WRT300N v1.0 is based on the Broadcom 4704 cpu. I guess it has about 300MHz. It has 4 MB flash and 32 MB SDRAM. The wireless NIC is a Broadcom Cardbus card with BCM4329 Chipset.  The switch is an Broadcom BCM5325 FKQMG.

'''WRT300N v2.0'''

The WRT300N v2.0 is based on the Intel IXP420 cpu which is part of the IXP425 family. The cpu runs at 266Mhz.  It has 4Mb of flash and 16Mb of RAM. It has a Marvell 88E6060 switch chip. The wireless is provided by a mini-pci card containing an ar5416 or ar5418 MAC. It is running linux out of the box.

'''Table summary'''

How to get info:

 * board info: {{{nvram show | grep board | sort}}}[[BR]]
 * cpu model: {{{grep cpu /proc/cpuinfo}}}
||'''Model''' ||'''boardrev''' ||'''boardtype''' ||'''boardflags''' ||'''boardflags2''' ||'''boardnum''' ||'''wl0_corerev''' ||'''cpu model''' ||'''boot_ver''' ||'''pmon_ver''' ||
||WRT300N v1.0 ||     0x10 ||  0x0472 ||      0x0010 ||       0 ||  42 ||       11 || BCM3302 V0.6 ||  v3.9 ||  CFE 4.81.17.0 ||
'''How to install OpenWRT'''

 . Precompiled RedBoot available at http://davidkra.net/downloads2.html, skip to step 10 if you use it.
[[BR]]Step 1: Get Linksys WRT300N v2.00.20 sources[[BR]][[BR]] Step 2: Untar sources and go to sources directory.[[BR]][[BR]] Step 3: Get this toolchain: ftp://ftp.ges.redhat.com/private/gnupro-xscale-030422/i686-pc-linux-gnulibc2.2-x-xscale-elf.tar.Z[[BR]][[BR]][[BR]] Step 4: mkdir gnutools && mv *xscale-elf.tar.Z gnutools && cd gnutools[[BR]][[BR]] Step 5: Untar toolchain with this command: gunzip2 *xscale-elf.tar.Z; tar xvf *xscale-elf.tar[[BR]][[BR]] Step 6: export PATH=$PWD/H-i686-pc-linux-gnulibc-2.2/bin:$PATH && cd ../src/redboot [[BR]][[BR]] Step 7: Edit options/startup_ROMRAM.edl: replace [[BR]][[BR]]

{{{
cdl_option CYGOPT_REDBOOT_FIS {
    user_value 0
}; }}}
with:

{{{
cdl_option CYGOPT_REDBOOT_FIS {
    user_value 1
}; }}}
and replace:

{{{
cdl_component CYGSEM_REDBOOT_FLASH_CONFIG {
    user_value 0
};}}}
with:

{{{
cdl_component CYGSEM_REDBOOT_FLASH_CONFIG {
    user_value 1
};}}}
Step 8: 'make' [[BR]][[BR]] Step 9: Setup a TFTPd or HTTPd, copy build/wrt300n/install/bin/redboot.bin to your filedir for your server[[BR]][[BR]] Step 10: Get into RedBoot ( Read this http://www.nslu2-linux.org/wiki/HowTo/ReflashUsingRedbootAndTFTP , serial console preferred), type:[[BR]][[BR]]

{{{
(only if via serial console) ether
ip -h {yourIP}
load -r -b 0x70000 -m (choose tftp or http, i'll use http) http /redboot.bin
fis write -f 0x50060000 -b 0x70000 -l 0x4d254 //possible typos: length and flash address. if it doesn't work, first try -l 0x4fd00 and if it still doesn't work, try -f 0x50000000
reset
}}}
Step 11: Get http://downloads.openwrt.org/kamikaze/7.09/ixp4xx-2.6/openwrt-ixp4xx-2.6-squashfs.img and http://downloads.openwrt.org/kamikaze/7.09/ixp4xx-2.6/openwrt-wrt300nv2-2.6-zImage , rename the first to wrt.img, second to wrt,zI. put them into your filedir for your server [[BR]][[BR]] Step 12: Get into RedBoot, again: type:

{{{
fis init
(only if via serial console) ether
ip -h {yourip}
load -r -b 0x70000 -m {http,tftp} http /wrt.zI
fis create kernel
load -r -b 0x70000 -m {http,tftp} http /wrt.img
fis create rootfs
}}}
Step 13: Almost done :-3 , final command in RedBoot:  {{{ fis load kernel }}} [[BR]][[BR]]Step 14. DONE[[BR]][[BR]][[BR]]

If you want to have your box auto-bootable, run 'fconfig boot_script', substitute false with true and enter:

{{{
ether
fis load kernel
exec
}}}
 . Set Timeout to something bigger than 1.'''OpenWRT boot log'''
{{{
Uncompressing Linux................................................................. done, booting the kernel.
Linux version 2.6.21.6 (nbd@ds10) (gcc version 4.1.2) #2 Sun Sep 30 20:44:34 CEST 2007
CPU: XScale-IXP42x Family [690541f1] revision 1 (ARMv5TE), cr=000039ff
Machine: Linksys WRT300N v2
Memory policy: ECC disabled, Data cache writeback
CPU0: D VIVT undefined 5 cache
CPU0: I cache: 32768 bytes, associativity 32, 32 byte lines, 32 sets
CPU0: D cache: 32768 bytes, associativity 32, 32 byte lines, 32 sets
Built 1 zonelists.  Total pages: 4064
Kernel command line: root=/dev/mtdblock2 rootfstype=squashfs,jffs2 noinitrd console=ttyS0,115200 init=/etc/preinit
PID hash table entries: 64 (order: 6, 256 bytes)
Dentry cache hash table entries: 2048 (order: 1, 8192 bytes)
Inode-cache hash table entries: 1024 (order: 0, 4096 bytes)
Memory: 16MB = 16MB total
Memory: 14172KB available (1788K code, 167K data, 76K init)
Mount-cache hash table entries: 512
CPU: Testing write buffer coherency: ok
NET: Registered protocol family 16
IXP4xx: Using 16MiB expansion bus window size
PCI: IXP4xx is host
PCI: IXP4xx Using direct access for memory space
PCI: bus0: Fast back to back transfers enabled
dmabounce: registered device 0000:00:01.0 on pci bus
Time: OSTS clocksource has been installed.
NET: Registered protocol family 2
IP route cache hash table entries: 1024 (order: 0, 4096 bytes)
TCP established hash table entries: 512 (order: 0, 4096 bytes)
TCP bind hash table entries: 512 (order: -1, 2048 bytes)
TCP: Hash tables configured (established 512 bind 512)
TCP reno registered
NetWinder Floating Point Emulator V0.97 (double precision)
squashfs: version 3.0 (2006/03/15) Phillip Lougher
Registering mini_fo version $Id$
JFFS2 version 2.2. (NAND) (C) 2001-2006 Red Hat, Inc.
io scheduler noop registered
io scheduler deadline registered (default)
IXP4xx Watchdog Timer: heartbeat 60 sec
Serial: 8250/16550 driver $Revision: 1.90 $ 2 ports, IRQ sharing disabled
serial8250.0: ttyS0 at MMIO 0xc8001000 (irq = 13) is a XScale
IXP4XX Q Manager 0.2.1 initialized.
IXP4XX NPE driver Version 0.3.0 initialized
ixp_crypto: No HW crypto available
IXP4XX-Flash.0: Found 1 x16 devices at 0x0 in 16-bit bank
 Amd/Fujitsu Extended Query Table at 0x0040
number of CFI chips: 1
cfi_cmdset_0002: Disabling erase-suspend-program due to code brokenness.
Searching for RedBoot partition table in IXP4XX-Flash.0 at offset 0x3f0000
5 RedBoot partitions found on MTD device IXP4XX-Flash.0
Creating 5 MTD partitions on "IXP4XX-Flash.0":
0x00000000-0x00080000 : "RedBoot"
0x00080000-0x00170000 : "kernel"
0x00170000-0x00290000 : "rootfs"
0x00260000-0x00290000 : "rootfs_data"
0x00290000-0x003f0000 : "unallocated"
0x003f0000-0x00400000 : "FIS directory"
i2c /dev entries driver
nf_conntrack version 0.5.0 (128 buckets, 1024 max)
ip_tables: (C) 2000-2006 Netfilter Core Team
TCP westwood registered
NET: Registered protocol family 1
NET: Registered protocol family 17
802.1Q VLAN Support v1.8 Ben Greear <greearb@candelatech.com>
All bugs added by David S. Miller <davem@redhat.com>
XScale DSP coprocessor detected.
ixp4xx_mac driver 0.3.1: eth0 on NPE-B with PHY[-1] initialized
ixp4xx_mac driver 0.3.1: eth1 on NPE-C with PHY[1] initialized
drivers/rtc/hctosys.c: unable to open rtc device (rtc0)
VFS: Mounted root (squashfs filesystem) readonly.
Freeing init memory: 76K
Warning: unable to open an initial console.
- preinit -
jffs2 not ready yet; using ramdisk
mini_fo: using base directory: /
mini_fo: using storage directory: /tmp/root
- init -
init started:  BusyBox v1.4.2 (2007-09-29 10:12:09 CEST) multi-call binary
Please press Enter to activate this console. eth0: NPE-B not running
eth0: NPE-B not running
PPP generic driver version 2.4.2
wlan: 0.8.4.2 (svn r2568)
ath_hal: module license 'Proprietary' taints kernel.
ath_hal: 0.9.30.13 (AR5210, AR5211, AR5212, AR5416, RF5111, RF5112, RF2413, RF5413, RF2133, REGOPS_FUNC)
ath_rate_minstrel: Minstrel automatic rate control algorithm 1.2 (svn r2568)
ath_rate_minstrel: look around rate set to 10%
ath_rate_minstrel: EWMA rolloff level set to 75%
ath_rate_minstrel: max segment size in the mrr set to 6000 us
wlan: mac acl policy registered
ath_pci: 0.9.4.5 (svn r2568)
PCI: enabling device 0000:00:01.0 (0340 -> 0342)
irq 25: nobody cared (try booting with the "irqpoll" option)
handlers:
[<bf089258>]
Disabling IRQ #25
MadWifi: unable to attach hardware: 'Hardware didn't respond as expected' (HAL status 3)
jffs2: Too few erase blocks (3)
BusyBox v1.4.2 (2007-09-29 10:12:09 CEST) Built-in shell (ash)
Enter 'help' for a list of built-in commands.
  _______                     ________        __
 |       |.-----.-----.-----.|  |  |  |.----.|  |_
 |   -   ||  _  |  -__|     ||  |  |  ||   _||   _|
 |_______||   __|_____|__|__||________||__|  |____|
          |__| W I R E L E S S   F R E E D O M
 KAMIKAZE (7.09) -----------------------------------
  * 10 oz Vodka       Shake well with ice and strain
  * 10 oz Triple sec  mixture into 10 shot glasses.
  * 10 oz lime juice  Salute!
 ---------------------------------------------------
root@OpenWrt:/# }}}
'''Hardware hacking'''

'''Opening the case'''

Pull off the blue Cover Plates on top and bottom of the Device, pull off the black Front cover and remove the 4 Screws in Bottom.

'''Debug Mode'''

''' '''To enable Debug Mode, log on to your router and type: http://you.rro.ute.rip/setup.cgi?todo=debug . Actually I don't know what happens to the router after enabling, but now i'm auditing the code.

'''Using ping to run commands'''

Like with other Linksys routers, it's possible to run system commands using "ping"; for instance, entering "; reboot" (without quotation marks) in the "ping" tool will reboot the router. //Doesn't work with 2.00.20

'''Recovering from a bad flash'''

To recover from a bad flash, issue these commands in RedBoot (flashing to linksys fw, assuming you already downloaded it.):

{{{
load -r -b 0x70000 -m (choose between 'http' or 'tftp', assuming http, default tftp) http -h 192.168.0.9 (change this to your ip) /wrt300n.bin
fis write -f 0x50000000 -b 0x70000 -l 0x3fffff}}}
'''WRT300N v2 Serial Console'''

There aren't many connector slots on the board. The serial console (JP1) is just above the flash chip on the same side as the power connector. Console speed is 115200,8n1

 . () Vcc () RX () TX () GND
----
 . CategoryModel
The console connector for the WRT300N v2 uses TTL voltage. Thus it cannot be directly connected to a PC RS232 port (you may fry your WRT300N v2 if you do so). It requires level shifting (by the use of MAX3232 component for example). Details about such a modified cable are widely available. Among other places you can find them at the WRT54G (linux) pages.

----
'''WRT300N v2 PCB's'''
attachment:wrt300nv2_side1.jpg



----
