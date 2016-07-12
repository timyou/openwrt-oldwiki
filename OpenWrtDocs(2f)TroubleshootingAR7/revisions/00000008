/!\ ~+'''WARNING'''+~ '''THIS GUIDE IS CURRENTLY WORK IN PROGRESS!'''

OpenWrtDocs [[TableOfContents]]

= Troubleshooting AR7 device with ADAM2 bootloader =
== Obtaining ADAM2 IP ==
=== by device model name ===
See here ["OpenWrtDocs/InstallingAR7#head-c4b218f29067ebd2e50fb42617c6a9f4228834d4"] (NOTE: default ["ADAM2"] IP shown, it can be changed)

=== by telnet with original firmware ===
You can sniff ADAM2 IP in advance (before you try to re-flash device) and write it down. Telnet to your device with original firmware, use "root" as login, and your device's admin password ("admin" by default), than

{{{
# cat /proc/ticfg/env | grep my_ipaddress
}}}
You should see something like this:

{{{
my_ipaddress    10.8.8.8
}}}

If it's not displayed (or just to change it), you can set it with the command:
{{{
# echo "my_ipaddress 192.168.0.1" > /proc/sys/dev/adam2/environment
}}}

NOTE: some devices comes with disabled telnet, you can't use this method with them

=== by serial console ===
Another method is using serial console and ADAM2 itself to find out it's IP

Attach serial console, power up device, console will show something like this:

{{{
ADAM2 Revision 0.22.02
(C) Copyright 1996-2003 Texas Instruments Inc. All Rights Reserved.
(C) Copyright 2003 Telogy Networks, Inc.
Usage: setmfreq [-d] [-s sys_freq, in MHz] [cpu_freq, in MHz]
Memory optimization Complete!
Adam2_AR7RD >
Press any key to abort OS load, or wait 3 seconds for OS to boot...
}}}
Press a key within specified period, and issue "printenv" command. You will see:

{{{
Adam2_AR7RD > printenv
---skipped---
my_ipaddress          10.8.8.8
---skipped---
Adam2_AR7RD >
}}}
see here for more details: http://www.seattlewireless.net/index.cgi/ADAM2

=== by adam itself ===
adam2 listen UDP port 5035. It is possible to send packet 192.168.0.2:5035 > 255.255.255.255:5035 00001602 01000000 00000000 00000000

and get responce like:

10.8.8.8:5035 > 192.168.0.2:5035 00001602 02000000 0808080a 00000000

0a080808 - IP address of ADAM 160202 - ADAM' version (0.22.02 in this example). Adam send info only if version in requesting package the same as it's native version (i.e. 0.22.XX for example).

For version 0.22 it is possible to use "adam2app.exe" TI service utility http://star.oai.pp.ru/jtag/adam2-oleg.zip

=== by opening ADAM2.bin ===
If you have saved your ADAM2 bootloader you can open it with notepad and scroll to the bottom or find my_ipaddress. This is particularly useful if you are flashing with a JTAG cable after corrupting your ADAM2 and you have downloaded ADAM2 from another source. Normally ADAM2 uses 10.8.8.8 or 192.168.1.1 but it may have DHCPOFFER which means that it will request an IP address from the network DHCP server, obviously if you don't have a DHCP server on your network you won't be able to access ADAM2 via FTP/Telnet

== Restoring mtd3 partition ==
Use telnet to port 21 to access ADAM2, than type in "USER adam2" and hit enter, next type "PASS adam2" and hit enter once more. Full transcript will be like this:

{{{
$ telnet 10.8.8.8 21
Trying 10.8.8.8...
Connected to 10.8.8.8 (10.8.8.8).
Escape character is '^]'.
220 ADAM2 FTP Server ready.
USER adam2
331 Password required for adam2.
PASS adam2
230 User adam2 successfully logged in.
}}}
NOTE: Use correct ADAM2 IP found in previous step instead of 10.8.8.8

Once you logged in, you can issue "GETENV <varname>" to find out value of ADAM2 envirounment variable or "SETENV <varname>,value" to change it. Something like this:

{{{
GETENV mtd0
mtd0                  0x900a0000,0x903e0000
SETENV mtd0,0x900a0000,0x903e0000
200 SETENV command successful
}}}
NOTE: GETENV displays varname and value separated whith spaces, while SETENV requires varname and value to be separated whith comma (","). Additional commas within value is okay.

4 variables is essential for successful operation:
||variable ||default value ||
||mtd0 ||0x900a0000,0x903f0000 ||
||mtd1 ||0x90010000,0x900a0000 ||
||mtd2 ||0x90000000,0x90010000 ||
||mtd3 ||0x903f0000,0x90400000 ||


Alternatively, you can set only mtd3 variable, and then upload entire mtd block. It's a good idea to save all mtd's before you begin to reflash you device. Or mtd3 can be found here: http://mcmcc.bat.ru/dlinkt/restore_mtd3_50xT.rar

= Troubleshooting AR7 device with PSPBoot bootloader =
/!\ To be written...
