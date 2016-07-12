'''Dropbear public key authentication howto'''

[[TableOfContents]]

= Why Public Key Authentication =
 * you no longer have to type the password,
  * less effort to log in,
  * less times for it to be seen on your fingers by others,
  * easier to automate things like SCP or remote commands,
 * the password is no longer sent encrypted to !OpenWrt,
  * less likely for an eavesdropper to capture it,
 * allows you to turn off password authentication,
  * impossible for an attacker to guess your password on !OpenWrt.
= Requirements =
 * SSH client to connect to !OpenWrt (see the links at the end of this document)
= Generate the Key Pair =
Create the public and private key pair and copy it to !OpenWrt. We show you how to create the key using Linux and Windows.

== Using OpenSSH client on Linux ==
If you haven't already got a {{{.ssh/id_dsa.pub}}} file on your Linux system (not !OpenWrt), open a shell and type:

{{{
ssh-keygen -t dsa}}}
Next copy the public key with SCP to !OpenWrt:

{{{
scp ~/.ssh/id_dsa.pub root@192.168.1.1:/tmp}}}
You can also copy & paste the public key into !OpenWrt after making a normal password-based SSH connection to it.  The public key is in text.

## future ... == Using Dropbear on another OpenWrt ==
== Using PuTTY on Windows ==
 * Start the PuTTY Key Generator with {{{puttygen.exe}}}.
 * Click on the button ''Generate''.
 * Click on ''Save public key''. Save the public key in a file called {{{OpenWrt-Public-Key}}}.
 * Click on ''Save private key''. Save the private key in a file called {{{OpenWrt-Private-Key.ppk}}}.
A public key looks like (the text is all one, without linebreaks):

{{{
ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAIEAmihVmFR3GH8V0BmN0uexjxmCMenVrYUQ8OKYUntz7knmxE1Wzxy
1ZF6unK36GXJAxEekK1WdSXXEEB50FLcVgbfQRoTo3RBVEP2acXyvTM5R3n5GRhXltEUVlkK5vL98f2xpQK5cqmu9+
jFz/z/BdXycORb5cO6m28TDLRD+9Fk= rsa-key-20050927
}}}
Next copy the public key with {{{pscp.exe}}} to !OpenWrt. For this open a CMD console:

## Why save it above and then paste it into a console?  Can't it be done in one command?  Quozl.
{{{
C:\> echo ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAIEAmihVmFR3GH8V0BmN0uexjxmCMenVrYUQ8OKYUnt
        z7knmxE1Wzxy1ZF6unK36GXJAxEekK1WdSXXEEB50FLcVgbfQRoTo3RBVEP2acXyvTM5R3n5GRhXl
        tEUVlkK5vL98f2xpQK5cqmu9+jFz/z/BdXycORb5cO6m28TDLRD+9Fk= rsa-key-20050927
        > OpenWrt-Public-Key.txt
C:\> pscp.exe -scp -l root -pw <your_router_password> OpenWrt-Public-Key.txt
        192.168.1.1:/tmp/id_rsa.pub}}}
You can also use copy & paste the public key to !OpenWrt after making a normal password SSH connection to it.

= Create authorized_keys =
Add the public key to the {{{authorized_keys}}} file on !OpenWrt by doing the following:

{{{
cd /etc/dropbear
cat /tmp/id_*.pub >> authorized_keys
chmod 0600 authorized_keys}}}
You can repeat this step with every new public key. Each key is appended to the {{{/etc/dropbear/authorized_keys}}} file.

= Connecting to OpenWrt with Public Key =
If you did everything right, you can now login using your key. It will not ask you for a password.

== Using the OpenSSH client ==
{{{
user@host:~$ ssh root@192.168.1.1
}}}
When you like to get some debug messages from OpenSSH then use ssh with the {{{-vv}}} parameter:

{{{
user@host:~$ ssh -vv root@192.168.1.1
BusyBox v1.00 (2006.03.27-00:00+0000) Built-in shell (ash)
Enter 'help' for a list of built-in commands.
  _______                     ________        __
 |       |.-----.-----.-----.|  |  |  |.----.|  |_
 |   -   ||  _  |  -__|     ||  |  |  ||   _||   _|
 |_______||   __|_____|__|__||________||__|  |____|
          |__| W I R E L E S S   F R E E D O M
 WHITE RUSSIAN (RC5) -------------------------------
  * 2 oz Vodka   Mix the Vodka and Kahlua together
  * 1 oz Kahlua  over ice, then float the cream or
  * 1/2oz cream  milk on the top.
 ---------------------------------------------------
root@ap1:~# Connection to ap1 closed.
user@host:~$ }}}
== Using PuTTY on Windows ==
Start {{{putty.exe}}} and do the following:

 * Session:
 In "Host Name" enter the router's DNS name or IP address, e.g. for access from the LAN enter {{{192.168.1.1}}} (your router's IP address) or from the WAN my-router.dyndns.org (your registered dynamic DNS name). If you change the port for Dropbear, then also adopt the "Port" statement here. The protocol ("connection type") is always "SSH".
 * Connection → Data:
 In the box "Login details" enter the "Auto-login username" which is {{{root}}}
 * Connection → SSH → Auth:
 In the box "Authentication Parameters" under "Private key file for Authentication" state the path to your private key file for this connection (e.g. the {{{OpenWrt-Private-Key.ppk}}} file you created before). Best is to click "Browse..." and select the file via the file dialog.
 * Session:
 Load- save or delete a stored session, enter {{{OpenWrt-Session}}} in Saved Sessions and click the Save button
 * (optional) Connection → SSH → Tunnels: Here you can define tunnels, which offer you the possibility to access services on your router and LAN with exposing them to the internet. The connection will be done through your SSH connection, hence tunnel. Example to access the router's WebIF: Define a "Local" tunnel with the source port "80" and the destination "localhost:80"; don't forget to "Add" it. This will allow you to access the router's WebIF in your browser via localhost:80. Note that the destination is always resolved on the other side of the tunnel.
'''TIP:''' To make a PuTTY shortcut with an automatically login, create one and append the saved session with an {{{@}}} sign, for example call PuTTY with:

{{{
C:\> putty.exe @OpenWrt-Session
}}}
== Using SSH Secure Shell Client on Windows ==
The Only difference in OpenSSH/PuTTY and this client is, the key pair generated has a {{{--Begin}}} and {{{--End}}}, and your {{{Comment}}} with date is also added in a new line. So first generate the key by opening SSH Client from menu options select Edit->Settings->Global Settings->User Authentication->Keys

 * Generate New will create id_dsa and id_dsa.pub
 * Upload (will not work if sftp is not enabled on WRT) simply creates a new authorized_keys2 (in most cases there is none) with the {{{---Begin Key, Comment}}}, {{{public_key}}} and {{{---End Key}}} lines
 * Delete everything else other than the public_key line {{{make sure its one line}}} and prepend, 'ssh-rsa' or 'ssh-dsa' (without quotes based on your key type) then save & exit.
 * {{{
cat tmp/.ssh/authorized_keys2 >> /etc/dropbear/authorized_keys; rm -rf /tmp/.ssh}}}
== Using WinSCP on Windows ==
There's a [:SFTPWithDropbearHowTo:HowTo for accessing Dropbear with WinSCP]

= Some final tasks =
== Disable password login ==
For more security you can disable Dropbear's password login. This is done by adding the {{{-s}}} parameter to Dropbear. Modify the last line in the {{{/etc/init.d/S50dropbear}}} init script.

{{{
cat /etc/init.d/S50dropbear}}}
The the last line should look like:

{{{
/usr/sbin/dropbear -s}}}
Now it's time to reboot.

If everything works as expected you may delete {{{/etc/init.d/S50telnet}}} script so that already disabled {{{telnetd}}} daemon does not start any more.

{{{
rm /etc/init.d/S50telnet}}}
The next reboot will free some CPU resources for you.

If you are worried that you might lose your private key (thereby by locking yourself out of your router if you used dropbear's {{{-s}}} switch), one way to provide a failsafe is to run ''another'' instance of dropbear on a different port, ''without'' the {{{-s}}} switch. For example, you could leave the last line of {{{/etc/init.d/S50dropbear}}} the way it is (i.e. without the {{{-s}}} switch) and add another line which starts a second instance of dropbear:

{{{
# failsafe for local access - port 22, pw auth allowed
/usr/sbin/dropbear
# secure for remote access - port 50022, pw auth not allowed
/usr/sbin/dropbear -s -p 50022}}}
In this example, the first instance is your failsafe, which runs on port 22 and allows password login. The second instance runs on port 50022 (the port number is arbitrary -- you can choose another open port if you so desire) and does NOT allow password login. If your router is internet-facing, only open port 50022 in your firewall; if your router is ''behind'' an internet-facing router, forward to port 50022 only. In other words, just use port 22 for local access.

The downside of this second instance strategy is that it takes up slightly more memory. In the future, it would be nice if {{{webif}}} could allow you to enable and disable password logins. For now, this second instance strategy works.

== Accessing your router via SSH from WAN (Internet) by changing firewall rules ==
'''Attention!!!''' First you need to be sure that Dropbear is configured for maximum security and only then start exposing it to the WAN. If you use passwords you are vulnerable to brute force attacks, so it is recommended to disable password logins and use public key authentication instead (see above).

To make it available you have to activate some rules in the file "/etc/firewall.user". There are already some simple predefined rules in it for SSH (WR 0.9), which you can just uncomment:

{{{
## -- This allows port 22 to be answered by (dropbear on) the router
iptables -t nat -A prerouting_wan -p tcp --dport 22 -j ACCEPT
iptables        -A input_wan      -p tcp --dport 22 -j ACCEPT
}}}
If you want to block brute force attacks then have a look at [http://forum.openwrt.org/viewtopic.php?id=7493 this forum thread]. It is based on the information of the documents ["IPTables"] and ThrottleConnectionsHowTo. It also provides an example how to access SSH via a non-standard port (e.g. 443 for restrictive firewalls) although Dropbear is still running on the standard port 22.

= Troubleshooting =
Make sure the {{{/etc/dropbear}}} directory is {{{chmod}}}ed 0700 and the {{{/etc/dropbear/authorized_keys}}} file 0600.

{{{
root@OpenWrt:~# ls -l /etc/|grep dropbear
drwx------    1 root     root            0 Feb 28 15:26 dropbear}}}
{{{
root@OpenWrt:~# ls -l /etc/dropbear/|grep authorized
-rw-------    1 root     root          626 Feb 28 15:31 authorized_keys}}}
If you see anything different than the above you can try these commands.

{{{
chmod 0700 /etc/dropbear
chmod 0600 /etc/dropbear/authorized_keys}}}
= Links =
The free OpenSSH client and server [[BR]]- http://www.openssh.org/

PuTTY is a free implementation of Telnet and SSH for Win32 ({{{puttygen.exe}}}, {{{putty.exe}}} and {{{pscp.exe}}}) [[BR]]- http://www.chiark.greenend.org.uk/~sgtatham/putty/

PuTTY with hardware token support [[BR]] - http://www.joebar.ch/puttysc/

Key authentication [[BR]]- http://en.wikipedia.org/wiki/Key_authentication
