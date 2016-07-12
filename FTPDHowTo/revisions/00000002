[[TableOfContents]]


= Introduction =

This Howto seeks to guide the user through installing and configuring a FTP
server.  When the user has completed the steps in this guide they will have
a fully functioning FTP server.

NOTE: FTP is NOT encrypted.  All passwords and files are sent in the clear.
For a higher level of security please refer to the [:SFTPWithDropbearHowTo].

== What is FTP? ==

FTP, which stands for file transfer protocol, provides a convenient way to
transfer files over networks.  FTP is a rather universal protocol in much the
same way that HTTP is widely used.  Since FTP is common, almost any operating
system has ample software to interact with it (in windows the client is even
integrated into Windows Explorer).

= Installing the Package =
Execute the following lines
{{{
ipkg update
ipkg install vsftpd
}}}

Due to a bug that the packagemanager needs to learn about, you have to execute the followring commands:

{{{
(cd /etc/init.d/;mv vsftpd S50vsftpd)
}}}

Once done all that is needed is a restart to activate the FTP daemon.
{{{
reboot
}}}

= Opening the Firewall to Allow Public Access =
Allowing public access to a non-secured FTP server is not a good idea.  If you
intend to use FTP over the internet please see [:SFTPWithDropbearHowTo].
 
Nevertheless there are some instances where allowing public access to FTP is
necessary.
For those instances adding the following lines to /etc/firewall.user will allow
FTP to get through the firewall.
{{{
### Allow FTP on the WAN interface
iptables -t nat -A prerouting_rule -i $WAN -p tcp --dport 21 -j ACCEPT
iptables        -A input_rule      -i $WAN -p tcp --dport 21 -j ACCEPT
}}}

Execute the following line or reboot to implement the firewall change
{{{
sh /etc/firewall.user
}}}

= What is My Username and Password? =
Your username is {{{root}}} and your password is the password you set with the
{{{passwd}}} command.
