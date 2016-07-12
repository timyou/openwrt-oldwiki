#pragma section-numbers off
[[TableOfContents]]

= Status =

= Hardware Info =
 * TI AR7 chipset
 * WLAN: TI TNETW1130GVF
 * 32 Mb RAM
 * 4 Mb Flash
 * built-in ADSL Modem
 * CPU: TNETD7300AGDW (AR7) @ 150 Mhz
 * Serial port

= Bootloader =
EVA bootloader (based on ADAM2?)

= Serial console access =

= Installing OpenWrt =

== Building OpenWrt ==

== Flashing your OpenWRT image ==

Once the image has been compiled, it is time to write it to the router's flash memory. This will be done through an FTP connection, during which the image will be transferred from the host to the router and then written into the flash. In order to do that, follow the steps below:

 * Reboot your router and activate the bootloader

 * Connect from your computer to the router through ftp:
{{{
  user@host:~$ ftp 192.168.178.1
}}}

 * Enter the username {{{adam2}}} and password {{{adam2}}} when prompted

 * Once logged in to the router, enter the following sequence of FTP commands:

{{{
  binary
  quote MEDIA FLSH
  passiv
  put </openwrt-image/folder>
  put </openwrt-image/folder>/openwrt-EVA-squashfs.bin mtd1
  quote REBOOT
  quit
}}}

=== Example: FTP session log ===

The following is an example of the terminal output during a typical image flashing process:

{{{
dpm@orthanc:~$ ftp 192.168.178.1
Connected to 192.168.178.1.
220 ADAM2 FTP Server ready
Name (192.168.178.1:dpm): adam2
331 Password required for adam2
Password:
230 User adam2 successfully logged in
Remote system type is AVM.
ftp> binary
200 Type set to BINARY
ftp> quote MEDIA FLSH
200 Media set to MEDIA_FLASH
ftp> passiv
Passive mode on.
ftp> put /home/dpm/op
openwrt-EVA-jffs2-128k.bin  openwrt-EVA-squashfs.bin
openwrt-EVA-jffs2-64k.bin   
ftp> put /home/dpm/openwrt-EVA-squashfs.bin mtd1
local: /home/dpm/openwrt-EVA-squashfs.bin remote: mtd1
227 Entering Passive Mode (192,168,178,1,6,122)
150 Opening BINARY data connection
226 Transfer complete
1769476 bytes sent in 14.99 secs (115.2 kB/s)
ftp> quote REBOOT
221 Thank you for using the FTP service on ADAM2
ftp> quit
221 Goodbye.
}}}

== Firmware images and configs ==

CategoryModel CategoryAR7Device
