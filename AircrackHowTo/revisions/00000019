## ##############################################
## Tip: Please write the howto more generic because OpenWrt runs on
## more routers than just the WRT54G and use a linebreak on char 80 makes
## the page source a lot easier to read and editable.
##
## Again, thanks for your help!
'''Aircrack Quick Guide for the WRT54G/S'''

[[TableOfContents]]
= Introduction =
== What is Aircrack? ==
Aircrack is a suite of tools that enables wireless traffic monitoring and penetration/security testing. The official page for Aircrack is [http://www.aircrack-ng.org here].

= Requirements =
 * A WRT54G/S in client mode
 * aircrack package.
 * {{{wl}}} utility.
 * External storage.

1. The following packages and the packages they depend upon
1. ["OpenWrtDocs/WhiteRussian/ClientMode"]
1. ["OpenWrtDocs/Kamikaze/ClientMode"]
1. Please refer to the RemoteFileSystemHowTo for instructions on how to set this up
1. (i.e. an NFS drive, or a CIFS drive)


= Installation =
Aircrack can easily be installed using !OpenWrt backports repository.  See ["OpenWrtDocs/Packages"]
for how to configure your device to use the repository, then install aircrack by typing:

{{{
ipkg install aircrack-ng
}}}

If you have a [http://en.wikipedia.org/wiki/PRISM_%28chipset%29 PRISM] chipset, in order to capture traffic, you need {{{wl}}}. This can be installed by typing:

{{{
ipkg install wl}}}

Likewise, Atheros/MadWIFI users need wlanconfig.  This *should* be in either kmod-madwifi or wireless-tools.

= Configuring Your WRT54G/S to Monitor =
Now that Aircrack is installed and ready to start capturing traffic, you have to tell your router to listen to all traffic and not just traffic of its own.  This is called "monitor mode."  To be able to change channels and sniff on all channels, you must have the router in client mode: ClientModeHowto

Users with a Broadcom chipset need to use the {{{wl}}} utility:
{{{
wl monitor 1
ifup prism0}}}

Users with an Atheros chipset need to use {{wlanconfig}}:
{{{
wlanconfig ath1 create wlandev wifi0 wlanmode monitor}}

MadWIFI allows you you have virtual interfaces, provided they are on the same channel.  This is why ath1 is specified.  All Atheros chipset cards have a wifi<instance> device, and each device can have multiple ath devices.



= Start Capturing =
Begin by changing into the directory that you want to store the dump file in. This is most likely the directory that is either a CIFS or NFS mount. The dump files can get large, and to capture a useful amount of data you will need more storage than what comes stock on these routers. Another reason and advantage for storing the dump file on another computer is so the processing of the dumpfile can be done in parallel with capturing.

Once you are in the directory that you want to store the dump file in, run the following commands:

{{{
airodump prism0 test 0 1}}}

What the above command does is:

 * prism0 - Use device {{{prism0}}}
 * test - Output to the file {{{test.cap}}} (the {{{.cap}}} is added automatically)
 * 0 - Listen on all channels
 * 1 - Write only the IVs found and drop everything else

We want to only write the IVs found because they are the packets that can be used to crack the WEP encryption.

After the command is run the Aircrack program starts to display information about the surrounding networks to the user. The user will see the ESSIDs of the surrounding networks and how many packets those networks are sending.

During capture, the user can run the aircrack program on the {{{test.cap}}} file using the computer that is hosting the network storage. Using this method, both airodump and aircrack can be run in parallel, without interfering with eachother.

Once you have enough packets logged just hit {{{CTRL+C}}} to quit airodump.

= Airodump Usage =
{{{
usage: airodump <interface name or pcap filename> <output prefix> <channel> [IVs flag]}}}

Newer versions (like in the Kamikaze release) use a different syntax:
{{{  Airodump-ng 0.9 - (C) 2006,2007 Thomas d'Otreppe
  Original work: Christophe Devine
  http://www.aircrack-ng.org

  usage: airodump-ng <options> <interface>[,<interface>,...]

  Options:
      --ivs               : Save only captured IVs
      --gpsd              : Use GPSd
      --write    <prefix> : Dump file prefix
      -w                  : same as --write
      --beacons           : Record all beacons in dump file
      --update     <secs> : Display update delay in seconds

  Filter options:
      --encrypt   <suite> : Filter APs by cypher suite
      --netmask <netmask> : Filter APs by mask
      --bssid     <bssid> : Filter APs by BSSID
      -a                  : Filter unassociated clients

  By default, airodump-ng hop on 2.4Ghz channels.
  You can make it capture on other/specific channel(s) by using:
      --channel <channels>: Capture on specific channels
      --band <abg>        : Band on which airodump-ng should hop
      --cswitch  <method> : Set channel switching method
                    0     : FIFO (default)
                    1     : Round Robin
                    2     : Hop on last
      -s                  : same as --cswitch

      --help              : Displays this usage screen
}}}
= Links =
 * If you get stuck on something, there are lots of good resources at the official aircrack [http://www.aircrack-ng.org website]
 * Aircrack discussion forums are [http://tinyshell.be/aircrackng/forum/ here]
 * You can also join the channel #aircrack-ng on Freenode IRC (irc.freenode.net)
