= Running Kamikaze images under qemu =

The Kamikaze x86 images run directly under qemu; all you need to do is to grow them
to the full size that the partition table defines. This will be roughly
20MB, since the default configuration is 4MB for the boot partition and 16MB
for the data partition, but will be a bit larger than this due to rounding
up to whole numbers of cylinders.

Work out the exact number of sectors that the image should be by looking at
the partition table, and multiplying the highest cylinder number by the
sectors per cylinder:

{{{
$ fdisk openwrt-x86-2.6-jffs2-128k.image
You must set cylinders.
You can do this from the extra functions menu.

Command (m for help): p

Disk openwrt-x86-2.6-jffs2-128k.image: 0 MB, 0 bytes
16 heads, 63 sectors/track, 0 cylinders
Units = cylinders of 1008 * 512 = 516096 bytes

                           Device Boot      Start         End      Blocks   Id System
openwrt-x86-2.6-jffs2-128k.image1   *           1           9        4504+  83 Linux
openwrt-x86-2.6-jffs2-128k.image2              10          42       16600+  83 Linux

Command (m for help): q

$ bc
bc 1.06
Copyright 1991-1994, 1997, 1998, 2000 Free Software Foundation, Inc.
This is free software with ABSOLUTELY NO WARRANTY.
For details type `warranty'.
42*1008
42336

$ dd if=/dev/null of=openwrt-x86-2.6-jffs2-128k.image seek=42336
0+0 records in
0+0 records out
0 bytes (0 B) copied, 2.5e-05 seconds, 0 B/s

$ ls -l openwrt-x86-2.6-jffs2-128k.image
-rw-r--r-- 1 yourname yourname 21676032 2007-10-23 11:20
}}}

Now you can boot this image directly:

{{{
$ sudo apt-get install qemu    # for Ubuntu
$ qemu openwrt-x86-2.6-jffs2-128k.image
}}}

Type 'qemu' by itself to get a list of options. Useful ones are '-snapshot'
which keeps your image pristine (writes are made to temporary files); '-k
en-gb' to set the keyboard layout; and '-m 64' to set the available memory
to 64MB (defaults to 128MB)

= Networking =

"User-mode" networking is enabled by default. If you edit
/etc/config/network, set "option proto dhcp", then run "ifup lan", the
br-lan interface will pick up an IP address from an internal private
network, 10.0.2.x.

It then has outbound access to the Internet via your host machine. You won't
be able to send an ICMP ping (qemu would need to run as root to provide
that), but you can open TCP connections and exchange UDP packets. For
example, "ipkg update" works as expected.

See http://www.gnome.org/~markmc/qemu-networking.html and
http://www.h7.dion.ne.jp/~qemu-win/HowToNetwork-en.html for information on
setting up more complex networking scenarios with qemu.

= See also =

 * SoekrisPort (for more details about partitioning)
 * [[Generic_x86-HowTo]]
 * [[RunningKamikazeOnVMwareHowTo]]
