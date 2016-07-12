#acl Known:read,write All:read
##
## Note: these pages document the firmware itself, not packages
##       questions/comments should be posted to the forum
##


[:OpenWrtDocs]
[[TableOfContents]]


= Using OpenWrt for the first time =

!OpenWrt uses the DMZ LED to signal bootup, turning the LED on while booting and
off once completely booted. Once booted, you should be able to telnet into the
router using the last address it was configured for.

{{{
Trying 192.168.1.1...
Connected to 192.168.1.1.
Escape character is '^]'.

BusyBox v1.00 (2005.09.22-14:58+0000) Built-in shell (ash)
Enter 'help' for a list of built-in commands.

  _______                     ________        __
 |       |.-----.-----.-----.|  |  |  |.----.|  |_
 |   -   ||  _  |  -__|     ||  |  |  ||   _||   _|
 |_______||   __|_____|__|__||________||__|  |____|
          |__| W I R E L E S S   F R E E D O M
 WHITE RUSSIAN (RC3) -------------------------------
  * 2 oz Vodka   Mix the Vodka and Kahlua together
  * 1 oz Kahlua  over ice, then float the cream or
  * 1/2oz cream  milk on the top.
 ---------------------------------------------------
root@OpenWrt:~#
}}}

The firmware itself is designed to occupy as little space as possible while
still providing a reasonably friendly commandline interface. With no packages
installed, the firmware will simply configure the network interfaces, setup a
basic NAT/firewall and load the telnet server and dnsmasq (a combination DNS
forwarder and DHCP server).

'''Why no telnet password?'''
Telnet is an insecure protocol with no encryption, we try to make a point of
this insecurity by not enabling a password. If you're in an environment that
requires password protection we suggest setting a password with the {{{passwd}}}
command, which will disable the telnet server and enable the Dropbear SSH
server.

'''What if I can't get in?'''
The problem is caused when the JFFS2 partition (see below) is detected but
unusable, either the result of previous !OpenWrt installation or occasionally
just caused by a brand new router. Simply boot into
[:OpenWrtDocs/Troubleshooting: failsafe mode] and run {{{firstboot}}} to reformat
the JFFS2 partition.

'''What if I can not access telnet when first booting?'''
This may very well be a problem with your firewall settings in linux or
windows. If you have any firewalls, disable them.

/!\ '''WARNING:''' Do this only if you know what you are doing and can restore
your iptables rules effortlessly. In GNU/Linux, you can flush iptables firewall
settings by issuing the following series of commands:

{{{
iptables -P INPUT ACCEPT
iptables -P OUTPUT ACCEPT
iptables -P FORWARD ACCEPT
iptables -F
}}}


= Firstboot / JFFS2 =

The following applies only to the SquashFS images of !OpenWrt. The JFFS2 images
just need an extra reboot, so you don't have to run {{{firstboot}}} yourself.

The !OpenWrt firmware contains two pieces, a kernel and a readonly filesystem
embeded in the firmare known as SquashFS. The job of the firstboot script is to
make a secondary, writable JFFS2 filesystem out of the free space in flash.

When !OpenWrt boots it will check for the existance of a JFFS2 partition and
attempt to boot from that, otherwise it will boot from the SquashFS filesystem.
The lack of a JFFS2 partition will ''automatically'' trigger the firstboot
script which will run in the background, creating a JFFS2 filesystem and
populating it with symbolic links to the SquashFS filesystem (which is now
remounted to the {{{/rom}}} directory). The effect of this is that the root
filesystem will suddenly appear to be writable shortly after bootup, this can
be verified with the mount command:

{{{
/dev/mtdblock/4 on / type jffs2 (rw)
}}}

If you do not see this line you may need to run firstboot manually (just type
{{{firstboot}}}). The firstboot script can also be used to erase all changes to
the JFFS2 partition, particularly useful when upgrading from previous !OpenWrt
versions with different filesystem layouts.


= Editing Files =

On JFFS2 firmware images, the whole root filesystem is writable, however on the
SquashFS builds you need some extra steps to edit the default configuration
files:

The use of symlinks by the firstboot script saves space on the JFFS2 partition,
but it does have some interesting side effects such as edititing files. Since
all files are by default symlinks to a readonly filesystem, you will not be
able to edit files directly -- you'll get a readonly error if you try. Instead
you have to delete the symlink and copy the file to the JFFS2 partition to be
able to edit it.

{{{
rm /etc/ipkg.conf
cp /rom/etc/ipkg.conf /etc/ipkg.conf
vim /etc/ipkg.conf
}}}


= ipkg =

The ipkg utility is a lightweight package manager used to download and install
!OpenWrt packages from the internet. (GNU/Linux users familiar with {{{apt-get}}}
will recognise the similarities)

||'''Command'''||'''Description'''||
||ipkg update||Download a list of packages available||
||ipkg list||View the list of packages||
||ipkg install dropbear||Install the dropbear package||
||ipkg remove dropbear||Remove the dropbear package||

More options can be found via {{{ipkg --help}}}.

Additional packages can be found through the [http://tracker.openwrt.org package tracker];
these packages can be installed using {{{ipkg install http://example.com/package.ipk}}}
or by adding the the source repository to your {{{/etc/ipkg.conf}}}.

If you have USB storage, or install packages to a destination other than root,
the shell script {{{ipkg-link}}} will create automatic symlinks to the root
filesystem for those packages. See the info on {{{ipkg-link}}} on the
[:UsbStorageHowto].


== Proxying ipkg ==

To use {{{ipkg}}} through a proxy, add the following to {{{/etc/ipkg.conf}}}

{{{
option http_proxy http://aaa.bbb.ccc.ddd:port/
option ftp_proxy ftp://aaa.bbb.ccc.ddd:port/
}}}

these are for if you need authentication

{{{
option proxy_username xxxx
option proxy_password xxxx
}}}

If the authentication with the above options in {{{/etc/ipkg.conf}}}
is not working try the following format:

{{{
option http_proxy http://username:password@aaa.bbb.ccc.ddd:port/
option ftp_proxy http://username:password@aaa.bbb.ccc.ddd:port/
}}}


= Configuration =

See [:OpenWrtDocs/Configuration].
