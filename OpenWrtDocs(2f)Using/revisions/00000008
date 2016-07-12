#acl Known:read,write All:read
##
## Note: these pages document the firmware itself, not packages
##       questions/comments should be posted to the forum
##
[:OpenWrtDocs]
[[TableOfContents]]
= Using OpenWrt for the first time =
OpenWrt uses the DMZ led to signal bootup, turning the led on while booting and off once completely booted. Once booted, you should be able to telnet into the router using the last address it was configured for.

{{{
Trying 192.168.1.1...
Connected to 192.168.1.1.
Escape character is '^]'.

BusyBox v1.00 (2004.12.24-03:19+0000) Built-in shell (ash)
Enter 'help' for a list of built-in commands.

  _______                     ________        __
 |       |.-----.-----.-----.|  |  |  |.----.|  |_
 |   -   ||  _  |  -__|     ||  |  |  ||   _||   _|
 |_______||   __|_____|__|__||________||__|  |____|
          |__| W I R E L E S S   F R E E D O M
          
root@OpenWrt:/# 
}}}

The firmware itself is designed to occupy as little space as possible while still providing a reasonably friendly commandline interface. With no packages installed, the firmware will simply configure the network interfaces, setup a basic NAT/firewall and load the telnet server and dnsmasq (a combination dns forwarder and dhcp server).

'''Why no telnet password?'''
Telnet is an insecure protocol with no encryption, we try to make a point of this insecurity by not enabling a password. If you're in an environment that requires password protection we suggest installing the dropbear ssh server.

'''What if I can't get in?'''
The problem is caused when the jffs2 partition (see below) is detected but unusable, either the result of previous OpenWrt installation or occasionally just caused by a brand new router. Simply boot into [:OpenWrtDocs/Troubleshooting: failsafe mode] and run firstboot to reformat the jffs2 partition.

= Firstboot / jffs2 =

The OpenWrt firmware contains two pieces, a kernel and a readonly filesystem embeded in the firmare known as squashfs. The job of the firstboot script is to make a secondary, writable jffs2 filesystem out of the free space in flash.

When OpenWrt boots it will check for the existance of a jffs2 partition and attempt to boot from that, otherwise it will boot from the squashfs filesystem. The lack of a jffs2 partition will ''automatically'' trigger the firstboot script which will run in the background, creating a jffs2 filesystem and populating it with symbolic links to the squashfs filesystem (which is now remounted to the /rom directory). The effect of this is that the root filesystem will suddenly appear to be writable shortly after bootup, this can be verified with the mount command:

{{{
/dev/mtdblock/4 on / type jffs2 (rw)
}}}

If you do not see this line you may need to run firstboot manually (just type "firstboot"). The firstboot script can also be used to erase all changes to the jffs2 partition, particularly useful when upgrading from previous OpenWrt versions with different filesystem layouts.

= Editing Files =

The use of symlinks by the firstboot script saves space on the jffs2 partition, but it does have some interesting side effects such as edititing files. Since all files are by default symlinks to a readonly filesystem, you will not be able to edit files directly -- you'll get a readonly error if you try. Instead you have to delete the symlink and copy the file to the jffs2 partition to be able to edit it.

{{{
rm /etc/ipkg.conf
cp /rom/etc/ipkg.conf /etc/ipkg.conf
vim /etc/ipkg.conf
}}}

= ipkg =
The ipkg utility is a lightweight package manager used to download and install OpenWrt packages from the internet.
(Linux users familiar with apt-get will recognise the similarities)

||{{{ipkg update}}}||Download a list of packages available||
||{{{ipkg list}}}||View the list of packages||
||{{{ipkg install dropbear}}}||Install the dropbear package||
||{{{ipkg remove dropbear}}}||Remove the dropbear package||
More options can be found via ''{{{ipkg --help}}}''.

Additional packages can be found through [http://nthill.free.fr/openwrt/tracker Nico's package tracker]; these packages can be installed using ''{{{ipkg install http://example.com/package.ipk}}}'' or by adding the the source repository to your ''/etc/ipkg.conf''.

= Configuration =
See [:OpenWrtDocs/Configuration]
