'''DDNS howto'''

[[TableOfContents]]
= About No-IP.com DDNS =
The DDNS service is for etablishing connections from computers on the Internet to your computer. This is useful if you want to run server software on your computer and only have a dynamic IP. There is a general purpose [:DDNSHowTo:DDNS client] for OpenWRT. If you use the No-IP.com service, however, you will need to follow this document.

!OpenWrt uses the package {{{noip_1.6.0}}} for providing No-IP.com DDNS updates.

= Requirements =
A recent OpenWrt version. This howto was written using the 'White Russian RC4' later release. It may work on earlier and probably on later releases.

An account with No-IP.com

= Installation =
The {{{noip}}} package is not in the main repositories. You can either update your repository list or install directly from a URI. I did the later.

{{{
-Find the noip package in the OpenWRT Package Tracker (http://tracker.openwrt.org/packages/).
 You will need the URI of package to install it.

-telnet or ssh shell into the router
-install from the URI you found above:
 # ipkg install <URI of package>

Ex: # ipkg install http://www.ramereth.net/openwrt/ipkg/noip_1.6.0_mipsel.ipk
}}}

= Configuration =
The configuration file is saved to /etc/no-ip.conf. For example, if you had example.no-ip.com and wanted it to be updated every 30 minutes, your config file should look something like this:

{{{
##############################################################################
# this is a sample configuration file for noip_updater
#       it should be changed to contain your values and
#       placed in /usr/local/lib/no-ip.conf or /usr/local/etc/no-ip.conf
#       The meaning of each line is desctribed in the README file
#
LOGIN    = login_name@address.ext
PASSWORD = myP4ssw0rd
HOSTNAME = example
DOMAIN   = no-ip.com
GROUP    =
DEVICE   = YourInternetConnectionDevice
PROXY    = N
NAT      = Y
DAEMON   = Y
INTERVAL = 30
#
##############################################################################
}}}

The device line doesn't seem to be required. If you would like to update a no-ip.com group rather than just an individual host, leave the hostname line blank and add something for group.

= Starting NOIP =
After starting the client, you should verify your host was updated by logging into your account at [http://www.no-ip.com no-ip.com] To start {{{noip}}} simply use:

{{{
# noip
}}}

The {{{noip}}} client will remain running and will continue to update every INTERVAL minutes. To stop it use

{{{
# killall noip
}}}

== Load on Boot ==
You'll probably want the client to start everytime the router boots. Create a link in /etc/init.d/ to the noip executable:

{{{
# ln -s /usr/bin/noip S90noip
}}}

Since we named this S90, this will be one of the last things run on bootup, so it should occur well after your network has been brought up.

== Debugging ==
If {{{noip}}} fails to update your ip address, it's probably a problem with the config file. To help troubleshoot such errors, run {{{noip}}} manually in verbose mode using:

{{{
# noip -dl
}}}

This helped me determine that if ''HOSTNAME='' is used in the config file, ''GROUP='' should be blank, and vice versa.

= Useful links =
http://forum.openwrt.org/viewtopic.php?id=111
----
CategoryHowTo
