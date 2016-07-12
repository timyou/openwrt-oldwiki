'''Printer sharing howto'''

[[TableOfContents]]

= Why should I use printer sharing? What is that? =
If you want to share printers with other PCs (clients) in your network, then this is the right howto for you. It was written for the small {{{p910nd}}} non-spooling printer server. An alternative would be using the {{{cups}}} package (which is also available) but in my opinion it's too much for the average !OpenWrt device (mostly because it needs to cache the print jobs before sending them and because there's not much space for that left without additional storage space).

From the p910nd man page: p910nd is a small printer daemon intended for diskless workstations that does not spool to disk but passes the job directly to the printer. Normally a lpr daemon on a spooling host connects to it with a TCP connection on port 910n (where n=0, 1, or 2 for lp0, 1 and 2 respectively). p910nd is particularly useful for diskless Linux workstations booted via Etherboot that have a printer hanging off them. Common Unix Printing System (CUPS) supports this protocol, it's called the !AppSocket protocol and has the scheme socket://. LPRng also supports this protocol and the syntax is lp=remotehost%9100 in /etc/printcap.

= Requirements =
 * a device supported by !OpenWrt with USB and/or parport (the Asus WL-500g has both USB and parport)
 * a recent !OpenWrt version installed (at least White Russian RC3)
 * configured USB and/or parport modules
 * the {{{p910nd}}} package (which is not yet included in White Russian)
 * GNU/Linux or Windows clients to connect to your printer server
 * a USB or parallel printer ('''TIP:''' I tested this with a noname USB-to-Parport adapter/converter too, works perfect!)
= Installation =
Configure your device to use the backports repository, see ["OpenWrtDocs/Packages"] for instructions, then install the package:

{{{
ipkg install p910nd}}}
== Printers connected via USB ==
To use an USB printer you must first add support for USB printers. First follow UsbStorageHowto to install the USB controller modules if you haven't already done so. You don't need {{{usb-storage}}} for the printer to work.

Additionally, you need the {{{usb-printer}}} module which you can install with {{{ipkg}}} as follows:

{{{
ipkg install kmod-usb-printer}}}
Now plug in the printer, run {{{dmesg}}} and check for the following lines:

{{{
hub.c: new USB device 01:02.0-1, assigned address 2
printer.c: usblp0: USB Bidirectional printer dev 2 if 0 alt 0 proto 2 vid 0x04A9 pid 0x1094
usb.c: USB disconnect on device 01:02.0-1 address 2
hub.c: new USB device 01:02.0-1, assigned address 3
printer.c: usblp1: USB Bidirectional printer dev 3 if 0 alt 0 proto 2 vid 0x04A9 pid 0x1094}}}
== Printers connected via parport (parallel port/LPT) ==
When you're connecting a parport printer you must install the {{{kmod-lp}}} package which installs the modules for parport support.

{{{
ipkg install kmod-lp}}}
Now you've to reboot your Wrt router.

{{{
reboot}}}
When you see the file {{{/dev/printers/0}}} than the installation is done. You can also check the output from {{{dmesg}}}.

= Configuring the printer daemon =
Edit the file {{{/etc/default/p910nd}}} to your needs. The file is well commented. The default file looks like that:

{{{
cat /etc/default/p910nd}}}
{{{
# printing port list, in the form "number [options]"
# where:
#  - number is the port number in the range [0-9]
#    the p910nd daemon will listen on tcp port 9100+number
#  - options can be :
#    -b to turn on bidirectional copying.
#    -f to specify a different printer device.
#
0  -b -f /dev/usb/lp0}}}
You can run more than one printer at the same time. For example one on USB and the other on the parport (f. e. {{{1  -b -f /dev/printers/0}}}) interface.

If you own ASUS WL-500 and connect to parallel port, you might need to modify {{{/etc/default/p910nd}}} to contain (only) {{{ -f /dev/printers/0}}} Save it and start the {{{p910nd}}} daemon with:

{{{
/etc/init.d/p910nd start}}}
To start it up automatically rename it as follows

{{{
mv /etc/init.d/p910nd /etc/init.d/S55p910nd}}}
= Configure the clients for printing =
Here I would demonstrate you, how to configure the printer driver on your client. It could be that these steps are not exactly the same on your operating system.

'''NOTE:''' Remember the ports you configured above. Default is port 9100 for a USB printer on the device {{{/dev/usb/lp0}}}.

You can check the ports on which {{{p910nd}}} is listening on with the command {{{netstat -an}}} executed on the router.

[[BR]][[BR]][[BR]]We need your help here!Please update this section with more client configurations. This should include a short list howto configure a client. Please do not use screenshots.Thanks.

== Linux clients ==
=== CUPS ===
Assuming the printer driver is installed locally, it's a simple matter of entering http://localhost:631 in your favorite web-browser, and pressing add printer under the "Printers" pane. Then:

 * Enter something into the information fields and press continue.
 * Select "Internet Printing Protocol (IPP)" and press continue.
 * Write "socket://<ip to router>:<listening port of router>". Here you have to fill in the appropriate info in the <> fields. Press continue.
 * Select the appropriate manufacturer and press continue.
 * Select the appropriate printer and press continue.
 * Voila...
Then you use your new printer like you would a local one.

=== kprinter (KDE) ===

 * Start kprinter
 * Select 'Add printer'
 * Select Network printer (TCP)
 * Use 192.168.1.1 (the router's IP address) as the printer's IP
 * Fill in the port you want to use (normally defaults to 9100)
 * Pick manufacturer and model
 * Pick the recommended driver 
 * Then you can new print a test page or change the settings of the printer further

=== Gnome ===

 * Select System -> Administration -> Printing
 * Select New Printer
 * Select Network Printer and "HP !JetDirect"
 * Enter your WRT's IP address and port 9100.
 * Select your printer's make and model. Continue forward and apply settings.
 * Check the properties to ensure you are using A4 or US Letter size as appropriate.
== OS X ==
=== Version 10.4.6 ===
 * select system preferences
 * Print & Fax
 * Click on + button
 * Click on IP Printer
 * set Protocol: HP Jet Direct - Socket, Address: <ipaddr>:<port> and then select brand and printer.
 * Type a name if you don't want the IP address for a name.
 * close the Printer Browser.
== Windows clients ==
=== Windows 2000/XP Home/Professional ===
'''NOTE:''' I have only tested this with Windows 2000 Professional, I just assume it works the same with XP and the Home versions.

 * Install your printer software as you would if it were a local printer.
 * Go to your printer properties in the control panel/printer settings.
 * Select the tab "Ports".
 * Select "Add Port".
 * Select "Standard TCP/IP Port" and click on "New Port...".
 * Follow the wizard. In the field "Printer Name or IP Address", enter the IP address of your router.
 * Windows will send a couple of UDP packets to port 161 of the Router. You can safely discard them.
 * You will need to select a Device Type. Select "Custom" and click "Settings...".
 * Be sure the protocol is "Raw" and the port number is correct (i.e. 9100).
 * Finish the Settings wizard and close the Add Port window. The newly created Port should now be selected.
 * You printer should be configred now. Be sure that your firewall allows communication to the chosen port.
 * You may print a test page to see if all went well.
= Ink level information for inkjet printers =
Most printer drivers cannot access ink level information through the 910nd deamon, so you may not know, which cartridge to change. You can use the attached ink-4.1 package attachment:ink%5F%30.%34.%31%2D%31%5Fmipsel.ipk to obtain the ink levels for most printers in OpenWrt (based on http://libinklevel.sourceforge.net/). If you want to display the inklevels in X-Wrt you may apply the following path to status-usb.sh:

{{{
...
end_form
EOF
?>
<?
usbpr=`ls /dev/usb/lp* 2>/dev/null`
if [ ! -z "$usbpr" ]; then
        inklevel_form=$(
        for pdev in $usbpr; do
                ink -d $pdev |  awk -v FS=":" '
                BEGIN
                {
                        line=0
                        print "string|<table style=\"width: 90%; margin-left: 2.
                }
                {
                        if (line==2)
                        {
                                print "string| <tr><td colspan=\"5\"><h3>@TR<<st
                        }
                        if (line >=4)
                        {
                                print "string| <tr><td width=200>" $1 "</td><td>
                                print "progressbar|inklevel||200||" $2 "||"
                                print "string|</td></tr>"
                        }
                        line++
                }
                END
                {
                        print "string|</table>"
                }'
        done;
        )
        display_form <<EOF
        start_form|@TR<<status_usb_printers_inklevels#USB printer inklevels>>
        $inklevel_form
        end_form
EOF
fi;
?>
<div class="settings">
<h3>@TR<<status_usb_Mounted_USB_SCSI#Mounted USB / SCSI devices>></h3>
<div>
...
}}}
= Troubleshooting =
 * Problem : the printer status shows "Attempting to connect to socket://<ip to router>:<listening port of router>" in the client CUPS interface (http://localhost:631) and nothing works (seen on ["OpenWrtDocs/Hardware/Asus/WL500GP"] / WhiteRussian RC6).
 * Solution : make sure you installed both USB 1.1 and USB 2.0 modules (see UsbStorageHowto).
= Not supported printers =
Here you should create a list of printers which are '''not''' working with the {{{p910nd}}} package. Please include manufacturer, model, interface (USB/Parport), driver working and some short comment.

The combination Windows 2000 with a canon pixma iP4000 seems not to work with bidirectional mode. If your printer dosent work, try disabling bidirectional mode.

Please add not working combinations here.

Konica Minolta PagePro 1300W doesn't seem to work in bidirectional mode under win xp.

Canon i560 is not working in bidirectional mode. Remove the -b option on the router and disable bidirectional mode and the Canon Status Monitor in Windows. Make sure that the uhci kernel module is loaded since it seems to be usb 1.1.

Canon MP600 does not work in bidirectional mode on Windows XP using p910nd v0.7. Remove -b from line in /etc/defaults/p910nd and kill/restart the p910nd process. Uses the ehci-hcd module (USB 2.0).

= Links =
- http://etherboot.sourceforge.net/p910nd/ [[BR]]- http://wl500g.dyndns.org/printing/ [[BR]]- http://wl500g.dyndns.org/
