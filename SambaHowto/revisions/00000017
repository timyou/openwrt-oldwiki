'''Samba howto'''

[[TableOfContents]]
= Intro =
This howto shows you how to give all users on your network a shared drive where they can read and write files aka a file server, using the Linux implementation of Windows networking (NetBIOS/SMB) - called Samba.

I decided to package Samba 2.0.x version of it to !OpenWrt, because the newer versions are just overkill for a Wrt router.

Samba offers a lot more options but this would be out of the scope of this howto. For more information on Samba please see the links at the button.

= Requirements =
 * supported router by !OpenWrt
 * a recent OpenWrt version installed (at least White Russian RC3)
 * some kind of a external storage device (optional)

= Installation =
The Samba package has been backported for !OpenWrt White Russian. So you can install it from the backports repository. Just add the following line to /etc/ipkg.conf:

{{{
src backports http://downloads.openwrt.org/backports/rc5
}}}

Next, update ipkg and install samba by typing (you'll need internet-access for this):

{{{
ipkg update
ipkg install samba
}}}

It'll check for dependencies and get all the packages it needs.'''
'''

'''TIP:''' A Samba client package is available too.

= Configuration =
The default Samba configuration uses the {{{/tmp}}} directory for storage.

/!\ '''WARNING:''' All data is lost in {{{/tmp}}} after a reboot.

To change settings edit the {{{/etc/samba/smb.conf}}} file.

Start Samba with

{{{
/etc/init.d/samba start
}}}

= Clients =
'''NOTE:''' In the default config file all users are only able to read on the share, since all users use the {{{nobody}}} account. You can change this in the {{{/etc/samba/smb.conf}}} file.

== Linux clients ==
List shares with {{{smbclient}}}:

{{{
smbclient -L <server_name> -N
}}}

Connect to a Samba share with:

{{{
smbclient //<server_name>/<share> -U <username>
}}}

Connect with {{{smbfs}}}:

{{{
smbmount //<server_name>/<share> /<local_mount_point> -o username=<username>
}}}

== Windows clients ==
Now you should be able to browse your share called {{{tmp}}} from any computer that is a member of {{{OpenWrt}}} workgroup (the default workgroup name in Windows is {{{WORKGROUP}}}).

== MacOS X clients ==
In the Finder, press Command-K for the mount popup.  In the Server Address text box, type:

{{{
smb://<server_ip>/<share>
}}}

You may press the "+" sign to save this in your list.  Press "Browse" to see all shares on a server, or "Connect" to mount the share.  You'll see the icon appear on the desktop, and the share will be mounted in /Volumes.

= Links =
 * Samba homepage [[BR]]- http://www.samba.org/

 * USB storage howto - Extend the storage capacity of your USB enabled Wrt router [[BR]]- UsbStorageHowto

 * Parts of this documentation are taken from [[BR]]- http://www.macsat.com/OpenWRT/samba.php
