= Airlink AR335W/AR430W WIP=

Those two routers have almost identical hardware. Both are based on an Atheros System on Chip (SoC) and both have limited Redboot. 


[[ImageLink(AR335W,width=width[,height=height]])]]

= Hardware =
== Info ==
||<tablewidth="460px" tableheight="345px">'''Architecture''' ||MIPS 5KEc ? ||
||'''Vendor''' || ||
||'''Bootloader''' ||!RedBoot ||
||'''System-On-Chip''' ||Atheros AR2317/AR2318 ||
||'''CPU Speed''' ||182 MHz ||
||'''Flash size''' ||4 MB ||
||'''RAM''' ||16 MB ||
||'''Switch''' ||IC+ IP175C||
||'''Wireless''' ||Integrated Atheros 802.11b/g (*also Atheros™ Super G™: 108 Mbps on AR430W) ||
||'''Ethernet''' ||5x RJ45 (1x Wan , 4x Lan)||
||'''USB''' ||No ||
||'''Serial''' ||Yes ||
||'''JTAG''' ||No ||
 * 5V power supply
 * Antenna


= Installing OpenWrt with RedBoot =
'''You will need to flash modified Redboot before you continue.'''

Once you have gained access to [:RedBoot:!RedBoot] either by telnet or the serial console you can install [:OpenWrt:!OpenWrt] with the following method.

You have to download two files (right click and save as).

 * [http://downloads.openwrt.org/kamikaze/7.09/atheros-2.6/openwrt-atheros-2.6-vmlinux.lzma openwrt-atheros-2.6-vmlinux.lzma]
 * [http://downloads.openwrt.org/kamikaze/7.09/atheros-2.6/openwrt-atheros-2.6-root.squashfs openwrt-atheros-2.6-root.squashfs]
Copy openwrt-atheros-2.6-vmlinux.lzma and openwrt-atheros-2.6-root.squashfs to /tftpboot/ and flash them like this:

{{{
^C
DD-WRT> load -r -b %{FREEMEMLO} openwrt-atheros-2.6-vmlinux.lzma
Using default protocol (TFTP)
Raw file loaded 0x80041000-0x800f0fff, assumed entry at 0x80041000
DD-WRT> fis init}}}
The values for the -e and -r switches in the 'fis create' !RedBoot command below is the Kernel entry point. Do not change this value.

{{{
RedBoot> fis create -e 0x80041000 -r 0x80041000 vmlinux.bin.l7
An image named 'vmlinux.bin.l7' exists - continue (y/n)? y
... Erase from 0xa8730000-0xa87e0000: ...........
... Program from 0x80041000-0x800f1000 at 0xa8730000: ...........
... Erase from 0xa87e0000-0xa87f0000: .
... Program from 0x80ff0000-0x81000000 at 0xa87e0000: .
}}}
"fis free" will print the first and last free block

{{{
DD-WRT> fis free
      0xA80F0000 .. 0xA87E0000
}}}
Now do the math (last - first, cause you need the difference)

{{{
server:~# bc
obase=16
ibase=16
A87E0000 - A80F0000
6F0000
}}}
Replace ''0xLENGTH'' with the value above (0x006F0000 in my case) and flash the the rootfs:

{{{
DD-WRT> load -r -b %{FREEMEMLO} openwrt-atheros-2.6-root.squashfs
Using default protocol (TFTP)
|
Raw file loaded 0x80041000-0x80200fff, assumed entry at 0x80041000
RedBoot> fis create -l 0xLENGTH rootfs
An image named 'rootfs' exists - continue (y/n)? y
... Erase from 0xa8030000-0xa8730000: ................................................................................................................
... Program from 0x80041000-0x80741000 at 0xa8030000: ..............................................................................................................
... Erase from 0xa87e0000-0xa87f0000: .
... Program from 0x80ff0000-0x81000000 at 0xa87e0000: .

now type fconfig and configure the bootscript to
Run script at boot: true 
Enter script, terminate with empty line 
>> fis load -l vmlinux.bin.l7
>> exec 
>><--- just press enter 
Boot script timeout (1000ms resolution): 5 
Use BOOTP for network configuration: false <--- just press enter 
Gateway IP address: <--- just press enter 
Local IP address: 192.168.1.1 
Local IP address mask: 255.255.255.0 
Default server IP address: 192.168.1.254 
Console baud rate: 9600 
GDB connection port: 9000 
Force console for special debug messages: false  <--- just press enter 
Network debug at boot time: false  <--- just press enter 
Update RedBoot non-volatile configuration - continue (y/n)? y 
... Erase from 0xbffe0000-0xbfff0000: . 
... Program from 0x80ff0000-0x81000000 at 0xbffe0000: . 
DD-WRT>reset

}}}

If everything is okay, then it will now look like this:
