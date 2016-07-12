== Official packages ==
The [http://downloads.openwrt.org/whiterussian/packages/ official packages] are supported by !OpenWrt and are known to work on the latest stable White Russian release. Please use the official packages whenever possible.  The {{{/etc/ipkg.conf}}} file should have these lines:

{{{
src whiterussian http://downloads.openwrt.org/whiterussian/packages
src non-free http://downloads.openwrt.org/whiterussian/packages/non-free
}}}
'''TIP:''' If you copy & paste this into your {{{/etc/ipkg.conf}}} file, make sure that you don't get a trailing space. If you do, {{{ipkg update}}} will look like it's updating but files will not be created in {{{/usr/lib/ipkg/lists}}}.

== Backports ==
Some useful packages have been backported from the development branch (trunk) to White Russian. See the [http://downloads.openwrt.org/backports/rc5/00-README RC5 00-README] file for more details.

To use the packages from the backports repository edit {{{/etc/ipkg.conf}}} and add:

{{{
src backports http://downloads.openwrt.org/backports/rc5
}}}
Now run {{{ipkg update}}} and you will see new packages.

== Third party packages ==
'''''NOTE:''' Third party packages are not supported by the OpenWrt developers.''

Third party packages are untested by !OpenWrt and some can even mess up or even brick you router. The !OpenWrt developers do not want to support or give help for these packages anyway on any conditions. Get help from the person who released the package, not OpenWrt developers.

== Some third-party packages ==

Some common third-party packages will be mentioned in this section. There are '''many''' more packages available.

=== X-Wrt ===

[http://www.bitsum.com/xwrt.htm X-Wrt] is a project to enhance the end user experience of OpenWrt. It is currently under active development. X-Wrt is developed by a different group than is the base OpenWrt firmware and is therefore not affiliated with OpenWrt, nor is it supported by OpenWrt. Since many users may be interested what X-Wrt has to offer, some basic information about it is included here.

'''X-Wrt Links:'''

 * [http://www.bitsum.com/xwrt.asp X-Wrt Base Information]
 * [http://developer.berlios.de/projects/xwrt/ Project Hosting (repository, mailing lists, etc..)]
 * [http://www.bitsum.com/smf/index.php?board=17.0 User Forums]

==== webif^2^: An ehanced HTTP based management console ====

'''webif^2^''' is an enhanced webif (HTTP based management console). It offers a large number of new features and is constantly  being improved. Some of the more popular additions are the real-time traffic and CPU graphs. 

Information on X-Wrt, including links to installable packages, pre-built firmwares, and project hosting can be found [http://www.bitsum.com/xwrt.htm here].

To install the latest daily build of webif^2^:

 ipkg install http://ftp.berlios.de/pub/xwrt/webif_latest.ipk

=== uPnP ===
'''uPnP''' is Universal Plug and Play.  OpenWRT now has a working Linux-IGD package available which works with MSN Messenger for audio & video conversations.

Documentation and the background of uPnP can be found at ["OpenWrtDocs/upnp"]

=== CUPS - Printing system with spooling ===
You can't print a testpage on the local cups, because this would need to have ghostscript installed on your embedded system.

If you have a special Postscript Printer Description (ppd) file for your printer, copy it to /usr/share/cups/model/ and restart cupsd. Cups will install it in /etc/cups/ppd and you can choose it via the web interface. (192.168.1.1:631)

If you have problems with permissions, try to change /etc/cups/cupsd.conf to fit your local TCP/IP network:

{{{
<Location />
Order Deny,Allow
Deny From All
Allow from 127.0.0.1
Allow from 192.168.1.0/24 #your ip area.
</Location>
}}}
MacOS X tip: Configure your extended printer settings. If you use the standard printer settings and add an IPP printer, MacOS X will add after the server adress /ipp . But this class etc. does not exist on your cupsd.

=== ether-wake/wol - Wake on LAN ===
If you have trouble using wol to wake up your PC give ether-wake a try. Since ether-wake uses an ethernet frame instead of an UDP packet it might be what you're looking for. Make sure you enabled WOL for your NIC with [http://sourceforge.net/projects/gkernel/ ethtool] before shutting down your PC.

=== srelay - socks proxy ===
There is a socks proxy available for !OpenWrt, it is called '''srelay''' (Find via the package tracker). However, there is no documentation for this package. So, here is a quick guide:

Srelay comes with a configuration file: /etc/srelay.conf. It has some examples, but basically you will want to do this:

{{{
192.168.1.0/24 any -
}}}
This should give every computer in the 192.168.1.0 subnet access to srelay while keeping everything else out.

Another interpretation about the config file is that it configures proxy chaining. You can specify what the next proxy hop should be for a specific destination. If you want srelay to directly connect to any destination you can use a config file like this:

{{{
# destination                  port range      next-hop/port
0.0.0.0                          any
}}}
Then start srelay: '''srelay -c /etc/srelay.conf -r -s'''. Find out more about the available options with '''srelay -h'''.

Keep in mind that this information was found using trial-and-error-methods, so it might still be faulty or have unwanted side effects.

== Other ==

Some third-party can be searched for via http://www.ipkg.be/.

== Building your own packages ==

To build your own packages for !OpenWrt use the SDK, see BuildingPackagesHowTo.
