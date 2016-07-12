## Please add only OpenWrt and WRT300N related things to this page! Thanks.
'''Linksys WRT300N'''

'''Identification by S/N'''

Useful for identifying shrinkwrapped units. The '''S/N''' can be found on the box, below the UPC barcode.
||||<style="text-align: center;"> (!) '''Please contribute to this list.''' (!) ||||<style="text-align: center;">'''!OpenWrt''' ||
||'''Model''' ||<style="text-align: center;"> '''S/N''' ||<style="text-align: center;">  '''Stable[[BR]]White Russian''' ||<style="text-align: center;">  '''Development[[BR]]Kamikaze''' ||
||WRT300N v1.0 ||<style="text-align: center;"> CNP01 || ( ) || ( ) ||
||WRT300N v2.0 ||<style="text-align: center;"> SNP00 || ( ) || ( ) ||


'''WRT300N v1.0'''

The WRT300N v1.0 is based on the Broadcom 4704 cpu. I guess it has about 300MHz. It has 4 MB flash and 32 MB SDRAM. The wireless NIC is a Broadcom Cardbus card with BCM4329 Chipset.  The switch is an Broadcom BCM5325 FKQMG.

'''WRT300N v2.0'''

The WRT300N v2.0 is based on the Intel IXP420 cpu which is part of the IXP425 family. The cpu runs at 266Mhz.  It has 4Mb of flash and 16Mb of RAM. It has a Marvell 88E6060 switch chip. The wireless is provided by a mini-pci card containing an ar5416 MAC. It is running linux out of the box.

'''Table summary'''

How to get info:

 * board info: {{{nvram show | grep board | sort}}}[[BR]]
 * cpu model: {{{grep cpu /proc/cpuinfo}}}
||'''Model''' ||'''boardrev''' ||'''boardtype''' ||'''boardflags''' ||'''boardflags2''' ||'''boardnum''' ||'''wl0_corerev''' ||'''cpu model''' ||'''boot_ver''' ||'''pmon_ver''' ||
||WRT300N v1.0 ||     0x10 ||  0x0472 ||      0x0010 ||       0 ||  42 ||       11 || BCM3302 V0.6 ||  v3.9 ||  CFE 4.81.17.0 ||
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
