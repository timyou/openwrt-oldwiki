= Kismet with OpenWRT on a Linksys WRT54 =
== Introduction ==
'''Kismet '''can be used to find and analyze wireless networks. Per default, it puts the network card into promiscuous mode so it can see all packets the network card receives. Packets are saved in a dump file and can then be analyzed with a tool like Wireshark which is available for Linux, many Unix derivates, and Windows. On Windows, Wireshark can't be used to capture 802.11 frames as Windows drivers only forward 802.3 pseudo frames instead of the real 802.11 frames. Also, it is not possible to see 802.11 management frames. Other programs such as Airopeek for Windows do exist which bring their own drivers. Unfortunately, they are very expensive. Kismet on a Linksys router is an interesting alternative.

More info on Kismet in general can be found[http://www.kismetwireless.net/documentation.shtml here].

== Installation ==
I'''nstalling Kismet on OpenWRT is quite simple:'''

 * Ensure the router running OpenWRT is connected to the Internet. Verify by pinging a host on the Internet from a telnet/ssh session (e.g. ping www.google.com)
 * If not already done update the installable package library on the router by typeing ''''ipkg update''''
 * Next, install the kismet server by executing the following command: ''''ipkg install kismet-server''''. This program collects the wireless lan packets.
 * Afterwards, install the kismet client on the router with the follwong command: ''''ipkg install kismet-client''''
That's most there is to it except for one thing: Kismet dumps all packets it receives from the network card of the router into a file in the directory in which it is executed (see below). As there is not much space on the router itself, you might want to install a CIFS driver on the router to access a share on your Windows computer. For details of how to install the CIFS driver and how to mount a Windows share on the router take a look at section 2 of the RemoteFileSystemHowTo.

== Operation ==
To run Kismet on the router



Useful tips
