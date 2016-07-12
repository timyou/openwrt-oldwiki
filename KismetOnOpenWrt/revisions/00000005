= Kismet with OpenWRT on a Linksys WRT54 =
== Introduction ==
'''Kismet '''can be used to find and analyze wireless networks. Per default, it puts the network card into promiscuous mode so it can see all packets the network card receives. Packets are saved in a dump file and can then be analyzed with a tool like [http://www.wireshark.org/ Wireshark ]which is available for Linux, many Unix derivates, and Windows. On Windows, Wireshark can't be used to capture 802.11 frames as Windows drivers only forward 802.3 pseudo frames instead of the real 802.11 frames. Also, it is not possible to see 802.11 management frames. Other programs such as Airopeek for Windows do exist which bring their own drivers. Unfortunately, they are very expensive. Kismet on a Linksys router is an interesting alternative.

More info on Kismet in general can be found[http://www.kismetwireless.net/documentation.shtml here].

== Installation ==
I'''nstalling Kismet on OpenWRT is quite simple:'''

 * Ensure the router running OpenWRT is connected to the Internet. Verify by pinging a host on the Internet from a telnet/ssh session (e.g. ping www.google.com)
 * If not already done update the installable package library on the router by typing ''''ipkg update''''
 * Next, install the kismet server by executing the following command: ''''ipkg install kismet-server''''. This program collects the wireless lan packets.
 * Afterwards, install the kismet client on the router with the follwing command: ''''ipkg install kismet-client''''
That's most there is to it except for one thing: Kismet dumps all packets it receives from the network card of the router into a file in the directory in which it is executed (see below). As there is not much space on the router itself, you might want to install a CIFS driver on the router to access a share on your Windows computer. For details of how to install the CIFS driver and how to mount a Windows share on the router take a look at section 2 of the RemoteFileSystemHowTo.

== Operation ==
To run Kismet on the router change to the directory in which the files Kismet creates should be stored. An ideal directory to start from is a drive mounted from the PC (cp. installing a CIFS driver to mount Windows shares on the router, see above). In the directory, type 'kismet_server' (note the UNDERLINE). That's it. Here's how the output looks like when the kismet server is started:

attachment:kismet-server.gif

To get an overview what the Kismet server has found, open another telnet/ssh window, connect to the router and execute 'kismet_client' (note the UNDERLINE again) in any directory. A semi-graphical display will then show the networks found and lots of other info. Hit the 'h' (help key) to see how to branch into sub-windows of the kismet client to get even more info. Here's a picture of how the kismet client looks like:

attachment:kismet-client.gif

To stop the kismet server, press CTRL-C in the ssh window in which the server is executed. This stops the server and closes all files kismet stores information in about the current tracing session. For network analysis the .dump file is probably the most interesting file. Rename the file into .pcap and it can be used immediately with Wireshark.

== Useful tips ==
 * '''Configuration file''': The kismet server configuration file can be found in /etc/kismet.
 * '''Toggle Packet Dumping to a File: '''In the config file a number of things can be changed. To just get an overview of networks on the air it might be a good idea not to create .dump file as they grow big quite quickly. This can be done by changing the config file accordingly.
 * '''Limits of the Config File: '''Some options in the config file don't seem to work in the kismet port of OpenWRT: hoping/no hopping selection does not work.
 * '''To scan on all channels: G'''o to the web configuration interface of the router and change from Access Point mode to Client mode. This will activate hopping for Kismet, although most of the time the router will stay on the frequency selected for the client mode. Nevertheless the router will pick up all network on all channels quite quickly.
 * '''To use Kismet on one channel only:''' Set the router into Access Point mode, e.g. via the web interface, and start the server again. Even though hoping is selected in the config file, Kismet will nevertheless only stay on the channel selected in the web interface of the router.
