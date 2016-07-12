#pragma section-numbers off
[[TableOfContents]]
= Actiontec GT701-WG =
The [http://www.actiontec.com Actiontec] [wiki:SeattleWireless:ActiontecGT701 GT701-WG]
is a TI AR7-based device. Thus ["AR7Port"] is compatible with these devices.
This model is distributed by [http://www.qwest.com Qwest] as their current modem
of choice.

== Flash Map ==
||partition||start||end||description||
||mtd0||`0x900d0000`||`0x903e0000`||squashfs filesystem||
||mtd1||`0x90010000`||`0x900d0000`||kernel||
||mtd2||`0x90000000`||`0x90010000`||["ADAM2"]||
||mtd3||`0x903f0000`||`0x90400000`||ADAM2 environment variables followed by `config.xml`||
||mtd4||`0x903e0000`||`0x903f0000`||unknown/unused (32 zero bits followed entirely by ones)||

The physical order of these partitions is:
 1. mtd2
 1. mtd1
 1. mtd0
 1. mtd4
 1. mtd3

== Installing OpenWrt ==
List of commands to be issued before flashing using the FTP method as directed in ["OpenWrtDocs/InstallingAR7"]
 1. create mtd5 spanning mtd1-mtd0 (`quote SETENV mtd5,0x90010000,0x903e0000`).
 2. set the `MAC_PORT` variable to `0` (`quote SETENV MAC_PORT,0`).
 3. flash to mtd5 instead of mtd4

== Restoring Qwest Firmware ==
First obtain and extract
http://www.qwest.com/internethelp/modems/gt701/docs/gt701_wg_qw04_3_60_2_0_6_3_recovery.zip.
The files you need are in the "gt701-wg qw04-3.60.2.0.6.3_recovery/image" directory.

During the ["ADAM2"] access window (approx 2-7 seconds after power up) connect to 192.168.0.1 with a console-based FTP client.
The following assumes you're in the previously specified directory. Both the username
and password are "adam2".

{{{
$ ftp 192.168.0.1
Connected to 192.168.0.1.
220 ADAM2 FTP Server ready.
Name (192.168.0.1:user): adam2
Password:
230 User adam2 successfully logged in.
Remote system type is UNIX.
ftp> binary
200 Type set to I.
ftp> quote UNSETENV mtd5
200 UNSETENV command successful
ftp> quote UNSETENV MAC_PORT
200 UNSETENV command successful
ftp> quote MEDIA FLSH
200 Media set to FLSH.
ftp> put nsp.ar7wrd.squashfs.img "nsp.ar7wrd.squashfs.img mtd0"
local: nsp.ar7wrd.squashfs.img remote: nsp.ar7wrd.squashfs.img mtd0
502 Command not implemented - Try HELP.
227 Entering Passive Mode (192,168,0,1,4,45).
150 Opening BINARY mode data connection for file transfer.
100% |*************************************|  1940 KB   82.54 KB/s    00:00 ETA
226 Transfer complete.
1986560 bytes sent in 00:23 (81.18 KB/s)
ftp> put ram_zimage_pad.ar7wrd.nsp.squashfs.bin "ram_zimage_pad.ar7wrd.nsp.squashfs.bin mtd1"
local: ram_zimage_pad.ar7wrd.nsp.squashfs.bin remote: ram_zimage_pad.ar7wrd.nsp.squashfs.bin mtd1
227 Entering Passive Mode (192,168,0,1,4,45).
150 Opening BINARY mode data connection for file transfer.
100% |*************************************|   640 KB   85.43 KB/s    00:00 ETA
226 Transfer complete.
655360 bytes sent in 00:07 (81.14 KB/s)
ftp> quote REBOOT
221-Thank you for using the FTP service on ADAM2.
221 Goodbye.
ftp> ^D
$ 
}}}

== Serial Port ==
Information about the serial port can be found at
[wiki:SeattleWireless:ActiontecGT701 SeattleWireless].
It is duplicated here.
{{{
          SoC            |
  Flash                  |
             JP603       |
       # # # # # #       |
_________________________|

       G T R   V
       N X X   C
       D       C
}}}
The serial port needs a level converter chip to be used with a RS232 port.
The logic level is 3.3v. The parameters are `38400-N-1`.

== Misc ==
http://forum.openwrt.org/viewtopic.php?id=2446
----
CategoryModel
