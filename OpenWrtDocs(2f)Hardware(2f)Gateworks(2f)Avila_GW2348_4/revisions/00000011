=== Hardware ===
http://www.gateworks.com/images/GW2348_4.JPG

The GW2348-4, is a member of the Gateworks Avila Network Processor family. The GW2348-4 meets the requirements for enterprise and residential network applications. This single board network processor consists of an Intel® IXP425 XScale®  processor operating at 533MHz, 64Mbytes of SDRAM, and 16Mbytes of Flash. Peripherals include four Type III Mini-PCI sockets, two 10/100 Base-TX Ethernet channels, Compact Flash socket, and two RS-232 serial ports for management and debug. Additional features include digital I/O, serial EEPROM, real time clock, voltage and temperature monitor, fan controller, watchdog timer, passive power over Ethernet,  wide input range DC/DC power supply, and extended temperature operation.

== Features ==
 1. Intel® XScale® IXP425 533MHz Processor
 1. 64Mbytes SDRAM
 1. 16Mbytes Flash
 1. Four Type III Mini-PCI Slots
 1. Two 10/100 Base-TX Ethernet Ports
 1.  Compact Flash Socket
 1. Two RS-232 Serial Ports
 1. General Purpose Digital I/O
 1. 1Kbyte Serial EEPROM
 1. Battery Powered Real Time Clock
 1. Voltage and Temperature Monitor
 1. Thermally Activated Fan Controller
 1. Watchdog Timer
 1. User LED and Push-button Reset
 1. Optional Dual Type A USB Host Ports
 1. Passive Power Over Ethernet
 1. Reverse Voltage and Transient Protection
 1. 9 to 48VDC Input Voltage Range
 1. 18W Shared Between Mini-PCI Sockets
 1. 5W Typical Operating Power
 1. -40°C to +85°C Operating Temperature
 1. Software Support for Linux and VxWorks
 1. 1 Year Warranty
== Installing OpenWRT ==
 we need a tftpd server, I use dnsmasq, listening at 192.168.3.1, the default IP for the Gatework Avila is 192.168.3.2

 Plug in the GW2348 power supply while watching the Hyperterminal Window. When you see the line:

{{{
== Executing boot script in 2.500 seconds - enter ^C to abort}}}
 you have 2 and one half seconds to hit CTRL-C. When you do you should see a prompt that looks like this:

{{{
^C
RedBoot>}}}
 At this prompt enter the line:

{{{
fis init -f}}}
 The GW2348 will respond with:

{{{
About to initialize [format] FLASH image system - continue (y/n)?}}}
 As long as you are ready to continue enter a Y to get the following response:

{{{
*** Initialize FLASH Image System
... Erase from 0x50080000-0x50fe0000: ...............................
.....................................................................
.......................
... Unlock from 0x50fe0000-0x51000000: .
... Erase from 0x50fe0000-0x51000000: .
... Program from 0x03fe0000-0x04000000 at 0x50fe0000: .
... Lock from 0x50fe0000-0x51000000: .
RedBoot>
}}}
 Enter the following line: (you may want to refer to the flashing.txt file for this and subsequent lines to enter since they could change in future builds)

{{{
load -r -v -b 0x00800000 openwrt-avila-2.6-zImage}}}
 At this point you will find out for sure if your TFTP server is working correctly. If it isn't you will get something like this:

{{{
Using default protocol (TFTP)
__udp_sendto: Can't find address of server
Can't load 'zImage': some sort of network error
RedBoot>
}}}
 When I got this message it was because I had forgotten to set my TFTP server to use 192.168.3.1 as it's address so it was not seeing the TFTP request coming from the GW2348. I changed the setting and then the reply coming from the GW2348 looked like this:

{{{
Using default protocol (TFTP)
/
Raw file loaded 0x00800000-0x00967c93, assumed entry at 0x00800000
RedBoot>
}}}
 This took several seconds as the zimage file was downloaded to the Gateworks board from my computer. After this completes execute the following command:

{{{
fis create -b 0x00800000 -f 0x050080000 -l 0x00200000 -r 0x00800000 linux}}}
 The response should look like this:

{{{
... Erase from 0x50080000-0x50280000: ................
... Program from 0x00800000-0x00a00000 at 0x50080000: ................
... Unlock from 0x50fe0000-0x51000000: .
... Erase from 0x50fe0000-0x51000000: .
... Program from 0x03fe0000-0x04000000 at 0x50fe0000: .
... Lock from 0x50fe0000-0x51000000: .
RedBoot>
}}}
  Then enter this command:

{{{
fis create -n linux}}}
 You will get a caution message:

{{{
An image named 'linux' exists - continue (y/n)? y
* CAUTION * about to program 'linux'
at 0x50080000..0x501e7c93 from 0x00800000 - continue (y/n)? y
}}}
 The message repeats twice since this is when you are actually overwriting the original version of linux installed on the board. They really want you to be sure and it is wise to reread your command line to be sure that you aren't doing something stupid... but forge ahead... The GW2348 will respond:

{{{
... Unlock from 0x50fe0000-0x51000000: .
... Erase from 0x50fe0000-0x51000000: .
... Program from 0x03fe0000-0x04000000 at 0x50fe0000: .
... Lock from 0x50fe0000-0x51000000: .
RedBoot>
}}}
  Now it is time to TFTP in the rootfs file:

{{{
load -r -v -b 0x00800000 openwrt-ixp4xx-2.6-jffs2-128k.img}}}
 If all is working well the response should look something like this:

{{{
Using default protocol (TFTP)
/
Raw file loaded 0x00800000-0x00d13fff, assumed entry at 0x00800000
RedBoot>
}}}
 When the loading of the root filesystem is complete (it will take a few seconds because it is a large file) you will create several files The first looks like this:

{{{
fis create -b 0x00800000 -f 0x050280000 -l 0x00D20000 ramdisk}}}
 The response from the GW2348 will look like:

{{{
... Erase from 0x50280000-0x50fa0000: ...............................
.....................................................................
.....
... Program from 0x00800000-0x01520000 at 0x50280000: ...............
.....................................................................
.....................
... Unlock from 0x50fe0000-0x51000000: .
... Erase from 0x50fe0000-0x51000000: .
... Program from 0x03fe0000-0x04000000 at 0x50fe0000: .
... Lock from 0x50fe0000-0x51000000: .
}}}
 Programming this block of the flash memory takes quite a while because it is a very large file. 

When it is done we will run the fconfig utility at the RedBoot> prompt. The GW2348's output is shown in regular type. Your entries are shown in italic:

{{{
RedBoot> fconfig
Run script at boot: true
Boot script:
.. fis load ramdisk
.. fis load zimage
.. exec
Enter script, terminate with empty line
>> fis load linux
>> exec
>>
Boot script timeout (100ms resolution): 25
Use BOOTP for network configuration: false
Gateway IP address:
Local IP address: 192.168.3.2
Local IP address mask: 255.255.255.0
Default server IP address: 192.168.3.1
Console baud rate: 115200
GDB connection port: 9000
Force console for special debug messages: false
Network debug at boot time: false
Default network device: npe_eth0
Update RedBoot non-volatile configuration - continue (y/n)? y
... Unlock from 0x50fe0000-0x51000000: .
... Erase from 0x50fe0000-0x51000000: .
... Program from 0x03fe0000-0x04000000 at 0x50fe0000: .
... Lock from 0x50fe0000-0x51000000: .
RedBoot>
}}}
  yoy may now reset the unit:

{{{
reset}}}

----
 CategoryModel ["CategoryIXP4xxDevice"]
