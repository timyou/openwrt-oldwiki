== MyLoader ==
MyLoader is the bootloader only seen so far on Compex wireless routers. If you have seen this bootloader on other devices that you own please add them to the bottom of the page. Unlike CFE or Redboot, MyLoader is a menu driven bootloader like the standard one on all adm5120 platforms by Edimax, Sweex and others. There are more details on the standard bootloader available on the midge website: http://midge.vlad.org.ua Below is a set of instructions which can be used to update the bootloader to CFE using the bundle provided for the WP54-WRT. I have tried this on my WP54G-1D but after a few seconds the board freezes.  Also JTAG seems to be a bit odd on these boxes, and as yet I have to get some sensible looking results from it.

{{{
MyLoader version 2.32.0515
System memory: 16MB ram, 4MB flash
Probe Flash Device: 00400000 at bfc00000
Flash Device: Found 1 x16 devices at 0x0 in 16-bit mode
 Amd/Fujitsu Extended Query Table v1.1 at 0x0040
number of CFI chips: 1
Load Firmware
Loading Firmware  CRC error.
Update Firmware (Image Mode)
Mini TFTP Server 1.0 (IP : 192.168.168.1)
Usage (Windows 2000/XP) :
  tftp -i 192.168.168.1 put <filename>
Main Menu
1 - Load Firmware
2 - Load Program
3 - BIOS Setup
4 - Fdisk Utility
5 - Update Flash (Binary Mode)
6 - Update Firmware (Image Mode)
7 - Reboot System
Please select :}}}
As you can see I have pre-broken my image, MyLoader checks the whole image against a CRC before booting. At this point you can select 5, Update Flash which opens a new menu.

{{{
Update Flash (Binary Mode)
1 - Update BIOS
2 - Update System Paramters
3 - Update Board Paramters
4 - Update Partition Table
5 - Update Partition
Please select : }}}
Then select 1 - Update BIOS. You can send any binary file, and it will just overwrite the bootloader.'''Warning -- This will toast your router if you send a bad file.'''

{{{
Update BIOS
Mini TFTP Server 1.0 (IP : 192.168.168.1)
Usage (Windows 2000/XP) :
  tftp -i 192.168.168.1 put <filename>}}}
You then TFTP your file to the router and given any luck you should see:

{{{
Starting the TFTP download from IP (192.168.168.2)...
........
TFTP download completed...
Update BIOS ......................... Done
Update Flash (Binary Mode)
1 - Update BIOS
2 - Update System Paramters
3 - Update Board Paramters
4 - Update Partition Table
5 - Update Partition
Please select : }}}
Escape out of that menu:

{{{
Main Menu
1 - Load Firmware
2 - Load Program
3 - BIOS Setup
4 - Fdisk Utility
5 - Update Flash (Binary Mode)
6 - Update Firmware (Image Mode)
7 - Reboot System
Please select :}}}
Then select 7. This is the point of no return. If you were sensible enough to save a copy of the previous images then continue at your leasure.

{{{
Reboot System
CFE version 1.2.5 for WP54G (32bit,SP,LE,MIPS)
Build Date: Wed Aug 16 09:09:30 SGT 2006 (ttyaw@linux01)
Initializing Arena.
Initializing PCI. [normal]
PCI bus 0 slot 0/0: ADMtek ADM5120 Host Bridge (host bridge)
PCI bus 0 slot 2/0: Atheros product 0x001a (ethernet network, rev 0x01)
Initializing Devices.
CPU type 0x1800B: 175MHz
Total memory: 0x1000000 bytes (16MB)
Total memory used by CFE:  0x80F83000 - 0x80FFFAE0 (510688)
Initialized Data:          0x80FBA824 - 0x80FBCA50 (8748)
BSS Area:                  0x80FBCA50 - 0x80FBDAE0 (4240)
Local Heap:                0x80FBDAE0 - 0x80FFDAE0 (262144)
Stack Area:                0x80FFDAE0 - 0x80FFFAE0 (8192)
Text (code) segment:       0x80F83000 - 0x80FBA115 (225557)
Boot area (physical):      0x00F42000 - 0x00F82000
Relocation Factor:         I:E1383000 - D:E1383000
CFE>}}}
At which point I can enter commands for a few seconds, but after that it freezes for me.
