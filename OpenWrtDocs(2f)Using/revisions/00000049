#acl Known:read,write All:read
##
## Note: these pages document the firmware itself, not packages
##       questions/comments should be posted to the forum
##
##
##
##
## PLEASE POST ALL QUESTIONS ABOUT THE DOCUMENTATION ON THE FORUM.
## I DO NOT WANT TO HAVE TO LOCK DOWN EDITS ON THESE PAGES
## - mbm
##
## (no, don't reply here, use the forum)
##
##
##
##
##
##
##
##
##
##
##
##
##
OpenWrtDocs [[TableOfContents]]

= Bootup =
On routers with DMZ LED !OpenWrt will use the LED to signal bootup, turning the LED on while booting and off once completely booted.

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

== Why no default password? ==
People are lazy. We don't want to give people a false sense of security by creating a password that everyone knows. We want to make sure you know that it's insecure by not even prompting for it.

== What if I can't access telnet when first booting? ==
This may very well be a problem with your firewall settings in linux or windows. If you have any firewalls, you may disable them.

However once OpenWRT is installed and you do the first reboot, telnet no longer functions (reason of security).  Use SSH as the alternative.  There are good clients out there (Tunnelier, Putty, etc).

== What if I can't access SSH after setting a password? ==
Try again after a minute or two. On the first bootup OpenWrt will be busy setting up the filesystem and generating SSH keys; the SSH server won't start until after the keys have been generated.

== Why does it reject my password or display SSH warnings after upgrading? ==
Upgrading !OpenWrt completely replaces the filesystem. This means that your previous password and ssh keys will be erased and you will have to set your password again.

= Package management =
See [:OpenWrtDocs/Packages:]
