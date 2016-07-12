/!\ ~+'''WARNING'''+~ '''THIS GUIDE IS CURRENTLY WORK IN PROGRESS!'''

OpenWrtDocs [[TableOfContents]]

= Overview =

You will find here information about how to recover AR7 based devices which don't boot correctly. The general ideas apply perfectly to other systems as well but the details will be different.

The devices we focus on here have flash memory as permanent storage only. Once powered up the processor starts executing code from a predefined point in the flash. This could be directly the system you finally want to run but it usually isn't. Usually there is an small "program" called boot loader that is run first. And the boot loader sets up the system to run the final operating system. The reason for that is that the boot loader provides ways to 'change' the the final operating system by reflashing the parts of the flash where itself is not on.

... to be finished.

Apart from the operating system and the boot loader it is common to have a part on flash where variables are stored, like "variable_name=value".

Anyway, a good boot loader also provides a way to provide arguments to the system which may influence it. With Linux (at least) this is called the 'kernel command line'. What you can put on it is very broad and can be read in the Linux kernel documentation. The important part: it is possible to influence in many stages how the system is brought up. This way you can start a system that would otherwise not boot through.

The kernel image may carry a default command line, and with OpenWRT it does so. On PCs it is usually the boot loader that provides the defaults. The AR7 specific kernel start-up code even modifies the command line from within the kernel: it reads from the flash variables the serial console settings and adds up a corresponding part like "console=ttyS0,38400n8".

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

PSPBoot has a "help" command that shows a list of commands. What "help boot" does not reveal is that you actually can provide a kernel command line with "boot". E.g. "boot rootfstype=squashfs init=/etc/preinit". The image default command line does get used (I'm not sure if this "image default" is loaded from the kernel itself or the boot loader...).

To see the default just boot normally, it gets shown soon in the normal kernel messages. Apart from the "console=..." stuff (see Overview above), you may provide what the kernel normally sees.

-- RobertSiemer [[DateTime(2008-04-13T20:57:16Z)]]

= Restoring the original Firmware =
If you have trouble flashing the firmware back via ADAM2, then just download DSL-G604T_2.00B07.AU_20060901.exe from dlink.com.au.

When executing it under Windows, just follow the instructions and click the "Corrupted Image mode" in the first window.

After that you can flash with the correct firmware via web-interface. It worked for my DSL-G684T, at least.
