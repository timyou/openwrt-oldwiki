'''Printer sharing howto'''

[[TableOfContents]]

= Why should I use printer sharing? What is that? =
If you want to share printers with other PCs (clients) in your network, then this is the right howto for you. It was written for the small {{{p910nd}}} non-spooling printer server. An alternative would be using the {{{cups}}} package (which is also available) but in my opinion it's too much for the average !OpenWrt device (mostly because it needs to cache the print jobs before sending them and because there's not much space for that left without additional storage space).

From the p910nd man page: p910nd is a small printer daemon intended for diskless workstations that does not spool to disk but passes the job directly to the printer. Normally a lpr daemon on a spooling host connects to it with a TCP connection on port 910n (where n=0, 1, or 2 for lp0, 1 and 2 respectively). p910nd is particularly useful for diskless Linux workstations booted via Etherboot that have a printer hanging off them. Common Unix Printing System (CUPS) supports this protocol, it's called the !AppSocket protocol and has the scheme socket://. LPRng also supports this protocol and the syntax is lp=remotehost%9100 in /etc/printcap.

= Requirements =
 * a device supported by !OpenWrt with USB and/or parport (the Asus WL-500g has both USB and parport)
 * a recent !OpenWrt version installed (at least Kamikaze 7.07)
 * configured USB and/or parport modules
 * the {{{p910nd}}} package
 * GNU/Linux or Windows clients to connect to your printer server
 * a USB or parallel printer ('''TIP:''' I tested this with a noname USB-to-Parport adapter/converter too, works perfect!)
= Installation =
Install the p910nd package:

{{{
ipkg install p910nd}}}
== Printers connected via USB ==
To use an USB printer you must first add support for USB printers. First follow UsbStorageHowto to install the USB controller modules if you haven't already done so. You don't need {{{usb-storage}}} for the printer to work. You might need both USB 1.1 and 2.0  installed to support both modes.

Additionally, you need the {{{usb-printer}}} module which you can install with {{{ipkg}}} as follows:

{{{
ipkg install kmod-usb-printer}}}
Now plug in the printer, run {{{dmesg}}} and check for the following lines:

{{{
hub.c: new USB ice 01:02.0-1, assigned address 2
printer.c: usblp0: USB Bidirectional printer  2 if 0 alt 0 proto 2 vid 0x04A9 pid 0x1094
usb.c: USB disconnect on ice 01:02.0-1 address 2
hub.c: new USB ice 01:02.0-1, assigned address 3
printer.c: usblp1: USB Bidirectional printer  3 if 0 alt 0 proto 2 vid 0x04A9 pid 0x1094}}}
== Printers connected via parport (parallel port/LPT) ==
When you are connecting a parport printer you must install the {{{kmod-lp}}} package which installs the modules for parport support.

{{{
ipkg install kmod-lp}}}
Now you've to reboot your Wrt router.

{{{
reboot}}}
When you see the file {{{/dev/printers/0}}} than the installation is done. You can also check the output from {{{dmesg}}}.

= Configuring the printer daemon =
The configuration has been migrated to use UCI and is stored in the /etc/config/p910nd config file. You can run more than one printer at the same time by adding additional sections. The default configuration is (list all configured printers):

{{{
uci show p910nd}}}
{{{
uci set p910nd.cfg1=p910nd
uci set p910nd.cfg1.ice=//usb/lp0
uci set p910nd.cfg1.port=0
uci set p910nd.cfg1.bidirectional=1
uci set p910nd.cfg1.enabled=01}}}
To add a second printer, do this:

{{{
uci set p910nd.cfg2=p910nd
uci set p910nd.cfg2.ice=//usb/lp1
uci set p910nd.cfg2.port=0
uci set p910nd.cfg2.bidirectional=1
uci set p910nd.cfg2.enabled=1
uci commit p910nd
/etc/init.d/p910nd restart}}}
To delete the second printer, do this:

{{{
uci del p910nd.cfg2
uci commit p910nd
/etc/init.d/p910nd restart}}}
Description of the options in the p910nd config file (/etc/config/p910nd):
||<tablewidth="1155px" tableheight="145px">'''Option''' ||'''Value''' ||'''Default value''' ||'''Description''' ||
||device ||/dev/usb/lp0 ||/dev/usb/lp0 ||The device your printer is connected to (e.g. /dev/usb/lp0 for USB - e.g. /dev/printers/0 for LPT) ||
||port ||[0-9] ||0 ||The p910nd daemon will listen on TCP port 9100+port ||
||bidirectional ||[1|0] ||1 ||1: Turn on bidirectional copying; 0: Turn off bidirectional copying ||
||enabled ||[1|0] ||0 ||1: Enable the printer; 0: Disable the printer ||


To start the p910nd daemon, do this:

{{{
/etc/init.d/p910nd start}}}
To start it up automatically on every boot, do this:

{{{
/etc/init.d/p910nd enable}}}
If your printer (mine hl-2030) spits out garbage after poweron, p910nd might be the cause. Add this to /etc/hotplug.d/usb/20-printer

{{{
#!/bin/sh (-)
# Copyright (C) 2006 OpenWrt.org
if [ "$PRODUCT" = "4f9/27/100" ]
then
case "$ACTION" in
        add)
        echo "`date`: Brother HL-2030 added" >> /tmp/hl-2030
        /etc/init.d/p910nd restart >> /tmp/hl-2030
        echo "Done." >> /tmp/hl-2030
        ;;
        remove)
        echo "`date`: Brother HL-2030 removed" >> /tmp/hl-2030
        /etc/init.d/p910nd stop >> /tmp/hl-2030
        echo "Done." >> /tmp/hl-2030
        ;;
esac
fi
}}}
Where "$PRODUCT" = "4f9/27/100" is your printers VendorId/ProductId/BcdVersion(1.00 = 100). Get it with lsusb -v

You might need to add "-INT" to the kill command in /etc/init.d/p910nd to actually have the stop work.

= Configuring the printer daemon with custom-user-startup =
Following (the original guide V2... below) did not work for '''X-WRT (OpenWrt White Russian 0.9)''' on Asus WL-500g. I did the "UCI SET" with many typos and re-did it perfectly finally, but it still didn't work. So i did read DD-WRT guide on the daemon, about d910nd and finally got it working.

--(2. )----(Now create a file into that directory named "'''usb.startup'''". In console type "nano" (get nano text edito with package manager or ipkg) to open the nano text editor. Write these lines:)-- ''(for some reasons striked method worked once after reboot, but not after second reboot.. no idea why)''--(
)--

2. In X-WRT go to System -> Startup and add these lines in the box:
(you are now editing a custom startup file.. mine was called "/etc/init.d/S95custom-user-startup"):

{{{
 #brother laser
 /jffs/usr/sbin/p910nd -b -f //usb/lp0 0
 #canon inkjet
 /jffs/usr/sbin/p910nd -b -f //usb/lp1 1}}}
--(Nano has a menu below. You use CTRL+X where X the character from the menu. Just start saving the file, put in the right filename and exit nano.)--

NB! correct the usb.startup content to match your setup. -b means bidirectional -f specifices device name The last number can be 0,1 or 2, making the print server listen at port 9100, 9101 and 9102 respectively. And don't forget the " & " mark... read the "custom-user-startup" file comments about that... if there is nothing in your version, then don't bother.

For Asus WL-500g with LaserJet 1020 i used this one, and it works:

{{{
 #LaserJet 1020
 /jffs/usr/sbin/p910nd -b -f //usb/lp0 0}}}
Additional debuging: Check that you have p910nd package installed and there is a file called "p910nd" at "/jffs/usr/sbin/p910nd/" In console check that you have "lp0" listed in "/dev/usb/" dir - if you have something else, use yours. For LPT devices check "/dev/printers/" dir.

Reboot your router and it should work... read below how to set up your printer in the computers. Note:
Try removing the '-b' option for p910nd, if it still doesn't work.

== Advertising the printer via Zeroconf (optional) ==
To avoid having to install the printer on multiple clients, you can advertise it via Zeroconf. The following example uses Avahi.

Apple's [http://developer.apple.com/networking/bonjour/specs.html Bonjour Printing Specification] discusses pretty much what needs to be done to advertise a printer over the network:

 * the service type is {{{_pdl-datastream._tcp.}}}, the [http://en.wikipedia.org/wiki/Page_description_language "needs a driver"] printer type
 * the {{{product}}}, {{{pdl}}}, {{{usb_MFG}}} & {{{usb_MDL}}} TXT records are required, and can be found in the printer's PPD file - OS X's Printer Setup utility uses these to search for the appropriate driver
 * ''the Apple doc notes that printers that don't provide the LPR service should still advertise that service (as "unsupported"); presumably that involves declaring a second service with a particular key to indicate "unsupported" - don't know how to do this with Avahi''
e.g. a [http://solutions.brother.com/hl2040_all/en_us/ Brother HL-2040], a "softprinter" (does not support Postscript or PCL, all processing is done on the client) shared via p910nd:

Create the file {{{/etc/avahi/services/printer.service}}}:

{{{
<service-group>
<name replace-wildcards="yes">Brother HL-2040 on %h</name>
<service protocol="any">
<type>_pdl-datastream._tcp.</type>
<host-name></host-name>
<port>9100</port>
<txt-record>product=(HL-2040 series)</txt-record>
<txt-record>pdl=application/vnd.cups-raster</txt-record>
<txt-record>usb_MFG=Brother</txt-record>
<txt-record>usb_MDL=HL-2040 series</txt-record>
<txt-record>note=Study</txt-record>
</service>
</service-group>
}}}
 * the {{{txt-record}}} items (except for {{{note}}}) are from OS X's HL-2040 PPD ({{{/private/etc/cups/ppd/HL_2040_series.ppd}}})
 * the printer will now show up in any Zeroconf client (tested with OS X 10.4.10)
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
=== Windows 2000/XP/Vista ===
The following instructions should work on all versions of windows from 2000 onwards, and have been tested in both Windows 2000 and Windows Vista.

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
Most printer drivers cannot access ink level information through the 910nd deamon, so you may not know, which cartridge to change. You can use the attached ink-4.1 package attachment:ink_0.4.1-1_mipsel.ipk to obtain the ink levels for most printers in OpenWrt (based on http://libinklevel.sourceforge.net/). If you want to display the inklevels in X-Wrt you may apply the following path to status-usb.sh:

{{{
...
end_form
EOF
?>
<?
usbpr=`ls //usb/lp* 2>//null`
if [ ! -z "$usbpr" ]; then
        inklevel_form=$(
        for p in $usbpr; do
                ink -d $p |  awk -v FS=":" '
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
<h3>@TR<<status_usb_Mounted_USB_SCSI#Mounted USB / SCSI ices>></h3>
<div>
...
}}}
= Troubleshooting =
 * Problem : the printer status shows "Attempting to connect to socket://<ip to router>:<listening port of router>" in the client CUPS interface (http://localhost:631) and nothing works (seen on ["OpenWrtDocs/Hardware/Asus/WL500GP"] / WhiteRussian RC6).
 * Solution : make sure you installed both USB 1.1 and USB 2.0 modules (see UsbStorageHowto).
= Not supported printers =
Here you should create a list of printers which are '''not''' working with the {{{p910nd}}} package. Please include manufacturer, model, interface (USB/Parport), driver working and some short comment.

The combination Windows 2000 with a canon pixma iP4000 seems not to work with bidirectional mode. If your printer dosent work, try disabling bidirectional mode.

Canon Pixma ip3000 and windows xp is not working in bidirectional mode. Disable bidirectional mode.

Please add not working combinations here.

Konica Minolta PagePro 1300W doesn't seem to work in bidirectional mode under win xp.

Canon i560 is not working in bidirectional mode. Remove the -b option on the router and disable bidirectional mode and the Canon Status Monitor in Windows. Make sure that the uhci kernel module is loaded since it seems to be usb 1.1.

Canon MP600 does not work in bidirectional mode on Windows XP using p910nd v0.7. Remove -b from line in /etc/defaults/p910nd and kill/restart the p910nd process. Uses the ehci-hcd module (USB 2.0).

= Links =
- http://etherboot.sourceforge.net/p910nd/ [[BR]]- http://wl500g.dyndns.org/printing/ [[BR]]- http://wl500g.dyndns.org/
