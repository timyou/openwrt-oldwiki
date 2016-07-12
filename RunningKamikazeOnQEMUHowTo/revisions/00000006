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

Inside the VGA window, use Ctrl-Alt to release the mouse, and Ctrl-Alt-1/2/3
to switch between guest VGA, qemu monitor (where you can manage qemu
itself), and serial port.

The '-nographic' option disables the VGA window display entirely and redirects
the serial console to stdin/stdout. There are some special key sequences here
for getting access to the monitor - type Ctrl-a h for help on these.

= Networking =

Network access to your image is provided by a virtual NE2000-type network
card in the emulated guest environment. To access this you will need the
''kmod-ne2k-pci'' package, which is included by default in the x86 image.

== User-mode networking ==

"User-mode" networking is enabled by default. Within the guest, if you edit
/etc/config/network, set "option proto dhcp", then run "ifup lan", the
br-lan interface will pick up an IP address from an internal private
network, 10.0.2.x.

It then has outbound access to the Internet via your host machine, which
appears to be a NAT firewall. You won't be able to send an ICMP ping
(qemu would need to run as root to provide that), but you can open TCP
connections and perform DNS lookups. For example, "ipkg update" works as expected. 

No root privileges are needed to run qemu this way. However, if you wish to
allow incoming connections then this has to be done via port forwarding
(see the -redir option), just like on a real NAT firewall.

== Bridged networking ==

A more powerful solution is to bridge your host adaptor's ethernet
directly with the virtual ethernet NIC(s) of your QEMU guest(s). This
gives them full access to your LAN as peers, and can pick up their own
IP addresses using your LAN's existing DHCP server.

To do this involves setting up software bridging on the host, and adding the
'tap' device to this same bridge. The following instructions are for
Ubuntu Linux.

Install the 'bridge-utils' package to get the '''brctl''' utility.

Now, you need to link your host PC's network port into
a software bridge. Let's say your existing 'outside' Internet connection
is via eth1, and you wish to bridge QEMU guests onto this. Firstly,
unconfigure your network using '''ifdown eth1'''. Now edit
/etc/network/interfaces and change
{{{
auto eth1
iface eth1 inet dhcp
}}}
to
{{{
auto br1
iface br1 inet dhcp
      bridge_ports eth1
}}}

Finally bring the interface back up using '''ifup br1'''. From now on,
your outside connection is via br1, which is linked to eth1. Use
'''brctl show''' to see this.

Next you need to edit '''/etc/qemu-ifup''', which is the script run by
qemu when it needs to access the interface, so that it can add itself
into the bridge.

{{{
#!/bin/sh
sudo -p "Password for $0:" /sbin/ifconfig $1 0.0.0.0 promisc up
sudo /usr/sbin/brctl addif br1 $1
}}}

Finally, start qemu like this:

{{{
qemu -net tap -net nic -hda openwrt-x86-2.6-squashfs.image
}}}

What happens is that qemu creates a new 'tap' interface, e.g. tap0,
connects this to the virtual NIC within the guest environment, and
the qemu-ifup script connects this to the software bridge in the host
environment.

If you get the following permission error:
{{{
warning: could not open /dev/net/tun: no virtual network emulation
Could not initialize device 'tap'
}}}

then you can chown /dev/net/tun to your own userid, or else run qemu as root.

If you are running multiple qemu instances simultaneously then each one will need
to have a unique MAC address assigned to it: e.g.

{{{
qemu -net tap -net nic,macaddr=52:54:0:0:0:1 -hda openwrt-x86-2.6-squashfs.image1
qemu -net tap -net nic,macaddr=52:54:0:0:0:2 -hda openwrt-x86-2.6-squashfs.image2
...
}}}

Conversely, it's possible to connect a single qemu instance to multiple software bridges
(and hence external NICs) on the host. This can be done by using a separate qemu-ifup
script for each one, linking to a separate software bridge instance.

{{{
qemu -net nic,vlan=1 -net nic,vlan=2 \
     -net tap,vlan=1,script=/etc/qemu-ifup -net tap,vlan=2,script=/etc/qemu-ifup2 \
     -hda openwrt-x86-2.6-squashfs.image
}}}

Now within the guest, eth0 connects to one bridge and eth1 connects to another.

== Other options ==

There are many other qemu networking possibilities, such as setting up IP-over-TCP
encapsulation for point-to-point links between qemus, or IP-over-UDP multicast.
Read the qemu manpage or google for other examples, e.g.
http://www.gnome.org/~markmc/qemu-networking.html and
http://www.h7.dion.ne.jp/~qemu-win/HowToNetwork-en.html

= See also =

 * SoekrisPort (for more details about partitioning)
 * ["Generic_x86-HowTo"]
 * ["RunningKamikazeOnVMwareHowTo"]
