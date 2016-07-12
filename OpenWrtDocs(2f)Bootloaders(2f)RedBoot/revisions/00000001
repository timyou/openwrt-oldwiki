= RedBoot =
RedBoot is an open source application that uses the eCos real-time operating system Hardware Abstraction Layer to provide bootstrap firmware for embedded systems.

RedBoot allows download and execution of embedded applications via serial or Ethernet, including embedded Linux and eCos applications. It provides debug support in conjunction with GDB to allow development and debugging of embedded applications. It also provides an interactive command line interface to allow management of the Flash images, image download, RedBoot configuration, etc., accessible via serial or ethernet. For unattended or automated startup, boot scripts can be stored in Flash allowing for example loading of images from Flash, hard disk, or a TFTP server.

== Configuration ==
The RedBoot configuration is stored as ordered pairs in an mtd block.
=== Within OpenWrt ===
The fconfig package can read from and write to the RedBoot.  To determine which block to use, look at the output of {{{dmesg}}} or {{{cat /proc/mtd
}}}, or listing each block with {{{fconfig}}}, e.g. {{{fconfig -l -d /dev/mtdX}}}.  The configuration has either a magic number or a checksum, so provided the mtd block has already been initialized, the command will only work on a block with a RedBoot configuration.

To list all ordered pairs, use this:
{{{fconfig -l -d /dev/mtdX}}}

To read a single ordered pair, use this:
{{{fconfig -r -d /dev/mtd3 -n bootp}}}

To write an ordered pair, do this:
{{{fconfig -w -d /dev/mtd3 -n bootp -x TRUE}}}

Caveat: {{{mtd}}} and the library it uses might not let you write to that mtd device.  The lock is a software lock, implemented to prevent the mtd block following the RedBoot config from being erased as the config spans only a partial flash erase block.  There is a patch that removes this limitation, but it requires replacing the kernel.

=== Within RedBoot ===
RedBoot, itself, also uses the {{{fconfig}} command, albeit a bit differently.

{{{
RedBoot> fconfig    //Press enter//
Run script at boot: true    //Press enter//
Boot script:
.. fis load -l vmlinux.bin.l7
.. exec
Enter script, terminate with empty line
>> fis load -l linux    //Enter command and press enter//
>> exec    //Enter command and press enter//
>>    //Press enter//
Boot script timeout (1000ms resolution): 10    //Press enter//
Use BOOTP for network configuration: false    //Press enter//
Gateway IP address:    //Press enter//
Local IP address: 192.168.1.254    //Press enter//
Local IP address mask: 255.255.255.0    //Press enter//
Default server IP address:    //Press enter//
Console baud rate: 9600    //Press enter//
GDB connection port: 9000    //Press enter//
Force console for special debug messages: false    //Press enter//
Network debug at boot time: false    //Press enter//
Update RedBoot non-volatile configuration - continue (y/n)? y    //Enter 'y' and press enter//
… Erase from 0xa87e0000-0xa87f0000: .
… Program from 0×80ff0000-0×81000000 at 0xa87e0000: .
}}}
=== Configuration variables ===
|| value               || description                                 || reasonable setting ||
|| boot_script         || Use a boot script to boot the device?       || true               ||
|| boot_script_data    || The script                                  || .. fis load -l vmlinux.bin.l7 .. exec ||
|| boot_script_timeout || How long to wait before booting; boot_wait  || 3 ||
|| bootp               || Obtain an IP address from bootp?            || false ||
|| bootp_my_gateway_ip || || 0.0.0.0 ||
|| bootp_my_ip_address || IP address to listen on for telnet connections? || 192.168.1.1 ||
|| bootp_my_ip_mask    || Subnet mask of above address                    || 255.255.255.0 ||
|| bootp_server_ip     ||                                                 || 0.0.0.0 ||
|| console_baud_rate   || Baud rate of the serial console                 || 9600 ||
|| gdb_port            || Port to listen on for a telnet connection       || 9000 ||
|| info_console_force  || || false ||
|| net_debug           || || false ||


== Connecting to RedBoot ==
RedBoot supports an internal serial connection and telnet sessions, though telnet sessions aren't always enabled (see above sections for how to enable it).

The default telnet login seems to be 192.168.1.254:9000, and serial connections might use 9600 baud, 8 bit, no parity, no flow control.

For both telnet and serial, reset the device.  RedBoot needs to receive Ctrl+c to pause the boot process.  For telnet connections, once a connection is established following the reset (a few seconds), hit Ctrl+c.  For serial connections, hit Ctrl+c until you see this:
{{{
== Executing boot script in 8.530 seconds - enter ^C to abort
^C
RedBoot>
}}}

The {{{-v}}} flag increased verbosity.
