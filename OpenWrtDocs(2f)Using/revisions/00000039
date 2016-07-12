#acl Known:read,write All:read
##
## Note: these pages document the firmware itself, not packages
##       questions/comments should be posted to the forum
##


[:OpenWrtDocs]
[[TableOfContents]]

On routers with DMZ LED !OpenWrt will use the LED to signal bootup, turning the LED on while booting and
off once completely booted. 

Once booted, you should be able to telnet into the router using the last address it was configured for:

{{{
telnet 192.168.1.1

Trying 192.168.1.1...
Connected to 192.168.1.1.
Escape character is '^]'.
 === IMPORTANT ============================
  Use 'passwd' to set your login password
  this will disable telnet and enable SSH
 ------------------------------------------


BusyBox v1.00 (2006.03.24-09:16+0000) Built-in shell (ash)
Enter 'help' for a list of built-in commands.

  _______                     ________        __
 |       |.-----.-----.-----.|  |  |  |.----.|  |_
 |   -   ||  _  |  -__|     ||  |  |  ||   _||   _|
 |_______||   __|_____|__|__||________||__|  |____|
          |__| W I R E L E S S   F R E E D O M
 WHITE RUSSIAN -------------------------------------
  * 2 oz Vodka   Mix the Vodka and Kahlua together
  * 1 oz Kahlua  over ice, then float the cream or
  * 1/2oz cream  milk on the top.
 ---------------------------------------------------
root@OpenWrt:~# passwd
Changing password for root
Enter the new password (minimum of 5, maximum of 8 characters)
Please use a combination of upper and lower case letters and numbers.
Enter new password: 
Re-enter new password:
Password changed.
root@OpenWrt:~# 
}}}

= Setting a password =

At this point we strongly suggest setting a password. Depending which firmware image you have installed, you can set the password either via !OpenWrt WebIf or via telnet using the {{{passwd}}} command. After setting the password, any attempt to telnet in will result in a "Login failed" message.

'''Why no default password?'''[[BR]]
People are lazy. We don't want to give people a false sense of security by creating a password that everyone knows. We want to make sure you know that it's insecure by not even prompting for it.

'''What if I can not access telnet when first booting?'''[[BR]]
This may very well be a problem with your firewall settings in linux or
windows. If you have any firewalls, you may disable them.

'''Why does it reject my password or display SSH warnings after upgrading?'''[[BR]]
Upgrading !OpenWrt completely replaces the filesystem. This means that your previous password and ssh keys will be erased and you will have to set your password again.

= Notes about SquashFS firmware =

'''Firstboot'''[[BR]]

The !OpenWrt firmware contains two pieces: a kernel and a read-only filesystem
(embedded in the firmware) known as SquashFS. Because the SquashFS filesystem
is readonly, a second writable filesystem has to be created using JFFS2 to hold
your changes.

When !OpenWrt boots it will check for the existence of a JFFS2 partition and
attempt to boot from that, otherwise it will boot from the SquashFS filesystem.
The lack of a JFFS2 partition will ''automatically'' trigger the firstboot
script which will run in the background, creating a JFFS2 filesystem and
populating it with symbolic links to the SquashFS filesystem (which is now
remounted to the {{{/rom}}} directory).

If at any time you wish to revert files back to their original condition
(in other words, recreate the symlinks to /rom), just run {{{firstboot}}}.

'''Editing files'''[[BR]]

Since the filesystem is a collection of symlinks to a readonly filesystem,
you can't simply edit files -- they're readonly. Instead you have to delete
the symlink, and copy the file so you have a writable version of the file to
edit:

{{{
rm /etc/ipkg.conf
cp /rom/etc/ipkg.conf /etc/ipkg.conf
vim /etc/ipkg.conf
}}}

= Notes about JFFS2 firmware =

The JFFS2 firmware will be READONLY when you boot it the first time, this is due
to the method used to create the filesystem; you must perform an extra REBOOT
after installing the firmware.

= Package management =

The ipkg utility is a lightweight package manager used to download and install
!OpenWrt packages from the internet. (GNU/Linux users familiar with {{{apt-get}}}
will recognise the similarities)

The firmware itself is designed to occupy as little space as possible while
still providing a reasonably friendly commandline interface or webadministration 
interface. With no packages
installed, the firmware will simply configure the network interfaces, setup a
basic NAT/firewall, and load the secure shell server and dnsmasq (a combination DNS
forwarder and DHCP server).

||'''Command'''||'''Description'''||
||ipkg update||Download a list of packages available||
||ipkg list||View the list of packages||
||ipkg install dropbear||Install the dropbear package||
||ipkg remove dropbear||Remove the dropbear package||

More options can be found via {{{ipkg --help}}}.

The configuration file for ipkg is {{{/etc/ipkg.conf}}}. Before you can install any
addon package, you need to freshen the package list with 
{{{
root@OpenWrt:~# ipkg update
}}}

'''Upgrade with ipkg'''

Never ipkg upgrade a whole release. You can upgrade addon-packages, but you should always reflash if you switching between releases and release candidates.

'''ipkg-link'''[[BR]]

If you have USB storage, or install packages to a destination other than root,
the shell script {{{ipkg-link}}} will create automatic symlinks to the root
filesystem for those packages. See the info on {{{ipkg-link}}} on the
[:UsbStorageHowto].

'''Proxy support'''[[BR]]

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
