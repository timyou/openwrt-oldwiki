'''Dropbear public key authentication howto'''


[[TableOfContents]]


= Why Public Key Authentication with Dropbear =

There are several resons for using public key authentication. Most important would be adding
more security, you like to get rid of entering your password everytime you login to your
router or you like to automate things like file transfers using SCP (Secure Copy).


= Requirements =

  * A recent OpenWrt version (>= White Russian RC3) installed on your router.
  * SSH client software to connect to the Dropbear SSH server (see the links at the
  end of this document)


= Installation =

No ipkg package installation is necessary. Dropbear is installed as the default
SSH server in !OpenWrt.


= Configuration =


== Generate the Public and Private Key pairs ==

Now we create our public and private key pairs. I show you how to create them
using Linux and Windows. In the same step we copy the public key onto the router.


=== With the OpenSSH client ===

On Linux open a shell and type:

{{{
ssh-keygen -t dsa
}}}

Next copy the public key with SCP onto the router:

{{{
scp ~/.ssh/id*.pub root@192.168.1.1:/tmp
}}}

You can also use copy & paste the public key to the router after making a normal password
SSH connection to it.


=== With PuTTY on Windows ===

Start the PuTTY Key Generator with {{{puttygen.exe}}}. Click on the button Generate.

  * After that click on the "Save public key" button. Save the public key in a file
  called {{{OpenWrt-Public-Key}}}.
  * Now save your private key by clicking on "Save private key". Save it to a file
  called {{{OpenWrt-Private-Key.ppk}}}.

[http://openwrt.ertl-net.net/downloads/test/putty-key-generator.jpg]

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
        192.168.1.1:/tmp/OpenWrt-Public-Key
}}}

You can also use copy & paste the public key to the router after making a normal password
SSH connection to it.


== Create the directories ==

Create the following directories (on the router) and set their permissions. They are
required later.

{{{
cd /
mkdir -p /root/.ssh
chmod -R 0700 /root
}}}


== Change root's home directory ==

Now it's time to change the root's home directory. This is necessary, because
the standard home directory for root ({{{/tmp}}}) does not have the right
permissions.

To do this, you have to edit the {{{/etc/passwd}}} file. It should look similar
the one below.

{{{
cat /etc/passwd
}}}

{{{
root:!:0:0:root:/root:/bin/ash
nobody:*:65534:65534:nobody:/var:/bin/false
}}}

/!\ '''NOTE:''' This will change in the upcoming White Russian RC4 release.
It's already changed in the stable White Russian CVS branch. The
{{{authorized_keys}}} file will than be stored in the {{{/etc/dropbear}}}
directory. So, on any later versions there is no need to change root's
home directory anymore.


== Add the Public Keys to authorized_keys ==

Once we have this we want to save our public key into the authorized keys
file (on the server) which can be done easily as follows. Your generated
key will look similar to the one below.

{{{
cat ~/.ssh/id_dsa.pub
}}}

{{{
ssh-dss AAAB3NzaC1kc3MAAACBAMJkHn6HPHRn4HVfFwx5dSeRqLhSGpceNqXNPNRe3hZMD9X5K
ra6VJM2VanrjDmjoiK127JszXqjQaryBI58P0dZI+Ts0YchxvgKMLTt1uF5U6lWYcFDxN4eGIxoN
SUK+Sa+HxyRmGhFgslTvLvSS0cLP0JPRF0mYbt80a1y9bFAAAAFQC5f+d+ojrcJOCRcn/7x1iOrL
c+ZQAAAH9J27XrWdP7Ht8qG0llrzNTUczDy8uLEbJcOoljGLPGZ6BSbqgwSmpRm7D6+61tSYk5YT
mGt59VFC1t9W+G3tNG7ZCImpgrSiHu0kQWsDzUgqxcDRRDo6aQc6BbeyKn80bnwUKBla3ebU2BFX
u1rgGt/8Rz3Xw0Vx4jhzT35i5EAAAAgCTCSutthoRNVuC2FD7LFA8j1KT59/PMqZ/pteRd8BzhJe
nOPK3iAhkL4sXy7EBCDyHybu8rLiY1iMKW4xtz4PWAPRy+9NJrtk4OAAvZmwb349pPEdnO/hQj7o
3bjxMzCG05lS7dss8c1kWGvwGe5Ace8eiiGNTn68x6k33DCzwM openwrt-dev@debian
}}}

Add the public key to the {{{autorized_keys}}} on the router by doing the following:

{{{
cd /root/.ssh
mv /tmp/id_*.pub /root/.ssh
cat id_*.pub >> authorized_keys
chmod 0600 id_*.pub authorized_keys
}}}

When using Windows you have to replace the {{{id_*.pub}}} by {{{OpenWrt-Public-Key}}}.

You can repeat this step with every new public key. It gets appended to the
{{{/root/.ssh/authorized_keys}}} file.


= Connecting to OpenWrt with Public Key =

If you did everything right, you can now login using your keys. It will
never ask you for a password.


== Using the OpenSSH client ==

{{{
openwrt-dev@debian:~/.ssh$ ssh root@192.168.1.1


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
root@OpenWrt:~# Connection to 192.168.1.1 closed.
openwrt-dev@debian:~/.ssh$
}}}

When you like to get some debug messages from OpenSSH then use ssh with the {{{-vv}}} parameter:

{{{
openwrt-dev@debian:~/.ssh$ ssh -vv root@192.168.1.1
}}}


== Using PuTTY on Windows ==

Start {{{putty.exe}}} and do the following:
 * Session / Host Name (or IP address), enter {{{192.168.1.1}}} (your router's IP address)
 * Connection / Data / Login details, Auto-login username is {{{root}}}
 * Connection / SSH / Auth / Authentication Parameters / Private key file for Authentication,
 and select the file {{{OpenWrt-Private-Key.ppk}}} file you created before
 * Session / Load- save or delete a stored session, enter {{{OpenWrt-Session}}} in Saved Sessions
 and click the Save button

When this is done click on the Open button, and a similar window as the one below will popup.[[BR]]

[http://openwrt.ertl-net.net/downloads/test/putty-dropbear-connection.jpg]

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

The the last line should look like:

{{{
cat /etc/init.d/S50dropbear
}}}

{{{
/usr/sbin/dropbear -s
}}}

Now it's time to reboot.


= Links =

The free OpenSSH client and server
[[BR]]- [http://www.openssh.org/]

PuTTY is a free implementation of Telnet and SSH for Win32 ({{{puttygen.exe}}},
{{{putty.exe}}} and {{{pscp.exe}}})
[[BR]]- [http://www.chiark.greenend.org.uk/~sgtatham/putty/]

Key authentication
[[BR]]- [http://en.wikipedia.org/wiki/Key_authentication]
