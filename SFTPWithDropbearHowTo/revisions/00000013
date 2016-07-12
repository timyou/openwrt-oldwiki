[:OpenWrtDocs]


[[TableOfContents]]


= Introduction =

This HOWTO explains how to configure SFTP for use with the Dropbear SSH package.
Dropbear is typically used because of its small size.  It is pre-installed on !OpenWrt.

== What is SFTP? ==

Secure File Transfer Protocol or SFTP is a protocol that was incorporated as part
of SSH. The idea behind SFTP is to have all of the features that FTP has, but
transfer both passwords and file data over an encrypted link.

= Activating Dropbear =

Dropbear is a small SSH daemon that comes pre-installed on !OpenWrt. However,
it is not active by default. To activate Dropbear, change the password.
You can do this on the web interface, or use the shell command:

{{{
passwd}}}

You will be prompted for a new {{{root}}} password, along with a verification prompt.
Once this is done, !OpenWrt will disable the telnet daemon and activate the
Dropbear SSH daemon.

= Installing the SFTP module =

Update the package list and install the ''openssh-sftp-server'' package.  You can do this on the web interface, using ''System'' - ''Installed Software'', ''Update package lists'', then ''Install'' the ''openssh-sftp-server'' package.  Or use the shell prompt:

{{{
ipkg update
ipkg install openssh-sftp-server}}}

For RC4 and earlier, you may need to install ''libopenssl'' and create a directory and link:
{{{
ipkg update
ipkg install libopenssl openssh-sftp-server
mkdir -p /usr/libexec
ln -s /usr/lib/sftp-server /usr/libexec/sftp-server}}}

= Windows SFTP clients =

Once both SSH and SFTP are installed you will be able to securely access the routers
files via a secure connection. Two of the most popular clients that support SFTP are the
[http://www.chiark.greenend.org.uk/~sgtatham/putty/ Putty SFTP client] and the
[http://filezilla.sourceforge.net/ FileZilla] graphical client. While the !FileZilla
client is actually built upon the Putty client they will be treated here as if they are
two distinct clients.


== FileZilla ==

The !FileZilla client is an ideal choice for most Windows users. The graphical interface
and relatively small learning curve allows the user to begin actively using the software
immediately.

See the [http://sourceforge.net/project/showfiles.php?group_id=21558 download page] and the
[http://sourceforge.net/forum/?group_id=21558 user’s forum].


== Putty SFTP ==

Called PSFTP the Putty SFTP client is a robust and stable implementation of the secure file
transfer protocol. While good, Putty's client is command-line based.  If you are used to
graphical clients, use !FileZilla instead.


See Putty's [http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html download page] and
Putty's [http://www.chiark.greenend.org.uk/~sgtatham/putty/docs.html documentation page].


== WinSCP ==

WinSCP is a Windows program that makes use of code from Simon Tatham's "Putty". It provides a GUI and can be either installed or run from a stand-alone exe without installation.

WinSCP has a shell extension, which is only available if the software is installed on the client machine, that will allow drag-and-drop usability from the WinSCP window to almost any other Explorer windows. For example, one could drag firewall.conf straight to the desktop.

However, if the non-installation method is chosen, e.g., it is run solely from the exe, then drag-and-drop capabilities will be restricted to within the WinSCP window only. The WinSCP windows can provide an interface either like Norton Comander (r) or like Windows (r) Explorer.

The software is free and open-source. You can download it [http://winscp.net/eng/download.php here] or visit the [http://winscp.net/eng/index.php home page].
