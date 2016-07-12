'''Dropbear public key authentication howto'''


[[TableOfContents]]


= Why Public Key Authentication with Dropbear =

There are several resons for using public key authentication. Most important would be adding
more security, you like to avoid entering your password everytime you login to your
router or you like to automate things like file transfers using SCP (Secure Copy).


= Requirements =

  * A recent OpenWrt version (>= White Russian RC4) installed on your router.
  * SSH client software to connect to the router (see the links at the end of this document)


= Installation =

No ipkg package installation is necessary. Dropbear is installed as the default
SSH server in !OpenWrt.


= Configuration =


== Generate the Public and Private Key pair ==

Create the public and private key pair and copy it to the router. We show you how to
create the key using Linux and Windows.


=== With the OpenSSH client on Linux ===

If you haven't already got a {{{.ssh/id_dsa.pub}}} file on your Linux system (not the
router), open a shell and type:

{{{
ssh-keygen -t dsa
}}}

Next copy the public key with SCP onto the router:

{{{
scp ~/.ssh/id_dsa.pub root@192.168.1.1:/tmp
}}}

You can also copy & paste the public key to the router after making a normal password
SSH connection to it.  The public key is in text.


=== With PuTTY on Windows ===

Start the PuTTY Key Generator with {{{puttygen.exe}}}. Click on the button Generate.

  * After that click on the "Save public key" button. Save the public key in a file
  called {{{OpenWrt-Public-Key}}}.
  * Now save your private key by clicking on "Save private key". Save it to a file
  called {{{OpenWrt-Private-Key.ppk}}}.

See the example PuTTY Key Generator
[http://openwrt.ertl-net.net/downloads/test/putty-key-generator.jpg screenshot].

The public key in PuTTY looks like (the keys are all in one line, without linebreaks):

{{{
ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAIEAmihVmFR3GH8V0BmN0uexjxmCMenVrYUQ8OKYUntz7knmxE1Wzxy
1ZF6unK36GXJAxEekK1WdSXXEEB50FLcVgbfQRoTo3RBVEP2acXyvTM5R3n5GRhXltEUVlkK5vL98f2xpQK5cqmu9+
jFz/z/BdXycORb5cO6m28TDLRD+9Fk= rsa-key-20050927
}}}

Next copy the public key with {{{pscp.exe}}} onto the router. For this open a CMD console:

{{{
C:\> echo ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAIEAmihVmFR3GH8V0BmN0uexjxmCMenVrYUQ8OKYUnt
        z7knmxE1Wzxy1ZF6unK36GXJAxEekK1WdSXXEEB50FLcVgbfQRoTo3RBVEP2acXyvTM5R3n5GRhXl
        tEUVlkK5vL98f2xpQK5cqmu9+jFz/z/BdXycORb5cO6m28TDLRD+9Fk= rsa-key-20050927
        > OpenWrt-Public-Key.txt
C:\> pscp.exe -scp -l root -pw <your_router_password> OpenWrt-Public-Key.txt
        192.168.1.1:/tmp/id_rsa.pub
}}}

You can also use copy & paste the public key to the router after making a normal password
SSH connection to it.


== Add the Public Key to authorized_keys ==

Add the public key to the {{{authorized_keys}}} file on the router by doing the following:

{{{
cd /etc/dropbear
cat /tmp/id_*.pub >> authorized_keys
chmod 0600 authorized_keys
}}}

You can repeat this step with every new public key. Each key is appended to the
{{{/etc/dropbear/authorized_keys}}} file.


= Connecting to OpenWrt with Public Key =

If you did everything right, you can now login using your key. It will
not ask you for a password.


== Using the OpenSSH client ==

{{{
user@host:~$ ssh root@192.168.1.1


BusyBox v1.00 (2005.09.22-14:58+0000) Built-in shell (ash)
Enter 'help' for a list of built-in commands.

  _______                     ________        __
 |       |.-----.-----.-----.|  |  |  |.----.|  |_
 |   -   ||  _  |  -__|     ||  |  |  ||   _||   _|
 |_______||   __|_____|__|__||________||__|  |____|
          |__| W I R E L E S S   F R E E D O M
 WHITE RUSSIAN (RC4) -------------------------------
  * 2 oz Vodka   Mix the Vodka and Kahlua together
  * 1 oz Kahlua  over ice, then float the cream or
  * 1/2oz cream  milk on the top.
 ---------------------------------------------------
root@OpenWrt:~# Connection to 192.168.1.1 closed.
user@host:~$
}}}

When you like to get some debug messages from OpenSSH then use ssh with the {{{-vv}}} parameter:

{{{
user@host:~$ ssh -vv root@192.168.1.1
}}}


== Using PuTTY on Windows ==

Start {{{putty.exe}}} and do the following:
 * Session / Host Name (or IP address), enter {{{192.168.1.1}}} (your router's IP address)
 * Connection / Data / Login details, Auto-login username is {{{root}}}
 * Connection / SSH / Auth / Authentication Parameters / Private key file for Authentication,
 and select the file {{{OpenWrt-Private-Key.ppk}}} file you created before
 * Session / Load- save or delete a stored session, enter {{{OpenWrt-Session}}} in Saved Sessions
 and click the Save button

When this is done click on the Open button, and a similar window similar to
[http://openwrt.ertl-net.net/downloads/test/putty-dropbear-connection.jpg this] will popup.[[BR]]

'''TIP:''' To make a PuTTY shortcut with an automatically login, create one and append the saved
session with an {{{@}}} sign, for example call PuTTY with:

{{{
C:\> putty.exe @OpenWrt-Session
}}}


= Some final tasks =


== Disable password login ==

For more security you can disable Dropbear's password login. This is done
by adding the {{{-s}}} parameter to Dropbear. Modify the last line in the
{{{/etc/init.d/S50dropbear}}} init script.

{{{
cat /etc/init.d/S50dropbear
}}}

The the last line should look like:

{{{
/usr/sbin/dropbear -s
}}}

Now it's time to reboot.

= Troubleshooting =

Make sure the /etc/dropbear directory is chmodded 0700 and the /etc/dropbear/authorized_keys file 0600.

{{{
root@OpenWrt:~# ls -l /etc/|grep dropbear
drwx------    1 root     root            0 Feb 28 15:26 dropbear
}}}
{{{
root@OpenWrt:~# ls -l /etc/dropbear/|grep authorized
-rw-------    1 root     root          626 Feb 28 15:31 authorized_keys
}}}

If you see anything different than the above you can try these commands.
{{{
chmod 0700 /etc/dropbear
chmod 0600 /etc/dropbear/authorized_keys
}}}

= Links =

The free OpenSSH client and server
[[BR]]- [http://www.openssh.org/]

PuTTY is a free implementation of Telnet and SSH for Win32 ({{{puttygen.exe}}},
{{{putty.exe}}} and {{{pscp.exe}}})
[[BR]]- [http://www.chiark.greenend.org.uk/~sgtatham/putty/]

Key authentication
[[BR]]- [http://en.wikipedia.org/wiki/Key_authentication]
