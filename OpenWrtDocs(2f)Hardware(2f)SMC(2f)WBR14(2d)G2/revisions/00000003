#pragma section-numbers off

= SMC WBR14-G2 =

The [http://www.smc.com SMC] [http://www.smc.com/index.cfm?event=viewProduct&localeCode=EN_USA&cid=5&scid=26&pid=1535 WBR14-G2] is an Atheros 2317-based device. (for more information look at ["AtherosPort"])

This device runs Atheros's own bootloader, and VxWorks proprietary OS, which doesn't have network (ethernet) firmware uploading/downloading support, so no boot_wait either. It supports uploads/downloads via serial console (XMODEM).
It also seems that SMC removed the atheros board configuration data from the flash ROM, so it has to be reprogrammed.


== Hardware Info ==

CPU: Atheros AR2317 WiSoC @ 240 Mhz

RAM: PSC A2V64S4OCTP (8MB)

Flash: ST 25P16V6P (2MB)

Ethernet: 5x 10/100 RJ45 Ports (ICPlus PHY)

Wireless: Atheros AR2317 integrated

Other: Reset button, 8 led's, serial and jtag port

=== Serial Console ===

A TTL/RS232 converter is needed to access the serial console of the bootloader.
Default baudrate: 115200 8N1
Pinout: (the first pin is marked with a white arrow on the PCB):
||'''Pin''' ||'''Function''' ||
|| #1 || VCC (+3.3V) ||
|| #2 || TxD ||
|| #3 || RxD ||
|| #4 || Ground (GND) ||
|| #5 || Not connected ||

=== JTAG ===

The JTAG connector (MIPS EJTAG v2.5 compliant) can be found next to the serial connector.
Pinout:
||'''Function''' ||'''Pin''' ||'''Pin''' ||'''Function''' ||
|| TRST_N || #1 || #8 || GND ||
|| TDI || #2 || #9 || GND ||
|| TDO || #3 || #10 || GND ||
|| TMS || #4 || #11 || GND ||
|| TCK || #5 || #12 || GND ||
|| SRST_N || #6 || #13 || Unused ||
|| Unused || #7 || #14 || VCC ||

The unbuffered Xilinx-type cable works perfectly.
For more information see ["OpenWrtDocs/Customizing/Hardware/JTAG_Cable"].

Notice: JTAG might not work "out of the box". If JTAG SPI flash programmers like tjtagspi fail to recognise the CPU (CPU Chip ID: 11111111111111111111111111111111 (FFFFFFFF)), then it may help to short the VCC and TRST_N pins on the JTAG interface. Doing this is DANGEROUS and may cause permanent damage to your board, so do it at your own risk.

=== Default Flash Layout ===

0xbfc00000 - 0xbfc1ffff (128  kbytes): Bootloader
0xbfc20000 - 0xbfc3ffff (128  kbytes): Configuration / NVRAM
0xbfc40000 - 0xbfcbffff (512  kbytes): Web Image
0xbfcc0000 - 0xbfddffff (1152 kbytes): VxWorks OS
0xbfde0000 - 0xbfdeffff (64   kbytes): Customer Area
0xbfdf0000 - 0xbfdfffff (64   kbytes): Boot Settings

== Installing RedBoot ==

=== Testing if RedBoot Works ===

You need at least a serial connection for this to work (JTAG if you screw up something).
Be sure to use software which supports XModem uploads (i used minicom), or alternatively you can do it in a terminal. When the bootloader prints "Starting XModem download ...", you have at most 10 seconds to start the upload. If you're late, the upload will fail, because the loader will send "NAK" response to each packet (no idea why). Don't worry if it doesn't work at first, the loader doesn't modify anything before the full file is uploaded. If you're stuck at an upload spitting NAK-s, just unplug and replug the power cord to the device, and try again. DO NOT unplug the device if any other error occurs during flashing. Chances are that you will brick your router.

Connect serial cable, boot up the device. The boot log is something like
{{{
ar531xPlus rev 0x00000087 boot loader startup...
Flash initialized
SDRAM initialized
Cache initialized

Copy program from 0xbfc00000 to 0x80520000, length 0x0000c56c bytes ... done
Jump to SDRAM 0x80520cb4 [0x10000008, 0x00000000, 0x00000000]
Clear BSS section ... done
Stack: 0x8053e390
Heap: 0x8053e3a0



==================================================================
 Wireless Gateway WG4005E Loader V0.03 build Mar 29 2005 15:25:28
                  Arcadyan Technology Corporation
==================================================================

Flash Found. It is 2MB Flash....

Copying boot params.....DONE
cpuFreq=240000000 sysFreq=60000000 cntFreq=120000000

Press any key to enter command mode ...
}}}

At this point, of course, you will press a key.
Each character you type is a command. When you type the character, you don't have to press enter, the bootloader executes it right away, so be careful and don't make typos.
Pressing "H" brings up the list of available commands.
{{{
[WG4005E Boot]:h
======================
 [U] Upload to Flash
 [E] Erase Flash
 [M] Upload to Memory
 [R] Read from Memory
 [W] Write to Memory
 [T] Memory Test
 [Y] Go to Memory
 [G] Run Runtime Code
 [A] Set MAC Address
 [#] Set Serial Number
 [V] Set Board Version
 [P] Print Boot Params
 [0] ALERT LED Off
 [1] ALERT LED On
 [2] WLAN LEDs Off
 [3] WLAN LEDs On
 [4] Ethernet LED On
 [C] Set Country Code
 [B] Reboot
======================
}}}

You have to test if RedBoot works properly, so an upload to memory instead of flash will do it at first.
Press "M", and when it asks for memory address, type "80041000".
You have 10 seconds to start XModem upload. You can either upload your customized RedBoot loader, or mine. You should upload the ROMRAM version of RedBoot, not the RAM one (bootloader does not support ELF images).
{{{
RAM upload destination: (default:0x80001000) : 0x80041000
Starting XModem download...(press Enter to abort)
CCC
Execute uploaded code? (Y/n)
}}}

Just press "Y". Set your serial port speed temporarily to "9600 8N1".
Wait a few seconds and then type "help". If the RedBoot help appears, then proceed to uploading RedBoot. If it doesn't, it either means that you just had bad luck and it didn't work (unlikely), or that you are in trouble and either you or the loader screwed up something (more likely).

=== Uploading RedBoot ===

At first, you should try the "bdrestore" command, which locates and moves Atheros Board Configuration to a more sensible location (and hopefully prevents RedBoot configuration from overwriting it).
Then, you should tell RedBoot to write itself to the flash ROM.
If it is smaller than 128 kbytes then use
"fis write -b 0x80041000 -f 0xbfc00000 -l 0x00020000"
If it is between 128 and 192 kbytes, use
"fis write -b 0x80041000 -f 0xbfc00000 -l 0x00030000"
If it is bigger than 192 kbytes then you probably need a smaller one, because of the limited amount of flash memory.
("fis write" does not need the flash image system to be initialised)
When the flash programming is done, use the "reset" command and wait.
You should see RedBoot booting instead of the Atheros bootloader.
After RedBoot loaded, use "fconfig -i" and "fis init" to initialise the configuration and images.

To be continued ...

----
 CategoryModel ["CategoryAtherosDevice"]
