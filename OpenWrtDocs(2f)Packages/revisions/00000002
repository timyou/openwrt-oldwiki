Describe OpenWrtDocs/Packages here.

=== uPnP ===

'''uPnP''' is Universal Plug and Play.  You can use either the LinkSys binary from the
original firmware or the compiled version.

Documentation and the background of uPnP can be found at [:OpenWrtDocs/upnp]


=== CUPS - Printing system with spooling ===

You can't print a testpage on the local cups, because this would need to have ghostscript
installed on your embedded system.

If you have a special Postscript Printer Description (ppd) file for your printer, copy it
to /usr/share/cups/model/ and restart cupsd. Cups will install it in /etc/cups/ppd and you
can choose it via the web interface. (192.168.1.1:631)

If you have problems with permissions, try to change /etc/cups/cupsd.conf to fit your local
TCP/IP network:

{{{
<Location />
Order Deny,Allow
Deny From All
Allow from 127.0.0.1
Allow from 192.168.1.0/24 #your ip area.
</Location>
}}}

MacOS X tip:
Configure your extended printer settings. If you use the standard printer settings and add
an IPP printer, MacOS X will add after the server adress /ipp . But this class etc. does
not exist on your cupsd.


=== Wake on LAN ===

If you have trouble using [http://tracker.openwrt.org/packages/list.php?name=wol wol] to
wake up your PC give [http://openwrt.org/downloads/people/nico/testing/mipsel/packages/ ether-wake]
a try. Since ether-wake uses an ethernet frame instead of an UDP packet it might be what you're
looking for. Make sure you enabled WOL for your NIC with [http://sourceforge.net/projects/gkernel/ ethtool]
before shutting down your PC.

=== NFS ===

You need to install kmod-nfs and portmap to be able to mount remote NFS file systems.

=== socks-Proxy ===

There is a Socks-proxy available for !OpenWrt, it is called '''srelay''' (Find via the
package tracker). However, there is no documentation for this package. So, here is a
quick guide:

Srelay comes with a configuration file: /etc/srelay.conf (surprise surprise). It has some
examples, but basically you will want to do this:

{{{
192.168.1.0/24 any -
}}}

This should give every computer in the 192.168.1.0 subnet access to srelay while keeping
everything else out.

Then start srelay: '''srelay -c /etc/srelay.conf -r -s'''. Find out more about the
available options with '''srelay -h'''.

Keep in mind that this information was found using trial-and-error-methods, so it might
still be faulty or have unwanted side effects.

=== Building your own packages ===

To build your own packages for !OpenWrt with the SDK, see [:BuildingPackagesHowTo].
