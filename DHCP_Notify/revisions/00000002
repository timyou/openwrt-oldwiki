= DHCP Notify =
The functionality we will be adding here is about sending a notification to a given email address about any changes in the DHCP server,
which includes newly added clients or dead clients which are later removed from the database.
It comes in handy in case that you would like to put up an open-authentication Wireless system and receive updates about clients
that connect to it.
== Install and Configure ==
'''Installing the SMTP client'''
I chose the mini-sendmail program. It should be in your ipkg repository so go right ahead and perform
{{{
ipkg install mini-sendmail}}}
'''Configuring dnsmasq'''
OpenWRT/X-WRT uses the dnsmasq utility to handle DHCP leases.
It is required to simply open up the configuration file''/etc/dnsmasq.conf''and add the following configuration directive inside
{{{
dhcp-script=/sbin/mailme}}}
The idea is that on every dhcp action performed dnsmasq will execute the script with certain arguments that we can use to get some info.
'''Creating /sbin/mailme'''
Let's create the script to email us:
{{{
#!/bin/sh
# mailme
# upon execution append the current date along with all arguments passed to us
# and pipe them to the mini_sendmail program.
#
# Replace <SMTP_SERVER> with your smtp server address
#         <PORT> with the port number of your smtp server (default is 25)
#         <TO_EMAIL> with the email address you would like to send these notifications to
#
# Jan 1 2008 - Liran Tal <liran.tal@gmail.com>
date +"%D %T $*" | mini_sendmail -s<SMTP_SERVER> -p<SMTP_PORT> -t <TO_EMAIL>
}}}
The idea is that on every dhcp action performed dnsmasq will execute the script with certain arguments that we can use to get some info.
Replace the above <> variables with proper settings and we're done.
==== Regards,Liran Tal. ====
----
CategoryHowTo
