[[TableOfContents]]


= Why should I use printer sharing? What is that? =

If you want to share printers with other PCs (clients) in your
network, then this is the right howto for you. It was written
for the small {{{p910nd}}} non-spooling printer server.
An alternative would be using the cups package (which is also available) but
in my opinion it's too much for the average OpenWrt device (mostly because
it needs to cache the print jobs before sending them and because there's
not much space for that left without additional storage space).

From the p910nd man page:[[BR]]
p910nd is a small printer daemon intended for diskless workstations
that does not spool to disk but passes the job directly to the
printer. Normally a lpr daemon on a spooling host connects to it with
a TCP connection on port 910n (where n=0, 1, or 2 for lp0, 1 and 2
respectively). p910nd is particularly useful for diskless Linux
workstations booted via Etherboot that have a printer hanging off
them. Common Unix Printing System (CUPS) supports this protocol, it's
called the AppSocket protocol and has the scheme socket://. LPRng also
supports this protocol and the syntax is lp=remotehost%9100
in /etc/printcap.


= Requirements =

   * Supported router by OpenWrt with USB and/or parport (the
   Asus WL-500g has both USB and parport)
   * a recent OpenWrt version installed (at least White Russian RC3)
   with already configured USB and/or parport modules and the
   {{{p910nd}}} package (which is not yet included in White Russian)
   * GNU/Linux or Windows clients to connect to your printer server
   * A USB or parallel printer


= Installation =

For now please install the {{{p910nd}}} package from Nico's testing
repository with the command:

{{{
ipkg install http://downloads.openwrt.org/people/nico/testing/ \
        mipsel/packages/p910nd_0.7-1_mipsel.ipk
}}}

'''TIP:''' These binary packages from Nico's repository can be used
in the stable White Russian release (except the kmod-* and kernel
packages).

The {{{p910nd}}} package will be included in White Russian RC4.


= Configuring the printer daemon =

Edit the file {{{/etc/default/p910nd}}} to your needs. The file is
well commented.

Save it and start the {{{p910nd}}} daemon with:

{{{
/etc/init.d/S70p910nd start
}}}

You can run more than one printer at the same time. For example
one on USB and the other on the parport interface.


= Configure the clients for printing =

Here I would demonstrate you, how to configure the printer driver
on your client. It could be that these steps are not exactly the
same on your operating system.

'''NOTE:''' Port 9101 is USB connections and port 9100 is for parallel
port (LPT) connections.


== Linux clients ==

We need your help here!

Please update this section with more client configurations. This
should include a short list howto configure a client. Please do not
use screenshots.

Thanks for your help.

=== CUPS ===

Please fill this section with some useful content.


=== kprinter (KDE) ===

Please translate this to english. Thanks.

[[BR]]- Start kprinter
[[BR]]- Drucker hinzufügen / Weiter / select Netzwerkdrucker (TCP), Weiter
[[BR]]- Bei Druckeradresse 192.168.1.1 (the routers IP address) eingeben
[[BR]]- Bei Port 9100 (for LPT) bzw. 9100 (for USB) eingeben / Weiter
[[BR]]- Hersteller und Modell auswählen / Weiter
[[BR]]- Bei Treiberauswahl den empfohlenen auswählen / Weiter
[[BR]]- You can new print a test page or change the Einstellungen / Weiter


=== Gnome ===

Please fill this section with some useful content.


== Windows clients ==


=== Windows XP Home/Professional ===

Please fill this section with some useful content.


= Not supported printers =

Here you should create a list of printers which are '''not''' working
with the {{{p910nd}}} package. Please include manufacturer, model,
interface (USB/Parport), driver working  and some short comment.

Please update this section with some useful content.


= Links =

- [http://etherboot.sourceforge.net/p910nd/]
[[BR]]- [http://wl500g.dyndns.org/printing/]
[[BR]]- [http://wl500g.dyndns.org/]
