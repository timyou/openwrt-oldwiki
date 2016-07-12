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
   * a USB or parallel printer (I tested this with a noname USB-to-Parport
   adapter too, works perfect!)


= Installation =

For now please install the {{{p910nd}}} package from Nico's testing
repository with the command:

{{{
ipkg install http://downloads.openwrt.org/people/nico/testing/ \
        mipsel/packages/p910nd_0.7-2_mipsel.ipk
}}}

'''TIP:''' These binary packages from Nico's repository can be used
in the stable White Russian release (except the kmod-* and kernel
packages).

The {{{p910nd}}} package will be included in White Russian RC4.


= Configuring the printer daemon =

Edit the file {{{/etc/default/p910nd}}} to your needs. The file is
well commented. The default file looks like that:

{{{
cat /etc/default/p910nd
}}}

{{{
# printing port list, in the form "number [options]"
# where:
#  - number is the port number in the range [0-9]
#    the p910nd daemon will listen on tcp port 9100+number
#  - options can be :
#    -b to turn on bidirectional copying.
#    -f to specify a different printer device.
#
0  -b -f /dev/usb/lp0
}}}

You can run more than one printer at the same time. For example
one on USB and the other on the parport (f. e. {{{1  -b -f /dev/printers/0}}})
interface.

Save it and start the {{{p910nd}}} daemon with:

{{{
/etc/init.d/p910nd start
}}}

I will startup automatically on the next reboot.


= Configure the clients for printing =

Here I would demonstrate you, how to configure the printer driver
on your client. It could be that these steps are not exactly the
same on your operating system.

'''NOTE:''' Remember the ports you configured above. Default is port
9000 for a USB printer on the device {{{/dev/usb/lp0}}}.

You can check the ports on which {{{p910nd}}} is listening on with
the command {{{netstat -an}}} executed on the router.

[[BR]][[BR]][[BR]]

We need your help here!

Please update this section with more client configurations. This
should include a short list howto configure a client. Please do not
use screenshots.

Thanks.


== Linux clients ==


=== CUPS ===

Please fill this section with some useful content.


=== kprinter (KDE) ===

Please translate this to english. Thanks.

 * Start kprinter
 * Drucker hinzufügen / Weiter / select Netzwerkdrucker (TCP) / Weiter
 * Bei Druckeradresse 192.168.1.1 (the routers IP address) eingeben
 * Bei Port den soeben configurierten eingeben eingeben / Weiter
 * Hersteller und Modell auswählen / Weiter
 * Bei Treiberauswahl den empfohlenen auswählen / Weiter
 * You can new print a test page or change the Einstellungen / Weiter


=== Gnome ===

Please fill this section with some useful content.


== Windows clients ==


=== Windows 2000/XP Home/Professional ===

'''NOTE:''' I have only tested this with Windows 2000 Professional, I just
assume it works the same with XP and the Home versions.

 * Install your printer software as you would if it were a local printer.
 * Go to your printer properties in the control panel/printer settings.
 * Select the tab "Ports".
 * Select "Add Port".
 * Select "Standard TCP/IP Port" and click on "New Port...".
 * Follow the wizard. In the field "Printer Name or IP Address", enter the
 IP address of your router.
 * Windows will send a couple of UDP packets to port 161 of the Router. You
 can safely discard them.
 * You will need to select a Device Type. Select "Custom" and click "Settings...".
 * Be sure the protocol is "Raw" and the port number is correct (f. e. 9100).
 * Finish the Settings wizard and close the Add Port window. The newly created Port
 should now be selected.
 * You printer should be configred. Be sure that your firewall allows communication
 to that port numbers respectively.
 * You may print a test page to see if all went well.


= Not supported printers =

Here you should create a list of printers which are '''not''' working
with the {{{p910nd}}} package. Please include manufacturer, model,
interface (USB/Parport), driver working  and some short comment.

Please update this section with some useful content.


= Links =

- [http://etherboot.sourceforge.net/p910nd/]
[[BR]]- [http://wl500g.dyndns.org/printing/]
[[BR]]- [http://wl500g.dyndns.org/]
