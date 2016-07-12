#acl Known:read,write All:read
[:OpenWrtDocs]
[[TableOfContents]]
= Using OpenWrt for the first time =
OpenWrt uses the DMZ led to signal bootup, turning the led on while booting and off when completely booted. OpenWrt uses many of the same network settings as other firmwares, meaning that once the system has booted you should be able to telnet the router at whatever address it was last configured for.

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

'''Why no telnet password?'''
Telnet is an insecure protocol with no encryption, we try to make a point of this insecurity by not enabling a password. If you're in an enviornment that requires password protection we suggest installing the dropbear ssh server.

= Firstboot =
The OpenWrt firmware contains two pieces, a kernel and a readonly filesystem known as squashfs. The job of the firstboot script is to make a secondary, writable jffs2 filesystem out of the free space in flash.

When OpenWrt boots it will check for the existance of a jffs2 partition and attempt to boot from that, otherwise it will boot from the squashfs filesystem contained within the firmware. The lack of a jffs2 partition will ''automatically'' trigger the firstboot script which will run in the background, creating a jffs2 filesystem and populating it with symbolic links to the squashfs filesystem (which is now remounted to the /rom directory). The effect of this is that the root filesystem will suddenly appear to be writable shortly after bootup, this can be verified with the mount command:

{{{
/dev/mtdblock/4 on / type jffs2 (rw)
}}}

If you do not see this line you may need to run firstboot manually (just type "firstboot"). The firstboot script can also be used to erase all changes to the jffs2 partition, particularly useful when upgrading from previous OpenWrt versions with different filesystem layouts.

= editing files =

The use of symlinks by the firstboot script saves space on the jffs2 partition, but it does have some interesting side effects such as edititing files. Since all files are by default symlinks to a readonly filesystem, you will not be able to edit files directly -- you'll get a readonly error if you try. Instead you have to delete the symlink and copy the file to the jffs2 partition to be able to edit it.

{{{
rm /etc/ipkg.conf
cp /rom/etc/ipkg.conf /etc/ipkg.conf
vim /etc/ipkg.conf
}}}

= ipkg =
To be written ....
