'''Samba HowTo'''
(note: no longer works in rc6 due to missing libgcc_s.so.1)

[[TableOfContents]]
= Intro =
This shows you how to give all users on your network a shared drive where they can read and write files.  We use Samba, the Open Source implementation of Windows networking (NetBIOS/SMB).

Samba 2.0.x was packaged for !OpenWrt, because the newer versions are overkill for the CPU and memory available on a typical device.

Samba offers a lot more options but this would be out of the scope. For more information on Samba see the links at the button.

= Requirements =
 * a device supported by !OpenWrt
 * a recent !OpenWrt version installed (at least White Russian RC3)
 * some kind of a storage device (optional)

= Installation =
Configure your device to use the backports repository, see ["OpenWrtDocs/Packages"] for instructions, then install the package:
{{{
ipkg install samba}}}

'''TIP:''' A Samba client package is available too.

= Configuration =
The default Samba configuration uses the {{{/tmp}}} directory for storage.

/!\ '''WARNING:''' All data is lost in {{{/tmp}}} after a reboot.  See LocalFileSystemHowTo for alternative storage options.

To change settings edit the {{{/etc/samba/smb.conf}}} file.

Start Samba with

{{{
/etc/init.d/samba start}}}

== localhost ==

If samba does not start, try adding your router's name and ip in /etc/hosts.
(see also http://forum.openwrt.org/viewtopic.php?id=5401)

= Clients =
'''NOTE:''' In the default config file all users are only able to read on the share, since all users use the {{{nobody}}} account. You can change this in the {{{/etc/samba/smb.conf}}} file.

== Linux clients ==
List shares with {{{smbclient}}}:

{{{
smbclient -L <server_name> -N}}}

Connect to a Samba share with:

{{{
smbclient //<server_name>/<share> -U <username>}}}

Connect with {{{smbfs}}}:

{{{
smbmount //<server_name>/<share> /<local_mount_point> -o username=<username>}}}

== Windows clients ==
Now you should be able to browse your share called {{{tmp}}} from any computer that is a member of {{{OpenWrt}}} workgroup (the default workgroup name in Windows is {{{WORKGROUP}}}).

== MacOS X clients ==
In the Finder, press Command-K for the mount popup.  In the Server Address text box, type:

{{{
smb://<server_ip>/<share>}}}

You may press the "+" sign to save this in your list.  Press "Browse" to see all shares on a server, or "Connect" to mount the share.  You'll see the icon appear on the desktop, and the share will be mounted in /Volumes.

= Links =
 * [http://www.samba.org/ Samba]

 * UsbStorageHowto

 * IdeStorageHowTo

 * LocalFileSystemHowTo - configuring local storage,

 * Parts of this documentation are taken from [[BR]]- http://www.macsat.com/OpenWRT/samba.php
